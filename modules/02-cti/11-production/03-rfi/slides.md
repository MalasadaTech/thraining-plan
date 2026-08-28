# Module 2.11.3 – Handling RFIs  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.11.3 – Handling RFIs  
**Subtitle:** Answer the question. Do not open a second case.  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
2.11.2 sent the finished product. This lesson is the RFI answer: take the question, decide whether you can answer it and whether it goes first, and write the answer. It is not a second incident and not a shop queue policy.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts answer the question another desk sent.

That ask is an **RFI** (Request for Information).  
SOC already has a case. They still need a fact.

You do not open a second incident.

**Speaker Notes:**  
This slide is the student intro. The RFI is the question, not a second case. SOC type pick is 1.5.1. This lesson is the answer.

---

### Slide 3 – Purpose and lifecycle
**Title:** Purpose and lifecycle

**Purpose** — someone needs information they do not have. The RFI *is* the question.

**Lifecycle** — receive → evaluate → prioritize → respond.

This classroom queue is **lesson-only**. It is not live org policy.

**Speaker Notes:**  
Name purpose and the path before the three handling steps. Local queue names and SLAs are 2.12. Do not invent a DYA board here.

---

### Slide 4 – Evaluate, prioritize, respond
**Title:** Evaluate, prioritize, respond

**Evaluate** — can we answer with what we have? What is missing?

**Prioritize** — open incident versus standing work (not a live case).

**Respond** — answer the question. Do not rewrite the SOC ticket.

**Speaker Notes:**  
Those three are the handling steps. Receive is how the ask arrives. If they cannot answer, they say what is missing. They do not invent a second question.

---

### Slide 5 – What good looks like
**Title:** Evaluate it. Answer A12.

**Evaluate** — bounded question. Zeek A record plus the host file. **Can answer.**

**Prioritize** — open incident. IR has the host. **Work now.**

**Respond** — **likely** yes. The update domain / `203.0.113.88` is the payload host. Treat it as such.

Not a country. Not a new case.

**Speaker Notes:**  
Show this given before the knowledge check. A12 is the classroom incident on WS-JLEE. Two sentences. Do not hop to a sibling domain. Do not tell the intro plot.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Answering an RFI means opening a second incident. True or false?  
2. What three steps do you take on an RFI?  
3. Write a two-sentence **A12** RFI response (no country, no second case).

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

The RFI is the question.  
Evaluate, prioritize, answer.  
Do not rewrite the ticket. Do not open a second case.

**Next:** **2.12.1** Local priorities

**Speaker Notes:**  
2.11 ends. 2.12.1 is obtain the local card. Do not invent a queue policy unless that lesson is scheduled.
