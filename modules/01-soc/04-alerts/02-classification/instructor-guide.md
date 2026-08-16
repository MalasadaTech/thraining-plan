# Instructor Guide – Module 1.4.2 – Alert Classification

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.2.1 A / B / C · 1.4.2.2 2b / 3c / 4c  
- Hunter: 1.4.2.1 B / C / C · 1.4.2.2 2b / 3c / 4c  
- CTI: 1.4.2.1 A / A / B · 1.4.2.2 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the four labels and force **cases + evidence**, including a **missed detection (FN)**. Do not teach FP *causes*.

**Key Teaching Points:**
- TP/FP need a fired detection. TN/FN usually do not.
- FN ≠ “I hate this alert.”
- Evidence is a cite, not a slogan.
- Park **1.4.3** the moment they say “over-broad rule.”

**Common Student Challenges:**
- Labeling a miss as FP.
- Inventing a queue row for TN/FN.
- Classifying without a cite.
- Writing the cause class on Example 2.
- Grading CTI as SOC 5 (1a / 1a / 2b on the task).

**Required Materials:**
- Student Guide
- Slide Deck
- 2×2 on the board: detection said bad/not × reality bad/benign
- Answer key (this guide)

---

## Learning Objectives

1. Define the four labels.
2. Classify cases and cite evidence.
3. Treat FN as a missed detection.

**Mapped Items:** K 1.4.2.1 · T 1.4.2.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & 2×2             | 8 min    | FN off the queue |
| Definitions + evidence         | 12 min   | a–d |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Five cases |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~64 min** | Stretch FN if they call it FP |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: A / 2b — get the 2×2 right and one cite.
- Hunter: B / 2b at 3-level. Push FN from logs with no alert.
- CTI: nomenclature + simple classify at 7 (2b).

**Draw:** Detection fired? Y/N. Activity bad? Y/N. Four cells.

**Examples:** Ex 1 TP. Ex 2 FP (park cause). Ex 3 FN + mention TN intranet PDF.

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail “FN = bad alert.” Fail a 1.4.3 paragraph. Fail no-cite.

**Summaries:**
- Ex 1: TP — encoded PS from wscript occurred.
- Ex 2: FP — Get-Help under explorer; cite the cmdline.
- Ex 3: FN — GET update.exe on 8080, no fire.

**Cases:**

| Item | Label | Evidence (accept equivalents) |
|------|-------|-------------------------------|
| A | **TP** | Unexpected Office → cmd; rule is for that parent/child. |
| B | **TN** | Documented export script; no alert; correctly quiet. (If they say FP they invented an alert.) |
| C | **FN** | Same download, no alert. Miss. |
| D | **FP** | Lab replay, not a live user. Fired, activity is authorized test traffic. Cause class → 1.4.3. |
| E | **TN** | Intranet PDF, no alert. |

If a student calls B **FP**, they added a phantom alert — correct them.

---

## Knowledge Check – Answer Key

1. **Four labels?**  
   **Answer:** TP = fired + bad. FP = fired + benign. TN = quiet + benign. FN = quiet + bad.  
   **Explanation:** Outline a–d.

2. **Why FN is not a queue row?**  
   **Answer:** FN means no detection fired. The object is the missed activity (log/PCAP/hunt), not an alert you re-label.  
   **Explanation:** Task must include a miss.

3. **Evidence?**  
   **Answer:** A concrete cite (parent, cmdline, URI, “no sid for 8080”). Not “malicious.”  
   **Explanation:** Task wording.

4. **TN that is never a ticket?**  
   **Answer:** Expected browsing or a documented business script with no alert.  
   **Explanation:** Example TN / case E.

5. **Stop vs next?**  
   **Answer:** This lesson stops at FP + cite. Why it fired and what to change is **1.4.3**.  
   **Explanation:** Unit fence.

---

## Additional Instructor Resources

- Next recommended module: 1.4.3 Common false positive causes
