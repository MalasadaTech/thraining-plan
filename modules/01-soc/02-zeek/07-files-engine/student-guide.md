# Module 1.2.7 – Files Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.7.1 A / B / C ; 1.2.7.2 2b / 3c / 4c ; 1.2.7.3 2b / 3c / 4c  
- Hunter: 1.2.7.1 B / C / C ; 1.2.7.2 3c / 4c / 4c ; 1.2.7.3 3c / 4c / 4c  
- CTI: 1.2.7.1 A / A / B ; 1.2.7.2 1a / 1a / 2b ; 1.2.7.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek **files** event: name, MIME type, hash, who sent and received it, and the connection UID that joins other Zeek logs.
2. Describe what a `files` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.7.1 – Files engine
- T: 1.2.7.2 – Analyze a Zeek files log and accurately describe what occurred
- T: 1.2.7.3 – Create a SIEM query to detect specific file transfer activity

---

## 1. Key Concepts

SOC analysts read the Zeek **files** log to see a file on the **wire**. An alert may name a download, an attachment, or a hash. The job in this lesson is to say what moved: the name if the protocol gave one, the MIME type, the hash if Zeek calculated it, who sent it, and who received it. **1.2.1** said engines extract protocol. This lesson is the **files** engine. It is **not** host file activity (**1.1.3**). It is **not** YARA (**1.3**).

The **files** log is one **event** for a file Zeek analyzed on the wire. In a SIEM, that event usually shows up as a **row** in a files table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **File name** | `filename` — when the protocol gave one. It can lie. Empty means not logged. |
| **MIME type** | `mime_type` — what Zeek thinks the bytes are (for a Windows executable, often `application/x-dosexec`). It can disagree with the name. |
| **Hash** | `md5` / `sha1` / `sha256` when calculated. Empty is not “clean.” Do not invent a hash. |
| **Source / dest** | `tx_hosts` sent the bytes. `rx_hosts` received them. These are not `id.orig_h` / `id.resp_h`. |
| **Connection UID** | `conn_uids` — those values *are* the `uid` on `conn` / `http` / `smtp`. Copy one and search. |

This is the **extract**. Zeek does not have to write the bytes to disk. The host may or may not create a file. A Temp path on the host is a different sensor (**1.1.3**).

**What good looks like:**

- Describe: one sentence — name if logged, MIME, hash if logged, who sent to whom. Then say which `uid` you would open on `conn` or `http`. Do not describe a Sysmon 11.
- Given: `filename` `update.exe`, `mime_type` `application/x-dosexec`, `sha256` present, `tx_hosts` `203.0.113.88`, `rx_hosts` a workstation, `conn_uids` present. **What occurred:** that IP sent `update.exe` (executable MIME, hash logged) to that host on the wire. Copy `conn_uids` and search the other Zeek logs. The Temp file-create is **1.1.3**.
- Query: names a **specific** pattern (name, MIME, hash, or tx/rx), not every `files` event.

---

## 2. Knowledge Check

1. A Zeek `files` event is the same thing as a Sysmon 11 file create. True or false?
2. `update.exe`, MIME `application/x-dosexec`, hash logged, from `203.0.113.88` to a workstation. In one sentence, what occurred?
3. A SIEM query that matches every `files` event is a good “specific file transfer” query. True or false?

---

## 3. Summary

A `files` event is a transfer on the wire: name, MIME, hash, who sent and received. `conn_uids` joins `conn` / `http` / `smtp`. The host file event is a different sensor.

**Next:** **1.2.8** Weird engine.

---

## 4. Related modules

- 1.2.6 – SMTP engine (previous)
- 1.2.5 – HTTP engine
- 1.2.8 – Weird engine
- 1.1.3 – File system activity (host)
