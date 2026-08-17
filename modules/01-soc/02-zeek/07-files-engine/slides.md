# Module 1.2.7 – Files Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.2.7 – Files Engine  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Wire file, not host 1.1.3. Join is conn_uids.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Explain filename, MIME, hashes, tx/rx hosts, and connection UID linking
2. Analyze a Zeek `files` log entry and describe what occurred
3. Write a SIEM query for *specific* file-transfer activity
4. Pivot with `conn_uids` (and say what `fuid` is)

**Mapped Items:**  
K: 1.2.7.1 | T: 1.2.7.2 | T: 1.2.7.3

**Speaker Notes:**  
CTI is A / A / B and 1a / 1a / 2b.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose of the files log
- Fields (outline a–e)
- conn_uids vs fuid
- Three worked examples
- Two queries
- Knowledge check

**Speaker Notes:**  
YARA is 1.3.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Sysmon 11 / `DeviceFileEvents` (**1.1.3**)  
HTTP URI without the files row (**1.2.5**)  
YARA (**1.3**)  
How to enable extract-to-disk  

**Key Point:** Describe *this* `files` row.

**Speaker Notes:**  
Park extract admin.

---

### Slide 5 – Purpose of the files Log
**Title:** Purpose of the files Log

- File Zeek saw **on the wire**
- HTTP download, SMTP attachment, similar
- Complements `http` / `smtp` (how) and `conn` (session)

**Key Point:** Sensor file ≠ host file create.

**Speaker Notes:**  
Ask: “Wire or host?”

---

### Slide 6 – Name, MIME, Hash
**Title:** Filename, MIME, Hashes

**filename** — when the protocol gave a name  
**mime_type** — what Zeek thinks the bytes are  
**md5 / sha1 / sha256** — when calculated

Empty hash → “not logged,” not clean.  
Name vs MIME mismatch = lead.

**Speaker Notes:**  
Same hash-is-bytes rule as 1.1.3, different sensor.

---

### Slide 7 – Who Sent / Who Got
**Title:** tx_hosts and rx_hosts

**tx_hosts** — sender  
**rx_hosts** — receiver  
**source** — `HTTP`, `SMTP`, …

**Speaker Notes:**  
Outline d.

---

### Slide 8 – The Join
**Title:** conn_uids vs fuid

`files` often has **no** `uid` column.  
**`conn_uids`** = connection `uid`s → search `conn` / `http` / `smtp`  
**`fuid`** = this *file*

**Analyst Tip:** Searching `files` for `uid` and finding nothing is the usual trap.

**Speaker Notes:**  
Write the equality on the board.

---

### Slide 9 – Example 1: Expected PDF
**Title:** Example 1 – HTTP PDF

- `q3-notes.pdf` / `application/pdf`
- tx `10.10.8.20` → rx `10.10.50.23`
- `conn_uids` = HTTP Example 1 `uid`

**Interpretation:**  
Expected.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: HTTP EXE
**Title:** Example 2 – update.exe

- `application/x-dosexec`
- hashes not in catalog
- Same `conn_uids` as HTTP GET `/payload/update.exe`

**Interpretation:**  
Lead. Pivot to `http` + `conn`.

**Speaker Notes:**  
Name + MIME + hash together.

---

### Slide 11 – Example 3: SMTP Mismatch
**Title:** Example 3 – invoice.jpg is Executable

- `filename` `invoice.jpg`
- `mime_type` `application/x-dosexec`
- `source` SMTP; `conn_uids` = SMTP Example 2

**Interpretation:**  
Lead. Name vs MIME.

**Speaker Notes:**  
Not a host file create.

---

### Slide 12 – Pivoting
**Title:** Pivoting from files

1. Interesting `files` row  
2. Copy a **`conn_uids`** value  
3. Search `conn` / `http` / `smtp` where `uid` equals it  
4. Use `fuid` if you need the same file again  

**Speaker Notes:**  
Demonstrate once.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- `files.uid` (column often missing)  
- Sysmon 11 as “the same row”  
- Empty hash = clean  
- Query with no filter  
- YARA in this hour  

**Speaker Notes:**  
Then the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize each example.
2. Two queries: HTTP executable name/MIME; name vs MIME (or watchlisted hash).
3. Explain `conn_uids` vs `fuid`.
4. Identify the four items.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. `files` vs 1.1.3?
2. Filename, MIME, hash fields?
3. tx_hosts / rx_hosts?
4. How do you join to `conn`? What is `fuid`?
5. `.jpg` name + executable MIME — what do you write?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- `files` = wire transfer: name, MIME, hashes, tx/rx, source.
- Pivot with **`conn_uids`**. `fuid` is the file.
- Empty fields → “not logged.”
- Next: Weird engine (**1.2.8**).

**Speaker Notes:**  
Last protocol-ish engine is weird.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Files — Quick Reference

| Need | Look at |
|------|---------|
| Name / type / bytes | `filename` `mime_type` `sha256` |
| Direction | `tx_hosts` `rx_hosts` `source` |
| Session join | `conn_uids` → `uid` |
| File join | `fuid` |

**Coming next:** Module 1.2.8 – Weird Engine

**Footer:** SOC / Hunter / CTI Training Program
