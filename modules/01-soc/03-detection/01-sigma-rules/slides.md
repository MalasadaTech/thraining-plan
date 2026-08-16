# Module 1.3.1 – SIGMA Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.3.1 – SIGMA Rules  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Portable YAML. Propose, do not deploy. SOC create is 1a/2b/3c.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Explain SIGMA purpose and structure
2. Read fields / selectors
3. Describe how SIGMA becomes a SIEM query
4. Analyze an existing rule
5. Create or modify a *basic* rule (propose only)

**Mapped Items:**  
K: 1.3.1.1 | T: 1.3.1.2 | T: 1.3.1.3

**Speaker Notes:**  
Do not grade SOC 3 as DE.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose and structure
- Selectors
- Translation to SIEM
- Three worked examples
- Analyze + create/modify
- Knowledge check

**Speaker Notes:**  
1.3.2 Suricata and 1.4 alerts are later.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Deploying to the SIEM  
`sigmac` / pipeline admin  
Suricata / YARA  
Alert triage (**1.4**)  
“Any PowerShell is a detection”

**Key Point:** Read the YAML. Propose a basic rule.

**Speaker Notes:**  
Park deploy questions.

---

### Slide 5 – Purpose
**Title:** What SIGMA Is

- Generic **YAML** detection
- Write once → translate to a SIEM query
- Not the SIEM, not Suricata, not YARA

**SOC:** propose. **DE:** review and deploy.

**Speaker Notes:**  
Ask: “If this is not a SIEM, why write it?”

---

### Slide 6 – Structure
**Title:** Required Blocks

`title` / `description`  
`logsource` — product / category / service  
`detection` — named selections  
`condition` — how selections combine  

Optional: `falsepositives`, `level`, `tags`

**Analyst Tip:** No logsource + condition = not a detection.

**Speaker Notes:**  
Outline a.

---

### Slide 7 – Selectors
**Title:** Fields / Selectors

`Image|endswith: '\powershell.exe'`  
`CommandLine|contains: '-enc'`  
Lists = OR inside the selection  
`condition: selection and not filter`

Field names must match the **logsource**.

**Speaker Notes:**  
Outline b. One regex mention, then stop.

---

### Slide 8 – Translation
**Title:** SIGMA → SIEM Query

1. `logsource` → table  
2. Selectors → `where`  
3. `condition` → and / or / not  
4. Filters → extra `where`

You write the **shape**. Authorship of the saved SIEM rule is **1.3.4**.

**Speaker Notes:**  
Outline c. Map Image → FileName live.

---

### Slide 9 – Example 1: Narrow
**Title:** Example 1 – Encoded PS from Script Host

- process_creation
- powershell + `-enc` + wscript/cscript parent

**Interpretation:**  
Useful, explainable. Expected *as a rule*.

**Speaker Notes:**  
Tie to 1.1.1 Example 2.

---

### Slide 10 – Example 2: Broad
**Title:** Example 2 – Any PowerShell

- Only `Image|endswith: '\powershell.exe'`

**Interpretation:**  
Lead about the **rule**. Modify before you propose it.

**Speaker Notes:**  
Students name what else to add.

---

### Slide 11 – Example 3: Wrong Field
**Title:** Example 3 – uri on process_creation

- `uri|contains: '/api/v1/beacon'`
- That field is **HTTP (1.2.5)**

**Interpretation:**  
Broken mapping. Lead.

**Speaker Notes:**  
Do not write Suricata here.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- SIGMA = already alerting  
- Any-PowerShell proposal  
- Zeek/HTTP fields on Windows process  
- Asking how to deploy  
- Opening 1.4  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Hunting / Proposal Ideas
**Title:** Useful SIGMA Starting Points

- Script host / Office → powershell / cmd  
- `-enc` / `-EncodedCommand`  
- User-writable path + `.exe` child  
- Always: logsource + a second selector  

**Speaker Notes:**  
Starting points. Local allow-lists later.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize each example.
2. Analyze “Office Spawns Cmd.”
3. Modify Example 2 **or** create script-host/Office → shell.
4. Translate your rule to a SIEM-shaped query.

**Speaker Notes:**  
Instructor Guide key. SOC 3 may use a template.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. What is SIGMA / not?
2. Three required blocks? What does logsource control?
3. What do `|endswith` / `|contains` do?
4. How does it become a SIEM query? Who deploys?
5. Why is “any PowerShell” a poor proposal?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- YAML detection: logsource + selectors + condition.
- Fields must match the logsource.
- Translate to a table + `where`. Do not deploy.
- SOC proposes (1a / 2b / 3c). Next: Suricata (**1.3.2**).

**Speaker Notes:**  
Do not open a Suricata lab unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** SIGMA — Quick Reference

| Need | Look at |
|------|---------|
| Telemetry | `logsource` |
| Tests | `detection` selections |
| Logic | `condition` |
| SIEM | table + `where` + boolean |

**Coming next:** Module 1.3.2 – Suricata rules

**Footer:** SOC / Hunter / CTI Training Program
