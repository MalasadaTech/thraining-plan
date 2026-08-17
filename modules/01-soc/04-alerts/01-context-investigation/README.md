# Alert Context and Investigation

**Path:** `modules/01-soc/04-alerts/01-context-investigation`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 30 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.4.1.1 | K | Alert context and investigation | 1.4.1 a–e | A / B / C | B / C / C | A / A / B |
| 1.4.1.2 | T | Review an alert and identify which context is present and which is missing | 1.4.1.1 task 1 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.3 | T | Review the alert configuration and explain what would fire | 1.4.1.1 task 2 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.4 | T | Trace an alert to its upstream detection logic and name each hop | 1.4.1.1 task 3 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.5 | T | Collect related endpoint logs and state what they add (or fail to add) | 1.4.1.1 task 4 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 1a |
| 1.4.1.6 | T | Collect related PCAP and state what it adds versus the alert fields | 1.4.1.1 task 5 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 1a |

The teaching-unit ID is **1.4.1**. Detection authoring is **1.3**. Classification is **1.4.2**. First alert is the process create. VirusTotal on a hash, IP, or domain you have is part of context (**0.7**). Not Relations (**3.9**). No lab.

## Concepts taught

- alert context (present vs missing)
- VirusTotal lookup (hash, IP, or domain) as alert context
- alert configuration (what would fire)
- upstream alerting hops
- related endpoint logs for an alert
- related PCAP versus alert fields

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty
