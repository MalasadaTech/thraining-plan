# SMTP Engine

**Path:** `modules/01-soc/02-zeek/06-smtp-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

SMTP records describe mail transactions visible to a network sensor. They help identify envelope addresses and selected headers while leaving mailbox delivery, user action, and attachment behavior to other evidence.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.2.6.1 | K | SMTP engine | 1.2.10 a–e | A / B / C | B / C / C | A / A / B |
| 1.2.6.2 | T | Analyze a Zeek SMTP log and accurately describe what occurred | 1.2.11 task 1 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.6.3 | T | Create a SIEM query to detect specific SMTP activity | 1.2.11 task 2 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |

## Concepts taught

- `smtp` log
- mail from
- rcpt to
- SMTP subject
- message ID
- source and destination fields in SMTP logs

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.2.5 – HTTP Engine](../05-http-engine/student-guide.md)

Next: [1.2.7 – Files Engine](../07-files-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — smtp.log](https://docs.zeek.org/en/current/reference/logs/smtp.html)
