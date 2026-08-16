# Instructor Guide – Module 1.8.4 – Investigation Documentation

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.8.4.1 2b / 3c / 4c  
- Hunter: 1.8.4.1 3c / 4c / 4c  
- CTI: 1.8.4.1 2b / 3c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach where and how notes are saved. Force a **notes line** plus a rejected unofficial-only path. Do not teach IR decisions.

**Key Teaching Points:**
- Harbor ticket worklog is a stand-in. Overlay the site case system if you have one.
- Scratch pads are fine **during** the call; empty ticket **after** is the fail.
- Wiki is allowed when **linked** from the ticket.
- Hunter 3-level is already **3c**.

**Common Student Challenges:**
- Desktop as the record.
- Slack as searchable archive.
- Mixing 1.7.1 changeover form with case notes.
- Writing the 1.8.5 isolate decision here.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site notes SOP
- Answer key (this guide)

---

## Learning Objectives

1. Where notes live.
2. How (minimum fields).
3. Reject unofficial-only.

**Mapped Items:** T 1.8.4.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & card            | 12 min   | where + how |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~54 min** | Stretch Ex 2 if they defend “later” |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: 2b — put the fact on the ticket, label hypothesis.
- Overlay real names (ServiceNow work notes, TheHive, etc.).

**Question:**  
“If the ticket system is down, is Slack the record?” (No. Named fallback on the site card — they do not invent USB/home as the archive.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail desktop-only, USB, Slack-only. Accept C (wiki + link + one-liner).

**Summaries:**
- Ex 1: A12 worklog, fields, not local-only.
- Ex 2: content OK, location failed.
- Ex 3: Slack is not the record.

**Cases:**

| Item | Where | How | Reject |
|------|-------|-----|--------|
| A | RFI ticket worklog | ts, case, FACT: CTI cluster known, next | Chat-only |
| B | **Ticket** after the call (scratch OK *during*) | paste timeline + labels | Notepad as the only copy |
| C | Ticket + **linked** wiki | link + one-line summary | — **complete** |
| D | Ticket (not USB) | same fields | USB / home |

---

## Knowledge Check – Answer Key

1. **System of record?**  
   **Answer:** Case ticket worklog (Harbor: ticket.harbor.internal).  
   **Explanation:** Task.

2. **How — four pieces?**  
   **Answer:** Timestamp, case ID, fact vs hypothesis labeled, next action.  
   **Explanation:** Classroom how.

3. **Wiki allowed?**  
   **Answer:** Yes, if **linked from the ticket**. Wiki-only fails.  
   **Explanation:** Card; C.

4. **“Paste later”?**  
   **Answer:** The record does not exist yet. After the call, the ticket must have it.  
   **Explanation:** Example 2 / B.

5. **Vs 1.7.1?**  
   **Answer:** 1.7.1 is the **changeover** form (`SOC-CHANGEOVER`). This is **case** working notes.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Site case-system SOP
- Next recommended module: 1.8.5 Incident response processes
