# Instructor Guide – Module 3.7.4 – Defender’s ThreatMesh Framework (DTF)

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.7.4 A / A / B · 3.7.4.1 1a / 1a / 2b · 3.7.4.2 1a / 1a / 2b · 3.7.4.3 1a / 1a / 2b  
- Hunter: 3.7.4 A / B / B · 3.7.4.1 1a / 2b / 3c · 3.7.4.2 1a / 2b / 3c · 3.7.4.3 1a / 2b / 3c  
- CTI: 3.7.4 B / C / C · 3.7.4.1 3c / 4c / 4d · 3.7.4.2 3c / 4c / 4d · 3.7.4.3 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Real DTF: pick **PTA + P**, cite the characteristic, name candidate infra, name the **next lookup**, reject weak neighbors. **No scores.**

**Key Teaching Points:**
- Source of truth: [defenders-threatmesh-framework](https://github.com/MalasadaTech/defenders-threatmesh-framework). Do not copy it into this folder.
- Real IDs only. Invented `P9999` fails. T1486 is not a DTF ID.
- SOC K is **A / A / B**. Hunter K is **A / B / B**. CTI **4d** on 3.7.4.1–2 = distinctive vs weak pivot (NS+substring vs /24), not a number. 3.7.4.3 is **4c**.
- Survey four tactics. Apply Domain + IP. SSL/HTTP stay named unless you overlay a cert/page card.
- 3.8.1 still owns the generic hop sentence. This hour’s product is the **ID line**.
- Do not copy `modules/shared/frameworks/` into this folder.

**Common Student Challenges:**
- Reaching for the old mesh+recency+reach card.
- /24 or Example Cloud as “theirs.”
- Vendor APT / T1486 as a pivot.
- Opening RDAP/Silent Push and calling that the DTF product.
- Re-teaching 3.7.1–3.7.3 instead of one complement sentence each.

**Required Materials:**
- Student Guide (apply table)
- Slide Deck
- Optional: live DTF matrix for lookup
- Answer key (this guide)

---

## Learning Objectives

1. DTF = discover more infra; communicate/record the pivot.
2. Real PTA/P; reject the weak neighbor.
3. Name the next lookup.
4. Complement, do not replace, the other three.

**Mapped Items:** K 3.7.4 · T 3.7.4.1 · T 3.7.4.2 · T 3.7.4.3

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not a scorecard; not 3.7.1–3 redo |
| Purpose, PTA/P, apply set, complement | 16 min | a–e |
| Walkthrough Examples           | 12 min   | |
| Hands-On Exercise              | 18 min   | Lines + lookups + three sentences |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep the /24 |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they can name P0101.010. Push **why** that NS is distinctive and **why** P0202 fails (4d).
- P0101.010 + P0102.002 together is stronger than either alone. That is not a numeric score.
- No PTR on the classroom card → P0201 is **not on card**, not a fail and not a take.
- hIGMA / masq-monitor: one “out of scope” sentence if asked.

**Question:**  
“What would make P0202 legal on *this* card — and do we have it?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail D (/24). Fail E (not infra). Fail invented P-codes. Fail T-IDs in the DTF line. Fail a numeric total.

**Summaries:**
- Ex 1: PTA0001 stack → `login-nightowl.net`.
- Ex 2: /24 / AS = hosting.
- Ex 3: no DTF ID for T1486 / APT; no minted P-code.

**DTF lines:**

| Item | PTA | P-ID | Candidate | Notes |
|------|-----|------|-----------|-------|
| A | **PTA0001** | **P0101.010** | other names on `cdn-test.net` NS | Distinctive NS |
| B | **PTA0001** | **P0102.002** | **`login-nightowl.net`** | Substring |
| C | **PTA0001** | **P0103.003** | **`login-nightowl.net`** / same A | Stack with A–B |
| D | **Reject** | P0202 | — | Shared /24 |
| E | **None** | — | — | Not infrastructure |

**Lookups (A–C):** A → RDAP NS (**3.5**). B → PDNS / name search for substring. C → PDNS same A (**3.3.2 / 3.9.3**). Optional stack: P0103.004 → SOA RNAME (**3.6**). Do not run the tools.

**Complement (must hit all three):**
- ATT&CK: *how* (T-IDs). DTF: *where else* (PTA/P).
- Diamond: empty Adversary allowed. DTF does not fill it.
- Kill Chain: order of stages. DTF does not relabel them.

---

## Knowledge Check – Answer Key

1. **DTF for?**  
   **Answer:** Discover additional adversary infrastructure from a known-bad seed; communicate and record the pivot.  
   **Explanation:** Outline a.

2. **DTF line besides the P-ID?**  
   **Answer:** Seed, PTA, shared characteristic, candidate infra, why not coincidence.  
   **Explanation:** Tasks 3.7.4.1–2.

3. **Why not the /24?**  
   **Answer:** Shared hosting. P0202 / P0203 are weak alone.  
   **Explanation:** Example 2.

4. **This hour — do / don’t?**  
   **Answer:** Name the next lookup (RDAP NS, SOA RNAME, PDNS A). Do **not** invent a score. Do **not** run **3.8.1** as a generic hop without IDs.  
   **Explanation:** Outline d.

5. **Complement (any one)?**  
   **Answer:** ATT&CK = behavior IDs; Diamond = gaps; Kill Chain = order. DTF = defender discovery pivots. It does not assign T-IDs, fill Adversary, or replace stages.  
   **Explanation:** Outline e / 3.7.4.3.

---

## Additional Instructor Resources

- [DTF matrix](https://github.com/MalasadaTech/defenders-threatmesh-framework/blob/main/matrix.md)
- Next recommended module: 3.8.1 Identifying additional adversary infrastructure from seed indicators
