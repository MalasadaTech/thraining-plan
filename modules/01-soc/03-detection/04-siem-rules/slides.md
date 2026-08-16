# Module 1.3.4 – SIEM Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.3.4 – SIEM Rules  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Last 1.3 unit. Propose detections. Alerts are 1.4.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Explain SIEM detection / correlation structure
2. Turn log fields into detections (wildcards / regex)
3. Analyze an existing SIEM rule
4. Create a *basic* rule from **fields** or from **SIGMA**

**Mapped Items:**  
K: 1.3.4.1 | T: 1.3.4.2 | T: 1.3.4.3

**Speaker Notes:**  
SOC create is 1a/2b/3c. Either create path is enough.

---

### Slide 3 – Agenda
**Title:** Agenda

- Structure
- Fields → detections
- Regex vs wildcards
- From SIGMA
- Three worked examples
- Analyze + create
- Knowledge check — close 1.3

**Speaker Notes:**  
1.4 is next unit.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Clicking Publish / deploy  
Alert triage and PCAP (**1.4**)  
Rewriting SIGMA YAML (**1.3.1** already did)  
“All process events” as a rule

**Key Point:** Name, table, logic, window, output.

**Speaker Notes:**  
Park the SIEM admin UI.

---

### Slide 5 – Structure
**Title:** Detection / Correlation Search

Name / description  
**Table**  
**Logic** (filter, join, threshold)  
**Window** / schedule  
**Output** fields  

Correlation = optional join or count. Single-table still counts.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Fields → Detections
**Title:** Turning Log Fields into Detections

1. Table  
2. Fields you already know  
3. Specificity (parent, token, path)  
4. Optional count / join  
5. Output for the analyst  

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Wildcards vs Regex
**Title:** Two Matching Techniques

**Wildcard / has** — `\Temp\`, `*.exe`  
**Regex** — `-e` / `-enc` / `-EncodedCommand`  

Do not regex an `endswith`.  
Empty field → do not invent it.

**Speaker Notes:**  
Outline c.

---

### Slide 8 – From SIGMA
**Title:** SIGMA → Named SIEM Rule

logsource → table  
selectors → `where`  
condition → boolean  
Then: **name, window, outputs**

Converter tools optional. Mapping is the obligation.

**Speaker Notes:**  
Task 2 second path.

---

### Slide 9 – Example 1: From SIGMA
**Title:** Example 1 – Encoded PS from Script Host

- `DeviceProcessEvents`
- FileName + `-enc` + script-host parent

**Interpretation:**  
Expected *as a rule*. Mapped from 1.3.1 Ex 1.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: No Filter
**Title:** Example 2 – All Process Events

- Table only, 24-hour window

**Interpretation:**  
Not a detection. Lead about the rule.

**Speaker Notes:**  
Ask what to add.

---

### Slide 11 – Example 3: Fields + Wildcard
**Title:** Example 3 – GET *.exe count

- Zeek `http`, `method` + URI wildcard
- `count_ > 1` per orig

**Interpretation:**  
Good field start. Threshold may be noisy.

**Speaker Notes:**  
Wildcard, not regex.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Unfiltered table  
- Regex for a suffix  
- SIGMA `uri` on a process table  
- Writing the 1.4 playbook  
- Asking to publish  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Proposal Ideas
**Title:** Useful Starting Points

- 1.3.1 encoded-PS SIGMA → DeviceProcessEvents  
- http POST + PowerShell UA  
- Office → cmd / powershell  
- Always: table + two fields + window + outputs  

**Speaker Notes:**  
Local naming later.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize each example.
2. Analyze “Office to shell.”
3. Create **one** rule: from **http fields** **or** from Office-Spawns-Cmd SIGMA.
4. Wildcard, regex, or neither — why?

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Pieces of a SIEM detection?
2. Fields → detection — what are the steps?
3. Wildcard vs regex?
4. How do you build from SIGMA?
5. Who deploys? Why not an unfiltered table?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Name, table, logic, window, output.
- From fields or from SIGMA.
- Wildcard vs regex on purpose.
- Propose only. Unit **1.3** ends. Next: **1.4** Alerts.

**Speaker Notes:**  
Do not open a 1.4 lab unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** SIEM Rules — Quick Reference

| Need | Look at |
|------|---------|
| What / where | name + table |
| Logic | fields + optional count/join |
| When | window |
| Analyst | output fields |
| From SIGMA | table + `where` + wrap |

**Coming next:** Module 1.4.1 – Alert context and investigation

**Footer:** SOC / Hunter / CTI Training Program
