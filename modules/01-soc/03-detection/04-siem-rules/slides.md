# Module 1.3.4 – SIEM Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.3.4 – SIEM Rules  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Last 1.3 hour. Named logic that can fire an alert. Propose, do not deploy.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts **read** a saved detection and **propose** a basic one.

Opening the alert is **1.4**. Deploy is **4.x**.

**Speaker Notes:**  
YARA was bytes. This is log fields.

---

### Slide 3 – Structure
**Title:** Name, table, logic, window, output

A table with no `where` is not a detection.

A join or count in a window is correlation — optional for a basic rule.

**Speaker Notes:**  
Outline a.

---

### Slide 4 – Fields, SIGMA, match
**Title:** From fields or from SIGMA

Table + fields you already know + specificity.

**SIGMA path** — logsource → table, selectors → `where`, then name it and give it a window.

**Wildcard** — path / substring.  
**Regex** — when the token varies.

**Speaker Notes:**  
Outline b–c. Same mapping as 1.3.1, then wrap it.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No alert console.  
No converter lab.  
No production push.

**Speaker Notes:**  
1.3 ends here.

---

### Slide 6 – What good looks like
**Title:** Read it. Propose a basic one.

**Given:** `DeviceProcessEvents`, powershell, `-enc`, parent `wscript`, 5-minute window.

**Detects:** the **1.1.2** process create. Mapped from the **1.3.1** SIGMA.

An unfiltered table is not a create.

**Speaker Notes:**  
Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A SIEM table with no filter is a detection. True or false?  
2. The given rule — what does it detect, in one sentence?  
3. When do you use a wildcard instead of a regex?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Named logic on a table, in a window, with outputs.  
From fields or from SIGMA.  
You propose. You do not deploy.

**Next:** **1.4.1** Alert context and investigation

**Speaker Notes:**  
1.3 is done. Alerts next.
