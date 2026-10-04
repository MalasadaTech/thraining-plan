# Module 1.3.1 – SIGMA Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.1.1 A / B / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 1a / 2b / 3c  
- Hunter: 1.3.1.1 B / C / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 2b / 3c / 4c  
- CTI: 1.3.1.1 A / B / B ; 1.3.1.2 1a / 2b / 3c ; 1.3.1.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret a Sigma rule’s purpose, structure, field tests, and condition.
2. Describe the events a rule would match.
3. Create or modify a basic rule and explain its translation to a local query.

**Mapped Proficiency Items:**
- K: 1.3.1.1 – SIGMA rules
- T: 1.3.1.2 – Analyze an existing SIGMA rule and describe what it detects
- T: 1.3.1.3 – Create or modify a basic SIGMA rule

## Why This Matters

Sigma expresses a detection idea in a shareable format. Reading its source, field tests, and condition helps you understand what a matching event actually proves and what must be mapped before the rule can run in a local platform.

## 1. Understanding the rule structure

A basic Sigma rule uses YAML. The `title` describes the rule, `logsource` identifies the required telemetry, and `detection` contains named selections and a condition. Metadata such as status, references, and false-positive notes helps readers assess the proposal; it does not replace matching logic.

Within a selection, different field tests are normally combined with AND. A list of values for one field is normally OR unless a modifier changes that behavior. Modifiers such as `endswith`, `contains`, and `re` express suffix, substring, or regular-expression tests. Read the condition to see how selections combine.

Sigma can describe many kinds of log sources, not only endpoint logs. Conversion requires a supported backend and field/logsource mappings appropriate to the target platform.

## 2. Reading a basic proposal

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

This teaching rule selects a Windows process-creation event whose image ends in `powershell.exe`, whose parent ends in `wscript.exe`, and whose command line contains `-enc`. All three tests must match.

The substring test may include longer arguments or incidental text and can miss other invocation forms. A match establishes the selected pattern, not malicious intent. The experimental status and false-positive note make the proposal's maturity and a plausible benign explanation visible.

## 3. Modifying and translating the idea

To include both Script Host programs, change the parent selection to a list:

```yaml
    ParentImage|endswith:
      - '\wscript.exe'
      - '\cscript.exe'
```

The list allows either parent while retaining the PowerShell image and command-line tests. In an MDE process-creation query, the corresponding fields are `FileName`, `InitiatingProcessFileName`, and `ProcessCommandLine`; preserve the intended suffix/filename and substring semantics when translating.

A useful proposal explains expected matches, a relevant nonmatch, and known limitations. The course's SOC workflow sends basic rule proposals to Detection Engineering for review and testing under local change procedures.

## Knowledge Check

1. What do logsource, selections, and condition contribute?
2. Describe exactly what the teaching rule matches and one limitation.
3. Modify the rule to allow wscript.exe or cscript.exe as parent. Does the command-line test still apply?

## Summary

Sigma makes detection logic shareable. Explain the source, tests, and condition, preserve their meaning during translation, and propose changes with clear expected behavior and limitations.

## Course Connections

Previous: [1.2.8 – Weird Engine](../../02-zeek/08-weird-engine/student-guide.md)

Next: [1.3.2 – Suricata Rules](../02-suricata-rules/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)
- [Sigma — Conditions](https://sigmahq.io/docs/basics/conditions.html)
