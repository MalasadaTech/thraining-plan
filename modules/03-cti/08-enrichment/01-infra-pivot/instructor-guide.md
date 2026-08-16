# Instructor Guide – Module 3.8.1 – Identifying Additional Adversary Infrastructure from Seed Indicators

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.8.1 A / B / B · 3.8.1.1 1a / 2b / 3c  
- Hunter: 3.8.1 B / C / C · 3.8.1.1 3c / 4c / 4d  
- CTI: 3.8.1 B / C / C · 3.8.1.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Do the hop **3.7.4** only named: seed → shared property → **additional infrastructure**. Reject weak public NS / cloud CIDR hops and uncited vendor names.

**Key Teaching Points:**
- Do not re-teach RDAP fields, SOA timers, or Silent Push vs VT. Point at the **cards** and the hop.
- Classroom PDNS / TIP rows are **lesson-only**, same rule as Harbor / DTF cards.
- SOC K is **A / B / B**. Hunter/CTI task **3c / 4c / 4d**. The 4d move is *why this hop is not a coincidence*.
- Do not open **3.8.2**, **3.8.3**, **3.8.4**, or **3.9**.

**Common Student Challenges:**
- Treating Example Cloud /24 as “theirs.”
- Shared CDN NS as a cluster.
- Pasting `evil-c2.net` from the vendor PDF.
- Re-scoring DTF or writing T-IDs.
- Opening VT Relations because “that’s pivoting.”

**Required Materials:**
- Student Guide (classroom cards)
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Pivot = seed + shared property + additional infra.
2. Pick a source; cite the hop.
3. Reject weak / uncited hops.

**Mapped Items:** K 3.8.1 · T 3.8.1.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 3.5/3.6 redo; not 3.8.2 / 3.9 |
| Pivot concepts + sources       | 14 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Pivot lines |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep the /24 |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they already stacked SOA in **3.6**. Push **two properties** (MNAME+NS *and* same A).
- 4d: “same NS” is not enough if that NS is public. `cdn-test.net` is distinctive *in this classroom* because it is not Cloudflare and it pairs with the same A.
- Redacted RDAP still gives NS — they should already know that from **3.5**. One reminder, then move.

**Question:**  
“What would make `evil-c2.net` a legal additional-infra hop on *this* card?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail B (/24). Fail D (uncited). Fail E (3.11). Accept A and C as the same hop if they cite MNAME+NS and/or same A.

**Summaries:**
- Ex 1: `login-nightowl.net` via SOA/NS + PDNS A.
- Ex 2: cloud /24 or public NS is weak.
- Ex 3: vendor name with no property stays out.

**Pivot lines:**

| Item | Additional infra | Source | Shared | Notes |
|------|------------------|--------|--------|-------|
| A | **`login-nightowl.net`** | SOA/NS and/or PDNS | MNAME+NS and/or A `203.0.113.88` | Supported |
| B | **None / reject** | — | /24 only | Hosting, not theirs |
| C | **`login-nightowl.net`** | PDNS + SOA | A **and** MNAME+NS | Strongest cite |
| D | **None** | — | None on the card | Uncited |
| E | **Refuse** | — | — | **3.11** |

**Product sentence:** “From `nightowl-updates.net`: `login-nightowl.net` (same MNAME+NS and same A `203.0.113.88`).”

---

## Knowledge Check – Answer Key

1. **What is a pivot?**  
   **Answer:** Start from a seed, follow a shared property, name additional infrastructure you can cite.  
   **Explanation:** Outline a.

2. **Two sources + property?**  
   **Answer:** Any two of: RDAP → NS; SOA → MNAME/NS; PDNS → historical A; TIP → internal sighting.  
   **Explanation:** Outline b.

3. **Why not the cloud /24?**  
   **Answer:** Shared hosting. RDAP org is the cloud, not the adversary. Many tenants.  
   **Explanation:** Example 2.

4. **Why not the vendor domain?**  
   **Answer:** No shared property on *this* evidence. Uncited names stay out.  
   **Explanation:** Example 3.

5. **Harbor-applicable TTPs?**  
   **Answer:** **3.8.2**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Classroom cards (student guide)
- Next recommended module: 3.8.2 Extracting applicable TTPs from intelligence reports
