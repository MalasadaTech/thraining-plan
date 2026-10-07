# Module 2.5.4 – Advanced DNS Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.4 B / C / C ; 2.5.4.1 3c / 4c / 4d  
- Hunter: 2.5.4 B / C / C ; 2.5.4.1 2b / 3c / 4c  
- SOC: 2.5.4 A / A / B ; 2.5.4.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret the key fields of an **SOA** record, especially MNAME, RNAME, and SERIAL.
2. Use authoritative DNS records such as NS, MX, TXT, and SRV to enrich a domain and identify **candidate pivots** without treating shared infrastructure as proof of common ownership or control.

**Mapped Proficiency Items:**
- K: 2.5.4 – Advanced DNS concepts (SOA and other records of intelligence value)
- T: 2.5.4.1 – Interpret an SOA record and use advanced DNS data to enrich or pivot

## 1. Key Concepts

This lesson focuses on **authoritative DNS data**: records published for a DNS zone.

That is different from:
- a Zeek `dns` log showing that a host made a DNS query;
- passive DNS history showing how resolutions changed over time; or
- registration data from RDAP.

Authoritative DNS tells you what the zone currently publishes. Those records can expose infrastructure relationships worth investigating, but the strength of the relationship depends on how distinctive the shared record is.

### SOA: the zone's authority record

The **Start of Authority (SOA)** record contains management parameters for a zone.

[RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html) defines several fields. This lesson focuses on three:

| Field | Meaning | Analytic use |
|---|---|---|
| **MNAME** | Domain name of the name server that is the original or primary source of data for the zone. | Identifies the server named as the zone's primary source in the SOA record. |
| **RNAME** | Domain-name encoding of the mailbox of the person responsible for the zone. | Provides an administrative/responsible mailbox value. |
| **SERIAL** | Unsigned 32-bit version number of the zone data. | Helps identify that the published zone version changed; it is not a file hash or guaranteed timestamp. |

The full SOA also contains REFRESH, RETRY, EXPIRE, and MINIMUM fields, which control aspects of zone transfer and caching behavior.

### Reading RNAME correctly

RNAME is written in DNS-name form rather than ordinary email notation.

For a simple value such as:

`hostmaster.cdn-test.net.`

the conventional mailbox rendering is:

`hostmaster@cdn-test.net`

The conversion can involve escaped dots in more complicated local parts, so treat the field as a DNS-encoded mailbox rather than assuming every dot has the same meaning.

RNAME tells you the mailbox published in the SOA record. It does not prove that the mailbox owner is the malicious operator.

### SERIAL is a version, not a clock

The SOA SERIAL is the zone's version number. Operators often choose serial formats that resemble dates, but DNS does not require the serial to be a timestamp.

A changed serial can support the statement:

> The zone version changed between the two observations.

It cannot automatically support:

> The domain was modified at exactly the date encoded in this number.

The serial is also not a cryptographic hash.

### Other DNS records that support enrichment

| Record | What it represents | Potential intelligence value |
|---|---|---|
| **NS** | Authoritative name servers for a zone or delegation. | Candidate pivot to other names using the same distinctive DNS infrastructure. |
| **MX** | Mail exchanger for the domain. | Can expose related mail-host infrastructure. |
| **TXT** | Arbitrary published text. | Unique verification tokens or unusual strings may provide pivots; common SaaS tokens may be weak signals. |
| **SRV** | Location of a named service, including target host and port. | Can expose additional hostnames associated with a service. |
| **A / AAAA** | IPv4 / IPv6 address for a hostname. | Useful infrastructure context, but shared hosting can make the relationship weak. |
| **CNAME** | Alias pointing to a canonical name. | Can reveal hosting or service-provider relationships. |

NS, A/AAAA, and other record meanings are defined in the core DNS specifications, including [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html) and [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html). SRV is defined in [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782.html).

### Shared DNS records create candidates, not automatic siblings

Suppose the A12 update domain and `login-prd.net` share:

- `ns1.cdn-test.net`;
- `ns2.cdn-test.net`; and
- A record `203.0.113.88`.

That is useful. But the correct first conclusion is:

> `login-prd.net` is a candidate related domain because it shares multiple DNS infrastructure features with the update domain.

The strength of that relationship depends on context.

If the nameservers belong to a huge managed-DNS provider and the IP is shared hosting, the overlap may be weak. If the nameserver pair is rare, the address is unusual, registration timing is similar, and additional records also match, the case becomes stronger.

DNS pivots are most reliable when **multiple independent, distinctive features converge**.

### Keep Infrastructure Claims at the Scope the DNS Evidence Supports

If two domains resolve to `203.0.113.88`, that supports a relationship involving that address at the observed time.

It does not establish that the threat actor controls all of `203.0.113.0/24`.

The previous RDAP lesson may tell you who the network is registered to. DNS tells you which address the name publishes or resolves to. Neither fact alone establishes ownership of the larger block by the actor.

### A practical pivot workflow

Start with the A12 update domain.

1. **Read the SOA.** Record MNAME, RNAME, SERIAL, and any relevant timing fields.
2. **Collect useful records.** NS, A/AAAA, CNAME, MX, TXT, or SRV as appropriate.
3. **Normalize the values.** Compare hostnames, addresses, and tokens consistently.
4. **Identify candidate pivots.** Look for other names sharing distinctive values.
5. **Ask how common the feature is.** A public DNS provider is weaker than rare infrastructure.
6. **Corroborate.** Combine DNS with registration data, timing, internal telemetry, passive DNS, or other evidence before asserting shared control.

This workflow turns DNS into a disciplined source of hypotheses rather than a shortcut to ownership claims.

### Paired platform application

Return to [Silent Push](../../04-platforms/05-silent-push/student-guide.md). Compare a supplied authoritative record with a passive-DNS result. Record the type, value, source, and query/observation time, then identify a candidate relationship whose time window is relevant.

Keep the result with the enrichment record started in [2.5.1](../01-ioc-handling/student-guide.md).

## 2. Knowledge Check

1. What do MNAME, RNAME, and SERIAL mean in an SOA record?
2. The SOA serial changes from one observation to the next. What can you safely infer, and what should you avoid assuming?
3. Two domains share the same NS pair and A address. What is a defensible first conclusion, and what additional questions determine whether the relationship is strong?

## 3. Summary

Authoritative DNS records describe the zone and the services it publishes.

SOA MNAME identifies the named primary source of zone data, RNAME encodes the responsible mailbox, and SERIAL is the zone version. NS, A/AAAA, CNAME, MX, TXT, and SRV records can expose useful infrastructure relationships.

Shared DNS values are **pivots**, not automatic proof of common ownership. Stronger infrastructure analysis comes from combining distinctive DNS overlaps with independent registration, timing, telemetry, or historical evidence.


## 4. Related Modules

- 2.5.3 – RDAP / WHOIS (previous)
- 2.3.1 – ATT&CK for CTI
- 1.2.3 – Zeek DNS / DGA
- 0.7 – External tool survey / passive DNS
- 2.5.5 – Infrastructure pivoting

## Supporting References

- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) — explains zones, authoritative servers, and NS/SOA roles.
- [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) — defines SOA fields and core DNS resource records.
- [RFC 2782 — A DNS RR for Specifying the Location of Services (SRV)](https://www.rfc-editor.org/rfc/rfc2782.html) — defines SRV records.

**Next:** [2.5.5 – Identifying Additional Adversary Infrastructure from Seed Indicators](../05-infra-pivot/student-guide.md).
