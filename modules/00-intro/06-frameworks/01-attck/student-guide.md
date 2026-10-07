# Module 0.6.1 – MITRE ATT&CK

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.1.1 A / B / C ; 0.6.1.2 2b / 3c / 4c  
- Hunter: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- CTI: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- DE: 0.6.1.1 A / B / B ; 0.6.1.2 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose and structure of ATT&CK.
2. Distinguish a tactic, technique, and sub-technique.
3. Map one observed behavior, cite the supporting evidence, and choose the better-supported mapping when two nearby ATT&CK labels appear plausible.

**Mapped Proficiency Items:**
- K: 0.6.1.1 – MITRE ATT&CK
- T: 0.6.1.2 – Map observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence

## Why This Matters

ATT&CK gives analysts a shared vocabulary for describing adversary behavior. A useful mapping connects that vocabulary to evidence, so another analyst can understand why the label fits. This lesson introduces the matrix and shows how to support one mapping from an observed event.

## 1. Reading the matrix

The [Enterprise ATT&CK matrix](https://attack.mitre.org/matrices/enterprise/) organizes behavior by tactics, techniques, and sub-techniques.

| Element | Meaning | Example |
|---|---|---|
| Tactic | The goal the behavior serves. | Execution |
| Technique | A way to achieve a goal. | T1059 — Command and Scripting Interpreter |
| Sub-technique | A more specific form of a technique. | T1059.001 — PowerShell |

Tactics appear as columns. Techniques and their sub-techniques describe behaviors within that structure. The matrix helps you find a relevant description; the description and your evidence determine whether a mapping is supported.

## 2. Building an evidence-supported mapping

Suppose a process event records `wscript.exe` starting `powershell.exe`, and the command-line field contains an encoded PowerShell command. The event supports **Execution / T1059.001 — PowerShell** because it shows the PowerShell interpreter being invoked to run commands. The parent process and command line provide the evidence to cite.

A short mapping could read: “Execution / T1059.001 — PowerShell; the process event shows `wscript.exe` launching `powershell.exe` with an encoded command.” Include the event reference or relevant fields in the actual record so the reader can check your reasoning.

The broader T1059 label describes the interpreter family. When the evidence identifies PowerShell, the sub-technique gives a more precise description.


## 3. Choosing between plausible mappings

Sometimes two ATT&CK labels can both seem reasonable at first glance. The useful question is not simply whether a label can be made to fit; it is which mapping best describes the observed behavior at the level of specificity the evidence supports.

Suppose a registry event shows `reg.exe` creating value `Updater` under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and pointing it to `%TEMP%\update.exe`. Two labels may come to mind:

- **T1112 – Modify Registry** describes registry modification broadly.
- **T1547.001 – Registry Run Keys / Startup Folder** specifically describes use of a Run key for boot or logon autostart execution.

If you must choose the primary mapping for this event, **T1547.001** is better supported because the observed registry location is itself a Run key and the event records a value being configured there. T1112 describes the generic mechanism, but it is less specific to what this event shows.

If the event only showed an unspecified registry value being changed, without evidence that the key was a Run/Startup persistence location, **T1112** would be the safer mapping. The evidence determines how specific the mapping can be.

## 4. Keeping the conclusion within the evidence

This event alone does not establish Command and Control: it contains no evidence of communication with an external controller. That behavior might appear in another event and support an additional mapping. More than one mapping can be appropriate when each has evidence.

An ATT&CK label also does not establish that an event is malicious. Administrators use PowerShell for legitimate tasks. The mapping describes behavior; assessing its significance requires context such as the command, user, parent process, and surrounding activity.

## Knowledge Check

1. How do a tactic, technique, and sub-technique differ?
2. A process event shows `wscript.exe` launching `powershell.exe` with an encoded command. Give a supported mapping, identify the evidence, and explain whether the same event establishes Command and Control or malicious intent.
3. A registry event shows `reg.exe` creating a value under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`. Between T1112 and T1547.001, which should be the primary mapping, and why? When would T1112 be the safer choice?

## Summary

ATT&CK provides names for behavior. A useful mapping identifies the tactic and technique or sub-technique, cites the supporting evidence, and explains why the label fits. When two labels look plausible, choose the one whose specificity is best supported by the observed behavior, and keep additional conclusions tied to additional evidence.

## Course Connections

Previous: [0.5 – Where the jobs lightly overlap](../../05-where-jobs-overlap/student-guide.md)

Next: [0.6.2 – Diamond Model](../02-diamond-model/student-guide.md)

## References and Further Reading

- [MITRE ATT&CK — Enterprise matrix](https://attack.mitre.org/matrices/enterprise/) — Explore the matrix structure.
- [MITRE ATT&CK — PowerShell (T1059.001)](https://attack.mitre.org/techniques/T1059/001/) — Read the behavior description used in the example.
- [MITRE ATT&CK — Modify Registry (T1112)](https://attack.mitre.org/techniques/T1112/) — Compare the broader registry-modification behavior.
- [MITRE ATT&CK — Registry Run Keys / Startup Folder (T1547.001)](https://attack.mitre.org/techniques/T1547/001/) — Compare the more specific Run-key persistence behavior.
