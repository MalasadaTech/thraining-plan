# Module 1.3.2 – Suricata Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.2.1 A / B / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 1a / 2b / 3c  
- Hunter: 1.3.2.1 B / C / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 2b / 3c / 4c  
- CTI: 1.3.2.1 A / B / B ; 1.3.2.2 1a / 2b / 3c ; 1.3.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name action, header, and options, and how a Suricata hit relates to a Zeek row.
2. Read an existing rule and say what it detects; propose a **basic** create or modify.

**Mapped Proficiency Items:**
- K: 1.3.2.1 – Suricata rules
- T: 1.3.2.2 – Analyze an existing Suricata rule and describe what it detects
- T: 1.3.2.3 – Create or modify a basic Suricata rule

---

## 1. Key Concepts

SOC analysts **read** a network signature and **propose** a basic one. **1.3.1** was SIGMA (host YAML). This hour is Suricata. You do **not** deploy it. How detections run as a service is **4.x**.

**Suricata** inspects packets / streams and can **alert**. This lesson uses `alert` only.

```
alert proto src_ip src_port -> dst_ip dst_port ( options )
```

| Idea | What to read |
|------|----------------|
| **Action, header, options** | Action = `alert`. Header = proto, addresses, ports, `->`. Options = `msg`, `sid`, `rev`, and the match keywords |
| **Common options** | `content:"..."`. HTTP buffers: `http.uri`, `http.method`, `http.user_agent`. TLS: `tls.sni` (same *idea* as Zeek `server_name`). `flow:established,to_server` |
| **ASCII / hex / regex** | ASCII = `content:"/update.exe"`. Hex = `content:"\|4d 5a\|"` (`MZ`). Regex = `pcre:"/update\\.(exe\|dll)/i"`. Do not paste exploit payloads |
| **Vs Zeek** | Same session can make a Suricata hit **and** a Zeek `http` / `ssl` / `conn` row. Suricata = signature matched. Zeek = parsed fields. Pivot with time + 5-tuple. Do not put Zeek field names in the rule |

**What good looks like:**

- Analyze: name action, header, options, and what would fire. A raw `content:"GET"` on `tcp any any` is too broad.
- Given:

```
alert http $HOME_NET any -> $EXTERNAL_NET any (
  msg:"GET /update.exe";
  flow:established,to_server;
  http.method; content:"GET";
  http.uri; content:"/update.exe";
  sid:1000001; rev:1;)
```

**What it detects:** outbound HTTP GET whose URI contains `/update.exe`. Same object as **1.2.5**. A matching session should have a Zeek `http` row.

- Modify / create: a **basic** `alert` with header, `msg`, `sid`, `rev`, and one specific `content` in the right buffer. Tightening “any GET” by adding `http.uri` is a modify. SOC **proposes**. DE reviews.

---

## 2. Knowledge Check

1. A Suricata rule is action, header, and options. True or false?
2. The given rule above — what does it detect, in one sentence?
3. Why is `content:"GET"` on `tcp any any` a poor proposal?

---

## 3. Summary

Suricata is action + header + options. Put the match in the right buffer. ASCII, hex, and regex are techniques. Zeek tells you the session. You propose. You do not deploy.

**Next:** **1.3.3** YARA rules.

---

## 4. Related modules

- 1.3.1 – SIGMA rules (previous)
- 1.2.5 – HTTP engine
- 1.3.3 – YARA rules
- 4.x – How detections run as a service
