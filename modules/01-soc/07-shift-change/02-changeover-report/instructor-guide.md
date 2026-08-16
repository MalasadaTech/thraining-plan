# Instructor Guide – Module 1.7.2 – Required Content of the Changeover Report

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.7.2.1 A / B / C · 1.7.2.2 2b / 3c / 4c  
- Hunter: 1.7.2.1 A / B / B · 1.7.2.2 1a / 2b / 3c  
- CTI: 1.7.2.1 A / A / A · 1.7.2.2 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the five required buckets. Force a **complete report** and a rejected missing-element draft. Close **1.7**.

**Key Teaching Points:**
- Silence ≠ none. They write **none**.
- Planned (c) and occurred (d) are different.
- Policy (e) is its own line, not a clause on A12.
- Hunter 3-level task is **1a**. CTI is **1a** at all three levels. Do not collapse to SOC 2b/3c/4c.
- Overlay a site template if you have one — keep the five outline buckets.

**Common Student Challenges:**
- Open-ticket list only.
- Mixing planned and occurred outages.
- Burying the 15:00 IR-concurrence rule inside A12.
- Rewriting the incident body.
- Re-doing the 1.7.1 handoff line.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site changeover template
- Answer key (this guide)

---

## Learning Objectives

1. Name the five buckets.
2. Produce all five (or explicit none).
3. Reject a missing-element draft.

**Mapped Items:** K 1.7.2.1 · T 1.7.2.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 1.7.1 / 1.6 / 1.8 |
| Five buckets                   | 14 min   | a–e |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | They write the report |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Close 1.7 |
| **Total**                      | **~64 min** | Stretch Ex 2 if they defend “open tickets” |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: 2b — fill the template from a fact sheet with guidance.
- Accept paraphrase of Example 1 if all five buckets are present and facts are not swapped.
- Fail a beautiful A12 narrative that skips outages and policy.

**Question:**  
“If nothing planned is on the board, do you omit the line?” (No. Write `Planned outages: none`.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail open-tickets-only. Fail swapped planned/occurred. Fail missing policy.

**Summaries:**
- Ex 1: all five lines.
- Ex 2: missing b, c, d, e.
- Ex 3: c/d collapsed; e buried in A12.

**Complete report (accept paraphrase):**

| Bucket | Must include |
|--------|----------------|
| Open | A12 WS-JLEE (IR has host); RFI CTI / nightowl-updates.net waiting |
| Opened / updated / closed | Informational TN PDF opened+closed; HelpdeskSvc FP closed |
| Planned | EDR 02:00–03:00 tomorrow, 10.10.8.0/24 |
| Occurred | Zeek span-2 13:10–13:40, recovered; no PCAP that window |
| Policy | Do not close Night Owl-related cases without IR concurrence |

**Cases:**

| Item | Call |
|------|------|
| A | Missing opened/closed detail beyond HelpdeskSvc (TN PDF), planned, occurred, policy. **Incomplete.** |
| B | Missing **e** (policy). **Incomplete.** |
| C | **d** is false — Zeek drop is in the fact sheet. **Incomplete / inaccurate.** |
| D | **c** and **d** **swapped**. Facts exist, elements misplaced. **Reject** as not matching required elements. |

---

## Knowledge Check – Answer Key

1. **Five buckets?**  
   **Answer:** Open / in-progress; opened-updated-closed this shift; planned outages; ongoing or occurred-this-shift outages; urgent process or policy.  
   **Explanation:** Outline a–e.

2. **Empty bucket?**  
   **Answer:** Write **none**. Do not omit the line.  
   **Explanation:** Completeness.

3. **Why planned ≠ occurred?**  
   **Answer:** Incoming crew plans around *upcoming* windows and *already lost* visibility separately.  
   **Explanation:** Outline c vs d; Example 3.

4. **Why not just open tickets?**  
   **Answer:** That is only bucket a. Closes, outages, and policy still required.  
   **Explanation:** Task / Example 2.

5. **Where recorded / which lesson?**  
   **Answer:** System of record from **1.7.1** (classroom: `SOC-CHANGEOVER`). This lesson is the *content*.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Site changeover template
- Next recommended module: 1.8.1 Environment orientation
