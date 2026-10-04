# Module 2.5.5 – Identifying Additional Adversary Infrastructure from Seed Indicators

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.5 B / C / C ; 2.5.5.1 3c / 4c / 4d  
- Hunter: 2.5.5 B / C / C ; 2.5.5.1 3c / 4c / 4d  
- SOC: 2.5.5 A / B / B ; 2.5.5.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Pivot from a known seed to a **candidate** infrastructure object and write a concise hop sentence that preserves the shared evidence.
2. Judge whether the shared characteristic is distinctive enough to pursue and identify the source class that would support the next enrichment step.

**Mapped Proficiency Items:**
- K: 2.5.5 – Identifying additional adversary infrastructure from seed indicators
- T: 2.5.5.1 – Pivot from a seed indicator to additional adversary infrastructure

## 1. Key Concepts

Infrastructure pivoting begins with a **seed**: a domain, IP address, certificate, hostname, or other infrastructure object already connected to the intelligence problem.

A pivot uses one characteristic of that seed to find another object worth investigating.

The key word is **candidate**. A shared nameserver, address, certificate field, or page characteristic can reveal potentially related infrastructure, but the pivot itself does not prove common ownership or adversary control.

### The hop sentence

This course records one pivot with:

`seed | shared characteristic | candidate | why the relationship is worth pursuing`

Example:

> `update-domain | uncommon NS pair ns1/ns2.cdn-test.net | login-prd.net | same uncommon authoritative NS pair; corroborate with registration and DNS history`

This sentence captures the reasoning without requiring the DTF PTA/P identifiers taught in 2.5.6.

### Distinctiveness matters

Not every shared value has the same evidentiary weight.

**Stronger candidate pivots** tend to involve characteristics that are:
- relatively uncommon;
- specific enough to identify a small set of infrastructure;
- observed close in time; or
- supported by more than one independent feature.

**Weaker pivots** often involve:
- large public DNS providers;
- CDN or shared-hosting addresses;
- broad cloud netblocks;
- common certificate issuers;
- generic HTTP titles.

The right question is not simply, “Do these objects share something?”

It is:

> **How surprising is it that unrelated infrastructure would share this characteristic?**

### Common source classes

| Source class | Useful pivot information |
|---|---|
| **Registration / RDAP** | Registrar, registration events, nameservers, public entities |
| **Authoritative DNS** | NS, A/AAAA, CNAME, MX, TXT, SOA values |
| **Passive / historical DNS** | Other names associated with an address or changes over time |
| **TLS certificate data** | SAN names, subject, issuer, serial/fingerprint, validity |
| **HTTP / application data** | Titles, favicons, resources, headers, page fingerprints |

The detailed mechanics belong to the earlier or later tool lessons. Here, the analyst selects the source class that can test the pivot.

For registration context, see the [ICANN RDAP transition guidance](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en). For authoritative DNS semantics, see [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html).

### Worked A12 example

Seed: A12 update domain  
Known address: `203.0.113.88`  
Known nameservers: `ns1.cdn-test.net`, `ns2.cdn-test.net`

Candidate: `login-prd.net`

If `login-prd.net` shares the same uncommon NS pair, that is a reasonable candidate hop.

If it also resolves to the same address during the relevant time window, the relationship becomes more interesting because two different features converge.

A defensible hop sentence is:

> `update-domain | uncommon NS pair + same observed A | login-prd.net | multiple shared infrastructure features; investigate further`

That is stronger than:

> `203.0.113.88 is inside 203.0.113.0/24, so the whole /24 is adversary infrastructure.`

The second statement expands one observation into ownership of a shared range without enough evidence.

### One hop should lead to a testable next step

After writing the hop, identify what would strengthen or weaken it.

Examples:
- shared NS → search for other domains using that NS and compare registration timing;
- shared IP → check historical DNS and hosting density;
- shared certificate SAN → inspect whether the certificate is unique or mass-issued;
- shared HTTP title → determine whether the title is distinctive or generic.

The purpose of the pivot is not to collect an ever-growing graph. It is to generate a **defensible candidate relationship** that the next lookup can test.

### Paired platform application

Return to [Silent Push](../../04-platforms/05-silent-push/student-guide.md) and [urlscan.io](../../04-platforms/06-urlscan/student-guide.md). Use the retained DNS result and a supplied browser-scan result to propose one infrastructure hop. Separate page-controlled or distinctive features from common third-party services. Record the seed, shared characteristic, candidate, reason to pursue, and next lookup.

Keep the result with the enrichment record started in [2.5.1](../01-ioc-handling/student-guide.md).

## 2. Knowledge Check

1. What four parts belong in the course's hop sentence?
2. The update domain and `login-prd.net` share a large public DNS provider. Is that enough to call them related infrastructure? What would make the relationship stronger?
3. Why is “same `/24`” weaker than “same uncommon NS pair plus same observed A address” in the A12 example?

## 3. Summary

A pivot starts with a known seed and produces a candidate.

Record the seed, the shared characteristic, the candidate, and why the relationship deserves investigation. Weight the pivot by **distinctiveness**, and use the next lookup to test whether the relationship survives scrutiny.


## Supporting References

- [Defender's ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework) – the formal pivot-ID framework taught in 2.5.6.
- [ICANN – Launching RDAP; Sunsetting WHOIS](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en)
- [RFC 1035 – Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html)

**Next:** [2.5.6 – MalasadaTech Defender's ThreatMesh Framework (DTF)](../06-dtf/student-guide.md).
