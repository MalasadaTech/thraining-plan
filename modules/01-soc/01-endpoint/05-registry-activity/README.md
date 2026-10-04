# Registry Activity

**Path:** `modules/01-soc/01-endpoint/05-registry-activity`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

Registry events record changes to Windows configuration. Reading the key, value name, value data, and initiating process separately helps explain exactly what changed and what follow-up evidence would be useful.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.1.5.1 | K | Registry activity concepts | 1.1.5 a–e |
| 1.1.5.2 | T | Analyze a registry event (Sysmon or MDE) and accurately describe what occurred | 1.1.5.1 task 1 |
| 1.1.5.3 | T | Create a SIEM query to detect specific registry operations | 1.1.5.1 task 2 |

## Concepts taught

- registry activity
- hives and key → value
- registry set / delete / rename
- common persistence locations (Run, Services)
- initiating process (registry events)
- Sysmon 12 / 13 / 14 and DeviceRegistryEvents

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.1.4 – Network Activity (Endpoint)](../04-network-activity/student-guide.md)

Next: [1.1.6 – Image and Driver Load Activity](../06-image-driver-load/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceRegistryEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceregistryevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
