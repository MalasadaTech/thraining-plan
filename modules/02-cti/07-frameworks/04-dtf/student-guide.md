# Module 2.7.4 – Defender’s ThreatMesh Framework (DTF)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.4 B / C / C ; 2.7.4.1 3c / 4c / 4d ; 2.7.4.2 3c / 4c / 4d ; 2.7.4.3 3c / 4c / 4c  
- Hunter: 2.7.4 A / B / B ; 2.7.4.1 1a / 2b / 3c ; 2.7.4.2 1a / 2b / 3c ; 2.7.4.3 1a / 2b / 3c  
- SOC: 2.7.4 A / A / B ; 2.7.4.1 1a / 1a / 2b ; 2.7.4.2 1a / 1a / 2b ; 2.7.4.3 1a / 1a / 2b  
**Estimated Time:** 25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why DTF exists, and pick a **real** PTA + P ID from a seed.
2. Cite the shared characteristic, reject the weak neighbor, name the **next lookup**, and say how DTF differs from ATT&CK / Diamond / Kill Chain.

**Mapped Proficiency Items:**
- K: 2.7.4 – DTF for infrastructure discovery
- T: 2.7.4.1 – Apply DTF: select a pivot and reject the weak neighbor
- T: 2.7.4.2 – Use a selected DTF pivot to guide the next lookup
- T: 2.7.4.3 – Explain how DTF complements ATT&CK, Diamond, and Kill Chain

---

## 1. Key Concepts

DTF is MalasadaTech’s **defender discovery** matrix. It finds **more infrastructure** from a known-bad seed and records the pivot. There is **no score**. Do not invent `P` codes. Do not assign T-IDs (**2.7.1**). The generic hop sentence without IDs is **2.8.1**.

| Tactic | Name | Pivot on |
|--------|------|----------|
| **PTA0001** | Domain | Registration, string, DNS |
| **PTA0002** | IP | Reverse, proximity, AS |
| **PTA0003** | SSL | Issuer / SAN (only if a cert card exists) |
| **PTA0004** | Application | HTTP title / resources (only if a page card exists) |

Pivots nest: `P0101` Registration → `P0101.010` Name Server.

**Seed:** update domain / `203.0.113.88` / sibling `login-prd.net` / NS `ns1.cdn-test.net`.

| Evidence | ID | Call |
|----------|-----|------|
| Same NS | **PTA0001 / P0101.010** | Take if NS is distinctive |
| Same A | **PTA0001 / P0103.003** | Take → sibling |
| Whole `203.0.113.0/24` | **PTA0002 / P0202** | **Reject** — shared cloud |
| Vendor APT / T-ID | — | **No DTF ID** |

**Next lookup:** the P-ID names what to ask next (RDAP for NS = **2.5**; SOA RNAME = **2.6**; PDNS same A = **0.7** / **2.9.3**). This hour **names** that lookup.

**Complement:** ATT&CK = behavior. Diamond = know/don’t-know. Kill Chain = progression. DTF = discovery pivots. Same shape. Different job.

**Line:** `seed | PTA | P-ID | characteristic | candidate | why not coincidence`

---

## 2. Knowledge Check

1. DTF replaces ATT&CK. True or false?
2. Same NS on the update domain and `login-prd.net`. PTA / P-ID, or reject?
3. Whole `203.0.113.0/24`. Take or reject, and what is the next lookup if you took same-A instead?

---

## 3. Summary

Real PTA/P only. Cite the characteristic. Reject shared cloud. Name the next lookup. DTF does not replace the other three.

**Next:** **2.8.1** Infrastructure hop sentence.

---

## 4. Related modules

- 2.7.3 – Kill Chain (previous)
- 2.8.1 – Generic hop (no P-ID)
- 2.5 / 2.6 / 0.7 – The lookups DTF names
- [DTF](https://github.com/MalasadaTech/defenders-threatmesh-framework)
