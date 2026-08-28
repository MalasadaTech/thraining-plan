# Module 2.2.2 – Structured Analytic Techniques  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.2.2 – Structured Analytic Techniques  
**Subtitle:** Named methods so a favorite story does not win  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is two named methods: Key Assumptions Check and Analysis of Competing Hypotheses. Pick the one the problem needs. Do not invent a third official technique.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts use a **named method** so a favorite story does not win by habit.

A draft often already has a preferred explanation. This lesson is how you pick a method and apply it.

Not a likelihood word. Not a source letter. Not a bias name.

**Speaker Notes:**  
This slide is the student intro. The job is to slow the jump to one story. Estimative language was the previous lesson. Admiralty and bias names wait.

---

### Slide 3 – Purpose of a structured technique
**Title:** Purpose of a structured technique

A **structured analytic technique** is a named way to test a call.

Purpose: make the jump to one story slower and inspectable.

Pick the technique that matches the problem.  
Do not run both to fill time.

**Speaker Notes:**  
Name the purpose before the two techniques. The product is one method applied, not a stack of methods that look thorough.

---

### Slide 4 – Two techniques
**Title:** Key Assumptions Check vs ACH

**Key Assumptions Check** — one claim is carrying the call. List it. Say what breaks it.  
**ACH** — two or more explanations. See which evidence **hurts** each one.

This lesson teaches those two only.

**Speaker Notes:**  
One line each. Stop. Hurt means evidence that is hard for a hypothesis to live with. Do not score ACH by how many facts support the favorite story.

---

### Slide 5 – What good looks like
**Title:** Apply one

**Key Assumptions Check** — assumption: a vendor APT name is who they are. Break: it is a PDF label.  
**ACH** — H1 payload host for **A12**. H2 ordinary browse. `GET /update.exe` `:8080` hurts H2.

You do not need a full spreadsheet.

**Speaker Notes:**  
Show these givens before the knowledge check. A12 is the classroom incident on WS-JLEE. Do not retell the whole plot. Name H1, H2, and what hurts, then stop.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. You should always run ACH and a Key Assumptions Check on every product. True or false?  
2. When do you pick a Key Assumptions Check instead of ACH?  
3. For **A12**, name one assumption a Key Assumptions Check would test.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Named method.  
ACH when two stories compete.  
Key Assumptions Check when one claim is carrying the call.

**Next:** **2.2.3** Admiralty Code

**Speaker Notes:**  
Admiralty is next. Stay off source letters unless that lesson is scheduled.
