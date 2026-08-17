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

1. Name the syllabus types: **incident report**, **RFI**, and **other** as your shop uses it.
2. Pick the type for a situation and **justify why it is not the adjacent type**.

**Mapped Proficiency Items:**
- K: 1.5.1.1 – Report types
- T: 1.5.1.2 – Identify the correct report type for a given situation and why it is not the adjacent type

---

## 1. Key Concepts

SOC analysts pick the **kind of record** so the next desk gets a **case** or a **question**, not both mixed in one product. You pick one type and say why the **neighbor** is wrong. You do **not** write the body. You do **not** assign a due clock (**1.5.2**). You do **not** route it (**1.5.3**). You do **not** write a finished intel product (**3.11**).

| Type | Use when | Adjacent — not this |
|------|----------|---------------------|
| **Incident report** | You are recording a security incident (or a strongly supported suspected one) that needs a case / IR handoff | **RFI** — you already have enough to record the case; asking a question is a different product |
| **RFI** (Request for Information) | You need information from another desk (CTI, hunt, IT, a vendor) to continue | **Incident** — an RFI can sit **beside** a case; it is the question, not a second case record |
| **Other (your shop)** | A name your site already uses | Say the local name and which neighbor you rejected. Do not invent a type. Do not park a finished intel paper here (**3.11**) |

The adjacent pair is **incident ↔ RFI**. The RFI is the door into CTI. The task is two sentences: **type** and **not the neighbor because …**.

**What good looks like:**

- **Incident, not RFI:** First record for **A12** — `WS-JLEE` / `jlee`, `wscript` → `-enc`, Temp `invoice.vbs`. Type **incident report**. Not RFI: you are recording the case for IR, not asking a question. (A later RFI on the domain is a second product.)
- **RFI, not incident:** **A12** already exists. You want CTI to work the update domain / file. Type **RFI**. Not incident: the case is already open; this product is the question.

Do not invent a DYA type list. If you need **other**, use a name your real shop already has.

---

## 2. Knowledge Check

1. This hour is who gets the report and which channel. True or false?
2. What is an incident report for, versus an RFI?
3. **A12** already exists. You want CTI to work the update domain. Type, and why not the adjacent one?

---

## 3. Summary

Incident = case record. RFI = question (and the door into CTI). Other is a name your shop already uses. Reject the neighbor.

**Next:** **1.5.2** Reporting timeline requirements.

---

## 4. Related modules

- 1.4.5 – SLA / response time goals (previous — alert clocks, not report clocks)
- 1.5.2 – Reporting timeline requirements
- 1.5.3 – Notification and distribution
- 3.11 – Intelligence production (not a 1.5 type)
