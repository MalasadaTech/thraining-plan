# Instructor Guide – Module 1.2.2 – Conn Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.2.1 A / B / C ; 1.2.2.2 2b / 3c / 4c ; 1.2.2.3 2b / 3c / 4c  
- Hunter: 1.2.2.1 B / C / C ; 1.2.2.2 3c / 4c / 4c ; 1.2.2.3 3c / 4c / 4c  
- CTI: 1.2.2.1 A / A / B ; 1.2.2.2 1a / 1a / 2b ; 1.2.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a Zeek `conn` row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read the conn log to see who talked to whom on the wire, and how the connection ended.
- How it hooks to the hour before: 1.2.1 said engines extract. This hour is the first extract — five-tuple plus state.
- How it hooks to the hour after: 1.2.3 is DNS. Same flow can have a dns row later.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–e only. No lab this pass.
- What we are *not* doing this hour: Process name (1.1.4). Beacon / scan methodology. Full state catalog. uid-pivot as a unit. No lab.
- Extra step: none.

Continue `203.0.113.88:443` as the given. Do not tell the PRD plot. Do not invent a site VLAN.

**Key Teaching Points:**
- orig vs resp.
- SF / S0 / REJ are enough to start. History is the flag string.
- No process on this row.
- A query is specific.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.2.2.1 ; T 1.2.2.2 ; T 1.2.2.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Wire, not host |
| Key Concepts            | 16 min    | Five fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write orig_h / orig_p / resp_h / resp_p / state. Stop.

If they name `powershell.exe`: “1.1.4. Not on this row.”  
If they start beacon math: “Not this hour. Describe the row.”  
If they write `conn=*` : “Not specific.”

---

## Knowledge Check – Answer Key

1. **`id.orig_h` is the destination. True or false?**  
   **Answer:** False. It is the originator IP. Destination is `id.resp_h`.  
   **Explanation:** Outline a / c.

2. **Workstation → 203.0.113.88:443, SF. What occurred?**  
   **Answer:** That host completed a TCP connection to 203.0.113.88 on 443.  
   **Explanation:** Outline a–e and 1.2.3 task 1.

3. **A query that matches every conn row is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (resp IP or port + state).  
   **Explanation:** 1.2.3 task 2.

---

## Additional Instructor Resources

- Next: 1.2.3 DNS engine
