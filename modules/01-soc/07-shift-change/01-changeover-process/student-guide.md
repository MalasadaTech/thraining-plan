# Module 1.7.1 – Shift Changeover Process

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.7.1.1 A / B / C · 1.7.1.2 2b / 3c / 4c  
- Hunter: 1.7.1.1 A / B / B · 1.7.1.2 1a / 2b / 3c  
- CTI: 1.7.1.1 A / A / A · 1.7.1.2 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain **why** a structured shift change exists.
2. Name **who** must participate and **where** the changeover is recorded.
3. **Conduct or participate**: write a handoff line (who runs it, who attends, your role, record location) and reject the informal path.

**Mapped Proficiency Items:**
- K: 1.7.1.1 – Shift changeover process
- T: 1.7.1.2 – Conduct or participate in a shift changeover

---

## 1. Key Concepts

This hour is the **process**: purpose, people, record location. What goes *in* the report is **1.7.2**. Incident / RFI / informational products, their clocks, and their routes are **1.6**. How to log into tools is **1.8**.

**Classroom changeover (this lesson only — not a live org policy):**

| Piece | Outline | Classroom stand-in |
|-------|---------|-------------------|
| **Purpose** | a | Incoming crew can take the floor without losing open work, outages, or urgent policy. A hallway “you’re good” is not a changeover. |
| **Who runs it** | b | **Outgoing SOC lead** conducts. **Incoming SOC lead** receives. |
| **Who must attend** | b | Both leads. Outgoing analysts who **own open cases** (or their lead covering them). **IR** only if an active incident is in handoff. |
| **Where recorded** | c | Case-system form **`SOC-CHANGEOVER`**. That is the system of record. |

If your site uses different names (bridge, watch log, “pass-down”), substitute them. The obligation is **structured + named participants + system of record**, not these labels.

**Not a changeover (classroom):** Slack DM, kitchen brief with no incoming lead, personal notebook as the only record, 1.6.3 notification ticket used *as* the changeover log.

| This lesson | Other |
|-------------|-------|
| Who / where / your role | Five content buckets — **1.7.2** |
| Not which *type* or *channel* for an incident | **1.6.1** / **1.6.3** |
| Not how to open the SIEM | **1.8** |

The task is a **handoff line**, not “we should do a shift change.”

`who runs | who attends | your role | record location | rejected informal path`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Outgoing lead runs; incoming lead + owners of open cases; log `SOC-CHANGEOVER` | Slack DM “WS-JLEE still open” and leave |
| IR in the room when A12 is still an active handoff | Kitchen brief with no incoming lead |
| Incoming analyst with no open cases **attends**, does not run | Personal notebook as the only record |

---

## 2. Detailed Walkthrough / Examples

Classroom roster: outgoing lead **Pat**, incoming lead **Riley**, you own Incident **A12** (`WS-JLEE`), Jordan owns the Night Owl **RFI**, IR analyst **Sam** is on A12.

### Example 1: Day → Swing, You Own A12 (Expected)

**Situation:** Changeover at 16:00. A12 is still open. RFI still waiting on CTI.

**Handoff:** **Pat** runs. Attend: **Riley**, **you**, **Jordan**. Your role: **outgoing analyst** — 60-second A12 brief. Record: **`SOC-CHANGEOVER`**.  
**Reject:** Telling Riley in the hallway and skipping the form.

### Example 2: Slack DM and Walk Out (Lead)

**Situation:** You DM a friend on swing: “`WS-JLEE` still open, encoded PS + Run.” You leave. No lead. No form.

**Correct handoff:** Pat runs; Riley + you + Jordan; you brief A12; **`SOC-CHANGEOVER`**.  
**Reject:** Slack DM as the changeover. Missing incoming lead. Missing system of record.  
**Lead:** The *facts* might be right. The **process** failed.

### Example 3: Active IR Not Invited (Lead)

**Situation:** Sam is downstairs with the A12 host. Pat starts changeover with only Riley and the analysts. “IR will figure it out.”

**Correct handoff:** Same as Example 1 **plus Sam**. Active incident in handoff → IR participates.  
**Reject:** “They’ll figure it out” without IR in the room (or explicitly covering on the bridge).

---

## 3. Hands-On Exercise

**Objective:** Write a handoff line and reject the informal path.

**Use the classroom roster and `SOC-CHANGEOVER`** unless the instructor overlays site names.

**Instructions:**

1. One sentence each for Examples 1–3: who runs + who attends + your role + record + rejected path.
2. For each item, write the **handoff line** (`who runs | who attends | your role | record | rejected`).

   - A. Incoming lead Riley is late. Pat briefs only you and Jordan in the kitchen and leaves.
   - B. You are the **incoming** analyst with **no** open cases. Who runs it? Do you conduct?
   - C. Pat writes the changeover only in a personal notebook. The form is empty.
   - D. Night Owl IR (Sam) is still on the floor for A12. They were not invited.

3. Do not write the five content buckets (**1.7.2**). Do not re-type the incident (**1.6.1**). Do not route A12 (**1.6.3**).
4. If the facts are right but the people or the record are wrong, say so.

**Expected Outcome:**
- Three example summaries
- Four handoff lines
- No five-bucket report

---

## 4. Knowledge Check

1. What problem does a **structured** shift change prevent?
2. Who **conducts** the classroom changeover, and who **must attend**?
3. When does **IR** participate?
4. Where is the changeover **recorded** in this lesson, and what does **not** count?
5. Why is “I told swing in chat” not participating?

---

## 5. Summary

- Purpose, named people, system of record.
- Handoff line + reject the informal path.
- Next: required content of the changeover report (**1.7.2**).

---

## 6. References & Further Reading

- Related modules:
  - 1.6.3 – Notification and distribution (previous unit)
  - 1.7.2 – Required content of the changeover report (next)
  - 1.8 – Site-specific knowledge
- Local watch-to-watch / changeover SOP (optional — substitutes classroom names)
