# Module 1.4.5 – SLA / Response Time Goals

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.5.1 A / B / C ; 1.4.5.2 2b / 3c / 4c ; 1.4.5.3 2b / 3c / 4c  
- Hunter: 1.4.5.1 A / B / B ; 1.4.5.2 1a / 2b / 3c ; 1.4.5.3 1a / 2b / 3c  
- CTI: 1.4.5.1 A / A / A ; 1.4.5.2 1a / 1a / 1a ; 1.4.5.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two clocks: time to **begin** investigation, and time to **close or escalate**.
2. Given timestamps, say **which clock is at risk**.
3. Close or escalate and **record it against the correct clock**.

**Mapped Proficiency Items:**
- K: 1.4.5.1 – Service Level Agreements / Response Time Goals
- T: 1.4.5.2 – Given timestamps, identify whether the start clock or the close/escalate clock is at risk
- T: 1.4.5.3 – Close or escalate an alert and record it against the correct clock

---

## 1. Key Concepts

SOC analysts watch **two clocks** on a queue row so a case does not sit untouched, and so it does not sit open with no disposition. You name **which** clock is in danger. “Work faster” is not the task. You do **not** re-investigate (**1.4.1**). You do **not** re-label TP/FP or category (**1.4.2** / **1.4.4**). You do **not** write a report (**1.6**).

**Classroom numbers (this lesson only — not a live shop policy):**

| Clock | From → to | Classroom |
|-------|-----------|-----------|
| **Start** | alert **created** → first touch (`started`) | **15 minutes** |
| **Close / escalate** | first touch → `closed` or `escalated` | **45 minutes** |

If nobody has touched it, only the **start** clock exists. After a first touch, start is already met (or already breached); the remaining clock is **close/escalate**.

If your real shop uses different minutes, use those. The obligation is **two clocks**, not 15 and 45.

**Record** (task 2) is one line: **closed** or **escalated**, **which clock**, and the **time**. If you have not touched it yet, the first line is **started** against the **start** clock — do not close an untouched row to “meet SLA.” This is a classroom line, not a ticketing-product class.

**What good looks like:**

- **Start at risk:** Created `14:00`. No `started`. Now `14:18`. Clock: **start** (18 minutes, past 15). Close/escalate has no origin. Record: `started | start (breached) | 14:18`. Then investigate. Do not write `closed` yet.
- **Close/escalate at risk:** Alert **A12** (the `wscript` → `-enc` case you already started). Started `13:28`. Still open. Now `14:20`. Clock: **close/escalate** (52 minutes since start, past 45). Start already met. Record: `escalated | close-escalate (breached) | 14:20` — or `closed` if the card is actually done.

---

## 2. Knowledge Check

1. If nobody has touched the alert, which clock can be at risk?
2. What are the two clocks, and when does each start?
3. Started `13:28`, still open at `14:20`. Which clock, and what do you record?

---

## 3. Summary

Two clocks: **start** from created; **close/escalate** from first touch. Name the clock. Record closed or escalated against it.

**Next:** **1.6.1** Report types. This closes unit **1.4**.

---

## 4. Related modules

- 1.4.4 – Common alert categorizations (previous)
- 1.6.1 – Report types
- 1.4.1 – Alert context and investigation
- 1.6.2 – Reporting timeline requirements (not these alert clocks)
