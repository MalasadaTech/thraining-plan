# Module 1.7.2 – Required Content of the Changeover Report

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.7.2.1 A / B / C · 1.7.2.2 2b / 3c / 4c  
- Hunter: 1.7.2.1 A / B / B · 1.7.2.2 1a / 2b / 3c  
- CTI: 1.7.2.1 A / A / A · 1.7.2.2 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the **five required buckets** of a changeover report.
2. **Produce** a complete report (or mark **none** in an empty bucket).
3. Reject a draft that is missing a required element.

**Mapped Proficiency Items:**
- K: 1.7.2.1 – Required content of the changeover report
- T: 1.7.2.2 – Produce a complete changeover report that includes all required elements

---

## 1. Key Concepts

You already know **who** runs it and **where** it is recorded (**1.7.1**). This hour is **what must be in the report**. It is not an incident write-up (**1.6.1**), not a 1.6.2 clock, and not a 1.6.3 route.

**Five required buckets (outline a–e):**

| Bucket | Outline | Put here | Empty looks like |
|--------|---------|----------|------------------|
| **Open / in-progress** | a | Cases still live at changeover | `Open: none` |
| **Opened / updated / closed this shift** | b | What *changed* during the shift, including closes | `Opened/updated/closed: none` |
| **Planned outages** | c | Upcoming maintenance you were told about | `Planned outages: none` |
| **Ongoing / occurred-during-shift outages** | d | Sensors, tools, or services that were or still are down | `Outages this shift: none` |
| **Urgent process / policy** | e | New “do / do not” the next crew must know **now** | `Urgent policy: none` |

A complete report has **all five lines**. Silence is not “none.” You write **none**.

**Classroom template:**

```
Open:
Opened / updated / closed this shift:
Planned outages:
Ongoing / occurred this shift:
Urgent process / policy:
```

| This lesson | Other |
|-------------|-------|
| Five buckets, or explicit none | Who / where — **1.7.1** |
| Not the incident body | **1.6.1** |
| Not the 30/60 submit clock | **1.6.2** |
| Not the IR ticket route | **1.6.3** |

The task is **complete report + reject the missing-element draft**, not “list the open tickets.”

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Five lines, including `none` where empty | Only the open-ticket list |
| Planned *and* already-occurred outages in different buckets | Mixing planned 02:00 window with a 13:10 drop as one line |
| New “do not close without IR” under policy | Burying policy inside the A12 one-liner |

---

## 2. Detailed Walkthrough / Examples

**Classroom shift facts (day crew, changeover 16:00):**

- **A12** Incident — `WS-JLEE`, encoded PS + Run, IR (Sam) still has the host. Still **open**.
- **RFI** to CTI — is `nightowl-updates.net` a known cluster? Still **open** / waiting.
- **Informational** — TN intranet `q3-notes.pdf` did not page. **Opened and closed** this shift.
- **HelpdeskSvc** scanner FP — **closed** this shift (**1.4.3**).
- **Planned:** EDR sensor maintenance **02:00–03:00** tomorrow on `10.10.8.0/24`.
- **Occurred:** Zeek sensor on `span-2` dropped **13:10–13:40** (recovered). No PCAP for that window.
- **Policy (15:00):** SOC lead — do **not** close Night Owl-related cases without IR concurrence.

### Example 1: Complete Five-Bucket Report (Expected)

```
Open: A12 WS-JLEE (IR has host); RFI to CTI on nightowl-updates.net (waiting)
Opened / updated / closed this shift: Informational TN PDF (opened+closed); HelpdeskSvc FP closed
Planned outages: EDR 02:00–03:00 tomorrow, VLAN 10.10.8.0/24
Ongoing / occurred this shift: Zeek span-2 down 13:10–13:40, recovered; no PCAP that window
Urgent process / policy: Do not close Night Owl-related cases without IR concurrence
```

All five present. Incoming crew can take the floor.

### Example 2: Open Tickets Only (Lead)

**Draft:** “Open: A12 and the Night Owl RFI. Have a good night.”

**Missing:** opened/closed this shift, planned EDR window, Zeek drop, IR-concurrence policy.  
**Lead:** The two open names are true. The report is **not complete**.

### Example 3: Outages Collapsed, Policy Buried (Lead)

**Draft:** lists A12 and the RFI, then “sensors were weird today, EDR window tonight, don’t close Night Owl without asking Sam — that’s in A12.”

**Reject:** planned (c) and occurred (d) are **different** buckets. Policy (e) is its own line, not a clause on A12.  
**Lead:** They remembered the facts. They did not produce the required *elements*.

---

## 3. Hands-On Exercise

**Objective:** Produce the five-bucket report and reject a missing-element draft.

**Use the classroom shift facts** unless the instructor overlays site items.

**Instructions:**

1. One sentence each for Examples 1–3: complete vs which buckets were missing.
2. Write a **complete** five-line report from the classroom facts (Example 1 is the model — write it in your own words).
3. For each draft, name **which required element is missing or misplaced** (or say complete).

   - A. “Open: A12. Closed HelpdeskSvc. Night.”
   - B. Full open + opened/closed + both outage lines. **No** policy line.
   - C. “No outages” — but the Zeek 13:10 drop is in the fact sheet.
   - D. All five lines, but the EDR 02:00 window is under **occurred** and the Zeek drop is under **planned**.

4. Do not rewrite A12 as an incident report. Do not score 1.6.2 clocks. Do not change who attends (**1.7.1**).
5. If a bucket is truly empty, the correct text is **`none`**, not silence.

**Expected Outcome:**
- Three example summaries
- One complete five-line report
- Four missing/misplaced-element calls
- No handoff-line redo

---

## 4. Knowledge Check

1. Name the **five** required buckets.
2. What do you write if a bucket has nothing?
3. Why are **planned** outages and **occurred-this-shift** outages different lines?
4. Why is “here are the open tickets” not a complete changeover report?
5. Where do you record the report, and which lesson taught that?

---

## 5. Summary

- Five buckets, or explicit **none**.
- Complete report + reject the missing-element draft.
- This closes unit **1.7**. Next unit: **1.8** Site-specific knowledge.

---

## 6. References & Further Reading

- Related modules:
  - 1.7.1 – Shift changeover process (previous)
  - 1.6.1 – Report types
  - 1.8.1 – Environment orientation (next unit)
- Local changeover template (optional — same five buckets, site field names)
