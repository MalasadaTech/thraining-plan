# TLS Engine

**Path:** `modules/01-soc/02-zeek/04-tls-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.2.4.1 | K | TLS engine | 1.2.6 a–f |
| 1.2.4.2 | T | Analyze a Zeek TLS log and accurately describe what occurred | 1.2.7 task 1 |
| 1.2.4.3 | T | Create a SIEM query to detect specific TLS activity | 1.2.7 task 2 |

The teaching-unit ID is **1.2.4**. Outline headings `1.2.6` / `1.2.7` are the K/T pair. Zeek writes this data to the `ssl` log. DNS is **1.2.3**. HTTP is **1.2.5**. Not decrypted HTTP. Not the process. No lab.

## Concepts taught

- TLS / ssl log (also: TLS events, TLS logs)
- SNI (`server_name`)
- certificate subject / issuer
- JA3 / JA3S (where available)
- TLS version
- cipher suite
- source and destination fields in TLS logs

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty
