# Module 2.4.5 – Silent Push

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.5 B / C / C ; 2.4.5.1 3c / 4c / 4d  
- Hunter: 2.4.5 A / B / B ; 2.4.5.1 2b / 3c / 4c  
- SOC: 2.4.5 A / A / B ; 2.4.5.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## How to use this platform guide

**Orientation now (about 5 minutes):** retrieve an instructor-provided result, identify the queried seed, returned record type, and observation window, and state one limitation. The first pass is about finding and recording evidence.

**Application with [2.5.4](../../05-enrichment/04-advanced-dns/student-guide.md):** return to the detailed concepts, worked example, and knowledge check below when studying DNS records and historical relationships. The lesson's total estimated time includes both passes; this is one lesson delivered in two parts. Complete its platform performance check during the application pass.

## Learning Objectives

By the end of this module, you will be able to:

1. Use Silent Push passive-DNS data to enrich a domain or IP with historical DNS observations.
2. Pivot from a seed to candidate infrastructure using record-specific PADNS relationships while considering time, hosting density, and distinctiveness.

**Mapped Proficiency Items:**
- K: 2.4.5 – Silent Push
- T: 2.4.5.1 – Enrich an indicator and pivot in Silent Push

## 1. Key Concepts

Silent Push provides passive-DNS and infrastructure intelligence that can help analysts examine how domains and IP addresses have been associated over time.

References:
- [Silent Push – DNS Data](https://help.silentpush.com/docs/dns-data)
- [Silent Push – Passive DNS and Record-Specific Lookups](https://help.silentpush.com/v1/docs/perform-passive-dns-scans-and-record-specific-lookups)

Current Silent Push documentation supports forward and reverse PADNS lookups across record types including A, AAAA, CNAME, MX, NS, TXT, and SOA.

### Passive DNS is historical observation

Authoritative DNS tells you what a zone publishes when queried.

**Passive DNS (PADNS)** stores observations of DNS relationships seen over time.

That lets an analyst ask questions such as:
- Which IPs has this domain resolved to?
- Which domains have been observed on this IP?
- Which domains share a nameserver?
- How did those relationships change over time?

A PADNS association means the relationship was **observed by the provider's data collection**. It is not proof that the relationship existed everywhere or for the entire time window.

### Time matters

Infrastructure changes.

A domain that resolved to one address in January may resolve somewhere else in October.

When comparing two objects, record or consider:
- first/last seen;
- overlapping time window;
- whether the relationship is historical or current;
- whether the hosting environment is shared.

Two domains using the same IP five years apart are a weaker relationship than two suspicious domains co-resolving to a rare IP during the same campaign window.

### Forward and reverse pivots

**Forward-style question**
> What addresses or DNS answers have been observed for this domain?

**Reverse-style question**
> What domains or records have been observed pointing to this address or server?

Silent Push also supports record-specific queries, so the analyst can pivot on more than just A records.

### Density and shared hosting matter

An IP with hundreds or thousands of unrelated domains is less distinctive than an address hosting a small, suspicious cluster.

Likewise, a common managed nameserver is weaker evidence than a rare nameserver associated with a tight group of domains.

Silent Push can help identify candidate relationships, but **provider data does not remove the need for contextual judgment**.

### A12 example

Seed: `203.0.113.88`

Classroom result shows:
- update domain observed on the IP during the A12 period;
- `login-prd.net` observed on the same IP during an overlapping period;
- many unrelated hosts elsewhere in the larger cloud range.

A defensible result is:

> Silent Push PADNS shows the update domain and `login-prd.net` associated with `203.0.113.88` during overlapping time periods; `login-prd.net` is a candidate related domain.

A weak conclusion is:

> The entire `203.0.113.0/24` belongs to the actor.

### Enrich first, then pivot

A useful workflow:

1. Query the seed.
2. Review observed record relationships and time.
3. Identify candidate related objects.
4. Ask how common the shared value is.
5. Compare additional records or independent sources.
6. Promote the relationship only as strongly as the evidence supports.

## 2. Knowledge Check

1. What is the difference between authoritative DNS and passive DNS?
2. Why does overlapping time matter when two domains share an IP?
3. Silent Push shows `login-prd.net` on the same IP as the update domain during the same period. What is the strongest first conclusion?

## 3. Summary

Silent Push helps reconstruct historical DNS relationships and find candidate infrastructure.

Use time, hosting density, record type, and distinctiveness to judge the relationship. A PADNS association is evidence of an observed DNS relationship—not automatic proof of common ownership.


## Supporting References

- [Silent Push – DNS Data](https://help.silentpush.com/docs/dns-data)
- [Silent Push – Passive DNS and Record-Specific Lookups](https://help.silentpush.com/v1/docs/perform-passive-dns-scans-and-record-specific-lookups)

**Next:** [2.4.6 – urlscan.io](../06-urlscan/student-guide.md).
