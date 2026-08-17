# Module 2.1.3 – Intelligence Types

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.3 B / C / C ; 2.1.3.1 3c / 4c / 4c  
- Hunter: 2.1.3 A / B / B ; 2.1.3.1 1a / 2b / 3c  
- SOC: 2.1.3 A / A / A ; 2.1.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the four types: **strategic**, **operational**, **tactical**, **technical**.
2. Classify a product or requirement by type, and say why it is not the neighbor.

**Mapped Proficiency Items:**
- K: 2.1.3 – Intelligence types (strategic, operational, tactical, technical)
- T: 2.1.3.1 – Classify an intelligence product or requirement by type

---

## 1. Key Concepts

CTI analysts pick the **kind of answer** so the consumer gets the decision they can make. Type follows the **question**, not the file length. You already know the layer (**2.1.1**) and the stage (**2.1.2**). This hour is **type**. You do **not** write a PIR (**2.1.4**). You do **not** rewrite for audience format (**2.1.6**). You do **not** write the actor profile (**2.11**).

| Type | Question it answers | Neighbor — not this |
|------|---------------------|---------------------|
| **Strategic** | What should leadership change about risk or posture (months to years)? | **Operational** — a campaign run over days is not a program decision |
| **Operational** | How do we run this incident or hunt over days to weeks? | **Tactical** — “what do I do on this host *now*” is not the campaign picture |
| **Tactical** | What should a responder do **now** on this activity? | **Technical** — the observable is not the action |
| **Technical** | What are the observables we can detect or pivot on? | **Tactical** — a hash is not “isolate the host” |

A long PDF is not automatically strategic. A hash is not automatically intelligence. Type applies to **intelligence** (or the requirement that asks for it). A raw IOC list is still **data**.

Stage ≠ type. You can collect technical data in service of a tactical question.

**What good looks like:**

- **Technical, not tactical:** the A record `203.0.113.88` and `GET /update.exe :8080` for the update domain. Observables. Not “isolate **WS-JLEE**.”
- **Tactical, not technical:** “Treat the update domain as the payload host for **A12**; IR has the host.” Action now. Not a hash dump.
- **Strategic** would be a posture line for leadership (no hash). **Operational** would be how the desk runs **A12** over the next days. Do not invent extra victims to fill those rows.

---

## 2. Knowledge Check

1. A long PDF is strategic because it is long. True or false?
2. Name the four types.
3. “Isolate **WS-JLEE**; treat the update domain as the **A12** payload host.” Type, and why not the neighbor?

---

## 3. Summary

Type follows the question. Strategic / operational / tactical / technical. Reject the neighbor.

**Next:** **2.1.4** Intelligence requirements.

---

## 4. Related modules

- 2.1.2 – Intelligence lifecycle (previous)
- 2.1.4 – Intelligence requirements
- 2.1.6 – Tailoring to audience (format, not type)
- 2.11 – Finished products
