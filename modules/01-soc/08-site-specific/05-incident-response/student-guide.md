# Module 1.8.5 – Incident Response Processes

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.8.5.1 2b / 3c / 4c  
- Hunter: 1.8.5.1 3c / 4c / 4c  
- CTI: 1.8.5.1 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Follow the **site IR process** for a given situation.
2. Name the **next process step** and **who owns containment**.
3. Reject **freelance** containment.

**Mapped Proficiency Items:**
- T: 1.8.5.1 – Follow site-specific incident response processes

---

## 1. Key Concepts

You already know the **incident type** and **route** (**1.6**) and **where notes go** (**1.8.4**). This hour is **follow the IR card** — not invent containment.

**Classroom IR card (this lesson only — not a live playbook):**

| Step | Harbor stand-in |
|------|-----------------|
| 1 | Confirm **incident** (**1.6.1**) and use/open the **incident ticket** |
| 2 | Page IR: ticket + duty SOC lead (**1.6.3**) — do not SMS-only |
| 3 | Read the **severity** row (below) — that row says who owns containment |
| 4 | Record every action in the ticket (**1.8.4**) |
| 5 | Do **not** wipe a host. Do **not** isolate OT or a crown jewel without IR |

| Severity | When (Harbor) | Containment owner |
|----------|---------------|-------------------|
| **Sev1** | Crown jewel, OT, or widespread | **IR lead** — SOC does not freelance |
| **Sev2** | Single user host (A12 / `WS-JLEE`) | SOC may isolate **with IR concurrence** |
| **Sev3** | No live host / awareness only | SOC documents — no isolate |

If your site has a real playbook, use it. The obligation is **next step + owner + reject freelance**, not these Sev numbers.

| This lesson | Other |
|-------------|-------|
| Follow the IR card | Who gets the *report* — **1.6.3** |
| Not the notes *location* | **1.8.4** |
| Crown jewel *identity* | **1.8.1.f** |

The task is a **process line**:

`situation | severity | next step | who owns containment | rejected freelance`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| A12 Sev2 → page IR, isolate only with concurrence | Unplug `pay-db-01` without IR |
| OT historian Sev1 → IR owns | SOC isolates OT “to be safe” |
| TN PDF Sev3 → document only | Opening Sev1 for an informational |

---

## 2. Detailed Walkthrough / Examples

### Example 1: A12 Sev2 (Expected)

**Situation:** Confirmed incident. Encoded PS + Run on `WS-JLEE` only.

**Severity:** **Sev2**.  
**Next:** Incident ticket + page IR (ticket + duty lead).  
**Containment:** Isolate `WS-JLEE` **only with IR concurrence**.  
**Reject:** Unplug the NIC before IR is in the loop.

### Example 2: Unplug the Payroll DB (Lead)

**Situation:** Suspicious query on `pay-db-01` (`10.10.20.15`). Analyst pulls the cable.

**Severity:** **Sev1** (crown jewel).  
**Next:** Ticket + page IR. **IR lead** owns containment.  
**Reject:** Freelance unplug.  
**Lead:** The *instinct* (protect payroll) is not the process.

### Example 3: OT Historian (Lead)

**Situation:** Beacon-like traffic from `ot-hist-01`.

**Severity:** **Sev1** (OT).  
**Next:** Page IR. SOC does **not** isolate OT.  
**Reject:** “Sev2 — it’s one host.” OT is Sev1 on this card regardless of host count.

---

## 3. Hands-On Exercise

**Objective:** Write the process line and reject freelance.

**Use the Harbor IR card.**

**Instructions:**

1. One sentence each for Examples 1–3: severity + next + owner + rejected.
2. For each item, write the **process line**.

   - A. Confirmed incident on `WS-JLEE` only. IR is already on the ticket.
   - B. Guest-network malware, one laptop, no jewel, no OT. First IR page.
   - C. Informational TN PDF — lead wants the DC “taken offline just in case.”
   - D. Widespread encoded-PS on **twelve** user PCs.

3. Do not rewrite the 1.6.3 route chart. Do not move notes to Slack (**1.8.4**).
4. If C is not an incident, say **Sev3 / document** and reject isolating `dc-01`.

**Expected Outcome:**
- Three example summaries
- Four process lines
- No notes-location redo, no Harbor architecture lecture

---

## 4. Knowledge Check

1. What are the Harbor **severity** rows, and who owns containment on each?
2. What is the **next step** after you confirm an incident?
3. Why is unplugging `pay-db-01` not “following IR process”?
4. How is this different from **1.6.3** (who gets the report)?
5. Who owns the live playbook if it differs from Harbor Sev1/2/3?

---

## 5. Summary

- Next step + owner. Reject freelance.
- This closes unit **1.8**. Hunt unit **2.1** is next in the outline (not generated here).

---

## 6. References & Further Reading

- Related modules:
  - 1.8.4 – Investigation documentation (previous)
  - 1.6.1 – Report types
  - 1.6.3 – Notification and distribution
  - 1.8.1 – Crown jewels / OT (orientation)
- Local IR playbook / severity matrix (optional — substitutes Harbor)
