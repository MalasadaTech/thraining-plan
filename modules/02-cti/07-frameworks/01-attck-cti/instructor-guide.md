# Instructor Guide – Module 2.7.1 – MITRE ATT&CK for CTI Analysis and Reporting

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- Hunter: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- SOC: 2.7.1 A / B / B ; 2.7.1.1 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Map a report or activity set to tactic + ID + evidence. Reject the neighbor.

**Context (plain language):**

- What this hour is for: CTI analysts put a reusable ATT&CK line on the product.
- How it hooks to the hour before: 2.6.1 was DNS. This hour is behavior IDs.
- How it hooks to the hour after: 2.7.2 is Diamond vertices.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a. Floor is 0.6.1. Hunt planning is 3.5.
- What we are *not* doing this hour: Hunt coverage. DTF. SOC category. No lab.
- Extra step: none.

**Key Teaching Points:**
- Same map rule as 0.6. Product-level, not a queue category.
- Encoded PS is T1059.001, not C2.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.7.1 ; T 2.7.1.1

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Product-level map |
| Key Concepts            | 12 min    | A12 two rows |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Remind tactic / technique. Walk A12 process as T1059.001. Fail C2 with no flow.

If they write hunt coverage: “3.5.”  
If they write a SOC category: “1.4.4.”

---

## Knowledge Check – Answer Key

1. **This hour is hunt planning. True or false?**  
   **Answer:** False. That is 3.5.  
   **Explanation:** Stay-in.

2. **Three things on a CTI ATT&CK line?**  
   **Answer:** Tactic, technique or sub-technique, evidence.  
   **Explanation:** Outline a / task 1.

3. **wscript → -enc. Tactic, ID, not C2?**  
   **Answer:** Execution / **T1059.001**. No C2 in that row.  
   **Explanation:** Task 1.

---

## Additional Instructor Resources

- Next: 2.7.2 Diamond Model for CTI
