# Instructor Guide – Module 1.3.4 – SIEM Rules

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.4.1 A / B / C · 1.3.4.2 2b / 3c / 4c · 1.3.4.3 1a / 2b / 3c  
- Hunter: 1.3.4.1 B / C / C · 1.3.4.2 2b / 3c / 4c · 1.3.4.3 2b / 3c / 4c  
- CTI: 1.3.4.1 A / B / B · 1.3.4.2 1a / 2b / 3c · 1.3.4.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read a SIEM detection / correlation search, build one from **fields** or from **SIGMA**, and use wildcards/regex on purpose. Close unit **1.3**. Do not open **1.4**.

**Key Teaching Points:**
- Name, table, logic, window, output.
- Fields → filters (+ optional count/join).
- Wildcard vs regex.
- SIGMA → table + `where` + wrap as a named rule.
- SOC create **1a / 2b / 3c**. Propose, do not deploy.

**Common Student Challenges:**
- Unfiltered table as a “rule.”
- Regex for a simple suffix.
- Leaving SIGMA `uri` on `DeviceProcessEvents`.
- Writing the alert-triage playbook.
- Asking how to click Publish in the SIEM.
- Grading SOC 3 as detection engineer.

**Required Materials:**
- Student Guide
- Slide Deck
- 1.3.1 Example 1 YAML (or the student guide copy)
- Answer key (this guide)

---

## Learning Objectives

1. Explain SIEM rule / correlation structure.
2. Turn log fields into detections; regex vs wildcards.
3. Analyze an existing SIEM rule.
4. Create a basic rule from fields **or** SIGMA (propose only).

**Mapped Items:**
- K: 1.3.4.1 – SIEM rules
- T: 1.3.4.2 – Analyze an existing SIEM rule
- T: 1.3.4.3 – Create a basic SIEM detection from log fields or a SIGMA rule

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Last 1.3 unit |
| Structure                      | 10 min   | a |
| Fields, regex/wildcards, SIGMA | 14 min   | b–c + task 2 paths |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | One path is enough |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Close 1.3 → 1.4 |
| **Total**                      | **~70 min** | Stretch Example 2 if they ship no-filter |

---

## Detailed Teaching Notes

### 1. Structure

**Talking Points:**
- Same 3/5/7 split. CTI create 1a / 1a / 2b.
- Correlation = optional join/threshold. Single-table rules count.
- Window is part of the rule. 24h no-filter is a warehouse, not a detection.

**Question to ask:**  
“What table, and what would an analyst see in the output?”

### 2. Fields, matching, SIGMA

**Talking Points:**
- Walk b–c. Map SIGMA selectors live if they have 1.3.1 notes.
- Wildcard for `\Temp\` and `*.exe`. Regex only for `-e` / `-enc` / `-EncodedCommand` style variation.
- Task 2 accepts **either** path. Do not require both.

**Question to ask:**  
“Did you need a regex, or would `has` / `endswith` do?”

### 3. Examples

**Example 1:** SIGMA → SIEM. Gold path.  
**Example 2:** No filter.  
**Example 3:** Field-based wildcard + count. Untuned threshold = lead.

---

## Hands-On Exercise – Instructor Guidance

**How to run:** 14–16 minutes. Either create path passes. Fail deploy. Fail 1.4 playbook.

**Summaries:**
- Example 1: Encoded PS from script host; from SIGMA; expected as a rule.
- Example 2: All DeviceProcessEvents / 24h; not a detection; lead.
- Example 3: GET `*.exe` count by orig; field-based; lead if threshold untested.

**Office to shell analysis:**  
`DeviceProcessEvents`, 5 min. Parent Office, child cmd/powershell. Fires on Office → shell. No `-enc` required. Output not listed — call that a gap.

**Create — from fields (equivalent is fine):**

```
Name: PowerShell UA POST
Source: Zeek http
Window: 5 minutes
Logic: method == "POST" and user_agent has "PowerShell"
Output: ts, uid, id.orig_h, host, uri, user_agent
```

**Create — from SIGMA (equivalent is fine):**

```
Name: Office Spawns Cmd
Source: DeviceProcessEvents
Window: 5 minutes
Logic:
  InitiatingProcessFileName in ("winword.exe","excel.exe","outlook.exe")
  and FileName in ("cmd.exe","powershell.exe")
Output: Timestamp, DeviceName, FileName, ProcessCommandLine,
        InitiatingProcessFileName
```

Matching note: `has "PowerShell"` = substring, not regex. `matches @"*.exe*"` = wildcard.

SOC 3 pass: names table + two field filters + a window. SOC 5: coherent proposal + output fields.

---

## Knowledge Check – Answer Key

1. **Pieces?**  
   **Answer:** Name/description, source table, logic (filters / join / threshold), time window / schedule, output fields (and severity).  
   **Explanation:** Outline a.

2. **Fields → detection?**  
   **Answer:** Pick the table, constrain the fields you already know, add enough specificity (and optional count/join) that it is not “all events.”  
   **Explanation:** Outline b.

3. **Wildcard vs regex?**  
   **Answer:** Wildcard / `has` for a simple path or suffix. Regex when the token actually varies. Do not regex an `endswith`.  
   **Explanation:** Outline c.

4. **From SIGMA?**  
   **Answer:** logsource → table, selectors → `where`, condition → boolean, then wrap with name, window, and outputs.  
   **Explanation:** Task 2 + 1.3.1.

5. **Deploy? Unfiltered table?**  
   **Answer:** DE deploys. SOC proposes (1a / 2b / 3c). A table with no logic matches everything and is not a detection.  
   **Explanation:** Example 2 + matrix.

---

## Additional Instructor Resources

- Local analytics-rule template / required output fields
- Next recommended module: 1.4.1 Alert context and investigation
