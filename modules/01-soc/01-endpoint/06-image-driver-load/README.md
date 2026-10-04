# Image and Driver Load Activity

**Path:** `modules/01-soc/01-endpoint/06-image-driver-load`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

An image-load event shows a module being loaded into a process. A driver-load event concerns code loaded into the kernel. Understanding the difference helps you describe the execution context without confusing a file on disk with a recorded load.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.1.6.1 | K | Image and driver load activity concepts | 1.1.6 a–d |
| 1.1.6.2 | T | Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred | 1.1.6.1 task 1 |
| 1.1.6.3 | T | Create a SIEM query to detect specific image or driver load activity | 1.1.6.1 task 2 |

## Concepts taught

- image and driver load activity
- user-mode image load vs kernel driver load
- path, hashes, signed vs unsigned
- initiating process (image load)
- Sysmon 6 / 7 and DeviceImageLoadEvents

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.1.5 – Registry Activity](../05-registry-activity/student-guide.md)

Next: [1.2.1 – Zeek Concepts](../../02-zeek/01-concepts/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceImageLoadEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceimageloadevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
