# TLS Engine

**Path:** `modules/01-soc/02-zeek/04-tls-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

TLS can conceal application content while leaving some handshake information visible. Reading that information carefully helps describe the observed session without treating a hostname, certificate, or fingerprint as a verdict.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.2.4.1 | K | TLS engine | 1.2.6 a–f |
| 1.2.4.2 | T | Analyze a Zeek TLS log and accurately describe what occurred | 1.2.7 task 1 |
| 1.2.4.3 | T | Create a SIEM query to detect specific TLS activity | 1.2.7 task 2 |

## Concepts taught

- TLS / ssl log (also: TLS events, TLS logs)
- SNI (`server_name`)
- certificate subject / issuer
- JA3 / JA3S (where available)
- TLS version
- cipher suite
- source and destination fields in TLS logs

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.2.3 – DNS Engine](../03-dns-engine/student-guide.md)

Next: [1.2.5 – HTTP Engine](../05-http-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — ssl.log](https://docs.zeek.org/en/current/reference/logs/ssl.html)
- [Zeek — x509.log](https://docs.zeek.org/en/current/reference/logs/x509.html)
