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

SOC analysts keep an alert from sitting untouched, and from sitting open with no close or escalate. That is the job in this lesson: name **which** response-time goal is at risk, then record closed or escalated against it. “Work faster” is not the task.

A **service-level agreement (SLA)** here is a **response-time goal**: the maximum time allowed for a step. This lesson uses two **clocks** — the short word for those goals.

| Clock | What it measures | Classroom goal |
|-------|------------------|----------------|
| **Start** | Alert **created** → first touch (`started`) | **15 minutes** |
| **Close / escalate** | First touch → `closed` or `escalated` | **45 minutes** |

The 15-minute and 45-minute figures are **this lesson only**. They are not a live shop policy. If your real shop uses different minutes, use those. The obligation is **two clocks**, not 15 and 45.

If nobody has touched the alert, only the **start** clock exists. Close/escalate has no origin until a first touch. After a first touch, start is already met (or already breached); the remaining clock is **close/escalate**.

This is **not** re-investigating the alert (**1.4.1**). It is **not** true-positive / false-positive or a category (**1.4.2**, **1.4.4**). It is **not** a report, and it is **not** the report clocks in **1.5**.

**Record** is one classroom line: **closed** or **escalated**, **which clock**, and the **time**. If you have not touched the alert yet, the first line is **started** against the **start** clock. Do not close an untouched alert to “meet SLA.” This is a classroom line, not a ticketing-product class.

**What good looks like:**

- **Start at risk:** Created `14:00`. No `started`. Now `14:18`. Clock: **start** (18 minutes, past 15). Close/escalate has no origin. Record: `started | start (breached) | 14:18`. Then investigate. Do not write `closed` yet.
- **Close/escalate at risk:** An alert first touched at `13:28` is still open at `14:20`. Clock: **close/escalate** (52 minutes since start, past 45). Start already met. Record: `escalated | close-escalate (breached) | 14:20` — or `closed` if the investigation is actually done.

---

## 2. Knowledge Check

1. If nobody has touched the alert, which clock can be at risk?
2. What are the two clocks, and when does each start?
3. An alert was first touched at `13:28` and is still open at `14:20`. Which clock is at risk, and what do you record?

---

## 3. Summary

Two clocks: **start** from created; **close/escalate** from first touch. Name the clock. Record closed or escalated against it.

**Next:** **1.5.1** Report types. This closes unit **1.4**.

---

## 4. Related modules

- 1.4.4 – Common alert categorizations (previous)
- 1.5.1 – Report types
- 1.4.1 – Alert context and investigation
- 1.5.2 – Reporting timeline requirements (not these alert clocks)
