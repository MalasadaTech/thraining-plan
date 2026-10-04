# Module 1.1.3 – File System Activity

- Interpret file operations, paths, hashes, and initiating processes.
- Describe a file event without inferring execution.
- Create or modify a query for a specific file operation.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

File events help establish what happened to an object on an endpoint and which process performed the operation. Keeping the operation, path, and initiating process together helps distinguish a file arriving from that file later being used.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading file operations

Read the operation, path, initiating process, and available identity data. Sysmon 11 records creation or overwrite.

**Speaker notes:** Explain create/overwrite and distinguish event-time deletion from a current filesystem assessment. Ask what coverage would be needed to discuss file reads.

---

## Reference — Reading file operations

| Detail | Interpretation |
|---|---|
| Create or overwrite | Sysmon 11 records file creation or overwrite. The record does not by itself distinguish every prior state of the path. |
| Rename or move | A source may record a new name or location, with previous path/name fields where available. |
| Delete | Sysmon 23 records deletion with archiving; 26 records deletion without archiving. A deletion record concerns that operation, not permanent absence afterward. |
| Modify or read | Coverage depends on the source and configuration; these operations are not comprehensively represented by Sysmon 11/23/26. |
| Path and extension | Identify the target object. An extension is a name, not proof of content or execution. |
| Hash | Use a recorded hash when available. Sysmon 11 does not supply a file hash; MDE hash population varies. |
| Initiator | Sysmon `Image` or MDE `InitiatingProcess*` identifies the process associated with the file operation. |

**Speaker notes:** Explain create/overwrite and distinguish event-time deletion from a current filesystem assessment. Ask what coverage would be needed to discuss file reads. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

Script Host creates or overwrites the recorded Temp file. A hash and later execution require their own evidence.

**Speaker notes:** Require the path, operation, and initiator in the description. A missing hash does not change the observed operation.

---

## Supplied example

A Sysmon 11 event on `WS-JLEE` records `Image=wscript.exe` and `TargetFilename=C:\Users\jlee\AppData\Local\Temp\update.exe`, with no hash field. Describe it as: “Sysmon recorded Script Host creating or overwriting `update.exe` at the Temp path; this event supplies no file hash.”

**Speaker notes:** Require the path, operation, and initiator in the description. A missing hash does not change the observed operation.

---

## Creating a focused file query

Search the operation, initiator, path, and filename pattern. A name filter does not inspect file contents.

**Speaker notes:** Use one .exe and one .dll name to discuss the filter change. Keep the query task separate from a verdict about the returned files.

---

## Reference — Creating a focused file query

| where Timestamp > ago(1d)
| where ActionType == "FileCreated"
| where InitiatingProcessFileName =~ "wscript.exe"
| where FolderPath contains @"\Temp\"
| where FileName endswith ".exe"
| project Timestamp, DeviceName, ActionType, FolderPath, FileName,

**Speaker notes:** Use one .exe and one .dll name to discuss the filter change. Keep the query task separate from a verdict about the returned files. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused file query

```kusto
DeviceFileEvents
| where Timestamp > ago(1d)
| where ActionType == "FileCreated"
| where InitiatingProcessFileName =~ "wscript.exe"
| where FolderPath contains @"\Temp\"
| where FileName endswith ".exe"
| project Timestamp, DeviceName, ActionType, FolderPath, FileName,
          InitiatingProcessCommandLine, SHA1, SHA256
```

**Speaker notes:** Use one .exe and one .dll name to discuss the filter change. Keep the query task separate from a verdict about the returned files. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. What does Sysmon 11 establish, and does it prove execution?
2. Describe the supplied event when its hash is unavailable.
3. Modify the query to search for DLL-named files and explain the limitation.

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

File evidence describes an operation on a path by an associated process. Use the available identity fields, preserve coverage gaps, and query the operation that answers the investigation question.

Previous: [1.1.2 – Process Activity](../02-process-activity/student-guide.md)

Next: [1.1.4 – Network Activity (Endpoint)](../04-network-activity/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceFileEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicefileevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
