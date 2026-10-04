# DNS Engine

**Path:** `modules/01-soc/02-zeek/03-dns-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

DNS evidence connects a question about a name to the response observed on the network. Distinguishing the resolver from the returned address helps prevent a common error when moving from a lookup to a connection investigation.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.2.3.1 | K | DNS engine | 1.2.4 a–d | A / B / C | B / C / C | A / B / B |
| 1.2.3.2 | T | Analyze a Zeek DNS log and accurately describe what occurred | 1.2.5 task 1 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 2b / 3c |
| 1.2.3.3 | T | Create a SIEM query to detect specific DNS activity | 1.2.5 task 2 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 2b / 3c |

## Concepts taught

- `dns` log (also: DNS events, DNS logs)
- DNS query (question)
- DNS response (answer)
- common DNS record types
- source and destination fields in DNS logs

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.2.2 – Conn Engine](../02-conn-engine/student-guide.md)

Next: [1.2.4 – TLS Engine](../04-tls-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — dns.log](https://docs.zeek.org/en/current/reference/logs/dns.html)
