# Module 1.1.2 – Process Activity

- Interpret process creation, termination, and access events.
- Describe a process event using its recorded fields and limitations.
- Create or modify a query for a specific process pattern.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

A process event helps answer which program ran, what started it, and under which account. Reading those relationships carefully gives the investigation a stronger starting point than relying on the executable name alone.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading a process event

Read the operation, process identity, command line, parent, account, integrity, and available hashes. Process access differs from creation.

**Speaker notes:** Have learners identify the operation first, then explain parent, user, and stable identity. Clarify that hash and original-name fields describe files or metadata rather than intent.

---

## Reference — Reading a process event

| Detail | What to examine |
|---|---|
| Operation | Sysmon 1 records process creation, 5 termination, and 10 process access. These are different operations. |
| Process identity | Image path, PID, event time, and a stable process identifier where available. PIDs can be reused. |
| Command line | Recorded arguments explain how the program was invoked; they may be incomplete or attacker-controlled. |
| Parent and account | Parent fields and user context help explain the launch relationship. In an MDE creation event, `InitiatingProcess*` describes the initiating process. |
| Integrity and elevation | Use recorded integrity and token information to assess execution context. An empty field leaves a gap. |
| Hash and original filename | Identify the file and its embedded metadata. MDE uses `ProcessVersionInfoOriginalFileName`; a name or trusted hash alone does not establish benign use. |

**Speaker notes:** Have learners identify the operation first, then explain parent, user, and stable identity. Clarify that hash and original-name fields describe files or metadata rather than intent. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

Script Host launches PowerShell with an encoded argument as jlee. Decoded behavior and hidden-window execution remain unestablished.

**Speaker notes:** Ask which field supports each phrase. Challenge the word “hidden” if a learner introduces it without evidence.

---

## Supplied example

The supplied creation event records `wscript.exe` launching `powershell.exe -enc …` as `jlee`. A supported description is: “Script Host launched PowerShell with an encoded-command argument under the recorded account `jlee`.” The parent, command line, and account fields support the sentence.

**Speaker notes:** Ask which field supports each phrase. Challenge the word “hidden” if a learner introduces it without evidence.

---

## Creating a focused process query

Filter the process-created event by image, parent, and command-line pattern. Explain substring matching and coverage limits.

**Speaker notes:** Read each query filter aloud and compare one matching event with a nonmatching parent. This is a worked query discussion; execution in a live tenant is not required.

---

## Reference — Creating a focused process query

| where Timestamp > ago(1d)
| where ActionType == "ProcessCreated"
| where FileName =~ "powershell.exe"
| where InitiatingProcessFileName =~ "wscript.exe"
| where ProcessCommandLine contains "-enc"
| project Timestamp, DeviceName, AccountName, ProcessCommandLine,

**Speaker notes:** Read each query filter aloud and compare one matching event with a nonmatching parent. This is a worked query discussion; execution in a live tenant is not required. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused process query

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

**Speaker notes:** Read each query filter aloud and compare one matching event with a nonmatching parent. This is a worked query discussion; execution in a live tenant is not required. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. What distinguishes Sysmon events 1, 5, and 10?
2. Describe the supplied wscript-to-PowerShell event and identify one unknown.
3. Modify the query to look for the same PowerShell pattern started by cscript.exe. What changes?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

A useful process description connects the operation, program, command line, parent, and account to recorded evidence. A focused query expresses the chosen pattern and makes its coverage limits clear.

Previous: [1.1.1 – Endpoint activity (the map)](../01-endpoint-activity/student-guide.md)

Next: [1.1.3 – File System Activity](../03-file-system-activity/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceProcessEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
