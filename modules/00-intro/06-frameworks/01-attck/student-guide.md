# Module 1.5.1 – MITRE ATT&CK

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C ; 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
- CTI: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
- DE: 1.5.1.1 A / B / B ; 1.5.1.2 1a / 2b / 2b  
**Estimated Time:** 20 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what ATT&CK is for, and what a tactic vs a technique (or sub-technique) is.
2. Map a one-line activity to a tactic and a technique (or sub-technique) and cite the evidence.

**Mapped Proficiency Items:**
- K: 1.5.1.1 – MITRE ATT&CK
- T: 1.5.1.2 – Map an alert or observed activity to MITRE ATT&CK tactics/techniques

---

## 1. Key Concepts

People on different desks will look at the same host or log. They need one name for **what the adversary was trying to do** and **how**. ATT&CK is that shared language. You use it to label what you saw, not to decorate a ticket.

**Purpose and structure.** ATT&CK is a knowledge base of adversary **behaviors**. The Enterprise matrix puts **tactics** as columns and **techniques** (and **sub-techniques**) as cells.

**Tactic** = *why* — the goal at that step (Execution, Persistence, Command and Control, …).

**Technique** = *how* — a named way to reach that goal (`T1059` Command and Scripting Interpreter).

**Sub-technique** = a more specific how (`T1059.001` PowerShell).

You do not memorize every cell. You must know what the columns and cells are.

**How to map.** Read what the row actually shows. Name the **goal** (tactic). Name the **how** (technique or sub-technique). Cite one field (command line, URI, parent, hive). If two IDs fit, pick the **primary** for this row and say why the neighbor is weaker. An ID with no evidence is a slogan.

**What good looks like (1.5.1.2):** given “`wscript` launched encoded PowerShell,” you write Execution / `T1059.001` PowerShell and cite the encoded command line. You do not write Command and Control because “it might beacon later.”

Hunt planning with ATT&CK is later (**2.5**). Diamond is next (**1.5.2**).

---

## 2. Knowledge Check

1. What is a tactic, and what is a technique?
2. Why is an ATT&CK ID with no cited field not a finished map?
3. Encoded PowerShell ran from a script. Name a tactic and a technique (or sub-technique) and what you would cite.

---

## 3. Summary

ATT&CK labels behavior. Tactic is why. Technique is how. Map the row in front of you and cite the field.

**Next:** **1.5.2** Diamond Model.

---

## 4. Related modules

- 1.5.2 – Diamond Model
- 1.5.3 – Cyber Kill Chain
- 2.5 – Hunt planning with ATT&CK (later)
