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
Turn a messy question into a requirement that drives collection and analysis — and say what you will not chase.

**Context (plain language):**

- What this lesson is for: CTI analysts write the question the work exists to answer so they do not collect everything interesting.
- How it hooks to the lesson before: 2.1.3 was the kind of answer. This lesson is the question.
- How it hooks to the lesson after: 2.1.5 is whether the product can be used. Not whether the question is a PIR.
- Why we are doing it this way: name the requirement, including PIR as a ranked type, before anyone scores a product or picks a source class. Do not invent a DYA PIR list.
- What we are *not* doing in this lesson: source classes (2.1.8). Actionable test (2.1.5). Local standing list (2.12.1). No lab.
- Extra step: none.

Use the same names as the student guide: **intelligence requirement**, **Priority Intelligence Requirement (PIR)**, **standing**, **ad-hoc**, and **drives collection and analysis**. Do not invent **PIR-01**. The **A12** RFI question is enough. **IR** in this course also means incident response, so say **intelligence requirement** (or **requirement**) unless you mean Sam’s desk.

**Key Teaching Points:**
- A requirement focuses work on a decision. It is the question, not the product.
- A PIR is ranked. Standing and ad-hoc requirements are still requirements. They are not all PIRs.
- The requirement names what you collect, what you analyze, and what you will not chase.

**Common Student Challenges:**
- Treat every requirement as a PIR. Why: PIR is the label people remember. Example: tagging the A12 RFI as PIR-01 when leadership did not rank it.
- Invent a shop PIR list. Why: the classroom wants numbers. Example: writing PIR-01 through PIR-05 for DYA.
- File the slogan. Why: it already looks like a question. Example: recording “Are we seeing them?” as the requirement.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.1.4 – Intelligence requirements and Priority Intelligence Requirements (PIRs)
- T: 2.1.4.1 – Develop or refine intelligence requirements
- T: 2.1.4.2 – Translate stakeholder questions into clear intelligence requirements
- T: 2.1.4.3 – Explain how a given requirement drives analytic work

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | The question the work exists to answer |
| Key Concepts            | 12 min    | Purpose; PIR vs other types; A12 translate |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: write the question so collection is not everything interesting.
- Walk purpose, then types. A PIR is ranked. Standing and ad-hoc still count. They are not all PIRs.
- Walk “drives collection and analysis”: what you collect, what you analyze, and what you will not chase.
- Walk the given: “Are we seeing them?” → “Is the update domain the payload host for **A12** in this window?” Name the sibling domain as out of scope for this requirement.
- If they invent PIR-01: that list is 2.12.1. Obtain it. Do not invent it.
- If they pick VirusTotal versus RDAP: that is 2.1.8.
- If they score whether the product can be used: that is 2.1.5.
- If they tell the rest of the A12 plot: stay on the question. The given is enough.

---

## Knowledge Check – Answer Key

1. **Every intelligence requirement is a PIR. True or false?**  
   **Answer:** False. A PIR is a *priority* requirement.  
   **Explanation:** Standing and ad-hoc requirements are still requirements. Leadership or the program has to rank a PIR.

2. **What does a PIR add that a standing or ad-hoc requirement may not have?**  
   **Answer:** Rank — leadership or the program put it first.  
   **Explanation:** The extra fact is priority, not a different grammar of the question.

3. **“Are we seeing them?” Translate it for A12, and name one thing not to chase.**  
   **Answer:** “Is the update domain the payload host for **A12** in this window?” Do not chase the sibling domain on this requirement.  
   **Explanation:** The slogan has no object and no window. The refined question names both. The sibling hop is later enrichment, not this requirement.

---

## Additional Instructor Resources

- Next: 2.1.5 Ensuring intelligence is actionable
