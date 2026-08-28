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
Name the kind of record — incident, RFI, or a shop-named other — and say why the neighbor is wrong.

**Context (plain language):**

- What this lesson is for: After you decide an alert is a case, or that you need another desk's help, you pick the kind of record. The next desk needs a case or a question, not both mixed in one product. This lesson names those types.
- How it hooks to the lesson before: 1.4.5 closed the alert clocks. This lesson opens reporting.
- How it hooks to the lesson after: 1.5.2 is when the report is due, not which type it is.
- Why we are doing it this way: name the type before anyone writes a body, assigns a clock, or names recipients.
- What we are *not* doing in this lesson: Write the body. Assign a report clock. Route it. Write an intel product. Invent a DYA type list. Open **1.7** (retired). No lab.
- Extra step: none.

Use the same names as the student guide: **incident report**, **RFI** (Request for Information), **other**, **adjacent** (the next-closest wrong type), and **neighbor**. Do not invent Harbor or DYA report names as policy. Do not tell the PRD plot. Do not dump the Run key or the sibling domain. The first case is **A12** (`wscript` → encoded PowerShell, Temp `invoice.vbs`). The RFI asks intel to work the update domain / file.

**Key Teaching Points:**
- Incident records the case. RFI asks a question. Other is a name the shop already uses.
- An RFI can sit beside an incident. It is not a second case.
- The pair that gets mixed up is incident ↔ RFI.

**Common Student Challenges:**
- Open a second incident for the domain question. Why: every product feels like a case. Example: writing “incident report” when **A12** is already open and they only need CTI to work the domain.
- Mix the case and the question into one record. Why: both feel like “the A12 write-up.” Example: one ticket that both records the IR handoff and asks CTI the domain question, with no type named.
- Call a shift-change log **other**. Why: they need a bucket for notes. Example: labeling a turnover paste as a 1.5 type. **1.7** is retired — do not send them there.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.5.1.1 – Report types
- T: 1.5.1.2 – Identify the correct report type for a given situation and why it is not the adjacent type

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

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

**Talking Points:**
- Open with the job: after an alert is a case, or you need another desk's help, you pick the kind of record so the next desk is not handed a mixed product.
- Write incident, RFI, and other. Stop there. Do not write a body, a clock, or a recipient list.
- Walk the two “given” lines from the student guide. The product is the type plus why the neighbor is wrong, not the rest of the incident.
- If they start writing the report body: this lesson is the type only.
- If they assign a clock: that is 1.5.2.
- If they name recipients: that is 1.5.3.
- If they open a second incident for the domain: that product is the question, not a new case.
- If they invent a DYA type: other is a name their real shop already uses.
- If they write a shift-change log as other: that is not a 1.5 type. 1.7 is retired — do not send them there.
- If they write T1059 or an intel paper: frameworks are 0.6; finished intel is 2.11.

---

## Knowledge Check – Answer Key

1. **An RFI is a second incident case. True or false?**  
   **Answer:** False. An RFI is the question. It can sit beside an incident; it is not a second case record.  
   **Explanation:** The pair that gets mixed up is incident ↔ RFI. Recording the case and asking another desk for information are two products.

2. **What is an incident report for, versus an RFI?**  
   **Answer:** An incident report records a case / IR handoff. An RFI asks another desk for information.  
   **Explanation:** Name the two products. Do not mix them into one write-up.

3. **A12 already exists. You want CTI to work the update domain. Type, and why not the adjacent one?**  
   **Answer:** **RFI.** Not incident: the case is already open; this product is the question.  
   **Explanation:** The task is the type plus why the neighbor is wrong. A later question does not rewrite the incident.

---

## Additional Instructor Resources

- Next: 1.5.2 Reporting timeline requirements
