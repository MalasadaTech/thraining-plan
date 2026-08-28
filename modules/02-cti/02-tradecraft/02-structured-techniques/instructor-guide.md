# Instructor Guide – Module 2.2.2 – Structured Analytic Techniques

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.2 B / C / C ; 2.2.2.1 3c / 4c / 4d  
- Hunter: 2.2.2 A / B / B ; 2.2.2.1 1a / 2b / 3c  
- SOC: 2.2.2 A / A / A ; 2.2.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Pick Analysis of Competing Hypotheses (ACH) or a Key Assumptions Check and apply it. Do not invent a third official technique.

**Context (plain language):**

- What this lesson is for: CTI analysts use a named method so a favorite story does not win by habit. A draft often already has a preferred explanation. This lesson is how you pick a method that matches the problem and apply it.
- How it hooks to the lesson before: 2.2.1 was the likelihood word. This lesson is the method behind the call.
- How it hooks to the lesson after: 2.2.3 is source letters. 2.2.4 names the bias.
- Why we are doing it this way: two syllabus techniques only. Pick the one the problem needs. Do not run both to fill time.
- What we are *not* doing in this lesson: Admiralty. Bias names. A full ACH spreadsheet. No lab.
- Extra step: none.

Use the same names as the student guide: **structured analytic technique**, **Key Assumptions Check**, and **Analysis of Competing Hypotheses (ACH)**. **Hurt** means evidence that is hard for a hypothesis to live with, not a vote for the favorite story. The given uses course-fiction names (**A12**, `WS-JLEE`, `update.exe` on port **8080**). Do not turn it into the intro plot.

**Key Teaching Points:**
- Pick the technique that matches the problem.
- A Key Assumptions Check lists the claim that is carrying the call and what would break it.
- ACH asks what evidence *hurts* a hypothesis.

**Common Student Challenges:**
- Run both techniques on every product. Why: it looks thorough. Example: a Key Assumptions Check plus a 12-row ACH when only one claim is carrying the call.
- Score ACH by how much evidence supports H1. Why: confirmation feels like analysis. Example: “H1 has three hits so it wins” instead of “`:8080` `GET /update.exe` hurts ordinary browse.”
- Add devil’s advocacy as a required third class. Why: they have heard the name. Example: listing it as syllabus for this lesson.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.2.2 – Structured analytic techniques
- T: 2.2.2.1 – Apply a structured analytic technique and select the right one for a scenario

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Named method so habit does not pick the story |
| Key Concepts            | 12 min    | ACH vs Key Assumptions Check; A12 givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a draft already has a preferred explanation, and you pick a named method so that story does not win by habit.
- Write the two techniques. Stop there. Do not add a third official class.
- Walk vendor-name as a Key Assumptions Check. Walk payload-host versus ordinary browse as ACH. Name H1, H2, and what hurts. Stop.
- If they add devil’s advocacy as required: that is not a third official class for this lesson.
- If they want a 12-row ACH matrix: name H1, H2, and what hurts. Stop.
- If they start Admiralty letters: that is 2.2.3.
- If they start naming biases: that is 2.2.4. Today is the method, not the bias list.

---

## Knowledge Check – Answer Key

1. **You should always run ACH and a Key Assumptions Check on every product. True or false?**  
   **Answer:** False. Pick the one the problem needs.  
   **Explanation:** Running both to fill time is not the task. One claim carrying the call is a Key Assumptions Check. Two live explanations is ACH.

2. **When do you pick a Key Assumptions Check instead of ACH?**  
   **Answer:** When one claim is carrying the call, not when two full stories are competing.  
   **Explanation:** ACH is for competing explanations. A Key Assumptions Check tests the claim the draft is already standing on.

3. **For A12, name one assumption a Key Assumptions Check would test.**  
   **Answer:** A vendor APT name is who they are.  
   **Explanation:** The vendor PDF label is the claim carrying a who-they-are call. What would break it: the name is a PDF, not internals.

---

## Additional Instructor Resources

- Next: 2.2.3 Admiralty Code
