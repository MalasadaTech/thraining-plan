# Module 2.7.2 – Diamond Model Application in CTI

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.2 B / C / C ; 2.7.2.1 3c / 4c / 4d  
- Hunter: 2.7.2 B / C / C ; 2.7.2.1 3c / 4c / 4d  
- SOC: 2.7.2 A / B / B ; 2.7.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Fill the four Diamond vertices from a report or activity set.
2. Name the **weakest** vertex and reject a vendor-name **Adversary** fill.

**Mapped Proficiency Items:**
- K: 2.7.2 – Diamond Model application in CTI
- T: 2.7.2.1 – Apply the Diamond Model to an intelligence problem

---

## 1. Key Concepts

CTI analysts use Diamond to see **what they know and do not know**. The floor is **0.6.2**. This hour is a **report / activity set**. You do **not** assign ATT&CK IDs (**2.7.1**). You do **not** fill Adversary with “PRD APT.”

| Vertex | Fill with | A12 classroom |
|--------|-----------|----------------|
| **Adversary** | Who you can defend against | Unknown cluster — **not** a vendor label |
| **Capability** | What they used | Encoded PowerShell; `update.exe` |
| **Infrastructure** | Where they hosted it | Update domain / `203.0.113.88` |
| **Victim** | Who was hit | **WS-JLEE** / `jlee` / DYA |

**Weakest** is usually **Adversary** until internals support a cluster. A PDF name does not fill that vertex.

**What good looks like:** four fills + “weakest = Adversary (label only).” Reject “Adversary = PRD APT.”

---

## 2. Knowledge Check

1. A vendor APT name fills the Adversary vertex. True or false?
2. Name the four vertices.
3. Fill Diamond for **A12** and name the weakest vertex.

---

## 3. Summary

Four vertices. Weakest named. Vendor label is not Adversary.

**Next:** **2.7.3** Kill Chain for CTI.

---

## 4. Related modules

- 2.7.1 – ATT&CK for CTI (previous)
- 2.7.3 – Kill Chain
- 0.6.2 – Diamond floor
- 2.1.7 – Attribution
