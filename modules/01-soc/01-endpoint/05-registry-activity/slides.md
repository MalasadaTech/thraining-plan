# Module 1.1.5 – Registry Activity

- Interpret registry structure and create, set, delete, and rename operations.
- Describe a registry change and its evidence limits.
- Create or modify a query for specific registry operations.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

Registry events record changes to Windows configuration. Reading the key, value name, value data, and initiating process separately helps explain exactly what changed and what follow-up evidence would be useful.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading the registry structure

Separate hive, key, value name, and value data. Read the specific create, set, delete, or rename operation.

**Speaker notes:** Draw the hierarchy in words using the table: hive, key, value name, data. Explain that HKCU depends on account context.

---

## Reference — Reading the registry structure

| Operation or field | What to read |
|---|---|
| Create/delete | Sysmon 12 records creation or deletion of registry objects; read the event's operation detail. |
| Set value | Sysmon 13 records a value being set, with details subject to the value type and logging behavior. |
| Rename | Sysmon 14 records key or value rename. |
| MDE fields | `DeviceRegistryEvents`: `RegistryKey`, `RegistryValueName`, `RegistryValueData`, `ActionType`, and `InitiatingProcess*`. |
| Locations | Run/RunOnce and service configuration keys can be relevant to startup behavior. Location alone does not establish malicious persistence. |

**Speaker notes:** Draw the hierarchy in words using the table: hive, key, value name, data. Explain that HKCU depends on account context. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

PowerShell sets the user’s Run value Updater to a Temp executable path. Later execution remains a separate question.

**Speaker notes:** Ask learners to separate configured behavior from later execution. This preserves the useful persistence connection without claiming a completed hunt.

---

## Supplied example

The supplied event records PowerShell setting value `Updater` under the user's `Software\Microsoft\Windows\CurrentVersion\Run` key to `C:\Users\jlee\AppData\Local\Temp\update.exe`.

**Speaker notes:** Ask learners to separate configured behavior from later execution. This preserves the useful persistence connection without claiming a completed hunt.

---

## Creating a focused registry query

Query the set operation, initiating process, key suffix, and value name. Explain which locations the predicates cover.

**Speaker notes:** Check that learners broaden only the requested value-name scope. Do not accept replacing the query with every registry event.

---

## Reference — Creating a focused registry query

| where Timestamp > ago(1d)
| where ActionType == "RegistryValueSet"
| where InitiatingProcessFileName =~ "powershell.exe"
| where RegistryKey endswith @"\Software\Microsoft\Windows\CurrentVersion\Run"
| where RegistryValueName =~ "Updater"
| project Timestamp, DeviceName, RegistryKey, RegistryValueName,

**Speaker notes:** Check that learners broaden only the requested value-name scope. Do not accept replacing the query with every registry event. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused registry query

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

**Speaker notes:** Check that learners broaden only the requested value-name scope. Do not accept replacing the query with every registry event. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. How do a key, value name, and value data differ?
2. Describe the supplied Updater change and one thing it leaves unknown.
3. Modify the query to find any value set by PowerShell under the same Run key.

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

A registry finding should identify the operation, key, named value, available data, and initiating process. This makes the configuration change clear while leaving later behavior and authorization to additional evidence.

Previous: [1.1.4 – Network Activity (Endpoint)](../04-network-activity/student-guide.md)

Next: [1.1.6 – Image and Driver Load Activity](../06-image-driver-load/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceRegistryEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceregistryevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
