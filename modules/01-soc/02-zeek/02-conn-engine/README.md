# Conn Engine

**Path:** `modules/01-soc/02-zeek/02-conn-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

A connection record gives you a network-level starting point: the endpoints, transport, and progress Zeek observed. That description helps you select the related protocol records without assigning a purpose to the traffic too early.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.2.2.1 | K | Conn engine | 1.2.2 a–e | A / B / C | B / C / C | A / A / B |
| 1.2.2.2 | T | Analyze a Zeek conn log and accurately describe what occurred | 1.2.3 task 1 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.2.3 | T | Create a SIEM query to detect specific connection activity | 1.2.3 task 2 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |

## Concepts taught

- `conn` log (also: `conn` event, connection log)
- `id.orig_h` / `id.orig_p` (originator / source)
- `id.resp_h` / `id.resp_p` (responder / destination)
- `conn_state` / `history`

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.2.1 – Zeek Concepts](../01-concepts/student-guide.md)

Next: [1.2.3 – DNS Engine](../03-dns-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html)
