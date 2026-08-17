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
Read a host registry row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read host registry rows to see what changed in the registry, and by which process.
- How it hooks to the hour before: 1.1.4 was the host-network row. This hour is the registry row on the same host telemetry.
- How it hooks to the hour after: 1.1.6 is image / driver load — last 1.1 child. Persistence *how-to* is 2.6.
- Why we are doing it this way: Short 0.x / 4.x voice. Tasks stay as what good looks like. No lab this pass.
- What we are *not* doing this hour: Persistence catalog (2.6). Zeek. Sysmon install. File-create or process-create write-ups. No lab.
- Extra step: none.

Plant the Run value **`Updater`** → Temp `update.exe` as a **location + set**. Do not turn it into a hunt package. Do not invent `ActionType` values. Do not tell the PRD plot.

**Key Teaching Points:**
- Hive, key, value. Set / delete / rename.
- Run and Services are examples, not 2.6.
- Event 13 is SetValue. Event 12 is key create/delete. Event 14 is rename.
- A query is specific, not “all registry events.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.1.5.1 ; T 1.1.5.2 ; T 1.1.5.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Registry row, not a hunt |
| Key Concepts            | 16 min    | Fields a–e; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk hive vs key vs value. Stop on Run: location, not a persistence lecture.

If they start listing every persistence method: “2.6.”  
If they describe the file create of `update.exe`: “1.1.3.”  
If they write `DeviceRegistryEvents` with no filter: “Not specific.”

---

## Knowledge Check – Answer Key

1. **A Run-key row is a finished persistence hunt. True or false?**  
   **Answer:** False. This hour describes the set. Persistence techniques are 2.6.  
   **Explanation:** Outline c.

2. **PowerShell SetValue Run\\Updater = Temp update.exe. What occurred?**  
   **Answer:** PowerShell set HKCU Run value `Updater` to that Temp path.  
   **Explanation:** Outline a–d and 1.1.5.1 task 1.

3. **A query that matches every registry event is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (initiator + key path).  
   **Explanation:** 1.1.5.1 task 2.

---

## Additional Instructor Resources

- Next: 1.1.6 Image and driver load
