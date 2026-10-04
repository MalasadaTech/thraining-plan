# Advanced DNS Concepts

**Path:** `modules/02-cti/05-enrichment/04-advanced-dns`  
**Primary role:** CTI Analyst  
**Secondary:** Threat Hunter, SOC Analyst  
**Time:** about 20–25 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|---|---|---|---|---|
| 2.5.4 | K | Advanced DNS concepts (SOA and other records of intel value) | A / A / B | B / C / C | B / C / C |
| 2.5.4.1 | T | Interpret an SOA record and use advanced DNS data to enrich or pivot | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4d |

The teaching-unit ID is **2.5.4**. Zeek DNS is **1.2.3**. RDAP is **2.5.3**. External/passive-DNS tools are introduced in **0.7**. No lab.

## Concepts taught

- authoritative DNS versus registration and observed/passive DNS
- SOA MNAME, RNAME, and SERIAL
- RNAME mailbox encoding
- SOA serial as a zone version rather than a hash or guaranteed timestamp
- NS, A/AAAA, CNAME, MX, TXT, and SRV as infrastructure-enrichment records
- distinctiveness and evidentiary weight of shared DNS infrastructure
- candidate pivots versus proof of common ownership/control
- avoiding subnet-ownership claims from one shared address

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty

## Supporting references

- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html)
- [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html)
- [RFC 2782 — SRV Resource Record](https://www.rfc-editor.org/rfc/rfc2782.html)

## Revision status

The canonical student guide, instructor guide, and slide deck are aligned to the explanatory voice used in Modules 2.1–2.5.3. The lesson now uses the RFC definitions for SOA fields and treats shared DNS infrastructure as a weighted pivot rather than automatic proof of shared control.
