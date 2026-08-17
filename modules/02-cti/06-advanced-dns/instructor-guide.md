# Instructor Guide – Module 2.6.1 – Advanced DNS Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.6.1 B / C / C ; 2.6.1.1 3c / 4c / 4d  
- Hunter: 2.6.1 B / C / C ; 2.6.1.1 2b / 3c / 4c  
- SOC: 2.6.1 A / A / B ; 2.6.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read an SOA and use NS / sibling / same A as enrichment. Shared cloud is not “theirs.”

**Context (plain language):**

- What this hour is for: CTI analysts see who runs the zone and whether another name shares that control.
- How it hooks to the hour before: 2.5.1 planted the NS pair.
- How it hooks to the hour after: 2.7.1 maps behavior (ATT&CK), not DNS records.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c. Story bible sibling + NS + SOA RNAME land here.
- What we are *not* doing this hour: Zeek dns. RDAP redo. PDNS. No lab.
- Extra step: none.

**Key Teaching Points:**
- SOA = MNAME / RNAME / serial.
- Same NS + same A can be a sibling. /24 is shared hosting.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.6.1 ; T 2.6.1.1

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Who runs the zone |
| Key Concepts            | 12 min    | SOA; sibling |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write SOA fields. Walk `hostmaster.cdn-test.net`. Walk sibling same NS + same A. Reject whole /24.

If they open Zeek: “1.2.3.”  
If they redo RDAP: “2.5 is done.”

---

## Knowledge Check – Answer Key

1. **This hour is Zeek dns. True or false?**  
   **Answer:** False. Authoritative records.  
   **Explanation:** Stay-in.

2. **Two SOA fields?**  
   **Answer:** MNAME (primary NS) and RNAME (responsible mailbox). Serial is also on the record.  
   **Explanation:** Outline a.

3. **Same NS + same A on login-prd.net. Say / not say?**  
   **Answer:** Related name / sibling. Do not say the whole `203.0.113.0/24` is theirs.  
   **Explanation:** Outline c / task 2.

---

## Additional Instructor Resources

- Next: 2.7.1 ATT&CK for CTI
