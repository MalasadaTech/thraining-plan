# File System Activity

**Path:** `modules/01-soc/01-endpoint/03-file-system-activity`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

File events help establish what happened to an object on an endpoint and which process performed the operation. Keeping the operation, path, and initiating process together helps distinguish a file arriving from that file later being used.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.1.3.1 | K | File system activity concepts | 1.1.3 a–e | A / B / C | A / B / B | A / A / A |
| 1.1.3.2 | T | Analyze a file event (Sysmon or MDE) and accurately describe what occurred | 1.1.3.1 task 1 | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.3.3 | T | Create a SIEM query to detect specific file operations | 1.1.3.1 task 2 | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |

## Concepts taught

- file system activity (also: file events, file logs)
- file create / rename-move / delete / modify / read
- path, name, and extension
- file hashes
- initiating process (file events)
- Sysmon 11 / 23 / 26 and DeviceFileEvents

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.1.2 – Process Activity](../02-process-activity/student-guide.md)

Next: [1.1.4 – Network Activity (Endpoint)](../04-network-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceFileEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicefileevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
