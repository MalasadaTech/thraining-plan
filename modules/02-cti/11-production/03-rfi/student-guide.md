# Module 2.11.3 – Handling RFIs

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.11.3 B / C / C ; 2.11.3.1 3c / 4c / 4d  
- Hunter: 2.11.3 A / A / B ; 2.11.3.1 1a / 1a / 2b  
- SOC: 2.11.3 A / A / A ; 2.11.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what an **RFI** is for, and name how it moves (receive → evaluate → prioritize → respond).
2. Evaluate and prioritize the **A12** RFI, and write a **response** that answers the question.

**Mapped Proficiency Items:**
- K: 2.11.3 – Handling RFIs
- T: 2.11.3.1 – Evaluate, prioritize, and produce a response to an RFI

---

## 1. Key Concepts

CTI analysts **answer the question another desk sent** because that desk needs a fact it does not have. That ask is an **RFI** (Request for Information). SOC already recorded the case. They still need to know whether the update domain is the host that served the payload. That is the job in this lesson: take the question, decide whether you can answer it and whether it goes first, and write the answer. You do not open a second incident. You do not rewrite the SOC ticket.

**2.11.2** sent the finished product. SOC picking incident versus RFI as a ticket type is **1.5.1**. This lesson is the **answer**. The five-element product structure is **2.11.1**. Local queue policy is **2.12** — obtain it; do not invent it. The classroom queue in this lesson is **lesson-only**, not live org policy.

| Idea | What it is |
|------|------------|
| **Purpose** | Someone needs information they do not have. The RFI *is* the question |
| **Lifecycle** | **Receive** the question. **Evaluate.** **Prioritize.** **Respond.** Then you are done with this ask |
| **Evaluate** | Can we answer it with what we have? What is missing? Is the question bounded? |
| **Prioritize** | Does it support an open incident, or does it sit behind **standing work** (work not tied to a live case, such as a blog read)? |
| **Respond** | Answer the question. Do not rewrite the SOC ticket. Do not open a second case |

If you cannot answer, say what is missing. Do not invent a second question.

**A12** is the classroom incident on workstation **WS-JLEE**. The RFI seed is the update domain / `203.0.113.88`.

**What good looks like:**

- **Evaluate:** The question is “Is the update domain / `203.0.113.88` the **payload host** — the host that served the file — for **A12**?” You have the **Zeek A record** (the name-to-IP the network sensor logged) and the host file (this host logged the talk). The question is bounded. **You can answer.**
- **Prioritize:** An incident is open, and incident response (**IR**) already has the host. **Work now.** Do not put it behind a blog read.
- **Respond:** “**Likely** yes — the update domain / `203.0.113.88` is the payload host for **A12**. Treat it as such.” Not a nation-state paragraph. Not a new incident.

---

## 2. Knowledge Check

1. Answering an RFI means opening a second incident. True or false?
2. What three steps do you take on an RFI?
3. Write a two-sentence **A12** RFI response (no country, no second case).

---

## 3. Summary

The RFI is the question. Receive it, evaluate it, prioritize it, and answer it. Do not rewrite the SOC ticket. Do not open a second case.

**Next:** **2.12.1** Local priorities (obtain, do not invent).

---

## 4. Related modules

- 2.11.2 – Disseminating intelligence to the correct audiences (previous)
- 2.11.1 – Creating finished intelligence products
- 1.5.1 – Report types (SOC type pick)
- 2.12 – Site-specific CTI knowledge (local queue)
- 2.1.4 – Intelligence requirements
