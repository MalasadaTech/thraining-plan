# Instructor Guide – Module 2.2.1 – Estimative language

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.1 B / C / C ; 2.2.1.1 3c / 4c / 4c  
- Hunter: 2.2.1 A / B / B ; 2.2.1.1 1a / 2b / 3c  
- SOC: 2.2.1 A / A / A ; 2.2.1.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Write and read a likelihood term. Do not confuse it with confidence.

**Context (plain language):**

- What this lesson is for: CTI analysts write judgments that other people act on. Those people should not have to guess whether “could be” means likely or remote. This lesson is the likelihood word.
- How it hooks to the lesson before: 2.1.8 was where you collect. This lesson is how you word the call.
- How it hooks to the lesson after: 2.2.2 is a method (ACH / assumptions). It is not a word list.
- Why we are doing it this way: pick a likelihood term so the next reader can compare products, and keep that term off the 2.1.7 evidence scale. Classroom terms only. No invented percents.
- What we are *not* doing in this lesson: Admiralty letters. Actor profile. Confidence scale rewrite. Structured techniques. No lab.
- Extra step: none.

Use the same names as the student guide: **likelihood**, **confidence**, and the classroom terms **almost certainly**, **highly likely**, **likely**, **even chance**, **unlikely**, **highly unlikely**, and **remote**. **Confidence level** on an estimative statement still means how probable, not the 2.1.7 low / medium / high evidence scale. **A12** is the course incident. **PRD** is the course-fiction adversary.

**Key Teaching Points:**
- Likelihood is not confidence.
- “Could be” is not a term.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.2.1 – Estimative language
- T: 2.2.1.1 – Use and interpret estimative language in analytic judgments

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Likelihood words, not the evidence scale |
| Key Concepts            | 12 min    | Terms; write and interpret |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: analysts write judgments other people act on, and those people should not guess whether “could be” means likely or remote.
- Write the purpose: make uncertainty comparable. Do not hide behind “we believe.”
- Walk the classroom list. Stop. These are this lesson’s terms, not a live ODNI card. No percents unless their shop card says so.
- Likelihood is how probable. Confidence is how good the evidence is (2.1.7). They can both appear. They are not the same word.
- Walk “likely the A12 payload host.” Fail “could be PRD.”
- If they say high confidence: that is 2.1.7. Different axis.
- If they put 75%: no percents unless their shop card says so.
- If they want Admiralty letters: that is 2.2.3. If they want ACH: that is 2.2.2.

---

## Knowledge Check – Answer Key

1. **“Likely” and “high confidence” mean the same thing. True or false?**  
   **Answer:** False. Likelihood is how probable. High confidence is how good the evidence is.  
   **Explanation:** The two words can both appear in one judgment. They are not interchangeable.

2. **Why does estimative language exist?**  
   **Answer:** So uncertainty is comparable. The reader does not guess.  
   **Explanation:** “Could be” and “we believe” hide whether the claim is likely or remote.

3. **Write one A12 sentence that uses a classroom term (not “could be”).**  
   **Answer:** Any legal classroom term in a full sentence, e.g. “The update domain is **likely** the payload host for A12.”  
   **Explanation:** The product is a term the next reader can compare. “Could be PRD” fails.

---

## Additional Instructor Resources

- Next: 2.2.2 Structured analytic techniques
