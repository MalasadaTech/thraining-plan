# Instructor Guide – Module 2.1.4 – Intelligence Requirements

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.4 B / C / C ; 2.1.4.1 3c / 4c / 4d ; 2.1.4.2 3c / 4c / 4d ; 2.1.4.3 3c / 4c / 4c  
- Hunter: 2.1.4 A / B / B ; 2.1.4.1 1a / 2b / 3c ; 2.1.4.2 1a / 2b / 3c ; 2.1.4.3 1a / 2b / 3c  
- SOC: 2.1.4 A / A / B ; 2.1.4.1 1a / 1a / 1a ; 2.1.4.2 1a / 1a / 1a ; 2.1.4.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Turn a messy question into a requirement that drives work — and say what you will not chase.

**Context (plain language):**

- What this hour is for: CTI analysts write the question so they do not collect “everything interesting.”
- How it hooks to the hour before: 2.1.3 was the type of answer. This hour is the question.
- How it hooks to the hour after: 2.1.5 is whether the *product* can be used. Not whether the question is a PIR.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c. No invented DYA PIR list.
- What we are *not* doing this hour: Source classes. Actionable test. Local standing list. No lab.
- Extra step: none.

Do not invent PIR-01. The **A12** RFI question is enough.

**Key Teaching Points:**
- PIR = ranked. Not every IR is a PIR.
- Translate the slogan. Name what you will not chase.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.1.4 ; T 2.1.4.1 ; T 2.1.4.2 ; T 2.1.4.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | The question |
| Key Concepts            | 12 min    | PIR vs IR; A12 translate |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write purpose / PIR / drives work. Walk “are we seeing them?” → A12 payload-host question.

If they invent PIR-01: “2.12.1. Obtain. Do not invent.”  
If they pick VT vs RDAP: “2.1.8.”  
If they score the product: “2.1.5.”

---

## Knowledge Check – Answer Key

1. **Every requirement is a PIR. True or false?**  
   **Answer:** False. A PIR is a *priority* requirement.  
   **Explanation:** Outline b.

2. **What does a PIR add?**  
   **Answer:** Rank — leadership or the program put it first.  
   **Explanation:** Outline b.

3. **“Are we seeing them?” Translate; name one thing not to chase.**  
   **Answer:** “Is the update domain the payload host for **A12** in this window?” Do not chase the sibling domain on this requirement.  
   **Explanation:** Tasks 1–3.

---

## Additional Instructor Resources

- Next: 2.1.5 Ensuring intelligence is actionable
