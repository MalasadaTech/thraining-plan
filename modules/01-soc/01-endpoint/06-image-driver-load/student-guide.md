# Module 1.1.6 – Image and Driver Load Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.6.1 A / B / C ; 1.1.6.2 2b / 3c / 4c ; 1.1.6.3 2b / 3c / 4c  
- Hunter: 1.1.6.1 A / B / B ; 1.1.6.2 1a / 2b / 3c ; 1.1.6.3 1a / 2b / 3c  
- CTI: 1.1.6.1 A / A / A ; 1.1.6.2 1a / 1a / 1a ; 1.1.6.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Distinguish user-mode image loads from kernel driver loads.
2. Describe load paths, process context, hashes, and signature evidence.
3. Create or modify a query for specific image or driver load activity.

**Mapped Proficiency Items:**
- K: 1.1.6.1 – Image and driver load activity concepts
- T: 1.1.6.2 – Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.6.3 – Create a SIEM query to detect specific image or driver load activity

## Why This Matters

An image-load event shows a module being loaded into a process. A driver-load event concerns code loaded into the kernel. Understanding the difference helps you describe the execution context without confusing a file on disk with a recorded load.

## 1. Reading image and driver loads

| Detail | Interpretation |
|---|---|
| User-mode image load | Sysmon 7: `Image` identifies the process and `ImageLoaded` the module. MDE `DeviceImageLoadEvents` concerns DLL loads. |
| Kernel driver load | Sysmon 6 records the loaded driver. It does not provide a user-mode parent-process relationship equivalent to event 7. |
| Path and hash | Identify the loaded object using the available path and hashes. A .sys extension by itself does not prove a kernel load. |
| Signature | Interpret signature fields for the loaded object where supplied. Missing is different from explicitly unsigned, and signed does not mean harmless. |
| Coverage | Image-load collection can be high volume and selectively enabled. Confirm collection and retention before interpreting an absence. |

In MDE, fields prefixed `InitiatingProcess` describe the initiating process; they should not be mistaken for the loaded DLL's identity or signing status. A loaded-object SHA1/SHA256, when available, concerns the object named by the event.

## 2. Working through the example

A Sysmon 7 event records `Image=powershell.exe`, `ImageLoaded=C:\Users\jlee\AppData\Local\Temp\update.dll`, and `Signed=false`.

A supported description is: “PowerShell loaded the DLL at the recorded Temp path; Sysmon reports the loaded object as unsigned.” The load, path, and reported signature state warrant examination in context. They do not alone establish how the DLL arrived, what code it executed, or whether the activity was malicious. A related file event may explain arrival, while process and other evidence may explain subsequent behavior.

## 3. Creating a focused image-load query

The following KQL example illustrates the requested search. Confirm the table, fields, and supported `ActionType` values in your environment before using it. Adjust the time range to the investigation.

```kusto
DeviceImageLoadEvents
| where Timestamp > ago(1d)
| where InitiatingProcessFileName =~ "powershell.exe"
| where FolderPath contains @"\Temp\"
| where FileName endswith ".dll"
| project Timestamp, DeviceName, FolderPath, FileName, SHA1, SHA256,
          InitiatingProcessFileName, InitiatingProcessCommandLine
```

This searches for DLL loads associated with PowerShell from Temp paths. It does not filter for unsigned DLLs because no loaded-object signature field has been assumed. A kernel-driver question calls for verified driver-load telemetry, such as Sysmon 6, and a query mapped to that source.

For a driver-specific question, this separate KQL example assumes a classroom `SysmonEvents` table with normalized `TimeGenerated`, `EventID`, `Computer`, and `ImageLoaded` columns:

```kusto
SysmonEvents
| where TimeGenerated > ago(1d)
| where EventID == 6
| where ImageLoaded endswith @"\trainingdriver.sys"
| project TimeGenerated, Computer, ImageLoaded
```

It finds recorded driver loads for the specified path suffix; it does not determine whether that driver is safe. Map the table and parsed fields to the actual Sysmon ingestion schema.

## Knowledge Check

1. How do Sysmon 6 and 7 differ?
2. Describe the supplied event and distinguish missing signature data from Signed=false.
3. Modify the query for DLLs loaded by rundll32.exe. Does it become a driver-load query?

## Summary

Image and driver events describe different kinds of loads. Identify the loaded object, execution context, and available signature evidence, then search the source that actually records the operation of interest.

## Course Connections

Previous: [1.1.5 – Registry Activity](../05-registry-activity/student-guide.md)

Next: [1.2.1 – Zeek Concepts](../../02-zeek/01-concepts/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceImageLoadEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceimageloadevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
