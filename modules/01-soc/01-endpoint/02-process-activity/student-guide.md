# Module 1.1.2 – Process Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.2.1 A / B / C ; 1.1.2.2 2b / 3c / 4c ; 1.1.2.3 2b / 3c / 4c  
- Hunter: 1.1.2.1 A / B / B ; 1.1.2.2 1a / 2b / 3c ; 1.1.2.3 1a / 2b / 3c  
- CTI: 1.1.2.1 A / A / A ; 1.1.2.2 1a / 1a / 1a ; 1.1.2.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret process creation, termination, and access events.
2. Describe a process event using its recorded fields and limitations.
3. Create or modify a query for a specific process pattern.

**Mapped Proficiency Items:**
- K: 1.1.2.1 – Process activity concepts
- T: 1.1.2.2 – Analyze a process event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.2.3 – Create a SIEM query to detect specific process activity

## Why This Matters

A process event helps answer which program ran, what started it, and under which account. Reading those relationships carefully gives the investigation a stronger starting point than relying on the executable name alone.

## 1. Reading a process event

| Detail | What to examine |
|---|---|
| Operation | Sysmon 1 records process creation, 5 termination, and 10 process access. These are different operations. |
| Process identity | Image path, PID, event time, and a stable process identifier where available. PIDs can be reused. |
| Command line | Recorded arguments explain how the program was invoked; they may be incomplete or attacker-controlled. |
| Parent and account | Parent fields and user context help explain the launch relationship. In an MDE creation event, `InitiatingProcess*` describes the initiating process. |
| Integrity and elevation | Use recorded integrity and token information to assess execution context. An empty field leaves a gap. |
| Hash and original filename | Identify the file and its embedded metadata. MDE uses `ProcessVersionInfoOriginalFileName`; a name or trusted hash alone does not establish benign use. |

`DeviceProcessEvents` provides process creation and related observations. Use its in-portal schema to confirm event types rather than assuming every Sysmon operation has a direct equivalent there. For process access, describe the recorded source and target; opening a handle alone does not establish injection.

## 2. Working through the example

The supplied creation event records `wscript.exe` launching `powershell.exe -enc …` as `jlee`. A supported description is: “Script Host launched PowerShell with an encoded-command argument under the recorded account `jlee`.” The parent, command line, and account fields support the sentence.

The abbreviated command line does not show the decoded instructions. It also does not establish a hidden window: that needs an appropriate argument or other evidence. Record the event reference and time so another analyst can recover the source. A legitimate PowerShell binary can be used for either authorized or malicious activity.

## 3. Creating a focused process query

The following KQL example illustrates the requested search. Confirm the table, fields, and supported `ActionType` values in your environment before using it. Adjust the time range to the investigation.

```kusto
DeviceProcessEvents
| where Timestamp > ago(1d)
| where ActionType == "ProcessCreated"
| where FileName =~ "powershell.exe"
| where InitiatingProcessFileName =~ "wscript.exe"
| where ProcessCommandLine contains "-enc"
| project Timestamp, DeviceName, AccountName, ProcessCommandLine,
          InitiatingProcessCommandLine, ProcessId, SHA1, SHA256
```

The filters search for the three observed characteristics together. `contains` performs a substring search; this teaching example can match longer text and does not cover every spelling or form of PowerShell invocation. Review the returned command lines before interpreting a match. To create a query for a different parent, change the initiating-process predicate and explain how the result set changes.

## Knowledge Check

1. What distinguishes Sysmon events 1, 5, and 10?
2. Describe the supplied wscript-to-PowerShell event and identify one unknown.
3. Modify the query to look for the same PowerShell pattern started by cscript.exe. What changes?

## Summary

A useful process description connects the operation, program, command line, parent, and account to recorded evidence. A focused query expresses the chosen pattern and makes its coverage limits clear.

## Course Connections

Previous: [1.1.1 – Endpoint activity (the map)](../01-endpoint-activity/student-guide.md)

Next: [1.1.3 – File System Activity](../03-file-system-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceProcessEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
