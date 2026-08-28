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
Read a Zeek `http` log and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read Zeek HTTP logs to see a request and response on the wire — method, host, URI, User-Agent, status, and who talked to whom.
- How it hooks to the lesson before: 1.2.4 was the TLS handshake. This lesson is HTTP that Zeek still parsed.
- How it hooks to the lesson after: 1.2.6 is SMTP. File extract of an HTTP GET is 1.2.7.
- Why we are doing it this way: after the handshake, read one protocol extract so you can describe a request before you open mail or files.
- What we are *not* doing in this lesson: the initiating process (1.1.4). uid-pivot as a unit. Body content. SMTP fields. Course-fiction plot. No lab.
- Extra step: none.

Use the same names as the student guide: **method**, **host**, **URI**, **URL**, **User-Agent**, **status**, and **orig / resp**. **Row** is the SIEM-table gloss from the student intro, not the headline word. **host** is the Host header, not the destination IP. The given uses `GET /update.exe` to `203.0.113.88:8080` with status `200` and an empty User-Agent. Do not invent a Host header if the log does not have one. Do not turn the given into the intro plot.

**Key Teaching Points:**
- URL is host + URI. There is often no single `url` field.
- User-Agent can lie. Empty means it was not logged.
- Status 200 is not a verdict.
- A query is specific, not every `http` log.

**Common Student Challenges:**
- Treat `host` as the destination IP. Why: the word sounds like a machine. Example: writing `203.0.113.88` as `host` when that value is `id.resp_h`.
- Treat status 200 as benign. Why: 200 means the server answered OK, not that the request is safe. Example: calling `/update.exe` fine because the status is 200.
- Write `http=*` as a “specific” query. Why: the task is a named pattern. Example: every HTTP log with no method, host, URI, User-Agent, or dest filter.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.2.5.1 – HTTP engine
- T: 1.2.5.2 – Analyze a Zeek HTTP log and accurately describe what occurred
- T: 1.2.5.3 – Create a SIEM query to detect specific HTTP activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | HTTP request/response on the wire, not body or process |
| Key Concepts            | 16 min    | Fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a web request, and you have to say method, host, URI, status, and who talked to whom.
- Walk the field table. Stop on `host`: it is the Host header, not `id.resp_h`.
- URL is host plus URI. Do not invent a Host header if the log does not have one.
- Stop on status: 200 is not benign. 404 is not safe.
- Walk the given: `GET /update.exe` to `203.0.113.88:8080`, status `200`, User-Agent empty. One sentence. Do not name a process. Do not invent the body.
- If they name `powershell.exe`: that is 1.1.4. Stay on this log.
- If they open TLS SNI: that is a different log. 1.2.4.
- If they write `http=*`: that is not a specific query.

---

## Knowledge Check – Answer Key

1. **`host` is the destination IP. True or false?**  
   **Answer:** False. It is the Host header. Destination IP is `id.resp_h`.  
   **Explanation:** `host` is what the client put in the Host header. Empty means it was not logged, not that there was no destination.

2. **GET /update.exe to 203.0.113.88:8080, 200, User-Agent empty. What occurred?**  
   **Answer:** The originator requested GET `/update.exe` from `203.0.113.88` on port 8080 and received status 200. User-Agent was not logged.  
   **Explanation:** Describe this log only. Do not invent a Host header. Do not name a process. Do not mix in a TLS handshake.

3. **A query that matches every `http` log is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (method, host, URI, User-Agent, or dest).  
   **Explanation:** Every HTTP log is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.2.6 SMTP engine
