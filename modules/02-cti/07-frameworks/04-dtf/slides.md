# Module 3.7.4 – DTF  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.7.4 – Defender’s ThreatMesh Framework  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Real DTF. Discovery pivots. No score.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Discover additional infra from a known-bad seed
2. Pick a real PTA + P
3. Cite the characteristic; reject the weak neighbor
4. Name the next lookup
5. Complement ATT&CK, Diamond, Kill Chain

**Mapped Items:**  
K: 3.7.4 | T: 3.7.4.1 · 3.7.4.2 · 3.7.4.3

**Speaker Notes:**  
SOC K is A/A/B. CTI 4d is distinctive vs weak.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose, PTA/P, apply set
- Three examples
- DTF lines + lookups + complement
- Knowledge check

**Speaker Notes:**  
3.8.1 is next, not this hour’s product.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

ATT&CK IDs (**3.7.1**)  
Diamond vertices (**3.7.2**)  
Kill Chain stages (**3.7.3**)  
Generic hop without IDs (**3.8.1**)  
Mesh + 0–3 score (**retired**)

**Key Point:** Real PTA/P. No score.

**Speaker Notes:**  
Fence. Link the GitHub repo; do not copy it.

---

### Slide 5 – Purpose
**Title:** Discover · Communicate · Record

Known-bad seed → shared characteristic → candidate infra.

**Speaker Notes:**  
Outline a. Official DTF README.

---

### Slide 6 – Four Tactics
**Title:** PTA0001–0004

Domain · IP · SSL · Application  
Depth this hour: Domain + IP.

**Speaker Notes:**  
Outline b. SSL/HTTP named only.

---

### Slide 7 – Apply Set (Real IDs)
**Title:** Night Owl Seed

P0101.010 NS · P0102.002 substring · P0103.003 same A  
P0202 /24 = reject. T1486 = not a DTF ID.

**Speaker Notes:**  
Outline c. IDs from the live matrix.

---

### Slide 8 – Lines
**Title:** DTF Line · Lookup Line

`seed | PTA | P-ID | characteristic | candidate | why`  
`P-ID | next lookup | what you hope to learn`

**Speaker Notes:**  
Tasks 3.7.4.1–2.

---

### Slide 9 – Complements
**Title:** Four Frameworks, Four Jobs

ATT&CK = behavior  
Diamond = gaps  
Kill Chain = order  
DTF = defender discovery

**Speaker Notes:**  
Outline e. Same shape as ATT&CK, different job.

---

### Slide 10 – Example 1
**Title:** Example 1 – Distinctive Stack

NS + substring + same A → `login-nightowl.net`

**Speaker Notes:**  
Students first.

---

### Slide 11 – Example 2
**Title:** Example 2 – Weak P0202

Cloud /24 is not theirs.

**Speaker Notes:**  
Lead. 4d.

---

### Slide 12 – Example 3
**Title:** Example 3 – Not Infra / Invented ID

T1486 and `P9999` fail.

**Speaker Notes:**  
Lead.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Mesh + recency + reach  
- /24 as P0202  
- T-IDs in the DTF line  
- Opening Silent Push as the product  

**Speaker Notes:**  
Then the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–E: DTF lines.
3. Lookup lines for A–C.
4. One complement sentence each (ATT&CK / Diamond / Kill Chain).

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. DTF for?
2. DTF line besides the P-ID?
3. Why not the /24?
4. This hour — do / don’t?
5. One complement?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Real PTA/P. Cite. Reject the weak one. Name the lookup.
- Next: **3.8.1** generic infra hop.

**Speaker Notes:**  
Do not open 3.8.1 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** DTF — Quick Reference

| Evidence | ID |
|----------|-----|
| Distinctive NS | P0101.010 |
| `nightowl` substring | P0102.002 |
| Same A | P0103.003 |
| /24 or T1486 | none |

**Coming next:** Module 3.8.1 – Identifying additional adversary infrastructure

**Footer:** SOC / Hunter / CTI Training Program
