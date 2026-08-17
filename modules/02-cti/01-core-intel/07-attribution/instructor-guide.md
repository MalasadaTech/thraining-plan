# Instructor Guide – Module 3.1.7 – Attribution

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.1.7 A / A / A · 3.1.7.1 1a / 1a / 1a  
- Hunter: 3.1.7 A / B / B · 3.1.7.1 1a / 2b / 3c  
- CTI: 3.1.7 B / C / C · 3.1.7.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach purpose, challenges, confidence, and types. Force an **assess line**. Do not write actor profiles.

**Key Teaching Points:**
- Low/medium/high is a stand-in. Overlay the site scale if you have one.
- Activity group ≠ nation-state.
- Vendor nickname ≠ country.
- SOC 3-level is **1a / 1a / 1a**. CTI is **3c / 4d**. Do not collapse.
- 3.11.1.2 is the finished-product form of this skill.

**Common Student Challenges:**
- Equating cluster with country.
- High confidence on one blog.
- Writing a profile instead of assessing the statement.
- Opening 3.2.1 lexicon or 3.2.3 Admiralty.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site confidence card
- Answer key (this guide)

---

## Learning Objectives

1. Purpose and challenges.
2. Confidence + types.
3. Assess claim vs evidence.

**Mapped Items:** K 3.1.7 · T 3.1.7.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.11.1.2 / 3.2.1 / 3.2.3 |
| Purpose, confidence, types     | 16 min   | a–c |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~64 min** | Stretch Ex 2 if they defend the flag |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they should *downgrade* an over-claim, not just define attribution.
- Shared infra is the usual challenge on Night Owl SNI.

**Question:**  
“If we can cluster Night Owl, what *additional* evidence would you need before a nation-state sentence?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail country-from-blog. Fail high-on-one-hit. Accept D as supported-low.

**Summaries:**
- Ex 1: supported medium cluster.
- Ex 2: over-claim nation-state / high.
- Ex 3: type OK, confidence inflated.

**Cases:**

| Item | Type | Confidence | Call |
|------|------|------------|------|
| A | Activity group | Medium | **Supported** — two internals, two lines |
| B | Nation-state claimed | High claimed | **Over-claim** — one blog. Downgrade type and confidence |
| C | Nation-state via vendor map | — | **Wrong type** + over-claim. Cluster ≠ country |
| D | Activity group | Low | **Supported** — caveated; shared CDN noted |

---

## Knowledge Check – Answer Key

1. **Purpose / one challenge?**  
   **Answer:** Focus defense and collection. Challenges: shared infra, false flags, vendor names, thin sources.  
   **Explanation:** Outline a.

2. **Medium vs high?**  
   **Answer:** Medium = more than one line, alternatives remain. High = several independent lines, alternatives weak.  
   **Explanation:** Outline b.

3. **Why group ≠ state?**  
   **Answer:** Clustering tooling/infra does not prove a government. Nation-state is a higher claim.  
   **Explanation:** Outline c.

4. **Why not high on a blog flag?**  
   **Answer:** Single external nickname is not independent evidence.  
   **Explanation:** Example 2.

5. **Actor profile?**  
   **Answer:** **3.11.1.2**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Site attribution / confidence card
- Next recommended module: 3.1.8 Collection sources and methods
