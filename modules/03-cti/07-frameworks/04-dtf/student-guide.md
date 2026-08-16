# Module 3.7.4 – Defender’s ThreatMesh Framework (DTF)

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.7.4 A / A / B · 3.7.4.1 1a / 1a / 2b · 3.7.4.2 1a / 1a / 2b · 3.7.4.3 1a / 1a / 2b  
- Hunter: 3.7.4 A / B / B · 3.7.4.1 1a / 2b / 3c · 3.7.4.2 1a / 2b / 3c · 3.7.4.3 1a / 2b / 3c  
- CTI: 3.7.4 B / C / C · 3.7.4.1 3c / 4c / 4d · 3.7.4.2 3c / 4c / 4d · 3.7.4.3 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State **why DTF exists**: discover **additional adversary infrastructure** from a known-bad seed, and **communicate / record** the pivot.
2. Name the **four pivot tactics** and pick a **real** `PTA` + `P` ID.
3. **Apply** that ID: cite the shared characteristic, name the candidate, **reject** the weak neighbor.
4. Use the selected ID to **name the next lookup** — do not re-teach RDAP/SOA/PDNS, and do not invent a score.
5. Explain how DTF **complements** ATT&CK, Diamond, and Kill Chain.

**Mapped Proficiency Items:**
- K: 3.7.4 – Defender’s ThreatMesh Framework (DTF) for infrastructure discovery
- T: 3.7.4.1 – Apply DTF: select a pivot tactic and pivot from a seed and reject the weak neighbor
- T: 3.7.4.2 – Use a selected DTF pivot to guide the next enrichment or lookup
- T: 3.7.4.3 – Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain

---

## 1. Key Concepts

DTF is MalasadaTech’s **defender discovery** matrix ([defenders-threatmesh-framework](https://github.com/MalasadaTech/defenders-threatmesh-framework)). It is **inspired by ATT&CK** (tactic → technique IDs) and **discovery only**. There is **no scoring methodology**. Do not invent `P` codes. Do not assign T-IDs here (**3.7.1**).

**Purpose (outline a):** From *known-bad* infrastructure, pick a pivot, cite the shared characteristic, name **candidate additional infra** (or the next lookup). Also: communicate the pivot to another analyst and record it for a recurring check.

**Components (outline b) — real IDs; survey all four tactics:**

| Pivot tactic | Name | What you pivot on |
|--------------|------|-------------------|
| **PTA0001** | Domain | Registration, domain string, DNS |
| **PTA0002** | IP | Reverse lookup, proximity, AS |
| **PTA0003** | SSL | Issuer, SAN, not-before (named this hour; apply only if a cert card exists) |
| **PTA0004** | Application | HTTP title / resources (named this hour; apply only if a page card exists) |

Pivots nest like ATT&CK techniques: `P0101` Registration → `P0101.010` Name Server.

**Related infra from a seed (outline c) — classroom apply set (real IDs only).** Seed: `nightowl-updates.net` / `203.0.113.88` / sibling `login-nightowl.net` / NS `ns1.cdn-test.net` (same cards as **3.5 / 3.6 / 3.8.1**).

| Evidence | DTF ID | Call |
|----------|--------|------|
| Same NS `ns1.cdn-test.net` | **PTA0001 / P0101.010** | Take if NS is distinctive |
| Substring `nightowl` | **PTA0001 / P0102.002** | Take → `login-nightowl.net` |
| Same A `203.0.113.88` | **PTA0001 / P0103.003** | Take |
| SOA RNAME `hostmaster.cdn-test.net` | **PTA0001 / P0103.004** | Take **with** NS (stack) |
| Reverse of the IP | **PTA0002 / P0201** | Take only if a PTR is on the card; else **not on card** |
| Whole `203.0.113.0/24` | **PTA0002 / P0202** | **Reject** — shared cloud |
| AS / org Example Cloud | **PTA0002 / P0203** | Hosting context, not “theirs” |
| Vendor T1486 / “APT” | — | **No DTF ID** — not infrastructure |

**Next lookup (outline d):** The ID tells you *what to ask next* — RDAP for NS (**3.5**), SOA RNAME (**3.6**), PDNS same A (**3.3.2 / 3.9.3**). This hour **names** that lookup. The generic hop sentence without PTA/P IDs is **3.8.1**. Do not re-teach those tools.

**Complement (outline e):**

| Framework | Owns | DTF does **not** |
|-----------|------|------------------|
| **ATT&CK (3.7.1)** | Adversary *behavior* (T-IDs) | Assign T-IDs |
| **Diamond (3.7.2)** | Know / don’t-know vertices | Fill Adversary |
| **Kill Chain (3.7.3)** | Ordered stages | Relabel Delivery / Installation |
| **DTF** | Defender *discovery* pivots | Score, prioritize defense, or replace the other three |

Same ATT&CK-like *shape*. Different job.

**DTF line:**  
`seed | PTA | P-ID | shared characteristic | candidate infra | why not coincidence`

**Lookup line:**  
`P-ID | next lookup (tool/field) | what you hope to learn`

| This lesson | Other |
|-------------|-------|
| Real PTA/P + characteristic | Generic hop — **3.8.1** |
| Do not re-teach RDAP/SOA/SP | **3.5 / 3.6 / 3.9.3** |
| Not T-IDs / Diamond / stages | **3.7.1–3.7.3** |
| Not hIGMA | Out of this hour |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| P0101.010 + P0102.002 + P0103.003 → `login-nightowl.net` | Entire /24 as P0202 “theirs” |
| Distinctive NS + substring | Invented `P9999` or T1486 as a DTF ID |
| Name the next lookup | Re-scoring mesh+recency+reach |

---

## 2. Detailed Walkthrough / Examples

**Seed (Night Owl):** `nightowl-updates.net` A `203.0.113.88`; NS `ns1.cdn-test.net` / `ns2.cdn-test.net`; SOA RNAME `hostmaster.cdn-test.net`; sibling `login-nightowl.net` same A. Vendor PDF lists T1486 and “Night Owl APT.” No PTR on the classroom card.

### Example 1: Distinctive Domain Pivots (Expected)

**DTF line:** `nightowl-updates.net | PTA0001 | P0101.010 + P0102.002 + P0103.003 | distinctive NS + substring nightowl + same A | login-nightowl.net | two+ distinctive properties`  
**Lookup line:** `P0101.010 → RDAP NS; P0103.003 → PDNS same A; P0103.004 → SOA RNAME (stack with NS)`  
**Not:** a score. **Not:** the 3.8.1 hop sentence without IDs.

### Example 2: /24 as P0202 (Lead)

**Draft:** PTA0002 / P0202 / P0203 — every name on `203.0.113.0/24` or in Example Cloud is Night Owl.

**Fail.** Proximity and AS are **shared hosting**. Same reject as **3.8.1**.  
**Lead:** Weak neighbor. 4d is *why* NS+substring beats /24.

### Example 3: Not Infrastructure (Lead)

**Draft A:** T1486 / “APT” as a DTF pivot.  
**Draft B:** Invent `P9999`.

**Fail.** DTF IDs are for **infra characteristics**. Behavior IDs are **3.7.1**. Blank is better than a minted P-code.  
**Lead:** Real IDs only.

---

## 3. Hands-On Exercise

**Objective:** Apply real DTF IDs. Name the next lookup. Reject /24 and non-infra.

**Use only the classroom apply table. Real IDs only.**

**Instructions:**

1. One sentence each for Examples 1–3: take vs fail.
2. **Apply** (3.7.4.1): write a **DTF line** for each.

   - A. Same NS `ns1.cdn-test.net`.  
   - B. Substring `nightowl` → `login-nightowl.net`.  
   - C. Same A `203.0.113.88`.  
   - D. Whole `203.0.113.0/24`.  
   - E. Vendor T1486 / “Night Owl APT.”

3. **Lookup** (3.7.4.2): for A–C only, one **lookup line** each (RDAP NS / SOA RNAME / PDNS A). Do not run the query.
4. **Complement** (3.7.4.3): one sentence each — DTF vs ATT&CK, vs Diamond, vs Kill Chain.
5. Do not invent P-codes. Do not assign T-IDs. Do not fill Diamond. Do not pick a Kill Chain stage. Do not open Silent Push / VT Relations.

**Expected Outcome:**
- Three example summaries
- Five DTF lines (D and E fail)
- Three lookup lines
- Three complement sentences
- No score, no invented ID

---

## 4. Knowledge Check

1. What is DTF **for**, in one sentence?
2. What must a **DTF line** include besides a P-ID?
3. Why is the **cloud /24** a weak P0202?
4. What does a selected DTF ID tell you to do **this hour** — and what does it **not** tell you to do?
5. Give one way DTF **complements** ATT&CK, Diamond, **or** Kill Chain without replacing it.

---

## 5. Summary

- Real PTA/P. Cite the characteristic. Reject the weak neighbor. Name the next lookup. No score.
- Next: **3.8.1** generic infra hop (no DTF IDs required).

---

## 6. References & Further Reading

- Related modules:
  - 3.7.3 – Kill Chain in CTI (previous)
  - 3.7.1 – ATT&CK for CTI
  - 3.7.2 – Diamond in CTI
  - 3.8.1 – Generic infra hop (next)
  - 3.5.1 / 3.6.1 / 3.9.3 – RDAP / SOA / Silent Push
- [Defender’s ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework) (lookup; do not copy here)
- Classroom apply table in this guide (Night Owl IOCs only — IDs are real)
