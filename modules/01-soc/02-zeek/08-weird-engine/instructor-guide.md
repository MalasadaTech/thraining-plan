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
Read a Zeek **weird** log and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read the type Zeek flagged and join it to the session. A lead, not a ticket by itself.
- How it hooks to the lesson before: 1.2.7 was the file on the wire. This lesson is “the protocol looked off.”
- How it hooks to the lesson after: 1.3 is rule syntax (SIGMA first). How detections run as a service is 4.x.
- Why we are doing it this way: after the protocol engines, read the log Zeek writes when the protocol looked off-spec, so you can describe a lead and name a specific query.
- What we are *not* doing in this lesson: `notice.log`. The Zeek weird catalog. Process name. PCAP analysis. Course fiction plot. No lab.
- Extra step: none.

Use the same names as the student guide: **weird** log, **event**, `name`, `notice`, `uid`, `id.orig_h` / `id.resp_h`. **Row** is the SIEM-table gloss from the student intro, not the headline word. `notice` on this log is a boolean flag, not the `notice.log` table. The given uses dest `203.0.113.88:8080` so it can sit next to the HTTP GET from 1.2.5 if they remember it. This lesson still describes only the **weird** event.

**Key Teaching Points:**
- `name` is the type you query.
- `notice` on this log is a flag, not the notice log.
- `uid` joins `conn`.
- A query is specific.

**Common Student Challenges:**
- Treat one **weird** event as an incident. Why: the word “weird” sounds like malware. Example: writing “malicious C2” from `data_before_established` with no other logs.
- Open `notice.log` because the field is named `notice`. Why: `notice` on this log is a boolean. Example: leaving the **weird** event to hunt the notices table.
- Write `weird=*` as a “specific” query. Why: the task is a named type. Example: matching every **weird** event instead of `name` `data_before_established`.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.2.8.1 – Weird engine
- T: 1.2.8.2 – Analyze a Zeek weird log and accurately describe what occurred
- T: 1.2.8.3 – Create a SIEM query to detect specific weird activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Lead, not verdict |
| Key Concepts            | 12 min    | Fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: the sensor saw protocol behavior that is off-spec, and you have to say what Zeek flagged before you call it an incident.
- Walk the field table. Stop on `notice`: it is a boolean on this log, not a `notice.log` lesson.
- Walk the given: `data_before_established` to `203.0.113.88:8080`, `uid` present. One sentence. Type, dest, then which `uid` to open on `conn`.
- If they start listing every Zeek weird name: that is not this lesson. Describe the `name` you have.
- If they name a process: that is 1.1.4. Stay on this log.
- If they open `notice.log`: the field is a flag. Stay on the **weird** event.
- If they write `weird=*`: that is not a specific query.

---

## Knowledge Check – Answer Key

1. **A single weird event is an incident. True or false?**  
   **Answer:** False. It is a lead. Many types fire on noisy or broken traffic.  
   **Explanation:** Describe the `name`. Do not open a ticket from one event.

2. **`name` `data_before_established`, dest `203.0.113.88:8080`, `uid` present. What occurred?**  
   **Answer:** Zeek saw data before the TCP handshake finished to that dest. Open `conn` on the `uid`.  
   **Explanation:** The type is data before the handshake. The dest and `uid` are how you join. That is the event. It is not a process name and not an incident.

3. **A query that matches every weird event is specific. True or false?**  
   **Answer:** False. A good query names a specific `name` (or dest).  
   **Explanation:** “All weird events” is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.3.1 SIGMA rules
