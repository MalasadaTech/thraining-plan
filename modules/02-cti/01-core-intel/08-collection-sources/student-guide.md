# Module 2.1.8 – Collection sources and methods

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.8 B / C / C ; 2.1.8.1 3c / 4c / 4c ; 2.1.8.2 3c / 4c / 4d  
- Hunter: 2.1.8 A / B / B ; 2.1.8.1 1a / 1a / 2b ; 2.1.8.2 1a / 1a / 2b  
- SOC: 2.1.8 A / A / B ; 2.1.8.1 1a / 1a / 1a ; 2.1.8.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the three **source classes**: OSINT, commercial, and internal.
2. Pick the class(es) for a requirement and **plan** collection: order, first action, and what you will not collect.

**Mapped Proficiency Items:**
- K: 2.1.8 – Collection sources and methods (OSINT, commercial, internal)
- T: 2.1.8.1 – Identify appropriate collection source classes for a given requirement
- T: 2.1.8.2 – Plan collection against an intelligence requirement

---

## 1. Key Concepts

CTI analysts choose **where** to collect so they can answer a requirement without skipping the logs they already have, and without treating every public blog as the first stop. A requirement names a question. This lesson names the three **source classes** — kinds of places you collect from — and what a short collection **plan** looks like.

**2.1.2** named collection as a **stage**: the lifecycle job of gathering. This lesson is **where** you gather from. You do not operate VirusTotal or a threat intelligence platform (**0.7** / **2.3** / **2.9**). You do not file the local request ticket (**2.12.2.1**). You do not rewrite the requirement (**2.1.4**).

| Class | What it is | Good for | Not enough when |
|-------|------------|----------|-----------------|
| **OSINT** (open-source intelligence) | Public reporting, public DNS, open blogs | The public story | The question is *our* presence / *our* logs |
| **Commercial** | Paid threat intelligence platform (TIP), premium sandbox, vendor intel | Packaged enrichment | You have not checked internals the question asked for |
| **Internal** | SIEM, EDR, Zeek, tickets, internal TIP, hunt output | “Are *we* seeing this?” | The question is only the public story |

Classes **stack**. You may use more than one. The **order** follows the requirement, not habit. The **method** in this lesson is that short plan: **source class**, **first action**, and **what you will not collect**.

**What good looks like:** someone gives you a requirement. You name the class(es) and write the short plan. You do not open a tool or file a ticket yet.

- Given: the classroom **A12** question — “Is this the payload host *here*?” First class: **internal**. First action: look in telemetry you already have (the Zeek A record, or the file from the host). Then OSINT or commercial if you still need the public story. Do not start with a public blog and skip internals.
- What you will **not** collect on this plan: a paid vendor account you do not have; a sibling domain the requirement did not ask for.

---

## 2. Knowledge Check

1. Collection as a lifecycle stage and a source class are the same thing. True or false?
2. Name the three source classes.
3. A requirement asks: is this the payload host *here*? Name the first class, the first action, and one thing you will not collect.

---

## 3. Summary

OSINT, commercial, and internal. Order follows the question. Internals first when the question is “are *we* seeing this?” A plan names the class, the first action, and what you will not collect.

**Next:** **2.2.1** Estimative language.

---

## 4. Related modules

- 2.1.7 – Attribution (previous)
- 2.2.1 – Estimative language
- 2.1.2 – Lifecycle collection stage
- 2.1.4 – Intelligence requirements
- 2.12.2.1 – Local collection request
- 0.7 / 2.3 / 2.9 – Tool survey / TIP / platform depth
