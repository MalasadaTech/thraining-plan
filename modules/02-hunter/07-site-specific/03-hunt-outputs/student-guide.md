# Module 2.7.3 – Hunt Outputs and Hand-off

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.7.3 B / C / C · 2.7.3.1 3c / 4c / 4c  
- SOC: 2.7.3 A / A / B · 2.7.3.1 1a / 1a / 2b  
- CTI: 2.7.3 A / A / B · 2.7.3.1 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State that **what a finished hunt must produce** and **who it is handed to** (SOC, IR, CTI) **varies by site**.
2. Treat finding that chart as **early orientation** — you do not invent recipients.
3. **Hand off** only on the path you were shown. If you were shown none, you **do not** email a made-up SOC queue.

**Mapped Proficiency Items:**
- K: 2.7.3 – Hunt outputs and hand-off
- T: 2.7.3.1 – Produce required hunt outputs and perform proper hand-off

---

## 1. Key Concepts

**2.7.2** was where the hunt is *written down*. This hour is what **leaves** the hunt: the required output and the **hand-off** to SOC, IR, or CTI.

This course **does not** publish Harbor’s output list or recipient chart. Every shop decides what “done” looks like and who gets it.

**What exists locally (outline a–b) — not the names:**

| Path | You will be shown (locally) | You do **not** do this hour |
|------|-----------------------------|-----------------------------|
| **Outputs** | What “done” always includes here (findings note, detection ask, close reason, …) | Invent “Harbor always files an incident report” |
| **Hand-off** | Which team (SOC / IR / CTI) and which local channel | Invent “email soc@harbor.example” as policy |

You still know *that* hunts often go to SOC, IR, or CTI. You do **not** know *this site’s* names, queues, or “always IR if Night Owl.”

**Orientation line:**  
`outputs / hand-off | who I asked | I have / do not have the local chart | next step`

**Hand-off line:**  
`what I think I found | output + recipient I was shown | I follow it / I still need the chart / I invented a recipient (fail)`

If no one has shown you the chart, you **do not send**.

| This lesson | Other |
|-------------|-------|
| Find and use the *site* output + recipient | Write the hunt down — **2.7.2** |
| Not SOC report *types* | **1.6** |
| Not site IR runbook | **1.8.5** |
| Not a finished CTI product | **3.11** |
| Not hunt control | **2.7.1** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| “Asked lead; no hand-off chart in this packet; I will not send yet” | “Always page IR for Night Owl” as policy |
| Park the Run-key finding until the recipient is named | Slack the SOC channel you guessed |

---

## 2. Detailed Walkthrough / Examples

**Work on the desk:** a Run-key hunt that found HKCU `Updater` on **WS-JLEE**.

### Example 1: Honest Orientation (Expected)

**Ask:** your hunt lead.  
**Shown:** nothing in *this* packet.  
**Orientation:** `outputs + hand-off | lead | do not have the local chart | get the chart before I send the Run-key finding`  
**Hand-off:** `Updater on WS-JLEE | none shown | I still need the chart`

### Example 2: Invented Recipient (Lead)

**Draft:** “Harbor always pages IR and files SOC incident type Access. I sent both.”

**Fail.** You wrote a chart this course does not own (and borrowed **1.6** / **1.8.5**).  
**Lead:** Inventing the recipient is not “proper hand-off.”

### Example 3: Found It, So I Sent It (Lead)

**Draft:** DM a SOC analyst you met at lunch. Call it handed off. Never asked the local path.

**Fail.** Channel is local (**outline b**). A friendly DM is not the site hand-off unless the lead *showed* you that.  
**Lead:** Ask who and how. Then send there.

---

## 3. Hands-On Exercise

**Objective:** Orient. Do not invent a hand-off chart. Send only on a path you were shown.

**This packet contains no local output list or recipient chart. That is intentional.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. Write an **orientation line** as a new arrival (who you would ask; that you do not have the chart in this packet).
3. **Hand-off** lines for:

   - A. Run-key finding on WS-JLEE. No chart shown.  
   - B. Your lead *in class* reads a real site chart (if they do). Follow *that* text only. If they do not, write “still need the chart.”  
   - C. “I will use the 1.6 classroom notification matrix as this hunt’s hand-off.”

4. Do not invent a SOC queue. Do not write a **3.11** product. Do not run **1.8.5**.
5. Invented Harbor recipient text is a fail.

**Expected Outcome:**
- Three example summaries
- One orientation line (do not have the chart)
- Three hand-off lines (A = need the chart; C = fail)
- No invented recipient

---

## 4. Knowledge Check

1. Why can this course **not** hand you “the” hunt hand-off chart?
2. What two local things must you obtain this hour?
3. What belongs on an **orientation line**?
4. Can you **send** the Run-key finding if no one has shown you the recipient?
5. Where do you learn SOC **report types** (not hunt hand-off)?

---

## 5. Summary

- Outputs and recipients are local. Obtain. Do not invent. Do not send without the chart.
- Hunt site-specific block ends here.

---

## 6. References & Further Reading

- Related modules:
  - 2.7.2 – Hunt documentation (previous)
  - 1.6 – SOC report types
  - 1.8.5 – Site IR process
  - 3.11 – Finished CTI products
- Your lead and the local chart they name (not this repo)
