# Instructor Guide – Module 2.1.2 – Intelligence lifecycle

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.2 B / C / C ; 2.1.2.1 3c / 4c / 4c  
- Hunter: 2.1.2 A / B / B ; 2.1.2.1 1a / 2b / 3c  
- SOC: 2.1.2 A / A / A ; 2.1.2.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the six stages and say the flow loops. A stage is a job, not a folder.

**Context (plain language):**

- What this lesson is for: CTI analysts name which job they are in so a question becomes a used answer, and so they know when to collect again instead of briefing a guess.
- How it hooks to the lesson before: 2.1.1 was the layer (data / information / intelligence). This lesson is the loop around that path.
- How it hooks to the lesson after: 2.1.3 is type (strategic / tactical). Type is not a stage.
- Why we are doing it this way: name the stage and the loop before requirement format, source classes, or types. A reader with no live instructor still has to follow.
- What we are *not* doing in this lesson: PIR format (2.1.4). Source classes (2.1.8). Audience rewrite (2.1.6). Finished paper (2.11). Actor profile (2.11.1.2). Local collection-request process (2.12.2.1). No lab.
- Extra step: none.

Use the same names as the student guide: **Planning and Direction**, **Collection**, **Processing and Exploitation**, **Analysis and Production**, **Dissemination**, **Evaluation and Feedback**. **Exploitation** here means turning collected material into a form an analyst can use, not exploiting a host. **TIP** is threat intelligence platform. **RFI** is request for information. **PIR** is priority intelligence requirement — name it only as not this lesson. Do not invent a seventh stage. Do not tell the PRD plot. The **A12** RFI is enough.

**Key Teaching Points:**
- Six stages. The flow loops; it is not a one-way pipeline.
- Collection gathers data. Processing turns it into information. Analysis produces intelligence.
- A stage is a job, not a folder. Missing material means go back to collection.

**Common Student Challenges:**
- Treat a folder or chat title as the stage. Why: shops name rooms “INTEL.” Example: calling a TIP paste “analysis” because it sits in an intel folder.
- Treat dissemination as the end. Why: the list looks like a pipeline. Example: sending the note and never asking whether anyone used it.
- Skip collection when analysis has a gap. Why: they want to answer now. Example: disseminating “probably the payload host” with no A record yet.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.1.2 – Intelligence lifecycle
- T: 2.1.2.1 – Identify the lifecycle stage of an activity and describe the flow

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Job, not folder; this lesson is the loop |
| Key Concepts            | 12 min    | Six stages; A12 given; the flow loops |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an RFI lands, and you have to name which job you are in so a question becomes a used answer.
- Write the six names. One purpose line each. Stop. Do not add a seventh stage. Shops may rename; the work stays.
- Walk exploitation as “make it usable,” not “exploit a host.” A TIP paste is processing, not analysis.
- Walk the A12 RFI as Planning, the A-record pull as Collection, the TIP store as Processing, the assess sentence as Analysis, delivery to SOC as Dissemination. If they skip collection: loop back. After SOC uses or ignores it, that is Evaluation and Feedback.
- If they write a PIR: that is 2.1.4.
- If they pick OSINT vs commercial: that is 2.1.8.
- If they start types (strategic / tactical): that is 2.1.3.
- If they start the PRD plot: stay on the A12 RFI.

---

## Knowledge Check – Answer Key

1. **Dissemination is the last stage and the work stops. True or false?**  
   **Answer:** False. Evaluation and Feedback can open the next question. Analysis can send you back to collection.  
   **Explanation:** The flow loops. Dissemination is a stage, not the end of the work.

2. **Name the six stages of the intelligence lifecycle in order (the loop can still return).**  
   **Answer:** Planning and Direction; Collection; Processing and Exploitation; Analysis and Production; Dissemination; Evaluation and Feedback.  
   **Explanation:** These six names. Shops may collapse labels; do not invent a seventh.

3. **“Pull the A record for the update domain against the A12 RFI.” Which stage?**  
   **Answer:** Collection.  
   **Explanation:** Gathering the raw material against the question is collection. The RFI itself was planning. Writing the assessment would be analysis.

---

## Additional Instructor Resources

- Next: 2.1.3 Intelligence types
