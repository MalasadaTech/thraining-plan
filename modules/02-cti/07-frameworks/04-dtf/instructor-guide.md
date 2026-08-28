# Instructor Guide – Module 2.7.4 – MalasadaTech Defender's ThreatMesh Framework (DTF)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.4 B / C / C ; 2.7.4.1 3c / 4c / 4d ; 2.7.4.2 3c / 4c / 4d ; 2.7.4.3 3c / 4c / 4c  
- Hunter: 2.7.4 A / B / B ; 2.7.4.1 1a / 2b / 3c ; 2.7.4.2 1a / 2b / 3c ; 2.7.4.3 1a / 2b / 3c  
- SOC: 2.7.4 A / A / B ; 2.7.4.1 1a / 1a / 2b ; 2.7.4.2 1a / 1a / 2b ; 2.7.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Pick a real PTA/P from a known-bad seed, cite the characteristic, reject shared cloud, and name the next lookup. DTF does not replace ATT&CK, Diamond, or Kill Chain.

**Context (plain language):**

- What this lesson is for: CTI analysts start from a known-bad seed and need more adversary infrastructure. This lesson is the shared language for that discovery pivot — a real DTF ID, a cited characteristic, a rejected weak neighbor, and a named next lookup.
- How it hooks to the lesson before: 2.7.3 was Kill Chain progression on a report. This lesson is infrastructure discovery.
- How it hooks to the lesson after: 2.8.1 is the hop sentence without P-IDs.
- Why we are doing it this way: official DTF IDs only. No score. No invented P-codes. Do not teach every P-code. The product is the DTF ID line. The student guide has to stand alone.
- What we are *not* doing in this lesson: re-teach RDAP (2.5), SOA (2.6), or PDNS (0.7 / 2.9.3). ATT&CK T-IDs (2.7.1). Hunt planning (3.5). Shared-floor 0.6. Lumped 2.7.5. Actor profile (2.11). No lab. Do not tell the PRD plot.
- Extra step: none.

Use the same names as the student guide: **DTF**, **pivot tactic (PTA)**, **pivot (P)**, **seed**, **characteristic**, **candidate**, **next lookup**, and **DTF ID line**. Use `login-prd.net`, `ns1.cdn-test.net`, and `203.0.113.88`. Do not invent P-codes.

**Key Teaching Points:**
- Four tactics. Real IDs only.
- Same NS / same A can take when distinctive. Whole `/24` is reject.
- Next lookup is a name, not a tool class you operate here.
- DTF is discovery. ATT&CK is behavior. Diamond is know / don’t-know. Kill Chain is progression.

**Common Student Challenges:**
- Invent a P-code. Why: they want a cell for every idea. Example: writing `P9999` for “feels related.”
- Score the pivot. Why: ATT&CK-like shape looks like a grade. Example: “high-confidence 80.”
- Take the whole `/24`. Why: proximity is a real PTA0002 pivot. Example: calling every host in `203.0.113.0/24` theirs.
- Put a T-ID on the DTF line. Why: 2.7.1 just used ATT&CK. Example: writing T1059 instead of PTA0001 / P0101.010.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.7.4 – Defender’s ThreatMesh Framework (DTF) for infrastructure discovery
- T: 2.7.4.1 – Apply DTF: select a pivot tactic and pivot from a seed and reject the weak neighbor
- T: 2.7.4.2 – Use a selected DTF pivot to guide the next enrichment or lookup
- T: 2.7.4.3 – Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Discovery from a seed; no score |
| Key Concepts            | 16 min    | Four PTA; take/reject; next lookup; complement |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a known-bad seed is on the desk, and they have to find more infrastructure and write the pivot so someone else can run it again.
- Write the four tactics. Stop. Do not walk every P-code. PTA0003 and PTA0004 wait for a cert card or a page card.
- Walk same NS (`P0101.010`) and same A (`P0103.003`) as takes. Walk whole `/24` (`P0202`) as reject — shared cloud, not distinctive.
- The P-ID names the next lookup. Name RDAP, SOA, or PDNS. Do not open those tools.
- One pass on the complement table: ATT&CK = behavior, Diamond = know / don’t-know, Kill Chain = progression, DTF = discovery.
- Walk the DTF ID line from the student guide. The product is that line, not a story of the incident.
- If they invent `P9999`: that ID is not in DTF.
- If they score the line: there is no scoring.
- If they assign T1059: that is 2.7.1, not a DTF pivot.
- If they write the hop with no P-ID: that is 2.8.1.

---

## Knowledge Check – Answer Key

1. **DTF replaces ATT&CK. True or false?**  
   **Answer:** False. DTF is discovery. ATT&CK is behavior.  
   **Explanation:** Same matrix shape, different job. DTF does not replace Diamond or Kill Chain either.

2. **Same NS on the update domain and `login-prd.net`. Which PTA / P-ID, or reject?**  
   **Answer:** **Take: PTA0001 / P0101.010** (Registration: Name Server), if the NS is distinctive.  
   **Explanation:** Cite `ns1.cdn-test.net`. Candidate is `login-prd.net`. Do not reject a distinctive NS the way you reject a public resolver.

3. **Whole `203.0.113.0/24`. Take or reject, and what is the next lookup if you took same-A instead?**  
   **Answer:** **Reject** **P0202** (Proximity). If you took same-A (**P0103.003**), the next lookup is passive DNS / other names on that A (**0.7** / **2.9.3**).  
   **Explanation:** Shared cloud is coincidence. Same A is a different pivot and names a different lookup.

---

## Additional Instructor Resources

- Next: 2.8.1 Infrastructure hop sentence
- https://github.com/MalasadaTech/defenders-threatmesh-framework
