# Module 1.3.3 – YARA Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.3.3 – YARA Rules  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Byte patterns. Propose, do not deploy. Not SIGMA. Not Suricata.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts **read** a byte-pattern rule and **propose** a basic one.

Scan a file you already have (**1.2.7**), or memory the shop already collects.

**Speaker Notes:**  
Do not dump memory this hour.

---

### Slide 3 – Structure
**Title:** Purpose and structure

**YARA** — match bytes in a file or in memory.

Need **`strings`** and a real **`condition`**.  
**`meta`** is notes, not the match.

**Speaker Notes:**  
Outline a. `condition: true` is not a proposal.

---

### Slide 4 – Matching and where
**Title:** ASCII, hex, regex; file vs memory

**ASCII** — `"update.exe" ascii nocase`.  
**Hex** — `{ 4D 5A }` (`MZ`).  
**Regex** — `/pattern/`. Easy to over-match.

**File** — `at 0` and `filesize` can apply.  
**Memory** — usually drop those.

**Speaker Notes:**  
Outline b–d. Same three techniques as Suricata, different syntax.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No memory-acquisition how-to.  
No YARA on a log row.  
No production push.

**Speaker Notes:**  
SIEM next.

---

### Slide 6 – What good looks like
**Title:** Read it. Propose a basic one.

**Given:** MZ at 0 **and** `"update.exe"`, `filesize < 5MB`.

**Detects:** a PE that contains that name. Fits the **1.2.7** extract.

`MZ at 0` alone matches Notepad.

**Speaker Notes:**  
Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. YARA is a SIEM query language. True or false?  
2. The given rule — what does it detect, in one sentence?  
3. Why is `{ 4D 5A } at 0` alone a poor proposal?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Meta + strings + condition.  
ASCII / hex / regex.  
File vs memory.  
You propose. You do not deploy.

**Next:** **1.3.4** SIEM rules

**Speaker Notes:**  
Log fields or a SIGMA rule next.
