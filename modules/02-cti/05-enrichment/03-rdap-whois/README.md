# RDAP and WHOIS Concepts

**Path:** `modules/02-cti/05-enrichment/03-rdap-whois`  
**Primary role:** CTI Analyst  
**Secondary:** Threat Hunter, SOC Analyst  
**Time:** about 20–25 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|---|---|---|---|---|
| 2.5.3 | K | RDAP and WHOIS concepts | A / A / B | A / B / B | B / C / C |
| 2.5.3.1 | T | Query RDAP/WHOIS and interpret fields for enrichment or attribution | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4c |

The teaching-unit ID is **2.5.3**. Advanced DNS is **2.5.4**. External tool survey is **0.7**. Attribution is **2.1.8**. No lab.

## Concepts taught

- purpose and limits of registration data
- RDAP as the modern structured registration-data protocol
- legacy WHOIS and where it may still appear
- registrar, registrant/entity, registry, and network-holder roles
- domain registration events and nameservers
- redacted/nonpublic registration information
- IP-network registration and hosting-provider attribution limits
- nameservers as candidate pivots rather than proof of common control

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty

## Supporting references

- [ICANN — Launching RDAP; Sunsetting WHOIS](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en)
- [RFC 9082 — RDAP Query Format](https://www.rfc-editor.org/rfc/rfc9082.html)
- [RFC 9083 — RDAP JSON Responses](https://www.rfc-editor.org/rfc/rfc9083.html)
- [RFC 3912 — WHOIS Protocol Specification](https://www.rfc-editor.org/rfc/rfc3912.html)

## Revision status

The canonical student guide, instructor guide, and slide deck are aligned to the explanatory voice used in Modules 2.1–2.5.2. The lesson now reflects the 2025 gTLD transition to RDAP, treats WHOIS as a legacy access method rather than the default, and separates registration relationships from actor attribution.
