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
On a case already labeled FP, name the cause class and one change.

**Context (plain language):**

- What this hour is for: SOC analysts say *why* this FP happened and what they would change — not the label again.
- How it hooks to the hour before: 1.4.2 put FP on any-PowerShell / Get-Help.
- How it hooks to the hour after: 1.4.4 is category (scan, root, user), not cause.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–b only. Name the change; DE deploys.
- What we are *not* doing this hour: Reclassify. Deploy. Invent a third official class. No lab.
- Extra step: none.

Do not invent Harbor scanner IPs as policy. Do not tell the PRD plot.

**Key Teaching Points:**
- Two classes: analyst/tool vs overly broad.
- A change is one concrete sentence.
- Pick a primary class if both could apply.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.4.3.1 ; T 1.4.3.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | After the label |
| Key Concepts            | 12 min    | Two classes; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write a vs b. Walk Get-Help as **b**, replay as **a**.

If they reclassify TP: “Already FP. 1.4.2 is done.”  
If they say “tune it”: “Name the selector.”  
If they want to deploy: “4.x / DE.”

---

## Knowledge Check – Answer Key

1. **This hour is TP vs FP. True or false?**  
   **Answer:** False. The label is done. This hour is cause + change.  
   **Explanation:** Stay-in / vs 1.4.2.

2. **Two syllabus classes?**  
   **Answer:** Analyst or tool activity. Untuned or overly broad logic.  
   **Explanation:** Outline a–b.

3. **Any-PowerShell on Get-Help. Class and change?**  
   **Answer:** **b**. Require `-enc` and a script-host parent.  
   **Explanation:** Outline b / task 1.

---

## Additional Instructor Resources

- Next: 1.4.4 Common alert categorizations
