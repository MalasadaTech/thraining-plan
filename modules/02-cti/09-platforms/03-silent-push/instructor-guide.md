# Instructor Guide – Module 3.9.3 – Silent Push

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.9.3 A / A / B · 3.9.3.1 1a / 1a / 2b  
- Hunter: 3.9.3 A / B / B · 3.9.3.1 2b / 3c / 4c  
- CTI: 3.9.3 B / C / C · 3.9.3.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Silent Push depth: enrich the PDNS record, pivot on a **cited field**, reject /24 and sandbox-use.

**Key Teaching Points:**
- SOC K is **A / A / B**. Hunter K is **A / B / B**. CTI task **4d** — the second field on the sibling (first-seen) vs spraying the CIDR.
- Do not re-teach SOA timers or RDAP created-date. Point at **SP fields**.
- Same sibling as **3.8.1** / **3.6** is OK — the *source* this hour is Silent Push, not the zone card.
- Classroom cards only.

**Common Student Challenges:**
- Treating SP score as attribution.
- Entire cloud /24.
- Opening AnyRun “because we’re pivoting.”
- Re-lecturing MNAME/RNAME.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Capabilities that matter (and what they are not).
2. Enrich the seed record.
3. Pivot on a cited SP field.

**Mapped Items:** K 3.9.3 · T 3.9.3.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 3.3.2 / 3.6 / 3.8.1 redo |
| Capabilities + enrich/pivot    | 14 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep the /24 |

---

## Detailed Teaching Notes

**Talking Points:**
- 4d: A = same A (legal hop). C = first-seen on that sibling (ages the cluster, still not a registrant). B = /24 (illegal).
- Distinctive NS on *this* card is `cdn-test.net`. If they say “NS cluster,” make them name the NS — not Cloudflare.

**Question:**  
“You already have `login-nightowl.net` from the same A. What does first-seen 2026-08-10 add — and what does it still not prove?”

---

## Hands-On Exercise – Instructor Guidance

**Enrich:** `nightowl-updates.net | A 203.0.113.88 first 2026-08-01 / NS cdn-test.net | young name on that NS | not a person or country`

**Pivot:**

| Item | Additional infra | Field | Notes |
|------|------------------|-------|-------|
| A | **`login-nightowl.net`** | Same A | Yes |
| B | **Reject** | /24 | Hosting |
| C | (same sibling) | First-seen 2026-08-10 | Adds age; not a new name |
| D | **Refuse** | — | Sandbox is **3.9.2** / **3.9.1** |

---

## Knowledge Check – Answer Key

1. **Two capabilities + not?**  
   **Answer:** Any two of: PDNS (not a screenshot), siblings (not unlabeled related), NS cluster (not public CDN), score (not a verdict).  
   **Explanation:** Outline a.

2. **Enrich line?**  
   **Answer:** Indicator, A/first-seen/NS, what it suggests, what you must not claim.  
   **Explanation:** Task 1.

3. **Why not /24?**  
   **Answer:** Shared cloud tenants. Same reject as **3.8.1**.  
   **Explanation:** Example 2.

4. **First-seen on the sibling?**  
   **Answer:** Ages the second name (2026-08-10). Does not name a registrant or prove they are the same *actor*.  
   **Explanation:** 4d / item C.

5. **Process tree?**  
   **Answer:** **3.9.2** AnyRun or **3.9.1** Behavior — not Silent Push.  
   **Explanation:** Example 3.

---

## Additional Instructor Resources

- Classroom Silent Push cards
- Next recommended module: 3.9.4 URLScan
