# Instructor Guide – Module 1.5.2 – Reporting Timeline Requirements

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C ; 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 A / B / B ; 1.5.2.2 2b / 3c / 4c  
- CTI: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name which report clock applies — submit-by-type or escalate-for-more-info — and whether it is at risk.

**Context (plain language):**

- What this hour is for: SOC analysts keep a case record and a CTI question from sitting, and they escalate a blocker instead of waiting in silence.
- How it hooks to the hour before: 1.5.1 picked the type (incident vs RFI). This hour is the clock for that type.
- How it hooks to the hour after: 1.5.3 is who gets it and which channel. Not when it is due.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–b. Classroom 30 / 60 / 15 so the timestamp task has numbers. Not a live shop SLA. Hunter K is A / B / B. CTI works the task at 3-level (3c).
- What we are *not* doing this hour: Alert 15 / 45. Pick the type again. Route the report. Invent an informational / changeover clock. Invent DYA minutes. No lab. **1.7** is retired.
- Extra step: none.

Do not invent a Harbor or DYA reporting-SLA card. Do not tell the PRD plot. Do not dump the Run key. **A12** is the incident they already opened. The RFI asks intel to work the update domain / file.

**Key Teaching Points:**
- Submit starts from the decision or the question. Blocked starts when you cannot finish without another desk.
- Name the clock. RFI is not scored on the incident 30.
- When blocked, act on escalate-for-more-info first. Submit is still running.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.5.2.1 ; T 1.5.2.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Report clocks, not alert 15 / 45 |
| Key Concepts            | 12 min    | Submit vs blocked; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write submit-by-type vs blocked. Walk the unsent RFI as **submit — RFI, at risk**. Walk the blocker as **escalate-for-more-info**.

If they use 15 / 45: “That is 1.4.5. Different origin.”  
If they score the RFI on 30: “Type drives the number.”  
If they say “late” with no clock: “Which one?”  
If they sit on submit while blocked: “Name escalate-for-more-info first.”  
If they invent informational / changeover minutes: “Other is a shop name. 1.7 is retired.”  
If they ask for DYA minutes: “Classroom 30 / 60 / 15. Their real shop substitutes.”

---

## Knowledge Check – Answer Key

1. **This hour is the same 15 / 45 as 1.4.5. True or false?**  
   **Answer:** False. Those are alert start / close. These clocks start from a report decision, a question, or a blocker.  
   **Explanation:** Stay-in / vs 1.4.5.

2. **When does escalate-for-more-info start?**  
   **Answer:** When you become blocked — you cannot finish the report without another desk. Classroom 15 minutes from that moment.  
   **Explanation:** Outline b.

3. **RFI question 13:30, still unsent at 14:40. Which clock, at risk?**  
   **Answer:** **Submit — RFI.** At risk (70 minutes, past 60).  
   **Explanation:** Outline a / task 1.

---

## Additional Instructor Resources

- Next: 1.5.3 Notification and distribution
