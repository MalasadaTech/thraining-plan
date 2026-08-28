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

- What this lesson is for: SOC analysts watch report clocks so a case record and a CTI question leave the desk on time, and so a blocker is escalated instead of sitting.
- How it hooks to the lesson before: 1.5.1 named the type (incident report vs RFI). This lesson is the clock for that type.
- How it hooks to the lesson after: 1.5.3 is who gets the report and which channel. Not when it is due.
- Why we are doing it this way: after the type is known, name the clock before anyone routes the report. Classroom 30 / 60 / 15 give the timestamp task numbers. They are not a live shop SLA.
- What we are *not* doing in this lesson: Alert 15 / 45. Pick the type again. Route the report. Invent an informational or changeover clock. Invent DYA minutes. No lab. **1.7** is retired.
- Extra step: none.

Use the same names as the student guide: **submit — incident**, **submit — RFI**, **escalate-for-more-info**, and **at risk**. **A12** is the incident they already opened. The RFI asks intel to work the update domain. Do not invent a Harbor or DYA reporting-SLA card. Do not tell the PRD plot.

**Key Teaching Points:**
- Submit starts from the decision or the question. Blocked starts when you cannot finish without another desk.
- Name the clock. RFI is not scored on the incident 30.
- When blocked, act on escalate-for-more-info first. Submit is still running.

**Common Student Challenges:**
- Use the alert 15 / 45 as report clocks. Why: **1.4.5** just taught those numbers. Example: scoring an unsent RFI as “start clock at risk.”
- Score the RFI on the incident 30. Why: one “submit” word, two numbers. Example: question at `13:30`, unsent at `14:05`, calling it at risk on 30.
- Sit on submit while blocked. Why: the submit clock is still visible. Example: writing only “28 of 30” and not naming **escalate-for-more-info**.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.5.2.1 – Reporting timeline requirements
- T: 1.5.2.2 – Given timestamps, identify which report timeline applies and whether it is at risk

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

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

**Talking Points:**
- Open with the job: a case record and a CTI question need a submit clock, and a blocker needs an escalate clock.
- Write submit-by-type versus blocked. Stop. Do not pick the type again.
- Walk the unsent RFI as **submit — RFI, at risk**. Walk the blocker as **escalate-for-more-info**.
- If they use 15 / 45: that is **1.4.5**. Those clocks start from alert created or first touch.
- If they score the RFI on 30: the type drives the number.
- If they say “late” with no clock: ask which one.
- If they sit on submit while blocked: name **escalate-for-more-info** first. Submit is still running.
- If they invent informational or changeover minutes: **other** is a shop name. **1.7** is retired.
- If they ask for DYA minutes: classroom 30 / 60 / 15. Their real shop substitutes.

---

## Knowledge Check – Answer Key

1. **This lesson uses the same 15 / 45 clocks as 1.4.5. True or false?**  
   **Answer:** False. Those are alert start / close. These clocks start from a report decision, a question, or a blocker.  
   **Explanation:** **1.4.5** is the alert start / close clocks. This lesson is the report clocks.

2. **When does the escalate-for-more-info clock start?**  
   **Answer:** When you become blocked — you cannot finish the report without another desk. Classroom 15 minutes from that moment.  
   **Explanation:** The escalate clock does not start at the report decision. It starts when you cannot finish without another desk.

3. **RFI question 13:30, still unsent at 14:40. Which clock, and is it at risk?**  
   **Answer:** **Submit — RFI.** At risk (70 minutes, past 60).  
   **Explanation:** The type is RFI, so the submit clock is 60 minutes from the question, not the 30-minute incident clock.

---

## Additional Instructor Resources

- Next: 1.5.3 Notification and distribution
