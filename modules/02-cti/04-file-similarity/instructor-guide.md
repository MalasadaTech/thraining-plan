# Instructor Guide – Module 2.4.1 – Hashing and Similarity Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.1 B / C / C ; 2.4.1.1 3c / 4c / 4d ; 2.4.1.2 3c / 4c / 4c  
- Hunter: 2.4.1 A / B / B ; 2.4.1.1 1a / 2b / 3c ; 2.4.1.2 1a / 2b / 3c  
- SOC: 2.4.1 A / A / B ; 2.4.1.1 1a / 1a / 2b ; 2.4.1.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name a cousin with a similarity hash, and read a code-signing field. Do not invent a match cutoff as policy.

**Context (plain language):**

- What this hour is for: CTI analysts find related samples when SHA256 does not match.
- How it hooks to the hour before: 2.3.1 was the TIP. This hour is the hash type.
- How it hooks to the hour after: 2.5.1 is registration, not file hashes.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d. Classroom thresholds only.
- What we are *not* doing this hour: MD5/SHA identity. VT Relations. Nation-state from unsigned. No lab.
- Extra step: none.

**Key Teaching Points:**
- imphash ≠ identical file.
- Unsigned is a fact.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.4.1 ; T 2.4.1.1 ; T 2.4.1.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Cousins, not SHA256 |
| Key Concepts            | 12 min    | Four tools; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the four rows. Walk same imphash as related compile. Walk unsigned as a fact.

If they open Relations: “2.9.”  
If they say unsigned = nation-state: “2.1.7.”  
If they invent a 90% cutoff as DYA policy: “Shop card or stand-in only.”

---

## Knowledge Check – Answer Key

1. **Same imphash = byte-identical. True or false?**  
   **Answer:** False. Import table, not the whole file.  
   **Explanation:** Outline a.

2. **What does ssdeep/TLSH find that SHA256 does not?**  
   **Answer:** A near-duplicate / cousin when bytes change.  
   **Explanation:** Outline b–c / task 1.

3. **Unsigned update.exe. Learn / not claim?**  
   **Answer:** Learned: no signer. Do not claim nation-state or “malware because unsigned.”  
   **Explanation:** Outline d / task 2.

---

## Additional Instructor Resources

- Next: 2.5.1 RDAP / WHOIS
