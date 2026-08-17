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
Read a host load row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read host load rows to see that a module entered a process, or that a driver entered the kernel.
- How it hooks to the hour before: 1.1.5 was the registry row (`Updater`). This hour is the last 1.1 child — the load row.
- How it hooks to the hour after: 1.2 is Zeek — network-sensor telemetry, not another host row.
- Why we are doing it this way: Short 0.x / 4.x voice. Tasks stay as what good looks like. No lab this pass.
- What we are *not* doing this hour: File-create write-up (1.1.3). Persistence / BYOVD (2.6). Zeek. Sysmon install. No lab.
- Extra step: none.

Do not invent MDE `ActionType` values. Do not plant `helpdesk.sys` as a required story beat. Encoded PowerShell / Temp path continues the 1.1 thread — do not tell the PRD plot.

**Key Teaching Points:**
- Event 7 / MDE = user-mode load. Event 6 = kernel driver.
- A file create is not a load.
- Signed empty = not logged, not “unsigned.”
- A query is specific, not “all image loads.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.1.6.1 ; T 1.1.6.2 ; T 1.1.6.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Load row, last 1.1 child |
| Key Concepts            | 16 min    | Fields a–d; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk user-mode vs kernel first. Stop on Event 6: no user-mode parent.

If they treat a Sysmon 11 as a load: “File create. 1.1.3. You cannot say it was loaded.”  
If they start BYOVD: “2.6.”  
If they write `DeviceImageLoadEvents` with no filter: “Not specific.”

---

## Knowledge Check – Answer Key

1. **Event 6 is a DLL load into a process. True or false?**  
   **Answer:** False. Event 6 is a kernel driver load. User-mode image load is Event 7 / `DeviceImageLoadEvents`.  
   **Explanation:** Outline a / d.

2. **PowerShell loads Temp update.dll, Signed=false. What occurred?**  
   **Answer:** PowerShell loaded an unsigned DLL from Temp.  
   **Explanation:** Outline a–c and 1.1.6.1 task 1.

3. **A query that matches every image-load event is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (path or loader + `.dll` / `.sys`).  
   **Explanation:** 1.1.6.1 task 2.

---

## Additional Instructor Resources

- Next: 1.2.1 Zeek concepts
