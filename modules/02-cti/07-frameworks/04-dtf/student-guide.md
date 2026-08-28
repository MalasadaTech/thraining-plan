# Module 2.7.4 – MalasadaTech Defender's ThreatMesh Framework (DTF)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.4 B / C / C ; 2.7.4.1 3c / 4c / 4d ; 2.7.4.2 3c / 4c / 4d ; 2.7.4.3 3c / 4c / 4c  
- Hunter: 2.7.4 A / B / B ; 2.7.4.1 1a / 2b / 3c ; 2.7.4.2 1a / 2b / 3c ; 2.7.4.3 1a / 2b / 3c  
- SOC: 2.7.4 A / A / B ; 2.7.4.1 1a / 1a / 2b ; 2.7.4.2 1a / 1a / 2b ; 2.7.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why DTF exists, and pick a **real** pivot tactic (PTA) and pivot (P) ID from a known-bad seed.
2. Cite the shared characteristic, reject the weak neighbor, name the **next lookup**, and say how DTF differs from ATT&CK, Diamond, and Kill Chain.

**Mapped Proficiency Items:**
- K: 2.7.4 – Defender’s ThreatMesh Framework (DTF) for infrastructure discovery
- T: 2.7.4.1 – Apply DTF: select a pivot tactic and pivot from a seed and reject the weak neighbor
- T: 2.7.4.2 – Use a selected DTF pivot to guide the next enrichment or lookup
- T: 2.7.4.3 – Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain

---

## 1. Key Concepts

CTI analysts start from a **known-bad seed** — a domain, IP, certificate, or page they already treat as adversary infrastructure. The job is to find **more** of that infrastructure and write the pivot so another analyst can run it again. That is the job in this lesson: pick a real DTF ID, cite the shared characteristic, reject the weak neighbor, and name the next lookup. DTF does **not** score the pivot. It does **not** replace ATT&CK, Diamond, or Kill Chain.

**DTF** (Defender's ThreatMesh Framework) is MalasadaTech's **defender discovery** matrix. It is shaped like ATT&CK: **pivot tactics** are columns; **pivots** are the named cells. The job is discovery, not behavior.

| Tactic | Name | Pivot on |
|--------|------|----------|
| **PTA0001** | Domain | Registration, domain string, DNS |
| **PTA0002** | IP | Reverse lookup, proximity, AS |
| **PTA0003** | SSL | Issuer / SAN — only if a cert card exists |
| **PTA0004** | Application | HTTP title / resources — only if a page card exists |

Pivots nest. **P0101** is Registration. **P0101.010** is Registration: Name Server. Use only IDs that exist in DTF. Do not invent a `P` code. Do not teach every P-code. Do not assign ATT&CK T-IDs here (**2.7.1**). The generic hop sentence without DTF IDs is **2.8.1**.

**Seed:** the update domain and its A record `203.0.113.88`. Candidate sibling `login-prd.net`. Name server `ns1.cdn-test.net`.

DTF finds related infrastructure when the candidate **shares a characteristic** with the seed: registration, domain string, DNS, IP, SSL, or HTTP. Same name server or same A can be a take when that fact is distinctive. A whole cloud `/24` is coincidence, not a take.

| Evidence | ID | Call |
|----------|-----|------|
| Same NS | **PTA0001 / P0101.010** (Registration: Name Server) | Take if the NS is distinctive |
| Same A | **PTA0001 / P0103.003** (DNS: IP Address) | Take → sibling |
| Whole `203.0.113.0/24` | **PTA0002 / P0202** (Proximity) | **Reject** — shared cloud |
| Vendor APT / T-ID | — | **No DTF ID** |

The selected P-ID **names** the next lookup. It does not run that tool in this lesson.

| Selected pivot | Next lookup to name |
|----------------|---------------------|
| **P0101.010** Name Server | RDAP / WHOIS for that NS (**2.5**) |
| **P0103.004** DNS: SOA RName | SOA RNAME (**2.6**) |
| **P0103.003** DNS: IP Address | Passive DNS / other names on that A (**0.7** / **2.9.3**) |

**Complement:** ATT&CK labels **behavior**. Diamond shows **know / don’t-know**. Kill Chain shows **progression**. DTF records **discovery** pivots. Same matrix shape. Different job.

**What good looks like:** someone gives you a seed and a shared fact. You write the **DTF ID line**. You do not tell the rest of the incident.

`seed | PTA | P-ID | characteristic | candidate | why not coincidence`

- Given: same NS `ns1.cdn-test.net` on the update domain and `login-prd.net`. **Take:** **PTA0001 / P0101.010**. Cite the distinctive name server (not a public resolver). Candidate `login-prd.net`. Next lookup: RDAP for that NS.
- Given: both names resolve to `203.0.113.88`. **Take:** **PTA0001 / P0103.003**. Next lookup: passive DNS / other names on that A.
- Given: whole `203.0.113.0/24`. **Reject** **P0202**. Shared cloud is not “theirs.”

Do not score the line. Do not invent `P9999`. Do not write T1059 as a DTF pivot.

---

## 2. Knowledge Check

1. DTF replaces ATT&CK. True or false?
2. Same NS on the update domain and `login-prd.net`. Which PTA / P-ID, or reject?
3. Whole `203.0.113.0/24`. Take or reject, and what is the next lookup if you took same-A instead?

---

## 3. Summary

DTF is defender discovery. Use a real PTA and P ID. Cite the characteristic. Reject shared cloud. Name the next lookup. DTF does not replace ATT&CK, Diamond, or Kill Chain.

**Next:** **2.8.1** Infrastructure hop sentence.

---

## 4. Related modules

- 2.7.3 – Cyber Kill Chain in intelligence analysis (previous)
- 2.8.1 – Generic hop sentence (no P-ID)
- 2.5 / 2.6 / 0.7 – The lookups DTF names
- [Defender's ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework)
