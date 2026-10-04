# Suricata Rules

**Path:** `modules/01-soc/03-detection/02-suricata-rules`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

Suricata rules express conditions to inspect in network traffic. Reading the protocol, direction, and inspection buffer helps explain why a signature matched and whether its meaning agrees with the analyst’s description.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.3.2.1 | K | Suricata rules | 1.3.3 a–d | A / B / C | B / C / C | A / B / B |
| 1.3.2.2 | T | Analyze an existing Suricata rule and describe what it detects | 1.3.4 task 1 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 2b / 3c |
| 1.3.2.3 | T | Create or modify a basic Suricata rule | 1.3.4 task 2 | 1a / 2b / 3c | 2b / 3c / 4c | 1a / 1a / 2b |

## Concepts taught

- Suricata rules
- Suricata rule structure (action, header, options)
- Suricata rule options (`content`, `http.*`, `tls.*`)
- matching techniques: ASCII, hex, and regex
- how Suricata rules relate to Zeek / network logs

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.3.1 – SIGMA Rules](../01-sigma-rules/student-guide.md)

Next: [1.3.3 – YARA Rules](../03-yara-rules/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Suricata — Rule format](https://docs.suricata.io/en/latest/rules/intro.html)
- [Suricata — HTTP keywords](https://docs.suricata.io/en/latest/rules/http-keywords.html)
