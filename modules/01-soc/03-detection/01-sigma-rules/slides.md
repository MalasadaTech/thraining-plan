# Module 1.3.1 – SIGMA Rules

- Interpret a Sigma rule’s purpose, structure, field tests, and condition.
- Describe the events a rule would match.
- Create or modify a basic rule and explain its translation to a local query.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

Sigma expresses a detection idea in a shareable format. Reading its source, field tests, and condition helps you understand what a matching event actually proves and what must be mapped before the rule can run in a local platform.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Understanding the rule structure

Sigma combines logsource, named selections, and a condition. Conversion requires appropriate backend and field mappings.

**Speaker notes:** Read the YAML structure before explaining modifiers. Ask learners which sections affect matching and which provide review context.

---

## Reading a basic proposal

The example requires PowerShell, a Script Host parent, and a command-line substring. A match is a behavior pattern.

**Speaker notes:** Use a matching command line and a different parent as a nonmatch. Avoid calling a successful pattern match confirmed malicious activity.

---

## Worked example — Reading a basic proposal

```yaml
title: Training PowerShell Encoded Argument From Script Host
status: experimental
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\powershell.exe'
    ParentImage|endswith: '\wscript.exe'
    CommandLine|contains: '-enc'
  condition: selection
falsepositives:
  - Authorized automation using the same invocation pattern
level: medium
```

**Speaker notes:** Use a matching command line and a different parent as a nonmatch. Avoid calling a successful pattern match confirmed malicious activity. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Modifying and translating the idea

A parent list permits alternatives while other field tests still apply. Explain matching and nonmatching examples.

**Speaker notes:** Have learners produce the parent list, then explain AND across fields and OR within that list. Include translation semantics in feedback, not just field renaming.

---

## Worked example — Modifying and translating the idea

```yaml
    ParentImage|endswith:
      - '\wscript.exe'
      - '\cscript.exe'
```

**Speaker notes:** Have learners produce the parent list, then explain AND across fields and OR within that list. Include translation semantics in feedback, not just field renaming. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. What do logsource, selections, and condition contribute?
2. Describe exactly what the teaching rule matches and one limitation.
3. Modify the rule to allow wscript.exe or cscript.exe as parent. Does the command-line test still apply?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

Sigma makes detection logic shareable. Explain the source, tests, and condition, preserve their meaning during translation, and propose changes with clear expected behavior and limitations.

Previous: [1.2.8 – Weird Engine](../../02-zeek/08-weird-engine/student-guide.md)

Next: [1.3.2 – Suricata Rules](../02-suricata-rules/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)
- [Sigma — Conditions](https://sigmahq.io/docs/basics/conditions.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
