# Module 0.6.3 – Cyber Kill Chain

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.3.1 A / B / C ; 0.6.3.2 2b / 3c / 4c  
- Hunter: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- CTI: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- DE: 0.6.3.1 A / B / B ; 0.6.3.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the seven Kill Chain stages and say what the chain is for.
2. Place a one-line activity on one stage and say why it is not the previous or next stage.

**Mapped Proficiency Items:**
- K: 0.6.3.1 – Cyber Kill Chain
- T: 0.6.3.2 – Identify the Kill Chain stage of observed activity

---

## 1. Key Concepts

You often see **one step** of an attack: a file in email, a program that ran, a callback. Before you treat that step as the whole intrusion, you have to name **where it sits in the sequence**. That is the job in this lesson: place the activity you have on one stage, and refuse the previous or next stage you did not see.

The Lockheed Martin **Cyber Kill Chain** shows attack **progression** as a short sequence of stages. It is a staging tool, not a complete model of every intrusion.

You have one activity — one log or one-line description. In a SIEM that often shows up as a **row**. Later lessons may still say “row.” Here it means the activity in front of you.

| Stage | What this stage is |
|-------|--------------------|
| **Reconnaissance** | Researching the target |
| **Weaponization** | Building a deliverable payload |
| **Delivery** | The weapon arrives (email, web, USB) |
| **Exploitation** | It runs against a vulnerability, or as the exploit |
| **Installation** | Code or an implant is on the host |
| **Command and Control** | A callback or control channel |
| **Actions on Objectives** | The goal (theft, encryption, and so on) |

Place **this activity** on **one** stage. Say why it is not the **previous** or **next** stage. Do not invent stages you did not see.

**What good looks like:** someone gives you one line. You name the stage. You reject the neighbor you did not see. You do not fill the rest of the chain.

- Given: “A user received a `.vbs` in email.” **Delivery.** It is not **Weaponization** (you did not see them build it). It is not **Exploitation** (you did not see it run). Do not skip to Command and Control without a callback.

This lesson is **not** ATT&CK (**0.6.1**). It is **not** Diamond (**0.6.2**). Listing every supported stage on an intelligence product is later (**2.7.3**).

---

## 2. Knowledge Check

1. What is the Cyber Kill Chain for?
2. Name the seven stages in order.
3. A user received a `.vbs` in email. Why is that Delivery, and why is it not Exploitation?

---

## 3. Summary

Seven stages. Place the activity you have. Reject the previous or next stage you did not see. Do not invent the rest of the chain.

**Next:** **0.7** External tools (tool survey).

---

## 4. Related modules

- 0.6.1 – MITRE ATT&CK
- 0.6.2 – Diamond Model
- 0.7 – External tools
- 2.7.3 – Cyber Kill Chain in intelligence analysis (later)
