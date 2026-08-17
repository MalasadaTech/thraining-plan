# Module 1.4.5 – SLA / Response Time Goals  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.4.5 – SLA / Response Time Goals  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Two clocks. Classroom 15 / 45. Closes 1.4. CTI is A/1a.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Explain start clock vs close/escalate clock
2. Given timestamps, which clock is at risk
3. Record close or escalate against the correct clock

**Mapped Items:**  
K: 1.4.5.1 | T: 1.4.5.2 | T: 1.4.5.3

**Speaker Notes:**  
Hunter 3 is A / 1a.

---

### Slide 3 – Agenda
**Title:** Agenda

- Two clocks
- Classroom 15 / 45
- Three worked examples
- Four timestamp cards
- Knowledge check — close 1.4

**Speaker Notes:**  
0.6 is next unit.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Investigation how-to (**1.4.1**)  
TP / FP / category  
Ticketing-product admin  
“Work faster”  
One blended “we’re late”

**Key Point:** Name the clock. Record the disposition.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Start Clock
**Title:** Clock A — Begin Investigation

From **created** → first touch (`started`).  
Classroom: **15 minutes**.

Untouched → this is the only clock that exists.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Close / Escalate Clock
**Title:** Clock B — Process the Alert

From **started** → `closed` or `escalated`.  
Classroom: **45 minutes**.

Start already met (or already breached). This is the remaining clock.

**Speaker Notes:**  
Outline b.

---

### Slide 7 – The Record
**Title:** Four Fields

`alert_id | closed or escalated (or started) | which clock | timestamp`

Not a CMDB class.

**Speaker Notes:**  
Task 2.

---

### Slide 8 – Example 1: Both OK
**Title:** Example 1 – A12

Created 14:00 · started 14:08 · closed 14:40

Start OK (8). Close OK (32).

**Speaker Notes:**  
Students first.

---

### Slide 9 – Example 2: Start
**Title:** Example 2 – A13 Untouched

Created 14:00 · now 14:18 · no start

**Start** breached. Do not close yet.  
Record **started**.

**Speaker Notes:**  
No close-escalate origin.

---

### Slide 10 – Example 3: Close/Escalate
**Title:** Example 3 – A14 Open Too Long

Started 13:28 · now 14:20 (52 min)

**Close/escalate** breached. Escalate or close.  
Start already met.

**Speaker Notes:**  
Name the clock.

---

### Slide 11 – Site Numbers
**Title:** Classroom vs Site

15 / 45 are **this lesson**.  
If you have a site card, overlay it.  
Keep **two clocks**.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- “Late” with no clock  
- Close without a start  
- Close-escalate measured from created  
- Relitigating TP  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Now = 15:00
**Title:** Exercise Clock

Start 15 · close/escalate 45  
Now **15:00**

**Speaker Notes:**  
Leave up.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize Ex 1–3.
2. A–D: which clock + one record line.
3. No investigation rewrite.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Two clocks — when does each start?
2. Untouched — which clock?
3. Why not “work faster”?
4. Four record fields?
5. Who owns live-org numbers?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Start from created. Close/escalate from first touch.
- Name the clock. Record the disposition.
- Unit **1.4** ends. Next unit: **0.6** Frameworks.

**Speaker Notes:**  
Do not open ATT&CK unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** SLA — Quick Reference

| Clock | From → to | Classroom |
|-------|-----------|-----------|
| Start | created → started | 15 min |
| Close/escalate | started → closed/escalated | 45 min |

**Coming next:** Module 0.6.1 – MITRE ATT&CK

**Footer:** SOC / Hunter / CTI Training Program
