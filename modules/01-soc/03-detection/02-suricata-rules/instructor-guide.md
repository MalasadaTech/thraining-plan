# Instructor Guide – Module 1.3.2 – Suricata Rules

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.2.1 A / B / C · 1.3.2.2 2b / 3c / 4c · 1.3.2.3 1a / 2b / 3c  
- Hunter: 1.3.2.1 B / C / C · 1.3.2.2 2b / 3c / 4c · 1.3.2.3 2b / 3c / 4c  
- CTI: 1.3.2.1 A / B / B · 1.3.2.2 1a / 2b / 3c · 1.3.2.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read a Suricata **alert** rule, describe the match, relate it to Zeek, and propose a basic signature. No sensor admin. No exploit payloads.

**Key Teaching Points:**
- Action + header + options.
- Buffers (`http.*`, `tls.*`) beat raw `content` on `tcp any any`.
- ASCII / hex / regex — one of each, then stop.
- Suricata ≠ Zeek. Same session, different job.
- SOC create **1a / 2b / 3c**. Training SIDs ≥ 1000000.

**Common Student Challenges:**
- `content:"GET"` on all TCP.
- Putting Zeek field names in the rule.
- Asking how to reload Suricata or write `drop`.
- Pasting hex they cannot explain.
- Opening **1.4** PCAP class.
- Grading SOC 3 as signature engineer.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard: header vs options vs Zeek `http` row
- Answer key (this guide)

---

## Learning Objectives

1. Explain action, header, options.
2. Read `content`, `http.*`, `tls.*`, and ASCII/hex/regex.
3. Relate a hit to Zeek logs.
4. Analyze an existing rule.
5. Create or modify a basic rule (propose only).

**Mapped Items:**
- K: 1.3.2.1 – Suricata rules
- T: 1.3.2.2 – Analyze an existing Suricata rule
- T: 1.3.2.3 – Create or modify a basic Suricata rule

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | alert only |
| Structure                      | 10 min   | action / header / options |
| Options, matching, Zeek        | 14 min   | b–d |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~70 min** | Stretch Example 2 if they defend any-GET |

---

## Detailed Teaching Notes

### 1. Structure

**Talking Points:**
- Same 3/5/7 split as SIGMA. CTI create is 1a / 1a / 2b.
- Draw `alert http HOME any -> EXT any ( ... )` and label the three parts.
- `$HOME_NET` is local policy. Do not invent the site’s CIDRs.

**Question to ask:**  
“What protocol and direction does this even inspect?”

### 2. Options, matching, Zeek

**Talking Points:**
- Walk b–d. Sticky buffer: set `http.uri` then `content`.
- Hex: `4D 5A` = MZ only. No shellcode.
- Regex: one `pcre` example. Over-match risk.
- Zeek pivot: time + 5-tuple → `http`/`ssl`/`conn`. No `uid` in the signature.

**Question to ask:**  
“If Suricata fires and Zeek has no `http` row, what do you still have?”

### 3. Examples

**Example 1:** Good URI GET. Tie to 1.2.5 Ex 3.  
**Example 2:** Raw GET. Tear it down.  
**Example 3:** UA regex — better buffer, still needs scope.

---

## Hands-On Exercise – Instructor Guidance

**How to run:** 14–16 minutes. Fail exploit hex. Fail `drop`. Fail Zeek field names in the rule.

**Summaries:**
- Example 1: GET `/payload/update.exe` outbound HTTP; useful; expected as a rule.
- Example 2: ASCII `GET` on any TCP; too broad; lead.
- Example 3: PowerShell UA regex on `http.user_agent`; better; still needs scope; lead if shipped raw.

**Beacon POST analysis:**  
`alert` + `http` + HOME→EXT. Options: flow to_server, method POST, URI `/api/v1/beacon`. Fires on the 1.2.5 Ex 2 path. Does not inspect UA.

**Create / modify (equivalent is fine):**

```
alert http $HOME_NET any -> $EXTERNAL_NET any (
  msg:"BUILDINGC TRAIN GET exe URI";
  flow:established,to_server;
  http.method; content:"GET";
  http.uri; content:".exe";
  sid:1000010; rev:1;)
```

A fix of Example 2 that adds `http` + `http.method` + a URI also passes.

**Zeek confirm:** Search `http` for that time window, `id.orig_h`, `id.resp_h`, matching `method`/`uri`. Then `uid` → `conn`.

SOC 3 pass: names action, proto, one content, sid. SOC 5: buffers + flow.

---

## Knowledge Check – Answer Key

1. **Three parts?**  
   **Answer:** Action (`alert`), header (proto, addresses, ports, direction), options (`msg`, `sid`, match keywords).  
   **Explanation:** Outline a.

2. **Why HTTP buffers?**  
   **Answer:** They bind `content` to the URI / UA / method, not arbitrary TCP bytes. Raw `content:"GET"` over-matches.  
   **Explanation:** Outline b.

3. **ASCII / hex / regex?**  
   **Answer:** ASCII = readable string (`/payload/update.exe`). Hex = raw bytes (`|4d 5a|` for MZ). Regex = `pcre` when the string varies. Choose the simplest that is specific.  
   **Explanation:** Outline c.

4. **Relate to Zeek?**  
   **Answer:** Same session can have a signature hit *and* an `http`/`ssl`/`conn` row. Pivot on time + 5-tuple; use Zeek `uid` on the Zeek side. Suricata does not replace Zeek.  
   **Explanation:** Outline d.

5. **Who deploys? SOC ceiling?**  
   **Answer:** Detection Engineering deploys. SOC proposes a basic rule (1a / 2b / 3c).  
   **Explanation:** Matrix.

---

## Additional Instructor Resources

- Local `$HOME_NET` definition if you can show it
- Next recommended module: 1.3.3 YARA rules
