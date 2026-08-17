# Instructor Guide – Module 3.4.1 – Hashing and Similarity Concepts

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.4.1 A / A / B · 3.4.1.1 1a / 1a / 2b · 3.4.1.2 1a / 1a / 2b  
- Hunter: 3.4.1 A / B / B · 3.4.1.1 1a / 2b / 3c · 3.4.1.2 1a / 2b / 3c  
- CTI: 3.4.1 B / C / C · 3.4.1.1 3c / 4c / 4d · 3.4.1.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach imphash / ssdeep / TLSH purpose and force **related vs not** plus a **cert interpret**. Do not teach VT Relations or AnyRun.

**Key Teaching Points:**
- Classroom ssdeep ≥ 50 is a stand-in. Overlay the site cutoff if you have one.
- SHA256 match = identity, not similarity.
- Signed ≠ trusted. Subject string ≠ issuer.
- SOC 3-level tasks are **1a / 2b**. CTI similarity is **3c / 4d**; cert is **3c / 4c**. Do not collapse.
- Outline task 1 (purpose/use case) is in the table — do not skip it.

**Common Student Challenges:**
- Calling S1/S4 an ssdeep finding.
- Trusting “Microsoft” in the subject.
- Mixing TLSH distance with ssdeep score.
- Opening 3.9.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional live PE + `sigcheck` / VT details tab
- Answer key (this guide)

---

## Learning Objectives

1. Purpose / use case of imphash, ssdeep, TLSH.
2. Related vs not, which hash.
3. Interpret cert fields.

**Mapped Items:** K 3.4.1 · T 3.4.1.1 · T 3.4.1.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 1.2.7-as-whole / 3.9 |
| Three hashes + cert fields     | 16 min   | a–d |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Related + cert |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 3 if they trust the subject |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they should *pick the hash* and *read the issuer*, not recite “fuzzy hashing exists.”
- imphash collisions: two unrelated droppers that both import `WinInet` + `CreateFile` can share an imphash. If ssdeep is 8, say **imports match, body does not**.

**Question:**  
“S2 matches S1 on imphash and ssdeep. What have you *not* proven?” (Same campaign, same actor, same capability — only related samples.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail S1/S4 as similarity. Fail D as trusted. Fail mixing scales.

**Summaries:**
- Ex 1: related (imphash + ssdeep 72).
- Ex 2: identity, not similarity.
- Ex 3: fake Microsoft; not similar to S1.

**Similarity:**

| Item | Related? | Hash | Why |
|------|----------|------|-----|
| A S1–S2 | **Yes** | imphash + ssdeep 72 | Same imports; fuzzy ≥ 50 |
| B S1–S3 | **No** | imphash differ; ssdeep 8 | Below cutoff |
| C S1–S4 | **Identical** | SHA256 | Not a 3.4.1.1 similarity call |

**Cert:**

| Item | Interpret |
|------|-----------|
| S3 | Signed; subject Microsoft-like; issuer **Harbor Test CA** — not Microsoft; **expired**. Does not prove legit or Night Owl |
| D | Signed, self-signed Harbor IT, currently valid. **Not** a public trusted CA. Use serial to pivot if needed |
| E | **Unsigned**. Common. Does not prove malware |

---

## Knowledge Check – Answer Key

1. **imphash vs SHA256?**  
   **Answer:** imphash = same PE import set (related builder/family possible). SHA256 = same bytes.  
   **Explanation:** Outline a / task 1.

2. **ssdeep / ≥ 50?**  
   **Answer:** Fuzzy similarity after small edits. Classroom ≥ 50 = related enough. 0 or 8 is not.  
   **Explanation:** Outline b; stand-in cutoff.

3. **TLSH vs ssdeep?**  
   **Answer:** Different algorithms and scales. Compare TLSH to TLSH only.  
   **Explanation:** Outline c.

4. **Why not trust “Microsoft” in subject?**  
   **Answer:** Anyone can put that string. Trust follows **issuer / chain**, not the subject label.  
   **Explanation:** Outline d / Example 3.

5. **Behavior?**  
   **Answer:** **3.3.2** AnyRun (if you have the file), not this hash card.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Local ssdeep/TLSH SOP
- Next recommended module: 3.5.1 RDAP / WHOIS
