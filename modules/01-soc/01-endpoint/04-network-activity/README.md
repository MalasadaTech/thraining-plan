# Network Activity (Endpoint)

**Path:** `modules/01-soc/01-endpoint/04-network-activity`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

Endpoint network events connect network activity to a process on a device. That process context can help explain a connection that a network sensor sees only as traffic between addresses.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.1.4.1 | K | Network activity (endpoint) concepts | 1.1.4 a–e |
| 1.1.4.2 | T | Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred | 1.1.4.1 task 1 |
| 1.1.4.3 | T | Create a SIEM query to detect specific endpoint network activity | 1.1.4.1 task 2 |

## Concepts taught

- network activity (endpoint) (also: host-network events, endpoint network logs)
- source / dest IP and port, protocol, direction
- domain / URL (endpoint-logged)
- initiating process (endpoint network)
- Sysmon 3 / 22 and DeviceNetworkEvents
- host-observed vs Zeek

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.1.3 – File System Activity](../03-file-system-activity/student-guide.md)

Next: [1.1.5 – Registry Activity](../05-registry-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceNetworkEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicenetworkevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
