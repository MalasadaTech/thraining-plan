# Module 3.8.1 – Identifying Additional Adversary Infrastructure from Seed Indicators

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.8.1 A / B / B · 3.8.1.1 1a / 2b / 3c  
- Hunter: 3.8.1 B / C / C · 3.8.1.1 3c / 4c / 4d  
- CTI: 3.8.1 B / C / C · 3.8.1.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain a **pivot**: start from a **seed**, follow a **shared property**, name **additional infrastructure**.
2. Pick a **data source** that can earn that hop (without re-teaching the source).
3. **Pivot** from a seed and **cite** the link.
4. **Reject** a weak hop (shared CDN / cloud /24) and an **uncited** vendor name.

**Mapped Proficiency Items:**
- K: 3.8.1 – Identifying additional adversary infrastructure from seed indicators
- T: 3.8.1.1 – Pivot from a seed indicator to additional adversary infrastructure

---

## 1. Key Concepts

**3.7.4** already recorded DTF IDs from this seed (`nightowl-updates.net`). This hour writes the **generic hop sentence** — no PTA/P IDs required. You already know how to read RDAP (**3.5**), SOA/NS (**3.6**), and when Silent Push is the right tool (**3.3.2**). Do not re-open those lessons.

Applicable TTPs are **3.8.2**. Broader IOC handling is **3.8.3**. “Does this matter to Harbor?” is **3.8.4**. VT Relations *depth* is **3.9**. A finished actor profile is **3.11**.

**Pivoting (outline a):**

| Term | Meaning |
|------|---------|
| **Seed** | The indicator you start with (here: `nightowl-updates.net`) |
| **Shared property** | NS set, SOA MNAME/RNAME, historical A, TIP sighting |
| **Additional infra** | Another **domain / IP / host** you can cite |
| **Stop** | One cited hop this hour unless the card already gives the second name |

A group name is not infrastructure. A T-ID is not infrastructure. A cloud CIDR is not “theirs.”

**Common sources (outline b) — classroom set. Not a catalog.**

| Source | Shared property | Taught | Use here |
|--------|-----------------|--------|----------|
| **RDAP** | Nameservers, created, registrar | **3.5** | Same NS on a second name |
| **SOA / NS / TXT** | MNAME + NS stack | **3.6** | Same stack on a second name |
| **PDNS (Silent Push)** | Historical A / sibling | **3.3.2** | Same A on a second name |
| **TIP** | Internal sighting | **3.3.1** | Another Harbor host or name |
| **VT Relations** | Graph of contacted infra | **3.9** | **Not this hour** |

File similarity (**3.4**) finds *samples*, not infra, unless a sample *names* a host — still not the product this hour.

**Classroom cards (this lesson only, not live feeds):**

**Seed:** `nightowl-updates.net` (same classroom name as **3.7.4**).

| Source | What the card shows |
|--------|---------------------|
| RDAP | NS `ns1.cdn-test.net`, `ns2.cdn-test.net`. Registrant redacted. Created 14 days ago. |
| SOA / NS | MNAME `ns1.cdn-test.net`. RNAME `hostmaster.cdn-test.net`. Same NS pair. TXT `harbor-verify=nightowl`. |
| PDNS | `nightowl-updates.net` A `203.0.113.88`. **`login-nightowl.net` A `203.0.113.88`**. |
| SOA on the sibling | `login-nightowl.net`: **same** MNAME + NS. No TXT. |
| TIP | `WS-JLEE` GET to the seed. No other Harbor host yet. |
| Cloud | IP org Example Cloud LLC. `203.0.113.0/24` has many tenants. |

**Pivot line:**  
`seed | source | shared property | additional infra | why not a coincidence`

**In the product:** “From `nightowl-updates.net`: `login-nightowl.net` (same MNAME+NS and same A `203.0.113.88`).” Not “Night Owl APT.” Not the whole /24.

| This lesson | Other |
|-------------|-------|
| Seed → cited hop → additional name/IP | DTF ID line — **3.7.4** |
| Use RDAP / SOA / PDNS *results* | How to read those fields — **3.5** / **3.6** / **3.3.2** |
| Not applicable TTPs | **3.8.2** |
| Not VT Relations depth | **3.9** |
| Not nation-state | **3.1.7** / **3.11** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Sibling name on same MNAME+NS **and** same A | Shared Cloudflare NS = “theirs” |
| Cite the shared property | Vendor `evil-c2.net` with no link |
| Stop at the cited hop | Entire Example Cloud /24 as adversary infra |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Seed → Sibling (Expected)

**Seed:** `nightowl-updates.net`.  
**Sources:** SOA/NS (**3.6** card) + PDNS (this card).  
**Shared:** MNAME `ns1.cdn-test.net` + NS pair **and** A `203.0.113.88`.  
**Additional infra:** `login-nightowl.net`.  
**Why not coincidence:** two independent properties, not a public CDN NS alone.  
**Product:** the sentence in §1. Do not add T1486. Do not name a group.

### Example 2: Shared Cloud / Public NS (Lead)

**Draft:** “Example Cloud `203.0.113.0/24` is Night Owl infrastructure.”  
**Or:** “Anything on `ns1.cloudflare.com` is theirs.”

**Fail.** Popular NS and cloud CIDRs are **shared**. RDAP org = hosting, not the actor (**3.5**).  
**Lead:** Weak pivot. Need a *distinctive* stack (MNAME+NS, unique TXT, same A *plus* that stack).

### Example 3: Uncited Vendor Name (Lead)

**Draft:** Copy `evil-c2.net` from the vendor PDF into “additional infra.”

**Fail.** No shared property on the classroom cards. Same rule as uncited T1486 (**3.7.1**) and a weak / invented DTF pivot (**3.7.4**).  
**Lead:** Additional infra is **evidence-bound**.

---

## 3. Hands-On Exercise

**Objective:** Pivot from the seed. Reject weak and uncited hops.

**Use only the classroom cards above.**

**Instructions:**

1. One sentence each for Examples 1–3: supported vs fail.
2. **Pivot** (task): write a **pivot line** for each.

   - A. Seed `nightowl-updates.net` → what additional name, from which source, sharing what?  
   - B. “Same /24 as `203.0.113.88`” as additional infra.  
   - C. `login-nightowl.net` on the same A **and** same MNAME+NS.  
   - D. Vendor line “they also use `evil-c2.net`” — not on any card.  
   - E. “Write the Night Owl actor profile from this hop.”

3. Write the **product hop sentence** for A/C only.
4. Do not extract applicable TTPs (**3.8.2**). Do not write DTF PTA/P IDs (**3.7.4**). Do not open VT Relations (**3.9**). Do not assign a 3.1.7 confidence letter.
5. Empty hop is allowed. Guessing is not.

**Expected Outcome:**
- Three example summaries
- Five pivot lines (B, D, E fail or refuse)
- One product sentence
- No TTP list, no actor profile

---

## 4. Knowledge Check

1. What is a **pivot**, in one sentence?
2. Name **two** data sources that can earn an infra hop, and what shared property each gives you.
3. Why is a shared **cloud /24** not additional adversary infrastructure?
4. Why is a vendor domain with **no shared property** not a hop?
5. Where do you decide which **TTPs apply to Harbor**?

---

## 5. Summary

- Seed → shared property → cited additional name/IP. Weak public NS / cloud CIDR stays out.
- Use RDAP, SOA/NS, PDNS, TIP as *sources*. Do not re-teach them. Do not open 3.9.
- Next: **3.8.2** Extracting applicable TTPs from intelligence reports.

---

## 6. References & Further Reading

- Related modules:
  - 3.7.4 – DTF (PTA/P ID line)
  - 3.5.1 – RDAP / WHOIS
  - 3.6.1 – SOA / advanced DNS
  - 3.3.2 – Silent Push / PDNS
  - 3.8.2 – Applicable TTPs (next)
- Classroom cards in this guide (lesson-only)
