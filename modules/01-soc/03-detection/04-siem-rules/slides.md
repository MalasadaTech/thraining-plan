# Module 1.3.4 – SIEM Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.3.4 – SIEM Rules  
**Subtitle:** Named logic that can fire an alert  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is the saved SIEM detection: named logic on ingested logs. Students read one and propose a basic one. They do not deploy it, and they do not open the alert console.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

An alert names a **rule**.

SOC analysts **read** that saved detection and **propose** a basic one, so they can say what the rule looks at before they treat the alert as a fact.

You propose. You do not deploy. Opening the alert is **1.4**.

**Speaker Notes:**  
This slide is the student intro. The job is the saved rule, not the alert queue and not a production push. The next slides name the pieces of that rule.

---

### Slide 3 – Name, table, logic, window, output
**Title:** Name, table, logic, window, output

A **SIEM rule** (analytics rule / **correlation search**) is named logic that can fire an alert.

**Name. Table. Logic. Window. Output fields.**

A table with no filter is not a detection.

A join or count in a window is extra. A basic rule can be a filter on one table.

**Speaker Notes:**  
Correlation search means the saved detection, not a requirement to join events. Stay on structure. Fields and the SIGMA wrap are the next slide.

---

### Slide 4 – From fields or from SIGMA
**Title:** From fields or from SIGMA

**From fields** — name the table. Pick fields that exist on it. Add a parent, token, or destination so it is not “all PowerShell.”

**From SIGMA** — logsource → table, selectors → logic, condition → and/or/not. Then name it, give it a window, list outputs.

You are not required to run a converter.

**Speaker Notes:**  
Two legal creates: from log fields you already know, or by wrapping a SIGMA rule. Same destination object. Map SIGMA; do not re-teach YAML as a new format.

---

### Slide 5 – Wildcard vs regex
**Title:** Wildcard vs regex

**Wildcard** (or substring) — when a path or fixed token is enough (`*\\Temp\\*`, `-enc`).

**Regex** — when the token itself varies (`-e` / `-enc` / `-EncodedCommand`).

Do not regex an empty field into existence.

**Speaker Notes:**  
This is matching on SIEM fields, not byte patterns on a file. If the string is stable, a wildcard or substring is enough. Regex is for variation.

---

### Slide 6 – Read it. Propose a basic one.
**Title:** Read it. Propose a basic one.

**Given:** `DeviceProcessEvents`, powershell, `-enc`, parent `wscript`, 5-minute window.

**Detects:** process create of PowerShell with `-enc` and parent `wscript`.

An unfiltered table is not a create. SOC proposes. Detection engineering reviews.

**Speaker Notes:**  
Walk the given from the student guide before the knowledge check. One sentence for what it detects. Do not tell the intro plot. Do not open the alert.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A SIEM table with no filter is a detection. True or false?  
2. The given rule — what does it detect, in one sentence?  
3. When do you use a wildcard instead of a regex?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Named logic on a table, in a window, with outputs.  
From fields or from SIGMA.  
You propose. You do not deploy.

**Next:** **1.4.1** Alert context and investigation

**Speaker Notes:**  
The next lesson is the alert that this object can create, not more rule syntax.
