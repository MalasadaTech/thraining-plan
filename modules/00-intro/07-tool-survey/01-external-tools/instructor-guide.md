# Instructor Guide – Module 3.3.2 – External Tools

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.3.2 A / B / B · 3.3.2.1 1a / 2b / 3c  
- Hunter: 3.3.2 B / C / C · 3.3.2.1 3c / 4c / 4d  
- CTI: 3.3.2 B / C / C · 3.3.2.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the four-tool card and force **select + one hop**. Close **3.3**. Do not teach 2.3.1 SIEM conversion or 3.9 Relations.

**Key Teaching Points:**
- Card is a stand-in for *when*, not a vendor cert.
- TIP first for internal presence (**3.3.1**).
- One hop = this lesson’s “advanced.” Graphs = **3.9**.
- Hunter 3-level is already **3c / 4d** on the task (same as CTI). SOC is **1a / 2b / 3c**. Do not collapse.
- Live demos are optional; the sign-off is the select/pivot *lines*.

**Common Student Challenges:**
- URLScan for PDNS.
- AnyRun with no file.
- VT for “have we seen it?”
- 12-hop Relations.
- Writing a Zeek query (2.3.1).

**Required Materials:**
- Student Guide
- Slide Deck
- Optional live tools (sanitized hash/URL)
- Answer key (this guide)

---

## Learning Objectives

1. Purpose / strength / weakness of each.
2. When in the intel process.
3. Select + reject neighbor.
4. One hop.

**Mapped Items:** K 3.3.2 · T 3.3.2.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.3.1 / 2.3.1 / 3.9 |
| Four-tool card + when          | 16 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Select + hop |
| Knowledge Check & Discussion   | 8 min    | Close 3.3 |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they defend URLScan |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they should *name the hop*, not “I would enrich it.”
- If you demo, stop after **one** click off the hash.

**Question:**  
“You pivoted VT → domain. You now want history. Is that the same hop or a new select?” (New select: Silent Push.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail C as VT. Fail URLScan on D. Fail AnyRun on A.

**Summaries:**
- Ex 1: VT + one contacted domain/file.
- Ex 2: Silent Push, not URLScan.
- Ex 3: no AnyRun without a sample.

**Select:**

| Item | Tool | Reject | Why |
|------|------|--------|-----|
| A | **URLScan** | AnyRun / Silent Push | Live page now |
| B | **AnyRun** | VT-only (VT can *precede* but behavior needs detonation) | Have a binary |
| C | **3.3.1 TIP** | All four | Internal presence |
| D | **Silent Push** | URLScan / VT as first | Infra cluster / history |

**Pivot:**

| Item | Query | One hop | For |
|------|-------|---------|-----|
| A | The live URL in URLScan | Redirect or contacted host | Page infra *this load* |
| B | Submit `update.exe` | Dropped hash or C2 host | Behavior |
| D | `nightowl-updates.net` in Silent Push | Historical A or sibling | Cluster |

---

## Knowledge Check – Answer Key

1. **Strength / weakness each?**  
   **Answer:** VT: coverage / public+no PDNS. AnyRun: behavior / needs file+evasion. Silent Push: history / not a sandbox. URLScan: live page / not PDNS.  
   **Explanation:** Outline a.

2. **Silent Push vs URLScan?**  
   **Answer:** History / cluster → Silent Push. Live page now → URLScan.  
   **Explanation:** Outline b / Example 2.

3. **VT hop vs 3.9?**  
   **Answer:** One contacted domain or communicating file. 3.9 is Relations/Behavior depth.  
   **Explanation:** Fence.

4. **Internal presence?**  
   **Answer:** **3.3.1** TIP, not these four.  
   **Explanation:** Fence / C.

5. **Hunt / SIEM query?**  
   **Answer:** **2.3.1**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Local licenses / safe-demo IOCs
- Cluster **3.3** is complete. Next: **3.4** File similarity and hashing
