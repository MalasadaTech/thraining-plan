# Instructor Guide – Module 3.1 – Purpose of Threat Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.1.1 B / C / C ; 3.1.1.1 3c / 4c / 4c ; 3.1.1.2 3c / 4c / 4d  
- SOC: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
- CTI: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Why hunt exists: missed activity and gaps. Not a rewritten SOC ticket.

**Context (plain language):**

- What this hour is for: Hunters look for what the queue did not catch, and for holes in detections.
- How it hooks to the hour before: CTI closed at 2.12. The RFI answered the domain.
- How it hooks to the hour after: 3.2.1 is hunt types.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–b. Story bible: Run key is first *used* in hunt.
- What we are *not* doing this hour: Hunt card. Hunt types. Invented tickets. No lab.
- Extra step: none.

**Key Teaching Points:**
- FN GET /update.exe is missed activity.
- Hunt looks for Updater / more invoice.vbs.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 3.1.1 ; T 3.1.1.1 ; T 3.1.1.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Missed + gaps |
| Key Concepts            | 12 min    | A12 FN + Run key |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write missed vs gap. Walk FN GET. Walk Run key as hunt look-for, not first-alert field.

If they rewrite the SOC ticket: “Different product.”  
If they invent a Jira: “3.7.”

---

## Knowledge Check – Answer Key

1. **Hunt rewrites the SOC ticket. True or false?**  
   **Answer:** False. Different product.  
   **Explanation:** Stay-in / 0.4.

2. **Two jobs?**  
   **Answer:** Find missed activity. Find detection / visibility gaps.  
   **Explanation:** Outline a–b.

3. **Missed + look-for?**  
   **Answer:** Missed: GET /update.exe with no alert. Look-for: Run **Updater** / more `invoice.vbs` / `update.exe` on other hosts.  
   **Explanation:** Task 2 / story bible.

---

## Additional Instructor Resources

- Next: 3.2.1 Hunt types
