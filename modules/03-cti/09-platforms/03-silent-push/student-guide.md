# Module 3.9.3 – Silent Push

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.9.3 A / A / B · 3.9.3.1 1a / 1a / 2b  
- Hunter: 3.9.3 A / B / B · 3.9.3.1 2b / 3c / 4c  
- CTI: 3.9.3 B / C / C · 3.9.3.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State Silent Push **capabilities** that matter for intel (PDNS, first/last seen, siblings, NS cluster).
2. **Enrich** an indicator *in Silent Push* (not by re-reading SOA/RDAP).
3. **Pivot** to additional infrastructure and **cite** the Silent Push field.
4. **Reject** the cloud /24 and using Silent Push as a sandbox.

**Mapped Proficiency Items:**
- K: 3.9.3 – Silent Push
- T: 3.9.3.1 – Enrich an indicator and pivot in Silent Push

---

## 1. Key Concepts

**3.3.2** taught *when* Silent Push is the tool (domain/IP **history**). **3.8.1** taught the *idea* of a hop. **3.6** taught SOA fields. This hour is **the Silent Push record**: enrich, then pivot *inside* that UI.

VT Relations is **3.9.1**. URLScan is *this page load* (**3.9.4**). RDAP created/registrar is **3.5**.

**Capabilities (outline a) — classroom set:**

| Capability | Intel use | Not |
|------------|-----------|-----|
| **PDNS / resolutions** | Historical A, first/last seen | Live page screenshot |
| **Sibling / related names** | Other names on the same A or NS | “Related” with no field |
| **NS cluster** | Names sharing `ns1.cdn-test.net` | Public CDN NS as “theirs” |
| **Risk / score** | A *hint* to look closer | A verdict or attribution |

**Enrich + pivot (outline b):** enrich = fill the Silent Push fields for the seed. Pivot = follow **one cited field** to another name/IP.

**Classroom Silent Push cards (this lesson only):**

**Seed:** `nightowl-updates.net`

| Field | Value |
|-------|--------|
| Current A | `203.0.113.88` |
| First seen (A) | 2026-08-01 |
| Last seen | this window |
| NS | `ns1.cdn-test.net`, `ns2.cdn-test.net` |
| Siblings on same A | **`login-nightowl.net`** (first seen 2026-08-10) |
| Same /24 | many Example Cloud tenants |
| Same public CDN NS | (none — this NS is distinctive *on the card*) |

**Enrich line:** `indicator | A / first-seen / NS | what that tells you | what you must not claim`  
**Pivot line:** `seed | Silent Push field | additional infra | why not coincidence`

| This lesson | Other |
|-------------|-------|
| SP fields + in-tool hop | When to pick SP — **3.3.2** |
| Not SOA timer reading | **3.6** |
| Not conceptual hop without SP | **3.8.1** |
| Not VT contacted-domain graph | **3.9.1** |
| Not URLScan this-load hosts | **3.9.4** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Sibling on same A + NS | Entire `203.0.113.0/24` |
| First-seen as *age*, not a hash | SP as a sandbox |
| One cited hop, then optional second field on the sibling | 20-name NS spray |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Enrich + Sibling (Expected)

**Enrich:** `nightowl-updates.net` — A `203.0.113.88` since 2026-08-01, NS `cdn-test.net`. Young name. Not a registrant (**3.5**).  
**Pivot:** same A → `login-nightowl.net` (first seen 2026-08-10).  
**Product:** “SP: sibling `login-nightowl.net` (same A `203.0.113.88`).”

### Example 2: Cloud /24 (Lead)

**Draft:** Every name on `203.0.113.0/24` is Night Owl.

**Fail.** Same hosting reject as **3.8.1**. Silent Push showing neighbors in a CIDR is not a cluster.  
**Lead:** Need same A *or* distinctive NS — not the cloud block.

### Example 3: Silent Push as Sandbox (Lead)

**Draft:** Open Silent Push to get the process tree for `update.exe`.

**Fail.** No sample, no detonation. That is **3.9.2** / **3.9.1** Behavior.  
**Lead:** Right IOC type (you *have* a domain). Wrong capability.

---

## 3. Hands-On Exercise

**Objective:** Enrich the seed in Silent Push. Pivot on a cited field. Reject /24 and sandbox use.

**Use only the classroom cards.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Enrich** (task 1): one **enrich line** for `nightowl-updates.net`.
3. **Pivot** (task 2): write a **pivot line** for each.

   - A. Same A → `login-nightowl.net`.  
   - B. Same /24 as additional infra.  
   - C. First-seen on the sibling (what it *adds* after A).  
   - D. “Get the process tree from Silent Push.”

4. Do not re-read the SOA card (**3.6**). Do not open VT Relations. Do not query RDAP.
5. A second hop is allowed only if it is a *field on the sibling* (C), not a new CIDR spray.

**Expected Outcome:**
- Three example summaries
- One enrich line
- Four pivot lines (B and D fail)
- No SOA lecture, no sandbox

---

## 4. Knowledge Check

1. Name **two** Silent Push capabilities and what each is *not*.
2. What belongs on an **enrich line**?
3. Why is the **cloud /24** not a pivot?
4. What does **first-seen** on the sibling add after you already have the same A?
5. Where do you get a **process tree**?

---

## 5. Summary

- Enrich the SP record. Pivot on a cited field. /24 and sandbox stay out.
- Next: **3.9.4** URLScan.

---

## 6. References & Further Reading

- Related modules:
  - 3.9.2 – AnyRun (previous)
  - 3.3.2 – When to open Silent Push
  - 3.8.1 – Conceptual infra hop
  - 3.9.4 – URLScan (next)
- Classroom Silent Push cards in this guide (lesson-only)
