# Instructor Guide – Module 2.5.4 – Advanced DNS Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.4 B / C / C ; 2.5.4.1 3c / 4c / 4d  
- Hunter: 2.5.4 B / C / C ; 2.5.4.1 2b / 3c / 4c  
- SOC: 2.5.4 A / A / B ; 2.5.4.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners interpret authoritative DNS records and use them to generate defensible infrastructure pivots without converting shared hosting or shared DNS providers into unsupported ownership claims.

**Context:** Module 2.5.3 taught registration data. This lesson examines records published by the DNS zone itself. Learners should understand both the semantics of the records and the evidence boundary around infrastructure clustering.

**Technical correction to preserve:** A shared NS pair or shared A record does not automatically mean “same control.” It creates a candidate relationship whose strength depends on how distinctive the shared infrastructure is and what independent evidence corroborates it.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Interpret the key fields of an SOA record, especially MNAME, RNAME, and SERIAL.
2. Use authoritative DNS records such as NS, MX, TXT, and SRV to enrich a domain and identify candidate pivots without treating shared infrastructure as proof of common ownership or control.

**Mapped Proficiency Items:**
- K: 2.5.4 – Advanced DNS concepts (SOA and other records of intelligence value)
- T: 2.5.4.1 – Interpret an SOA record and use advanced DNS data to enrich or pivot

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---:|---|
| Introduction | 3 minutes | Separate authoritative DNS from wire logs and registration. |
| SOA fields | 6 minutes | Interpret MNAME, RNAME, SERIAL, and evidence limits. |
| Other records | 5 minutes | Explain infrastructure value of NS/MX/TXT/SRV/A/CNAME. |
| Pivot reasoning | 5 minutes | Weight distinctiveness and shared-hosting alternatives. |
| A12 example | 3 minutes | Build a candidate relationship without overclaiming. |
| Knowledge check | 3 minutes | Test interpretation and pivot judgment. |
| **Total** | **25 minutes** | Compress discussion slightly if needed. |

## Detailed Teaching Notes

### 1. Separate three different data sources

Write three headings:

- **Registration data** — RDAP / WHOIS.
- **Authoritative DNS** — the zone's published records.
- **Observed DNS activity** — telemetry or passive DNS history.

This lesson owns the middle category.

### 2. Teach SOA from the standard definitions

Use [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html) as the reference.

**MNAME** is the domain name of the name server designated as the original or primary source of zone data.

**RNAME** encodes the mailbox of the person responsible for the zone.

**SERIAL** is the unsigned 32-bit version number of the zone.

Avoid simplifying MNAME to “who runs the zone” or RNAME to “the operator.” Those may be useful clues, but the record's technical meaning is narrower.

### 3. Explain the RNAME mailbox notation

Use `hostmaster.cdn-test.net.` and render it as `hostmaster@cdn-test.net` for the simple classroom example.

Mention that escaped dots can appear in the mailbox local part. The goal is recognition, not a full DNS escaping lesson.

### 4. Correct the serial misconception

A serial that looks like `2026100101` may encode a date by operator convention, but the DNS standard only requires a version number with sequence arithmetic.

Ask learners what a changed serial supports: **the zone version changed**.

It does not guarantee an exact human-readable modification time.

### 5. Teach infrastructure records as weighted evidence

For each record, ask two questions:

1. What infrastructure value does it reveal?
2. How common is that value?

Examples:
- common Cloudflare NS pair → usually weak clustering evidence;
- rare self-hosted NS pair shared by two recent domains → stronger;
- same A on a shared cloud IP → weak by itself;
- same rare TXT token across multiple domains → potentially stronger, but still investigate the token's origin.

### 6. Use the A12 sibling as a candidate, not a verdict

Present `login-prd.net` with the same NS pair and same A as the update domain.

Expected language:

> Candidate related domain based on shared DNS infrastructure; corroboration required.

Then ask what would strengthen the case:
- rare NS pair;
- similar registration timing;
- shared unique TXT/CNAME/MX;
- passive DNS co-movement;
- same certificate or file-delivery behavior;
- internal telemetry linking both names.

### 7. Protect the network-boundary inference

If both names resolve to `203.0.113.88`, the observed relationship is to that address.

The analyst should not claim the entire `/24` belongs to the actor. RDAP may identify the larger block's holder, but that holder can be a shared provider.

## Common Student Challenges

| Misunderstanding | Teaching response |
|---|---|
| SOA MNAME is always the actual human/operator running the zone. | Use the RFC definition: named primary source of zone data. |
| RNAME is an ordinary hostname. | Explain the DNS-encoded mailbox semantics. |
| SERIAL is a timestamp or hash. | Describe it as the zone version; date-like formatting is only a convention. |
| Same NS proves same actor. | Ask how common the DNS provider is and what independent evidence matches. |
| Same A means the actor owns the subnet. | Separate one observed address from registered block ownership. |
| Authoritative DNS is the same as passive DNS history. | Re-establish the three data-source categories. |

## Knowledge Check – Answer Key

### 1. MNAME, RNAME, SERIAL

**Expected answer:** MNAME is the name server designated as the original/primary source of zone data; RNAME is the DNS-encoded responsible mailbox; SERIAL is the zone version number.

### 2. Serial changes

**Expected answer:** The published zone version changed. Do not automatically infer an exact modification timestamp unless a documented operator convention and supporting context justify that interpretation.

### 3. Same NS pair + same A

**Expected answer:** The domains are candidate related infrastructure and merit further investigation. The strength depends on whether the nameservers/address are distinctive or widely shared and whether other evidence—registration timing, unique records, passive DNS, telemetry, etc.—corroborates common control.

## Summary and Transition

Close with: **DNS records create pivots; converging evidence turns pivots into defensible relationships.**

The next module combines the registration and DNS evidence into a justified infrastructure pivot.

## Instructor References

- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html)
- [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html)
- [RFC 2782 — SRV Resource Record](https://www.rfc-editor.org/rfc/rfc2782.html)

## Paired application

Complete the application portion of 2.4.5 with this lesson. Compare a supplied authoritative record with a passive-DNS result. Record the type, value, source, and query/observation time, then identify a candidate relationship whose time window is relevant. Use the existing platform-guide answer key for its knowledge check. Account for the remaining platform time separately from this method lesson; do not repeat the orientation.
