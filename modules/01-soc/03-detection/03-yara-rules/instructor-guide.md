# Instructor Guide – Module 1.3.3 – YARA Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.3.1 A / B / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 1a / 2b / 3c  
- Hunter: 1.3.3.1 B / C / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 2b / 3c / 4c  
- CTI: 1.3.3.1 A / B / B ; 1.3.3.2 1a / 2b / 3c ; 1.3.3.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a YARA rule and propose a basic create or modify. Do not deploy it.

**Context (plain language):**

- What this lesson is for: SOC analysts match byte patterns on a file they already have, or on memory the shop already scans. They read a YARA rule and propose a basic create or modify. They do not deploy it.
- How it hooks to the lesson before: 1.3.2 was the network signature for GET /update.exe. This lesson is the file bytes (a 1.2.7 extract, if you scan that object).
- How it hooks to the lesson after: 1.3.4 is SIEM — log fields or a SIGMA rule, not bytes.
- Why we are doing it this way: a log-field detection cannot see file bytes. After the wire signature, read the byte-pattern language so you can say what would hit a file you already have.
- What we are *not* doing in this lesson: Memory-acquisition how-to. Malware writing. Night Owl / PRD strings. Deploy. SIGMA or Suricata authoring. No lab.
- Extra step: none.

Use the same names as the student guide: **meta**, **strings**, **condition**, **ASCII**, **hex**, **regex**, **file**, and **memory**. Hex is `{ 4D 5A }` only. The given uses `update.exe` and MZ. Do not tell the PRD plot.

**Key Teaching Points:**
- YARA matches bytes in a file or in memory. It is not a SIEM query.
- Need `strings` and a real `condition`. `meta` is notes, not the match.
- ASCII, hex, and regex — same three techniques as Suricata, different syntax.
- File rules may use `at 0` and `filesize`. Process memory usually must not.
- MZ-only is too broad. SOC proposes. DE reviews.

**Common Student Challenges:**
- Treat YARA as a SIEM query. Why: SIGMA and SIEM sit next to this lesson. Example: writing a `DeviceProcessEvents` filter and calling it a YARA rule.
- Propose `{ 4D 5A } at 0` alone. Why: every PE starts with MZ. Example: a rule that would also hit Notepad.
- Copy Suricata hex into YARA. Why: both use hex. Example: putting `content:"|4d 5a|"` in a YARA `strings` block.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.3.3.1 – YARA rules
- T: 1.3.3.2 – Analyze an existing YARA rule and describe what it detects
- T: 1.3.3.3 – Create or modify a basic YARA rule

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Bytes, not logs |
| Key Concepts            | 16 min    | Structure, match, file vs memory |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a log can name a file; YARA is how you ask whether known bytes are in it.
- Walk the three blocks. `meta` does not match. A strings block with no real condition is not a proposal.
- Hex is braces `{ 4D 5A }`. If they paste Suricata `content:"|4d 5a|"`, stop and switch syntax.
- File vs memory: `filesize` does not apply on a process scan, so that rule will not match. MZ at offset 0 is a file-header check.
- Walk the given: MZ at 0 **and** `update.exe`, under 5 MB. One sentence. File rule, not a log match, not a conviction.
- Contrast with MZ-only: every PE, including Notepad.
- If they want to dump LSASS or write malware: that is not this lesson.
- If the shop does not scan memory: say so and stay on files.
- If they want to deploy: DE reviews. This lesson is propose.

---

## Knowledge Check – Answer Key

1. **YARA is a SIEM query language. True or false?**  
   **Answer:** False. It matches byte patterns in a file or in memory.  
   **Explanation:** YARA is not SIGMA and not a saved SIEM search. A log line is not the bytes.

2. **The given rule — what does it detect?**  
   **Answer:** A file that starts with MZ and contains `update.exe`, under 5 MB.  
   **Explanation:** `$mz at 0` is the PE header check. `$name` is the distinctive string. `filesize` means this is a file rule.

3. **Why is `{ 4D 5A } at 0` alone a poor proposal?**  
   **Answer:** Every PE matches, including Notepad. Add a distinctive string or other check.  
   **Explanation:** MZ at the start of the file is a file-type check, not a detection of `update.exe`. Tightening by adding that string is a modify.

---

## Additional Instructor Resources

- Next: 1.3.4 SIEM rules
