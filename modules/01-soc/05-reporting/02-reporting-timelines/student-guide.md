# Module 1.5.2 – Reporting Timeline Requirements

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C ; 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 A / B / B ; 1.5.2.2 2b / 3c / 4c  
- CTI: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two kinds of report clock: **submit** (by type) and **escalate-for-more-info**.
2. Given timestamps, say **which clock applies** and whether it is **at risk**.

**Mapped Proficiency Items:**
- K: 1.5.2.1 – Reporting timeline requirements
- T: 1.5.2.2 – Given timestamps, identify which report timeline applies and whether it is at risk

---

## 1. Key Concepts

SOC analysts watch **report** clocks so the case record and the CTI question leave the desk on time — and so a blocker gets escalated instead of sitting. You already know the **type** (**1.5.1**). This hour you name **which clock** and whether it is **at risk**. You do **not** use the alert 15 / 45 (**1.4.5**). You do **not** pick the type again. You do **not** route the report (**1.5.3**).

**Classroom numbers (this lesson only — not a live shop policy):**

| Clock | From | Classroom |
|-------|------|-----------|
| **Submit — incident** | Decision that an **incident report** is required | **30 minutes** |
| **Submit — RFI** | The **question** arises | **60 minutes** |
| **Escalate-for-more-info** | You become **blocked** (cannot finish without another desk) | **15 minutes** |

If your shop uses different minutes, use those. The obligation is **submit-by-type** plus **blocked → escalate**, not 30 / 60 / 15. If your shop has an **other** type, it has its own submit number — do not invent one here.

**At risk** means the named clock will miss if you wait, or it is already past. “Late” with no clock name is not the task.

Two clocks can be live. When you are blocked, name **escalate-for-more-info** first. Submit is still running.

**What good looks like:**

- **Submit — RFI, at risk:** **A12** exists. Question to CTI on the update domain at `13:30`. Still unsent. Now `14:40`. Clock: **submit — RFI** (70 minutes, past 60). Not the 30-minute incident clock. Not the alert-close clock.
- **Escalate-for-more-info, at risk:** **A12** incident decision `14:00`. At `14:10` you cannot finish without another desk. Still blocked. Now `14:28`. Clock: **escalate-for-more-info** (18 minutes, past 15). Submit-incident is still running (28 of 30) — act on the blocker.

---

## 2. Knowledge Check

1. This hour is the same 15 / 45 clocks as **1.4.5**. True or false?
2. When does the **escalate-for-more-info** clock start?
3. RFI question at `13:30`, still unsent at `14:40`. Which clock, and is it at risk?

---

## 3. Summary

Submit-by-type. Blocked → escalate. Name the clock. Not the alert SLA.

**Next:** **1.5.3** Notification and distribution.

---

## 4. Related modules

- 1.5.1 – Report types (previous)
- 1.5.3 – Notification and distribution
- 1.4.5 – SLA / response time goals (alert clocks, not these)
