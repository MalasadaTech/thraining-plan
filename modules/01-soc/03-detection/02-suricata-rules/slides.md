# Module 1.3.2 – Suricata Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.3.2 – Suricata Rules  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Network signature. Propose, do not deploy. Alert only.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts **read** a network signature and **propose** a basic one.

You do **not** deploy it. That is **4.x**.

**Speaker Notes:**  
1.3.1 was YAML. This is packets/streams.

---

### Slide 3 – Structure
**Title:** Action, header, options

`alert proto src port -> dst port ( options )`

**Action** — `alert` this hour.  
**Header** — who/what it looks at.  
**Options** — `msg`, `sid`, `rev`, match keywords.

**Speaker Notes:**  
Outline a. HOME_NET is a site variable — do not invent the range.

---

### Slide 4 – Options and matching
**Title:** Buffers, ASCII, hex, regex

**`content`** in the right buffer: `http.uri`, `http.method`, `tls.sni`.

**ASCII** — `/update.exe`.  
**Hex** — `|4d 5a|` (`MZ`).  
**Regex** — `pcre`. Easy to over-match.

**Speaker Notes:**  
Outline b–c. No exploit payloads.

---

### Slide 5 – Vs Zeek
**Title:** Same session, different job

Suricata — this signature matched.  
Zeek — parsed fields (`method`, `uri`, `uid`).

Pivot with time + 5-tuple.  
Do not put Zeek field names in the rule.

**Speaker Notes:**  
Outline d.

---

### Slide 6 – What good looks like
**Title:** Read it. Propose a basic one.

**Given:** `alert http`, GET, `http.uri` `/update.exe`.

**Detects:** outbound GET of `/update.exe`. Same object as **1.2.5**.

`content:"GET"` on `tcp any any` is too broad.

**Speaker Notes:**  
Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A Suricata rule is action, header, and options. True or false?  
2. The given rule — what does it detect, in one sentence?  
3. Why is `content:"GET"` on `tcp any any` a poor proposal?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Action + header + options.  
Right buffer. ASCII / hex / regex.  
Zeek tells you the session.  
You propose. You do not deploy.

**Next:** **1.3.3** YARA rules

**Speaker Notes:**  
Files and memory next.
