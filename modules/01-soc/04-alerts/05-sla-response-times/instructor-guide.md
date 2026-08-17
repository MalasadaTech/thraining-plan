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

- What this hour is for: SOC analysts keep a queue row from sitting untouched, and from sitting open with no disposition. They name the clock and write closed or escalated against it.
- How it hooks to the hour before: 1.4.4 was the site bucket (scan / root / user).
- How it hooks to the hour after: 1.6 is reports. Those have their own timelines. This hour is the alert clocks only.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–b. Classroom 15 / 45 so the timestamp task has numbers. Not a live shop SLA. Hunter 3 is A / 1a. CTI names the words (A / 1a).
- What we are *not* doing this hour: Re-investigate. Re-label TP/FP or category. Write a report. Invent DYA minutes. No lab. **1.7** is retired — do not open shift change.
- Extra step: none.

Do not invent a Harbor or DYA SLA card. Do not tell the PRD plot. **A12** is the same encoded-PowerShell alert they already started.

**Key Teaching Points:**
- Start from **created**. Close/escalate from **started**.
- Untouched → only start exists.
- Record: closed or escalated, which clock, the time. Do not close an untouched row.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.4.5.1 ; T 1.4.5.2 ; T 1.4.5.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Two clocks, not “work faster” |
| Key Concepts            | 12 min    | 15 / 45 classroom; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | Close 1.4; next is 1.6 |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the two clocks. Walk the untouched row as **start**. Walk **A12** still open as **close/escalate**.

If they say “we’re late” with no clock: “Which one?”  
If they close an untouched row: “Start first. Close/escalate has no origin.”  
If they measure close/escalate from created: “From first touch.”  
If they reopen TP or category: “1.4.2 / 1.4.4 are done.”  
If they ask for DYA minutes: “Classroom 15 / 45. Their real shop substitutes.”

---

## Knowledge Check – Answer Key

1. **Untouched — which clock?**  
   **Answer:** Only the **start** clock. Close/escalate has no origin yet.  
   **Explanation:** Task 1.

2. **Two clocks, when does each start?**  
   **Answer:** Start = created → first touch (classroom 15 min). Close/escalate = first touch → closed or escalated (classroom 45 min).  
   **Explanation:** Outline a–b.

3. **Started 13:28, still open at 14:20. Which clock, and what do you record?**  
   **Answer:** **Close/escalate** (52 minutes, past 45). Record `escalated` (or `closed` if the card is done) against the close/escalate clock at `14:20`.  
   **Explanation:** Tasks 1 and 2.

---

## Additional Instructor Resources

- Next: 1.6.1 Report types
