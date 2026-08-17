# Module 2.9.1 – VirusTotal (Relations and Behavior)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.1 B / C / C ; 2.9.1.1 3c / 4c / 4d  
- Hunter: 2.9.1 B / C / C ; 2.9.1.1 3c / 4c / 4d  
- SOC: 2.9.1 A / B / B ; 2.9.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use **Relations** to name additional infra from a seed you already have.
2. Use **Behavior** to extract file, network, registry, or process events.

**Mapped Proficiency Items:**
- K: 2.9.1 – VirusTotal (Relations and Behavior tabs)
- T: 2.9.1.1 – Use VirusTotal Relations and Behavior to pivot and extract events

---

## 1. Key Concepts

CTI analysts open the **tabs** 0.7 told them to pick VT *for*. Purpose / when is **0.7**. The hop *sentence* is **2.8.1**. This hour is **Relations** and **Behavior**. Classroom card only — no live account required. Hunt conversion to SIEM is **3.3.1**.

| Tab | Job |
|-----|-----|
| **Relations** | Contacted domains / IPs / dropped files from a seed hash or URL |
| **Behavior** | Process, file, registry, network events from a sandbox run |

**What good looks like:**

- **Relations:** seed = hash of `invoice.vbs` or `update.exe`. Write contacted host / dropped name **if the card has it**. Or **not on card**.
- **Behavior:** extract one process or file event that adds to **A12** (e.g. a write to Temp). Do not invent a Run key if the card does not show it.

---

## 2. Knowledge Check

1. This hour is “when to pick VT.” True or false?
2. What does Relations give you that Behavior does not?
3. Seed hash of `update.exe`. One Relations result you may write, and one thing you must **not** invent.

---

## 3. Summary

Relations = extra infra. Behavior = events. Card only. Do not invent a hit.

**Next:** **2.9.2** AnyRun.

---

## 4. Related modules

- 2.8.4 – Relevance (previous)
- 2.9.2 – AnyRun
- 0.7 – When to pick VT
- 2.8.1 – Hop sentence
