# Instructor Guide – Module 3.9.2 – AnyRun

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.9.2 A / A / B · 3.9.2.1 1a / 1a / 2b  
- Hunter: 3.9.2 A / B / B · 3.9.2.1 2b / 3c / 4c  
- CTI: 3.9.2 B / C / C · 3.9.2.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Search AnyRun (tag / IP / domain / hash) and review a run for **actionable** events. Classroom cards only — no live detonation.

**Key Teaching Points:**
- SOC K is **A / A / B** (not A/B/B). Hunter K is **A / B / B**. Task Hunter/CTI ends at **4c** (not 4d — that is VT / Silent Push).
- Do not detonate student USB samples. Cards are the lab.
- Do not re-teach 3.3.2 “when AnyRun.” One sentence: you need a sample or a public run.
- AnyRun labels ≠ **3.8.2** applicable TTPs.

**Common Student Challenges:**
- Searching tag `apt` first.
- Taking R2 because it is tagged `nightowl`.
- Copying AnyRun’s MITRE matrix.
- Opening VT Behavior and calling it AnyRun.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Search by four query types.
2. Keep the run whose events match.
3. Extract tree / drop / C2 only.

**Mapped Items:** K 3.9.2 · T 3.9.2.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | No live detonation; not 3.9.1 |
| Search + review                | 14 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep tag `apt` |

---

## Detailed Teaching Notes

**Talking Points:**
- Domain/IP search finds runs that *contacted* that infra — still verify the tree.
- Hash search is exact. Empty ≠ clean.
- R1 vs R2 is the whole point of review.

**Question:**  
“R2 is tagged `nightowl`. What event would you need before you keep it?”

---

## Hands-On Exercise – Instructor Guidance

**Search:**

| Item | Query | Keep | Notes |
|------|-------|------|-------|
| A | Hash `6734f374…` | **R1** | Exact sample |
| B | Domain | **R1** | Events match |
| C | Tag `apt` | **None / too broad** | Not a first query |
| D | IP | **R1** | Same as domain card |

**Review R1:** `wscript→powershell -enc | %TEMP%\update.exe | nightowl-updates.net:8080 GET | not T1486 tag`  
**R2:** reject — miner, tag-only.

---

## Knowledge Check – Answer Key

1. **Four search types?**  
   **Answer:** Tag, IP, domain, hash.  
   **Explanation:** Outline a.

2. **Actionable?**  
   **Answer:** Events from *this* run — tree, dropped file, C2 — not a score or a tag.  
   **Explanation:** Outline b.

3. **Why not tag `apt` first?**  
   **Answer:** Unrelated runs. Tag is a filter, not a cluster.  
   **Explanation:** Example 2.

4. **Why not the T1486 tag?**  
   **Answer:** R1 has no encrypt event. Uncited label stays out.  
   **Explanation:** Example 3.

5. **VT Behavior instead?**  
   **Answer:** Events *already on a VT hash* — **3.9.1**. AnyRun is search/review of *runs* (and detonation when you have a file).  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Classroom AnyRun cards
- Next recommended module: 3.9.3 Silent Push
