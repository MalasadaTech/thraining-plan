# Instructor Guide – Module 3.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique

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
Turn one named persistence or privilege-escalation method into a bounded hunt. Reject the whole tactic and the wrong class.

**Context (plain language):**

- What this lesson is for: Hunters search for activity the alerts missed. After they can recognize a method, they still have to turn it into a hunt someone can run — one named method, a unique pattern, and a bound.
- How it hooks to the lesson before: 3.6.2 recognized elevation. 3.6.1 recognized persistence.
- How it hooks to the lesson after: 3.7.1 is how the shop starts and controls a hunt.
- Why we are doing it this way: recognition already happened; this lesson is the hunt product so they do not treat the class as the hunt.
- What we are *not* doing in this lesson: hunt types (3.2.1). Full card rewrite (3.2.2). ATT&CK remapping (3.5). Invented tickets (3.7). Recognition drill. No lab.
- Extra step: none.

Use the same names as the student guide: **named technique**, **class**, **unique pattern**, **scope**, and **hunt line**. **Privilege escalation** is the student-guide word, not a shop shortening. The given uses the course-fiction Run value **`Updater`** → `%TEMP%\update.exe`. Do not retell the incident. Do not invent a ticket name.

**Key Teaching Points:**
- Named method, not the class.
- Unique pattern is what you search — the value name `Updater`, not any Run key.
- Wrong class fails: a SYSTEM scheduled task is not privilege escalation unless elevation is shown.
- The product is a bounded hunt, not a SOC-ticket rewrite and not a ticket you invent.

**Common Student Challenges:**
- Write “hunt persistence” as the hunt. Why: the class is what they just learned to recognize. Example: “search all Run keys / all scheduled tasks.”
- Call a SYSTEM scheduled task privilege escalation. Why: SYSTEM looks high-privilege. Example: hunting “SYSTEM tasks” as elevation when no user-to-SYSTEM step is in the log.
- Invent a ticket so the hunt has a number. Why: they want a place to file it. Example: “open Hunt-17.” That is 3.7.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- T: 3.6.3 – Hunt for specific persistence or privilege escalation techniques

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | One named method, not the class |
| Key Concepts            | 12 min    | Hunt line; two fails |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: hunters look for missed activity, and a class is not a hunt.
- Write the five hunt-line pieces from the student guide. Stop there. Do not rewrite the 3.2.2 card.
- Walk the given: HKCU Run **`Updater`** → `%TEMP%\update.exe` on user workstations, last 14 days, registry + file. Unique pattern is the value name.
- Fail “hunt persistence”: no unique pattern and no bound.
- Fail swapping a SYSTEM scheduled task into privilege escalation when no elevation was shown.
- If they invent a ticket name: that is 3.7. This lesson does not open one.
- If they rewrite the SOC ticket: different product. This lesson is a bounded hunt.
- If they remap to ATT&CK: that is 3.5. Naming the technique here is enough.

---

## Knowledge Check – Answer Key

1. **“Hunt persistence” is a valid 3.6.3 hunt. True or false?**  
   **Answer:** False. Persistence is a class, not a hunt.  
   **Explanation:** A hunt names one method and a unique pattern. “Hunt persistence” has neither a unique pattern nor a bound.

2. **What does named mean in this lesson?**  
   **Answer:** A method you can point at — a value name, a parent/child pair, a specific binary — not the tactic.  
   **Explanation:** HKCU Run **`Updater`** is named. “Persistence” is not.

3. **Write one hunt line for HKCU Run `Updater` → `%TEMP%\update.exe` (named technique, class, unique pattern, scope).**  
   **Answer:** Run **`Updater`** → `%TEMP%\update.exe` \| persistence \| value name `Updater` (not any Run key) \| user workstations / last 14 days / registry + file.  
   **Explanation:** Unique pattern is the value name. Class is persistence. Scope is bounded. Why not the whole tactic: this value, not every autorun.

---

## Additional Instructor Resources

- Next: 3.7.1 Hunt control and lead management
