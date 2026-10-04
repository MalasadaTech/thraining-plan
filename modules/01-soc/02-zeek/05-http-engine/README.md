# HTTP Engine

**Path:** `modules/01-soc/02-zeek/05-http-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

An HTTP record helps explain what a client requested and what response status the sensor observed. Separating request details, server response, and any transferred content makes the resulting account more precise.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.2.5.1 | K | HTTP engine | 1.2.8 a–f |
| 1.2.5.2 | T | Analyze a Zeek HTTP log and accurately describe what occurred | 1.2.9 task 1 |
| 1.2.5.3 | T | Create a SIEM query to detect specific HTTP activity | 1.2.9 task 2 |

## Concepts taught

- http log (also: HTTP events, HTTP logs)
- HTTP method
- HTTP host
- URI / URL
- User-Agent
- HTTP status code
- source and destination fields in HTTP logs

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.2.4 – TLS Engine](../04-tls-engine/student-guide.md)

Next: [1.2.6 – SMTP Engine](../06-smtp-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
