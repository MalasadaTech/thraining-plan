# Hashing and Similarity Concepts

**Path:** `modules/02-cti/05-enrichment/02-file-similarity`  
**Primary role:** CTI Analyst  
**Secondary:** Threat Hunter, SOC Analyst  
**Time:** about 20–25 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|---|---|---|---|---|
| 2.5.2 | K | Hashing and similarity concepts (imphash, ssdeep, TLSH, code-signing certificates) | A / A / B | A / B / B | B / C / C |
| 2.5.2.1 | T | Use file similarity hashes to identify related samples | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 2.5.2.2 | T | Extract and interpret certificate / code-signing information from a file | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4c |

The teaching-unit ID is **2.5.2**. MD5/SHA identity hashes are **1.2.7**. Platform/file-pivot depth is **2.4**. TLS certificates are **1.2.4**. Attribution is **2.1.8**. Classroom similarity thresholds are instructional stand-ins, not universal operational policy.

## Concepts taught

- exact identity versus file similarity
- imphash as a PE import-structure pivot
- ssdeep fuzzy-hash comparison
- TLSH locality-sensitive comparison
- interpreting similarity scores without treating them as proof of relationship
- code-signing signer / subject, issuer, validity, and verification status
- evidence boundaries for signed and unsigned files

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty

## Revision status

The canonical student guide, instructor guide, and slide deck are aligned to the explanatory voice used in Modules 2.1–2.4. The lesson now treats similarity techniques as discovery and triage pivots rather than family or attribution verdicts, clarifies the opposite score directions of ssdeep and TLSH, and explains code-signing as certificate identity/integrity evidence rather than a trust label.


## Supporting references

- [Mandiant — Tracking Malware with Import Hashing](https://cloud.google.com/blog/topics/threat-intelligence/tracking-malware-import-hashing)
- [ssdeep — Getting Started](https://ssdeep-project.github.io/ssdeep/usage.html)
- [Trend Micro — TLSH](https://github.com/trendmicro/tlsh)
- [Microsoft — Authenticode Digital Signatures](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/authenticode)
