# Instructor Guide – Module 3.2.2 – Structured Analytic Techniques

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.2.2 A / A / A · 3.2.2.1 1a / 1a / 2b  
- Hunter: 3.2.2 A / B / B · 3.2.2.1 1a / 2b / 3c  
- CTI: 3.2.2 B / C / C · 3.2.2.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach purpose, the classroom pair (KAC + ACH), when to use each, and force **select + apply**. Do not teach Admiralty or the bias catalog.

**Key Teaching Points:**
- Classroom pair is a stand-in. Overlay a site SAT list if you have one — sign-off here is still **these two**.
- ACH: fewest **I**, not most **C**.
- KAC when the story is already locked.
- Neither when there is no second hyp and no judgment yet — collect.
- SOC 3-level task is **1a / 1a / 2b**. Hunter 3-level is **1a**. CTI is **3c / 4d**. Do not collapse.
- Estimative wording is **3.2.1**. They may add a term after the SAT; do not grade the lexicon.

**Common Student Challenges:**
- ACH because it looks senior.
- Scoring ACH by “how much I like H1.”
- Twelve-column matrices.
- Opening 3.2.3 / 3.2.4 / 3.1.7 country claims.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard or shared doc for a live mini matrix
- Optional site SAT card
- Answer key (this guide)

---

## Learning Objectives

1. Purpose of SATs.
2. Classroom ACH and KAC.
3. Select the right one.
4. Apply one small table.

**Mapped Items:** K 3.2.2 · T 3.2.2.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.2.1-as-SAT / 3.2.3 / 3.2.4 |
| Purpose, pair, when            | 16 min   | a–c |
| Walkthrough Examples           | 14 min   | Fill Ex 1 matrix live |
| Hands-On Exercise              | 18 min   | Select + apply |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they open ACH on a slogan |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they should *fill* a table, not recite “ACH exists.”
- Walk Ex 1 on the board. Force them to put **I** on H2 for E1–E3 before you do.

**Question:**  
“If every cell is C, what did you fail to do?” (Hyps are not distinct, or evidence cannot discriminate — collect or rewrite hyps.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail prestige-ACH. Fail scoring by favorites. Accept a 2-hyp ACH for A.

**Summaries:**
- Ex 1: ACH; H2 dies on I’s.
- Ex 2: KAC on a locked story.
- Ex 3: neither or KAC on the TLS-always assumption — not a fake ACH.

**Select:**

| Item | SAT | Why |
|------|-----|-----|
| A | **ACH** | Two live hyps + discriminating evidence |
| B | **KAC** | Locked nation-state sentence; must-bes hidden. (Also a 3.1.7 type problem — do not run ACH to “prove China.”) |
| C | **Neither** | Collect first |
| D | **KAC** | Coverage “always” is an assumption, not two actor hyps |

**Apply — A (ACH), accept 2 hyps:**

| Evidence | H1 Night Owl | H2 scanner FP |
|----------|--------------|---------------|
| E1 SNI | C | I |
| E2 JA3 | C | I |
| E3 PS+Run | C | I |
| E4 scanner hour | N | C |
| E5 shared CDN | N | N |

H2 has more **I**. H1 stands.

**Apply — B or D (KAC), accept three rows, paraphrase OK:**

| Assumption | If false |
|------------|----------|
| SNI unique to Night Owl | Shared CDN → do not isolate on SNI alone |
| JA3 = same actor | Shared library → need another line |
| Scanner hour is coincidence | Could be 1.4.3 FP — check scanner inventory |
| (D) Zeek sees OT | **1.8.1** — no OT span; hunt is blind |

---

## Knowledge Check – Answer Key

1. **What problem does a SAT prevent?**  
   **Answer:** Locking onto the first story; hiding must-be-true claims.  
   **Explanation:** Outline a.

2. **What is I / how do you read ACH?**  
   **Answer:** I = evidence is hard to square with that hyp. Prefer the hyp with the **fewest I**, not the most C.  
   **Explanation:** Outline b / Example 1.

3. **When KAC first?**  
   **Answer:** A judgment is already written and the assumptions are unstated.  
   **Explanation:** Outline c / Example 2.

4. **When neither?**  
   **Answer:** No second hyp and no judgment to check — collect (**3.1.8**).  
   **Explanation:** Example 3 / C.

5. **Bias catalog?**  
   **Answer:** **3.2.4**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Site SAT / tradecraft card
- Next recommended module: 3.2.3 Admiralty Code
