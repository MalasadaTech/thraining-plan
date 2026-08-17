# Module 3.2.1 – Hunt Types  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC, CTI sit this too  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.2.1 – Hunt Types  
**Subtitle:** Threat Hunter (SOC / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Four types. Execute = type + look-for. No lab.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Pick **why** you are searching.

Name the type and the look-for.  
Not the written card.

**Speaker Notes:**  
3.1 was why hunt exists.

---

### Slide 3 – Four types
**Title:** Intel, hypothesis, reactive, anomaly

**Intel-driven** — CTI seed.  
**Hypothesis-driven** — if they persist, we should see X.  
**Reactive** — after a known incident.  
**Anomaly-based** — odd pattern, no intel yet.

**Speaker Notes:**  
Outline a–d.

---

### Slide 4 – What good looks like
**Title:** A12 execute lines

**Intel** — search the update domain / file.  
**Hypothesis** — search Run **`Updater`**.  
**Reactive** — more `invoice.vbs` after A12.  
**Anomaly** — GET `:8080` `/update.exe` with no alert.

**Speaker Notes:**  
Tasks 4–7 as product lines.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No hunt card (**3.2.2**).  
No SIEM session.  
No invented ticket (**3.7**).

**Speaker Notes:**  
Development next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. All four types start from a CTI report. True or false?  
2. Name the four types.  
3. “If they persist, we should see Run `Updater` on more hosts.” Which type, and what do you search?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Four starts. Execute = type + look-for.

**Next:** **3.2.2** Hunt development

**Speaker Notes:**  
Do not open the card unless scheduled.
