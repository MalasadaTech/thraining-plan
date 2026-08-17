# Instructor Guide – Module 1.2.5 – HTTP Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.5.1 A / B / C ; 1.2.5.2 2b / 3c / 4c ; 1.2.5.3 2b / 3c / 4c  
- Hunter: 1.2.5.1 B / C / C ; 1.2.5.2 3c / 4c / 4c ; 1.2.5.3 3c / 4c / 4c  
- CTI: 1.2.5.1 A / B / B ; 1.2.5.2 1a / 2b / 3c ; 1.2.5.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a Zeek `http` row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read method, host, URI, User-Agent, and status when Zeek parsed HTTP.
- How it hooks to the hour before: 1.2.4 was the TLS handshake on :443 (SNI empty). This hour is cleartext HTTP — GET /update.exe on :8080 to the same IP.
- How it hooks to the hour after: 1.2.6 is SMTP. File extract of that GET is 1.2.7.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–f only. No lab this pass.
- What we are *not* doing this hour: Process name (1.1.4). uid-pivot as a unit. Night Owl / Harbor names. Body content. No lab.
- Extra step: none.

Plant `GET /update.exe` → `203.0.113.88:8080` `200`. Do not invent a Host header if you do not have one. Do not tell the PRD plot.

**Key Teaching Points:**
- URL = host + URI.
- UA can lie; empty = not logged.
- 200 is not a verdict.
- A query is specific.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.2.5.1 ; T 1.2.5.2 ; T 1.2.5.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | HTTP metadata, not body |
| Key Concepts            | 16 min    | Fields a–f; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write method, host+URI, UA, status, orig/resp. Stop on “no body.”

If they name `powershell.exe`: “1.1.4.”  
If they open TLS SNI: “Different row. 1.2.4.”  
If they write `http=*` : “Not specific.”

---

## Knowledge Check – Answer Key

1. **`host` is the destination IP. True or false?**  
   **Answer:** False. It is the Host header. Dest IP is `id.resp_h`.  
   **Explanation:** Outline b / f.

2. **GET /update.exe to 203.0.113.88:8080, 200, UA empty. What occurred?**  
   **Answer:** That host GET /update.exe from 203.0.113.88 on 8080 and got 200. UA not logged.  
   **Explanation:** Outline a–f and 1.2.9 task 1.

3. **A query that matches every http row is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (method, host, URI, UA, or dest).  
   **Explanation:** 1.2.9 task 2.

---

## Additional Instructor Resources

- Next: 1.2.6 SMTP engine
