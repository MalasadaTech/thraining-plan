# Instructor Guide – Module 1.1.4 – Network Activity (Endpoint)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.4.1 A / B / C ; 1.1.4.2 2b / 3c / 4c ; 1.1.4.3 2b / 3c / 4c  
- Hunter: 1.1.4.1 A / B / B ; 1.1.4.2 1a / 2b / 3c ; 1.1.4.3 1a / 2b / 3c  
- CTI: 1.1.4.1 A / A / A ; 1.1.4.2 1a / 1a / 1a ; 1.1.4.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Endpoint network events connect network activity to a process on a device. That process context can help explain a connection that a network sensor sees only as traffic between addresses.

## Learning Objectives

1. Interpret endpoint network addresses, operations, direction, names, and process context.
2. Describe the supplied event with its evidence limits.
3. Create or modify a query for specific endpoint network activity.

**Mapped Proficiency Items:**
- K: 1.1.4.1 – Network activity (endpoint) concepts
- T: 1.1.4.2 – Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.4.3 – Create a SIEM query to detect specific endpoint network activity

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

### 1. Reading the endpoint view

Distinguish local/remote from source/destination and initiation. Use Sysmon Initiated as one concrete source-specific example.

**Key point to reinforce:** Read outcome, endpoints, protocol, direction evidence, names, and associated process. Local/remote does not by itself establish initiation.

### 2. Working through the example

Have learners build the sentence from supplied fields; discuss why a commonly used port is insufficient to identify application behavior.

**Key point to reinforce:** PowerShell is associated with a recorded successful TCP connection to 203.0.113.88:443. The record lacks a URL/FQDN.

### 3. Creating a focused network query

Ask what broadens when the process filter is removed. This tests query reasoning without requiring a live connection or tenant.

**Key point to reinforce:** Search the specified process and destination. A connection query and a DNS query answer different questions.

## Knowledge Check — Answer Key

### 1. What does endpoint network evidence add to a native Zeek connection record?

**Expected answer:** It may associate the network activity with an operating-system process and its command line.

### 2. What can you say about the supplied TCP/443 event when RemoteUrl is blank?

**Expected answer:** A successful TCP connection was recorded with PowerShell to the specified remote IP and port; no name is recorded. HTTPS, C2, and hidden execution are not established.

### 3. How would you modify the query to find the same destination used by any process?

**Expected answer:** Remove the initiating-process filename predicate and keep the destination and outcome filters; retain process fields in the output to compare the results.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Endpoint network evidence helps connect a process to a recorded network operation. Describe the outcome, endpoints, protocol, and available names, then use a focused query to investigate the chosen pattern.

Previous: [1.1.3 – File System Activity](../03-file-system-activity/student-guide.md)

Next: [1.1.5 – Registry Activity](../05-registry-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceNetworkEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicenetworkevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
