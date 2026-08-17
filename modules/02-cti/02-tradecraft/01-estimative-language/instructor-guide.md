# Instructor Guide – Module 3.2.1 – Estimative Language

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.2.1 A / A / A · 3.2.1.1 1a / 1a / 1a  
- Hunter: 3.2.1 A / B / B · 3.2.1.1 1a / 2b / 3c  
- CTI: 3.2.1 B / C / C · 3.2.1.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach purpose, the term card, and likelihood vs confidence. Force **write** and **interpret**. Do not teach Admiralty or ACH.

**Key Teaching Points:**
- Classroom table is a stand-in. Overlay the site card if you have one.
- Likelihood ≠ confidence. *Likely + medium confidence* is the model sentence.
- Banned: is / will / could / might / we believe.
- SOC 3-level is **1a / 1a / 1a**. Hunter 3-level is **1a**. CTI is **3c / 4c**. Do not collapse.
- 3.1.7 already owns low/medium/high. Reuse it; do not rename it.

**Common Student Challenges:**
- Treating “high confidence” as “highly likely.”
- Leaving *is* / *will* in the sentence.
- Putting percents in the product.
- Opening 3.2.2 / 3.2.3.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site estimative card
- Answer key (this guide)

---

## Learning Objectives

1. Purpose.
2. Card terms.
3. Likelihood vs confidence.
4. Write + interpret.

**Mapped Items:** K 3.2.1 · T 3.2.1.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.2.2 / 3.2.3 |
| Purpose, terms, two axes       | 16 min   | a–c |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Write + interpret |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they defend “is” |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they already *know* the words. Make them *use* and *read* them.
- If they want percents: “Classroom order only. Not in the product unless the site card prints numbers.”

**Question:**  
“Can something be *likely* and *low confidence* at the same time?” (Yes. Pattern fits; evidence is thin.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail *is* / *will* / *might*. Fail high-confidence-as-highly-likely. Accept paraphrase of A/B if the term is on the card.

**Summaries:**
- Ex 1: likely + medium — two axes.
- Ex 2: is/will = not estimative; split into two judgments.
- Ex 3: could banned; country over-claim; rewrite cluster vs state.

**Write:**

| Item | Accept (paraphrase) |
|------|---------------------|
| A | **Likely** (or **highly likely** if they argue two internals) Night Owl **cluster**, **medium** confidence. Fail *is*. |
| B | **Likely** or **even chance** it continues this quarter, **medium** or **low** confidence. Fail *will*. |

**Interpret:**

| Item | Term | Meaning | Confidence stated? | Call |
|------|------|---------|--------------------|------|
| C | Highly unlikely | Low likelihood | Yes — low | **Legal.** Thin guest hit. |
| D | *Might* | **Not on the card** | No | **Fail.** Rewrite with a term. |
| E | Almost certainly | Very high | Yes — high | **Language legal, claim too strong** for one shared SNI. Downgrade term and/or confidence. |
| F | Even chance | About as likely as not | No | **Legal likelihood.** Note confidence missing (not automatically a fail if they flag it). |

---

## Knowledge Check – Answer Key

1. **What problem does it prevent?**  
   **Answer:** The consumer guessing whether “could” means likely or remote. Makes uncertainty comparable.  
   **Explanation:** Outline a.

2. **Three card terms / one banned?**  
   **Answer:** Any three from the table. Banned: is, will, could, might, may, we believe, suggests.  
   **Explanation:** Outline b.

3. **Likely vs medium confidence?**  
   **Answer:** *Likely* = greater than even (likelihood). *Medium* = evidence quality (3.1.7). Different axes.  
   **Explanation:** Outline c.

4. **Why not “is”?**  
   **Answer:** It claims certainty. A judgment needs a card term.  
   **Explanation:** Example 2 / task 1.

5. **Source letters?**  
   **Answer:** **3.2.3** Admiralty Code.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Site estimative-language card
- Next recommended module: 3.2.2 Structured analytic techniques
