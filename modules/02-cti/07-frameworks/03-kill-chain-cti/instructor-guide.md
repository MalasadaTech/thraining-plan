# Instructor Guide – Module 3.7.3 – Cyber Kill Chain in Intelligence Analysis

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.7.3 A / B / B · 3.7.3.1 2b / 3c / 4c  
- Hunter: 3.7.3 B / C / C · 3.7.3.1 3c / 4c / 4c  
- CTI: 3.7.3 B / C / C · 3.7.3.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Advanced Kill Chain for CTI: place a **report/activity set** on the seven stages, reject previous/next, list only **supported** stages in the product, reject unobserved Weaponization and Actions on Objectives.

**Key Teaching Points:**
- Do not re-teach the 0.6.3 seven-stage tour. One recap sentence, then the excerpt.
- GET `update.exe` is **Delivery** on the chain even if **3.7.1** mapped it to T1105 / T1071.001. Frameworks do not share labels.
- SOC K is **A / B / B** (not A/B/C). Task **2b / 3c / 4c**. Hunter/CTI **3c / 4c / 4c** (not 4d — that is Diamond / DTF). Do not collapse.
- Do not copy `modules/00-intro/06-frameworks/` into this folder.

**Common Student Challenges:**
- Collapsing the whole set to Actions on Objectives.
- Inventing Weaponization.
- Calling the GET **C2** because ATT&CK used T1071.001 (beacon POST is C2; this GET is the drop).
- Putting ATT&CK IDs or Diamond vertices on the stage line.
- Treating 1.4.4 categories as stages.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Kill Chain on an intelligence problem (report / activity set).
2. Stage + reject previous/next + product list.
3. Reject unobserved stages.

**Mapped Items:** K 3.7.3 · T 3.7.3.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 0.6.3 redo / 3.7.1 / 3.7.2 |
| Advanced place + product use   | 14 min   | a |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Stage lines |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep T1486 as stage 7 |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they already staged single rows in 0.6.3. Push **set + product list**.
- If they put GET on C2: ask whether the row is a *channel* (beacon) or a *drop* (file GET). Harbor excerpt is the drop.
- Product order is **chain order** (Delivery, Exploitation, Installation), not excerpt order.

**Question:**  
“The vendor listed T1486. What would have to appear in the Harbor excerpt before Actions on Objectives is legal *here*?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail Actions on Objectives from T1486. Fail invented Weaponization. Fail GET as C2 unless they can show a beacon. Fail ATT&CK IDs on the stage line.

**Summaries:**
- Ex 1: three supported stages with neighbors.
- Ex 2: uncited T1486 ≠ Actions on Objectives.
- Ex 3: Weaponization stays **not observed**.

**Stage lines:**

| Item | Stage | Reject | Notes |
|------|-------|--------|-------|
| A | **Exploitation** | Delivery / Installation | Encoded PS running; persist is B |
| B | **Installation** | Exploitation / C2 | Run key cited; no channel |
| C | **Delivery** | Weaponization / Exploitation | File GET, not a beacon |
| D | **None / not observed** | — | Reported, not observed |
| E | **None / not observed** | — | Invented builder |

**Product list:** `Delivery, Exploitation, Installation` (drop any they cannot cite).

---

## Knowledge Check – Answer Key

1. **Advanced vs 0.6.3?**  
   **Answer:** Report or activity set; several spans; only supported stages in the *intel product*; reject unobserved stages. 0.6.3 stages a single row.  
   **Explanation:** Outline a.

2. **Stage line besides the stage?**  
   **Answer:** Evidence span, not previous because, not next because.  
   **Explanation:** Task.

3. **Why not vendor T1486 as Actions on Objectives?**  
   **Answer:** Not in *this* evidence. Uncited stage 7 stays out of this product.  
   **Explanation:** Example 2.

4. **Why is Weaponization usually not observed?**  
   **Answer:** Pairing exploit + payload happens off your network. “They must have built it” is not a product stage.  
   **Explanation:** Example 3.

5. **ATT&CK tactic ≠ Kill Chain stage?**  
   **Answer:** ATT&CK is a behavior matrix (IDs). Kill Chain is an ordered progression. Same GET can be Delivery here and T1105 in **3.7.1**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Intelligence-Driven Computer Network Defense (lookup)
- Next recommended module: 3.7.4 MalasadaTech Defender’s ThreatMesh Framework (DTF)
