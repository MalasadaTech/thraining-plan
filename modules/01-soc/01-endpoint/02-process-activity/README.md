# Process Activity

**Path:** `modules/01-soc/01-endpoint/02-process-activity`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

A process event helps answer which program ran, what started it, and under which account. Reading those relationships carefully gives the investigation a stronger starting point than relying on the executable name alone.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.1.2.1 | K | Process activity concepts | 1.1.2 a–g |
| 1.1.2.2 | T | Analyze a process event (Sysmon or MDE) and accurately describe what occurred | 1.1.2.1 task 1 |
| 1.1.2.3 | T | Create a SIEM query to detect specific process activity | 1.1.2.1 task 2 |

## Concepts taught

- process activity (also: process events, process logs)
- process create / terminate
- PID, name, and command line
- parent-child process
- integrity / user context
- hashes and original filename
- process access (Sysmon Event ID 10)
- Sysmon 1 / 5 / 10 and DeviceProcessEvents

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.1.1 – Endpoint activity (the map)](../01-endpoint-activity/student-guide.md)

Next: [1.1.3 – File System Activity](../03-file-system-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceProcessEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
