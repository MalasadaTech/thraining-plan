# Module 0.6.1 – MITRE ATT&CK

- Explain the purpose and structure of ATT&CK.
- Distinguish a tactic, technique, and sub-technique.
- Map one observed behavior and cite the evidence supporting the mapping.

**Speaker notes:** Introduce the purpose and connect it to the shared course sequence. The objectives describe the understanding learners should demonstrate by the end.

---

## Why this matters

ATT&CK gives analysts a shared vocabulary for describing adversary behavior. A useful mapping connects that vocabulary to evidence, so another analyst can understand why the label fits. This lesson introduces the matrix and shows how to support one mapping from an observed event.

**Speaker notes:** Ask learners where this topic could help them understand an investigation. Use their answers to introduce the example without requiring prior operational experience.

---

## Reading the matrix

Tactic: the goal.

Technique: how the goal is pursued.

Sub-technique: a more specific behavior.

Example: Execution → T1059 → T1059.001 PowerShell.

**Speaker notes:** Open the Enterprise matrix and locate Execution and PowerShell. Ask learners to explain the relationship in their own words. They need to navigate and interpret the structure rather than memorize its contents.

---

## Building an evidence-supported mapping

Observed: wscript.exe launches powershell.exe with an encoded command.

Mapping: Execution / T1059.001 — PowerShell.

Support: process relationship and command-line fields.

**Speaker notes:** Walk from the recorded process fields to the behavior, then to the label. Explain why the sub-technique is more precise than T1059 here. The encoded content need not be decoded to recognize the interpreter, although further investigation may be needed to understand what it did.

---

## Keeping the conclusion within the evidence

Explain why the selected label fits the event.

Additional labels need additional support.

Behavioral mapping informs an investigation; context determines its significance.

**Speaker notes:** If a learner proposes Command and Control, ask which field demonstrates communication. If they assume all PowerShell is malicious, ask how an authorized administrator might use it. Accept alternative mappings only when the learner can support them with the supplied evidence.

---

## Knowledge check

1. How do a tactic, technique, and sub-technique differ?
2. A process event shows wscript.exe launching powershell.exe with an encoded command. Give a supported mapping and identify the evidence.
3. Does that event establish Command and Control or malicious intent? Explain.

**Speaker notes:** Ask learners to explain the evidence or reasoning behind each answer. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for expected responses and feedback.

---

## Summary and next step

ATT&CK provides names for behavior. A useful mapping identifies the tactic and technique or sub-technique, cites the supporting evidence, and explains why the label fits. Keep additional conclusions tied to additional evidence.

Previous: [0.5 – Where the jobs lightly overlap](../../05-where-jobs-overlap/student-guide.md)

Next: [0.6.2 – Diamond Model](../02-diamond-model/student-guide.md)

**Speaker notes:** Revisit any uncertainty from the knowledge check, then connect the lesson to the next topic.

---

## References and further reading

- [MITRE ATT&CK — Enterprise matrix](https://attack.mitre.org/matrices/enterprise/) — Explore the matrix structure.
- [MITRE ATT&CK — PowerShell (T1059.001)](https://attack.mitre.org/techniques/T1059/001/) — Read the behavior description used in the example.

**Speaker notes:** These linked resources support the lesson and provide a place to check definitions and service details.
