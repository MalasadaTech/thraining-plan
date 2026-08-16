# Module 1.3.2 – Suricata Rules

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.2.1 A / B / C · 1.3.2.2 2b / 3c / 4c · 1.3.2.3 1a / 2b / 3c  
- Hunter: 1.3.2.1 B / C / C · 1.3.2.2 2b / 3c / 4c · 1.3.2.3 2b / 3c / 4c  
- CTI: 1.3.2.1 A / B / B · 1.3.2.2 1a / 2b / 3c · 1.3.2.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain Suricata rule structure: action, header, and options.
2. Read common options (`content`, `http.*`, `tls.*`) and matching techniques (ASCII, hex, regex).
3. Say how a Suricata rule relates to Zeek / network logs (same session, different job).
4. Analyze an existing Suricata rule and state what it detects.
5. Create or modify a **basic** Suricata rule (propose only).

**Mapped Proficiency Items:**
- K: 1.3.2.1 – Suricata rules
- T: 1.3.2.2 – Analyze an existing Suricata rule and describe what it detects
- T: 1.3.2.3 – Create or modify a basic Suricata rule

---

## 1. Key Concepts

### 1.1 Structure: action, header, options

**Suricata** inspects packets / streams and can **alert** (or drop, in IPS mode). This lesson is **alert** rules you can read and propose. You do not deploy signatures or run the sensor.

```
alert proto src_ip src_port -> dst_ip dst_port ( options )
```

| Part | What to read | Why it matters |
|------|----------------|----------------|
| **Action** | `alert` (this course) | `drop` / `pass` / `reject` are policy. Park them. |
| **Header** | `proto`, addresses, ports, direction `->` | Who/what it looks at. `$HOME_NET` / `$EXTERNAL_NET` are site variables. |
| **Options** | `msg`, `sid`, `rev`, match keywords | What must be true, and how you name the hit |

**Minimum options you always name:** `msg` (what the analyst sees), `sid` (unique id), `rev` (version). Training SIDs in class use the 1,000,000+ range unless your site says otherwise.

| This lesson | Later / other |
|-------------|---------------|
| Signature text | Alert triage / PCAP — **1.4** |
| `http.*` / `tls.*` buffers | Zeek field analysis — **1.2** |
| Propose a basic rule | Sensor/rule-set admin |

### 1.2 Options, matching, and Zeek

**Common options (outline b)**

| Option | Role |
|--------|------|
| `content:"..."` | Byte/string match (ASCII unless `|hh|` hex) |
| `http.uri` / `http.method` / `http.user_agent` | Sticky **HTTP** buffers (after you set the buffer, `content` applies there) |
| `tls.sni` (or site-equivalent TLS buffer) | Hostname the client requested — same *idea* as Zeek `server_name` |
| `flow:established,to_server` | Direction / state so you do not match every packet |
| `pcre:"/regex/"` | Regex (use when ASCII/hex is not enough) |
| `classtype:` | Category hint |

**Matching techniques (outline c)**

| Technique | Looks like | Use |
|-----------|------------|-----|
| **ASCII** | `content:"/payload/update.exe"` | Readable strings |
| **Hex** | `content:"\|4d 5a\|"` | Raw bytes (here: `MZ`). Do not paste exploit payloads. |
| **Regex** | `pcre:"/update\\.(exe\|dll)/i"` | Variation. Easy to over-match. |

**How Suricata relates to Zeek (outline d):**  
Same conversation can produce a **Suricata alert** *and* a Zeek `http` / `ssl` / `conn` row. Suricata says “this signature matched.” Zeek says “here are the parsed fields” (`method`, `host`, `uri`, `uid`). You **pivot** with time + 5-tuple (and `uid` on the Zeek side). You do not put Zeek field names inside a Suricata rule.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| `alert http` + `http.uri` + a specific path + `flow:to_server` | `content:"GET"` on `tcp any any -> any any` with no buffer |
| One `sid`, clear `msg` | Copied sid, or `msg` that does not match the content |
| ASCII URI you can explain | Hex blob you cannot read and did not justify |
| Aligns with a Zeek `http` story | “Suricata replaces Zeek” |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Useful HTTP URI Rule (Expected)

```
alert http $HOME_NET any -> $EXTERNAL_NET any (
  msg:"BUILDINGC TRAIN GET /payload/update.exe";
  flow:established,to_server;
  http.method; content:"GET";
  http.uri; content:"/payload/update.exe";
  classtype:trojan-activity;
  sid:1000001; rev:1;)
```

**What it detects:** Outbound HTTP **GET** whose URI contains `/payload/update.exe`. Same object as **1.2.5** Example 3.

**Zeek relation:** A matching session should have an `http` row (`method=GET`, `uri` with that path). Copy time + orig/resp and search Zeek. Do not expect a `uid` *inside* the signature.

**Interpretation:** Expected *as a rule*: proto, direction, HTTP buffers, specific URI.

### Example 2: No Buffer, Any GET (Lead)

```
alert tcp any any -> any any (
  msg:"GET";
  content:"GET";
  sid:1000002; rev:1;)
```

**What it detects:** The three ASCII bytes `GET` anywhere in any TCP session — web, binary blobs, pipelined noise.

**Interpretation:** Lead **about the rule**. Missing `http` proto, missing `http.method` buffer, missing direction, missing specificity. Modify before you propose it.

### Example 3: User-Agent + Regex (Lead if Unscoped)

```
alert http $HOME_NET any -> $EXTERNAL_NET any (
  msg:"BUILDINGC TRAIN PowerShell User-Agent";
  flow:established,to_server;
  http.user_agent; pcre:"/[Pp]ower[Ss]hell/";
  sid:1000003; rev:1;)
```

**What it detects:** Outbound HTTP whose User-Agent matches that regex — the **1.2.5** Example 2 beacon UA would hit. So would some admin tools.

**Interpretation:** Better than Example 2 (right buffer). Still a lead if you ship it with no host/URI/scope. Name `pcre` as regex. A tighter proposal would add `http.uri` or a dest group. Hex is not required here; ASCII `content:"WindowsPowerShell"` would also work.

---

## 3. Hands-On Exercise

**Objective:** Practice reading Suricata and proposing a basic rule.

**Instructions:**

1. Summarize each example: what it matches, expected vs lead (as a *rule*).
2. **Analyze** this rule. Action, header, options, what fires:

```
alert http $HOME_NET any -> $EXTERNAL_NET any (
  msg:"BUILDINGC TRAIN POST beacon path";
  flow:established,to_server;
  http.method; content:"POST";
  http.uri; content:"/api/v1/beacon";
  sid:1000004; rev:1;)
```

3. **Modify** Example 2 **or create** a basic `alert http` rule for outbound GET of `.exe` on the URI (ASCII `content` + `http.uri`). Include `msg`, `sid`, `rev`, and `flow`.
4. In two sentences, say how you would confirm a hit with **Zeek** (`http` / `conn`). Do not write a Zeek script. Do not deploy Suricata.

**Expected Outcome:**
- Three summaries
- One analysis that names action + header + options
- One basic rule (create or modify)
- One Zeek confirmation path

---

## 4. Knowledge Check

1. What are the three parts of a Suricata rule (action, header, options)?
2. Why do `http.uri` / `http.user_agent` matter compared with a raw `content` on `tcp any any`?
3. Give one ASCII, one hex, and one regex (`pcre`) example — and when you would choose each.
4. How does a Suricata hit relate to a Zeek `http` or `ssl` row?
5. Who deploys the rule in this program, and what is SOC’s create ceiling?

---

## 5. Summary

- Suricata rule = action + header + options (`msg`, `sid`, match keywords).
- Put HTTP/TLS matches in the right **buffer**. ASCII / hex / regex are techniques, not three products.
- Suricata = signature match. Zeek = parsed session. Pivot with time + 5-tuple.
- SOC proposes (1a / 2b / 3c). Next: YARA (**1.3.3**). Alerts/PCAP are **1.4**.

---

## 6. References & Further Reading

- Suricata rule format documentation — as used in class
- Related modules:
  - 1.2.4 – TLS engine
  - 1.2.5 – HTTP engine
  - 1.3.1 – SIGMA rules (previous)
  - 1.3.3 – YARA rules (next)
  - 1.4.1 – Alert context and investigation
