# Instructor Guide – Module 1.4.5 – SLA / Response Time Goals

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.5.1 A / B / C ; 1.4.5.2 2b / 3c / 4c ; 1.4.5.3 2b / 3c / 4c  
- Hunter: 1.4.5.1 A / B / B ; 1.4.5.2 1a / 2b / 3c ; 1.4.5.3 1a / 2b / 3c  
- CTI: 1.4.5.1 A / A / A ; 1.4.5.2 1a / 1a / 1a ; 1.4.5.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name which of two clocks is at risk, then record a close or escalate against that clock.

**Context (plain language):**

- What this lesson is for: SOC analysts keep an alert from sitting untouched, and from sitting open with no close or escalate. They name the clock and write closed or escalated against it.
- How it hooks to the lesson before: 1.4.4 was the site bucket (scan / root / user).
- How it hooks to the lesson after: 1.5 is reports. Those have their own timelines. This lesson is the alert clocks only.
- Why we are doing it this way: two clocks, with classroom 15 / 45 so the timestamp task has numbers. Those minutes are this lesson only — not a live shop SLA.
- What we are *not* doing in this lesson: re-investigate. Re-label TP/FP or category. Write a report. Invent shop minutes. No lab. **1.7** is retired — do not open shift change.
- Extra step: none.

Use the same names as the student guide: **start clock**, **close/escalate clock**, **created**, **started**, **closed**, and **escalated**. Do not invent a Harbor or DYA SLA card. The givens are timestamps only; do not retell an earlier investigation plot.

**Key Teaching Points:**
- Start from **created**. Close/escalate from **started**.
- Untouched → only start exists.
- Record: closed or escalated, which clock, the time. Do not close an untouched alert.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.4.5.1 – Service Level Agreements / Response Time Goals
- T: 1.4.5.2 – Given timestamps, identify whether the start clock or the close/escalate clock is at risk
- T: 1.4.5.3 – Close or escalate an alert and record it against the correct clock

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Two clocks, not “work faster” |
| Key Concepts            | 12 min    | 15 / 45 classroom; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | Close 1.4; next is 1.5 |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert must not sit untouched, and it must not sit open with no close or escalate. Name which clock is at risk. “Work faster” is not the task.
- Write the two clocks. Start is created → first touch (classroom 15 minutes). Close/escalate is first touch → closed or escalated (classroom 45 minutes). Those minutes are this lesson only.
- Walk the untouched given as **start**. Close/escalate has no origin yet.
- Walk the still-open given as **close/escalate**. Start already met.
- If they say “we’re late” with no clock: ask which one.
- If they close an untouched alert: start first. Close/escalate has no origin.
- If they measure close/escalate from created: measure from first touch.
- If they reopen TP or category: those lessons are done. Stay on the clocks.
- If they ask for shop minutes: classroom 15 / 45. Their real shop substitutes.

---

## Knowledge Check – Answer Key

1. **If nobody has touched the alert, which clock can be at risk?**  
   **Answer:** Only the **start** clock. Close/escalate has no origin yet.  
   **Explanation:** Until a first touch, the close/escalate clock has nothing to measure from.

2. **What are the two clocks, and when does each start?**  
   **Answer:** Start = created → first touch (classroom 15 min). Close/escalate = first touch → closed or escalated (classroom 45 min).  
   **Explanation:** Two response-time goals, two origins. Do not measure both from created.

3. **An alert was first touched at 13:28 and is still open at 14:20. Which clock is at risk, and what do you record?**  
   **Answer:** **Close/escalate** (52 minutes, past 45). Record `escalated` (or `closed` if the investigation is done) against the close/escalate clock at `14:20`.  
   **Explanation:** Start already has a first touch. The remaining clock is close/escalate. Record the disposition against that clock.

---

## Additional Instructor Resources

- Next: 1.5.1 Report types
