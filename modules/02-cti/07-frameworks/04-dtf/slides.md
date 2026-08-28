# Module 2.7.4 – MalasadaTech Defender's ThreatMesh Framework (DTF)  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.7.4 – Defender's ThreatMesh Framework (DTF)  
**Subtitle:** Infrastructure discovery from a known-bad seed  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is defender discovery. Use real PTA and P IDs only. There is no score. Do not invent P-codes. Do not re-teach ATT&CK, Diamond, or Kill Chain.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts start from a **known-bad seed**.

The job is to find **more infrastructure** and record the pivot so someone else can run it again.

This lesson is that discovery language.

**Speaker Notes:**  
This slide is the student intro. They already have a seed. They need a shared ID for the pivot, a cited characteristic, and a named next lookup. Do not write the generic hop sentence today. That is 2.8.1.

---

### Slide 3 – Four pivot tactics
**Title:** Four pivot tactics

DTF is shaped like ATT&CK. The job is **discovery**, not behavior.

**PTA0001** Domain — registration, domain string, DNS.  
**PTA0002** IP — reverse lookup, proximity, AS.  
**PTA0003** SSL — issuer / SAN, only if a cert card exists.  
**PTA0004** Application — HTTP title / resources, only if a page card exists.

Pivots nest: **P0101.010** is Registration: Name Server.

**Speaker Notes:**  
Name the four tactics and stop. Do not walk every P-code. If they invent an ID, it is not in DTF. SSL and Application wait for a card this seed does not have.

---

### Slide 4 – Take versus reject
**Title:** Take versus reject

**Seed:** update domain / `203.0.113.88`. Candidate `login-prd.net`.

**Take** — same NS (`PTA0001 / P0101.010`) or same A (`PTA0001 / P0103.003`).  
**Reject** — whole `203.0.113.0/24` (`PTA0002 / P0202`). Shared cloud.  
**No DTF ID** — a vendor APT name or an ATT&CK T-ID.

Cite the characteristic. Reject the weak neighbor.

**Speaker Notes:**  
Walk the two takes and the /24 reject from the student guide. Distinctive NS is not a public resolver. Proximity is a real pivot; this /24 is still a reject because it is shared hosting.

---

### Slide 5 – Name the next lookup
**Title:** Name the next lookup

The selected P-ID **names** what to ask next. It does not run the tool.

**P0101.010** Name Server → RDAP / WHOIS (**2.5**).  
**P0103.004** SOA RName → SOA (**2.6**).  
**P0103.003** DNS: IP Address → passive DNS / other names on that A (**0.7** / **2.9.3**).

**Speaker Notes:**  
The product here is the name of the lookup. Do not open RDAP, SOA, or Silent Push. If they write a hop with no P-ID, that is 2.8.1.

---

### Slide 6 – Complements, does not replace
**Title:** Complements, does not replace

**ATT&CK** — behavior.  
**Diamond** — know / don’t-know.  
**Kill Chain** — progression.  
**DTF** — discovery pivots.

Same matrix shape. Different job.

**Speaker Notes:**  
One line each. Do not re-teach the other three frameworks. If they assign T1059, that is 2.7.1, not a DTF pivot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. DTF replaces ATT&CK. True or false?  
2. Same NS on the update domain and `login-prd.net`. Which PTA / P-ID, or reject?  
3. Whole `203.0.113.0/24`. Take or reject, and what is the next lookup if you took same-A instead?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Real PTA and P IDs only.  
Cite the characteristic. Reject shared cloud.  
Name the next lookup.  
DTF does not replace ATT&CK, Diamond, or Kill Chain.

**Next:** **2.8.1** Infrastructure hop sentence

**Speaker Notes:**  
2.8.1 is the hop sentence without P-IDs. Stay off the DTF ID line when you get there.
