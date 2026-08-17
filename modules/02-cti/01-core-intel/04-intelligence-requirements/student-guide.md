# Module 2.1.4 – Intelligence Requirements

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.4 B / C / C ; 2.1.4.1 3c / 4c / 4d ; 2.1.4.2 3c / 4c / 4d ; 2.1.4.3 3c / 4c / 4c  
- Hunter: 2.1.4 A / B / B ; 2.1.4.1 1a / 2b / 3c ; 2.1.4.2 1a / 2b / 3c ; 2.1.4.3 1a / 2b / 3c  
- SOC: 2.1.4 A / A / B ; 2.1.4.1 1a / 1a / 1a ; 2.1.4.2 1a / 1a / 1a ; 2.1.4.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why a requirement exists, and what a **PIR** is versus any other requirement.
2. Refine or translate a question into a clear requirement, and say what work it drives.

**Mapped Proficiency Items:**
- K: 2.1.4 – Intelligence requirements and Priority Intelligence Requirements (PIRs)
- T: 2.1.4.1 – Develop or refine intelligence requirements
- T: 2.1.4.2 – Translate stakeholder questions into clear intelligence requirements
- T: 2.1.4.3 – Explain how a given requirement drives analytic work

---

## 1. Key Concepts

CTI analysts write the **question the work exists to answer** so collection does not become “everything interesting.” Type (**2.1.3**) is the kind of answer. This hour is the **question**. You do **not** score actionable (**2.1.5**). You do **not** pick OSINT vs commercial (**2.1.8**). You do **not** invent a shop PIR list (**2.12.1**).

| Idea | Meaning |
|------|---------|
| **Purpose** | Focus collection and analysis on a decision |
| **PIR** | A *priority* requirement — leadership or the program ranked it. Standing and ad-hoc IRs are still requirements; they are not all PIRs |
| **Drives work** | Names what you collect, what you analyze, and what you will **not** chase |

A clear requirement is a **question** plus **whose decision** plus **what you will not chase**. If your shop publishes PIR IDs, use those. Do not invent a DYA list here.

**What good looks like:**

- **Translate:** Stakeholder: “Are we seeing them?” Refine: “Is the update domain the payload host for **A12** in this window?” Not a PIR ID you made up.
- **Drives work:** Collect the A record / file you already have. Analyze whether it answers that question. Do **not** chase the sibling domain — that is later enrichment (**2.5** / **2.8**), not this requirement.

---

## 2. Knowledge Check

1. Every intelligence requirement is a PIR. True or false?
2. What does a PIR add that a standing or ad-hoc IR may not have?
3. “Are we seeing them?” Translate it for **A12**, and name one thing the requirement tells you **not** to chase.

---

## 3. Summary

A requirement is the question. A PIR is a *ranked* one. It drives what you collect and what you skip. Do not invent the shop list.

**Next:** **2.1.5** Ensuring intelligence is actionable.

---

## 4. Related modules

- 2.1.3 – Intelligence types (previous)
- 2.1.5 – Actionable intelligence
- 2.1.8 – Collection source classes
- 2.12.1 – Local PIR list (obtain, do not invent)
