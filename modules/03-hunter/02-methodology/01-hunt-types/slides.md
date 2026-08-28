# Module 3.2.1 – Hunt Types  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.2.1 – Hunt Types  
**Subtitle:** Intel, hypothesis, reactive, anomaly  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson names the four hunt types and what execute looks like for each. It does not teach the hunt card, and it is not a SIEM session.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Hunters pick a **type** so the search has a reason.

After **A12**, the start might be a CTI domain, an if/then, a known incident, or an odd pattern with no intel yet.

Mix the starts and you look for the wrong thing.

**Speaker Notes:**  
This slide is the student intro. 3.1 said why hunting exists. This lesson is which kind of hunt you are running. Do not write the card today.

---

### Slide 3 – Four types
**Title:** Intel, hypothesis, reactive, anomaly

**Intel-driven** — starts from a CTI fact.  
**Hypothesis-driven** — starts from “if they persist, we should see X.”  
**Reactive** — starts from a known incident.  
**Anomaly-based** — starts from an odd pattern, with no intel naming it yet.

**Speaker Notes:**  
One line each. Stop. The start is the type. Neighbors and A12 look-for lines are the next slide.

---

### Slide 4 – Execute is type plus look-for
**Title:** Execute is type plus look-for

**Intel** — search hosts for the update domain or file CTI already worked.  
**Hypothesis** — search HKCU Run **`Updater`**.  
**Reactive** — after **A12**, more `invoice.vbs` or `update.exe` on other hosts.  
**Anomaly** — GET `:8080` `/update.exe` with no alert, and no intel yet.

Name the type, the seed, and the look-for. Not a live SIEM session. Not the written card (**3.2.2**).

**Speaker Notes:**  
Walk these four A12 lines before the knowledge check. Execute is that product line. If they open a SIEM or start the card, stop them. Do not invent a ticket.

---

### Slide 5 – The start decides the type
**Title:** The start decides the type

A CTI domain is **intel-driven**, not an if/then.

“If they persist, we should see Run **`Updater`**” is **hypothesis-driven**, even if a report mentioned persistence.

After **A12**, more `invoice.vbs` on other hosts is **reactive**. Rewriting the **WS-JLEE** process alert is SOC work.

**Speaker Notes:**  
This is the mix-up slide. A nearby CTI report does not make every hunt intel-driven. Reactive is more of the incident on other hosts, not a better write-up of the first alert.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. All four types start from a CTI report. True or false?  
2. Name the four types.  
3. “If they persist, we should see Run `Updater` on more hosts.” Which type, and what do you search?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Four starts. Execute is type plus look-for.  
Not a rewritten ticket. Not a SIEM session.

**Next:** **3.2.2** Hunt development

**Speaker Notes:**  
3.2.2 is the written card. Stay off hypothesis / scope / priority format unless that lesson is scheduled.
