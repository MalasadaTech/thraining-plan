# Module 1.1.1 – Endpoint activity (the map)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 2b / 2b  
- Hunter: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 1a / 2b  
- CTI: 1.1.1.1 A / A / A ; 1.1.1.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Recognize the five endpoint activity types.
2. Classify a short description by its recorded operation.
3. Explain why source and collection coverage matter when interpreting an event.

**Mapped Proficiency Items:**
- K: 1.1.1.1 – Endpoint activity (the map)
- T: 1.1.1.2 – Given a one-line description, name the activity type

## Why This Matters

Endpoint evidence helps you describe activity on a device. Recognizing the kind of activity first makes it easier to choose the right fields and explain what the event establishes. The next five lessons build that skill one activity type at a time.

## 1. Five kinds of endpoint activity

An event is a recorded observation. A log can contain many events, and a SIEM may display each event as a row. Collection settings determine which observations are recorded.

| Activity type | What the event concerns | Example |
|---|---|---|
| Process | A program starts, ends, or accesses another process. | A script interpreter launches PowerShell. |
| File | A file operation such as creation, rename, modification, reading, or deletion, where collected. | A process writes a file under Temp. |
| Registry | A Windows registry key or value changes. | A process sets a Run-key value. |
| Host-network | A connection or DNS operation observed by the endpoint. | PowerShell connects to a remote IP address. |
| Image / driver load | A module loads into a process, or a driver loads into the kernel. | A program loads a DLL. |

One sequence can generate several event types. Each observation adds a different part of the account.

## 2. Recognizing the observation

“A file named `update.dll` was created” describes file activity. “PowerShell loaded `update.dll`” describes image-load activity. The filename is shared, but the recorded operation differs. A creation event alone leaves loading or execution unestablished.

Likewise, a process-start event can explain how a program began, while a related host-network event can identify a connection associated with it. Linking the events develops the sequence without asking one record to prove everything.

## 3. Understanding the source

Sysmon and Microsoft Defender for Endpoint (MDE) can provide overlapping endpoint observations. Their event types, fields, and collection coverage differ, so translating between them requires checking the actual schema. They should not be treated as interchangeable copies of the same dataset.

Zeek observes network traffic at a sensor. Its native connection records generally identify network endpoints rather than the operating-system process that opened a socket. Endpoint and network evidence complement one another when host identity, timing, and the observed flow can be connected.

## Knowledge Check

1. Name the five activity types and give an example of each.
2. How does a file-create event differ from an image-load event for the same DLL?
3. Why should you check the schema when moving from Sysmon to MDE?

## Summary

Identify the recorded operation, then use the fields and coverage of its source to describe it. Related events can build a fuller sequence while retaining what each observation actually establishes.

## Course Connections

Previous: [1.1 – Endpoint Evidence Preview](../intro.md)

Next: [1.1.2 – Process Activity](../02-process-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — Advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables)
