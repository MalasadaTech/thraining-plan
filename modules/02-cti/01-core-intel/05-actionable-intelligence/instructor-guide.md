# Instructor Guide – Module 2.1.5 – Ensuring Intelligence Is Actionable

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.5 B / C / C ; 2.1.5.1 3c / 4c / 4d  
- Hunter: 2.1.5 A / B / B ; 2.1.5.1 1a / 2b / 3c  
- SOC: 2.1.5 A / A / B ; 2.1.5.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Say whether a product can be acted on, and why.

**Context (plain language):**

- What this lesson is for: CTI analysts check whether a write-up lets someone act. An interesting finding is not enough. Someone has to be able to do a specific next step, in time, on the question the work was supposed to answer. This lesson scores the product.
- How it hooks to the lesson before: 2.1.4 wrote the requirement — the question the work exists to answer.
- How it hooks to the lesson after: 2.1.6 is how you say the same facts to a given audience.
- Why we are doing it this way: name whether the product can be acted on before anyone rewrites it for a reader.
- What we are *not* doing in this lesson: audience rewrite (2.1.6). Hunt-useful test (3.4.1). Actor profile (2.11). No lab.
- Extra step: none.

Use the same names as the student guide: **actionable**, **requirement**, **product**, **who**, **what**, **in time**, and **how sure**. Teach the characteristics in the student table. Do not invent a DYA actionable form or a shop five-box rubric. Stay on **A12**. Do not turn the given into the intro plot.

**Key Teaching Points:**
- Actionable means the product answers the named question and names a who and a specific what.
- “Be aware” and “interesting” fail.
- This is not the hunt-useful test.

**Common Student Challenges:**
- Pass “be aware” or “monitor” as actionable. Why: it sounds like a finished product. Example: writing “SOC should be aware of new activity” with no next step.
- Use the hunt-useful test instead. Why: hunters also say “actionable.” Example: failing a product because it has no hunt telemetry, when IR already has a named host and a next step.
- Rewrite for a different audience, then score the rewrite. Why: they think actionable means “written for leadership.” Example: dropping the host name so a CEO would like it, then scoring that version. Audience rewrite is 2.1.6.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.1.5 – Ensuring intelligence is actionable
- T: 2.1.5.1 – Evaluate whether a piece of intelligence is actionable and explain why

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Score the product against the named question |
| Key Concepts            | 12 min    | Characteristics; fail reasons; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a write-up is not done when it is interesting. Someone has to act.
- Walk the table. Actionable when it answers the named requirement, names a who, names a specific what, is still in time, and states how sure you are. It fails when any of those is missing.
- Walk the A12 sentence as **actionable**. It answers the named question, names IR, and names a next step.
- Walk “New activity in the news. Be aware.” as **not** actionable. No requirement, no who, no next step.
- A hash dump with no judgment and no next step is still data. It is not actionable intelligence.
- If they rewrite for the CEO: that is 2.1.6. Score the product in front of them, not a new audience version.
- If they say hunt-useful: that is 3.4.1. This lesson asks whether someone can act, not whether a hunt is in scope.
- If they start an actor profile: that is 2.11. Stay on pass or fail plus why.

---

## Knowledge Check – Answer Key

1. **“Be aware” with no next step is actionable. True or false?**  
   **Answer:** False. No next step.  
   **Explanation:** “Be aware” names no who and no specific what. Awareness with no action is a fail.

2. **Name two reasons a product fails the actionable test.**  
   **Answer:** Any two: it does not answer the requirement; no who is named; the what is not specific (“be aware” / “monitor”); it is too late; it is a slogan with no caveat. A hash dump with no judgment and no next step is still data, so it also fails.  
   **Explanation:** Interesting is not a pass. The table is the fail list.

3. **“We assess the update domain is the A12 payload host; IR has the host.” Actionable? Why?**  
   **Answer:** Yes. It answers the named question and names IR plus a next step.  
   **Explanation:** Who is IR. What is treat the domain as the payload host / they have the host. That is a product someone can act on.

---

## Additional Instructor Resources

- Next: 2.1.6 Tailoring output to the audience
