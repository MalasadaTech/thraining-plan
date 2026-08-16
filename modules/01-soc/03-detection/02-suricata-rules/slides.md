# Module 1.3.2 – Suricata Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.3.2 – Suricata Rules  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Alert rules only. No drop. No exploit hex. Propose, don’t deploy.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Explain action, header, options
2. Read `content`, `http.*`, `tls.*`, and ASCII / hex / regex
3. Relate a hit to Zeek logs
4. Analyze an existing rule
5. Create or modify a *basic* rule

**Mapped Items:**  
K: 1.3.2.1 | T: 1.3.2.2 | T: 1.3.2.3

**Speaker Notes:**  
SOC create is 1a/2b/3c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Structure
- Options and matching
- Suricata vs Zeek
- Three worked examples
- Analyze + create/modify
- Knowledge check

**Speaker Notes:**  
1.4 PCAP is later.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

`drop` / IPS policy  
Reloading the sensor  
Exploit or shellcode hex  
Zeek scripts  
Alert playbooks (**1.4**)

**Key Point:** Read the signature. Propose a basic `alert`.

**Speaker Notes:**  
Park admin.

---

### Slide 5 – Structure
**Title:** Action, Header, Options

`alert proto src port -> dst port ( options )`

**action** — `alert` in this course  
**header** — who / proto / direction  
**options** — `msg`, `sid`, `rev`, match keywords  

**Speaker Notes:**  
Outline a. Label a live line.

---

### Slide 6 – Options
**Title:** content, http.*, tls.*

`content:"..."` — the bytes  
`http.uri` / `http.method` / `http.user_agent` — HTTP buffers  
`tls.sni` — same *idea* as Zeek `server_name`  
`flow:established,to_server` — direction  

**Analyst Tip:** Set the buffer, then `content`.

**Speaker Notes:**  
Outline b.

---

### Slide 7 – ASCII, Hex, Regex
**Title:** Three Matching Techniques

| Kind | Example |
|------|---------|
| ASCII | `content:"/payload/update.exe"` |
| Hex | `content:"\|4d 5a\|"` (MZ only) |
| Regex | `pcre:"/update\\.(exe\|dll)/i"` |

Pick the simplest specific match. No unexplained hex.

**Speaker Notes:**  
Outline c.

---

### Slide 8 – Suricata and Zeek
**Title:** Same Session, Different Job

**Suricata** — this signature matched  
**Zeek** — parsed `http` / `ssl` / `conn` fields  

Pivot: time + 5-tuple → Zeek. Then `uid` on the Zeek side.  
Do not put Zeek field names in the rule.

**Speaker Notes:**  
Outline d.

---

### Slide 9 – Example 1: URI GET
**Title:** Example 1 – /payload/update.exe

- `alert http` HOME → EXT
- `http.method` GET + `http.uri` path

**Interpretation:**  
Useful. Expected *as a rule*. Ties to 1.2.5 Ex 3.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Raw GET
**Title:** Example 2 – content GET on any TCP

- `alert tcp any any -> any any`
- `content:"GET"`

**Interpretation:**  
Lead about the rule. Too broad.

**Speaker Notes:**  
Ask what to add.

---

### Slide 11 – Example 3: UA Regex
**Title:** Example 3 – PowerShell User-Agent

- Right buffer: `http.user_agent`
- `pcre` for PowerShell
- No URI / dest scope

**Interpretation:**  
Better. Still tighten before you propose.

**Speaker Notes:**  
ASCII content would also work.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Any-TCP `GET`  
- Zeek `uri` inside Suricata  
- Unexplained hex  
- Asking to deploy / drop  
- Opening PCAP class  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Proposal Ideas
**Title:** Useful Starting Points

- Outbound GET of `.exe` on `http.uri`  
- POST `/api/v1/beacon`  
- PowerShell UA **plus** a URI or dest group  
- Always: proto + buffer + sid/msg/rev  

**Speaker Notes:**  
Local HOME_NET later.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize each example.
2. Analyze the POST `/api/v1/beacon` rule.
3. Modify Example 2 **or** create GET `.exe` on `http.uri`.
4. How would you confirm with Zeek?

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Action, header, options?
2. Why HTTP buffers vs raw TCP content?
3. ASCII vs hex vs regex — one example each?
4. How does a hit relate to Zeek?
5. Who deploys? SOC create ceiling?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Action + header + options.
- Buffer your `content`. ASCII / hex / regex.
- Suricata matches; Zeek parses. Pivot 5-tuple.
- Propose only. Next: YARA (**1.3.3**).

**Speaker Notes:**  
Do not open a YARA lab unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Suricata — Quick Reference

| Need | Look at |
|------|---------|
| Who | header + `flow` |
| HTTP | `http.uri` / `method` / `user_agent` |
| Bytes | `content` ASCII or `\|hh\|` |
| Variation | `pcre` |
| Confirm | Zeek `http`/`ssl`/`conn` |

**Coming next:** Module 1.3.3 – YARA rules

**Footer:** SOC / Hunter / CTI Training Program
