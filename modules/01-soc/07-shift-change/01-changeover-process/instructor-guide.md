# Instructor Guide – Module 1.7.1 – Shift Changeover Process

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.7.1.1 A / B / C · 1.7.1.2 2b / 3c / 4c  
- Hunter: 1.7.1.1 A / B / B · 1.7.1.2 1a / 2b / 3c  
- CTI: 1.7.1.1 A / A / A · 1.7.1.2 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach purpose, participants, and record location. Force a **handoff line** plus a rejected informal path. Do not write the five content buckets.

**Key Teaching Points:**
- Classroom roster / `SOC-CHANGEOVER` is a stand-in. Overlay the site SOP if you have one.
- Conduct = outgoing lead runs it. Participate = named seat + recorded brief.
- Hunter task is **1a** at 3-level (recognize). CTI is **1a** at all three levels. Do not collapse those to SOC 2b/3c/4c.
- Slack / kitchen / notebook is the usual fail.

**Common Student Challenges:**
- Treating a DM as the changeover.
- Incoming analyst with no cases trying to *run* it.
- Skipping IR on an active handoff.
- Writing the 1.7.2 report in this hour.
- Using 1.6.3’s ticket as the changeover log.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site changeover SOP
- Answer key (this guide)

---

## Learning Objectives

1. Purpose of a structured changeover.
2. Who participates and where it is recorded.
3. Handoff line + rejected informal path.

**Mapped Items:** K 1.7.1.1 · T 1.7.1.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 1.6 / 1.7.2 / 1.8 |
| Purpose, people, record        | 14 min   | a–c |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~64 min** | Stretch Ex 2 if they defend Slack |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: 2b — sit in the right seat and name the log. They do not invent a new SOP.
- Hunter 3 / CTI: 1a — they should *recognize* a failed handoff, not run the SOC changeover.
- Overlay site names (watch log, “pass-down”, bridge) if you can.

**Question:**  
“If the case system is down, do you skip changeover or invent Slack as the record?” (They escalate the blocker — they do not replace the system of record without a named fallback.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail Slack / kitchen / notebook as the changeover. Fail “IR will figure it out.”

**Summaries:**
- Ex 1: Pat runs; Riley + you + Jordan; you brief A12; `SOC-CHANGEOVER`.
- Ex 2: facts may be right; process failed (no lead, no log).
- Ex 3: Sam (IR) required; “they’ll figure it out” is not participation.

**Cases:**

| Item | Who runs | Who attends | Your role | Record | Reject |
|------|----------|-------------|-----------|--------|--------|
| A | Pat still runs — **wait for Riley** or named incoming cover | Riley (when present) + owners | Outgoing analyst | `SOC-CHANGEOVER` | Kitchen-only, leave before incoming lead |
| B | **Pat** (outgoing lead), not you | Both leads + owners; you **attend** | Incoming analyst, no open case — **do not conduct** | `SOC-CHANGEOVER` | Incoming junior running it |
| C | Pat | Riley + owners | Outgoing / as given | **`SOC-CHANGEOVER`** | Personal notebook as only record |
| D | Pat | Riley + owners + **Sam** | Outgoing A12 owner | `SOC-CHANGEOVER` | IR not invited on active handoff |

---

## Knowledge Check – Answer Key

1. **What problem does structured changeover prevent?**  
   **Answer:** Incoming crew taking the floor without open work, outages, or urgent policy. Informal “you’re good” drops cases.  
   **Explanation:** Outline a.

2. **Who conducts / must attend?**  
   **Answer:** Outgoing SOC lead conducts. Incoming lead + outgoing owners of open cases must attend.  
   **Explanation:** Outline b.

3. **When does IR participate?**  
   **Answer:** When an active incident is in handoff (classroom: Sam on A12).  
   **Explanation:** Outline b; Example 3.

4. **Where recorded / what does not count?**  
   **Answer:** Classroom: `SOC-CHANGEOVER` in the case system. Not Slack, not kitchen talk, not a personal notebook as the only record.  
   **Explanation:** Outline c.

5. **Why chat is not participating?**  
   **Answer:** Missing incoming lead, missing system of record, not a structured changeover.  
   **Explanation:** Task / Example 2.

---

## Additional Instructor Resources

- Site watch-to-watch SOP
- Next recommended module: 1.7.2 Required content of the changeover report
