# Module 1.2.7 – Files Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.7.1 A / B / C · 1.2.7.2 2b / 3c / 4c · 1.2.7.3 2b / 3c / 4c  
- Hunter: 1.2.7.1 B / C / C · 1.2.7.2 3c / 4c / 4c · 1.2.7.3 3c / 4c / 4c  
- CTI: 1.2.7.1 A / A / B · 1.2.7.2 1a / 1a / 2b · 1.2.7.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the Zeek `files` log: filename, MIME type, hashes, source/destination hosts, and connection UID linking.
2. Analyze a Zeek files log entry and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* file-transfer pattern — not “all files.”
4. Pivot from a `files` row to `conn` / `http` / `smtp` using `conn_uids` (and `fuid` when needed).

**Mapped Proficiency Items:**
- K: 1.2.7.1 – Files engine
- T: 1.2.7.2 – Analyze a Zeek files log and accurately describe what occurred
- T: 1.2.7.3 – Create a SIEM query to detect specific file transfer activity

---

## 1. Key Concepts

### 1.1 Purpose of the files Log

Zeek’s files engine writes the **`files` log**. Each row is a **file Zeek saw transferred on the network** (HTTP download, SMTP attachment, and similar). It is **not** a host file-create row (**1.1.3** `DeviceFileEvents` / Sysmon 11).

You get a name (when Zeek had one), a MIME type, hashes (when calculated), who sent and who received, and one or more **connection UIDs** that join this file to `conn` and the protocol log that carried it.

| This lesson | Other |
|-------------|-------|
| File *on the wire* | File *on the host* — **1.1.3** |
| `conn_uids` → `http` / `smtp` / `ssl` / `conn` | Weird types — **1.2.8** |
| Hashes Zeek computed | YARA on extracted bytes — **1.3** |

If filename or a hash is empty, say so. Do not invent it. Not every file is extracted to disk.

### 1.2 Key Fields

| Field | Description | Why it matters |
|-------|-------------|----------------|
| `ts` | Timestamp | When Zeek saw the transfer |
| `fuid` | File identifier | Joins multiple sightings of *this file* |
| `conn_uids` | Connection UID(s) | **The outline’s connection UID** — search `conn` / `http` / `smtp` for the same value |
| `tx_hosts` | Sender IP(s) | Who transmitted the file |
| `rx_hosts` | Receiver IP(s) | Who received it |
| `source` | Analyzer that saw it (`HTTP`, `SMTP`, …) | How it crossed the wire |
| `filename` | Name when known | Can lie or be missing |
| `mime_type` | Content type Zeek inferred | Can disagree with the name |
| `md5` / `sha1` / `sha256` | Hashes when calculated | Bytes of *this* transfer |

There is often **no** single `uid` column like `http` / `smtp`. The link is **`conn_uids`**. Treat each value in that list as a `uid` on the other logs.

**Most critical for daily work:** `filename`, `mime_type`, `sha256` (or md5/sha1), `tx_hosts`, `rx_hosts`, `conn_uids`, `source`, `fuid`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| `filename` `q3-notes.pdf`, `mime_type` `application/pdf`, hash known or “not logged” | `.exe` / `.dll` / `.ps1` over HTTP, or MIME `application/x-dosexec` |
| MIME matches the name | Name says `.jpg`; MIME says executable (or the reverse) |
| `source` HTTP from the intranet web server | SMTP attachment `.doc` / `.exe` from an unexpected `tx_hosts` |
| `rx_hosts` is a user workstation pulling a PDF | Server receiving an unexpected upload |
| Hash matches a catalogued document | Hash unknown **and** executable MIME / name |

**filename:** Present when the protocol gave a name (HTTP Content-Disposition, URI tail, SMTP filename). Empty → “not logged.” Name can lie.

**MIME type:** What Zeek *thinks* the bytes are. A mismatch with the name is a lead, not automatic malware.

**Hashes:** SHA256 / SHA1 / MD5 of the transferred bytes **when Zeek hashed them**. Empty ≠ clean. This is not the host `DeviceFileEvents` SHA256 from **1.1.3** — same idea, different sensor.

**tx_hosts / rx_hosts:** Source and destination of the *file*, not always identical to a single 5-tuple if Zeek attached the file to more than one connection.

**conn_uids:** Copy a value. Search `conn` for `uid == that value`. Then `http` or `smtp` the same way. That is the pivot this lesson owes.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal HTTP PDF

```
ts: 2026-08-15T14:10:03.400Z
fuid: FPdf12Ab34Cd56Ef
conn_uids: CHttpAb12Cd34Ef56
source: HTTP
tx_hosts: 10.10.8.20
rx_hosts: 10.10.50.23
filename: q3-notes.pdf
mime_type: application/pdf
sha256: (matches catalogued PDF)
```

**What occurred:** Intranet web server sent `q3-notes.pdf` (PDF MIME, known hash) to workstation `10.10.50.23` over HTTP. The `conn_uids` value is the same `uid` as Example 1 in **1.2.5**. Expected.

**Not done:** Did not rewrite this as a host Sysmon 11. Did not open YARA (**1.3**).

### Example 2: HTTP Executable, Generic Name (Lead)

```
fuid: FExe98Xy76Zt54Uv
conn_uids: CHttpQr11Mn22Op33
source: HTTP
tx_hosts: 198.51.100.80
rx_hosts: 10.10.22.17
filename: update.exe
mime_type: application/x-dosexec
md5: (not in catalog)
sha1: (not in catalog)
sha256: (not in catalog)
```

**What occurred:** Internet host sent `update.exe` (executable MIME, hashes not catalogued) to an internal workstation over HTTP. `conn_uids` matches the **1.2.5** Example 3 GET of `/payload/update.exe`.

**Interpretation:** Lead. Describe name + MIME + hash-not-in-catalog + tx/rx + source. Pivot `conn_uids` to `http` and `conn`. Do not treat the name as the host path. Do not write a YARA rule here.

### Example 3: SMTP Attachment, Name / MIME Disagree (Lead)

```
fuid: FAtt11Qr22Mn33Op
conn_uids: CSmtpXy98Zt76Uv54
source: SMTP
tx_hosts: 203.0.113.88
rx_hosts: 10.10.8.25
filename: invoice.jpg
mime_type: application/x-dosexec
sha256: (not in catalog)
```

**What occurred:** An SMTP transfer named the file `invoice.jpg` but Zeek’s MIME type is **executable**. Sender is the internet IP from **1.2.6** Example 2. Receiver is the internal mail server.

**Interpretation:** Lead. Name vs MIME mismatch. Pivot `conn_uids` to `smtp` and `conn`. Write hashes if present. Do not call it a host file create (**1.1.3**).

---

## 3. Hands-On Exercise

**Objective:** Practice describing files-log rows and writing queries that find a specific transfer.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (expected vs lead).
2. Write **two SIEM-style pseudo-queries**:
   - One for **executable MIME or** `.exe` / `.dll` / `.ps1` **filename** transferred over HTTP (`source == "HTTP"`).
   - One for **filename / MIME disagreement** (e.g. name ends `.jpg` / `.pdf` / `.gif` and `mime_type` is an executable type) **or** SHA256 you have watchlisted.
3. Explain how you would pivot from a suspicious `files` entry to `conn` and the protocol log using **`conn_uids`**. What is `fuid` for?
4. For each item below, say **files-log event** or **not this log**. Give one reason.
   - Zeek `files` `q3-notes.pdf` / `application/pdf`
   - Sysmon 11 `Temp\update.exe`
   - Zeek `http` GET `/payload/update.exe`
   - Zeek `smtp` invoice subject

**Expected Outcome:**
- Accurate short summaries
- Two specific file-transfer queries
- A correct `conn_uids` (and `fuid`) explanation
- Four identifications with a reason each

---

## 4. Knowledge Check

1. What is the primary purpose of the Zeek `files` log? How is it different from host file activity (**1.1.3**)?
2. Which fields carry **filename**, **MIME type**, and **hashes**?
3. What are `tx_hosts` and `rx_hosts`?
4. How do you join a `files` row to `conn` / `http` / `smtp`? What is `fuid`?
5. Filename says `.jpg` and `mime_type` is executable. What do you write, and what do you still need?

---

## 5. Summary

- The files engine writes the `files` log: a file **on the wire**, not on the host.
- Critical fields: `filename`, `mime_type`, hashes, `tx_hosts` / `rx_hosts`, `source`, `conn_uids`, `fuid`.
- Empty name or hash → “not logged.” MIME vs name mismatch is a lead.
- Pivot with **`conn_uids`** (those values *are* the connection `uid`s). `fuid` tracks the file.
- Next: Weird engine (**1.2.8**). YARA is **1.3**.

---

## 6. References & Further Reading

- Zeek files.log documentation: https://docs.zeek.org/en/current/scripts/base/files/main.zeek.html
- Related modules:
  - 1.1.3 – File system activity (host)
  - 1.2.2 – Conn engine
  - 1.2.5 – HTTP engine
  - 1.2.6 – SMTP engine (previous)
  - 1.2.8 – Weird engine (next)
  - 1.3.3 – YARA rules
