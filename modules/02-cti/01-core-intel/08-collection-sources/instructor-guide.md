# Instructor Guide – Module 2.1.8 – Collection sources and methods

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.8 B / C / C ; 2.1.8.1 3c / 4c / 4c ; 2.1.8.2 3c / 4c / 4d  
- Hunter: 2.1.8 A / B / B ; 2.1.8.1 1a / 1a / 2b ; 2.1.8.2 1a / 1a / 2b  
- SOC: 2.1.8 A / A / B ; 2.1.8.1 1a / 1a / 1a ; 2.1.8.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name OSINT, commercial, and internal, then write a short plan: order, first action, and what you will not collect.

**Context (plain language):**

- What this lesson is for: CTI analysts choose where to collect so they do not skip internals when the question is “are we seeing this?”
- How it hooks to the lesson before: 2.1.7 was who you claim. This lesson is where you look.
- How it hooks to the lesson after: 2.2.1 is how you word a judgment. It is not the ticket to request collection.
- Why we are doing it this way: name the three classes and write the short plan before anyone opens a tool or files a ticket.
- What we are *not* doing in this lesson: VirusTotal Relations or TIP navigation. Local request ticket. Rewrite the requirement. No lab. No site list. No second collection plan.
- Extra step: none.

Use the same names as the student guide: **OSINT** (open-source intelligence), **commercial**, **internal**, **source class**, and **plan** (class + first action + what you will not collect). Collection **stage** is the lifecycle job of gathering from **2.1.2**, not a fourth class. **A12** is the classroom incident behind the given question; do not retell the plot.

**Key Teaching Points:**
- Three source classes. They stack. Order follows the requirement.
- Internals first when the question is *our* presence.
- A plan is class, first action, and what you will not collect — not a ticket and not a tool click.

**Common Student Challenges:**
- Treat the collection stage and a source class as the same thing. Why: both use the word collection. Example: answering “where will you look?” with “we are in the Collection stage.”
- Start with a public blog when the question is “are we seeing this here?” Why: OSINT is familiar and easy to open. Example: searching vendor blogs for the update domain before looking in Zeek or host telemetry.
- Write a ticket or open a paid platform and call that the plan. Why: those feel like doing the work. Example: “file the local collection-request ticket” or “open VirusTotal Relations” instead of naming the class and the first internal look.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.1.8 – Collection sources and methods (OSINT, commercial, internal)
- T: 2.1.8.1 – Identify appropriate collection source classes for a given requirement
- T: 2.1.8.2 – Plan collection against an intelligence requirement

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Where you collect, not the lifecycle stage |
| Key Concepts            | 12 min    | Three classes; one A12 plan |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a requirement names a question, and you have to know which class of source can answer it before you gather.
- Write the three classes. Stop there. Do not list vendor sites or a shop source catalog.
- Walk the given: “Is this the payload host *here*?” First class is internal. First action is telemetry you already have (Zeek A record, or the file from the host).
- If they open VirusTotal Relations: that is 2.9 / 0.7.
- If they write a local collection-request ticket: that is 2.12.2.1.
- If they rewrite the question: 2.1.4 is done. Stay on class and plan.
- If they add a second plan or a sibling-domain chase: that is not this requirement.

---

## Knowledge Check – Answer Key

1. **Collection as a lifecycle stage and a source class are the same thing. True or false?**  
   **Answer:** False. Stage is the job of gathering. Class is where you collect from.  
   **Explanation:** **2.1.2** named the Collection stage. This lesson names OSINT, commercial, and internal.

2. **Name the three source classes.**  
   **Answer:** OSINT, commercial, internal.  
   **Explanation:** Those are the three classes this lesson teaches. Do not add HUMINT, SIGINT, or a vendor list.

3. **A requirement asks: is this the payload host *here*? First class, first action, one thing you will not collect.**  
   **Answer:** First class **internal**. First action: look in telemetry you already have (the Zeek A record, or the file from the host). Do not collect a sibling domain the requirement did not ask for, or a paid vendor account you do not have.  
   **Explanation:** The question is *our* presence, so internals come first. The short plan also names what you will not collect.

---

## Additional Instructor Resources

- Next: 2.2.1 Estimative language
