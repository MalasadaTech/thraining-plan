# Instructor Guide – Module 1.2.4 – TLS Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.4.1 A / B / C ; 1.2.4.2 2b / 3c / 4c ; 1.2.4.3 2b / 3c / 4c  
- Hunter: 1.2.4.1 B / C / C ; 1.2.4.2 3c / 4c / 4c ; 1.2.4.3 3c / 4c / 4c  
- CTI: 1.2.4.1 A / A / B ; 1.2.4.2 1a / 1a / 2b ; 1.2.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a Zeek TLS (`ssl`) row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read the handshake when the payload is encrypted — SNI, cert, version, cipher.
- How it hooks to the hour before: 1.2.3 was the A record for 203.0.113.88. This hour is TLS on that :443 flow.
- How it hooks to the hour after: 1.2.5 is HTTP — cleartext fields, not the handshake.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–f only. No lab this pass.
- What we are *not* doing this hour: Process name (1.1.4). Phishing catalog. uid-pivot as a unit. Invented JA3. No lab.
- Extra step: none.

Continue `203.0.113.88:443`. Empty SNI matches the host row (URL not logged). Do not invent Night Owl / Harbor names. Do not tell the PRD plot.

**Key Teaching Points:**
- `ssl` log = TLS engine.
- SNI is Client Hello, not the cert subject.
- JA3 only where logged — not a verdict.
- A query is specific.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.2.4.1 ; T 1.2.4.2 ; T 1.2.4.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Handshake, not payload |
| Key Concepts            | 16 min    | Fields a–f; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write SNI vs subject, then JA3 “where available,” then version/cipher, then orig/resp.

If they name `powershell.exe`: “1.1.4.”  
If they treat JA3 as malware: “Not a verdict. Missing means not logged.”  
If they write `ssl=*` : “Not specific.”

---

## Knowledge Check – Answer Key

1. **`server_name` is the name on the server certificate. True or false?**  
   **Answer:** False. It is SNI (Client Hello). The cert name is `subject`.  
   **Explanation:** Outline a–b.

2. **Workstation → 203.0.113.88:443, SNI empty, version/cipher present. What occurred?**  
   **Answer:** That host completed a TLS handshake to 203.0.113.88 on 443. SNI not logged.  
   **Explanation:** Outline a / d–f and 1.2.7 task 1.

3. **A query that matches every ssl row is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (SNI, subject, version, or dest).  
   **Explanation:** 1.2.7 task 2.

---

## Additional Instructor Resources

- Next: 1.2.5 HTTP engine
