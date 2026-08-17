# Instructor Guide – Module 1.5.1 – Report Types

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C ; 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C ; 1.5.1.2 2b / 3c / 4c  
- CTI: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Pick the kind of record — incident, RFI, or a shop-named other — and say why the neighbor is wrong.

**Context (plain language):**

- What this hour is for: SOC analysts choose a case record or a question so the next desk is not handed a mixed product. The RFI is the door into CTI.
- How it hooks to the hour before: 1.4.5 closed the alert clocks. This hour opens reporting.
- How it hooks to the hour after: 1.5.2 is when the report is due, not which type it is.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c. Type plus reject the neighbor. CTI already works the task at 3-level (3c).
- What we are *not* doing this hour: Write the body. Assign a report clock. Route it. Write an intel product. Invent a DYA type list. Open **1.7** (retired). No lab.
- Extra step: none.

Do not invent Harbor or DYA report names as policy. Do not tell the PRD plot. Do not dump the Run key or the sibling domain. The first case is **A12** (`wscript` → encoded PowerShell, Temp `invoice.vbs`). The RFI asks intel to work the update domain / file.

**Key Teaching Points:**
- Incident = case. RFI = question. Other = a name the shop already uses.
- An RFI can sit beside an incident. It is not a second case.
- Adjacent pair is incident ↔ RFI.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.5.1.1 ; T 1.5.1.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Case vs question |
| Key Concepts            | 12 min    | Three names; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write incident vs RFI vs other. Walk **A12** first record as **incident, not RFI**. Walk the domain question as **RFI, not a second incident**.

If they write the body: “Type only.”  
If they assign a clock: “1.5.2.”  
If they name recipients: “1.5.3.”  
If they open a second incident for the domain: “Question, not a new case.”  
If they invent a DYA type: “Other is a name their real shop already uses.”  
If they write a shift-change log as “other”: “Not a 1.5 type. 1.7 is retired — do not send them there.”  
If they write T1059 or an intel paper: “0.6 / 3.11.”

---

## Knowledge Check – Answer Key

1. **This hour is who gets the report and which channel. True or false?**  
   **Answer:** False. That is 1.5.3. This hour is which type.  
   **Explanation:** Stay-in / vs 1.5.3.

2. **Incident vs RFI?**  
   **Answer:** Incident records a case. RFI asks another desk for information.  
   **Explanation:** Outline a–b.

3. **A12 exists; CTI to work the update domain. Type and why not adjacent?**  
   **Answer:** **RFI.** Not incident: the case is already open; this product is the question.  
   **Explanation:** Outline b / task 1.

---

## Additional Instructor Resources

- Next: 1.5.2 Reporting timeline requirements
