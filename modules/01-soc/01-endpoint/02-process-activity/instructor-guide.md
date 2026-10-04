# Instructor Guide – Module 1.1.2 – Process Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.2.1 A / B / C ; 1.1.2.2 2b / 3c / 4c ; 1.1.2.3 2b / 3c / 4c  
- Hunter: 1.1.2.1 A / B / B ; 1.1.2.2 1a / 2b / 3c ; 1.1.2.3 1a / 2b / 3c  
- CTI: 1.1.2.1 A / A / A ; 1.1.2.2 1a / 1a / 1a ; 1.1.2.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

A process event helps answer which program ran, what started it, and under which account. Reading those relationships carefully gives the investigation a stronger starting point than relying on the executable name alone.

## Learning Objectives

1. Interpret process creation, termination, and access events.
2. Describe a process event using its recorded fields and limitations.
3. Create or modify a query for a specific process pattern.

**Mapped Proficiency Items:**
- K: 1.1.2.1 – Process activity concepts
- T: 1.1.2.2 – Analyze a process event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.2.3 – Create a SIEM query to detect specific process activity

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required. For query tasks, ask learners to write or modify the shown query and explain its predicates. Confirm the local schema if demonstrating it in an approved teaching environment.

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

### 1. Reading a process event

Have learners identify the operation first, then explain parent, user, and stable identity. Clarify that hash and original-name fields describe files or metadata rather than intent.

**Key point to reinforce:** Read the operation, process identity, command line, parent, account, integrity, and available hashes. Process access differs from creation.

### 2. Working through the example

Ask which field supports each phrase. Challenge the word “hidden” if a learner introduces it without evidence.

**Key point to reinforce:** Script Host launches PowerShell with an encoded argument as jlee. Decoded behavior and hidden-window execution remain unestablished.

### 3. Creating a focused process query

Read each query filter aloud and compare one matching event with a nonmatching parent. This is a worked query discussion; execution in a live tenant is not required.

**Key point to reinforce:** Filter the process-created event by image, parent, and command-line pattern. Explain substring matching and coverage limits.

## Knowledge Check — Answer Key

### 1. What distinguishes Sysmon events 1, 5, and 10?

**Expected answer:** They record process creation, termination, and process access respectively.

### 2. Describe the supplied wscript-to-PowerShell event and identify one unknown.

**Expected answer:** Script Host launched PowerShell with an encoded-command argument as jlee. The abbreviated command does not establish decoded behavior or hidden-window execution.

### 3. Modify the query to look for the same PowerShell pattern started by cscript.exe. What changes?

**Expected answer:** Replace the initiating-process predicate with `InitiatingProcessFileName =~ "cscript.exe"`; keep the process and command-line predicates. The results now concern that parent.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

A useful process description connects the operation, program, command line, parent, and account to recorded evidence. A focused query expresses the chosen pattern and makes its coverage limits clear.

Previous: [1.1.1 – Endpoint activity (the map)](../01-endpoint-activity/student-guide.md)

Next: [1.1.3 – File System Activity](../03-file-system-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceProcessEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
