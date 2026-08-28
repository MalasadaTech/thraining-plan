# Module 0.6.1 – MITRE ATT&CK

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.1.1 A / B / C ; 0.6.1.2 2b / 3c / 4c  
- Hunter: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- CTI: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- DE: 0.6.1.1 A / B / B ; 0.6.1.2 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what ATT&CK is for, and tell a **tactic** from a **technique** (or **sub-technique**).
2. Given one line of activity, name a tactic and a technique (or sub-technique) and cite the evidence.

**Mapped Proficiency Items:**
- K: 0.6.1.1 – MITRE ATT&CK
- T: 0.6.1.2 – Map observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence

---

## 1. Key Concepts

People on different desks will look at the same host or log. They need one name for **what the adversary was trying to do** and **how**. ATT&CK is that shared language. That is the job in this lesson: label the behavior you saw, so those desks are not using four different names for the same thing.

ATT&CK is a knowledge base of adversary **behavior**. You use it to name what you saw. You do not use it to decorate a ticket.

The **Enterprise** matrix puts **tactics** as columns and **techniques** (and **sub-techniques**) as cells. You do not memorize every cell. You must know what the columns and cells are.

| Piece | What it is |
|-------|------------|
| **Tactic** | *Why* — the goal at that step (Execution, Persistence, Command and Control) |
| **Technique** | *How* — a named way (`T1059` Command and Scripting Interpreter) |
| **Sub-technique** | A more specific how (`T1059.001` PowerShell) |

A finished **map** is that label: tactic + technique or sub-technique + **one cited field**. Read the line of activity in front of you (later lessons may still say **row**; here it means that one log or event). Name the goal. Name the how. Cite one field that actually shows it, such as the command line. If two IDs fit, pick the **primary** for this line and reject the neighbor. An ID with no cited field is not a map.

**What good looks like:** someone gives you one line. You name the tactic and the technique or sub-technique. You cite the field. You do not tell the rest of the incident.

- Given: “`wscript` launched encoded PowerShell.” **Label:** Execution / `T1059.001` PowerShell. **Cite:** the encoded command line. **Not:** Command and Control — this line does not show a beacon.

This is one line of activity, not an alert queue (**1.4**). Hunt planning with ATT&CK is later (**3.5**). Putting IDs on a CTI product is later (**2.7.1**). Diamond is next (**0.6.2**).

---

## 2. Knowledge Check

1. What is a tactic, and what is a technique?
2. An ATT&CK ID with no cited field is a finished map. True or false?
3. Encoded PowerShell ran from a script. Name a tactic and a technique (or sub-technique) and what you would cite.

---

## 3. Summary

ATT&CK labels behavior. A tactic is why. A technique is how. Name both for the line in front of you and cite the field.

**Next:** **0.6.2** Diamond Model.

---

## 4. Related modules

- 0.5 – Where the jobs lightly overlap
- 0.6.2 – Diamond Model
- 0.6.3 – Cyber Kill Chain
- 2.7.1 – ATT&CK for CTI (later)
- 3.5 – Hunt planning with ATT&CK (later)
