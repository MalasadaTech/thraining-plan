# Module 3.6.1 – Advanced DNS Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.6.1 – Advanced DNS  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Interpret SOA. Stack NS/MX/TXT/SRV. Overlay a live dig if you can.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Interpret an SOA
2. NS / MX / TXT / SRV intel value
3. Enrich and pivot from that stack

**Mapped Items:**  
K: 3.6.1 | T: 3.6.1.1

**Speaker Notes:**  
Hunter K is B/C/C. CTI task is 3c / 4d.

---

### Slide 3 – Agenda
**Title:** Agenda

- SOA + other types
- Three examples
- Interpret + four pivots
- Knowledge check

**Speaker Notes:**  
3.7 is next cluster.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Zeek `query` / DGA / tunnel (**1.2.3**)  
RDAP created / registrar (**3.5**)  
Historical A (**3.3.2** Silent Push)

**Key Point:** Zone records *now*. Then pivot.

**Speaker Notes:**  
Fence.

---

### Slide 5 – SOA Fields
**Title:** Start of Authority

**MNAME** — primary NS  
**RNAME** — admin (`dot` → `@`)  
**Serial** — zone version, **not** a hash  
Timers — defaults; weak cluster only

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Other Types
**Title:** Classroom Set

**NS** — who serves the zone  
**MX** — mail path (none is OK)  
**TXT** — SPF / unique token  
**SRV** — service locator  

A/AAAA are assumed. Not this unit.

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Stack
**Title:** How You Analyze

Same **MNAME + NS** (+ unique TXT) → cluster.  
Not a registrant. Not a country.

**Speaker Notes:**  
Outline c.

---

### Slide 8 – Two Lines
**Title:** Interpret · Pivot

`MNAME | RNAME | serial meaning | pivot | do not claim`  
`records | pivot | still unknown`

**Speaker Notes:**  
Task.

---

### Slide 9 – Example 1: Card
**Title:** Example 1 – Night Owl Zone

`ns1.cdn-test.net` / hostmaster@…  
Serial 2026080101 = zone rev.  
Pivot other names on that NS.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Serial
**Title:** Example 2 – Not a Hash

`2026080101` is not SHA256.  
Do not family-match on it.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: A Only
**Title:** Example 3 – Wrong Unit

A `203.0.113.88` is **1.2.3**.  
Come back with SOA/NS/TXT.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Serial as hash / WHOIS date  
- A-record-only  
- Cluster on generic SPF  
- RDAP or PDNS this hour  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use site `dig` / DNS tool if posted.  
Keep: SOA fields + stack to pivot.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. Interpret the Night Owl SOA.
3. A–D: pivot lines.
4. No RDAP. No Silent Push.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. MNAME, RNAME — serial is not?
2. Two other types — one use each?
3. Same operator vs weak?
4. Why not A-only?
5. Registration vs historical A — where?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Interpret SOA. Stack NS/MX/TXT/SRV.
- Next cluster: **3.7** frameworks.

**Speaker Notes:**  
Do not open 3.7 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Advanced DNS — Quick Reference

| Record | Pivot |
|--------|-------|
| SOA MNAME/RNAME | Same zone operator |
| NS | Shared nameservers |
| TXT unique | Search the token |
| MX / SRV | Mail / service infra |

**Coming next:** Module 3.7.1 – ATT&CK for intelligence

**Footer:** SOC / Hunter / CTI Training Program
