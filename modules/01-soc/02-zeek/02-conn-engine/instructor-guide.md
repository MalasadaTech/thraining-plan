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
Read a Zeek `conn` event and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read the `conn` log to see who talked to whom on the wire, and how the connection ended.
- How it hooks to the lesson before: 1.2.1 said engines extract protocol data. This lesson is the first extract — originator, responder, and state.
- How it hooks to the lesson after: 1.2.3 is DNS. The same flow can have a `dns` event later.
- Why we are doing it this way: after the Zeek map, read one engine so you can describe a connection before you open DNS or TLS.
- What we are *not* doing in this lesson: the initiating process (1.1.4). DNS and later engines. Beacon or scan methodology. A full `conn_state` catalog. PCAP analysis. No lab.
- Extra step: none.

Use the same names as the student guide: **`conn` log**, **event**, **originator**, **responder**, **`conn_state`**, and **`history`**. **Row** is the SIEM-table gloss from the student intro, not the headline word. Keep `203.0.113.88:443` as the given. Do not tell the course-fiction plot. Do not invent a site VLAN.

**Key Teaching Points:**
- Originator versus responder. `id.orig_h` is not the destination, and it is not automatically internal.
- `SF` / `S0` / `REJ` are enough to start. History is the flag string.
- No process on this log.
- A query is specific, not every connection.

**Common Student Challenges:**
- Treat `id.orig_h` as the destination, or as “our host.” Why: “source” sounds like the internal workstation. Example: writing the dest IP in `id.orig_h` because the workstation is “ours.”
- Name a process from the `conn` log. Why: 1.1.4 trained initiating process. Example: writing `powershell.exe` from a Zeek `conn` event.
- Write a query that matches every connection. Why: the task is a named pattern. Example: `conn=*` with no responder IP, port, or state.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.2.2.1 – Conn engine
- T: 1.2.2.2 – Analyze a Zeek conn log and accurately describe what occurred
- T: 1.2.2.3 – Create a SIEM query to detect specific connection activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

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

**Talking Points:**
- Open with the job: an alert names an IP or a connection, and you have to say who talked to whom on the wire and how it ended.
- Walk the field table. Stop on originator: it is not destination, and it is not “internal.”
- Teach `SF`, `S0`, and `REJ`. If they ask for every rare state, say what the field shows and stay on those three.
- Walk the given: workstation → `203.0.113.88:443`, `conn_state` `SF`. One sentence. Originator, responder, port, state.
- If they name `powershell.exe`: that is 1.1.4. It is not on this log.
- If they start beacon math or a scan write-up: stay on this event. Describe who talked to whom and how it ended.
- If they write `conn=*`: that is not a specific query.

---

## Knowledge Check – Answer Key

1. **`id.orig_h` is the destination IP. True or false?**  
   **Answer:** False. It is the originator IP. Destination is `id.resp_h`.  
   **Explanation:** Originator started the talk from Zeek’s view. Responder is who was contacted.

2. **Workstation → 203.0.113.88:443, SF. What occurred?**  
   **Answer:** That host completed a TCP connection to 203.0.113.88 on 443.  
   **Explanation:** Originator, responder, port, and `SF` (established and torn down). Who launched the socket is not on this log.

3. **A query that matches every connection is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (responder IP or port + state).  
   **Explanation:** “Every connection” is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.2.3 DNS engine
