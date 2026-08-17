# Module 2.7.1 – Hunt Control and Lead Management

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.7.1 B / C / C · 2.7.1.1 3c / 4c / 4c  
- SOC: 2.7.1 A / A / B · 2.7.1.1 1a / 1a / 2b  
- CTI: 2.7.1 A / A / B · 2.7.1.1 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State that **how hunts start, who controls them, and how leads are managed** **varies by site**.
2. Treat finding that path as **early orientation** — you do not invent it.
3. **Follow** the process you were shown. If you were shown none, you **do not open** a hunt on a made-up ticket.

**Mapped Proficiency Items:**
- K: 2.7.1 – Hunt control and lead management
- T: 2.7.1.1 – Follow the local process for initiating and controlling a hunt

---

## 1. Key Concepts

**2.6.3** wrote a hunt for a named technique. **2.2.2** taught the hunt card. This hour is the **site path** that makes that hunt official — who starts it, who owns it, where leads go.

This course **does not** publish Harbor’s hunt ticket, queue, or lead board. Every shop builds its own. A new hunter asks and records the path.

**What exists locally (outline a–b) — not the names:**

| Path | You will be shown (locally) | You do **not** do this hour |
|------|-----------------------------|-----------------------------|
| **Initiate** | How a hunt is opened | Invent “file a Harbor Hunt-17” |
| **Control** | Who can widen scope / pause / stop | Run Night Owl because it is interesting |
| **Leads** | Where new leads are parked and who triages them | Stand up a personal spreadsheet as policy |

**Orientation line:**  
`path (initiate / control / leads) | who I asked | I have / do not have the local steps | next step`

**Follow line:**  
`what I want to start | path I was shown | I follow it / I still need the path / I invented a path (fail)`

If no one has shown you the path, you **do not start** and you **do not invent** one.

| This lesson | Other |
|-------------|-------|
| Find and follow the *site* path | Write the hunt line — **2.6.3** |
| Not hunt-card format | **2.2.2** |
| Not hunt-type execute | **2.2.1** |
| Not SOC ticket types | **1.6** |
| Not hunt documentation store | **2.7.2** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| “Asked lead; no hunt queue in this packet; I will not open one yet” | “Harbor uses Jira board HUNT” as policy |
| Park the Run-key hunt until the path is shown | Start it in Slack because the pattern is good |

---

## 2. Detailed Walkthrough / Examples

**Work on the desk:** the **2.6.3** Run-key hunt (`Updater` → `%TEMP%\update.exe`).

### Example 1: Honest Orientation (Expected)

**Ask:** your hunt lead, first week.  
**Shown:** nothing in *this* packet.  
**Orientation:** `initiate | lead | do not have the local steps | get the path before I open the Run-key hunt`  
**Follow:** `start the Run-key hunt | none shown | I still need the path`

### Example 2: Invented Queue (Lead)

**Draft:** “Harbor Hunt tickets go in Jira project HUNT. I opened HUNT-17 for Night Owl.”

**Fail.** You wrote a control path this course does not own.  
**Lead:** Inventing the queue is not “following” it.

### Example 3: Interesting, So I Started (Lead)

**Draft:** Start the Run-key hunt in a personal note because the pattern is clean. Never asked who controls scope.

**Fail.** Control is local (**outline a**). Uncontrolled work is not followed process.  
**Lead:** Ask first. Then follow or wait.

---

## 3. Hands-On Exercise

**Objective:** Orient. Do not invent a hunt queue. Follow only a path you were shown.

**This packet contains no local hunt-control process. That is intentional.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Identify:** write an **orientation line** as a new arrival (who you would ask; that you do not have the path in this packet).
3. **Follow** lines for:

   - A. You want to open the Run-key hunt. No path shown.  
   - B. Your lead *in class* reads a real site path (if they do). Follow *that* text only. If they do not, write “still need the path.”  
   - C. “I will use last course’s example Jira board as this section’s process.”

4. Do not invent a ticket ID. Do not rewrite **2.6.3**. Do not write **2.7.2** documentation.
5. Invented Harbor queue text is a fail.

**Expected Outcome:**
- Three example summaries
- One orientation line (do not have the path)
- Three follow lines (A = need the path; C = fail)
- No invented ticket

---

## 4. Knowledge Check

1. Why can this course **not** hand you “the” hunt-control process?
2. What is the **first** task for a newly arrived hunter this hour?
3. What belongs on an **orientation line**?
4. Can you **open** the Run-key hunt if no one has shown you the path?
5. Where do you learn **where hunts are written down**?

---

## 5. Summary

- Initiate, control, and leads are local. Obtain. Do not invent.
- Next: **2.7.2** Hunt documentation standards.

---

## 6. References & Further Reading

- Related modules:
  - 2.6.3 – Hunt for a named technique (previous)
  - 2.2.2 – Hunt development
  - 2.7.2 – Hunt documentation (next)
- Your lead and the local store they name (not this repo)
