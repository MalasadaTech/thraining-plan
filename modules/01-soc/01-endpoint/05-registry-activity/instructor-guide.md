# Instructor Guide – Module 1.1.5 – Registry Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.5.1 A / B / C ; 1.1.5.2 2b / 3c / 4c ; 1.1.5.3 2b / 3c / 4c  
- Hunter: 1.1.5.1 A / B / B ; 1.1.5.2 1a / 2b / 3c ; 1.1.5.3 1a / 2b / 3c  
- CTI: 1.1.5.1 A / A / A ; 1.1.5.2 1a / 1a / 1a ; 1.1.5.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Registry events record changes to Windows configuration. Reading the key, value name, value data, and initiating process separately helps explain exactly what changed and what follow-up evidence would be useful.

## Learning Objectives

1. Interpret registry structure and create, set, delete, and rename operations.
2. Describe a registry change and its evidence limits.
3. Create or modify a query for specific registry operations.

**Mapped Proficiency Items:**
- K: 1.1.5.1 – Registry activity concepts
- T: 1.1.5.2 – Analyze a registry event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.5.3 – Create a SIEM query to detect specific registry operations

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

### 1. Reading the registry structure

Draw the hierarchy in words using the table: hive, key, value name, data. Explain that HKCU depends on account context.

**Key point to reinforce:** Separate hive, key, value name, and value data. Read the specific create, set, delete, or rename operation.

### 2. Working through the example

Ask learners to separate configured behavior from later execution. This preserves the useful persistence connection without claiming a completed hunt.

**Key point to reinforce:** PowerShell sets the user’s Run value Updater to a Temp executable path. Later execution remains a separate question.

### 3. Creating a focused registry query

Check that learners broaden only the requested value-name scope. Do not accept replacing the query with every registry event.

**Key point to reinforce:** Query the set operation, initiating process, key suffix, and value name. Explain which locations the predicates cover.

## Knowledge Check — Answer Key

### 1. How do a key, value name, and value data differ?

**Expected answer:** The key is the configuration path; the value name identifies an entry within it; the data is what that entry stores.

### 2. Describe the supplied Updater change and one thing it leaves unknown.

**Expected answer:** PowerShell set the user’s Run value Updater to the Temp executable path. The record alone does not establish file existence, later execution, or authorization.

### 3. Modify the query to find any value set by PowerShell under the same Run key.

**Expected answer:** Remove the RegistryValueName predicate while retaining the action, initiator, and key filter. Explain that the scope remains that Run location.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

A registry finding should identify the operation, key, named value, available data, and initiating process. This makes the configuration change clear while leaving later behavior and authorization to additional evidence.

Previous: [1.1.4 – Network Activity (Endpoint)](../04-network-activity/student-guide.md)

Next: [1.1.6 – Image and Driver Load Activity](../06-image-driver-load/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceRegistryEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceregistryevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
