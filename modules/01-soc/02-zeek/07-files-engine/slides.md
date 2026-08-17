# Module 1.2.7 – Files Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.7 – Files Engine  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
File on the wire. Not Sysmon 11. Not YARA.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read the Zeek **`files`** log: a file **on the wire**.

It is **not** a host file-create (**1.1.3**).

**Speaker Notes:**  
1.2.5 was GET /update.exe. This is those bytes.

---

### Slide 3 – Name, MIME, hash
**Title:** Name, MIME, hash

**`filename`** — when the protocol gave one. Can lie.  
**`mime_type`** — what Zeek thinks the bytes are.  
**`md5` / `sha1` / `sha256`** — when calculated. Empty ≠ clean.

**Speaker Notes:**  
Outline a–c. Name vs MIME can disagree.

---

### Slide 4 – Who, and the UID
**Title:** Sender, receiver, connection UID

**`tx_hosts` / `rx_hosts`** — who sent, who received.

**`conn_uids`** — those values *are* the `uid` on `conn` / `http` / `smtp`. Copy one and search.

**Speaker Notes:**  
Outline d–e. First hour that owes the join.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No Temp path. That is **1.1.3**.  
No YARA (**1.3**).  
Do not invent a hash.

**Speaker Notes:**  
Weird next.

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: name, MIME, hash if logged, who sent to whom.

**Given:** `update.exe`, executable MIME, hash logged, from `203.0.113.88`.

A query names a **specific** pattern — name, MIME, hash, or tx/rx.  
Not “all `files` rows.”

**Speaker Notes:**  
That IP sent update.exe on the same connection as the HTTP GET. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A Zeek `files` row is the same thing as a Sysmon 11 file create. True or false?  
2. `update.exe`, executable MIME, hash logged, from `203.0.113.88` to a workstation. In one sentence, what occurred?  
3. A SIEM query that matches every `files` row is a good “specific file transfer” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Name, MIME, hash, who sent and received.  
`conn_uids` joins the other Zeek logs.  
The host file row is a different sensor.

**Next:** **1.2.8** Weird engine

**Speaker Notes:**  
Protocol oddities next. Not a hash.
