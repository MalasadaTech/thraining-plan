# Instructor Guide – Module 3.7.1 – MITRE ATT&CK for CTI Analysis and Reporting

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.7.1 A / B / B · 3.7.1.1 2b / 3c / 4c  
- Hunter: 3.7.1 B / C / C · 3.7.1.1 3c / 4c / 4c  
- CTI: 3.7.1 B / C / C · 3.7.1.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Advanced ATT&CK for CTI: extract TTPs from a **report/activity set**, map to **real IDs**, cite, reject the neighbor, list only supported IDs in the product.

**Key Teaching Points:**
- Do not re-teach the 1.5.1 matrix tour. One recap sentence, then the excerpt.
- Do not invent T-IDs. Blank is better than `T9999`.
- Vendor ID dumps fail without local evidence.
- SOC 3-level K is **A / B / B** (not A/B/C). Task **2b / 3c / 4c**. Hunter/CTI **3c / 4c / 4c**. Do not collapse.
- Do not copy `modules/00-intro/06-frameworks/` into this folder.

**Common Student Challenges:**
- Mapping motive / “APT” to a tactic.
- Pasting the vendor’s matrix.
- Stopping at `T1059` when `.001` is in the evidence.
- Opening 2.5 Navigator or 3.8.2 applicability.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional ATT&CK site for lookup (not a dump)
- Answer key (this guide)

---

## Learning Objectives

1. ATT&CK in CTI analysis and reporting.
2. Extract → map → cite → reject neighbor.
3. Product lists only supported IDs.

**Mapped Items:** K 3.7.1 · T 3.7.1.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 1.5.1 redo / 2.5 / 3.8.2 |
| Advanced extract + report use  | 14 min   | a |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Map lines |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 3 if they keep T1486 |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they already mapped alerts in 1.5.1. Push **sub-technique + reject + product line**.
- C can be T1071.001 **and** T1105. That is not fence-sitting if both behaviors are in the GET.

**Question:**  
“The vendor listed T1486. What would have to appear in the Harbor excerpt before that ID is legal *here*?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail invented IDs. Fail APT→Impact. Fail uncited T1486 / DNS C2.

**Summaries:**
- Ex 1: four supported IDs with neighbors.
- Ex 2: no behavior → no tactic.
- Ex 3: vendor T1486 stays out.

**Maps:**

| Item | ID | Reject | Notes |
|------|-----|--------|-------|
| A | **T1059.001** | T1059.003 | Encoded PowerShell |
| B | **T1547.001** | Startup folder / .009 | Run key cited |
| C | **T1071.001** and/or **T1105** | T1071.004 | HTTP GET payload |
| D | **None** | — | Reported, not observed |
| E | **None** | Any tactic | Label, not a TTP |

**Product line:** `T1059.001, T1547.001, T1071.001, T1105` (drop any they cannot cite).

---

## Knowledge Check – Answer Key

1. **Advanced vs 1.5.1?**  
   **Answer:** Report or multi-event story; sub-technique; neighbor reject; only supported IDs in the *intel product*. 1.5.1 maps an alert.  
   **Explanation:** Outline a.

2. **Map line besides the ID?**  
   **Answer:** Evidence span, tactic, name, rejected neighbor, why.  
   **Explanation:** Task.

3. **Why not vendor T1486?**  
   **Answer:** Not in *this* evidence. Uncited IDs stay out of this product.  
   **Explanation:** Example 3.

4. **Why not “APT” → tactic?**  
   **Answer:** Motive / marketing name is not a behavior.  
   **Explanation:** Example 2.

5. **Harbor applicability?**  
   **Answer:** **3.8.2**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- ATT&CK Enterprise (lookup)
- Next recommended module: 3.7.2 Diamond Model in CTI
