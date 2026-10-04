# Weird Engine

**Path:** `modules/01-soc/02-zeek/08-weird-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 20–25 minutes

## Purpose

A weird record reports an unexpected condition encountered by Zeek. It is useful because it points to traffic or visibility worth examining, but its meaning depends on the named condition and the surrounding evidence.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.2.8.1 | K | Weird engine | 1.2.14 a–c | A / B / C | B / C / C | A / A / A |
| 1.2.8.2 | T | Analyze a Zeek weird log and accurately describe what occurred | 1.2.15 task 1 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 1a |
| 1.2.8.3 | T | Create a SIEM query to detect specific weird activity | 1.2.15 task 2 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 1a |

## Concepts taught

- `weird` log
- weird activity type (`name`)
- weird `notice` flag
- source and destination (weird)
- `uid` (link to other Zeek logs)

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.2.7 – Files Engine](../07-files-engine/student-guide.md)

Next: [1.3.1 – SIGMA Rules](../../03-detection/01-sigma-rules/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — weird.log and notice.log](https://docs.zeek.org/en/current/reference/logs/weird-and-notice.html)
