# Module 2.9.2 – AnyRun

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.2 B / C / C ; 2.9.2.1 3c / 4c / 4c  
- Hunter: 2.9.2 A / B / B ; 2.9.2.1 2b / 3c / 4c  
- SOC: 2.9.2 A / A / B ; 2.9.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Search AnyRun submissions by tag, IP, domain, or hash.
2. Review a submission and extract **actionable** intel (who / what — **2.1.5**), from a classroom card.

**Mapped Proficiency Items:**
- K: 2.9.2 – AnyRun
- T: 2.9.2.1 – Search and review AnyRun submissions for actionable intelligence

---

## 1. Key Concepts

CTI analysts search **public detonations** for a seed they already have. When to pick AnyRun is **0.7**. This hour is **search + review**. Card only. No live account.

| Move | Job |
|------|-----|
| **Search** | Tag, IP, domain, or hash you have (update domain / `update.exe` hash) |
| **Review** | Process tree, network, dropped files **on the card** |
| **Extract** | A who + what someone can act on — or **not on card** |

**What good looks like:** search `203.0.113.88` or the hash. Extract a contacted URI or dropped name **if present**. Do not invent a beacon POST (not the main plot). A count of “malicious” tags is **information**, not intelligence.

---

## 2. Knowledge Check

1. This hour is “when to pick AnyRun.” True or false?
2. What four things can you search by?
3. You open a card for the `update.exe` hash. Name one extract that is legal, and one you must **not** invent.

---

## 3. Summary

Search the seed. Review the card. Extract who/what or say missing. No live account.

**Next:** **2.9.3** Silent Push.

---

## 4. Related modules

- 2.9.1 – VirusTotal (previous)
- 2.9.3 – Silent Push
- 0.7 – When to pick AnyRun
- 2.1.5 – Actionable
