# Module 1.3.4 – SIEM Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.4.1 A / B / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 1a / 2b / 3c  
- Hunter: 1.3.4.1 B / C / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 2b / 3c / 4c  
- CTI: 1.3.4.1 A / B / B ; 1.3.4.2 1a / 2b / 3c ; 1.3.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Identify the source, logic, timing, trigger, and output of a saved detection.
2. Explain what a rule would match and what would create an alert.
3. Create a basic proposal from known log fields or a Sigma rule.

**Mapped Proficiency Items:**
- K: 1.3.4.1 – SIEM rules
- T: 1.3.4.2 – Analyze an existing SIEM rule and describe what it detects
- T: 1.3.4.3 – Create a basic SIEM detection rule from log fields or a SIGMA rule

## Why This Matters

A saved detection combines search logic with operating settings that determine when and how an alert is created. Reading both parts explains what an alert represents and helps turn a query into a reviewable detection proposal.

## 1. Understanding the detection proposal

| Component | What to specify |
|---|---|
| Name and purpose | The activity the detection is intended to identify. |
| Source | Required table, event types, and populated fields. |
| Logic | Matching predicates and any grouping, count, or threshold. |
| Lookback | How far back each run searches. |
| Frequency | How often it runs; distinct from lookback. |
| Output | Evidence and entity fields needed to investigate a result. |
| Alert behavior | How matches become alerts and how repeated matches are handled. |

A basic rule can filter one table; joining multiple sources is not required. A broad search may be useful for exploration, but a detection proposal should explain why the returned activity warrants attention and how much routine activity it may include.

## 2. Reading a worked proposal

**Name:** PowerShell encoded argument from Script Host. **Classroom schedule:** run every five minutes with a five-minute lookback. **Trigger:** one or more matching events. **Output:** event and host identifiers plus the command-line context below. Grouping and duplicate handling remain settings to confirm in the target platform.

```kusto
DeviceProcessEvents
| where Timestamp > ago(5m)
| where ActionType == "ProcessCreated"
| where FileName =~ "powershell.exe"
| where InitiatingProcessFileName =~ "wscript.exe"
| where ProcessCommandLine contains "-enc"
| project Timestamp, DeviceId, DeviceName, ReportId, AccountName,
          ProcessCommandLine, InitiatingProcessCommandLine
```

This KQL illustrates the three-field process pattern. It requires the supported MDE source and action. The simplified schedule may miss late-arriving data; a deployable rule needs appropriate lookback, timing, and duplicate handling. It has not been validated against a live tenant.

## 3. Creating or translating a basic rule

From log fields, choose the operation and predicates that express the target behavior, then specify schedule, trigger, and outputs. From Sigma, map `logsource` to the appropriate table/event and preserve the meaning of selections and condition. Translation is more than renaming fields.

Choose comparison operators according to the question. In KQL, `contains` is a substring operation, `has` is term-based, and `=~` is case-insensitive equality. A literal asterisk inside `contains` is not a general wildcard. Other SIEM languages have different wildcard and regex rules. Use regex when its additional pattern control is needed and describe the intended matches.

For example, broadening the parent predicate to `InitiatingProcessFileName in~ ("wscript.exe", "cscript.exe")` includes either Script Host program while retaining the other conditions. Submit the proposal with a matching and nonmatching example for review.

## Knowledge Check

1. How do lookback and run frequency differ?
2. Describe the example’s matching logic and trigger.
3. Create a modified proposal that permits both Script Host parents. What besides the predicate should it specify?

## Summary

A SIEM detection proposal connects clear logic to a source, schedule, trigger, and useful output. Preserve matching semantics when translating Sigma and review timing and alert behavior before deployment.

## Course Connections

Previous: [1.3.3 – YARA Rules](../03-yara-rules/student-guide.md)

Next: [1.3 – Detection Rules Summary](../summary.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
- [Microsoft — Custom detection rules](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules)
- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)
