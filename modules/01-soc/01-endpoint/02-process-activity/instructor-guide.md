# Instructor Guide – Module 1.1.2 – Process Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.2.1 A / B / C ; 1.1.2.2 2b / 3c / 4c ; 1.1.2.3 2b / 3c / 4c  
- Hunter: 1.1.2.1 A / B / B ; 1.1.2.2 1a / 2b / 3c ; 1.1.2.3 1a / 2b / 3c  
- CTI: 1.1.2.1 A / A / A ; 1.1.2.2 1a / 1a / 1a ; 1.1.2.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a host process row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read host process rows to see who ran what. This hour is that row — create, terminate, or who touched whom.
- How it hooks to the hour before: 1.1.1 named the five kinds of host rows. This hour is the process row.
- How it hooks to the hour after: 1.1.3 is file activity on the same host telemetry.
- Why we are doing it this way: You wanted section 1 revised to the short 0.x / 4.x voice. Tasks stay as what good looks like. No lab this pass.
- What we are *not* doing this hour: Zeek (1.2). Sysmon install. File / registry / image-load units. Persistence how-to (2.6). No lab.
- Extra step: none.

Say **create**, **terminate**, **process access**, and **command line** the way the student guide does. MDE `ActionType` on this table: **ProcessCreated**, **OpenProcess**. Do not invent `ProcessTerminated` here — terminate is Sysmon 5. `jlee` / Temp `invoice.vbs` is course fiction for the given — do not tell the PRD plot.

**Key Teaching Points:**
- Endpoint row, not Zeek.
- Command line and parent are the story. Name can lie.
- Event 10 is who touched whom, not a start.
- A query is specific, not “all processes.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.1.2.1 ; T 1.1.2.2 ; T 1.1.2.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Host row, not Zeek |
| Key Concepts            | 16 min    | Fields a–g; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk the field table. Stop on Event 10: not a create.

If they start installing Sysmon: “Not this hour.”  
If they open a file path as the story: “1.1.3. Stay on the process row.”  
If they write `process=*` : “Not specific.”

---

## Knowledge Check – Answer Key

1. **Event 10 is a process start. True or false?**  
   **Answer:** False. It is process access — who touched whom.  
   **Explanation:** Outline f.

2. **wscript (Temp vbs) → powershell -enc. What occurred?**  
   **Answer:** Script host launched hidden encoded PowerShell. Parent + command line is the story.  
   **Explanation:** Outline a–c and 1.1.2.1 task 1.

3. **A query that matches every process is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (parent + command-line fragment).  
   **Explanation:** 1.1.2.1 task 2.

---

## Additional Instructor Resources

- Next: 1.1.3 File system activity
