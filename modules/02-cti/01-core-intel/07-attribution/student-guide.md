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

CTI analysts name **who or what cluster** sits behind activity — at a type and a confidence — so collection, hunt, and defense aim at the right cluster. That is the job in this lesson: read an attribution statement, say what type it claims, and whether the evidence earns that confidence. This is not a finished actor profile (**2.11.1.2**). Estimative wording depth is **2.2.1**. You do **not** invent a nation-state as fact.

| Idea | Meaning |
|------|---------|
| **Purpose** | Focus collection, hunt, and defense on the right cluster |
| **Challenges** | Shared hosting, false flags, vendor marketing names, one-blog claims |
| **Activity group** | A cluster of activity (infra, malware, ops). You can defend against a cluster without a country |
| **Nation-state** | A government sponsor. Needs more than a vendor label |

**Shared hosting** means more than one customer sat on the same IP or range, so that address is not “theirs.” A **false flag** is planted evidence meant to look like someone else. A vendor marketing name is a **label**, not proof. One blog is one source.

**Classroom confidence (this lesson only — not a live ODNI card):** **Low** means the evidence is thin or single-source. **Medium** means more than one independent line, and alternatives still remain. **High** means several independent lines, and alternatives are weak. If your shop publishes a confidence card, use it. Do not treat these three words as live policy.

A name on a PDF (“PRD APT”) is a **vendor label**, not proof of who they are.

**What good looks like:** someone gives you a claim. You name the type claimed, the confidence claimed, and whether the evidence present earns both.

- Given: “Vendor PDF says PRD APT, so this is a nation-state, high confidence.” **Fail.** Type claimed is nation-state. Evidence is a label. Confidence is too high. Honest read: **activity group / low** until independent evidence supports more.
- Given: incident **A12** — encoded PowerShell, an update domain, and `203.0.113.88`. Those facts can support an **activity cluster**. They do **not** by themselves prove a government.

Do not write the finished actor profile. Do not swap in likelihood words such as likely or almost certainly (**2.2.1**).

---

## 2. Knowledge Check

1. A vendor “APT” name is high-confidence nation-state attribution. True or false?
2. What is the difference between an activity group and a nation-state?
3. “Vendor PDF says PRD APT — high confidence nation-state.” Assess the claim.

---

## 3. Summary

Attribute the cluster you can defend. Name type and confidence. A vendor label is not high-confidence nation-state.

**Next:** **2.1.8** Collection sources and methods.

---

## 4. Related modules

- 2.1.6 – Tailoring to audience (previous)
- 2.1.8 – Collection sources
- 2.2.1 – Estimative language
- 2.11.1.2 – Actor profile (not this lesson)
