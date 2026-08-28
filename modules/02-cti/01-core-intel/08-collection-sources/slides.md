# Module 2.1.8 – Collection sources and methods  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.1.8 – Collection sources and methods  
**Subtitle:** Where you collect: OSINT, commercial, internal  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson names the three source classes and what a short collection plan looks like. It is not the lifecycle Collection stage, and it is not the local request ticket.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

A requirement names a **question**.

Before you gather, know **which class of source** can answer it.

This lesson names the three classes and what a short **plan** looks like.

**Speaker Notes:**  
This slide is the student intro. CTI analysts choose where to collect so they do not skip internals when the question is “are we seeing this?” Do not open a tool or file a ticket in this lesson.

---

### Slide 3 – Three source classes
**Title:** OSINT, commercial, internal

**OSINT** — public reporting, public DNS, open blogs. The public story.  
**Commercial** — paid TIP, premium sandbox, vendor intel. Packaged enrichment.  
**Internal** — our SIEM, EDR, Zeek, tickets, TIP, hunt output. Are *we* seeing this?

**Speaker Notes:**  
One line each. Stop. Do not list vendor sites. OSINT is not enough when the question is our presence. Internal is not enough when the question is only the public story.

---

### Slide 4 – The plan
**Title:** Class, first action, what you will not collect

Classes **stack**. Order follows the **requirement**, not habit.

A plan is **source class** + **first action** + **what you will not collect**.

Not a tool click. Not a local request ticket.

**Speaker Notes:**  
This is the method in this lesson. The next slide is the one given. Do not invent a second plan or a shop source catalog.

---

### Slide 5 – What good looks like
**Title:** Plan for “payload host *here*?”

Question: is this the payload host **here**?  
First class: **internal**.  
First action: telemetry you already have (Zeek A record, or the file from the host).

Do **not** start with a public blog.  
Do **not** chase a sibling domain on this plan.

**Speaker Notes:**  
This is the classroom A12 question. Internals first because the requirement is our presence. Then OSINT or commercial if the public story is still needed. Do not file a ticket here.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Collection as a lifecycle stage and a source class are the same thing. True or false?  
2. Name the three source classes.  
3. A requirement asks: is this the payload host *here*? First class, first action, one thing you will not collect.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Three classes. Order follows the question.  
Internals first when it is *our* presence.  
A plan names the class, the first action, and what you will not collect.

**Next:** **2.2.1** Estimative language

**Speaker Notes:**  
The 2.1 cluster ends. Tradecraft is next. Stay off the local collection-request process when you get there; that is 2.12.
