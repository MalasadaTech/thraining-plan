# Module 1.4.5 – SLA / Response Time Goals

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.5.1 A / B / C · 1.4.5.2 2b / 3c / 4c · 1.4.5.3 2b / 3c / 4c  
- Hunter: 1.4.5.1 A / B / B · 1.4.5.2 1a / 2b / 3c · 1.4.5.3 1a / 2b / 3c  
- CTI: 1.4.5.1 A / A / A · 1.4.5.2 1a / 1a / 1a · 1.4.5.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the two classroom clocks: **start** (begin investigation) and **close/escalate** (process the alert).
2. Given timestamps, identify **which clock is at risk**.
3. Close or escalate an alert and **record it against the correct clock**.

**Mapped Proficiency Items:**
- K: 1.4.5.1 – Service Level Agreements / Response Time Goals
- T: 1.4.5.2 – Identify whether the start clock or the close/escalate clock is at risk
- T: 1.4.5.3 – Close or escalate an alert and record it against the correct clock

---

## 1. Key Concepts

Two clocks. “Work faster” is not a task. “Demonstrate understanding” is not a task.

**Classroom SLA (this lesson only — not a live org policy):**

| Clock | Outline | Classroom number | Starts from |
|-------|---------|------------------|-------------|
| **Start** | a. Maximum time before investigation must **begin** | **15 minutes** | Alert **created** → first touch (`started`) |
| **Close/escalate** | b. Required time to **process** (close or escalate) | **45 minutes** | First touch (`started`) → `closed` or `escalated` |

If nobody has touched the alert, only the **start** clock can be at risk. If it has been touched, the **start** clock is already met (or already breached); the remaining risk is **close/escalate**.

If your site uses different numbers, substitute them. The obligation is **two clocks**, not these minutes.

| This lesson | Other |
|-------------|-------|
| Which clock, then record close/escalate | How to investigate — **1.4.1** |
| Record against a clock | TP/FP, category — **1.4.2** / **1.4.4** |
| Escalate as a **disposition** | Hunt kickoff process — **2.7** |

**Record** (task 2) is a four-field line:

`alert_id | disposition (closed \| escalated) | clock (start already met / close-escalate) | timestamp`

You are not configuring the ticketing product.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Created 14:00, started 14:08 — start OK | Created 14:00, still untouched at 14:18 — **start** at risk |
| Started 14:05, closed 14:40 — close OK | Started 14:05, still open 15:00 — **close/escalate** at risk |
| Naming the clock that is in danger | “We’re late” with no clock |

---

## 2. Detailed Walkthrough / Examples

Now = **14:20** unless stated.

### Example 1: Both Clocks OK (Expected)

**Alert A12.** Created `14:00`. Started `14:08`. Closed `14:40` (same day).

**Start:** 8 minutes — OK.  
**Close/escalate:** 32 minutes from start — OK.

**Record (already done):** `A12 | closed | close-escalate (met) | 14:40`

### Example 2: Start Clock at Risk (Lead)

**Alert A13.** Created `14:00`. **No** `started`. Now `14:18`.

**Which clock:** **Start** — 18 minutes, past 15. Close/escalate has not started (no first touch).

**What you do:** Touch it now. Record start, then investigate. Do not write a close line yet.

**Record (start):** `A13 | started | start (breached) | 14:18`

### Example 3: Close/Escalate Clock at Risk (Lead)

**Alert A14.** Created `13:20`. Started `13:28`. Still open. Now `14:20`.

**Start:** 8 minutes — already met.  
**Which clock:** **Close/escalate** — 52 minutes since start, past 45.

**What you do:** **Escalate** (or close if the investigation is actually done). Do not keep it in the queue unsigned.

**Record:** `A14 | escalated | close-escalate (breached) | 14:20`

---

## 3. Hands-On Exercise

**Objective:** Name the clock, then write a close/escalate record.

**Classroom SLA:** start 15 min from created; close/escalate 45 min from started. Now = **15:00**.

**Instructions:**

1. One sentence each for Examples 1–3: which clock (or both OK) and why.
2. For each alert below, write **which clock is at risk (or OK)** and **one record line** (started / closed / escalated).

   - A. Created 14:50. No start. Now 15:00.
   - B. Created 13:00. Started 13:10. Still open. Now 15:00.
   - C. Created 14:30. Started 14:40. You finish the **1.4.1** card now and can close.
   - D. Created 14:20. Started 14:25. You need hunt/IR. Escalate now.

3. Do not rewrite the investigation. Do not classify. Do not change the classroom numbers unless the instructor substitutes site numbers.
4. If start is already breached and you touch now, the record is **started** against the **start** clock; close/escalate is a later line.

**Expected Outcome:**
- Three example summaries
- Four clock calls + four record lines
- No 1.4.1/1.4.2 write-up

---

## 4. Knowledge Check

1. What are the two clocks, and when does each start?
2. If nobody has touched the alert, which clock can be at risk?
3. Why is “process within required timeframes” not the same as “work faster”?
4. What four fields belong on the record line?
5. Who owns live-org numbers if they differ from the classroom 15 / 45?

---

## 5. Summary

- Two clocks: **start** from created; **close/escalate** from first touch.
- Name the clock at risk. Record close or escalate against that clock.
- Classroom 15 / 45 are for this lesson. This closes unit **1.4**. Next unit: **0.6** Frameworks.

---

## 6. References & Further Reading

- Related modules:
  - 1.4.1 – Alert context and investigation
  - 1.4.4 – Common alert categorizations (previous)
  - 0.6.1 – MITRE ATT&CK (next unit)
  - Local SLA card used on shift (optional — substitutes classroom numbers)
