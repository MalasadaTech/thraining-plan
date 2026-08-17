# Module 3.2.2 – Hunt Development  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC, CTI sit this too  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.2.2 – Hunt Development  
**Subtitle:** Threat Hunter (SOC / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Four-line card. No invented ticket.

---

### Slide 2 – What this hour is
**Title:** What this hour is

**Bound** the search.

Hypothesis. Scope. Priority. Unique pattern.

**Speaker Notes:**  
Type was last hour.

---

### Slide 3 – Four pieces
**Title:** Card contents

**Hypothesis** — if X, we see Y.  
**Scope** — where / how long / which tables.  
**Priority** — why now.  
**Pattern** — specific enough to search.

**Speaker Notes:**  
Outline a–d.

---

### Slide 4 – What good looks like
**Title:** A12 card

If persistors exist, Run **`Updater`** → `%TEMP%\update.exe`.  
Scope: user workstations, 14 days, registry + file.  
Priority: open incident + FN download.  
Pattern: value name **`Updater`**, not any Run key.

**Speaker Notes:**  
Tasks 1–3.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No SIEM session.  
No local template (**3.7.2**).  
No “hunt persistence” (**3.6.3**).

**Speaker Notes:**  
Tools next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A hunt card is “search everything for malware.” True or false?  
2. What four pieces does the card have?  
3. Write a one-line **A12** hypothesis and one unique pattern.

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Hypothesis, scope, priority, unique pattern.

**Next:** **3.3.1** Hunt tool capabilities

**Speaker Notes:**  
Do not open tools unless scheduled.
