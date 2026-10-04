# Module 2.3.1 – MITRE ATT&CK for CTI Analysis and Reporting

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.3.1 B / C / C ; 2.3.1.1 3c / 4c / 4c  
- Hunter: 2.3.1 B / C / C ; 2.3.1.1 3c / 4c / 4c  
- SOC: 2.3.1 A / B / B ; 2.3.1.1 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Map behavior from a report or activity set to an ATT&CK tactic and the most specific technique or sub-technique supported by the evidence.
2. Explain the evidence for the mapping and distinguish it from a nearby ATT&CK choice that would require evidence the product does not contain.

**Mapped Proficiency Items:**
- K: 2.3.1 – MITRE ATT&CK for CTI analysis and reporting
- T: 2.3.1.1 – Map activity or reports to MITRE ATT&CK

## 1. Key Concepts

MITRE ATT&CK gives analysts a shared vocabulary for describing adversary behavior. In a CTI product, the value of an ATT&CK mapping is not the ID by itself. The value comes from showing **which observed or reported behavior supports the mapping**.

A useful mapping starts with the evidence and moves to ATT&CK—not the other way around.

| ATT&CK element | Question it answers |
|---|---|
| **Tactic** | Why is the adversary performing this behavior at this point? |
| **Technique** | What general method is being used? |
| **Sub-technique** | What more specific implementation of the technique is supported? |
| **Procedure / evidence** | What concrete command, event, report sentence, or observation shows the behavior in this case? |

The [MITRE ATT&CK Enterprise knowledge base](https://attack.mitre.org/) is the authoritative reference for current tactic, technique, and sub-technique definitions.

### Map the behavior you actually have

Consider:

`wscript.exe` → `powershell.exe -enc ...`

The observable behavior is PowerShell execution. ATT&CK defines **T1059.001 – PowerShell** under the **Execution** tactic.

A strong CTI mapping is:

> **Execution / T1059.001 PowerShell** — supported by `powershell.exe -enc` launched by `wscript.exe`.

Reference: [MITRE ATT&CK – T1059.001 PowerShell](https://attack.mitre.org/techniques/T1059/001/)

The mapping does not need to guess what the PowerShell process might do later. If there is no callback in the evidence, there is no reason to add a Command and Control behavior merely because PowerShell *can* be used for C2.

### Use the most specific supported technique

If the evidence clearly identifies PowerShell, use **T1059.001** rather than stopping at the broader parent **T1059 Command and Scripting Interpreter**.

That does not mean “always choose the longest ID.” It means choose the most specific technique the evidence supports.

If a report only says “a command interpreter was used” and does not identify which one, the parent technique may be the defensible mapping.

### Map separate behaviors separately

One activity set can contain several behaviors.

Suppose the evidence shows:

1. `powershell.exe -enc ...`
2. the host successfully downloaded `/update.exe` from an external system.

The first behavior supports **T1059.001 PowerShell**.

The second can support **T1105 – Ingress Tool Transfer** when the evidence establishes that a tool or file was transferred from an external system into the compromised environment.

Reference: [MITRE ATT&CK – T1105 Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)

An HTTP request name alone is weaker evidence than a confirmed transfer. If all you know is that a request for `/update.exe` occurred, say exactly that. A response, file creation, or other transfer evidence makes the T1105 mapping stronger.

### A nearby technique may look plausible for the wrong reason

The best way to resolve close choices is to compare the ATT&CK definition with the behavior in the product.

For example:

- `powershell.exe -enc` → **T1059.001**
- confirmed external file transfer → **T1105**
- HTTP alone does not make something a command interpreter
- PowerShell alone does not make something Command and Control

The question is always: **what behavior does this evidence demonstrate?**

### Cite the evidence with the mapping

A reusable CTI mapping should preserve enough evidence that another analyst can review the decision.

A simple format is:

`Tactic | ATT&CK ID | Technique | Evidence`

Example:

`Execution | T1059.001 | PowerShell | powershell.exe -enc launched by wscript.exe`

This makes the ATT&CK line useful to threat hunting, detection engineering, and future analysis because the ID remains tied to the observation that produced it.

## 2. Knowledge Check

1. `wscript.exe` launches `powershell.exe -enc`. What tactic and ATT&CK sub-technique are supported, and what evidence would you cite?
2. A report says only that the host requested `/update.exe`. What additional evidence would make **T1105 Ingress Tool Transfer** a stronger mapping?
3. Why is “choose the most specific supported technique” better guidance than either always using the parent technique or always choosing the most detailed ID available?

## 3. Summary

ATT&CK mapping is evidence-bound behavior classification.

Start with the report or activity, identify the behavior, use the most specific ATT&CK technique or sub-technique the evidence supports, and preserve the evidence beside the ID. A nearby technique belongs in the product only when its own behavioral definition is actually demonstrated.


## 4. Related Modules

- 2.5.4 – Advanced DNS
- 2.3.2 – Diamond Model for CTI
- 0.6.1 – ATT&CK shared-floor introduction
- 3.5 – Hunt planning with ATT&CK
- 2.6.1 – TTP applicability to the environment

## Supporting References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [T1059.001 – PowerShell](https://attack.mitre.org/techniques/T1059/001/)
- [T1105 – Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)

**Next:** [2.3.2 – Diamond Model Application in CTI](../02-diamond-cti/student-guide.md).
