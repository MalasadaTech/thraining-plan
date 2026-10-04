# Module 2.5.3 – RDAP and WHOIS Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.3 B / C / C ; 2.5.3.1 3c / 4c / 4c  
- Hunter: 2.5.3 A / B / B ; 2.5.3.1 2b / 3c / 4c  
- SOC: 2.5.3 A / A / B ; 2.5.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain what RDAP and legacy WHOIS registration data are used for and how the two access methods differ.
2. Query a domain or IP registration record, extract useful fields, and interpret those fields without turning registration data into unsupported attribution.

**Mapped Proficiency Items:**
- K: 2.5.3 – RDAP and WHOIS concepts
- T: 2.5.3.1 – Query RDAP/WHOIS and interpret fields for enrichment or attribution

## 1. Key Concepts

Registration data helps an analyst answer questions such as:

- Which registrar maintains this domain?
- Which registry or Regional Internet Registry (RIR) is authoritative for the record?
- What nameservers are listed?
- When was the domain registered or last changed?
- Which organization is listed for an IP network?
- Which contact or entity information is publicly available?

Those facts are useful for enrichment, but registration data has an important limit: **it tells you what the registration system records about the name or network block. It does not, by itself, tell you who is operating malicious activity through that infrastructure.**

### RDAP is the modern structured protocol

The **Registration Data Access Protocol (RDAP)** is the modern IETF-standard protocol for retrieving registration data. RDAP uses HTTP/HTTPS and structured JSON responses, which makes fields easier for software and analysts to interpret consistently.

For generic top-level domains (gTLDs), ICANN made RDAP the definitive source for registration data on **January 28, 2025**, replacing the contractual requirement for registrar and registry WHOIS services.

**WHOIS** is the older registration-data protocol defined around free-text responses over TCP port 43. WHOIS still exists in some registries, RIRs, tools, archives, and operational environments, so analysts should understand how to read it. But it should be treated as a **legacy access method**, not as the preferred modern standard.

| Feature | RDAP | Legacy WHOIS |
|---|---|---|
| Transport | HTTP / HTTPS | TCP port 43 |
| Response | Structured JSON | Primarily free text |
| Field consistency | Defined object structure | Varies by server and operator |
| Modern role | Preferred / standardized registration access | Legacy and environment-dependent |
| Useful to analysts | Easier parsing, links, notices, events, entities | Historical familiarity and fallback where still offered |

### Registration roles are not interchangeable

Several names can appear in a registration record, and they describe different roles.

**Registry** — operates the authoritative database for a top-level domain or address-registration system.

**Registrar** — the company through which a domain registration is managed.

**Registrant / entity** — the person or organization associated with the registration when that information is available.

**RIR / network holder** — the organization to which an IP address range is registered or allocated.

These are not actor labels. A registrar can serve millions of unrelated customers. A cloud provider can hold the IP block used by many unrelated tenants.

### Useful domain fields

For a domain, useful RDAP/WHOIS fields commonly include:

- **registrar**;
- **domain status**;
- **registration / creation date**;
- **last changed / updated date**;
- **expiration date**, when exposed;
- **nameservers**;
- **entities / contacts**, when public;
- **remarks and notices**, which may explain redaction or policy.

If contact information is redacted or unavailable, record that accurately. **Redacted registration data is not the same thing as an empty lookup.** Other fields may still provide useful context.

### Useful IP-network fields

For an IP address, an RDAP lookup can lead to the registered network object. Useful fields may include:

- start and end address or CIDR/netblock;
- network handle or name;
- organization / entity;
- registration service;
- country or administrative metadata when present;
- remarks, notices, and abuse contacts.

If `203.0.113.88` falls inside a network registered to **Example Cloud**, the defensible statement is:

> The address is within a network registered to Example Cloud.

That is not the same as:

> Example Cloud conducted the activity.

Hosting and cloud providers routinely host unrelated customers.

### Nameservers are useful context, not automatic clustering proof

Nameservers can be useful pivots, especially when they are unusual or appear alongside other shared infrastructure. But the evidentiary value depends on **distinctiveness**.

Two domains using the same large managed-DNS provider may tell you very little. Two domains sharing a rare nameserver pair, a rare address, similar registration timing, and other independent characteristics present a stronger case for further investigation.

Treat a shared nameserver as a **candidate pivot**, not a finished attribution.

### Worked example: the A12 update domain

Suppose the RDAP record for the update domain shows:

- registrar: Example Registrar;
- nameservers: `ns1.cdn-test.net` and `ns2.cdn-test.net`;
- registration event: a recent creation date;
- registrant details: not publicly disclosed.

A useful enrichment line would be:

> RDAP lists Example Registrar and the nameservers `ns1.cdn-test.net` and `ns2.cdn-test.net`; registrant details are not publicly disclosed.

That statement preserves what the record actually says.

If another domain, `login-prd.net`, uses the same nameserver pair, that is a reason to examine the domain more closely. It is not enough by itself to call the domains the same infrastructure cluster or attribute them to the same actor.

### Worked example: the A12 IP

Suppose an RDAP lookup for `203.0.113.88` returns a network object covering `203.0.113.0/24` and identifies **Example Cloud** as the network holder.

Useful enrichment:

> `203.0.113.88` is within `203.0.113.0/24`, a network registered to Example Cloud.

Evidence boundary:

> The registration establishes the network holder, not the operator of the specific malicious activity and not ownership of the entire block by the threat actor.

### Paired platform application

Return to [platform selection](../../04-platforms/02-platform-selection/student-guide.md). Use an approved registration service or the supplied registration record. Identify the entity role, relevant dates, and redacted or unavailable fields. Record one useful lead and one conclusion the registration data cannot support.

Keep the result with the enrichment record started in [2.5.1](../01-ioc-handling/student-guide.md).

## 2. Knowledge Check

1. Why is RDAP generally preferable to legacy WHOIS for modern registration-data access?
2. A domain's registrant information is redacted, but the registrar, nameservers, and registration events are present. What useful intelligence remains?
3. `203.0.113.88` belongs to a network registered to a cloud provider. What can you state from that record, and what would be unsupported attribution?

## 3. Summary

RDAP and WHOIS provide registration data, not actor identity. RDAP is the modern structured protocol; WHOIS is a legacy access method that may still appear in some environments.

Extract the fields that are actually present, preserve redaction as a fact, and distinguish registrar, registrant, and network holder from the operator of malicious activity. Registration data is most useful when it becomes one line of evidence in a larger enrichment or infrastructure analysis.


## 4. Related Modules

- 2.5.2 – Hashing and similarity concepts (previous)
- 2.5.4 – Advanced DNS
- 0.7 – External tool survey
- 2.1.8 – Attribution

## Supporting References

- [ICANN — Launching RDAP; Sunsetting WHOIS](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en) — explains the January 2025 gTLD transition to RDAP as the definitive registration-data source.
- [RFC 9082 — RDAP Query Format](https://www.rfc-editor.org/rfc/rfc9082.html) — defines RDAP query structure.
- [RFC 9083 — RDAP JSON Responses](https://www.rfc-editor.org/rfc/rfc9083.html) — defines the structured JSON response model.
- [RFC 3912 — WHOIS Protocol Specification](https://www.rfc-editor.org/rfc/rfc3912.html) — documents the legacy WHOIS protocol.

**Next:** [2.5.4 – Advanced DNS Concepts](../04-advanced-dns/student-guide.md).
