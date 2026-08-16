# Instructor Guide – Module 1.2.7 – Files Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.7.1 A / B / C · 1.2.7.2 2b / 3c / 4c · 1.2.7.3 2b / 3c / 4c  
- Hunter: 1.2.7.1 B / C / C · 1.2.7.2 3c / 4c / 4c · 1.2.7.3 3c / 4c / 4c  
- CTI: 1.2.7.1 A / A / B · 1.2.7.2 1a / 1a / 2b · 1.2.7.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read the Zeek `files` log, describe a network file transfer, write a specific query, and pivot with `conn_uids`.

**Key Teaching Points:**
- Wire file, not host **1.1.2**.
- filename, MIME, hashes (where calculated), tx/rx hosts, `source`.
- Join is **`conn_uids`**, not a `uid` column. `fuid` is the file id.
- Stay out of YARA (**1.3**) and extract-to-disk admin.

**Common Student Challenges:**
- Searching `files` for `uid` and finding nothing.
- Treating this as Sysmon 11.
- Inventing a hash when empty.
- Writing `files` with no filter.
- Calling MIME mismatch an automatic incident.
- Grading CTI as SOC 5.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard: `fuid` vs `conn_uids` vs protocol `uid`
- Answer key (this guide)

---

## Learning Objectives

1. Explain filename, MIME, hashes, tx/rx hosts, and connection UID linking.
2. Analyze a Zeek files log entry and describe what occurred.
3. Write a SIEM query for *specific* file-transfer activity.
4. Pivot with `conn_uids` to `conn` / protocol logs.

**Mapped Items:**
- K: 1.2.7.1 – Files engine
- T: 1.2.7.2 – Analyze a Zeek files log
- T: 1.2.7.3 – Create a SIEM query to detect specific file transfer activity

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Wire vs host |
| Purpose of the files log       | 6 min    | |
| Key Fields                     | 16 min   | a–e; conn_uids on the board |
| Walkthrough Examples           | 14 min   | Tie to 1.2.5 / 1.2.6 uids |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~68 min** | Stretch pivot if they search `uid` |

---

## Detailed Teaching Notes

### 1. Purpose of the files Log

**Talking Points:**
- SOC 3: names of fields + one sentence.
- Hunter: already B / 3c — push MIME vs name and the join.
- CTI: A / A / B and 1a / 1a / 2b. Hash-as-artifact awareness at 7. Not a SOC query bar.

**Question to ask:**  
“Did this file cross the *wire*, or was it created on a *host*?”

### 2. Key Fields

**Talking Points:**
- Walk outline a–e. e is `conn_uids`. Write: `files.conn_uids` = `http.uid` = `conn.uid`.
- `fuid` stays in the files world.
- Hashes only when present. MIME is inferred.

**Question to ask:**  
“If I only give you `update.exe`, do you have a story yet?”

### 3. Examples

Reuse uids from HTTP/SMTP examples so the pivot is tangible.

**Example 1:** PDF, matches 1.2.5 Ex 1.  
**Example 2:** exe + HTTP GET from 1.2.5 Ex 3.  
**Example 3:** invoice.jpg / executable MIME + 1.2.6 Ex 2 smtp uid.

---

## Hands-On Exercise – Instructor Guidance

**How to run:** 14–16 minutes. Fail a Sysmon-11 query or a `files | where uid ==` that ignores `conn_uids`.

**Summaries:**
- Example 1: HTTP PDF intranet → workstation; expected.
- Example 2: HTTP `update.exe` / dosexec / unknown hash; lead.
- Example 3: SMTP `invoice.jpg` named, executable MIME; lead.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Zeek files PDF | **files-log event** | `files` |
| Sysmon 11 Temp update.exe | **Not this log** | **1.1.2** |
| Zeek http GET update.exe | **Not this log** | **1.2.5** — join via conn_uids |
| Zeek smtp invoice subject | **Not this log** | **1.2.6** |

**Pseudo-queries:**

```
files
| where source == "HTTP"
| where mime_type has "dosexec"
    or filename endswith ".exe"
    or filename endswith ".dll"
    or filename endswith ".ps1"
```

```
files
| where (filename endswith ".jpg" or filename endswith ".pdf" or filename endswith ".gif")
    and mime_type has "dosexec"
```

Watchlisted-hash variant is also fine: `sha256 == "<watchlist>"`.

**Pivot:** Take a value from `conn_uids`. Search `conn` (and `http`/`smtp`) where `uid` equals that value. `fuid` finds the same file again, not the connection.

---

## Knowledge Check – Answer Key

1. **Purpose vs 1.1.2?**  
   **Answer:** `files` is a file Zeek saw **transferred on the network**. **1.1.2** is a file operation **on the host** (Sysmon / MDE).  
   **Explanation:** Sensor vs endpoint.

2. **Name, MIME, hashes?**  
   **Answer:** `filename`, `mime_type`, `md5` / `sha1` / `sha256` (when calculated).  
   **Explanation:** Outline a–c.

3. **tx_hosts / rx_hosts?**  
   **Answer:** Who **sent** the file and who **received** it.  
   **Explanation:** Outline d.

4. **Join? fuid?**  
   **Answer:** `conn_uids` values are connection `uid`s — search `conn` / `http` / `smtp`. `fuid` identifies the *file* across rows.  
   **Explanation:** Outline e. There is often no `uid` column on `files`.

5. **Name vs MIME?**  
   **Answer:** Write both. Call it a **lead**, not an incident. Still use hashes, tx/rx, source, and the `conn_uids` pivot.  
   **Explanation:** Mismatch is a reason to look, not a conviction.

---

## Additional Instructor Resources

- Local extract policy (whether hashes always populate)
- Next recommended module: 1.2.8 Weird Engine
