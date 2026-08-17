# Instructor Guide – Module 1.2.8 – Weird Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.8.1 A / B / C ; 1.2.8.2 2b / 3c / 4c ; 1.2.8.3 2b / 3c / 4c  
- Hunter: 1.2.8.1 B / C / C ; 1.2.8.2 3c / 4c / 4c ; 1.2.8.3 3c / 4c / 4c  
- CTI: 1.2.8.1 A / A / A ; 1.2.8.2 1a / 1a / 1a ; 1.2.8.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a Zeek `weird` row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read the type Zeek flagged and join it to the session. A lead, not a ticket by itself.
- How it hooks to the hour before: 1.2.7 was the file on the wire. This hour is “the protocol looked off” on that same dest.
- How it hooks to the hour after: 1.3 is rule syntax (SIGMA first). How detections run as a service is 4.x.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c only. No lab this pass.
- What we are *not* doing this hour: notice.log course. Weird catalog. Process name. Harbor / Night Owl. No lab.
- Extra step: none.

Use `data_before_established` on `203.0.113.88:8080` so it sits next to the HTTP GET. Do not tell the PRD plot.

**Key Teaching Points:**
- `name` is the type you query.
- `notice` on the row is a flag, not the notice log.
- `uid` joins `conn`.
- A query is specific.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.2.8.1 ; T 1.2.8.2 ; T 1.2.8.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Lead, not verdict |
| Key Concepts            | 12 min    | Fields a–c; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write name, orig/resp, uid. Stop on “not an incident.”

If they open notice.log: “Flag only. Not this hour.”  
If they name powershell: “1.1.4.”  
If they write `weird=*` : “Not specific.”

---

## Knowledge Check – Answer Key

1. **A single weird row is an incident. True or false?**  
   **Answer:** False. It is a lead. Many names are noise.  
   **Explanation:** Outline a.

2. **data_before_established to 203.0.113.88:8080. What occurred?**  
   **Answer:** Zeek saw data before the handshake finished on that dest. Look at conn/http on the uid.  
   **Explanation:** Outline a–c and 1.2.15 task 1.

3. **A query that matches every weird row is specific. True or false?**  
   **Answer:** False. A good query names a specific `name` (or dest).  
   **Explanation:** 1.2.15 task 2.

---

## Additional Instructor Resources

- Next: 1.3.1 SIGMA rules
