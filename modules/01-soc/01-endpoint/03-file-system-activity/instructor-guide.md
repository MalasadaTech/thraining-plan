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
Read a host file event and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read file events on a host to see what happened to a file, where, and by which process.
- How it hooks to the lesson before: 1.1.1 named the five kinds of host activity. 1.1.2 was the process kind. This lesson is the file kind on the same host telemetry.
- How it hooks to the lesson after: 1.1.4 is host-observed network on that same host — not Zeek.
- Why we are doing it this way: after process, read the file kind on the same host telemetry so you can describe what happened to the file before you open network events.
- What we are *not* doing in this lesson: Zeek `files` / `conn` (1.2). Sysmon install. Process-create write-up (1.1.2). Persistence how-to. No lab.
- Extra step: none.

Use the same names as the student guide: **create**, **rename-move**, **delete**, **modify**, **read**, and **initiating process**. MDE `ActionType` on this table: **FileCreated**, **FileRenamed**, **FileDeleted**, **FileModified**. Do not invent `FileRead` here — read is where that action is logged. The given continues the 1.1.2 names (`wscript`, Temp `update.exe`). Do not turn it into the intro plot.

**Key Teaching Points:**
- Endpoint file event, not Zeek.
- Event 11 is create, not rename. 23 / 26 are delete.
- Path + initiator are what you write down. Empty hash is a gap.
- A query is specific, not “all file events.”

**Common Student Challenges:**
- Treat Event 11 as a rename. Why: create and rename both put a new path on the event. Example: writing “file renamed to update.exe” from a Sysmon 11.
- Write `DeviceFileEvents` with no filter as a “specific” query. Why: the task is a named pattern. Example: every file event, no initiator or path.
- Describe the process create of `wscript` as the file story. Why: this lesson is what happened to the file. Example: “script host launched PowerShell” when the event is Sysmon 11 creating `update.exe`.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.1.3.1 – File system activity concepts
- T: 1.1.3.2 – Analyze a file event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.3.3 – Create a SIEM query to detect specific file operations

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | File event, not Zeek |
| Key Concepts            | 16 min    | Fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a host, and you have to say what happened to a file, where, and by which process.
- Walk the field table. Stop on Event 11: it is create, not rename.
- MDE create is `FileCreated`. Rename-move is `FileRenamed` when logged. Delete is Sysmon 23 / 26 and MDE `FileDeleted`. Do not invent `FileRead` on `DeviceFileEvents`.
- Walk the given: Sysmon 11, `wscript.exe` → Temp `update.exe`, no hash. One sentence. Path + initiator. Hash not logged.
- If they start installing Sysmon: that is not this lesson.
- If they describe the process create of `wscript`: that is 1.1.2. Stay on the file event.
- If they open Zeek `files`: that is 1.2.
- If they write `DeviceFileEvents` with no filter: that is not a specific query.

---

## Knowledge Check – Answer Key

1. **Event 11 is a rename. True or false?**  
   **Answer:** False. It is file create. Rename-move is an MDE `FileRenamed` when logged.  
   **Explanation:** Sysmon 11 is a create. Rename-move is a different action and is not Event 11.

2. **wscript → Temp update.exe (Sysmon 11, no hash). What occurred?**  
   **Answer:** Script host created `update.exe` under Temp. Hash not logged.  
   **Explanation:** Path and initiator are what you write down. A missing hash is a gap, not clean. The process create of `wscript` is a different event.

3. **A query that matches every file event is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (initiator + path + extension).  
   **Explanation:** “All file events” is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.1.4 Network activity (endpoint)
