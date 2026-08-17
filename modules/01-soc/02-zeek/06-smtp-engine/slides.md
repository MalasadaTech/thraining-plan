# Module 1.2.6 – SMTP Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.6 – SMTP Engine  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Envelope and a few headers. Not a mailbox. Not the attachment hash.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read the Zeek **`smtp`** log: who the session claimed mail was from and to.

It does **not** name the initiating process.  
That was **1.1.4**.

**Speaker Notes:**  
1.2.5 was HTTP. This is mail on the wire.

---

### Slide 3 – Envelope
**Title:** Mail from, rcpt to

**`mailfrom`** — envelope MAIL FROM.  
**`rcptto`** — envelope RCPT TO (can be a list).

**Speaker Notes:**  
Outline a–b. Envelope, not a From header course.

---

### Slide 4 – Subject, message ID, who
**Title:** Subject, message ID, addresses

**`subject`** — easy to spoof. Empty = not logged.  
**`msg_id`** — Message-ID when logged. Not a file hash.

**`id.orig_*` → `id.resp_*`** — who talked to whom (often 25 / 587).

**Speaker Notes:**  
Outline c–e. Do not invent an MX name.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No process name.  
No attachment hash (**1.2.7**).  
No phishing playbook.

**Speaker Notes:**  
Encrypted submission may have no SMTP fields (1.2.4).

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: envelope from, envelope to, subject if logged.

**Given:** outside `mailfrom`, `rcptto` a user, subject present.

A query names a **specific** pattern — `mailfrom`, `rcptto`, subject, or dest.  
Not “all `smtp` rows.”

**Speaker Notes:**  
That client sent envelope mail from A to B with that subject. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. `mailfrom` is the attachment hash. True or false?  
2. Envelope from an outside address, `rcptto` a user, subject present. In one sentence, what occurred?  
3. A SIEM query that matches every `smtp` row is a good “specific SMTP activity” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Envelope from/to, subject, message ID, who talked to whom.  
The process and the hash are not on this row.  
A query is specific.

**Next:** **1.2.7** Files engine

**Speaker Notes:**  
Name, MIME, hash next.
