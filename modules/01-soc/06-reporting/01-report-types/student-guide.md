# Module 1.6.1 – Report Types

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.6.1.1 A / B / C · 1.6.1.2 2b / 3c / 4c  
- Hunter: 1.6.1.1 B / C / C · 1.6.1.2 2b / 3c / 4c  
- CTI: 1.6.1.1 B / C / C · 1.6.1.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain **incident report**, **RFI**, and **other** types used in the environment.
2. Identify the correct type for a situation and **why it is not the adjacent type**.

**Mapped Proficiency Items:**
- K: 1.6.1.1 – Report types
- T: 1.6.1.2 – Identify the correct report type and why it is not the adjacent type

---

## 1. Key Concepts

A **report type** is the *kind of record* you open. It is not the alert category (**1.4.4**), not TP/FP (**1.4.2**), and not a finished intel product (**3.11**). Shift-change write-ups are **1.7**.

| Type | Use when | Adjacent — do not confuse with |
|------|----------|--------------------------------|
| **Incident report** | You are recording a security incident (or a strongly supported suspected incident) that needs a case / IR handoff | **RFI** — you already have enough to *record the incident*; you are not primarily asking a question |
| **RFI** | You need **information** from another team or org (CTI, hunt, IT, vendor) to continue | **Incident** — an RFI can sit *beside* an incident; the RFI *is* the question, not the case record |
| **Other (local)** | Types your site already named (classroom: **Informational / awareness note**) | Do not invent “intel report” or “shift changeover” here — those are **3.11** / **1.7** |

Classroom **other** = **Informational note**: awareness only (no IR case). If your site has more names, use those under **other** and still reject the neighbor.

| This lesson | Later / other |
|-------------|---------------|
| Which *type* | When it is due — **1.6.2** |
| Which *type* | Who gets it / which channel — **1.6.3** |
| Not a changeover log | **1.7** |

The task is **type + reject the neighbor**, not “pick an appropriate report.”

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| TP encoded PS + Run persist → **Incident** | Same facts opened as RFI “is this bad?” |
| Need Night Owl attribution from one IP → **RFI** to CTI | Opened as a new incident with no case facts |
| TN intranet PDF, lead wants FYI → **Informational** | Opened as incident |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Incident, Not RFI (Expected)

**Situation:** **1.4.2** TP — `wscript` → `powershell -enc`, HKCU Run set to Temp `update.exe`. You need a case record and IR handoff.

**Type:** **Incident report**.  
**Not RFI:** You are not asking another team a question as the *primary* act. You are recording what happened. (A later RFI to CTI on the domain is a *second* product.)

### Example 2: RFI, Not Incident (Lead)

**Situation:** Incident A12 already exists for the beacon. You want CTI to say whether `checkin.nightowl-updates.net` is a known cluster. You have no new host activity.

**Type:** **RFI** (to CTI).  
**Not incident:** The case already exists. This product is a **question**. Opening a second incident for the same host/story is the wrong type.

### Example 3: Informational, Not Incident (Lead)

**Situation:** Chrome GET of intranet `q3-notes.pdf`. Classified **TN**. SOC lead wants a one-line awareness note that the any-GET-exe rule did *not* fire (correctly).

**Type:** **Other — Informational**.  
**Not incident:** There is no incident to record.  
**Not RFI:** You are not asking anyone for data.

---

## 3. Hands-On Exercise

**Objective:** Pick the type and reject the neighbor.

**Instructions:**

1. One sentence each for Examples 1–3: type + rejected neighbor.
2. For each situation, write **type**, **adjacent you reject**, and **why**.

   - A. GET `/payload/update.exe` on 8080, **FN** (no alert). You are opening the first record so IR can take the host.
   - B. You need IT to confirm whether `10.10.8.90` is the documented vuln-mgmt scanner (**1.4.3**).
   - C. End of shift; you must list open investigations for the next crew (**do not** use 1.6 types for this).
   - D. Leadership asked “are we seeing Night Owl?” after a news story. No matching internal case.

3. Do not write the report body. Do not assign a 1.4.5 clock. Do not route it (**1.6.3**).

**Expected Outcome:**
- Three example summaries
- Four type + neighbor pairs (C should point at **1.7**, not a 1.6 type)
- No timeline, no distribution chart

---

## 4. Knowledge Check

1. What is an **incident report** for, versus an **RFI**?
2. What belongs under **other** in this syllabus, and what must you *not* park there?
3. Why can an RFI sit *beside* an incident without being a second incident?
4. Why is “pick an appropriate report” not enough for sign-off?
5. Where does a shift-change write-up belong?

---

## 5. Summary

- Incident = case record. RFI = question. Other = named local types (classroom: informational).
- Reject the neighbor. Shift change is **1.7**.
- Next: reporting timelines (**1.6.2**).

---

## 6. References & Further Reading

- Related modules:
  - 1.4.2 – Alert classification
  - 1.6.2 – Reporting timelines (next)
  - 1.6.3 – Notification and distribution
  - 1.7 – Shift change
  - 3.11 – Intelligence production
- Local report-type list used on shift (optional)
