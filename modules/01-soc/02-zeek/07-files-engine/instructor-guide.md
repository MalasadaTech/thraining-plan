# Instructor Guide – Module 1.2.7 – Files Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.7.1 A / B / C ; 1.2.7.2 2b / 3c / 4c ; 1.2.7.3 2b / 3c / 4c  
- Hunter: 1.2.7.1 B / C / C ; 1.2.7.2 3c / 4c / 4c ; 1.2.7.3 3c / 4c / 4c  
- CTI: 1.2.7.1 A / A / B ; 1.2.7.2 1a / 1a / 2b ; 1.2.7.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a Zeek `files` row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read name, MIME, and hash when Zeek saw a file on the wire.
- How it hooks to the hour before: 1.2.5 GET /update.exe and 1.2.6 envelope mail. This hour is the bytes of that transfer.
- How it hooks to the hour after: 1.2.8 is weird — protocol oddities, not a file hash.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–e only. No lab this pass.
- What we are *not* doing this hour: Host file-create (1.1.3). YARA (1.3). Invented hashes. Harbor / Night Owl names. No lab.
- Extra step: none.

Plant `update.exe` + executable MIME + hash from `203.0.113.88`. Teach `conn_uids` as the join, not a pivot lab. Do not tell the PRD plot.

**Key Teaching Points:**
- Wire file, not host file.
- Name can lie. MIME can disagree.
- Empty hash = not logged.
- `conn_uids` = `uid` on the other Zeek logs.
- A query is specific.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.2.7.1 ; T 1.2.7.2 ; T 1.2.7.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Wire, not host |
| Key Concepts            | 16 min    | Fields a–e; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write name, MIME, hash, tx/rx, conn_uids. Stop on “not Sysmon 11.”

If they describe Temp path: “1.1.3. Different sensor.”  
If they start YARA: “1.3.”  
If they write `files=*` : “Not specific.”

---

## Knowledge Check – Answer Key

1. **A files row is the same as Sysmon 11. True or false?**  
   **Answer:** False. Files is the wire. Sysmon 11 is the host.  
   **Explanation:** Stay-in / outline vs 1.1.3.

2. **update.exe, executable MIME, hash logged, from 203.0.113.88. What occurred?**  
   **Answer:** That IP sent update.exe (executable MIME, hash logged) to the workstation on the wire.  
   **Explanation:** Outline a–d and 1.2.13 task 1.

3. **A query that matches every files row is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (name, MIME, hash, or tx/rx).  
   **Explanation:** 1.2.13 task 2.

---

## Additional Instructor Resources

- Next: 1.2.8 Weird engine
