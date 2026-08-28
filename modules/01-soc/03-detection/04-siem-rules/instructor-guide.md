# Instructor Guide – Module 1.3.4 – SIEM Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.4.1 A / B / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 1a / 2b / 3c  
- Hunter: 1.3.4.1 B / C / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 2b / 3c / 4c  
- CTI: 1.3.4.1 A / B / B ; 1.3.4.2 1a / 2b / 3c ; 1.3.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a SIEM detection and propose a basic create from log fields or from SIGMA. Do not deploy it.

**Context (plain language):**

- What this lesson is for: SOC analysts read a saved SIEM detection and propose a basic one so they can say what that rule looks at — which table, which fields, which match — before they treat the alert as a fact.
- How it hooks to the lesson before: 1.3.3 was YARA (byte patterns on a file or in memory). This lesson is named logic on ingested logs.
- How it hooks to the lesson after: 1.4.1 is the alert that this object can create — context and investigation, not more syntax.
- Why we are doing it this way: name the saved SIEM object (structure, fields or a SIGMA wrap, wildcard vs regex) so the next lesson can open the alert.
- What we are *not* doing in this lesson: Deploy. Alert queue. Converter lab. Invented SIEM product names as policy. How detections run as a service (4.x). No lab.
- Extra step: none.

Use the same names as the student guide: **SIEM rule**, **analytics rule**, **correlation search**, **table**, **logic**, **window**, **output**, **wildcard**, **regex**, **SIGMA**, **logsource**, and **selector**. **Correlation search** means the saved detection, not a join. The given uses encoded PowerShell and parent `wscript`. Do not turn it into the intro plot.

**Key Teaching Points:**
- Name, table, logic, window, output.
- A table with no filter is not a detection.
- Fields that exist on that table, or a SIGMA wrap, then name / window / outputs.
- Wildcard or substring when the token is stable. Regex when it varies.
- SOC proposes. Detection engineering reviews.

**Common Student Challenges:**
- Treat an unfiltered table as a detection. Why: the table is the log store, not the rule. Example: proposing `DeviceProcessEvents` with no filter.
- Regex a fixed token. Why: regex is for when the token varies. Example: a regex for `-enc` when a substring is enough.
- Put a field on the wrong table. Why: fields belong to that log source. Example: `uri` on `DeviceProcessEvents`.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.3.4.1 – SIEM rules
- T: 1.3.4.2 – Analyze an existing SIEM rule and describe what it detects
- T: 1.3.4.3 – Create a basic SIEM detection rule from log fields or a SIGMA rule

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Saved rule, not the alert |
| Key Concepts            | 16 min    | Structure, fields or SIGMA, match |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a rule, and you have to say what that rule looks at.
- Walk name, table, logic, window, and output. A table with no filter is not a detection. Correlation search means the saved detection, not a requirement to join.
- From fields: name the table, pick fields that exist on it, add a parent or token so it is not “all PowerShell.”
- From SIGMA: logsource to table, selectors to logic, then wrap with name, window, and outputs. They are not required to run a converter.
- Wildcard or substring when the path or token is stable. Regex when the token varies.
- Walk the given: `DeviceProcessEvents`, powershell, `-enc`, parent `wscript`, 5-minute window. One sentence: process create of PowerShell with `-enc` and parent `wscript`.
- If they open the alert console: that is 1.4.
- If they want to deploy: that is 4.x.
- If they put `uri` on `DeviceProcessEvents`: that field is not on this table.

---

## Knowledge Check – Answer Key

1. **A SIEM table with no filter is a detection. True or false?**  
   **Answer:** False. You need logic (and a name, window, and outputs).  
   **Explanation:** The table is the log store. A detection is named logic on that table.

2. **The given rule — what does it detect?**  
   **Answer:** Process create of PowerShell with `-enc` and parent `wscript`.  
   **Explanation:** Table, three predicates, and window are what fire. Do not narrate the rest of an incident.

3. **When do you use a wildcard instead of a regex?**  
   **Answer:** When a substring or path is enough. Regex when the token itself varies.  
   **Explanation:** `-enc` as a fixed token is a wildcard or substring. `-e` / `-enc` / `-EncodedCommand` is regex.

---

## Additional Instructor Resources

- Next: 1.4.1 Alert context and investigation
