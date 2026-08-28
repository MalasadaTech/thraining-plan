# Instructor Guide – Module 2.5.1 – RDAP and WHOIS Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.1 B / C / C ; 2.5.1.1 3c / 4c / 4c  
- Hunter: 2.5.1 A / B / B ; 2.5.1.1 2b / 3c / 4c  
- SOC: 2.5.1 A / A / B ; 2.5.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Query registration on a domain or IP and extract registrar, nameservers, dates, and block-holder fields. Redacted is a fact.

**Context (plain language):**

- What this lesson is for: CTI analysts look up registration on a domain or an IP so they can see who registered the name, who holds the address block, and which nameservers and dates sit on the record. Before they enrich an indicator or name an actor, they have to read that lookup.
- How it hooks to the lesson before: 2.4.1 was file hashes on the same chain.
- How it hooks to the lesson after: 2.6.1 is SOA and other DNS records.
- Why we are doing it this way: registration is a separate lookup from hashes and from DNS SOA. Teach the record here so 2.6 can read SOA without redoing WHOIS.
- What we are *not* doing in this lesson: SOA parse (2.6). Silent Push PDNS (0.7). Nation-state from redaction (2.1.7). The course fiction plot (DYA / PRD). No lab.
- Extra step: none.

Use the same names as the student guide: **WHOIS**, **RDAP**, **registration**, **registrar**, **nameservers**, **created / updated**, **registrant**, **redacted**, **CIDR**, and **org**. **Enrichment** means adding those fields to the indicator. **Attribution** means naming the actor — not this lesson’s product. Classroom givens: the update domain with NS `ns1.cdn-test.net` / `ns2.cdn-test.net`; IP `203.0.113.88` in Example Cloud `203.0.113.0/24`. Sibling `login-prd.net` can be *named*; SOA is next.

**Key Teaching Points:**
- WHOIS and RDAP are the same job: registration lookup. Query RDAP first.
- Redacted registrant is a fact, not an empty card and not a country.
- Distinctive NS is enrichment, not attribution. IP org is who holds the block, not the actor.

**Common Student Challenges:**
- Call redacted “no intel.” Why: the name is hidden so they skip the rest of the record. Example: writing “nothing to extract” when nameservers and created date are on the same lookup.
- Call the IP org the actor. Why: RDAP names a cloud on the block. Example: writing “this is Example Cloud’s campaign” from `203.0.113.0/24`.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.5.1 – RDAP and WHOIS concepts
- T: 2.5.1.1 – Query RDAP/WHOIS and interpret fields for enrichment or attribution

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Registration lookup, not DNS |
| Key Concepts            | 14 min    | Purpose; differences; fields; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~23 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a domain or IP is on the desk, and you have to read registration before you add facts or call the name empty.
- Same job, two protocols. RDAP first (JSON over HTTPS). WHOIS is free text on port 43, used when RDAP has no record. Do not call RDAP “WHOIS in JSON.”
- Walk the field table. Stop on redacted: write **registrant redacted**. Nameservers and dates may still be there.
- Walk the domain given: extract the NS pair, registrar, created date. Distinctive NS is enrichment. Do not claim nation-state. The sibling name can be named; do not read SOA.
- Walk the IP given: `203.0.113.88` → `203.0.113.0/24`, org Example Cloud. Who holds the block, not “theirs.”
- If they parse SOA: that is 2.6.
- If they open Silent Push: that is 0.7.
- If they start the DYA / PRD plot: that fiction is not this lesson.

---

## Knowledge Check – Answer Key

1. **A redacted registrant means you have no intelligence. True or false?**  
   **Answer:** False. Redaction is a fact. Nameservers, registrar, and dates may still be there.  
   **Explanation:** Hidden registrant is not an empty lookup. It is also not a country.

2. **Name one difference between WHOIS and RDAP.**  
   **Answer:** Same job. RDAP is JSON over HTTPS; WHOIS is free text on port 43. Query RDAP first; WHOIS is the fallback.  
   **Explanation:** Any one of those differences is enough. Do not accept “they look up different things.”

3. **You query the update domain and see `ns1.cdn-test.net`. What did you extract, and what must you not claim?**  
   **Answer:** Extracted a nameserver. Do not claim nation-state.  
   **Explanation:** Distinctive NS is enrichment. Attribution is 2.1.7. SOA is 2.6.

---

## Additional Instructor Resources

- Next: 2.6.1 Advanced DNS
