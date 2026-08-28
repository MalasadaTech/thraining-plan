# Instructor Guide – Module 1.1.6 – Image and Driver Load Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.6.1 A / B / C ; 1.1.6.2 2b / 3c / 4c ; 1.1.6.3 2b / 3c / 4c  
- Hunter: 1.1.6.1 A / B / B ; 1.1.6.2 1a / 2b / 3c ; 1.1.6.3 1a / 2b / 3c  
- CTI: 1.1.6.1 A / A / A ; 1.1.6.2 1a / 1a / 1a ; 1.1.6.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a host image or driver load event and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read image and driver load events on a host to see that a module entered a process, or that a driver entered the kernel.
- How it hooks to the lesson before: 1.1.5 was registry activity. This lesson is the image / driver load kind.
- How it hooks to the lesson after: 1.2 is Zeek — network-sensor telemetry, not another host event.
- Why we are doing it this way: after process, file, host-network, and registry, read the load kind so you can describe a module or driver load before you leave host telemetry for Zeek.
- What we are *not* doing in this lesson: File-create write-up (1.1.3). Persistence / BYOVD. Zeek (1.2). Sysmon install. No lab.
- Extra step: none.

Use the same names as the student guide: **user-mode image load**, **kernel driver load**, **path**, **hashes**, **signed vs unsigned**, and **initiating process**. MDE `ActionType` on this table: **ImageLoaded**. Do not invent a driver value on `DeviceImageLoadEvents` — that table is DLL loads. Driver load is Sysmon 6. The given uses `powershell.exe` and Temp `update.dll`. Do not turn it into the intro plot.

**Key Teaching Points:**
- Endpoint image or driver load event, not Zeek.
- Event 7 / MDE is user-mode. Event 6 is a kernel driver, not a DLL load into a process.
- A file create is not a load.
- Signed empty is not logged, not “unsigned.”
- A query is specific, not every image or driver load.

**Common Student Challenges:**
- Treat Event 6 as a DLL load into a process. Why: Event 7 is user-mode; Event 6 is kernel. Example: writing “powershell loaded a DLL” from an Event 6.
- Treat a file create as a load. Why: the file event is 1.1.3. Example: “update.dll was loaded” from a Sysmon 11 in Temp.
- Write `DeviceImageLoadEvents` with no filter as a “specific” query. Why: the task is a named pattern. Example: the whole table, no process or path.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.1.6.1 – Image and driver load activity concepts
- T: 1.1.6.2 – Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.6.3 – Create a SIEM query to detect specific image or driver load activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Image or driver load event, not Zeek |
| Key Concepts            | 16 min    | Fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a host, and you have to say what was loaded, into whom (or into the kernel), from where.
- Walk the field table. Stop on Event 6: it is a kernel driver, not a DLL load, and it has no user-mode parent field.
- MDE image load is `ImageLoaded` on `DeviceImageLoadEvents`. That table is DLL loads. Do not invent a driver `ActionType` there. Driver load is Sysmon 6.
- Walk the given: `powershell.exe` → Temp `update.dll`, `Signed=false`. One sentence. Path and initiator.
- If they start installing Sysmon: that is not this lesson.
- If they treat a Sysmon 11 as a load: that is a file create (1.1.3). You cannot say the module was loaded.
- If they start persistence or BYOVD: that is not this lesson.
- If they write `DeviceImageLoadEvents` with no filter: that is not a specific query.

---

## Knowledge Check – Answer Key

1. **Event 6 is a DLL load into a process. True or false?**  
   **Answer:** False. Event 6 is a kernel driver load. User-mode image load is Event 7 / `DeviceImageLoadEvents`.  
   **Explanation:** Event 6 has no user-mode parent. Event 7 `Image` is the process; `ImageLoaded` is the module.

2. **PowerShell loads Temp update.dll, Signed=false. What occurred?**  
   **Answer:** PowerShell loaded an unsigned DLL from Temp.  
   **Explanation:** Path and initiator are what you write down. The file create of that DLL, if you have one, is a different event.

3. **A query that matches every image or driver load event is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (process + path, or Event 6 + driver path).  
   **Explanation:** Every load event is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.2.1 Zeek concepts
