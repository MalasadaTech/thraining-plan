# Instructor Guide – Module 2.2.4 – Cognitive Biases and Mitigation

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.4 B / C / C ; 2.2.4.1 3c / 4c / 4d  
- Hunter: 2.2.4 A / B / B ; 2.2.4.1 1a / 2b / 3c  
- SOC: 2.2.4 A / A / A ; 2.2.4.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the bias in a judgment and apply a Key Assumptions Check or ACH. Not a pep talk.

**Context (plain language):**

- What this lesson is for: CTI analysts write judgments other people act on. A first label, a favorite story, or the last incident can lock that product. This lesson names the bias in the judgment and applies a named method so the product can still change.
- How it hooks to the lesson before: 2.2.3 was Admiralty — rating who said it and how this piece checks out. This lesson is why a first label still wins after a rating exists.
- How it hooks to the lesson after: 2.3.1 is the internal threat intelligence platform. The tradecraft unit ends here.
- Why we are doing it this way: name three biases and apply a method this course already named, so the product can still move. Do not invent a new method.
- What we are *not* doing in this lesson: a third official structured analytic technique. Diagnosing the author. Admiralty letters. Estimative wording. TIP navigation. Actor profiles. No lab.
- Extra step: none.

Use the same names as the student guide: **confirmation**, **anchoring**, **availability**, **Key Assumptions Check**, **Analysis of Competing Hypotheses (ACH)**, and **mitigation**. **PRD APT** is a vendor label on a PDF, not proof of who they are. **A12** is this course’s classroom incident — availability would copy it onto a new event with no shared host, malware, or infrastructure. **Structured analytic technique** means a named method; do not use SAT as the headline word.

**Key Teaching Points:**
- Confirmation, anchoring, and availability — and what each does to the product.
- A mitigation is a named method, not “try harder.”
- The product is the task, not the person who wrote it.

**Common Student Challenges:**
- Treat “be more objective” as a mitigation. Why: a pep talk is not a method you can run. Example: writing “I will stay objective” instead of listing the assumption that the vendor name is who they are.
- Treat extra bias names as required syllabus. Why: this lesson only requires three. Example: listing sunk cost and recency as names they must produce on the knowledge check.
- Diagnose the author. Why: the task is the judgment on the page. Example: “the vendor is biased” instead of “the first label stuck, so later internals cannot move the call.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.2.4 – Cognitive biases and mitigation
- T: 2.2.4.1 – Identify cognitive bias in a judgment and apply a mitigation technique

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Name the bias in the product |
| Key Concepts            | 12 min    | Three biases; two methods; PDF example |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: analysts write judgments other people act on, and a first label or last incident can lock the product.
- Write the three biases and what each does to the product. Stop there. Do not require a longer list.
- Gloss the two methods in one line each. Key Assumptions Check when one claim is carrying the call. ACH when two stories are live. Do not rebuild the 2.2.2 lesson.
- Walk the given: “Vendor PDF says PRD APT, so high nation-state.” Anchoring and confirmation. Mitigation is a Key Assumptions Check on “vendor name = who they are.”
- If they say “be more objective”: that is not a method. Name Key Assumptions Check or ACH.
- If they add ten more bias names as required: this lesson names three.
- If they diagnose the vendor or the author: the task is the judgment on the page, not the person.
- If they start Admiralty letters or an actor profile: that is 2.2.3 or 2.11. Stay on the bias in this sentence.
- If they open the TIP: that is 2.3.1.

---

## Knowledge Check – Answer Key

1. **“Be more objective” is a mitigation technique. True or false?**  
   **Answer:** False. A named method is a mitigation.  
   **Explanation:** “Be more objective” is a pep talk. Key Assumptions Check or ACH is a method you can run on the product.

2. **Name two biases from this lesson.**  
   **Answer:** Any two of confirmation, anchoring, availability.  
   **Explanation:** Those three are the syllabus set. Extra psychology names are not required.

3. **“Vendor PDF says PRD APT, so high nation-state.” Bias, and one mitigation.**  
   **Answer:** Anchoring and/or confirmation. Key Assumptions Check (or ACH if they list a competing cluster, such as activity group versus nation-state).  
   **Explanation:** The first vendor label stuck. A Key Assumptions Check tests “vendor name = who they are.” That assumption breaks.

---

## Additional Instructor Resources

- Next: 2.3.1 Internal threat intelligence platform
