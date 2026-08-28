# Instructor Guide – Module 2.2.3 – Admiralty Code

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.3 B / C / C ; 2.2.3.1 3c / 4c / 4d  
- Hunter: 2.2.3 A / B / B ; 2.2.3.1 1a / 2b / 3c  
- SOC: 2.2.3 A / A / B ; 2.2.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Assign a letter for the source and a number for this piece of information, then read the pair.

**Context (plain language):**

- What this lesson is for: CTI analysts split who said it from whether this piece of information checks out. A report lands, and you write a letter for the source and a number for this claim so a reader does not treat “a shop we trust said it” as “this report is confirmed.”
- How it hooks to the lesson before: 2.2.2 was the named method (ACH or a Key Assumptions Check). This lesson is the source and information rating.
- How it hooks to the lesson after: 2.2.4 names the bias that makes people skip the rating or collapse the two parts.
- Why we are doing it this way: name both scales, then combine them as a pair, before anyone writes “trusted” or “confirmed” as one word.
- What we are *not* doing in this lesson: estimative likelihood words (2.2.1). Attribution confidence (2.1.7). Nation-state rating. Inventing a new scale. No lab.
- Extra step: none.

Use the same names as the student guide: **source reliability**, **information credibility**, **Admiralty Code**, **letter**, and **number**. **A–F** is the source. **1–6** is this piece. If the shop has a printed card, overlay it on these standard labels. Do not invent letters.

**Key Teaching Points:**
- Two independent ratings. A is not “true.” 1 is not “trusted source.”
- Write letter plus number. Do not raise one because the other is high.
- Internal is not automatically A1.

**Common Student Challenges:**
- Collapse the two ratings into one “trusted” stamp. Why: a high letter feels like confirmation. Example: writing **A1** because the vendor is well known, without checking this claim.
- Mark every internal log **A1** because it is ours. Why: ownership is not a reliability record, and one query is not confirmation by other sources. Example: rating a single sensor log **A1** with no second source.
- Promote an anonymous blog because the title said INTEL. Why: the title is not the source. Example: writing **B2** on an unsigned post that says “block these now.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.2.3 – Admiralty Code / source reliability and information credibility
- T: 2.2.3.1 – Assign Admiralty Code ratings and evaluate source reliability and credibility

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Two independent ratings |
| Key Concepts            | 12 min    | Scales; combine; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a report lands, and you have to split who said it from whether this piece checks out.
- Write A–F and 1–6. Stop on F versus 6: reliability cannot be judged is not the same as truth cannot be judged.
- Walk the pair: **B2** is usually reliable source, this piece probably true. Do not raise the 2 to a 1 because the source is B.
- Walk the two givens from the student guide. The product is letter plus number, and a one-line meaning.
- If they say “likely”: that is 2.2.1. This lesson is the letter and the number.
- If they mark the blog **A1** or **B2**: source is **F** or **E**, information is **5** or **6**.
- If they mark internals **A1** just because they are ours: usually reliable is **B**. Confirmed is **1** only if another source matches.

---

## Knowledge Check – Answer Key

1. **A reliable source means the information is confirmed. True or false?**  
   **Answer:** False. Two independent ratings.  
   **Explanation:** Source reliability is the letter. Information credibility is the number. A high letter does not make this piece confirmed.

2. **What are the two parts of an Admiralty Code rating?**  
   **Answer:** Source reliability (A–F) and information credibility (1–6).  
   **Explanation:** Write them together as letter plus number. Do not collapse them into one word like “trusted.”

3. **Anonymous blog, no internals, “block these now.” Letter + number, and why.**  
   **Answer:** **F** or **E** and **5** or **6**. Cannot treat it as **B2**.  
   **Explanation:** You cannot judge the source, or it is unreliable. This claim is improbable or cannot be judged. The title is not a reliability record.

---

## Additional Instructor Resources

- Next: 2.2.4 Cognitive biases and mitigation
