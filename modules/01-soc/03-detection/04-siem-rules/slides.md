# Module 1.3.4 – SIEM Rules

- Identify the source, logic, timing, trigger, and output of a saved detection.
- Explain what a rule would match and what would create an alert.
- Create a basic proposal from known log fields or a Sigma rule.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

A saved detection combines search logic with operating settings that determine when and how an alert is created. Reading both parts explains what an alert represents and helps turn a query into a reviewable detection proposal.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Understanding the detection proposal

Specify source, logic, lookback, frequency, trigger, output, and alert handling. A query is one part of the detection.

**Speaker notes:** Separate the query from its scheduling and alert settings. Explain that an empty source or late ingestion can affect coverage even if the predicates are correct.

---

## Reference — Understanding the detection proposal

| Component | What to specify |
|---|---|
| Name and purpose | The activity the detection is intended to identify. |
| Source | Required table, event types, and populated fields. |
| Logic | Matching predicates and any grouping, count, or threshold. |
| Lookback | How far back each run searches. |
| Frequency | How often it runs; distinct from lookback. |
| Output | Evidence and entity fields needed to investigate a result. |
| Alert behavior | How matches become alerts and how repeated matches are handled. |

**Speaker notes:** Separate the query from its scheduling and alert settings. Explain that an empty source or late ingestion can affect coverage even if the predicates are correct. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Reading a worked proposal

The teaching proposal runs every five minutes over a five-minute window and triggers on matching process events.

**Speaker notes:** Read the query and then the trigger statement. A filter match and a platform-created alert are related but distinct steps.

---

## Reference — Reading a worked proposal

| where Timestamp > ago(5m)
| where ActionType == "ProcessCreated"
| where FileName =~ "powershell.exe"
| where InitiatingProcessFileName =~ "wscript.exe"
| where ProcessCommandLine contains "-enc"
| project Timestamp, DeviceId, DeviceName, ReportId, AccountName,

**Speaker notes:** Read the query and then the trigger statement. A filter match and a platform-created alert are related but distinct steps. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Reading a worked proposal

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

**Speaker notes:** Read the query and then the trigger statement. A filter match and a platform-created alert are related but distinct steps. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Creating or translating a basic rule

Translate field tests and their semantics. Review late data and repeated matches before operational use.

**Speaker notes:** Ask learners to produce the predicate and describe the surrounding rule settings. Compare contains and has without implying their semantics are interchangeable.

---

## Knowledge check

1. How do lookback and run frequency differ?
2. Describe the example’s matching logic and trigger.
3. Create a modified proposal that permits both Script Host parents. What besides the predicate should it specify?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

A SIEM detection proposal connects clear logic to a source, schedule, trigger, and useful output. Preserve matching semantics when translating Sigma and review timing and alert behavior before deployment.

Previous: [1.3.3 – YARA Rules](../03-yara-rules/student-guide.md)

Next: [1.4.1 – Alert Context and Investigation](../../04-alerts/01-context-investigation/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
- [Microsoft — Custom detection rules](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules)
- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
