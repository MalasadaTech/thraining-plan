# Instructor Guide – Module 1.4.3 – Common False Positive Causes

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.3.1 A / B / C · 1.4.3.2 2b / 3c / 4c  
- Hunter: 1.4.3.1 B / C / C · 1.4.3.2 2b / 3c / 4c  
- CTI: 1.4.3.1 A / A / B · 1.4.3.2 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
On an already-labeled FP, pick cause class **a** or **b** and name a change. Do not reclassify. Do not deploy.

**Key Teaching Points:**
- Starts after **1.4.2**.
- Two classes only (plus “other — not a/b”).
- Change = one concrete sentence.
- Example 3: primary class is the event in front of you.

**Common Student Challenges:**
- Relitigating TP.
- “Tune it” with no selector.
- Calling live user activity “analyst.”
- Writing a full SIGMA and calling that this lesson.
- Opening **1.4.4**.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Name classes a and b.
2. Given an FP: class + change.

**Mapped Items:** K 1.4.3.1 · T 1.4.3.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | After FP |
| Two classes                    | 12 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~62 min** | Stretch Ex 3 if they force both equally |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: name a vs b and a templated change.
- Hunter: 2b at 3-level — primary class + a usable change.
- CTI: 1a / 1a / 2b. 7-level can name a change.

**Question:**  
“If we removed the analyst from this story, would this still fire on a user?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail TP. Fail “tune it.” Fail a category.

**Summaries:**
- Ex 1: **a** — exclude/tag replay; keep the sid.
- Ex 2: **b** — add `-enc` + script-host parent.
- Ex 3: primary **a** — don’t test in prod; optional second ticket for export filter (**b**).

**Cases:**

| Item | Class | Change (equivalent is fine) |
|------|-------|------------------------------|
| A | **b** | Use `http.method` + `http.uri` (or drop raw TCP GET). |
| B | **a** | Hunter sample-download: lab net / allow-list hunter workstation during the run. |
| C | **b** | Do not alert on MZ-only; require a second string or detach YARA from the SIEM rule. |
| D | **a** | Allow-list scanner `10.10.8.90` (documented). Mention **b** only if they also want the Office rule tighter — not required. |

---

## Knowledge Check – Answer Key

1. **Two classes?**  
   **Answer:** (a) analyst or tool activity; (b) untuned or overly broad logic.  
   **Explanation:** Outline a–b.

2. **Why not classify again?**  
   **Answer:** The case is already an FP. This unit is cause + change.  
   **Explanation:** Fence with 1.4.2.

3. **Acceptable change?**  
   **Answer:** One concrete action (add selector, exclude lab range, detach MZ-only). Not “tune it.”  
   **Explanation:** Task.

4. **Other?**  
   **Answer:** When it is not a/b (clock skew, bad intel). Say “other — not a/b” and still name a change. Do not invent a third official class.  
   **Explanation:** Stay inside syllabus.

5. **Who deploys?**  
   **Answer:** Detection Engineering. SOC proposes (**1.3** ceiling).  
   **Explanation:** Same as 1.3.

---

## Additional Instructor Resources

- Next recommended module: 1.4.4 Common alert categorizations
