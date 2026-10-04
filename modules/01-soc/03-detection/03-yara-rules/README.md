# YARA Rules

**Path:** `modules/01-soc/03-detection/03-yara-rules`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

YARA examines content supplied to a scanner, such as a file or process memory. Understanding what bytes and conditions a rule tests helps you distinguish a content match from a filename, log entry, or conclusion about maliciousness.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.3.3.1 | K | YARA rules | 1.3.5 a–d | A / B / C | B / C / C | A / B / B |
| 1.3.3.2 | T | Analyze an existing YARA rule and describe what it detects | 1.3.6 task 1 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 2b / 3c |
| 1.3.3.3 | T | Create or modify a basic YARA rule | 1.3.6 task 2 | 1a / 2b / 3c | 2b / 3c / 4c | 1a / 1a / 2b |

## Concepts taught

- YARA rules
- YARA rule structure
- YARA strings and conditions
- matching techniques: ASCII, hex, and regex (YARA)
- how YARA is used with files / memory

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.3.2 – Suricata Rules](../02-suricata-rules/student-guide.md)

Next: [1.3.4 – SIEM Rules](../04-siem-rules/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [YARA — Writing rules](https://yara.readthedocs.io/en/stable/writingrules.html)
- [YARA — Command-line input options](https://yara.readthedocs.io/en/stable/commandline.html)
