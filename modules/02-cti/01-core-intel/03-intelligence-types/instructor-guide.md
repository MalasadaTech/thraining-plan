# Instructor Guide – Module 2.1.3 – Intelligence Types

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.3 B / C / C ; 2.1.3.1 3c / 4c / 4c  
- Hunter: 2.1.3 A / B / B ; 2.1.3.1 1a / 2b / 3c  
- SOC: 2.1.3 A / A / A ; 2.1.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Classify a product or requirement as strategic, operational, tactical, or technical. Reject the neighbor.

**Context (plain language):**

- What this lesson is for: CTI analysts pick the kind of answer so the consumer gets a decision they can make. This lesson names the type of the product or the requirement, and says why it is not the neighbor.
- How it hooks to the lesson before: 2.1.2 named the stage in the loop. Type is not a stage.
- How it hooks to the lesson after: 2.1.4 is writing the requirement. This lesson is only the type of answer.
- Why we are doing it this way: name the four types and reject the neighbor before anyone writes a PIR.
- What we are *not* doing in this lesson: PIR (priority intelligence requirement) format. Audience rewrite. Actor profile. Invent extra victims or a second campaign. No lab.
- Extra step: none.

Use the same names as the student guide: **strategic**, **operational**, **tactical**, **technical**, **requirement**, and **product**. Stay on **A12**. Do not invent a second campaign. **Technical** is its own type, not a nickname for tactical.

**Key Teaching Points:**
- Four types. Neighbor pairs: strategic ↔ operational; tactical ↔ technical.
- Type follows the question. Length is not type. A stage is not type.
- A hash is an observable, not an action.

**Common Student Challenges:**
- Call a long PDF strategic because it is long. Why: length looks like “leadership reading.” Example: labeling a 40-page indicator dump strategic.
- Call a hash tactical. Why: some shops use “tactical” for indicators. Example: writing “isolate the host” as the type for a SHA256 line.
- Call a lifecycle stage a type. Why: they just named stages. Example: “this is collection intelligence.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.1.3 – Intelligence types (strategic, operational, tactical, technical)
- T: 2.1.3.1 – Classify an intelligence product or requirement by type

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Kind of answer, not file length |
| Key Concepts            | 12 min    | Four types; A12 pair |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a consumer needs a decision they can make, and you have to name the kind of answer.
- Write the four types. Stop. Neighbors are strategic vs operational, and tactical vs technical.
- Type follows the question. Length is not type. A stage is not a type.
- Walk the givens: observables are **technical**; isolate / treat-as-payload is **tactical**; “what should IR do now?” is a **tactical** requirement.
- If they call a PDF strategic because it is long: ask what question it answers.
- If they call a hash tactical: that is an observable. Technical.
- If they write a PIR: that is 2.1.4.

---

## Knowledge Check – Answer Key

1. **A long PDF is strategic because it is long. True or false?**  
   **Answer:** False. Type follows the question.  
   **Explanation:** Length is not type. A long indicator dump can still be technical, or still data.

2. **Name the four types.**  
   **Answer:** Strategic, operational, tactical, technical.  
   **Explanation:** Those are the four types this course uses. Technical is not a nickname for tactical.

3. **Isolate WS-JLEE; treat the update domain as the A12 payload host. Type, and why not the neighbor?**  
   **Answer:** **Tactical.** Not technical: that sentence is the action now, not the observable.  
   **Explanation:** Technical would be the IP, the GET, or the hash. Isolate / treat-as-payload is what a responder does now.

---

## Additional Instructor Resources

- Next: 2.1.4 Intelligence requirements
