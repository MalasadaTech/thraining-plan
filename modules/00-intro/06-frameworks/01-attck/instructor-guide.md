# Instructor Guide – Module 0.6.1 – MITRE ATT&CK

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.1.1 A / B / C ; 0.6.1.2 2b / 3c / 4c  
- Hunter: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- CTI: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- DE: 0.6.1.1 A / B / B ; 0.6.1.2 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

ATT&CK gives analysts a shared vocabulary for describing adversary behavior. A useful mapping connects that vocabulary to evidence, so another analyst can understand why the label fits. This lesson introduces the matrix and shows how to support one mapping from an observed event.

Teach this as a shared introductory lesson using the supplied examples and discussion. Match the depth to the proficiency levels above. The focus is the mapped knowledge and task; operational procedures are developed in the later role tracks.

## Learning Objectives

1. Explain the purpose and structure of ATT&CK.
2. Distinguish a tactic, technique, and sub-technique.
3. Map one observed behavior and cite the evidence supporting the mapping.

**Mapped Proficiency Items:**
- K: 0.6.1.1 – MITRE ATT&CK
- T: 0.6.1.2 – Map observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence

## Preparation

Read the [student guide](student-guide.md) and use [slides.md](slides.md) to support the explanation. Review the answer key before teaching so the discussion and feedback reinforce the same concepts. This lesson uses discussion and worked examples; no lab is required.

## Suggested Timing

| Section | Time | Teaching purpose |
|---|---|---|
| Opening and purpose | 2 min | Connect this lesson to the previous topic. |
| Explanation and worked examples | 10 min | Use the three teaching sections below. |
| Knowledge check and feedback | 4 min | Ask for reasoning as well as an answer. |
| Summary and transition | 2 min | Consolidate the lesson and introduce the next topic. |
| **Total** | **18 min** | |

## Detailed Teaching Notes

### 1. Reading the matrix

Open the Enterprise matrix and locate Execution and PowerShell. Ask learners to explain the relationship in their own words. They need to navigate and interpret the structure rather than memorize its contents.

**Student-facing emphasis:** Tactic: the goal. Technique: how the goal is pursued. Sub-technique: a more specific behavior. Example: Execution → T1059 → T1059.001 PowerShell.

### 2. Building an evidence-supported mapping

Walk from the recorded process fields to the behavior, then to the label. Explain why the sub-technique is more precise than T1059 here. The encoded content need not be decoded to recognize the interpreter, although further investigation may be needed to understand what it did.

**Student-facing emphasis:** Observed: wscript.exe launches powershell.exe with an encoded command. Mapping: Execution / T1059.001 — PowerShell. Support: process relationship and command-line fields.

### 3. Keeping the conclusion within the evidence

If a learner proposes Command and Control, ask which field demonstrates communication. If they assume all PowerShell is malicious, ask how an authorized administrator might use it. Accept alternative mappings only when the learner can support them with the supplied evidence.

**Student-facing emphasis:** Explain why the selected label fits the event. Additional labels need additional support. Behavioral mapping informs an investigation; context determines its significance.

## Knowledge Check — Answer Key

### 1. How do a tactic, technique, and sub-technique differ?

**Expected answer:** A tactic describes a goal; a technique describes a way to achieve a goal; a sub-technique describes a more specific form of that behavior.

**Feedback and assessment:** Execution, T1059, and T1059.001 should occupy the correct levels.

### 2. A process event shows wscript.exe launching powershell.exe with an encoded command. Give a supported mapping and identify the evidence.

**Expected answer:** Execution / T1059.001 — PowerShell, supported by the process relationship and command-line fields.

**Feedback and assessment:** Accept T1059 as a broader mapping, then explain why the PowerShell sub-technique is more precise. A label alone leaves the reasoning uncheckable.

### 3. Does that event establish Command and Control or malicious intent? Explain.

**Expected answer:** Neither is established by that event alone. Command and Control needs supporting communication evidence; malicious intent needs context beyond the interpreter being used.

**Feedback and assessment:** Look for a distinction between observed behavior and an inference about purpose or intent.

## Closing and Transition

ATT&CK provides names for behavior. A useful mapping identifies the tactic and technique or sub-technique, cites the supporting evidence, and explains why the label fits. Keep additional conclusions tied to additional evidence.

Previous: [0.5 – Where the jobs lightly overlap](../../05-where-jobs-overlap/student-guide.md)

Next: [0.6.2 – Diamond Model](../02-diamond-model/student-guide.md)

## References and Further Reading

- [MITRE ATT&CK — Enterprise matrix](https://attack.mitre.org/matrices/enterprise/) — Explore the matrix structure.
- [MITRE ATT&CK — PowerShell (T1059.001)](https://attack.mitre.org/techniques/T1059/001/) — Read the behavior description used in the example.
