# Module 1.6.2 – Reporting Timelines

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.6.2.1 A / B / C · 1.6.2.2 2b / 3c / 4c  
- Hunter: 1.6.2.1 A / B / B · 1.6.2.2 2b / 3c / 4c  
- CTI: 1.6.2.1 B / C / C · 1.6.2.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain **submit** timelines by report type and the **escalate-for-more-info** timeline.
2. Given a situation and timestamps, identify **which clock applies** and whether it is **at risk**.

**Mapped Proficiency Items:**
- K: 1.6.2.1 – Reporting timeline requirements
- T: 1.6.2.2 – Identify which report timeline applies and whether it is at risk

---

## 1. Key Concepts

These clocks are for **reports**, not for touching an alert. Alert start / close-escalate is **1.4.5**. You already know the **type** from **1.6.1**. This hour is **which report clock** and **met vs at risk**.

**Classroom timelines (this lesson only — not a live org policy):**

| Clock | Outline | Classroom number | Starts from |
|-------|---------|------------------|-------------|
| **Submit — incident** | a | **30 minutes** | Decision that an **incident report** is required |
| **Submit — RFI** | a | **60 minutes** | The **question** arises |
| **Submit — informational** | a | **end of shift** (classroom: before changeover) | Decision that an FYI note is required |
| **Escalate-for-more-info** | b | **15 minutes** | You become **blocked** (cannot finish the report without someone else) |

If your site uses different numbers, substitute them. The obligation is **submit-by-type** plus **blocked → escalate**, not these minutes.

| This lesson | Other |
|-------------|-------|
| Report clocks | Alert 15 / 45 — **1.4.5** |
| Which clock / at risk | Who to send it to — **1.6.3** |
| Escalation *of the report* because you are blocked | Escalating the *alert* on the close clock — **1.4.5** |

**At risk** = now is inside the last third of the window, or already past it (**breached**). You must **name the clock**. “We’re late” is not the task.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Incident decision 14:00, draft sent 14:20 — submit-incident **met** | Using the 1.4.5 15-minute *alert start* clock on a report |
| RFI question 14:00, still unsent 15:10 — submit-RFI **breached** | Applying the 30-minute incident clock to an RFI |
| Blocked 14:10, still waiting 14:30 — escalate-for-more-info **breached** | Waiting silently on the submit clock only |

---

## 2. Detailed Walkthrough / Examples

Now = **14:40** unless stated.

### Example 1: Incident Submit Met (Expected)

**Type:** Incident (encoded PS + Run key). Decision at `14:00`. Report submitted `14:22`.

**Clock:** **Submit — incident** (30 min from 14:00).  
**Status:** **Met** (22 minutes).  
Not the alert-close clock. Not RFI-60.

### Example 2: RFI Submit Breached (Lead)

**Type:** RFI to CTI on `nightowl-updates.net`. Question arose `13:30`. Still not sent. Now `14:40`.

**Clock:** **Submit — RFI** (60 min from 13:30).  
**Status:** **Breached** (70 minutes).  
**Lead:** Do not score this against the 30-minute incident clock.

### Example 3: Blocked — Escalate Clock (Lead)

**Type:** Incident report. Decision `14:00`. At `14:10` you cannot get EDR for `WS-JLEE`. Still blocked. Now `14:28`.

**Clock:** **Escalate-for-more-info** (15 min from 14:10).  
**Status:** **Breached** (18 minutes blocked).  
The incident *submit* clock (30 from 14:00) is still running — but the syllabus *b* clock is the one at risk **now**. You escalate the blocker; you do not silently sit on submit.

---

## 3. Hands-On Exercise

**Objective:** Name the clock and met / at risk / breached.

**Classroom:** incident submit 30; RFI submit 60; informational before changeover (treat changeover as **16:00**); escalate-for-more-info 15 from blocked. Now = **15:00**.

**Instructions:**

1. One sentence each for Examples 1–3: clock + status.
2. For each row, write **which clock** and **met / at risk / breached** (and the elapsed minutes).

   - A. Incident decision 14:40. Not submitted. Now 15:00.
   - B. RFI question 14:00. Not sent. Now 15:00.
   - C. Informational note decided 14:50. Changeover 16:00. Not sent. Now 15:00.
   - D. Incident decision 14:20. Blocked on legal at 14:35. Still blocked. Now 15:00.

3. Do not route the report. Do not change the type. Do not use 1.4.5’s 15/45 unless you *label* that you are talking about the alert, not the report (that would be the wrong unit).
4. If two clocks exist, name the one the situation is asking about (blocked → escalate-for-more-info).

**Expected Outcome:**
- Three example summaries
- Four clock + status lines
- No distribution chart

---

## 4. Knowledge Check

1. What submit clocks does this lesson use, and how do they differ from **1.4.5**?
2. When does the **escalate-for-more-info** clock start?
3. Why must you **name** the clock, not just say “late”?
4. Can an incident submit clock and a blocked-escalate clock both be live? Which one do you act on first when blocked?
5. Who owns live-org minutes if they differ from 30 / 60 / 15?

---

## 5. Summary

- Submit-by-type vs escalate-when-blocked. Not alert SLA.
- Name the clock. Met / at risk / breached.
- Next: notification and distribution (**1.6.3**).

---

## 6. References & Further Reading

- Related modules:
  - 1.4.5 – SLA / response time goals (alert clocks)
  - 1.6.1 – Report types (previous)
  - 1.6.3 – Notification and distribution (next)
- Local reporting-SLA card (optional — substitutes classroom numbers)
