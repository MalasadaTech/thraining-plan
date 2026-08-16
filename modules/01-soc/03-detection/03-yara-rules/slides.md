# Module 1.3.3 – YARA Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.3.3 – YARA Rules  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Bytes in a file or memory. No dump lab. Propose, don’t deploy.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Explain purpose and `meta` / `strings` / `condition`
2. Read ASCII, hex, and regex strings
3. File scan vs memory scan
4. Analyze an existing rule
5. Create or modify a *basic* rule

**Mapped Items:**  
K: 1.3.3.1 | T: 1.3.3.2 | T: 1.3.3.3

**Speaker Notes:**  
SOC create is 1a/2b/3c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose and structure
- Strings and conditions
- Files vs memory
- Three worked examples
- Analyze + create/modify
- Knowledge check

**Speaker Notes:**  
1.3.4 SIEM is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

SIGMA / Suricata syntax  
How to dump process memory  
Malware authoring  
Host Event 11 as “the YARA hit”  
Deploying the rule pack

**Key Point:** Read the rule. Propose a basic pattern.

**Speaker Notes:**  
Park dump questions.

---

### Slide 5 – Purpose
**Title:** What YARA Is

- Pattern match on **bytes**
- Scan a file or memory your site already has
- Not a log query. Not a packet signature.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Structure
**Title:** meta, strings, condition

`rule Name { meta: ... strings: ... condition: ... }`

**meta** — notes, not a match  
**strings** — `$mz`, `$s1`  
**condition** — when it fires  

**Analyst Tip:** Strings without a real condition are not a proposal.

**Speaker Notes:**  
Outline a/b.

---

### Slide 7 – ASCII, Hex, Regex
**Title:** Three Matching Techniques

| Kind | YARA shape |
|------|------------|
| ASCII | `$s = "update.exe" ascii nocase` |
| Hex | `$mz = { 4D 5A }` |
| Regex | `$r = /checkin\.[a-z0-9-]+/` |

Different syntax from Suricata. Same three words.

**Speaker Notes:**  
Outline c.

---

### Slide 8 – Files vs Memory
**Title:** How YARA Is Used

**File** — extract (**1.2.7**), disk path → `at 0`, `filesize` OK  
**Memory** — process space your platform scans → often **drop** `at 0` / `filesize`  

If the tenant has no memory YARA, say so.

**Speaker Notes:**  
Outline d. No dump demo.

---

### Slide 9 – Example 1: Useful File
**Title:** Example 1 – MZ + update.exe

- `$mz at 0 and $name and filesize < 5MB`

**Interpretation:**  
Useful file rule. Expected *as a rule*. Not a verdict.

**Speaker Notes:**  
Tie to 1.2.7 Ex 2.

---

### Slide 10 – Example 2: MZ Only
**Title:** Example 2 – Any PE

- `{ 4D 5A }` at 0 only

**Interpretation:**  
Lead about the rule. Notepad matches.

**Speaker Notes:**  
Hex is fine. Condition is not.

---

### Slide 11 – Example 3: Target Matters
**Title:** Example 3 – nightowl string

- String-only condition
- File **or** memory depending on the scanner

**Interpretation:**  
Say the target. Do not bolt `at 0` onto a memory scan.

**Speaker Notes:**  
Students pick a target.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- MZ-only  
- File conditions on memory  
- Regex that matches everything  
- Asking how to dump memory  
- Treating YARA as SIGMA  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Proposal Ideas
**Title:** Useful Starting Points

- MZ + distinctive name (`update.exe`, `invoice.jpg`)  
- Distinctive domain string  
- Always: `meta.description` + a size cap on **file** rules  

**Speaker Notes:**  
No packer/exploit lab.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize each example.
2. Analyze MZ + `invoice.jpg`.
3. Modify Example 2 **or** create MZ + one training string + filesize.
4. File vs memory: what would you drop?

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. YARA vs SIGMA vs Suricata?
2. meta / strings / condition?
3. ASCII vs hex vs regex in YARA?
4. File vs memory conditions?
5. Who deploys? Why not MZ-only?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Bytes: meta + strings + condition.
- ASCII / hex / regex.
- File ≠ memory in the condition.
- Propose only. Next: SIEM rules (**1.3.4**).

**Speaker Notes:**  
Do not open a SIEM lab unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** YARA — Quick Reference

| Need | Look at |
|------|---------|
| Notes | `meta` |
| Patterns | `strings` |
| Logic | `condition` |
| File | `at 0`, `filesize` |
| Memory | string-first; drop file offsets |

**Coming next:** Module 1.3.4 – SIEM rules

**Footer:** SOC / Hunter / CTI Training Program
