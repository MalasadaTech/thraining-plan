# Module 1.1.6 – Image and Driver Load Activity

- Distinguish user-mode image loads from kernel driver loads.
- Describe load paths, process context, hashes, and signature evidence.
- Create or modify a query for specific image or driver load activity.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

An image-load event shows a module being loaded into a process. A driver-load event concerns code loaded into the kernel. Understanding the difference helps you describe the execution context without confusing a file on disk with a recorded load.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading image and driver loads

Sysmon 7 describes a process image load; Sysmon 6 a kernel driver load. Identify which object each field describes.

**Speaker notes:** Use Image versus ImageLoaded to distinguish the process and object. Emphasize which object each hash or signature field describes.

---

## Reference — Reading image and driver loads

| Detail | Interpretation |
|---|---|
| User-mode image load | Sysmon 7: `Image` identifies the process and `ImageLoaded` the module. MDE `DeviceImageLoadEvents` concerns DLL loads. |
| Kernel driver load | Sysmon 6 records the loaded driver. It does not provide a user-mode parent-process relationship equivalent to event 7. |
| Path and hash | Identify the loaded object using the available path and hashes. A .sys extension by itself does not prove a kernel load. |
| Signature | Interpret signature fields for the loaded object where supplied. Missing is different from explicitly unsigned, and signed does not mean harmless. |
| Coverage | Image-load collection can be high volume and selectively enabled. Confirm collection and retention before interpreting an absence. |

**Speaker notes:** Use Image versus ImageLoaded to distinguish the process and object. Emphasize which object each hash or signature field describes. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

PowerShell loads a Temp DLL reported unsigned by Sysmon. The event does not establish its origin or maliciousness.

**Speaker notes:** Require attribution of the signature assessment to the source. Discuss why a signed driver could still require investigation.

---

## Supplied example

A Sysmon 7 event records `Image=powershell.exe`, `ImageLoaded=C:\Users\jlee\AppData\Local\Temp\update.dll`, and `Signed=false`.

**Speaker notes:** Require attribution of the signature assessment to the source. Discuss why a signed driver could still require investigation.

---

## Creating a focused image-load query

Use DLL-load telemetry for a DLL question and driver-load telemetry for a driver question. Map the actual schema.

**Speaker notes:** Ask what source would be needed for a driver question. Avoid inventing a driver ActionType in the DLL table.

---

## Reference — Creating a focused image-load query

| where Timestamp > ago(1d)
| where InitiatingProcessFileName =~ "powershell.exe"
| where FolderPath contains @"\Temp\"
| where FileName endswith ".dll"
| project Timestamp, DeviceName, FolderPath, FileName, SHA1, SHA256,

**Speaker notes:** Ask what source would be needed for a driver question. Avoid inventing a driver ActionType in the DLL table. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Reference — Creating a focused image-load query

| where TimeGenerated > ago(1d)
| where EventID == 6
| where ImageLoaded endswith @"\trainingdriver.sys"
| project TimeGenerated, Computer, ImageLoaded

**Speaker notes:** Ask what source would be needed for a driver question. Avoid inventing a driver ActionType in the DLL table. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused image-load query

```kusto
DeviceImageLoadEvents
| where Timestamp > ago(1d)
| where InitiatingProcessFileName =~ "powershell.exe"
| where FolderPath contains @"\Temp\"
| where FileName endswith ".dll"
| project Timestamp, DeviceName, FolderPath, FileName, SHA1, SHA256,
          InitiatingProcessFileName, InitiatingProcessCommandLine
```

**Speaker notes:** Ask what source would be needed for a driver question. Avoid inventing a driver ActionType in the DLL table. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Worked example — Creating a focused image-load query

```kusto
SysmonEvents
| where TimeGenerated > ago(1d)
| where EventID == 6
| where ImageLoaded endswith @"\trainingdriver.sys"
| project TimeGenerated, Computer, ImageLoaded
```

**Speaker notes:** Ask what source would be needed for a driver question. Avoid inventing a driver ActionType in the DLL table. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. How do Sysmon 6 and 7 differ?
2. Describe the supplied event and distinguish missing signature data from Signed=false.
3. Modify the query for DLLs loaded by rundll32.exe. Does it become a driver-load query?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

Image and driver events describe different kinds of loads. Identify the loaded object, execution context, and available signature evidence, then search the source that actually records the operation of interest.

Previous: [1.1.5 – Registry Activity](../05-registry-activity/student-guide.md)

Next: [1.2.1 – Zeek Concepts](../../02-zeek/01-concepts/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceImageLoadEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceimageloadevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
