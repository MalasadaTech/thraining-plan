# Module 1.2.7 – Files Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 1.2.7 – Files Engine  
**Subtitle:** A file on the wire  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.2.1 said engines extract protocol. This lesson is the files engine. It is not host file activity and not YARA.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read the Zeek **files** log to see a file on the **wire**.

Name. MIME. Hash. Who sent it, who received it.

This is not a host file-create (**1.1.3**).

**Speaker Notes:**  
This slide is the student intro. An alert may name a download, an attachment, or a hash. The job is to say what moved on the wire. Do not teach a Temp path today.

---

### Slide 3 – Name, MIME, hash
**Title:** Name, MIME, hash

**`filename`** — when the protocol gave one. It can lie. Empty means not logged.

**`mime_type`** — what Zeek thinks the bytes are. A Windows executable is often `application/x-dosexec`. It can disagree with the name.

**`md5` / `sha1` / `sha256`** — when calculated. Empty is not “clean.” Do not invent a hash.

**Speaker Notes:**  
Walk name, MIME, and hash first. The name can say `.exe` while MIME disagrees, or the other way around. Empty hash means Zeek did not calculate one.

---

### Slide 4 – Sender, receiver, connection UID
**Title:** Sender, receiver, connection UID

**`tx_hosts`** sent the bytes. **`rx_hosts`** received them. These are not orig/resp.

**`conn_uids`** — those values *are* the `uid` on `conn` / `http` / `smtp`. Copy one and search.

**Speaker Notes:**  
For an HTTP GET of a file, the server is often the sender. Copy `conn_uids` and search other Zeek logs. That is the join, not a lab.

---

### Slide 5 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: name, MIME, hash if logged, who sent to whom.

**Given:** `update.exe`, MIME `application/x-dosexec`, hash logged, from `203.0.113.88` to a workstation.

A query names a **specific** pattern — name, MIME, hash, or tx/rx.  
Not every `files` event.

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: that IP sent update.exe on the wire. Copy conn_uids. Do not describe a Sysmon 11. Do not tell the course-fiction plot.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A Zeek `files` event is the same thing as a Sysmon 11 file create. True or false?  
2. `update.exe`, MIME `application/x-dosexec`, hash logged, from `203.0.113.88` to a workstation. In one sentence, what occurred?  
3. A SIEM query that matches every `files` event is a good “specific file transfer” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Name, MIME, hash, who sent and received.  
`conn_uids` joins the other Zeek logs.  
The host file event is a different sensor.

**Next:** **1.2.8** Weird engine

**Speaker Notes:**  
1.2.8 is protocol oddities. Stay off the file hash when you get there.
