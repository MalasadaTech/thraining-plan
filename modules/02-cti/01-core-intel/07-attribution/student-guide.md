# Module 2.1.7 – Attribution

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.7 B / C / C ; 2.1.7.1 3c / 4c / 4d  
- Hunter: 2.1.7 A / B / B ; 2.1.7.1 1a / 2b / 3c  
- SOC: 2.1.7 A / A / A ; 2.1.7.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why we attribute, why it is hard, and the difference between **activity group** and **nation-state**.
2. Assess a statement: claimed **confidence** versus the **evidence** present.

**Mapped Proficiency Items:**
- K: 2.1.7 – Attribution (purpose, confidence, types)
- T: 2.1.7.1 – Assess attribution statements for confidence and supporting evidence

---

## 1. Key Concepts

CTI analysts name **who or what cluster** — at a type and a confidence — so defense aims at the right cluster. This is not a finished actor profile (**2.11.1.2**). Estimative wording depth is **2.2.1**. You do **not** invent a nation-state as fact.

| Idea | Meaning |
|------|---------|
| **Purpose** | Focus collection, hunt, and defense on the right cluster |
| **Challenges** | Shared hosting, false flags, vendor marketing names, one-blog claims |
| **Activity group** | A cluster of activity (infra, malware, ops). You can defend against a cluster without a country |
| **Nation-state** | A government sponsor. Needs more than a vendor label |

**Classroom confidence (this lesson only — not a live ODNI card):** **Low** = thin or single-source. **Medium** = more than one independent line, alternatives remain. **High** = several independent lines; alternatives are weak.

A name on a PDF (“PRD APT”) is a **vendor label**, not proof of who they are.

**What good looks like:**

- **Assess:** “Vendor PDF says PRD APT, so this is a nation-state, high confidence.” **Fail.** Type claimed is nation-state; evidence is a label. Confidence is too high. You may say **activity group / low** until internals support more.
- **A12** internals (encoded PowerShell, update domain, `203.0.113.88`) support an **activity cluster**. They do **not** by themselves prove a government.

---

## 2. Knowledge Check

1. A vendor “APT” name is high-confidence nation-state attribution. True or false?
2. What is the difference between an activity group and a nation-state?
3. “Vendor PDF says PRD APT — high confidence nation-state.” Assess the claim.

---

## 3. Summary

Attribute the cluster you can defend. Name type and confidence. A PDF label is not high nation-state.

**Next:** **2.1.8** Collection sources and methods.

---

## 4. Related modules

- 2.1.6 – Tailoring to audience (previous)
- 2.1.8 – Collection sources
- 2.2.1 – Estimative language
- 2.11.1.2 – Actor profile (not this hour)
