# Files Engine

**Path:** `modules/01-soc/02-zeek/07-files-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

Zeek file analysis connects observed network content to the flow that carried it. It can help explain a download or attachment, while the available fields also show whether hashes or extracted bytes exist for further examination.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.2.7.1 | K | Files engine | 1.2.12 a–e | A / B / C | B / C / C | A / A / B |
| 1.2.7.2 | T | Analyze a Zeek files log and accurately describe what occurred | 1.2.13 task 1 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.7.3 | T | Create a SIEM query to detect specific file transfer activity | 1.2.13 task 2 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |

## Concepts taught

- `files` log
- filename (files log)
- MIME type
- files-log hashes (MD5, SHA1, SHA256)
- current endpoint / `is_orig` fields and legacy `tx_hosts` / `rx_hosts`
- current `uid` and legacy `conn_uids` (links to other Zeek logs)

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.2.6 – SMTP Engine](../06-smtp-engine/student-guide.md)

Next: [1.2.8 – Weird Engine](../08-weird-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — files.log](https://docs.zeek.org/en/current/reference/logs/files.html)
