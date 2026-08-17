# Instructor Guide – Module 3.6.1 – Persistence Techniques

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.1 B / C / C ; 3.6.1.1 3c / 4c / 4c  
- SOC: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
- CTI: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Recognize four persistence classes in telemetry. Not a tactic hunt. Not privesc.

**Context (plain language):**

- What this hour is for: Hunters name the mechanism that will run again, and the field that proves it.
- How it hooks to the hour before: 3.5.1 mapped A12 to T1547.001.
- How it hooks to the hour after: 3.6.2 is elevation, a different job.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d + recognize task. Story bible Run key is the classroom proof.
- What we are *not* doing this hour: Hunt TA0003. Token theft. Invented tickets. No lab.
- Extra step: none.

**Key Teaching Points:**
- One-off execution is not persistence.
- Class + proof, or visibility gap.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 3.6.1 ; T 3.6.1.1

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Runs again |
| Key Concepts            | 12 min    | Four classes; A12 Run |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write runs-again. Walk four classes. Walk A12 Run **`Updater`**.

If they say the VBS run is persistence: “One-off. The Run key is persistence.”  
If they hunt all Run keys: “3.6.3.”

---

## Knowledge Check – Answer Key

1. **One-off wscript is persistence. True or false?**  
   **Answer:** False.  
   **Explanation:** Outline / stay-in.

2. **Four classes?**  
   **Answer:** Registry. Startup folder. Scheduled task. Other (service / WMI / logon script).  
   **Explanation:** Outline a–d.

3. **Class + proof?**  
   **Answer:** Registry. HKCU Run value **`Updater`** → `%TEMP%\update.exe`.  
   **Explanation:** Task 1 / story bible.

---

## Additional Instructor Resources

- Next: 3.6.2 Privilege escalation techniques
