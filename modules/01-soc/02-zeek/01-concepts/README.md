# Zeek Concepts

**Path:** `modules/01-soc/02-zeek/01-concepts`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 15–20 minutes

## Purpose

Network-sensor evidence describes traffic visible at an observation point. Zeek turns that traffic into structured records that analysts can search and connect. Understanding how those records are produced helps you choose the right log and recognize when additional evidence is needed.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.2.1.1 | K | Zeek concepts | 1.2.1 a–d | A / B / C | B / C / C | A / B / B |

## Concepts taught

- Zeek as a network analysis framework
- Zeek analyzers and scripts produce structured observations
- engines surface applications and protocols
- PCAP can verify or expand observations when relevant traffic is available

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.1.6 – Image and Driver Load Activity](../../01-endpoint/06-image-driver-load/student-guide.md)

Next: [1.2.2 – Conn Engine](../02-conn-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — Log files](https://docs.zeek.org/en/master/reference/zeekscript/log-files.html)
- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html)
