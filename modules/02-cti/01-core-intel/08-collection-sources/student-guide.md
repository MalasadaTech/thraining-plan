# Module 2.1.8 – Collection Sources and Methods

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.8 B / C / C ; 2.1.8.1 3c / 4c / 4c ; 2.1.8.2 3c / 4c / 4d  
- Hunter: 2.1.8 A / B / B ; 2.1.8.1 1a / 1a / 2b ; 2.1.8.2 1a / 1a / 2b  
- SOC: 2.1.8 A / A / B ; 2.1.8.1 1a / 1a / 1a ; 2.1.8.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the three **source classes**: OSINT, commercial, internal.
2. Pick the class(es) for a requirement and **plan** collection (order, first action, what you will not collect).

**Mapped Proficiency Items:**
- K: 2.1.8 – Collection sources and methods (OSINT, commercial, internal)
- T: 2.1.8.1 – Identify appropriate collection source classes for a given requirement
- T: 2.1.8.2 – Plan collection against an intelligence requirement

---

## 1. Key Concepts

**2.1.2** named collection as a **stage**. This hour is **where** you collect from. You do **not** click VirusTotal depth (**0.7** / **2.9**). You do **not** file the local request ticket (**2.12.2.1**). You do **not** rewrite the requirement (**2.1.4**).

| Class | What it is | Good for | Not enough when |
|-------|------------|----------|-----------------|
| **OSINT** | Public reporting, public DNS, open blogs | The public story | The question is *our* presence / *our* logs |
| **Commercial** | Paid TIP, premium sandbox, vendor intel | Packaged enrichment | You have not checked internals the question asked for |
| **Internal** | SIEM, EDR, Zeek, tickets, internal TIP, hunt output | “Are *we* seeing this?” | The question is only the public story |

Classes **stack**. Order follows the **requirement**, not habit. A plan is: **class + first action + what you will not collect**.

**What good looks like:**

- **A12** RFI (“is this the payload host *here*?”): first class **internal** — Zeek A record / host file you already have. Then OSINT or commercial if you still need the public story. Do **not** start with a blog and skip internals.
- What you will **not** collect on this plan: a live vendor account you do not have; a sibling domain the requirement did not ask for.

---

## 2. Knowledge Check

1. Collection *stage* (**2.1.2**) and source *class* are the same thing. True or false?
2. Name the three source classes.
3. **A12** RFI: is this the payload host *here*? First class, first action, one thing you will not collect.

---

## 3. Summary

OSINT, commercial, internal. Order follows the question. Internals first when the question is “are *we* seeing this?”

**Next:** **2.2.1** Estimative language.

---

## 4. Related modules

- 2.1.7 – Attribution (previous)
- 2.2.1 – Estimative language
- 2.1.2 – Lifecycle collection *stage*
- 2.12.2.1 – Local collection *request* (not this hour)
- 0.7 / 2.9 – Tool survey / platform depth
