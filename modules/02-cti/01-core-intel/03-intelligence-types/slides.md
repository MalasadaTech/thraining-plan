# Module 2.1.3 – Intelligence Types  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.1.3 – Intelligence Types  
**Subtitle:** Strategic, operational, tactical, technical  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson names four types of intelligence. It does not teach how to write a PIR.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

A consumer needs a **decision they can make**.

An alert responder needs what to do **now**.  
Leadership needs whether to change **posture**.

This lesson names the **kind of answer**.

**Speaker Notes:**  
This slide is the student intro. Match the product or the requirement to the decision. Do not write a PIR today.

---

### Slide 3 – Four types
**Title:** Strategic, operational, tactical, technical

**Strategic** — what leadership should change about risk or posture (months to years).  
**Operational** — how we run this incident or hunt over days to weeks.  
**Tactical** — what a responder should do **now** on this activity.  
**Technical** — the observables we can detect or pivot on.

**Speaker Notes:**  
One line each. Stop. Technical is its own type, not a nickname for tactical. Neighbors are the next slide.

---

### Slide 4 – Type follows the question
**Title:** Type follows the question

A long PDF is not automatically strategic.  
A hash is not an action.

Neighbors are strategic vs operational, and tactical vs technical.

A **requirement** is the question. A **product** is the answer. Both get a type.

**Speaker Notes:**  
Length is not type. A lifecycle stage is not type. If they start writing a PIR, that is 2.1.4.

---

### Slide 5 – Type, and not the neighbor
**Title:** Type, and not the neighbor

**Technical** — A record `203.0.113.88`; `GET /update.exe` on port 8080.  
Not “isolate the host.”

**Tactical** — isolate **WS-JLEE**; treat the update domain as the **A12** payload host.  
Not a hash dump.

**Speaker Notes:**  
Walk these two givens before the knowledge check. Do not invent extra victims for operational or strategic.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A long PDF is strategic because it is long. True or false?  
2. Name the four types.  
3. “Isolate **WS-JLEE**; treat the update domain as the **A12** payload host.” Type, and why not the neighbor?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Type follows the question.  
Strategic, operational, tactical, technical.  
Reject the neighbor.

**Next:** **2.1.4** Intelligence requirements

**Speaker Notes:**  
2.1.4 is writing the requirement. Stay off PIR format unless that lesson is scheduled.
