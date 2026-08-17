# Instructor Guide – Module 1.4.5 – SLA / Response Time Goals

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.5.1 A / B / C · 1.4.5.2 2b / 3c / 4c · 1.4.5.3 2b / 3c / 4c  
- Hunter: 1.4.5.1 A / B / B · 1.4.5.2 1a / 2b / 3c · 1.4.5.3 1a / 2b / 3c  
- CTI: 1.4.5.1 A / A / A · 1.4.5.2 1a / 1a / 1a · 1.4.5.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach two clocks. Students name which is at risk and write a close/escalate record. Classroom 15 / 45 unless you substitute site numbers. Closes **1.4**.

**Key Teaching Points:**
- Start from **created**. Close/escalate from **started**.
- Untouched → only start can be at risk.
- Record four fields. Not a ticketing-admin class.
- Hunter A / 1a at 3-level (secondary). CTI A / 1a only.

**Common Student Challenges:**
- One blended “we’re late.”
- Closing an untouched alert to “meet SLA.”
- Using created as the close-escalate origin.
- Relitigating TP/category.
- Grading CTI as SOC 5.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional: site SLA card to overlay
- Answer key (this guide)

---

## Learning Objectives

1. Explain both clocks.
2. Given timestamps, which clock is at risk.
3. Record close or escalate against the correct clock.

**Mapped Items:** K 1.4.5.1 · T 1.4.5.2 · T 1.4.5.3

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & two clocks      | 10 min   | a–b; 15 / 45 |
| At-risk vs record              | 10 min   | |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Close 1.4 |
| **Total**                      | **~62 min** | Stretch Ex 2 if they close without starting |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: A / 2b — name the clock and copy the record line.
- Hunter 3: A / 1a — recognize the two clocks.
- CTI: A / 1a.

**Question:**  
“Has anyone touched it? If no, which clock even exists?”

Substitute site numbers on the board if you have them. Keep two clocks.

---

## Hands-On Exercise – Instructor Guidance

**Now = 15:00.** Start 15 / close-escalate 45.

**Summaries:**
- Ex 1: both OK; closed on close-escalate clock.
- Ex 2: **start** breached; record started, do not close yet.
- Ex 3: **close/escalate** breached; escalate (or close if done).

**Cases:**

| Item | Clock | Record (equivalent is fine) |
|------|-------|------------------------------|
| A | **Start** at risk (10 min, still inside 15) | `A | started | start (ok) | 15:00` |
| B | **Close/escalate** breached (110 min since start) | `B | escalated | close-escalate (breached) | 15:00` (close also OK if they finished the card) |
| C | Both OK; they can close | `C | closed | close-escalate (ok) | 15:00` |
| D | Close/escalate still OK (35 min); escalate by choice | `D | escalated | close-escalate (ok) | 15:00` |

Fail a close on A with no start. Fail “late” with no clock name.

---

## Knowledge Check – Answer Key

1. **Two clocks?**  
   **Answer:** Start = created → first touch (classroom 15 min). Close/escalate = first touch → closed or escalated (classroom 45 min).  
   **Explanation:** Outline a–b.

2. **Untouched?**  
   **Answer:** Only the **start** clock. Close/escalate has no origin yet.  
   **Explanation:** Task 1.

3. **Not “work faster”?**  
   **Answer:** You name *which* clock and record a disposition against it. Speed without a clock is not the task.  
   **Explanation:** Old restating task removed.

4. **Record fields?**  
   **Answer:** alert id, disposition (closed/escalated/started), which clock, timestamp.  
   **Explanation:** Task 2.

5. **Live numbers?**  
   **Answer:** The site SLA card. Classroom 15/45 are for this lesson only.  
   **Explanation:** Do not invent org policy.

---

## Additional Instructor Resources

- Site SLA card if you have one
- Next recommended module: 0.6.1 MITRE ATT&CK
