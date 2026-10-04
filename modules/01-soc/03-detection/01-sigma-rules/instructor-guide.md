# Instructor Guide – Module 1.3.1 – SIGMA Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.1.1 A / B / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 1a / 2b / 3c  
- Hunter: 1.3.1.1 B / C / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 2b / 3c / 4c  
- CTI: 1.3.1.1 A / B / B ; 1.3.1.2 1a / 2b / 3c ; 1.3.1.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Sigma expresses a detection idea in a shareable format. Reading its source, field tests, and condition helps you understand what a matching event actually proves and what must be mapped before the rule can run in a local platform.

## Learning Objectives

1. Interpret a Sigma rule’s purpose, structure, field tests, and condition.
2. Describe the events a rule would match.
3. Create or modify a basic rule and explain its translation to a local query.

**Mapped Proficiency Items:**
- K: 1.3.1.1 – SIGMA rules
- T: 1.3.1.2 – Analyze an existing SIGMA rule and describe what it detects
- T: 1.3.1.3 – Create or modify a basic SIGMA rule

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required. Learners should produce the requested basic modification and explain a match and nonmatch. Operational deployment follows the later Detection Engineering track and local change procedures.

Use the proficiency levels above to adjust prompting and explanation depth. The module focuses on its mapped knowledge and tasks; the linked next lesson develops the next step.

## Suggested Timing

| Section | Minutes | Focus |
|---|---|---|
| Opening | 2 | Connect the lesson to its purpose. |
| Explanation and worked example | 17 | Read the supplied evidence and demonstrate the reasoning. |
| Knowledge check and feedback | 6 | Complete the interpretation or modification tasks. |
| Summary and transition | 2 | Consolidate the result and connect the next lesson. |
| **Total** | **27** | |

## Detailed Teaching Notes

### 1. Understanding the rule structure

Read the YAML structure before explaining modifiers. Ask learners which sections affect matching and which provide review context.

**Key point to reinforce:** Sigma combines logsource, named selections, and a condition. Conversion requires appropriate backend and field mappings.

### 2. Reading a basic proposal

Use a matching command line and a different parent as a nonmatch. Avoid calling a successful pattern match confirmed malicious activity.

**Key point to reinforce:** The example requires PowerShell, a Script Host parent, and a command-line substring. A match is a behavior pattern.

### 3. Modifying and translating the idea

Have learners produce the parent list, then explain AND across fields and OR within that list. Include translation semantics in feedback, not just field renaming.

**Key point to reinforce:** A parent list permits alternatives while other field tests still apply. Explain matching and nonmatching examples.

## Knowledge Check — Answer Key

### 1. What do logsource, selections, and condition contribute?

**Expected answer:** They identify the telemetry, the field tests, and how the tests combine.

### 2. Describe exactly what the teaching rule matches and one limitation.

**Expected answer:** It matches the specified PowerShell image, wscript parent, and command-line substring together; the substring can overmatch or miss other invocation forms, and it does not establish intent.

### 3. Modify the rule to allow wscript.exe or cscript.exe as parent. Does the command-line test still apply?

**Expected answer:** Use the shown two-value ParentImage list. Either parent can match, and the separate image and command-line tests still apply.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Sigma makes detection logic shareable. Explain the source, tests, and condition, preserve their meaning during translation, and propose changes with clear expected behavior and limitations.

Previous: [1.2.8 – Weird Engine](../../02-zeek/08-weird-engine/student-guide.md)

Next: [1.3.2 – Suricata Rules](../02-suricata-rules/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)
- [Sigma — Conditions](https://sigmahq.io/docs/basics/conditions.html)
