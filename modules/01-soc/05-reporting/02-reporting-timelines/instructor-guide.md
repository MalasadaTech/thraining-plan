# Instructor Guide – Module 1.6.2 – Reporting Timelines

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.6.2.1 A / B / C · 1.6.2.2 2b / 3c / 4c  
- Hunter: 1.6.2.1 A / B / B · 1.6.2.2 2b / 3c / 4c  
- CTI: 1.6.2.1 B / C / C · 1.6.2.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach report **submit** clocks by type and **blocked → escalate**. Force **which clock + met/at risk/breached**. Do not teach 1.4.5 alert clocks as the answer.

**Key Teaching Points:**
- Classroom: incident 30, RFI 60, informational before changeover, blocked 15.
- Origins differ: decision vs question vs blocked-at.
- Hunter K is A/B/B (lower than types). CTI task 3c at 3-level.

**Common Student Challenges:**
- Using alert 15/45.
- Scoring RFI on the 30-minute incident clock.
- Ignoring the blocked clock and only watching submit.
- Routing the report.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site reporting-SLA card
- Answer key (this guide)

---

## Learning Objectives

1. Submit-by-type and escalate-when-blocked.
2. Which clock + at risk.

**Mapped Items:** K 1.6.2.1 · T 1.6.2.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction vs 1.4.5          | 8 min    | |
| Two outline clocks             | 12 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~62 min** | Stretch Ex 3 if they sit on submit |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: name the clock and do the subtraction.
- Overlay site numbers if you have them. Keep submit vs blocked as two *kinds*.

**Question:**  
“Are you blocked, or just slow to write?”

---

## Hands-On Exercise – Instructor Guidance

**Now = 15:00.**

**Summaries:**
- Ex 1: submit-incident met (22).
- Ex 2: submit-RFI breached (70).
- Ex 3: escalate-for-more-info breached (18 from 14:10).

**Cases:**

| Item | Clock | Status |
|------|-------|--------|
| A | Submit — incident (30 from 14:40) | **Met / not yet at risk** (20 min). Accept **OK**. |
| B | Submit — RFI (60 from 14:00) | **Met** on the nose (60). Accept **met** or **at risk** if they use last-third; 60 exactly = met. |
| C | Submit — informational (before 16:00) | **OK** (60 min left). |
| D | Escalate-for-more-info (15 from 14:35) | **Breached** (25 min blocked). Submit-incident still open (40 from 14:20) but they must name **blocked** clock. |

Fail 1.4.5 answers. Fail “late” with no clock name.

---

## Knowledge Check – Answer Key

1. **Submit vs 1.4.5?**  
   **Answer:** These clocks start from a **report decision / question**. 1.4.5 is alert created → start and start → close/escalate.  
   **Explanation:** Fence.

2. **Blocked clock start?**  
   **Answer:** When you become unable to finish without someone else. Classroom 15 minutes to escalate that blocker.  
   **Explanation:** Outline b.

3. **Name the clock?**  
   **Answer:** Different types have different submit windows. “Late” does not say which.  
   **Explanation:** Task.

4. **Both live?**  
   **Answer:** Yes. When blocked, act on **escalate-for-more-info** first. Submit is still running.  
   **Explanation:** Example 3.

5. **Live numbers?**  
   **Answer:** Site reporting-SLA card. Classroom 30/60/15 are for this lesson.  
   **Explanation:** Same pattern as 1.4.5.

---

## Additional Instructor Resources

- Next recommended module: 1.6.3 Notification and distribution
