# TLS Engine

**Path:** `modules/01-soc/02-zeek/04-tls-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter  
**Time:** 60–75 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.2.4.1 | K | TLS engine | 1.2.6 |
| 1.2.4.2 | T | Analyze a Zeek TLS log and accurately describe what occurred | 1.2.7 |
| 1.2.4.3 | T | Create a SIEM query to detect specific TLS activity | 1.2.7 |

Zeek writes this data to the `ssl` log. The teaching-unit ID is **1.2.4** (matrix). Outline headings `1.2.6` / `1.2.7` are the K/T pair.

## Concepts taught

- `ssl` log (Zeek TLS engine)
- SNI (`server_name`)
- certificate `subject` / `issuer`
- self-signed certificate
- SNI vs certificate mismatch
- missing / empty SNI
- JA3 / JA3S
- TLS version (`TLSv13`, `TLSv12`, `TLSv11`, `TLSv10`, `SSLv3`)
- cipher suite / weak ciphers
- pivoting with `uid` to `conn` and `dns`

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — lesson-specific images (empty)

Reusable Zeek logs belong in `labs/zeek/`, not here.
