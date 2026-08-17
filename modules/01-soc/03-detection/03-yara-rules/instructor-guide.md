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

- What this hour is for: SOC analysts match bytes on a file they already have (or memory the shop already scans).
- How it hooks to the hour before: 1.3.2 was the network signature for GET /update.exe. This hour is the file bytes from 1.2.7.
- How it hooks to the hour after: 1.3.4 is SIEM — log fields or a SIGMA rule, not bytes.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d only. SOC create is 1a/2b/3c.
- What we are *not* doing this hour: Memory dump how-to. Malware writing. Night Owl strings. Deploy. No lab.
- Extra step: none.

Use `update.exe` + MZ. Hex is `{ 4D 5A }` only. Do not tell the PRD plot.

**Key Teaching Points:**
- meta / strings / condition.
- ASCII, hex, regex — different syntax from Suricata.
- File vs memory conditions.
- MZ-only is too broad.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.3.3.1 ; T 1.3.3.2 ; T 1.3.3.3

---

## Suggested Timing

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

Walk the three blocks. Read the given rule. Contrast with MZ-only.

If they open Suricata hex: “Different syntax. Braces here.”  
If they want to dump LSASS: “Not this hour.”  
If the shop has no memory YARA: “Say so. Stay on files.”

---

## Knowledge Check – Answer Key

1. **YARA is a SIEM query language. True or false?**  
   **Answer:** False. It matches byte patterns in a file or in memory.  
   **Explanation:** Outline a.

2. **The given rule — what does it detect?**  
   **Answer:** A file that starts with MZ and contains update.exe, under 5 MB.  
   **Explanation:** Outline b–d and 1.3.6 task 1.

3. **Why is MZ at 0 alone a poor proposal?**  
   **Answer:** Every PE matches, including Notepad. Add a distinctive string or other check.  
   **Explanation:** Outline b / 1.3.6 task 2.

---

## Additional Instructor Resources

- Next: 1.3.4 SIEM rules
