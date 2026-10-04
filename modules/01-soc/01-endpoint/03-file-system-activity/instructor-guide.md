# Instructor Guide – Module 1.1.3 – File System Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.3.1 A / B / C ; 1.1.3.2 2b / 3c / 4c ; 1.1.3.3 2b / 3c / 4c  
- Hunter: 1.1.3.1 A / B / B ; 1.1.3.2 1a / 2b / 3c ; 1.1.3.3 1a / 2b / 3c  
- CTI: 1.1.3.1 A / A / A ; 1.1.3.2 1a / 1a / 1a ; 1.1.3.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

File events help establish what happened to an object on an endpoint and which process performed the operation. Keeping the operation, path, and initiating process together helps distinguish a file arriving from that file later being used.

## Learning Objectives

1. Interpret file operations, paths, hashes, and initiating processes.
2. Describe a file event without inferring execution.
3. Create or modify a query for a specific file operation.

**Mapped Proficiency Items:**
- K: 1.1.3.1 – File system activity concepts
- T: 1.1.3.2 – Analyze a file event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.3.3 – Create a SIEM query to detect specific file operations

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

### 1. Reading file operations

Explain create/overwrite and distinguish event-time deletion from a current filesystem assessment. Ask what coverage would be needed to discuss file reads.

**Key point to reinforce:** Read the operation, path, initiating process, and available identity data. Sysmon 11 records creation or overwrite.

### 2. Working through the example

Require the path, operation, and initiator in the description. A missing hash does not change the observed operation.

**Key point to reinforce:** Script Host creates or overwrites the recorded Temp file. A hash and later execution require their own evidence.

### 3. Creating a focused file query

Use one .exe and one .dll name to discuss the filter change. Keep the query task separate from a verdict about the returned files.

**Key point to reinforce:** Search the operation, initiator, path, and filename pattern. A name filter does not inspect file contents.

## Knowledge Check — Answer Key

### 1. What does Sysmon 11 establish, and does it prove execution?

**Expected answer:** It records file creation or overwrite. It does not establish execution.

### 2. Describe the supplied event when its hash is unavailable.

**Expected answer:** Script Host created or overwrote update.exe at the recorded Temp path on WS-JLEE; the event supplies no hash.

### 3. Modify the query to search for DLL-named files and explain the limitation.

**Expected answer:** Change `FileName endswith ".exe"` to `FileName endswith ".dll"`. The query matches names and file operations; it does not establish DLL loading or content.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

File evidence describes an operation on a path by an associated process. Use the available identity fields, preserve coverage gaps, and query the operation that answers the investigation question.

Previous: [1.1.2 – Process Activity](../02-process-activity/student-guide.md)

Next: [1.1.4 – Network Activity (Endpoint)](../04-network-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceFileEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicefileevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
