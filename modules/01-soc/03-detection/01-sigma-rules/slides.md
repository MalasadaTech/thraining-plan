# Module 1.3.1 – SIGMA Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.3.1 – SIGMA Rules  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Portable YAML. Propose, do not deploy. Not a SIEM product.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts **read** a detection and **propose** a basic one.

You do **not** deploy it. That is **4.x**.

**Speaker Notes:**  
1.2 was logs. This is syntax.

---

### Slide 3 – Structure
**Title:** Purpose and structure

**SIGMA** — write what to look for once.

Need **`logsource`**, **`detection`**, **`condition`**.

**Speaker Notes:**  
Outline a. Title helps a teammate. FP notes are hints.

---

### Slide 4 – Selectors and SIEM
**Title:** Selectors, then a query

**Selectors** — `endswith`, `contains`, lists. Fields must match the logsource.

**To SIEM** — logsource → table. Selections → `where`. Condition → and/or/not.

**Speaker Notes:**  
Outline b–c. Image/CommandLine = 1.1.2. No converter lab.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No Suricata. No YARA.  
No alert queue (**1.4**).  
No production push.

**Speaker Notes:**  
SOC 1a/2b/3c on create.

---

### Slide 6 – What good looks like
**Title:** Read it. Propose a basic one.

**Given:** `process_creation`, `powershell.exe`, `-enc`, parent `wscript`.

**Detects:** encoded PowerShell from a script host.

A modify adds a selector. “Any PowerShell” is too broad.

**Speaker Notes:**  
Same story as 1.1.2. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. SIGMA is a SIEM product. True or false?  
2. The given rule — what does it detect, in one sentence?  
3. Why is a rule that matches every `powershell.exe` a poor proposal?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Portable YAML: logsource, selectors, condition.  
Becomes a SIEM query.  
You propose. You do not deploy.

**Next:** **1.3.2** Suricata rules

**Speaker Notes:**  
Network rule syntax next.
