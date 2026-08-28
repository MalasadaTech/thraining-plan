# Instructor Guide – Module 1.1.5 – Registry Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.5.1 A / B / C ; 1.1.5.2 2b / 3c / 4c ; 1.1.5.3 2b / 3c / 4c  
- Hunter: 1.1.5.1 A / B / B ; 1.1.5.2 1a / 2b / 3c ; 1.1.5.3 1a / 2b / 3c  
- CTI: 1.1.5.1 A / A / A ; 1.1.5.2 1a / 1a / 1a ; 1.1.5.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a host registry event and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read registry events on a host to see what changed in a key or value, and which process changed it.
- How it hooks to the lesson before: 1.1.4 was host-network activity on the same host telemetry. This lesson is the registry kind.
- How it hooks to the lesson after: 1.1.6 is image / driver load — last 1.1 child. Persistence techniques are 3.6.
- Why we are doing it this way: after naming the kinds, read the registry kind so you can describe what changed in a key or value, and who changed it, without turning Run or Services into a persistence catalog.
- What we are *not* doing in this lesson: Persistence catalog (3.6). Zeek (1.2). Sysmon install. File-create or process-create write-ups. No lab.
- Extra step: none.

Use the same names as the student guide: **hive**, **key**, **value**, **set**, **delete**, **rename**, and **initiating process**. MDE `ActionType` on this table: **RegistryValueSet**, **RegistryKeyCreated**, **RegistryKeyDeleted**, **RegistryValueDeleted**, **RegistryKeyRenamed**. Do not invent `RegistryValueRenamed` here — value rename is Sysmon 14. The given uses the course-fiction Run value `Updater` → Temp `update.exe`. Do not turn it into a hunt package or the intro plot.

**Key Teaching Points:**
- Endpoint registry event, not Zeek.
- Hive, key, and value. Set, delete, or rename.
- Run and Services are example locations, not a persistence course.
- Event 13 is SetValue. Event 12 is create/delete. Event 14 is rename.
- A query is specific, not “all registry events.”

**Common Student Challenges:**
- Treat a Run-key event as a finished persistence hunt. Why: Run is a location in this lesson; persistence techniques are 3.6. Example: writing “attacker persisted via Run” as the whole product from one SetValue.
- Describe the file create of `update.exe` as the registry story. Why: the file is 1.1.3. Example: “malware dropped in Temp” when the event is PowerShell setting `Run\Updater`.
- Write `DeviceRegistryEvents` with no filter as a “specific” query. Why: the task is a named pattern. Example: the whole table, no initiator or key path.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.1.5.1 – Registry activity concepts
- T: 1.1.5.2 – Analyze a registry event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.5.3 – Create a SIEM query to detect specific registry operations

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Registry event, not a hunt |
| Key Concepts            | 16 min    | Fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a host, and you have to say what changed in a key or value, and who changed it.
- Walk hive vs key vs value. Native `\REGISTRY\USER\` and friendly HKCU are the same tree. Sysmon often writes `HKU\<SID>`.
- Stop on Run and Services: they are locations, not a persistence lecture.
- Walk the ActionType table. Event 13 is SetValue. Event 12 is create/delete. Event 14 is rename. Do not invent `RegistryValueRenamed` on `DeviceRegistryEvents`.
- Walk the given: Sysmon 13, `powershell.exe`, `Run\Updater` = Temp `update.exe`. One sentence. Key, value, initiator.
- If they start listing every persistence method: that is 3.6. Stay on this event.
- If they describe the file create of `update.exe`: that is 1.1.3. Stay on the registry event.
- If they write `DeviceRegistryEvents` with no filter: that is not a specific query.

---

## Knowledge Check – Answer Key

1. **A Run-key event is a finished persistence hunt. True or false?**  
   **Answer:** False. This lesson describes the set. Persistence techniques are 3.6.  
   **Explanation:** Run and Services are example locations. Naming the location is not a hunt package.

2. **PowerShell SetValue Run\\Updater = Temp update.exe. What occurred?**  
   **Answer:** PowerShell set HKCU Run value `Updater` to that Temp path.  
   **Explanation:** One sentence: what happened to which key/value, by whom. The file create of `update.exe` is a different event.

3. **A query that matches every registry event is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (initiator + key path).  
   **Explanation:** “All registry events” is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.1.6 Image and driver load
