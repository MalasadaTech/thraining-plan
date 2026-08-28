# Module 1.5.1 – Report Types

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C ; 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C ; 1.5.1.2 2b / 3c / 4c  
- CTI: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the three kinds of report: **incident report**, **RFI**, and **other** as your shop uses it.
2. Given a situation, pick the type and say why it is not the **adjacent** type.

**Mapped Proficiency Items:**
- K: 1.5.1.1 – Report types
- T: 1.5.1.2 – Identify the correct report type for a given situation and why it is not the adjacent type

---

## 1. Key Concepts

After you decide an alert is a case, or that you need another desk's help, you pick the **kind of record**. The next desk needs a **case** or a **question**, not both mixed in one product. That is the job in this lesson: name the type first, and say why the next-closest wrong type is wrong. That next-closest wrong type is the **adjacent** type (the **neighbor**).

| Type | What it is | Next-closest wrong type |
|------|------------|-------------------------|
| **Incident report** | Records a security incident (or a strongly supported suspected one) that needs a case / IR handoff | **RFI** — you already have enough to record the case; asking a question is a different product |
| **RFI** (Request for Information) | Asks another desk (CTI, hunt, IT, a vendor) for information so you can continue | **Incident** — an RFI can sit **beside** a case; it is the question, not a second case record |
| **Other (your shop)** | A name your site already uses | Say the local name and which neighbor you rejected. Do not invent a type. Do not park a finished intel paper here (**2.11**) |

The pair that gets mixed up is **incident ↔ RFI**. An RFI can sit beside an incident. It is not a second case. The RFI is the door into CTI.

**What good looks like:** two sentences — the **type**, and **not the neighbor because …**. You do not write the body yet.

- **Incident, not RFI:** First record for **A12** — `WS-JLEE` / `jlee`, `wscript` → `-enc`, Temp `invoice.vbs`. Type **incident report**. Not RFI: you are recording the case for IR, not asking a question. (A later RFI on the domain is a second product.)
- **RFI, not incident:** **A12** already exists. You want CTI to work the update domain / file. Type **RFI**. Not incident: the case is already open; this product is the question.

Do not invent a type list for this course's company. If you need **other**, use a name your real shop already has.

This lesson only names the type. Due clocks are **1.5.2**. Recipients and channel are **1.5.3**.

---

## 2. Knowledge Check

1. An RFI is a second incident case. True or false?
2. What is an incident report for, versus an RFI?
3. **A12** already exists. You want CTI to work the update domain. Type, and why not the adjacent one?

---

## 3. Summary

An incident report records the case. An RFI asks a question — and is the door into CTI. Other is a name your shop already uses. Name the type and reject the neighbor.

**Next:** **1.5.2** Reporting timeline requirements.

---

## 4. Related modules

- 1.4.5 – SLA / response time goals (previous — alert clocks, not report clocks)
- 1.5.2 – Reporting timeline requirements
- 1.5.3 – Notification and distribution
- 2.11 – Intelligence production (not a 1.5 type)
