# Instructor Guide – Module 1.2.3 – DNS Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.3.1 A / B / C ; 1.2.3.2 2b / 3c / 4c ; 1.2.3.3 2b / 3c / 4c  
- Hunter: 1.2.3.1 B / C / C ; 1.2.3.2 3c / 4c / 4c ; 1.2.3.3 3c / 4c / 4c  
- CTI: 1.2.3.1 A / B / B ; 1.2.3.2 1a / 2b / 3c ; 1.2.3.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a Zeek `dns` row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read the dns log to see the name that was asked and what answered.
- How it hooks to the hour before: 1.2.2 was who talked to 203.0.113.88:443. This hour is the lookup that can sit next to that flow.
- How it hooks to the hour after: 1.2.4 is TLS — SNI / cert on the same wire, not DNS.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d only. No lab this pass.
- What we are *not* doing this hour: Process name (1.1.4). DGA / tunneling hunt. uid-pivot as a unit. No lab.
- Extra step: none.

Continue `203.0.113.88` as the A answer. Do not invent Night Owl / Harbor resolver names. Do not tell the PRD plot.

**Key Teaching Points:**
- Question vs answer.
- Record types: A, AAAA, MX, CNAME, NS, TXT.
- orig_h asked; resp_h is the resolver, not the A record.
- A query is specific.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.2.3.1 ; T 1.2.3.2 ; T 1.2.3.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Name lookup, not conn |
| Key Concepts            | 16 min    | Fields a–d; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write query / answers / qtype / orig vs resp. Stop on resp_h: resolver, not the A.

If they name `powershell.exe`: “1.1.4.”  
If they start DGA: “Not this hour. Describe the row.”  
If they write `dns=*` : “Not specific.”

---

## Knowledge Check – Answer Key

1. **`id.resp_h` is the IP the name resolved to. True or false?**  
   **Answer:** False. It is the resolver. The A record is in `answers`.  
   **Explanation:** Outline b / d.

2. **Workstation A-query, answers 203.0.113.88. What occurred?**  
   **Answer:** That host asked for that name and got A 203.0.113.88.  
   **Explanation:** Outline a–d and 1.2.5 task 1.

3. **A query that matches every dns row is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (`query`, type, or `answers`).  
   **Explanation:** 1.2.5 task 2.

---

## Additional Instructor Resources

- Next: 1.2.4 TLS engine
