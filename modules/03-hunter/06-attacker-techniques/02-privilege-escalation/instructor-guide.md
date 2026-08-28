# Instructor Guide – Module 3.6.2 – Privilege Escalation Techniques

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.2 B / C / C ; 3.6.2.1 3c / 4c / 4c  
- SOC: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
- CTI: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Recognize a privilege change in host telemetry. Name the method and the indicator. This is not persistence, and it is not a named-technique hunt.

**Context (plain language):**

- What this lesson is for: Hunters read host telemetry to see whether an actor gained a higher privilege than they started with. They name the method and the indicator that proves the change.
- How it hooks to the lesson before: 3.6.1 recognized the Run key as persistence — something that will run again.
- How it hooks to the lesson after: 3.6.3 hunts one named technique, not the whole privilege-escalation class.
- Why we are doing it this way: after naming persistence, name elevation as a different job so the next lesson can hunt one method instead of the whole class.
- What we are *not* doing in this lesson: hunting a named technique (3.6.3). Calling the A12 Run key elevation. ATT&CK remapping (3.5). Invented tickets (3.7). No lab.
- Extra step: none.

Use the same names as the student guide: **privilege escalation**, **elevation**, **token theft / impersonation**, **UAC bypass**, **auto-elevate**, **privileged service / image abuse**, **indicator**, and **visibility gap**. The `helpdesk.exe` and `fodhelper.exe` lines are classroom examples. They are not A12 facts. The A12 Run key is persistence, not this class.

**Key Teaching Points:**
- Elevation is a privilege change. Persistence is something that will run again.
- A process that was already SYSTEM is not elevation. Usual UAC consent is not a bypass.
- Name the method and the indicator, or name a visibility gap.

**Common Student Challenges:**
- Call the Run key privilege escalation. Why: persistence also starts a process. Example: writing “elevation” for HKCU Run `Updater` when the child still runs as the logged-on user.
- Treat an already-SYSTEM process as elevation. Why: the task is a privilege *change*. Example: labeling a SYSTEM service start as token theft when the parent was already SYSTEM.
- Treat expected UAC consent as a bypass. Why: a Yes on a signed installer is usual. Example: calling `Setup.exe` with a consent event a UAC bypass.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.6.2 – Privilege escalation techniques
- T: 3.6.2.1 – Recognize privilege escalation techniques in logs or telemetry

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Privilege change, not autorun |
| Key Concepts            | 12 min    | Methods + indicators; three givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: hunters have to say whether the actor gained a higher privilege, or only set something to run again.
- Walk the method table. Stop on the distinguisher: an auto-elevate parent with no consent is UAC bypass; a user-context parent that is not auto-elevate, with a SYSTEM or High-integrity child, is token theft.
- Walk the three givens. `helpdesk.exe` → SYSTEM `cmd.exe` with no consent is token theft. `fodhelper.exe` → unknown executable with no consent is UAC bypass. HKCU Run `Updater` is persistence, same user.
- If they call Run `Updater` elevation: that is 3.6.1. It starts as the logged-on user.
- If they hunt “privilege escalation” as a class: that is 3.6.3. Today is recognize the method.
- If they invent a ticket name: that is local hunt control (3.7). Do not invent one here.

---

## Knowledge Check – Answer Key

1. **HKCU Run `Updater` is privilege escalation. True or false?**  
   **Answer:** False. It is persistence.  
   **Explanation:** The Run key starts as the logged-on user. That is 3.6.1. Elevation needs a privilege change you can point at.

2. **Name two privilege-escalation methods.**  
   **Answer:** Any two of: token theft / impersonation, UAC bypass, privileged service / image abuse. A named “other” method counts only if they can point at it.  
   **Explanation:** The lesson names those Windows methods. “Privilege escalation” as a class is not a method.

3. **A user `helpdesk.exe` launches `cmd.exe` as SYSTEM with no consent event. What method, and what indicator proves it?**  
   **Answer:** Token theft. Proof: parent identity versus child identity, and no consent.  
   **Explanation:** `helpdesk.exe` is not an auto-elevate Windows binary, so this is not a UAC bypass. The parent was user-context and the child is SYSTEM.

---

## Additional Instructor Resources

- Next: 3.6.3 Hunt one named technique
