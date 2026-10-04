# Module 1.1.3 – File System Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.3.1 A / B / C ; 1.1.3.2 2b / 3c / 4c ; 1.1.3.3 2b / 3c / 4c  
- Hunter: 1.1.3.1 A / B / B ; 1.1.3.2 1a / 2b / 3c ; 1.1.3.3 1a / 2b / 3c  
- CTI: 1.1.3.1 A / A / A ; 1.1.3.2 1a / 1a / 1a ; 1.1.3.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret file operations, paths, hashes, and initiating processes.
2. Describe a file event without inferring execution.
3. Create or modify a query for a specific file operation.

**Mapped Proficiency Items:**
- K: 1.1.3.1 – File system activity concepts
- T: 1.1.3.2 – Analyze a file event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.3.3 – Create a SIEM query to detect specific file operations

## Why This Matters

File events help establish what happened to an object on an endpoint and which process performed the operation. Keeping the operation, path, and initiating process together helps distinguish a file arriving from that file later being used.

## 1. Reading file operations

| Detail | Interpretation |
|---|---|
| Create or overwrite | Sysmon 11 records file creation or overwrite. The record does not by itself distinguish every prior state of the path. |
| Rename or move | A source may record a new name or location, with previous path/name fields where available. |
| Delete | Sysmon 23 records deletion with archiving; 26 records deletion without archiving. A deletion record concerns that operation, not permanent absence afterward. |
| Modify or read | Coverage depends on the source and configuration; these operations are not comprehensively represented by Sysmon 11/23/26. |
| Path and extension | Identify the target object. An extension is a name, not proof of content or execution. |
| Hash | Use a recorded hash when available. Sysmon 11 does not supply a file hash; MDE hash population varies. |
| Initiator | Sysmon `Image` or MDE `InitiatingProcess*` identifies the process associated with the file operation. |

MDE `DeviceFileEvents` includes file operations such as creation, modification, rename, and deletion where collected. Check the supported actions and previous-name fields in the schema. An absent record could reflect coverage or retention rather than absence of activity.

## 2. Working through the example

A Sysmon 11 event on `WS-JLEE` records `Image=wscript.exe` and `TargetFilename=C:\Users\jlee\AppData\Local\Temp\update.exe`, with no hash field. Describe it as: “Sysmon recorded Script Host creating or overwriting `update.exe` at the Temp path; this event supplies no file hash.”

The event does not establish that `update.exe` ran. To investigate execution, look for a related process event using the host, time, path, and any available identity evidence. Treat that as an additional observation rather than adding it to the file event's meaning.

## 3. Creating a focused file query

The following KQL example illustrates the requested search. Confirm the table, fields, and supported `ActionType` values in your environment before using it. Adjust the time range to the investigation.

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

This searches for executable-named file creations associated with Script Host under a Temp path. The name filter does not inspect the bytes. A rename question needs the appropriate rename action and available previous/current path fields, rather than treating file creation as a rename.

## Knowledge Check

1. What does Sysmon 11 establish, and does it prove execution?
2. Describe the supplied event when its hash is unavailable.
3. Modify the query to search for DLL-named files and explain the limitation.

## Summary

File evidence describes an operation on a path by an associated process. Use the available identity fields, preserve coverage gaps, and query the operation that answers the investigation question.

## Course Connections

Previous: [1.1.2 – Process Activity](../02-process-activity/student-guide.md)

Next: [1.1.4 – Network Activity (Endpoint)](../04-network-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceFileEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicefileevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
