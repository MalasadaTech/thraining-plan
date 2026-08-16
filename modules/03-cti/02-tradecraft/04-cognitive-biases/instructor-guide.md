# Instructor Guide – Module 3.2.4 – Cognitive Biases and Mitigation

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.2.4 A / A / A · 3.2.4.1 1a / 1a / 1a  
- Hunter: 3.2.4 A / B / B · 3.2.4.1 1a / 2b / 3c  
- CTI: 3.2.4 B / C / C · 3.2.4.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach four common biases, their impact, and force **identify + mitigate**. Close **3.2**. Do not re-teach the ACH matrix or Admiralty.

**Key Teaching Points:**
- Classroom four is a stand-in. Overlay a site list if you have one — sign-off is still these four plus a *step*.
- “Be aware” is a fail.
- ACH/KAC are mitigations you *invoke*, not this hour’s fill-the-grid drill.
- SOC 3-level is **1a / 1a / 1a**. Hunter 3-level is **1a**. CTI is **3c / 4d**. Do not collapse.

**Common Student Challenges:**
- Reciting ten extra bias names.
- Naming a bias with no textual tell.
- Re-running a full ACH instead of stating the mitigation step.
- Opening 3.2.3 on every example.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site bias card
- Answer key (this guide)

---

## Learning Objectives

1. Four biases + impact.
2. Identify in a judgment.
3. Apply a concrete mitigation.

**Mapped Items:** K 3.2.4 · T 3.2.4.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.2.2-as-lesson / 3.2.3 |
| Four biases, impact, mitigations | 16 min | a–c |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Identify + apply |
| Knowledge Check & Discussion   | 8 min    | Close 3.2 |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they stay on China/Admiralty |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they should *point at a sentence* and *name a next action*.
- If they list “mirror imaging,” map it to **availability** or **anchoring** unless you overlay it.

**Question:**  
“If the product already ran ACH and still omitted E4–E5, is that SAT failure or confirmation?” (Both. This hour you name **confirmation** and the mitigation is *put E4–E5 on the matrix*.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail nameless “bias.” Fail “be aware.” Accept one clearly argued neighbor bias.

**Summaries:**
- Ex 1: confirmation → ACH / add omitted rows.
- Ex 2: anchoring → rewrite without the first label.
- Ex 3: availability + closure → base rate + KAC.

**Identify:**

| Item | Bias | Tell |
|------|------|------|
| A | **Confirmation** | E4–E5 in the file, unused |
| B | **Anchoring** | APT-12 lead never revisited |
| C | **Premature closure** (availability if they argue vivid Night Owl) | Isolate + almost certainly on one guest SNI |
| D | **Anchoring** or **confirmation** | “Always” OT visibility — untested must-be; also a **1.8.1** fact. Prefer **premature closure** / untested assumption if they say KAC |

**Apply:**

| Item | Mitigation | Next action (accept paraphrase) |
|------|------------|--------------------------------|
| A | ACH / hunt **I** | Add E4–E5 to the matrix before rewrite |
| C | KAC + drop *almost certainly* | Test “one SNI ⇒ Night Owl”; do not isolate on that alone |

---

## Knowledge Check – Answer Key

1. **Four biases / one impact?**  
   **Answer:** Confirmation, anchoring, availability, premature closure. Impact: omitted evidence, stuck first label, vivid-case carryover, *is*/isolate too early.  
   **Explanation:** Outline a–b.

2. **Why not “be aware”?**  
   **Answer:** It is not a step. Mitigation names what you will *do*.  
   **Explanation:** Outline c / task 2.

3. **Confirmation mitigation?**  
   **Answer:** Small ACH; require a hunt for evidence that would **I** the favorite.  
   **Explanation:** Table / Example 1.

4. **Vs 3.2.2?**  
   **Answer:** 3.2.2 is how to run ACH/KAC. This hour is *spot the tilt* and *invoke* a technique (or another step).  
   **Explanation:** Fence.

5. **What cluster closes?**  
   **Answer:** **3.2** Analytic tradecraft. Next is **3.3** Tools.  
   **Explanation:** Sequence.

---

## Additional Instructor Resources

- Site bias / tradecraft card
- Cluster **3.2** is complete. Next: **3.3.1** Internal TIP
