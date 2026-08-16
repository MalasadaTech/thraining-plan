# Module 3.8.4 – Relevance and Impact  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.8.4 – So What, Here?  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Not the TTP list. Not a PIR.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Relevance to this estate
2. Impact if true
3. Reject skipped path, PIR, attribution

**Mapped Items:**  
K: 3.8.4 | T: 3.8.4.1

**Speaker Notes:**  
CTI 3c / 4c / 4d. Hunter tops at 4c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Relevance + impact
- Three examples
- Exercise
- Knowledge check

**Speaker Notes:**  
3.8 ends here.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

TTP apply (**3.8.2**)  
IOC file (**3.8.3**)  
Write / obtain PIRs (**3.1.4** / **3.12.1**)  
Attribution (**3.1.7**)

**Key Point:** So what *here*.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Relevance
**Title:** Does It Apply to This Estate?

Windows users — yes for Night Owl  
OT-only / ESXi — no on this card

**Speaker Notes:**  
Outline a. Harbor 1.8.1 stand-in.

---

### Slide 6 – Impact
**Title:** If True, What Changes?

User-estate persistence + HTTP C2  
Not automatically payroll

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Impact Line
**Title:** Impact Line

finding | relevant? (fact) | impact if true | not because

**Speaker Notes:**  
4d is the last clause.

---

### Slide 8 – Crown Jewels Are Bait
**Title:** `pay-db-01` Needs a Path

On the Harbor card.  
Not reached by WS-JLEE on *this* evidence.

**Speaker Notes:**  
Example 2.

---

### Slide 9 – Finding on the Desk
**Title:** Night Owl on WS-JLEE

Encoded PowerShell. Run `Updater`. HTTP GET.

**Speaker Notes:**  
Already handled in 3.8.3.

---

### Slide 10 – Example 1
**Title:** Expected — User Estate

Relevant. Impact = that estate. Jewel not shown.

**Key Point:** Product shape.

**Speaker Notes:**  
Students write first.

---

### Slide 11 – Example 2
**Title:** Lead — Payroll Is Down

Skipped path. Fail.

**Key Point:** Jewel ≠ impact.

**Speaker Notes:**  
Ask what cite would fix it.

---

### Slide 12 – Example 3
**Title:** Lead — PIR or Nation-State

Wrong product. Fail.

**Key Point:** 3.12.1 / 3.1.7.

**Speaker Notes:**  
Park both.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Resubmit the TTP list  
- Sink pay-db-01  
- Invent PIR-1  
- Attribution letter  

**Speaker Notes:**  
Park all four.

---

### Slide 14 – Hands-On Exercise
**Title:** Exercise

Impact lines A–E. Product is A.

**Speaker Notes:**  
B not relevant. C–E fail.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Relevance vs 3.8.2?  
2. Impact line?  
3. Why not pay-db-01?  
4. Why not a PIR?  
5. Where is the real list?

**Speaker Notes:**  
Answers in the instructor guide.

---

### Slide 16 – Summary
**Title:** Summary

Relevant to this estate. Impact on the evidence. Not shown stays not shown.

**Coming next:** Outside 3.8 (usually **3.9**)

**Speaker Notes:**  
Cluster complete.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Impact Line

`finding | relevant? (Harbor fact) | impact if true | not because`

**Speaker Notes:**  
Leave up during the exercise.
