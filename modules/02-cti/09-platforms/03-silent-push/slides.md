# Module 3.9.3 – Silent Push  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.9.3 – Silent Push Enrich and Pivot  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
SP fields, not SOA lecture. Classroom cards.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Capabilities that matter
2. Enrich the seed in Silent Push
3. Pivot on a cited field
4. Reject /24 and sandbox use

**Mapped Items:**  
K: 3.9.3 | T: 3.9.3.1

**Speaker Notes:**  
SOC K is A/A/B. CTI task 4d.

---

### Slide 3 – Agenda
**Title:** Agenda

- Capabilities + enrich/pivot
- Three examples
- Enrich line + four pivot lines
- Knowledge check

**Speaker Notes:**  
3.9.4 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

When to pick SP (**3.3.2**)  
SOA timers (**3.6**)  
Hop without the SP UI (**3.8.1**)  
VT Relations (**3.9.1**)  
URLScan this-load (**3.9.4**)

**Key Point:** Cited Silent Push field.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Capabilities
**Title:** PDNS · Siblings · NS · Score

Score is a hint, not a verdict.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Enrich then Pivot
**Title:** Fill the Record, Then One Field

Enrich = A / first-seen / NS.  
Pivot = follow that field.

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Classroom Record
**Title:** `nightowl-updates.net`

A `203.0.113.88` since 2026-08-01.  
Sibling `login-nightowl.net`.

**Speaker Notes:**  
Lesson-only.

---

### Slide 8 – Lines
**Title:** Two Lines

Enrich: `indicator | fields | tells you | must not claim`  
Pivot: `seed | SP field | infra | why`

**Speaker Notes:**  
Tasks.

---

### Slide 9 – Example 1
**Title:** Example 1 – Same A

`login-nightowl.net` is the hop.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2
**Title:** Example 2 – /24

Cloud tenants ≠ theirs.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3
**Title:** Example 3 – Not a Sandbox

No process tree here.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Score as attribution  
- CIDR spray  
- Re-teaching SOA  
- Opening AnyRun  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Same fields on a live SP page.  
Keep: cite the field; reject /24.

**Speaker Notes:**  
Lesson-only cards.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. One enrich line.
3. A–D: pivot lines.
4. No SOA card. No VT.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Two capabilities + not?
2. Enrich line?
3. Why not /24?
4. What does sibling first-seen add?
5. Where is the process tree?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Cited field. Not the cloud block.
- Next: **3.9.4** URLScan.

**Speaker Notes:**  
Do not open 3.9.4 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Silent Push — Quick Reference

| Field | Take |
|-------|------|
| Same A | `login-nightowl.net` |
| First-seen on sibling | ages the name |
| /24 | reject |
| Process tree | wrong tool |

**Coming next:** Module 3.9.4 – URLScan

**Footer:** SOC / Hunter / CTI Training Program
