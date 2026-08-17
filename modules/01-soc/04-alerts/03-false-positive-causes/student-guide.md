# Module 1.4.3 – Common False Positive Causes

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.3.1 A / B / C ; 1.4.3.2 2b / 3c / 4c  
- Hunter: 1.4.3.1 B / C / C ; 1.4.3.2 2b / 3c / 4c  
- CTI: 1.4.3.1 A / A / B ; 1.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two cause classes: analyst/tool activity, and untuned or overly broad logic.
2. Given an FP, pick the class and say **what you would change**.

**Mapped Proficiency Items:**
- K: 1.4.3.1 – Common false positive causes
- T: 1.4.3.2 – Given a false positive, identify the cause class and what you would change

---

## 1. Key Concepts

The case is **already an FP** (**1.4.2**). This hour you pick a **cause class** and a **change**. You do **not** re-argue TP vs FP. You do **not** deploy the change (**1.3** / **4.x**). You do **not** pick scan/root/user (**1.4.4**).

| Class | What it looks like | Change you can name |
|-------|--------------------|---------------------|
| **a. Analyst or tool activity** | Someone tested a rule that is already live; packet replay; a scanner the shop owns | Exclude the lab/replay/scanner identity; test in a lab window — not “delete the rule” |
| **b. Untuned or overly broad logic** | Any PowerShell; `content:"GET"` on any TCP; MZ-only YARA wired to an alert | Add a second selector (parent + `-enc`); bind an HTTP buffer; raise a threshold |

Those two classes are the syllabus. If neither fits, say **other — not a/b** and still name a change. Do not invent a third official class.

A change is one concrete sentence: “Require parent `wscript` and `-enc`.” Not “tune it.”

**What good looks like:**

- **b:** FP on any-PowerShell / `Get-Help` (**1.4.2**). Class **b**. Change: propose the **1.3.1** shape — `-enc` and a script-host parent. Hand it to DE.
- **a:** FP because an analyst replayed yesterday’s `GET /update.exe` PCAP into production. Class **a**. Change: exclude the replay window or interface. Do not delete the `/update.exe` signature.

---

## 2. Knowledge Check

1. This hour is for deciding TP vs FP. True or false?
2. What are the two syllabus cause classes?
3. FP: any-PowerShell on `Get-Help`. Class and one change sentence.

---

## 3. Summary

After FP: **class + change**. Analyst/tool vs overly broad. Name the change; you do not deploy it.

**Next:** **1.4.4** Common alert categorizations.

---

## 4. Related modules

- 1.4.2 – Alert classification (previous)
- 1.4.4 – Common alert categorizations
- 1.3.1 – SIGMA rules
- 4.x – How detections run as a service
