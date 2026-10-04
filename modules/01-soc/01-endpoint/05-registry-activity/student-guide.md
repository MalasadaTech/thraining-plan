# Module 1.1.5 – Registry Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.5.1 A / B / C ; 1.1.5.2 2b / 3c / 4c ; 1.1.5.3 2b / 3c / 4c  
- Hunter: 1.1.5.1 A / B / B ; 1.1.5.2 1a / 2b / 3c ; 1.1.5.3 1a / 2b / 3c  
- CTI: 1.1.5.1 A / A / A ; 1.1.5.2 1a / 1a / 1a ; 1.1.5.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret registry structure and create, set, delete, and rename operations.
2. Describe a registry change and its evidence limits.
3. Create or modify a query for specific registry operations.

**Mapped Proficiency Items:**
- K: 1.1.5.1 – Registry activity concepts
- T: 1.1.5.2 – Analyze a registry event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.5.3 – Create a SIEM query to detect specific registry operations

## Why This Matters

Registry events record changes to Windows configuration. Reading the key, value name, value data, and initiating process separately helps explain exactly what changed and what follow-up evidence would be useful.

## 1. Reading the registry structure

A hive is a top-level registry area. A key provides a path, and a value within that key has a name, type, and data. `HKLM` concerns machine configuration. `HKCU` refers to the current user's hive; records may instead identify that user's hive under `HKU\<SID>`. Preserve the SID and resolve its account context when needed.

| Operation or field | What to read |
|---|---|
| Create/delete | Sysmon 12 records creation or deletion of registry objects; read the event's operation detail. |
| Set value | Sysmon 13 records a value being set, with details subject to the value type and logging behavior. |
| Rename | Sysmon 14 records key or value rename. |
| MDE fields | `DeviceRegistryEvents`: `RegistryKey`, `RegistryValueName`, `RegistryValueData`, `ActionType`, and `InitiatingProcess*`. |
| Locations | Run/RunOnce and service configuration keys can be relevant to startup behavior. Location alone does not establish malicious persistence. |

If value data is blank, distinguish an absent or uncollected value from a genuinely empty value where the source permits it. Otherwise state that the available record does not resolve the distinction.

## 2. Working through the example

The supplied event records PowerShell setting value `Updater` under the user's `Software\Microsoft\Windows\CurrentVersion\Run` key to `C:\Users\jlee\AppData\Local\Temp\update.exe`.

Describe the configuration change: “PowerShell set the user's Run value `Updater` to the recorded Temp executable path.” This can configure a startup action, but the event does not establish that the file exists, that a later logon ran it, or that the change was unauthorized. Those questions require supporting file, process, and authorization context.

## 3. Creating a focused registry query

The following KQL example illustrates the requested search. Confirm the table, fields, and supported `ActionType` values in your environment before using it. Adjust the time range to the investigation.

```kusto
DeviceRegistryEvents
| where Timestamp > ago(1d)
| where ActionType == "RegistryValueSet"
| where InitiatingProcessFileName =~ "powershell.exe"
| where RegistryKey endswith @"\Software\Microsoft\Windows\CurrentVersion\Run"
| where RegistryValueName =~ "Updater"
| project Timestamp, DeviceName, RegistryKey, RegistryValueName,
          RegistryValueData, InitiatingProcessCommandLine
```

The key suffix and value-name predicates focus the search on this configuration change. Confirm how your source represents hive paths. Removing the value-name predicate broadens the search to other values under that Run key; it does not automatically cover RunOnce or all startup mechanisms.

## Knowledge Check

1. How do a key, value name, and value data differ?
2. Describe the supplied Updater change and one thing it leaves unknown.
3. Modify the query to find any value set by PowerShell under the same Run key.

## Summary

A registry finding should identify the operation, key, named value, available data, and initiating process. This makes the configuration change clear while leaving later behavior and authorization to additional evidence.

## Course Connections

Previous: [1.1.4 – Network Activity (Endpoint)](../04-network-activity/student-guide.md)

Next: [1.1.6 – Image and Driver Load Activity](../06-image-driver-load/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceRegistryEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceregistryevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
