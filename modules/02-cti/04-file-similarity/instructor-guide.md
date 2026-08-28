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
Name a related sample with a similarity hash, and read a code-signing field. Do not invent a match cutoff as shop policy.

**Context (plain language):**

- What this lesson is for: A sample usually arrives as a file or a hash. SHA256 tells you that exact file. CTI still has to find a cousin and say who claimed the binary. This lesson is those two products.
- How it hooks to the lesson before: 2.3.1 was the internal TIP — what this shop already holds. This lesson is the hash type on a file you already have.
- How it hooks to the lesson after: 2.5.1 is registration (WHOIS / RDAP), not file hashes.
- Why we are doing it this way: identity hashes answer “same file.” Similarity hashes and signing fields answer “cousin” and “who claimed it” before anyone opens Relations or registration.
- What we are *not* doing in this lesson: MD5 / SHA identity (**1.2.7**). VirusTotal Relations (**2.9**). TLS certificates (**1.2.4**). Nation-state from unsigned (**2.1.7**). No lab.
- Extra step: none.

Use the same names as the student guide: **imphash**, **ssdeep**, **TLSH**, and **code-signing**. Classroom stand-ins are **ssdeep 50 or higher** and **TLSH distance 30 or lower**. Those are not DYA policy. The given uses the course-fiction sample `update.exe`. Do not turn it into the intro plot.

**Key Teaching Points:**
- imphash is the PE import table, not the whole file. Same imphash is not byte-identical.
- ssdeep high is close. TLSH distance low is close. Do not read the two scores the same way.
- Unsigned is a fact. It is not malware and not a country.

**Common Student Challenges:**
- Treat same imphash as the same file. Why: imphash is the import list, not the bytes. Example: writing “identical to `update.exe`” from a matching imphash and a different SHA256.
- Read a TLSH distance like an ssdeep score. Why: the numbers run opposite ways. Example: treating TLSH 80 as “80% similar.”
- Upgrade “unsigned” to malware or nation-state. Why: unsigned means no signer. Example: “unsigned, so this is PRD.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.4.1 – Hashing and similarity concepts
- T: 2.4.1.1 – Use file similarity hashes to identify related samples
- T: 2.4.1.2 – Extract and interpret certificate / code-signing information from a file

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Cousin + who claimed it, not SHA256 |
| Key Concepts            | 12 min    | Four tools; opposite scores; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a sample arrives, SHA256 does not match, and you still have to name a cousin and who claimed the binary.
- Walk the four-row table. Stop on imphash: PE import table only, related compile or packer family, not the same file.
- Stop on scores: ssdeep higher is closer; TLSH distance lower is closer. Classroom stand-ins are ssdeep 50 and TLSH distance 30. They are not shop policy.
- Walk the related-sample given: same imphash as `update.exe`, different SHA256 → related compile. ssdeep 20 → not related on the classroom card.
- Walk the certificate given: extract signer / issuer / dates, or **unsigned**. Do not swap issuer for signer. This is the signature on the file, not a TLS certificate.
- If they open Relations: that is 2.9.
- If they say unsigned means nation-state: that is 2.1.7.
- If they invent a 90% cutoff as DYA policy: classroom card or stand-in only.

---

## Knowledge Check – Answer Key

1. **Same imphash means the two files are byte-identical. True or false?**  
   **Answer:** False. imphash is the PE import table, not the whole file.  
   **Explanation:** Same imphash means a related compile or packer family. The SHA256 can still differ.

2. **What does ssdeep (or TLSH) find that SHA256 does not?**  
   **Answer:** A near-duplicate / cousin when bytes change.  
   **Explanation:** SHA256 flips on a one-byte change. ssdeep (high score) and TLSH (low distance) can still call the files related. They score in opposite directions.

3. **You extract “unsigned” from `update.exe`. What did you learn, and what must you not claim?**  
   **Answer:** Learned: no signer. Do not claim nation-state or “malware because unsigned.”  
   **Explanation:** Unsigned is a missing field. Attribution is 2.1.7. Signed would still not mean trusted.

---

## Additional Instructor Resources

- Next: 2.5.1 RDAP / WHOIS
