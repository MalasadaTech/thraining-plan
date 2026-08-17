# Module 2.7.4 – Defender’s ThreatMesh Framework  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.7.4 – DTF  
**Subtitle:** CTI Analyst (Hunter / SOC sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Discovery only. Real PTA/P. No score. No invented P-codes.

---

### Slide 2 – What this hour is
**Title:** What this hour is

From a **known-bad seed**, pick a pivot.

Cite the characteristic. Name candidate infra.  
Name the **next lookup**.

**Speaker Notes:**  
Not ATT&CK. Not a hop sentence without IDs.

---

### Slide 3 – Four tactics
**Title:** PTA0001–0004

**PTA0001** Domain · **PTA0002** IP · **PTA0003** SSL · **PTA0004** Application  

Pivots nest: `P0101.010` Name Server.

**Speaker Notes:**  
Outline a–b. Official IDs only.

---

### Slide 4 – What good looks like
**Title:** Take vs reject

**Take** — same NS (`P0101.010`) or same A (`P0103.003`) → `login-prd.net`.  
**Reject** — whole `203.0.113.0/24` (`P0202`). Shared cloud.

Next lookup = RDAP / SOA / PDNS — **name** it.

**Speaker Notes:**  
Tasks 1–2. Do not re-teach those tools.

---

### Slide 5 – Not this hour
**Title:** Not this hour / complement

ATT&CK = behavior. Diamond = know/don’t-know. Kill Chain = stages.  
DTF = discovery. Same shape. Different job.

No invented P-codes. No 2.7.5 lump.

**Speaker Notes:**  
Outline e / task 3.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. DTF replaces ATT&CK. True or false?  
2. Same NS on the update domain and `login-prd.net`. PTA / P-ID, or reject?  
3. Whole `203.0.113.0/24`. Take or reject, and next lookup if you took same-A?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Real IDs. Cite. Reject shared cloud. Name the next lookup.

**Next:** **2.8.1** Infrastructure hop sentence

**Speaker Notes:**  
Do not open 2.8 unless that hour is scheduled.
