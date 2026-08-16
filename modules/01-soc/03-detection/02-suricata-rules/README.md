# Suricata Rules

**Path:** `modules/01-soc/03-detection/02-suricata-rules`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** 60–75 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.3.2.1 | K | Suricata rules | 1.3.3 a–d |
| 1.3.2.2 | T | Analyze an existing Suricata rule and describe what it detects | 1.3.4 task 1 |
| 1.3.2.3 | T | Create or modify a basic Suricata rule | 1.3.4 task 2 |

The teaching-unit ID is **1.3.2**. Outline headings `1.3.3` / `1.3.4` are the K/T pair. SIGMA is **1.3.1**. YARA is **1.3.3**. How a Suricata hit becomes a SIEM alert is **1.4**. SOC create/modify is **1a / 2b / 3c** (propose, do not deploy).

## Concepts taught

- Suricata rules
- Suricata rule structure (action, header, options)
- Suricata rule options (`content`, `http.*`, `tls.*`)
- matching techniques: ASCII, hex, and regex
- how Suricata rules relate to Zeek / network logs

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — lesson-specific images (empty)
