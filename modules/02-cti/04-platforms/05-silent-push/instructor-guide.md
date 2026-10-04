# Instructor Guide – Module 2.4.5 – Silent Push

**Estimated Time:** 20–25 minutes

## Two-pass delivery

Spend about 5 minutes here on retrieval and evidence capture: the queried seed, returned record type, and observation window. Use a supplied static result if a live account or permitted query is unavailable. Reserve the remaining stated lesson time and the knowledge check for 2.5.4, alongside DNS records and historical relationships. Do not mark the platform task complete after orientation alone.

Use the first two slides for orientation; use the remaining slides and worked example during the paired method lesson. Reuse the same result in both passes.

## Purpose

Teach learners to use passive DNS as historical infrastructure evidence and to weight pivots by time, density, and distinctiveness.

## Current Capability Note

Silent Push supports forward/reverse passive-DNS analysis and record-specific queries across multiple DNS record types.

References:
- [DNS Data](https://help.silentpush.com/docs/dns-data)
- [PADNS Lookups](https://help.silentpush.com/v1/docs/perform-passive-dns-scans-and-record-specific-lookups)

## Core Distinctions

**Authoritative DNS:** what a zone publishes when queried.  
**Passive DNS:** historical observations collected by a provider.

### Time
Co-occurrence during the same window strengthens a relationship.

### Density
Shared cloud/CDN infrastructure weakens a relationship.

### Provider coverage
A missing PADNS record means it was not present in the provider result—not that it never existed globally.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Treats PADNS as authoritative truth. | Call it provider-observed historical DNS. |
| Ignores time. | Compare first/last seen or overlapping periods. |
| Takes whole netblock. | Ask about hosting density and unrelated tenants. |
| Treats same IP as same actor. | Record candidate relation and seek corroboration. |

## Knowledge Check – Answer Key

1. Authoritative DNS is published zone data; PADNS is provider-collected history of observed DNS relationships.
2. Temporal overlap makes a shared infrastructure relationship more meaningful than unrelated use at distant times.
3. `login-prd.net` is candidate related infrastructure based on a same-IP PADNS association during the relevant period; corroborate further.

## References

- [Silent Push – DNS Data](https://help.silentpush.com/docs/dns-data)
- [Silent Push – PADNS Lookups](https://help.silentpush.com/v1/docs/perform-passive-dns-scans-and-record-specific-lookups)
