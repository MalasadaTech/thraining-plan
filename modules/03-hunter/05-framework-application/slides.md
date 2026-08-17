# Module 3.5.1 – Using MITRE ATT&CK for Hunt Planning
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC, CTI sit this too  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.5.1 – ATT&CK for Hunt Planning  
**Subtitle:** Threat Hunter (SOC / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Map this hunt. Not the whole matrix.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Map **this hunt** to tactic + technique.

Name the **gap**. ATT&CK **supports** priority.

**Speaker Notes:**  
Copied ID is 3.4.2. This hour is the map.

---

### Slide 3 – Map and gaps
**Title:** Map, then ask

**Map** — method → tactic + technique.  
**Detection gap** — data exists; no analytic.  
**Visibility gap** — you cannot see it. Do not hunt it.

**Speaker Notes:**  
Outline a–c.

---

### Slide 4 – What good looks like
**Title:** A12

**Map** — Run **`Updater`** → **TA0003** / **T1547.001**.  
**Detection gap** — registry logs, no `Updater` analytic.  
**Priority** — open incident + FN, not “Persistence first.”

**Speaker Notes:**  
Tasks 1–3.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No whole-enterprise layer (**0.6.1** / Navigator).  
No CTI product map (**2.7.1**).  
No Run-key how-to (**3.6.1**).

**Speaker Notes:**  
Persistence recognition next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Copying T1547.001 off a report is a coverage analysis. True or false?  
2. Detection gap vs visibility gap?  
3. Map A12 Run-**`Updater`**. If registry logs exist and no analytic fires, which gap is it?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Map this hunt. Name the gap. ATT&CK supports priority.

**Next:** **3.6.1** Persistence techniques

**Speaker Notes:**  
Do not open persistence unless scheduled.
