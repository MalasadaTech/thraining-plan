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
Query registration and extract registrar / NS / dates. Redacted is a fact.

**Context (plain language):**

- What this hour is for: CTI analysts read registration so they have NS and created dates to work with.
- How it hooks to the hour before: 2.4.1 was file hashes.
- How it hooks to the hour after: 2.6.1 is SOA and other DNS records.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c. First plant of the distinctive NS pair (story bible).
- What we are *not* doing this hour: SOA parse. PDNS. Nation-state from redaction. No live account lab.
- Extra step: none.

Classroom card: update domain, NS `ns1.cdn-test.net` / `ns2.cdn-test.net`. Sibling name can be *named*; SOA is next.

**Key Teaching Points:**
- RDAP is structured WHOIS.
- Redacted ≠ empty.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.5.1 ; T 2.5.1.1

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Registration |
| Key Concepts            | 12 min    | Fields; NS pair |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write WHOIS vs RDAP vs fields. Walk the NS extract. Fail “redacted = nation-state.”

If they parse SOA: “2.6.”  
If they open Silent Push: “0.7.”

---

## Knowledge Check – Answer Key

1. **Redacted = no intel. True or false?**  
   **Answer:** False. Redaction is a fact. NS and dates may still be there.  
   **Explanation:** Stay-in.

2. **WHOIS vs RDAP?**  
   **Answer:** Same job. RDAP is structured (JSON); WHOIS is text.  
   **Explanation:** Outline a–b.

3. **`ns1.cdn-test.net` on the update domain. Extract / not claim?**  
   **Answer:** Extracted a nameserver. Do not claim nation-state.  
   **Explanation:** Outline c / task 2.

---

## Additional Instructor Resources

- Next: 2.6.1 Advanced DNS
