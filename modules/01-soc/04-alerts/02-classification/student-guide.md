# Module 1.4.2 – Alert Classification

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.2.1 A / B / C · 1.4.2.2 2b / 3c / 4c  
- Hunter: 1.4.2.1 B / C / C · 1.4.2.2 2b / 3c / 4c  
- CTI: 1.4.2.1 A / A / B · 1.4.2.2 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Define True Positive, False Positive, True Negative, and False Negative.
2. Classify **given cases** (not only fired alerts) and **cite the evidence**.
3. Treat **False Negative** as a missed detection — something bad happened and no alert fired.

**Mapped Proficiency Items:**
- K: 1.4.2.1 – Alert classification (TP/FP/TN/FN)
- T: 1.4.2.2 – Classify given cases as TP, FP, TN, or FN and cite the evidence

---

## 1. Key Concepts

Classification is a **label plus evidence**. Naming the four letters is knowledge. The task is to apply them to **cases**, including cases where **no alert fired**.

| Label | Detection said | Reality | Typical object |
|-------|----------------|---------|----------------|
| **True Positive (TP)** | Bad | Bad | Fired alert, activity is malicious or policy-violating |
| **False Positive (FP)** | Bad | Benign | Fired alert, activity is authorized / expected |
| **True Negative (TN)** | Not bad | Benign | **No alert** on ordinary activity |
| **False Negative (FN)** | Not bad | Bad | **No alert** on activity that should have been detected |

**FN is not a fired alert you dislike.** It is a miss. You meet it in hunts, after-action, or a log you pulled in **1.4.1** that never produced a row in the queue.

**TN** is correctly quiet: Chrome GET of the intranet PDF, no alert. You do not ticket a TN.

| This lesson | Later / other |
|-------------|---------------|
| Which of the four labels, with evidence | *Why* this FP fired — **1.4.3** |
| Missed detection as FN | Hunt for activity controls missed — **2.1** |
| Investigation card | **1.4.1** (already done) |

Do not spend this hour on “analyst tested the rule” as a *cause class*. If the activity is benign and an alert fired, the label is **FP**. The cause is **1.4.3**.

**Evidence** is a short cite: parent + `-enc`, dest + URI, “no matching sid for :8080,” “explorer + Get-Help.” A slogan (“malicious”) is not evidence.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| TP: encoded PS from wscript, rule matches | Calling a miss “FP” because you wish it had fired |
| FP: helpdesk PowerShell help text, any-PS rule | Calling FN “the alert was wrong” |
| TN: no alert on intranet PDF | Inventing an alert so you can classify it |
| FN: GET `update.exe` on 8080, no sid | Classifying without a cite |

---

## 2. Detailed Walkthrough / Examples

### Example 1: True Positive (Expected)

**Case:** Alert `Encoded PowerShell from script host` on `WS-JLEE`. Investigation (**1.4.1** Ex 1) showed `wscript` + Temp `invoice.vbs` + `-enc`.

**Classify:** **TP**.  
**Evidence:** Encoded PowerShell from a script host is the activity the rule is for, and that activity occurred.

**Not done:** Did not open FP-cause class. Did not recategorize as “user-level” (**1.4.4**).

### Example 2: False Positive (Lead as a *label*)

**Case:** Alert `Any PowerShell` on `WS-JLEE`. **1.4.1** Ex 2 logs added `explorer.exe` + `Get-Help`. User asked for help text.

**Classify:** **FP**.  
**Evidence:** A process create of PowerShell occurred, but the activity is ordinary interactive help, not the encoded/script-host pattern.

**Interpretation:** The label is FP. *Why* the rule fired (it is only `Image=powershell.exe`) is **1.4.3**. Stop at the label + cite here.

### Example 3: False Negative (Lead — missed detection)

**Case:** Zeek `http` and PCAP show `10.10.22.17` GET `/payload/update.exe` on **8080** (**1.2.5** Ex 3). Queue has **no** alert. Sid `1000001` is deployed only for `$EXTERNAL_NET` on **80/443** in this classroom story — 8080 is out of scope.

**Classify:** **FN**.  
**Evidence:** The download occurred (PCAP/URI). No detection fired. That is a miss, not an FP.

**Nearby TN (not a third full example):** Chrome GET `intranet.buildingc.internal/docs/q3-notes.pdf` on 80, no alert. **TN** — correctly quiet. Cite: expected intranet GET, no matching malicious pattern.

---

## 3. Hands-On Exercise

**Objective:** Classify cases and cite evidence. Include at least one FN.

**Instructions:**

1. One sentence each for Examples 1–3: label + cite.
2. Classify each case below. Write **TP / FP / TN / FN** and **one evidence sentence**. At least one must be FN.

   - A. SIEM alert `Office Spawns Cmd`: `WINWORD.EXE` → `cmd.exe` on `WS-FIN01` after a macro the user did not expect.
   - B. No alert. `finance` ran `WINWORD.EXE` → `cmd.exe` to run a documented internal export script.
   - C. No alert. Same GET `/payload/update.exe` as Example 3, different host `10.10.22.18`.
   - D. Alert `BUILDINGC TRAIN GET /payload/update.exe` on a packet-broker **replay** of yesterday’s PCAP during a 7-level lab (traffic is the lab replay, not a live user).
   - E. No alert. `jlee` opened intranet `q3-notes.pdf` in Chrome.

3. For **one** FP in this exercise, do **not** write the cause class — that is **1.4.3**. Just the label + cite.
4. Do not assign scan/root/user categories (**1.4.4**).

**Expected Outcome:**
- Three example summaries
- Five classifications with a cite each
- At least one FN
- No FP-cause write-up

---

## 4. Knowledge Check

1. Define TP, FP, TN, and FN in one line each.
2. Why is FN **not** “a bad alert in the queue”?
3. What counts as **evidence** when you classify?
4. Give one TN that should never become a ticket.
5. You have an FP. What does this lesson stop at, and what is the next unit?

---

## 5. Summary

- Four labels. TN and FN usually have **no** queue row.
- Classify the **case** and cite evidence. FN = miss.
- Why an FP fired is **1.4.3**. Next: common false positive causes.

---

## 6. References & Further Reading

- Related modules:
  - 1.4.1 – Alert context and investigation (previous)
  - 1.4.3 – Common false positive causes (next)
  - 2.1 – Purpose of threat hunting (missed activity)
