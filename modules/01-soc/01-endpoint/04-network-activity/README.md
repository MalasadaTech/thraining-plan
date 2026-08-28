# Network Activity (Endpoint)

**Path:** `modules/01-soc/01-endpoint/04-network-activity`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.1.4.1 | K | Network activity (endpoint) concepts | 1.1.4 a–e |
| 1.1.4.2 | T | Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred | 1.1.4.1 task 1 |
| 1.1.4.3 | T | Create a SIEM query to detect specific endpoint network activity | 1.1.4.1 task 2 |

The teaching-unit ID is **1.1.4**. File activity is **1.1.3**. Registry is **1.1.5**. Zeek is **1.2**. Not Sysmon install or config. No lab.

## Concepts taught

- network activity (endpoint) (also: host-network events, endpoint network logs)
- source / dest IP and port, protocol, direction
- domain / URL (endpoint-logged)
- initiating process (endpoint network)
- Sysmon 3 / 22 and DeviceNetworkEvents
- host-observed vs Zeek

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty
