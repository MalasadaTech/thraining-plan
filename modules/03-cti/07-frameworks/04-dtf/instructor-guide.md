# Instructor Guide – Module 3.7.4 – MalasadaTech Defender’s ThreatMesh Framework (DTF)

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
Local DTF: mesh indicator / infrastructure / behavior, **score** on the classroom card, **prioritize**, name the **next seed**, and explain how DTF **complements** ATT&CK, Diamond, and Kill Chain.

**Key Teaching Points:**
- Shared `modules/shared/frameworks/` is empty. The **classroom card** is the stand-in. Say “lesson-only, not live org policy” out loud.
- If a site later posts a real DTF spec, swap the card. Keep purpose + mesh + score + seed + complement.
- SOC K is **A / A / B** (not A/B/B). Hunter K is **A / B / B**. CTI tasks **4d** on 3.7.4.1–2 (judgment on the score and the seed), **4c** on 3.7.4.3. Do not collapse.
- Do **not** run 3.8.1 this hour. Name the seed and stop.
- Do not copy `modules/shared/frameworks/` into this folder.

**Common Student Challenges:**
- Scoring the vendor PDF first.
- Putting T-IDs or Kill Chain stages in the score box.
- Treating the total as attribution (“8 = nation-state”).
- Opening RDAP / Silent Push / VT Relations.
- Re-teaching 3.7.1–3.7.3 instead of one complement sentence each.

**Required Materials:**
- Student Guide (classroom card)
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Purpose: pattern + prioritize.
2. Mesh + classroom score + next seed.
3. Complement, do not replace, the other three.

**Mapped Items:** K 3.7.4 · T 3.7.4.1 · T 3.7.4.2 · T 3.7.4.3

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Lesson-only card; not 3.7.1–3 redo / 3.8 |
| Purpose, mesh, score, complement | 16 min | a–e |
| Walkthrough Examples           | 12 min   | |
| Hands-On Exercise              | 18 min   | Lines + seed + three sentences |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they boost T1486 |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they can fill a table. Push **why Mesh is 3 not 1** and **why the seed is the domain not T1486** (4d).
- Mesh 3 on one host is allowed (three *node types* linked). A *second name* is the “same mesh on a second host or name” bump — item C.
- Reach 2 vs 3: they can hunt/block the domain; they have not shown they can interrupt every node. Do not invent a Harbor block policy.

**Question:**  
“The vendor listed T1486. What would have to appear in the Harbor excerpt before that claim is a DTF *node*?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail high scores on B. Fail T-IDs in the score box. Fail RDAP. Fail “8 = APT.” Accept Mesh 3 on A (three-node). On C, Mesh stays **3** if they already gave A a 3, or rises from 2 → 3 if they were conservative on A — both OK if they cite the second name.

**Summaries:**
- Ex 1: mesh 3 / recency 3 / reach 2 = 8; seed = domain.
- Ex 2: unmeshed vendor claim = 0.
- Ex 3: DTF does not replace the other three and does not pivot.

**DTF lines:**

| Item | Mesh | Recency | Reach | Total | Notes |
|------|------|---------|-------|-------|-------|
| A | **3** | **3** | **2** | **8** | Prioritize. Seed: `nightowl-updates.net` |
| B | **0** | **0** | **0** | **0** | No Harbor nodes |
| C | **3** | 3 | 2 | 8 | Second name *confirms* Mesh 3; still not a 3.8 pivot |

**Next seed (A):** `nightowl-updates.net` (infra is the linked, hunt-able node). Accept `203.0.113.88` if they say the IP is the same infra node. Reject T1486 / “Night Owl APT.”

**Complement (must hit all three):**
- ATT&CK: names *how* (T-IDs); DTF clusters/ranks those facts.
- Diamond: shows empty Adversary; DTF does not fill it.
- Kill Chain: orders Delivery / Exploitation / Installation; DTF does not relabel stages.

---

## Knowledge Check – Answer Key

1. **DTF for?**  
   **Answer:** See a pattern across indicator / infrastructure / behavior, then prioritize the next defensive or enrichment look.  
   **Explanation:** Outline a.

2. **DTF line besides the total?**  
   **Answer:** Nodes, links, the three factor scores, prioritize yes/no, next seed.  
   **Explanation:** Tasks 3.7.4.1–2.

3. **Why not T1486 high?**  
   **Answer:** Not in *this* evidence. No Harbor mesh. Uncited vendor claims score 0.  
   **Explanation:** Example 2.

4. **High score this hour?**  
   **Answer:** Name the next seed. Do **not** run **3.8.1**.  
   **Explanation:** Outline d.

5. **Complement (any one)?**  
   **Answer:** ATT&CK = IDs; Diamond = gaps; Kill Chain = order. DTF = cluster + rank. It does not assign T-IDs, fill Adversary, or replace stages.  
   **Explanation:** Outline e / 3.7.4.3.

---

## Additional Instructor Resources

- Classroom DTF card (student guide)
- Next recommended module: 3.8.1 Identifying additional adversary infrastructure from seed indicators
