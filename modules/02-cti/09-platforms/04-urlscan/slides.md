# Module 3.9.4 – URLScan  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.9.4 – URLScan Retrieve and Extract  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
No live malware submit. Classroom retrieve card.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Capabilities of a page scan
2. Retrieve (or submit) a result
3. Extract redirect / host / appearance
4. Reject PDNS-use and theft over-claim

**Mapped Items:**  
K: 3.9.4 | T: 3.9.4.1

**Speaker Notes:**  
SOC K is A/A/B. Task ends at 4c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Capabilities + interpret
- Three examples
- Retrieve/submit + extract
- Knowledge check

**Speaker Notes:**  
Closes 3.9. 3.10 is next unit.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

When to pick URLScan (**3.3.2**)  
PDNS history (**3.9.3**)  
File process tree (**3.9.2**)  
SIEM/Zeek query (**2.3.1**)  
Impact / profile (**3.8.4** / **3.11**)

**Key Point:** This page load only.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Capabilities
**Title:** This URL, This Load

Submit / retrieve · redirects · contacted hosts · screenshot

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Interpret
**Title:** What to Take

Redirect + host + appearance.  
Not history. Not theft success.

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Classroom Scan
**Title:** `invoice-harbor.example/pay`

Redirects to `nightowl-updates.net/invoice`.  
Contacted `203.0.113.88`. Fake Harbor login.

**Speaker Notes:**  
Retrieve, do not submit.

---

### Slide 8 – Lines
**Title:** Two Lines

`URL | submit or retrieve | why`  
`redirect | host | appearance | will not claim`

**Speaker Notes:**  
Tasks.

---

### Slide 9 – Example 1
**Title:** Example 1 – Retrieve

Redirect + host + appearance. Stop.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2
**Title:** Example 2 – Not PDNS

Last year’s IPs = Silent Push.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3
**Title:** Example 3 – Not Theft

Screenshot ≠ password sent.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Live malware submit from class  
- URLScan as PDNS  
- Screenshot as Sev1 theft  
- Writing the 3.11 profile  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Retrieve first. Never require a live bad submit.  
Keep: this-load facts only.

**Speaker Notes:**  
Safety.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–C: retrieve/submit lines.
3. Extract + D/E.
4. No live submit.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. URLScan for?
2. Retrieve vs submit?
3. Two extract fields?
4. Why not historical A?
5. Why not theft from the screenshot?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- This load. Not PDNS. Not a profile.
- Next unit: **3.10** STIX.

**Speaker Notes:**  
Do not open 3.10 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** URLScan — Quick Reference

| Field | Take |
|-------|------|
| Redirect | `nightowl-updates.net/invoice` |
| Contacted | name + `203.0.113.88` |
| Screenshot | appearance only |
| Historical A | wrong tool |

**Coming next:** Module 3.10 – Common STIX Objects

**Footer:** SOC / Hunter / CTI Training Program
