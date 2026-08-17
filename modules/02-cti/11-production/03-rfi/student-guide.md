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

1. Say what an RFI is for, and how it moves (receive → evaluate → answer).
2. Evaluate / prioritize the **A12** RFI and write a **response** that answers the question.

**Mapped Proficiency Items:**
- K: 2.11.3 – Handling RFIs
- T: 2.11.3.1 – Evaluate, prioritize, and produce a response to an RFI

---

## 1. Key Concepts

CTI analysts **answer the question SOC sent**. The RFI *type* is **1.5.1**. The product is this hour. You do **not** rewrite the SOC ticket. You do **not** invent a second question. Local queue policy is **2.12** — obtain, do not invent.

| Step | Job |
|------|-----|
| **Purpose** | Someone needs information they do not have. The RFI *is* the question |
| **Evaluate** | Can we answer it with what we have? What is missing? |
| **Prioritize** | Does it support an open incident (**A12**) or sit behind standing work? |
| **Respond** | Answer the question. Do not rewrite the notify |

**What good looks like:**

- **Evaluate:** A12 RFI = “is this the payload host?” We have Zeek A + file. **Can answer.**
- **Prioritize:** Open incident + IR has the host → **work now**, not behind a blog read.
- **Respond:** “**Likely** yes — update domain / `203.0.113.88` is the payload host for A12. Treat it as such.” Not a nation-state paragraph. Not a new incident.

---

## 2. Knowledge Check

1. Answering an RFI means opening a second incident. True or false?
2. What three steps do you take on an RFI?
3. Write a two-sentence **A12** RFI response (no country, no second case).

---

## 3. Summary

The RFI is the question. Evaluate, prioritize, answer. Do not rewrite the SOC ticket.

**Next:** **2.12.1** Local priorities (obtain, do not invent).

---

## 4. Related modules

- 2.11.2 – Dissemination (previous)
- 1.5.1 – RFI as a SOC type
- 2.12 – Local queue / process
- 2.1.4 – Requirements
