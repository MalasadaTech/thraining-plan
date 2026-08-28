# Instructor Guide – Module 1.1.4 – Network Activity (Endpoint)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.4.1 A / B / C ; 1.1.4.2 2b / 3c / 4c ; 1.1.4.3 2b / 3c / 4c  
- Hunter: 1.1.4.1 A / B / B ; 1.1.4.2 1a / 2b / 3c ; 1.1.4.3 1a / 2b / 3c  
- CTI: 1.1.4.1 A / A / A ; 1.1.4.2 1a / 1a / 1a ; 1.1.4.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a host-network event and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read host-network events on a host to see which process on this device talked, and to where.
- How it hooks to the lesson before: 1.1.3 is file activity on the same host telemetry.
- How it hooks to the lesson after: 1.1.5 is registry activity on the same host telemetry. Zeek protocol fields are 1.2.
- Why we are doing it this way: after file, the connect on the same host telemetry.
- What we are *not* doing in this lesson: Zeek `conn` / `dns` / JA3 (1.2). Sysmon install. Process-create or file-create write-ups. No lab.
- Extra step: none.

Use the same names as the student guide: **host-network event**, **initiating process**, **connect**, and **DNS query**. **Row** is the SIEM-table gloss from the student intro, not the headline word. MDE `ActionType` on this table: **ConnectionSuccess**. Do not invent a value. DNS on the endpoint is Sysmon 22 when that event is in the feed. The given continues the 1.1.2 encoded PowerShell (`powershell.exe -enc …` to `203.0.113.88:443`). Do not turn it into the intro plot.

**Key Teaching Points:**
- Endpoint network event, not Zeek.
- Initiating process is why this log exists next to Zeek.
- Event 3 is a connect. Event 22 is DNS, and only if the feed has it.
- A query is specific, not “all connections.”

**Common Student Challenges:**
- Treat a Zeek `conn` log as naming the process. Why: both describe a connection. Example: writing “powershell connected” from a Zeek `conn` that has no `Image`.
- Write `DeviceNetworkEvents` with no filter as a “specific” query. Why: the task is a named pattern. Example: `DeviceNetworkEvents` with no initiator or destination filter.
- Describe the process create as the network story. Why: the create is 1.1.2. Example: “wscript launched encoded PowerShell” when the event is `ConnectionSuccess` to an IP.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.1.4.1 – Network activity (endpoint) concepts
- T: 1.1.4.2 – Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.4.3 – Create a SIEM query to detect specific endpoint network activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Host-network event, not Zeek |
| Key Concepts            | 16 min    | Fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a host, and you have to say which process on this device talked, and to where.
- Walk the field table. Stop on initiating process: that is the point of this lesson versus Zeek.
- MDE connect is `ConnectionSuccess`. DNS on the endpoint is Sysmon 22. Do not invent an `ActionType` on `DeviceNetworkEvents`.
- Walk the given: `powershell.exe -enc …` → `203.0.113.88:443` as `ConnectionSuccess`, `RemoteUrl` empty. One sentence. Initiator + dest IP/port. URL not logged.
- If they start installing Sysmon: that is not this lesson.
- If they paste a Zeek `conn` and ask who did it: that is not on that log. Stay on the host-network event.
- If they describe the process create of `wscript` or the Temp file create: that is 1.1.2 or 1.1.3. Stay on the connect.
- If they write `DeviceNetworkEvents` with no filter: that is not a specific query.

---

## Knowledge Check – Answer Key

1. **A Zeek `conn` log names the initiating process. True or false?**  
   **Answer:** False. Zeek sees the wire. The process is on the host-network event (Sysmon 3 / `DeviceNetworkEvents`).  
   **Explanation:** A Zeek `conn` log can tell you the IPs and ports. It does not name the process that opened the socket.

2. **`powershell.exe -enc …` has `ConnectionSuccess` to `203.0.113.88:443` and no `RemoteUrl`. In one sentence, what occurred?**  
   **Answer:** Hidden encoded PowerShell successfully connected outbound TCP/443 to that IP. URL not logged.  
   **Explanation:** The image name of `powershell.exe` can still look fine. The initiator, destination, and empty URL are the event.

3. **A SIEM query that matches every endpoint network event is a good “specific endpoint network activity” query. True or false?**  
   **Answer:** False. A good query names a specific pattern (initiator + dest port or remote IP).  
   **Explanation:** “All connections” is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.1.5 Registry activity
