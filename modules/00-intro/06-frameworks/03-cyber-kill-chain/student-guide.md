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

1. Name the Kill Chain stages and what the chain is for.
2. Place a one-line activity on a stage and say why it is not the previous or next stage.

**Mapped Proficiency Items:**
- K: 0.6.3.1 – Cyber Kill Chain  
  SOC A / B / C · Hunter B / C / C · CTI B / C / C · DE A / B / B
- T: 0.6.3.2 – Identify the Kill Chain stage of observed activity  
  SOC 2b / 3c / 4c · Hunter 3c / 4c / 4c · CTI 3c / 4c / 4c · DE 1a / 2b / 2b

---

## 1. Key Concepts

ATT&CK named the behavior. Diamond named the empty corner. Kill Chain asks **where in time** this step sits. You use it so you do not call a first payload “the whole intrusion.”

**Purpose.** Show attack **progression** as a short sequence of stages. It is a staging tool, not a complete model of every intrusion.

**The stages** (Lockheed Martin Cyber Kill Chain):

1. Reconnaissance  
2. Weaponization  
3. Delivery  
4. Exploitation  
5. Installation  
6. Command and Control  
7. Actions on Objectives  

**How you use it.** Place **this row** on one stage. Say why it is not the **previous** or **next** stage. Do not skip ahead to a stage you did not see.

**What good looks like (0.6.3.2):** a user received a `.vbs` in email. That is **Delivery**. It is not Weaponization (you did not see them build it). It is not Exploitation (you did not see it run). Do not skip to Command and Control without a callback.

Tool survey is next (**0.7**).

---

## 2. Knowledge Check

1. What is the Kill Chain for?
2. Name the seven stages in order.
3. A user received a `.vbs` in email. Why is that Delivery, and why is it not Exploitation?

---

## 3. Summary

Seven stages. Place the row you have. Reject the neighbor. Do not invent the rest of the chain.

**Next:** **0.7** External tools (tool survey).

---

## 4. Related modules

- 0.6.1 – MITRE ATT&CK
- 0.6.2 – Diamond Model
- 0.7 – External tools
