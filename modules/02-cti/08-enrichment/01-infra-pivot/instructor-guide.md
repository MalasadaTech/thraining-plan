# Instructor Guide – Module 2.8.1 – Identifying additional adversary infrastructure from seed indicators

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4d  
- Hunter: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4d  
- SOC: 2.8.1 A / B / B ; 2.8.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Write a hop sentence from a seed. Name the source class. Reject shared hosting. Do not write a DTF P-ID and do not re-teach the tools.

**Context (plain language):**

- What this lesson is for: CTI analysts start from a seed they already have. One seed is rarely the whole picture. This lesson hops from that seed to other adversary infrastructure: what you share, what you found, and why it is not coincidence.
- How it hooks to the lesson before: 2.7.4 was the DTF ID line (PTA/P). This lesson is the same hop without those IDs.
- How it hooks to the lesson after: 2.8.2 is TTPs that apply here, not more infrastructure.
- Why we are doing it this way: the product is the sentence. This lesson selects and records enrichment; it does not re-teach the tool (0.7 / 2.9).
- What we are *not* doing in this lesson: RDAP class (2.5). SOA parse (2.6). Silent Push or VirusTotal operation (0.7 / 2.9). DTF P-IDs (2.7.4). TTP extract (2.8.2). Campaign tracking (2.8.3). No lab.
- Extra step: none.

Use the same names as the student guide: **seed**, **pivot** (hop), **shared characteristic**, **candidate**, and **hop sentence**. A **P-ID** is the DTF PTA/P code from 2.7.4, not a field on this sentence. **Registration**, **DNS**, **same A**, **TLS certificate**, and **HTTP title** are source classes you name, not tools you operate.

**Key Teaching Points:**
- Four-part hop sentence. No P-ID.
- Name the source class. Do not re-teach the lookup.
- Distinctive NS pair is a take. The whole `/24` is coincidence.

**Common Student Challenges:**
- Write a DTF P-ID on the hop. Why: the previous lesson was DTF. Example: putting `PTA0001 / P0101.010` on the NS hop instead of the four-part sentence.
- Take the whole `/24`. Why: the seed IP sits in that range. Example: calling `203.0.113.0/24` adversary infrastructure.
- Open a tool class. Why: the hop uses registration or DNS. Example: walking RDAP fields or a Silent Push screen instead of naming the source class.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.8.1 – Identifying additional adversary infrastructure from seed indicators
- T: 2.8.1.1 – Pivot from a seed indicator to additional adversary infrastructure

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Seed hop, not a P-ID |
| Key Concepts            | 12 min    | Sentence; sources; take vs `/24` |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: you already have a seed, and one seed is rarely the whole picture. The product today is the hop sentence.
- Write the four parts. Stop. Do not add a PTA/P code.
- Walk the source table. Name the class. If they open RDAP, SOA, Silent Push, or VirusTotal Relations: name it; do not teach it.
- Walk the take: update domain / `203.0.113.88`, distinctive NS pair `ns1.cdn-test.net` / `ns2.cdn-test.net`, candidate `login-prd.net`. Same A on that named sibling can support the hop. Still four parts, not a P-ID.
- Walk the reject: whole `203.0.113.0/24` is shared hosting. The seed IP in that range does not make the range theirs.
- If they write `P0101.010`: that is 2.7.4. This lesson is the sentence.
- If they start extracting TTPs: that is 2.8.2.

---

## Knowledge Check – Answer Key

1. **This lesson requires a DTF P-ID on the hop. True or false?**  
   **Answer:** False. That is 2.7.4.  
   **Explanation:** This lesson records the hop sentence. The PTA/P line was the previous lesson.

2. **What four parts does a hop sentence have?**  
   **Answer:** Seed, shared characteristic, candidate, why not coincidence.  
   **Explanation:** That is the product you record. A source class names where the shared characteristic came from; it is not a fifth part of the sentence.

3. **You have the update domain / `203.0.113.88`. Shared nameservers `ns1.cdn-test.net` / `ns2.cdn-test.net` point at `login-prd.net`. Write the hop, or say why you would reject the whole `203.0.113.0/24`.**  
   **Answer:** Seed = update domain / `203.0.113.88`; shared characteristic = distinctive NS pair; candidate = `login-prd.net`; why not coincidence = not a public resolver. Reject the whole `203.0.113.0/24` — shared hosting.  
   **Explanation:** The named sibling with a distinctive NS pair is the hop. The `/24` is coincidence.

---

## Additional Instructor Resources

- Next: 2.8.2 Applicable TTPs
