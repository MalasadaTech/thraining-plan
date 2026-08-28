# Module 1.4.2 – Alert Classification

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.2.1 A / B / C ; 1.4.2.2 2b / 3c / 4c  
- Hunter: 1.4.2.1 B / C / C ; 1.4.2.2 2b / 3c / 4c  
- CTI: 1.4.2.1 A / A / B ; 1.4.2.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Define **True Positive (TP)**, **False Positive (FP)**, **True Negative (TN)**, and **False Negative (FN)**.
2. Classify a given case and **cite the evidence**, including at least one miss as FN.

**Mapped Proficiency Items:**
- K: 1.4.2.1 – Alert classification (TP/FP/TN/FN)
- T: 1.4.2.2 – Classify given cases as TP, FP, TN, or FN and cite the evidence

---

## 1. Key Concepts

After you have looked at a case, you still have to **classify** it. A classification says whether the detection was right — a real hit, a noisy fire, ordinary activity that correctly stayed quiet, or a miss. You also **cite the evidence**: a short pointer to the field or log that proves the label. That is the job in this lesson. Without a label, the next person cannot tell a real hit from a miss. Without a cite, “malicious” is a slogan.

**1.4.1** gathered context on a fired alert. This lesson is the four labels. It is **not** why a false positive fired (**1.4.3**). It is **not** scan / root / user (**1.4.4**).

Fired alerts sit in an **alert queue** — the list waiting for an analyst. True negatives and false negatives usually are **not** in that list, because nothing fired.

| Label | Detection said | Reality |
|-------|----------------|---------|
| **True Positive (TP)** | Bad | Bad — a fired alert, and the activity is what the rule is for |
| **False Positive (FP)** | Bad | Benign — a fired alert, authorized or expected activity |
| **True Negative (TN)** | Not bad | Benign — **no alert**, ordinary activity |
| **False Negative (FN)** | Not bad | Bad — **no alert**, activity that should have been detected |

A **false negative is not a fired alert you dislike.** It is a **miss**. You find it in related logs, in a hunt, or after an incident — not as a fired alert in the queue.

**Evidence** is a short cite: parent plus `-enc`, destination plus URI, “no alert on that GET.” A slogan (“malicious”) is not evidence.

**What good looks like:** someone gives you a case. You name TP, FP, TN, or FN. You point at the field or log that proves it.

- **TP:** Alert `Encoded PowerShell from script host`. Cite: `wscript` plus `-enc` is the activity the rule is for, and it happened (**1.4.1**).
- **FP:** Alert on any PowerShell; logs show interactive `Get-Help`. Cite: PowerShell ran; it is ordinary help, not encoded script-host. *Why* the rule is broad is **1.4.3**.
- **TN:** No alert on ordinary browser activity. Cite: expected browse, no matching bad pattern. Do not invent an alert so you can classify it.
- **FN:** HTTP shows `GET /update.exe` to `203.0.113.88:8080`, **no** alert in the queue. Cite: the download occurred; nothing fired. That is a miss.

Do not pick a category yet (**1.4.4**). Do not explain why the false-positive rule is noisy (**1.4.3**).

---

## 2. Knowledge Check

1. FN is a bad alert sitting in the queue. True or false?
2. Alert `Encoded PowerShell from script host`, `wscript` + `-enc` confirmed. Classify and cite.
3. `GET /update.exe` to `203.0.113.88:8080`, no alert. Classify and cite.

---

## 3. Summary

Four labels. A true negative and a false negative usually have **no** alert in the queue. Classify the case and cite the evidence. Why a false positive fired is next.

**Next:** **1.4.3** Common false positive causes.

---

## 4. Related modules

- 1.4.1 – Alert context and investigation (previous)
- 1.4.3 – Common false positive causes
- 1.1.2 – Process activity
- 1.2.5 – HTTP engine
