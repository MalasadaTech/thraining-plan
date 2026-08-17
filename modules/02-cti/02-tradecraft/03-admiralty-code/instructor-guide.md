# Instructor Guide – Module 3.2.3 – Admiralty Code

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.2.3 A / A / B · 3.2.3.1 1a / 1a / 2b  
- Hunter: 3.2.3 A / B / B · 3.2.3.1 1a / 2b / 3c  
- CTI: 3.2.3 B / C / C · 3.2.3.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach A–F, 1–6, and the pair. Force **assign** and **explain**. Do not teach estimative terms or ACH.

**Key Teaching Points:**
- Classroom glosses are a stand-in. Overlay the site card if you have one.
- Two axes. **F1** and **B3** are the teaching pairs.
- **A1** is the usual vanity fail.
- SOC 3-level task is **1a / 1a / 2b**. Hunter 3-level is **1a**. CTI is **3c / 4d**. Do not collapse.
- *Likely* is **3.2.1**. *Medium confidence* is **3.1.7**. Do not let them substitute.

**Common Student Challenges:**
- Rating the *story they want* instead of source vs report.
- A1 on a first-time blog.
- Throwing away F sources.
- One code for a paragraph that contains two claims (hash vs country).

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site Admiralty / source-eval card
- Answer key (this guide)

---

## Learning Objectives

1. Source scale A–F.
2. Information scale 1–6.
3. Combine.
4. Assign + explain.

**Mapped Items:** K 3.2.3 · T 3.2.3.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.2.1 / 3.2.2 / 3.1.7 |
| Two scales + combine           | 16 min   | a–c |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Assign + explain |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they defend A1 |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they should *split* source and claim, not recite the table.
- Put **F1** and **B3** on the board and leave them up.

**Question:**  
“If Zeek is **B** and the country claim is untested, what is *wrong* with writing **B1**?” (You rated the *sensor* and then gave the *label* a 1 it did not earn.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail A1 on B. Fail one code covering hash + China. Accept B/C range if the reason is clean.

**Summaries:**
- Ex 1: B3.
- Ex 2: A1 rejected; F6 (or F5) on the country line.
- Ex 3: F1 on the confirmed hash; label rated separately.

**Assign:**

| Item | Source | Info | Code | Notes |
|------|--------|------|------|-------|
| A | **B** (known lead) | **1** (ticket + EDR independent) | **B1** | Isolate *fact*, not a Night Owl label |
| B | **F** | **6** or **5** | **F6** / **F5** | No internals; nation-state slogan |
| C | **C** (mixed paid vendor) | **3** | **C3** | No internal look yet |
| D | **C** | **1** | **C1** | Now independently confirmed internally. Source letter does **not** jump to A |

Accept **B** on C if they argue this TIP has a *local* good record — they must say so. Fail **A** on C or D.

**Explain:**

| Item | Letter | Number |
|------|--------|--------|
| E **C4** | Fairly reliable source | This report is doubtful |
| F **F1** | Cannot judge the source | This *claim* is independently confirmed |

---

## Knowledge Check – Answer Key

1. **Letter vs number?**  
   **Answer:** Letter = source reliability (track record). Number = credibility of *this* information.  
   **Explanation:** Outline a–b.

2. **When F or 6?**  
   **Answer:** No track record, or no way to test the claim. Do not guess A or 1.  
   **Explanation:** Outline a–b; F/6 rows.

3. **Why F1?**  
   **Answer:** Unknown source; *this* fact confirmed independently. Two axes.  
   **Explanation:** Outline c / Example 3.

4. **Why not A1 on a vendor PDF?**  
   **Answer:** No local reliability record; the headline is not independently confirmed.  
   **Explanation:** Example 2.

5. **B2 vs likely / medium?**  
   **Answer:** B2 = source usually reliable, report probably true. *Likely* is event probability (**3.2.1**). *Medium* is evidence quality on an attribution (**3.1.7**).  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Site source-evaluation card
- Next recommended module: 3.2.4 Cognitive biases and mitigation
