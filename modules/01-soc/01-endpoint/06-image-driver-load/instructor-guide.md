# Instructor Guide – Module 1.1.6 – Image and Driver Load Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.6.1 A / B / C ; 1.1.6.2 2b / 3c / 4c ; 1.1.6.3 2b / 3c / 4c  
- Hunter: 1.1.6.1 A / B / B ; 1.1.6.2 1a / 2b / 3c ; 1.1.6.3 1a / 2b / 3c  
- CTI: 1.1.6.1 A / A / A ; 1.1.6.2 1a / 1a / 1a ; 1.1.6.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

An image-load event shows a module being loaded into a process. A driver-load event concerns code loaded into the kernel. Understanding the difference helps you describe the execution context without confusing a file on disk with a recorded load.

## Learning Objectives

1. Distinguish user-mode image loads from kernel driver loads.
2. Describe load paths, process context, hashes, and signature evidence.
3. Create or modify a query for specific image or driver load activity.

**Mapped Proficiency Items:**
- K: 1.1.6.1 – Image and driver load activity concepts
- T: 1.1.6.2 – Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.6.3 – Create a SIEM query to detect specific image or driver load activity

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

### 1. Reading image and driver loads

Use Image versus ImageLoaded to distinguish the process and object. Emphasize which object each hash or signature field describes.

**Key point to reinforce:** Sysmon 7 describes a process image load; Sysmon 6 a kernel driver load. Identify which object each field describes.

### 2. Working through the example

Require attribution of the signature assessment to the source. Discuss why a signed driver could still require investigation.

**Key point to reinforce:** PowerShell loads a Temp DLL reported unsigned by Sysmon. The event does not establish its origin or maliciousness.

### 3. Creating a focused image-load query

Ask what source would be needed for a driver question. Avoid inventing a driver ActionType in the DLL table.

**Key point to reinforce:** Use DLL-load telemetry for a DLL question and driver-load telemetry for a driver question. Map the actual schema.

## Knowledge Check — Answer Key

### 1. How do Sysmon 6 and 7 differ?

**Expected answer:** Event 6 records a kernel driver load; event 7 records an image/module load with its process context.

### 2. Describe the supplied event and distinguish missing signature data from Signed=false.

**Expected answer:** PowerShell loaded the specified Temp DLL, which Sysmon reports as unsigned. A missing signature field would leave that status unknown in the record.

### 3. Modify the query for DLLs loaded by rundll32.exe. Does it become a driver-load query?

**Expected answer:** Change the initiating-process filename to rundll32.exe. It remains a DLL-load query; changing the process does not turn the source into kernel-driver telemetry.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Image and driver events describe different kinds of loads. Identify the loaded object, execution context, and available signature evidence, then search the source that actually records the operation of interest.

Previous: [1.1.5 – Registry Activity](../05-registry-activity/student-guide.md)

Next: [1.2.1 – Zeek Concepts](../../02-zeek/01-concepts/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceImageLoadEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceimageloadevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
