# Instructor Guide – Module 1.2.2 – Conn Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:** SOC A/2b → B/3c → C/4c | Hunter B/3c → C/4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach students how to read and interpret the most important Zeek log — the `conn` log. This is the foundation for almost all network-based triage and hunting.

**Key Teaching Points:**
- `conn` is the starting point for most network investigations.
- Students must become fluent in the core fields and connection states.
- Emphasize practical interpretation over memorizing every possible state.
- Teach the habit of pivoting with `uid`.

**Common Student Challenges:**
- Confusing originator vs responder.
- Memorizing too many `conn_state` values at once (focus on SF, S0, REJ, RSTO, S1 first).
- Not understanding why `uid` matters until they see a multi-log pivot.

**Required Materials:**
- Student Guide
- Sample `conn` log entries (can use the examples in the guide)
- SIEM or text editor for query practice (optional)

---

## Learning Objectives

1. Explain the purpose of the Zeek `conn` log.
2. Identify and interpret the most important fields.
3. Recognize common connection states and their meaning.
4. Analyze a `conn` log entry and accurately describe what occurred.
5. Create basic SIEM queries for interesting connection activity.

**Mapped Items:**
- K: 1.2.2.1 – Conn engine
- T: 1.2.2.2 – Analyze a Zeek conn log
- T: 1.2.2.3 – Create a SIEM query for connection activity

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | |
| Purpose of conn log            | 6 min    | |
| Key Fields deep dive           | 15 min   | Most important section |
| Connection States              | 12 min   | Focus on the top 6–7 states |
| Walkthrough Examples           | 12 min   | Work through all three examples |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~75 min** | |

---

## Detailed Teaching Notes

### 1. Purpose of the conn Log

**Talking Points:**
- Every connection Zeek sees generates one `conn` record.
- It is protocol-agnostic — works for TCP, UDP, ICMP.
- It is the “index” that ties other protocol logs together via `uid`.

**Question to ask:**  
“If you could only keep one Zeek log, which would it be and why?”  
(Most experienced analysts will say `conn`.)

### 2. Key Fields

**Teaching approach:**
- Project a real or sample `conn` entry.
- Walk field by field, but spend the most time on:
  - `id.orig_h` / `id.resp_h` / ports
  - `duration`
  - `orig_bytes` / `resp_bytes`
  - `conn_state`
  - `uid`

**Originator vs Responder reminder:**  
Originator = the side that started the connection (usually the client).  
Responder = the side that received the initial SYN (usually the server).

### 3. Connection States

**Focus list for this module (in order of importance):**
1. SF – Normal
2. S0 – Attempt, no reply
3. REJ – Rejected
4. RSTO / RSTR – Reset
5. S1 – Established but not terminated
6. OTH – Midstream / partial

**Teaching tip:**  
Create a quick “cheat sheet” on the whiteboard or slide with just these six states and one-line meanings.

### 4. Examples

Work through all three examples in the Student Guide interactively. Ask students to interpret before you reveal the explanation.

**Extra teaching point for Example 3 (long duration):**  
Ask: “What additional Zeek logs would you pivot to using the `uid`?”  
Expected answers: ssl, http, files, weird, etc.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- After completion, review answers as a group.

**What good answers look like:**

**Summaries:**
- Example 1: Clean HTTPS connection from internal host to external web server.
- Example 2: Failed connection attempt (possible scan or blocked traffic) to port 445.
- Example 3: Very long-lived connection with low data volume — possible beacon.

**Queries (pseudo examples):**
```
duration > 3600
```
```
(conn_state = "S0" OR conn_state = "REJ") 
AND id.resp_p IN (445, 3389, 22) 
AND id.orig_h IN internal_ranges
```

**uid explanation:**  
The `uid` is a unique identifier that links the `conn` record to related protocol logs (http, dns, ssl, files, etc.) for the same connection.

---

## Knowledge Check – Answer Key

1. **What is the primary purpose of the Zeek `conn` log?**  
   **Answer:** To record every connection observed by Zeek, providing foundational visibility into who talked to whom, for how long, and how much data was transferred.

2. **Which field uniquely identifies a connection and links it to other Zeek logs?**  
   **Answer:** `uid`

3. **What does the connection state `SF` indicate?**  
   **Answer:** Normal establishment and termination (clean, successful connection).

4. **What does the connection state `S0` usually indicate?**  
   **Answer:** A connection attempt was seen but no reply was received (host down, filtered, or scan).

5. **Name three fields you would examine when looking for possible C2 beaconing.**  
   **Answer:** Any three of: `duration`, `orig_bytes`, `resp_bytes`, `conn_state`, `id.resp_h`, `id.resp_p`, `history`

---

## Additional Instructor Resources

- Zeek conn.log documentation  
- Internal list of known-good long-lived connections (if available)  
- Next module recommendation: 1.2.3 DNS Engine or 1.2.5 HTTP Engine
