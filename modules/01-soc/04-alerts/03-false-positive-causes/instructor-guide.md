# Instructor Guide – Module 1.4.3 – Common False Positive Causes

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.3.1 A / B / C ; 1.4.3.2 2b / 3c / 4c  
- Hunter: 1.4.3.1 B / C / C ; 1.4.3.2 2b / 3c / 4c  
- CTI: 1.4.3.1 A / A / B ; 1.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
On a case already labeled false positive, name the cause class and one change.

**Context (plain language):**

- What this lesson is for: SOC analysts still have work after they call an alert a false positive. That fire used queue time, and the same benign activity will fire again unless someone says why it matched and what would stop it. This lesson is the cause class and one named change.
- How it hooks to the lesson before: 1.4.2 put the false-positive label on any-PowerShell / Get-Help. This lesson is why that fire happened, not the label again.
- How it hooks to the lesson after: 1.4.4 is category (scan, root, user), not cause.
- Why we are doing it this way: after the false-positive label, the queue still needs a cause and a named change so the same benign fire does not repeat. Detection engineering deploys the change.
- What we are *not* doing in this lesson: reclassify true positive versus false positive. Deploy the change. Invent a third official class. Pick scan, root, or user. No lab.
- Extra step: none.

Use the same names as the student guide: **analyst or tool activity**, **untuned or overly broad detection logic**, **cause class**, and **change**. Do not invent scanner IP addresses as shop policy. Do not tell the PRD plot. If both classes could apply, pick a primary class and still name one change.

**Key Teaching Points:**
- Two classes: analyst or tool activity, and untuned or overly broad detection logic.
- A change is one concrete sentence, not “tune it.”
- You name the change. You do not deploy it.

**Common Student Challenges:**
- Re-open true positive versus false positive. Why: the last lesson was the label. Example: arguing that `Get-Help` is a true positive because PowerShell ran.
- Write “tune it” as the change. Why: the task is a named change. Example: “tune the PowerShell rule” with no selector.
- Delete or deploy the rule. Why: SOC names the change; detection engineering deploys. Example: “delete the `/update.exe` signature” after a replay.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.4.3.1 – Common false positive causes
- T: 1.4.3.2 – Given a false positive, identify the cause class and what you would change

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Cause after the false-positive label |
| Key Concepts            | 12 min    | Two classes; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a false positive already used queue time. Name why it fired and one change that would stop the same miss.
- Write the two classes. Analyst or tool activity is your side causing the fire (download or test of a live rule, replay, shop-owned scanner). Untuned or overly broad logic is a detection that matches more than the bad activity it is for.
- Walk Get-Help as overly broad: require `-enc` and a script-host parent. Walk the replay as analyst or tool: exclude the replay; do not delete the `/update.exe` signature.
- A change is one concrete sentence. “Tune it” is not a change.
- If they reclassify true positive versus false positive: the case is already a false positive. Classification is done.
- If they want to deploy: detection engineering deploys. This lesson names the change.
- If they reach for scan, root, or user: that is category, next lesson.

---

## Knowledge Check – Answer Key

1. **This lesson is for deciding true positive versus false positive. True or false?**  
   **Answer:** False. The label is already done. This lesson is cause class plus one change.  
   **Explanation:** Classification is 1.4.2. A false positive still needs a cause and a named change so the same benign fire does not repeat.

2. **What are the two cause classes?**  
   **Answer:** Analyst or tool activity. Untuned or overly broad detection logic.  
   **Explanation:** Those are the two classes this lesson teaches. “Other” is a fallback, not a third official class.

3. **False positive: any-PowerShell on Get-Help. Class and one change sentence?**  
   **Answer:** Untuned or overly broad detection logic. Require `-enc` and a script-host parent.  
   **Explanation:** Interactive help is expected activity. The rule matched any PowerShell. Adding parent and `-enc` is the named change, not “tune it.”

---

## Additional Instructor Resources

- Next: 1.4.4 Common alert categorizations
