# TLS Engine

**Path:** `modules/01-soc/02-zeek/04-tls-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.2.4.1 | K | TLS engine | 1.2.6 a–f | A / B / C | B / C / C | A / A / B |
| 1.2.4.2 | T | Analyze a Zeek TLS log and accurately describe what occurred | 1.2.7 task 1 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.4.3 | T | Create a SIEM query to detect specific TLS activity | 1.2.7 task 2 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |

Zeek writes this data to the `ssl` log. Teaching-unit ID is **1.2.4**. Outline headings `1.2.6` / `1.2.7` are the K/T pair. DNS is **1.2.3**. HTTP is **1.2.5**. No lab.

## Concepts taught

- `ssl` log (Zeek TLS engine)
- SNI (`server_name`)
- certificate subject / issuer
- JA3 / JA3S (where available)
- TLS version and cipher suite
- source and destination fields in TLS logs

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty
