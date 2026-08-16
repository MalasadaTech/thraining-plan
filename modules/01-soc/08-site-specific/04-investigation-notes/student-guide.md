# Module 1.8.4 – Investigation Documentation

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.8.4.1 2b / 3c / 4c  
- Hunter: 1.8.4.1 3c / 4c / 4c  
- CTI: 1.8.4.1 2b / 3c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name **where** investigation notes are saved.
2. Name **how** they are written (minimum fields).
3. Reject the unofficial copy as the only record.

**Mapped Proficiency Items:**
- T: 1.8.4.1 – Where and how to save investigation notes

---

## 1. Key Concepts

This hour is the **working notes** for a case. It is not the 1.6 *report type*, not the 1.7.1 *changeover form*, and not the 1.8.5 *IR step*.

**Classroom notes card (this lesson only):**

| Piece | Harbor stand-in |
|-------|-----------------|
| **System of record** | The **case ticket worklog** (`https://ticket.harbor.internal` — A12, RFI, etc.) |
| **Optional twin** | SOC wiki `https://notes.harbor.internal/<case>` **linked from the ticket** |
| **How** | Timestamp, case ID, **fact vs hypothesis** labeled, next action |
| **Not the only copy** | Desktop `notes.txt`, Slack/Teams DM, personal email, USB |

If your site uses a different case system, substitute it. The obligation is **approved location + how + reject unofficial-only**.

| This lesson | Other |
|-------------|-------|
| Working notes on a case | Changeover form — **1.7.1** `SOC-CHANGEOVER` |
| Not the incident/RFI *type* | **1.6.1** |
| Not “page IR” | **1.8.5** |

The task is a **notes line**:

`case | where | how (fields) | rejected unofficial path`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| A12 facts in A12 worklog | Word file on the desktop as the only copy |
| Hypothesis labeled in the ticket | Slack paste as the record |
| Wiki OK if **linked** from the ticket | Wiki only, ticket empty |

---

## 2. Detailed Walkthrough / Examples

### Example 1: A12 Worklog (Expected)

**Need:** record `wscript` → `powershell -enc` and the Run key on `WS-JLEE`.

**Where:** Ticket **A12 worklog**.  
**How:** `15:05 | A12 | FACT: Run key set to Temp\update.exe | next: 1.8.5 IR concurrence on isolate`.  
**Reject:** Keeping that only in a local editor.

### Example 2: Desktop File Only (Lead)

**Draft:** “I have a solid Word doc on the desktop. I’ll paste it later.”

**Correct:** Worklog first (or same time). Desktop is a scratch pad, not the record.  
**Lead:** The *content* may be good. The **location** failed.

### Example 3: Slack as the Record (Lead)

**Draft:** Full encoded command line pasted to a hunter channel “so it’s searchable.”

**Correct:** Ticket worklog. Optional wiki **link**.  
**Reject:** Chat as the only copy. (Wrong 1.6.3 *channel* is a different fail — here the fail is **notes location**.)

---

## 3. Hands-On Exercise

**Objective:** Write the notes line and reject the unofficial-only path.

**Use the Harbor notes card.**

**Instructions:**

1. One sentence each for Examples 1–3: where + how + rejected.
2. For each item, write the **notes line**.

   - A. RFI to CTI on `nightowl-updates.net` — you just got “cluster known, see TLP:AMBER note.”
   - B. Scratch timeline in Notepad during a live call. Call ends. Ticket still empty.
   - C. Wiki page written and **linked** from A12. Worklog has the link + a one-line summary.
   - D. USB stick “so I can finish at home.”

3. Do not rewrite the incident type (**1.6.1**). Do not file the changeover form (**1.7.1**). Do not choose isolate vs not (**1.8.5**).
4. If C has ticket + linked wiki, that is **complete**.

**Expected Outcome:**
- Three example summaries
- Four notes lines
- No IR decision, no changeover buckets

---

## 4. Knowledge Check

1. What is the Harbor **system of record** for investigation notes?
2. What four things belong in **how** you write a note?
3. When is the wiki allowed?
4. Why is “I’ll paste it later” not saving notes?
5. How is this different from the **1.7.1** changeover form?

---

## 5. Summary

- Ticket worklog first. Wiki only if linked. Reject unofficial-only.
- Next: follow site IR process (**1.8.5**).

---

## 6. References & Further Reading

- Related modules:
  - 1.8.3 – Tool access (previous)
  - 1.8.5 – Incident response processes (next)
  - 1.7.1 – Changeover record location
- Local case-system / notes SOP (optional — substitutes Harbor)
