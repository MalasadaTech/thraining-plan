# Instructor Guide – Module 1.1.3 – File System Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.3.1 A / B / C ; 1.1.3.2 2b / 3c / 4c ; 1.1.3.3 2b / 3c / 4c  
- Hunter: 1.1.3.1 A / B / B ; 1.1.3.2 1a / 2b / 3c ; 1.1.3.3 1a / 2b / 3c  
- CTI: 1.1.3.1 A / A / A ; 1.1.3.2 1a / 1a / 1a ; 1.1.3.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a host file row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read host file rows to see what happened to a file, where, and by which process.
- How it hooks to the hour before: 1.1.2 was the process row (`wscript` launched encoded PowerShell). This hour is the file row on the same host telemetry.
- How it hooks to the hour after: 1.1.4 is host-observed network on that same host — not Zeek.
- Why we are doing it this way: Short 0.x / 4.x voice. Tasks stay as what good looks like. No lab this pass.
- What we are *not* doing this hour: Zeek `files` / `conn` (1.2). Sysmon install. Process create write-up (1.1.2). Persistence how-to (2.6). No lab.
- Extra step: none.

Say **create**, **rename-move**, **delete**, and **initiating process** the way the student guide does. Do not invent MDE `ActionType` values. `wscript` / Temp `update.exe` continues the 1.1.2 given — do not tell the PRD plot.

**Key Teaching Points:**
- Endpoint file row, not Zeek.
- Event 11 is create, not rename. 23 / 26 are delete.
- Path + initiator are the story. Empty hash is a gap.
- A query is specific, not “all file events.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.1.3.1 ; T 1.1.3.2 ; T 1.1.3.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | File row, not process, not Zeek |
| Key Concepts            | 16 min    | Fields a–e; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk the field table. Stop on Event 11: create, not rename.

If they start installing Sysmon: “Not this hour.”  
If they describe the process create of `wscript`: “1.1.2. Stay on the file row.”  
If they open Zeek `files`: “1.2.”  
If they write `DeviceFileEvents` with no filter: “Not specific.”

---

## Knowledge Check – Answer Key

1. **Event 11 is a rename. True or false?**  
   **Answer:** False. It is file create. Rename-move is an MDE `FileRenamed` when logged.  
   **Explanation:** Outline a / e.

2. **wscript → Temp update.exe (Sysmon 11, no hash). What occurred?**  
   **Answer:** Script host created `update.exe` under Temp. Hash not logged.  
   **Explanation:** Outline a–d and 1.1.3.1 task 1.

3. **A query that matches every file event is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (initiator + path + extension).  
   **Explanation:** 1.1.3.1 task 2.

---

## Additional Instructor Resources

- Next: 1.1.4 Network activity (endpoint)
