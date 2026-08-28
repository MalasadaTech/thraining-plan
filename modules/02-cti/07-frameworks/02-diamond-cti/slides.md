# Module 2.7.2 – Diamond Model Application in CTI  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.7.2 – Diamond Model Application in CTI  
**Subtitle:** Four vertices on a report or activity set  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is CTI application of Diamond. Fill the product from a report or activity set. Name the weakest vertex. Reject a vendor-name Adversary. Do not re-teach the shared Diamond lesson.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts put Diamond on a **report or activity set**.

The product shows what you **know** and what you **do not**.

Fill four vertices. Name the **weakest**.  
Reject a vendor APT name as **Adversary**.

**Speaker Notes:**  
This slide is the student intro. Hunt and detection reuse the card. The job is an honest intel product, not a group name from a PDF. Do not open ATT&CK IDs or Kill Chain stages.

---

### Slide 3 – Four vertices on the product
**Title:** Four vertices on the product

**Adversary** — who you can defend against, only with evidence.  
**Capability** — what they used.  
**Infrastructure** — where they hosted it or talked through it.  
**Victim** — who was hit.

Fill each from the report or activity set in front of you.

**Speaker Notes:**  
Name the four corners as the fills on a CTI product. Do not walk the shared-floor purpose lecture. The next slide is the A12 card.

---

### Slide 4 – A12 card
**Title:** A12 card

**Capability** — encoded PowerShell / `update.exe`.  
**Infrastructure** — update domain / `203.0.113.88`.  
**Victim** — **WS-JLEE** / `jlee` / DYA.  
**Adversary** — unknown cluster. **Weakest.**

The weakest vertex **constrains** the product. Do not guess a group to finish the card.

**Speaker Notes:**  
Walk the student table. Three vertices have internals. Adversary does not. Do not add the beacon POST. That row is not this activity set.

---

### Slide 5 – A vendor name is not Adversary
**Title:** A vendor name is not Adversary

“PRD APT” on a PDF is a **vendor label**.

It does **not** fill Adversary.

Write unknown cluster. Name Adversary as weakest.

**Speaker Notes:**  
This is the reject. A title that looks like a who is still not evidence. Actor profile and attribution types wait for later lessons.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A vendor APT name fills the Adversary vertex. True or false?  
2. Name the four vertices.  
3. Fill Diamond for **A12** and name the weakest vertex.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Four vertices on the CTI product.  
Weakest named — that gap drops a who-claim.  
A vendor label is not Adversary.

**Next:** **2.7.3** Kill Chain for CTI

**Speaker Notes:**  
Kill Chain is next. Same kind of product, now in stages. Stay off Diamond when you get there.
