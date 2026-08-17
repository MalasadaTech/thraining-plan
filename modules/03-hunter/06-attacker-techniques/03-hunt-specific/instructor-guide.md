# Instructor Guide – Module 3.6.3 – Hunt for a Specific Technique

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.3 3c / 4c / 4d  
- SOC: 3.6.3 1a / 1a / 2b  
- CTI: 3.6.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Hunt one named persist or privesc method. Reject the whole tactic and the wrong class.

**Context (plain language):**

- What this hour is for: Hunters turn a recognized method into a bounded hunt, not a tactic sweep.
- How it hooks to the hour before: 3.6.2 recognized elevation.
- How it hooks to the hour after: 3.7.1 is how the shop starts and controls a hunt.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline task 3 only. Story bible package is Updater / update.exe / more invoice.vbs.
- What we are *not* doing this hour: All four hunt types. Full card rewrite. Invented tickets. No lab.
- Extra step: none.

**Key Teaching Points:**
- Unique pattern is the 4d bar.
- Wrong class fails.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** T 3.6.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | One named method |
| Key Concepts            | 12 min    | Hunt line; two fails |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the hunt line. Walk A12 **`Updater`**. Fail “hunt persistence.” Fail swapping a SYSTEM task into privesc.

If they invent a Jira: “3.7.”  
If they rewrite the SOC ticket: “Different product.”

---

## Knowledge Check – Answer Key

1. **“Hunt persistence” is valid. True or false?**  
   **Answer:** False. Class, not a hunt.  
   **Explanation:** Stay-in.

2. **Named means?**  
   **Answer:** A method you can point at (value name, parent/child, specific binary) — not the tactic.  
   **Explanation:** Outline task 3.

3. **A12 hunt line?**  
   **Answer:** Run **`Updater`** → `%TEMP%\update.exe` | persist | value name `Updater` (not any Run key) | user workstations / bounded time / registry+file.  
   **Explanation:** Task 3 / story bible.

---

## Additional Instructor Resources

- Next: 3.7.1 Hunt control and lead management
