# Instructor Guide – Module 3.8.2 – Extracting Applicable TTPs from Intelligence Reports

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.8.2 A / B / B · 3.8.2.1 1a / 2b / 3c  
- Hunter: 3.8.2 B / C / C · 3.8.2.1 3c / 4c / 4d  
- CTI: 3.8.2 B / C / C · 3.8.2.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Two gates: **relevant in the report** (3.7.1), then **applicable on Harbor** (platform + path from **1.8.1**). Extract only IDs that pass both.

**Key Teaching Points:**
- Do not re-teach the 3.7.1 map. One recap: uncited IDs still fail gate 1.
- Harbor facts are **lesson-only**. If the site posts a real card, swap platform/path; keep the two gates.
- SOC K is **A / B / B**. Hunter/CTI task **3c / 4c / 4d**. 4d is *why* Unix/ESXi fail, not a longer ID list.
- Visibility ≠ applicability. Zeek `dns` does not rescue T1071.004.
- Impact / Sev / pay-db-01 is **3.8.4**. Do not go there.
- Do not invent T-IDs.

**Common Student Challenges:**
- Copying the vendor matrix because “we have computers.”
- Marking T1486 applicable because ransomware is scary (**3.8.4**).
- Using Zeek `dns` to pass a footnote T1071.004.
- Re-doing 3.7.1 neighbor rejects instead of Harbor facts.
- Opening 2.5 Navigator.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)
- Optional: 1.8.1 Harbor card

---

## Learning Objectives

1. Relevant TTP in the report (gate 1).
2. Harbor platform + path (gate 2).
3. Product lists only dual-pass IDs.

**Mapped Items:** K 3.8.2 · T 3.8.2.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 3.7.1 redo / 2.5 / 3.8.4 |
| Two gates + Harbor criteria    | 14 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Apply lines |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep ESXi T1486 |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they already mapped IDs. Push **Harbor fact on the apply line**.
- 4d: “no ESXi on the card” is the reason, not “ransomware is out of scope forever.” A later report with Windows T1486 *and a how* would pass gate 1 and likely gate 2.
- T1059.001 vs T1059.004 is a **platform** reject, not a 3.7.1 neighbor reject (that was .001 vs .003).

**Question:**  
“Harbor has Zeek `dns`. What else would T1071.004 need before it is legal *here*?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail D and E. Fail invented IDs. Fail “everything applies.” If they add T1071.004, fail gate 1.

**Summaries:**
- Ex 1: four Windows/HTTP IDs.
- Ex 2: Unix/ESXi fail platform.
- Ex 3: footnote fails gate 1.

**Apply lines:**

| Item | T-ID | Apply | Harbor fact |
|------|------|-------|-------------|
| A | **T1059.001** | **Yes** | Windows endpoints |
| B | **T1547.001** | **Yes** | Windows Run keys |
| C | **T1071.001** and **T1105** | **Yes** | HTTP egress + Zeek `http` |
| D | T1059.004 | **No** | No Unix user fleet |
| E | T1486 (ESXi) | **No** | No ESXi on the card |

**Product line:** `T1059.001, T1547.001, T1071.001, T1105`

---

## Knowledge Check – Answer Key

1. **Different from 3.7.1?**  
   **Answer:** 3.7.1 asks what the report *supports*. This hour asks which of those TTPs **apply on Harbor** (platform + path).  
   **Explanation:** Outline a–b.

2. **Two gates?**  
   **Answer:** Relevant in the report (behavior + how). Applicable here (Harbor platform + path).  
   **Explanation:** Task.

3. **Why not T1059.004?**  
   **Answer:** Unix Shell. Harbor user endpoints are Windows. Platform miss.  
   **Explanation:** Example 2.

4. **Why not T1071.004 from Zeek `dns`?**  
   **Answer:** Gate 1 failed — footnote about other campaigns, no how *here*. Visibility does not rescue it.  
   **Explanation:** Example 3.

5. **Organizational impact?**  
   **Answer:** **3.8.4**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- 1.8.1 Harbor card
- Next recommended module: 3.8.3 IOC handling and enrichment concepts
