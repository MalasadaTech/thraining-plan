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

1. Say why an intelligence requirement exists, and what a **Priority Intelligence Requirement (PIR)** is versus any other requirement.
2. Refine or translate a stakeholder question into a clear requirement, and say what collection and analysis it drives.

**Mapped Proficiency Items:**
- K: 2.1.4 – Intelligence requirements and Priority Intelligence Requirements (PIRs)
- T: 2.1.4.1 – Develop or refine intelligence requirements
- T: 2.1.4.2 – Translate stakeholder questions into clear intelligence requirements
- T: 2.1.4.3 – Explain how a given requirement drives analytic work

---

## 1. Key Concepts

CTI analysts write the **question the work exists to answer**. Without that question, collection becomes everything interesting, and analysis has no “done.” That is the job in this lesson: turn a messy ask into a requirement that names the decision, the evidence you need, and what you will not chase.

**2.1.3** named the kind of answer (strategic, operational, tactical, technical). This lesson is the question itself. You do **not** score whether a product is actionable (**2.1.5**). You do **not** pick OSINT versus commercial sources (**2.1.8**). You do **not** invent a shop PIR list (**2.12.1**).

| Idea | What it is |
|------|------------|
| **Purpose** | Focus collection and analysis on a decision someone can make |
| **PIR** | A *priority* requirement — leadership or the program ranked it |
| **Standing / ad-hoc** | Still requirements. They are not all PIRs. A **standing** requirement stays until leadership takes it off. An **ad-hoc** requirement is one-time, often from a Request for Information (**RFI**) or an incident |
| **Drives collection and analysis** | Names what you collect, what you analyze, and what you will **not** chase |

A clear requirement is a **question**, plus **whose decision**, plus **what you will not chase**. If your shop publishes PIR IDs, use those. Do not invent a PIR list for the classroom firm (**DYA**).

**What good looks like:**

- **Identify or refine:** A slogan is not a requirement. Name the decision, the object, and the window.
- **Translate:** Stakeholder: “Are we seeing them?” The desk is working **A12** — `wscript` launched encoded PowerShell on **WS-JLEE**, and an update domain is in the traffic. Refine: “Is the update domain the payload host for **A12** in this window?” Not a PIR ID you made up.
- **Drives work:** Collect the A record for that domain and the file already on the host. Analyze whether those answer the payload-host question. Do **not** chase the sibling domain on this requirement. That hop is later enrichment (**2.8**), not this question.

---

## 2. Knowledge Check

1. Every intelligence requirement is a PIR. True or false?
2. What does a PIR add that a standing or ad-hoc requirement may not have?
3. “Are we seeing them?” Translate it for **A12**, and name one thing the requirement tells you **not** to chase.

---

## 3. Summary

A requirement is the question the work exists to answer. A PIR is a ranked one. It drives what you collect, what you analyze, and what you skip. Do not invent the shop list.

**Next:** **2.1.5** Ensuring intelligence is actionable.

---

## 4. Related modules

- 2.1.3 – Intelligence types (previous)
- 2.1.5 – Actionable intelligence
- 2.1.8 – Collection source classes
- 2.12.1 – Local PIR list (obtain, do not invent)
