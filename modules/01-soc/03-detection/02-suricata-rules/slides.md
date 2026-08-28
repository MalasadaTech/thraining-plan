# Module 1.3.2 – Suricata Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.3.2 – Suricata Rules  
**Subtitle:** What on the wire would fire  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is the network signature. Read a Suricata rule and propose a basic one. It is not how detections run as a service, and it is not YARA.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read a **network signature** to see what on the wire would fire.

An alert names a rule. Say what it matches, and whether the match is specific.

You **propose** a basic create or modify. You do **not** deploy it.

**Speaker Notes:**  
This slide is the student intro. Name the parts of a Suricata rule and read one example. Do not teach YARA or how detections run as a service.

---

### Slide 3 – Action, header, options
**Title:** Action, header, options

`alert proto src port -> dst port ( options )`

**Action** — `alert` in this lesson. Not drop.  
**Header** — protocol, addresses, ports, direction.  
**Options** — `msg`, `sid`, `rev`, and the match keywords.

`$HOME_NET` and `$EXTERNAL_NET` are site variables. Do not invent the range.

**Speaker Notes:**  
Walk the three parts. Stop on action: this lesson is alert only. If they ask for the address range, it is a site variable.

---

### Slide 4 – Buffers, ASCII, hex, regex
**Title:** Buffers, ASCII, hex, regex

Put **`content`** in the right buffer: `http.uri`, `http.method`, `tls.sni`.

**ASCII** — `/update.exe`.  
**Hex** — `|4d 5a|` (`MZ`).  
**Regex** — `pcre`. Easy to over-match.

Do not paste exploit payloads.

**Speaker Notes:**  
A string in the wrong buffer is a different match. Hex is the MZ bytes only. Regex can over-match. Do not start an exploit-payload example.

---

### Slide 5 – Same session, different job
**Title:** Same session, different job

**Suricata** — this signature matched.  
**Zeek** — parsed fields (method, URI, who talked).

Join them with time plus the **5-tuple** (source IP, source port, destination IP, destination port, protocol).

Do not put Zeek field names in the Suricata rule.

**Speaker Notes:**  
Both can come from the same traffic. They are not two incidents. If they write `uri` into the rule, that is a Zeek field, not a Suricata buffer.

---

### Slide 6 – Read it. Propose a basic one.
**Title:** Read it. Propose a basic one.

**Given:** `alert http`, GET, `http.uri` `/update.exe`.

**Detects:** outbound HTTP GET whose URI contains `/update.exe`.

`content:"GET"` on `tcp any any` is too broad.

SOC proposes. Detection Engineering reviews.

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: outbound GET of `/update.exe`. Tightening any GET by adding the URI is a modify. Do not tell the intro plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Suricata and Zeek do the same job on a session. True or false?  
2. The given rule — what does it detect, in one sentence?  
3. Why is `content:"GET"` on `tcp any any` a poor proposal?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Action, header, and options.  
Put the match in the right buffer.  
ASCII, hex, and regex are techniques.  
Zeek tells you the session. You propose. You do not deploy.

**Next:** **1.3.3** YARA rules

**Speaker Notes:**  
1.3.3 is files and memory. Stay off this network signature when you get there.
