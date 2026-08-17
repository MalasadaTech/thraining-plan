# Instructor Guide – Module 2.1.1 – Difference between Data, Information, and Intelligence

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.1 B / C / C ; 2.1.1.1 3c / 4c / 4c  
- Hunter: 2.1.1 A / B / B ; 2.1.1.1 1a / 2b / 3c  
- SOC: 2.1.1 A / A / A ; 2.1.1.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Sort a product as data, information, or intelligence. Do not brief a raw field as intel.

**Context (plain language):**

- What this hour is for: CTI analysts label the layer so the next desk gets a judged answer, not a hash with a new title.
- How it hooks to the hour before: 1.5 closed SOC. The RFI asked intel to work the update domain / file.
- How it hooks to the hour after: 2.1.2 is the lifecycle. This hour is only the three words and the sort.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–b plus the categorize task. CTI 3 is already at B / 3c. SOC is A / 1a.
- What we are *not* doing this hour: Lifecycle stages. PIR format. Finished product. Attribution. VT Relations. Hunt. No lab.
- Extra step: none.

Do not invent a second plot. Do not dump the Run key. **A12** and the update domain are enough. Do not tell the PRD story.

**Key Teaching Points:**
- Data = recorded fact. Information = story. Intelligence = judged answer to a question.
- The path is add context, then add judgment. Not a rename.
- If they are unsure, it is not intelligence yet.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.1.1 ; T 2.1.1.1

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Sort the layer |
| Key Concepts            | 12 min    | Three terms; A12 path |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the three words. Walk `203.0.113.88` as **data**, the A-record / `invoice.vbs` story as **information**, the A12 assessment as **intelligence**.

If they call a VT count intelligence: “Context. Still information.”  
If they want PIR format: “2.1.4.”  
If they start the lifecycle: “2.1.2.”  
If they write a finished paper: “2.11.”  
If they invent a lookalike-Microsoft row: “Stay on A12.”

---

## Knowledge Check – Answer Key

1. **A hash with no other text is intelligence. True or false?**  
   **Answer:** False. That is data.  
   **Explanation:** Outline a / task 1.

2. **What must you add before information becomes intelligence?**  
   **Answer:** A judgment against a question, and a so-what (what someone should do).  
   **Explanation:** Outline b.

3. **“We assess the update domain is the payload host for A12; treat it as such.” Layer?**  
   **Answer:** **Intelligence.** It answers the RFI question and names a so-what.  
   **Explanation:** Task 1.

---

## Additional Instructor Resources

- Next: 2.1.2 Intelligence lifecycle
