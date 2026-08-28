# Module 3.2.2 – Hunt Development Concepts  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.2.2 – Hunt Development  
**Subtitle:** Hypothesis, scope, priority, unique pattern  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
3.2.1 named the hunt types. This lesson is the write-up: a four-line hunt card. It is not a SIEM session and not a ticket you invent.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Hunters bound a search **before** they query.

Write a short **hunt card**: hypothesis, scope, priority, unique pattern.

Not a SIEM session. Not a site ticket. Not “hunt persistence.”

**Speaker Notes:**  
This slide is the student intro. An unbounded look is not a hunt. Get the four pieces on paper before anyone opens a query.

---

### Slide 3 – Four pieces
**Title:** Four pieces of the hunt card

**Hypothesis** — if X is true, we should see Y.  
**Scope** — where, how long, which telemetry.  
**Priority** — why this hunt now.  
**Unique pattern** — specific enough to search internally.

**Speaker Notes:**  
A hypothesis is testable if/then, not a topic. Scope is not every log source. Priority is not a blog. Unique pattern is not “any Run key.”

---

### Slide 4 – What good looks like
**Title:** What good looks like

**Hypothesis:** If A12 persistors exist elsewhere, we see HKCU Run **`Updater`** → `%TEMP%\update.exe`.  
**Scope:** User workstations, last 14 days, registry and file events.  
**Priority:** Open A12 incident plus the missed `GET /update.exe` download.  
**Pattern:** Value name **`Updater`**, not any Run key.

**Speaker Notes:**  
Walk this A12 card before the knowledge check. Four lines. Do not write the SIEM query. The missed download is a false negative, not a fired alert they dislike.

---

### Slide 5 – Not this lesson
**Title:** Not this lesson

No SIEM session (**3.3.1**).  
No local template or ticket (**3.7.2**).  
No “hunt persistence” (**3.6.3**).

**Speaker Notes:**  
Keep them on the four-line card. Tools are next. Site forms and named-technique hunts come later.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A hunt card is “search everything for malware.” True or false?  
2. What four pieces does the hunt card have?  
3. Write a one-line **A12** hypothesis and one unique pattern (not “any Run key”).

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Hypothesis, scope, priority, unique pattern.  
Bound the search.  
The classroom card is training, not a ticket you invent.

**Next:** **3.3.1** Hunt tool capabilities

**Speaker Notes:**  
3.3.1 converts a hunt lead into a precise internal query. Do not open tools in this lesson.
