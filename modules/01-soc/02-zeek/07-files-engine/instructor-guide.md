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
Read a Zeek `files` event and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read name, MIME, and hash when Zeek saw a file on the wire — who sent it, who received it, and which connection UID joins the other Zeek logs.
- How it hooks to the lesson before: 1.2.6 is envelope mail. This lesson is the file extract on the wire, including an attachment if Zeek hashed it.
- How it hooks to the lesson after: 1.2.8 is weird — protocol oddities, not a file hash.
- Why we are doing it this way: after the protocol engines, read the files extract so you can describe a transfer without treating it as a host file-create.
- What we are *not* doing in this lesson: host file activity (1.1.3). YARA (1.3). PCAP analysis. Invented hashes. No lab.
- Extra step: none.

Use the same names as the student guide: **files log**, **event**, `filename`, `mime_type`, `md5` / `sha1` / `sha256`, `tx_hosts`, `rx_hosts`, and `conn_uids`. **Row** is the SIEM-table gloss from the student intro, not the headline word. The given uses `update.exe` and `203.0.113.88` (MIME `application/x-dosexec`). Teach `conn_uids` as the join, not a pivot lab. Do not tell the course-fiction plot.

**Key Teaching Points:**
- Wire file, not host file.
- Name can lie. MIME can disagree.
- Empty hash means not calculated, not clean.
- `tx_hosts` / `rx_hosts` are sender and receiver, not orig/resp.
- `conn_uids` values are the `uid` on the other Zeek logs.
- A query is specific.

**Common Student Challenges:**
- Treat a `files` event as a Sysmon 11. Why: both mention a file. Example: writing “`update.exe` was created in Temp” from the files log.
- Look for `id.orig_h` on this log. Why: conn and HTTP use orig/resp; files uses tx/rx. Example: calling the workstation the sender because it started the HTTP GET.
- Write a query that matches every `files` event. Why: the task is a named pattern. Example: no filename, MIME, hash, or tx/rx filter.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.2.7.1 – Files engine
- T: 1.2.7.2 – Analyze a Zeek files log and accurately describe what occurred
- T: 1.2.7.3 – Create a SIEM query to detect specific file transfer activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Wire file, not host file |
| Key Concepts            | 16 min    | Fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a download, an attachment, or a hash, and you have to say what moved on the wire.
- Walk the field table. Stop on MIME: `application/x-dosexec` is what Zeek often writes for a Windows executable, not the word “executable.”
- Stop on tx/rx: the host that sent the bytes is `tx_hosts`. For an HTTP GET of a file, that is often the server, not the client.
- Stop on `conn_uids`: copy a value and search other Zeek logs as `uid`. That is the join, not a lab.
- Walk the given: `update.exe`, MIME `application/x-dosexec`, hash logged, from `203.0.113.88` to a workstation. One sentence. Do not describe a Temp path.
- If they describe a Temp path: that is 1.1.3. Different sensor.
- If they start YARA: that is 1.3.
- If they write a query with no name, MIME, hash, or tx/rx filter: that is not specific.

---

## Knowledge Check – Answer Key

1. **A Zeek `files` event is the same thing as a Sysmon 11 file create. True or false?**  
   **Answer:** False. The files log is the wire. Sysmon 11 is the host.  
   **Explanation:** Zeek analyzed bytes on the network. A host file-create is 1.1.3. The host may never write the file.

2. **`update.exe`, MIME `application/x-dosexec`, hash logged, from `203.0.113.88` to a workstation. What occurred?**  
   **Answer:** That IP sent `update.exe` (executable MIME, hash logged) to the workstation on the wire.  
   **Explanation:** Name, MIME, hash, and tx/rx are what you write down. Copy `conn_uids` to join other Zeek logs. Do not add a Temp path.

3. **A query that matches every `files` event is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (name, MIME, hash, or tx/rx).  
   **Explanation:** Every files event is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.2.8 Weird engine
