# Module 1.5.3 – Cyber Kill Chain

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C ; 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 B / C / C ; 1.5.3.2 3c / 4c / 4c  
- CTI: 1.5.3.1 B / C / C ; 1.5.3.2 3c / 4c / 4c  
- DE: 1.5.3.1 A / B / B ; 1.5.3.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the Kill Chain stages and what the chain is for.
2. Place a one-line activity on a stage and say why it is not the previous or next stage.

**Mapped Proficiency Items:**
- K: 1.5.3.1 – Cyber Kill Chain
- T: 1.5.3.2 – Identify the Kill Chain stage of observed activity

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

**What good looks like (1.5.3.2):** a user got a `.vbs` in email and `wscript` ran it. That is **Delivery** (and you may also have Exploitation if the script ran). It is not Command and Control unless you have the callback. Encoded PowerShell on the host is **Installation** / later Execution on the host — not Reconnaissance.

Tool survey is next (**3.3.2**).

---

## 2. Knowledge Check

1. What is the Kill Chain for?
2. Name the seven stages in order.
3. A user received a `.vbs` in email and it ran. Why is that not Command and Control?

---

## 3. Summary

Seven stages. Place the row you have. Reject the neighbor. Do not invent the rest of the chain.

**Next:** **3.3.2** External tools (tool survey).

---

## 4. Related modules

- 1.5.1 – MITRE ATT&CK
- 1.5.2 – Diamond Model
- 3.3.2 – External tools
