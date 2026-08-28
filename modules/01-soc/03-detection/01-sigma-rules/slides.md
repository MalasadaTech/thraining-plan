# Module 1.3.1 – SIGMA Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.3.1 – SIGMA Rules  
**Subtitle:** Read a detection. Propose a basic one.  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is portable YAML for what to look for. You read a rule and propose a basic create or modify. You do not deploy it. It is not a SIEM product.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

An alert comes from a **detection**. Someone wrote what to look for.

SOC analysts **read** that write-up and **propose** a basic create or modify.

The shop may not all use the same SIEM. SIGMA is how you write the idea once.

**Speaker Notes:**  
This slide is the student intro. You do not deploy the rule. How detections run as a service is 4.x. Suricata is the next lesson, not this one.

---

### Slide 3 – Purpose and structure
**Title:** Purpose and structure

**SIGMA** is a generic detection format. You write what to look for once.

A rule needs **title**, **logsource** (which telemetry), and **detection** (named selections plus a **condition**).

Without those, it is not a detection.

**Speaker Notes:**  
Condition lives inside detection. Do not add status, level, or false-positive notes as required blocks. Title is what a teammate reads.

---

### Slide 4 – Fields and selectors
**Title:** Fields and selectors

**Selectors** are field tests: `endswith`, `contains`, a list, `re`.

Field names must match the logsource.

`Image` / `CommandLine` on `process_creation` are process-create fields (**1.1.2**).

**Speaker Notes:**  
Tests in one selection are typically and. A list under one field is typically or. If they put uri on process_creation, that is the wrong logsource.

---

### Slide 5 – How SIGMA becomes a SIEM query
**Title:** How SIGMA becomes a SIEM query

**logsource** → table or event type.

Named selections → `where` tests.

**condition** → and / or / not.

Write that in words. Running a converter is not this lesson.

**Speaker Notes:**  
The product here is the shape of the query, not a saved SIEM object. Name, window, and output fields are 1.3.4.

---

### Slide 6 – Read it. Propose a basic one.
**Title:** Read it. Propose a basic one.

**Given:** `process_creation`, `powershell.exe`, `-enc`, parent `wscript`.

**Detects:** encoded PowerShell launched from a script host.

A **modify** adds a selector. “Any PowerShell” is too broad.

SOC **proposes**. Detection engineering reviews.

**Speaker Notes:**  
Same process story as 1.1.2. Walk the three selectors, then stop. Do not tell the intro plot. Tightening any powershell.exe by adding parent or -enc is the create/modify task.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. SIGMA is a SIEM product. True or false?  
2. A `process_creation` rule matches `powershell.exe`, CommandLine `-enc`, and parent `wscript`. In one sentence, what does it detect?  
3. Why is a rule that matches every `powershell.exe` a poor proposal?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

SIGMA is portable YAML: logsource, selectors, condition.  
It becomes a SIEM query.  
You propose. You do not deploy.

**Next:** **1.3.2** Suricata rules

**Speaker Notes:**  
Suricata is network rule syntax, not YAML. Stay off packets until that lesson.
