# Instructor Guide – Module 1.3.4 – SIEM Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.4.1 A / B / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 1a / 2b / 3c  
- Hunter: 1.3.4.1 B / C / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 2b / 3c / 4c  
- CTI: 1.3.4.1 A / B / B ; 1.3.4.2 1a / 2b / 3c ; 1.3.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

A saved detection combines search logic with operating settings that determine when and how an alert is created. Reading both parts explains what an alert represents and helps turn a query into a reviewable detection proposal.

## Learning Objectives

1. Identify the source, logic, timing, trigger, and output of a saved detection.
2. Explain what a rule would match and what would create an alert.
3. Create a basic proposal from known log fields or a Sigma rule.

**Mapped Proficiency Items:**
- K: 1.3.4.1 – SIEM rules
- T: 1.3.4.2 – Analyze an existing SIEM rule and describe what it detects
- T: 1.3.4.3 – Create a basic SIEM detection rule from log fields or a SIGMA rule

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

### 1. Understanding the detection proposal

Separate the query from its scheduling and alert settings. Explain that an empty source or late ingestion can affect coverage even if the predicates are correct.

**Key point to reinforce:** Specify source, logic, lookback, frequency, trigger, output, and alert handling. A query is one part of the detection.

### 2. Reading a worked proposal

Read the query and then the trigger statement. A filter match and a platform-created alert are related but distinct steps.

**Key point to reinforce:** The teaching proposal runs every five minutes over a five-minute window and triggers on matching process events.

### 3. Creating or translating a basic rule

Ask learners to produce the predicate and describe the surrounding rule settings. Compare contains and has without implying their semantics are interchangeable.

**Key point to reinforce:** Translate field tests and their semantics. Review late data and repeated matches before operational use.

## Knowledge Check — Answer Key

### 1. How do lookback and run frequency differ?

**Expected answer:** Lookback is the time range searched by each run; frequency is how often the search runs.

### 2. Describe the example’s matching logic and trigger.

**Expected answer:** It selects process-created PowerShell events with the specified Script Host parent and -enc substring; the classroom trigger is one or more matches.

### 3. Create a modified proposal that permits both Script Host parents. What besides the predicate should it specify?

**Expected answer:** Use the two-value in~ parent predicate, preserve the other tests, and specify source, purpose/name, lookback, frequency, trigger, outputs, and reviewed alert handling.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

A SIEM detection proposal connects clear logic to a source, schedule, trigger, and useful output. Preserve matching semantics when translating Sigma and review timing and alert behavior before deployment.

Previous: [1.3.3 – YARA Rules](../03-yara-rules/student-guide.md)

Next: [1.4.1 – Alert Context and Investigation](../../04-alerts/01-context-investigation/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
- [Microsoft — Custom detection rules](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules)
- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)
