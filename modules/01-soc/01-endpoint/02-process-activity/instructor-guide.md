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
Read a host process event and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read process events on a host to see who ran what — create, terminate, or who touched whom.
- How it hooks to the lesson before: 1.1.1 named the five kinds of host activity. This lesson is the process kind.
- How it hooks to the lesson after: 1.1.3 is file activity on the same host telemetry.
- Why we are doing it this way: after naming the kinds, read one kind so you can describe who ran what before you open file or network events.
- What we are *not* doing in this lesson: Zeek (1.2). Sysmon install. File, registry, or image-load write-ups. Persistence how-to. No lab.
- Extra step: none.

Use the same names as the student guide: **create**, **terminate**, **process access**, and **command line**. MDE `ActionType` on this table: **ProcessCreated**, **OpenProcess**. Do not invent `ProcessTerminated` here — terminate is Sysmon 5. The given uses course-fiction names (`jlee`, Temp `invoice.vbs`). Do not turn it into the intro plot.

**Key Teaching Points:**
- Endpoint process event, not Zeek.
- Command line and parent are what you write down. The image name can be fake.
- Event 10 is who touched whom, not a start.
- A query is specific, not “all processes.”

**Common Student Challenges:**
- Treat Event 10 as a process start. Why: Event 1 is create; 10 is a handle open. Example: writing “powershell started” from an Event 10.
- Write `process=*` as a “specific” query. Why: the task is a named pattern. Example: `DeviceProcessEvents` with no parent or command-line filter.
- Describe the file path as the process story. Why: the file is 1.1.3. Example: “malware dropped in Temp” when the event is `wscript` creating PowerShell.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.1.2.1 – Process activity concepts
- T: 1.1.2.2 – Analyze a process event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.2.3 – Create a SIEM query to detect specific process activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Process event, not Zeek |
| Key Concepts            | 16 min    | Fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a host, and you have to say who ran what.
- Walk the field table. Stop on Event 10: it is not a create.
- MDE create is `ProcessCreated`. Terminate is Sysmon 5. Do not invent `ProcessTerminated` on `DeviceProcessEvents`.
- Walk the given: `wscript.exe` → `powershell.exe -enc …` as `jlee`. One sentence. Parent + command line.
- If they start installing Sysmon: that is not this lesson.
- If they open a file path as the story: that is 1.1.3. Stay on the process event.
- If they write `process=*`: that is not a specific query.

---

## Knowledge Check – Answer Key

1. **Event 10 is a process start. True or false?**  
   **Answer:** False. It is process access — who touched whom.  
   **Explanation:** Sysmon 1 is a create. Event 10 is a handle open from one process to another.

2. **wscript (Temp vbs) → powershell -enc. What occurred?**  
   **Answer:** Script host launched hidden encoded PowerShell. Parent + command line is what you write down.  
   **Explanation:** The image name of `powershell.exe` can still look fine. The parent and the `-enc` command line are the event.

3. **A query that matches every process is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (parent + command-line fragment).  
   **Explanation:** “All processes” is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.1.3 File system activity
