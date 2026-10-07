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
3. Map one observed behavior, cite the supporting evidence, and choose the better-supported mapping when two nearby ATT&CK labels appear plausible.

**Mapped Proficiency Items:**
- K: 0.6.1.1 – MITRE ATT&CK
- T: 0.6.1.2 – Map observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence

## Preparation

Read the [student guide](student-guide.md) and use [slides.md](slides.md) to support the explanation. Review the answer key before teaching so the discussion and feedback reinforce the same concepts. This lesson uses discussion and worked examples; no lab is required.

## Suggested Timing

| Section | Time | Teaching purpose |
|---|---|---|
| Opening and purpose | 2 min | Connect this lesson to the previous topic. |
| Explanation and worked examples | 12 min | Use the four teaching sections below. |
| Knowledge check and feedback | 4 min | Ask for reasoning as well as an answer. |
| Summary and transition | 2 min | Consolidate the lesson and introduce the next topic. |
| **Total** | **20 min** | |

## Detailed Teaching Notes

### 1. Reading the matrix

Open the Enterprise matrix and locate Execution and PowerShell. Ask learners to explain the relationship in their own words. They need to navigate and interpret the structure rather than memorize its contents.

**Student-facing emphasis:** Tactic: the goal. Technique: how the goal is pursued. Sub-technique: a more specific behavior. Example: Execution → T1059 → T1059.001 PowerShell.

### 2. Building an evidence-supported mapping

Walk from the recorded process fields to the behavior, then to the label. Explain why the sub-technique is more precise than T1059 here. The encoded content need not be decoded to recognize the interpreter, although further investigation may be needed to understand what it did.

**Student-facing emphasis:** Observed: wscript.exe launches powershell.exe with an encoded command. Mapping: Execution / T1059.001 — PowerShell. Support: process relationship and command-line fields.


### 3. Choosing between plausible mappings

Use a registry example to make the learner choose between a broad and a more specific mapping. Show an event where `reg.exe` creates `Updater` under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`. T1112 – Modify Registry is broadly true, but T1547.001 – Registry Run Keys / Startup Folder better describes the specific observed behavior because the target is a Run key used for autostart persistence.

Then remove the Run-key context and ask what changes. If the learner only knows that an unspecified registry value changed, T1112 becomes the safer mapping. This teaches evidence-supported specificity rather than memorizing a preferred answer.

**Student-facing emphasis:** When two labels look plausible, choose the primary mapping whose specificity is supported by the evidence. A broader label may still be true, but it should not replace a more specific supported mapping.

### 4. Keeping the conclusion within the evidence

If a learner proposes Command and Control, ask which field demonstrates communication. If they assume all PowerShell is malicious, ask how an authorized administrator might use it. Accept alternative mappings only when the learner can support them with the supplied evidence.

**Student-facing emphasis:** Explain why the selected label fits the event. Additional labels need additional support. Behavioral mapping informs an investigation; context determines its significance.

## Knowledge Check — Answer Key

### 1. How do a tactic, technique, and sub-technique differ?

**Expected answer:** A tactic describes a goal; a technique describes a way to achieve a goal; a sub-technique describes a more specific form of that behavior.

**Feedback and assessment:** Execution, T1059, and T1059.001 should occupy the correct levels.

### 2. A process event shows `wscript.exe` launching `powershell.exe` with an encoded command. Give a supported mapping, identify the evidence, and explain whether the same event establishes Command and Control or malicious intent.

**Expected answer:** Execution / T1059.001 — PowerShell, supported by the process relationship and command-line fields. The event alone does not establish Command and Control or malicious intent.

**Feedback and assessment:** Accept T1059 as a broader mapping, then explain why the PowerShell sub-technique is more precise. Look for the learner to separate observed behavior from unsupported conclusions about communication or intent.

### 3. A registry event shows `reg.exe` creating a value under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`. Between T1112 and T1547.001, which should be the primary mapping, and why? When would T1112 be the safer choice?

**Expected answer:** T1547.001 should be primary because the evidence identifies a Run key used for autostart persistence. T1112 is broader and describes the generic registry modification. If the event only showed an unspecified registry change without evidence of a Run/Startup persistence location, T1112 would be safer.

**Feedback and assessment:** The learner should choose based on evidence-supported specificity rather than treating both IDs as equally informative or guessing from the tactic name.

## Closing and Transition

ATT&CK provides names for behavior. A useful mapping identifies the tactic and technique or sub-technique, cites the supporting evidence, and explains why the label fits. When two labels look plausible, choose the one whose specificity is best supported by the observed behavior, and keep additional conclusions tied to additional evidence.

Previous: [0.5 – Where the jobs lightly overlap](../../05-where-jobs-overlap/student-guide.md)

Next: [0.6.2 – Diamond Model](../02-diamond-model/student-guide.md)

## References and Further Reading

- [MITRE ATT&CK — Enterprise matrix](https://attack.mitre.org/matrices/enterprise/) — Explore the matrix structure.
- [MITRE ATT&CK — PowerShell (T1059.001)](https://attack.mitre.org/techniques/T1059/001/) — Read the behavior description used in the example.
- [MITRE ATT&CK — Modify Registry (T1112)](https://attack.mitre.org/techniques/T1112/) — Broader registry-modification behavior.
- [MITRE ATT&CK — Registry Run Keys / Startup Folder (T1547.001)](https://attack.mitre.org/techniques/T1547/001/) — More specific Run-key persistence behavior.
