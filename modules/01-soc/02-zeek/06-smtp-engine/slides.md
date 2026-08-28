# Module 1.2.6 – SMTP Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.6 – SMTP Engine  
**Subtitle:** Envelope and a few headers on the wire  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.2.5 was HTTP on the same wire. This lesson is the SMTP engine. It is not a mailbox, not the attachment hash, and not the process that sent the mail.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read the Zeek **`smtp`** log to see who the session claimed mail was from and to.

Envelope and a few headers on the wire.  
Not a mailbox. Not the attachment hash. Not the process that sent it.

**Speaker Notes:**  
This is daily alert work: describe the mail transaction Zeek parsed. File hashes wait for 1.2.7. The process was 1.1.4.

---

### Slide 3 – Mail from, rcpt to
**Title:** Mail from, rcpt to

**`mailfrom`** — envelope MAIL FROM. Who the session claimed as sender. Not the From header.

**`rcptto`** — envelope RCPT TO. Can be more than one address.

**Speaker Notes:**  
Walk the envelope first. `mailfrom` is the MAIL FROM command, not the From header and not a file hash.

---

### Slide 4 – Subject, message ID, who
**Title:** Subject, message ID, who talked to whom

**`subject`** — the Subject header. Empty = not logged. Easy to spoof.

**`msg_id`** — Message-ID when logged. Not a file hash.

**`id.orig_*` → `id.resp_*`** — who talked to whom (often 25 / 587).

**Speaker Notes:**  
Empty subject or message ID means Zeek did not log it, not that there was no mail. Do not invent a site mail-gateway name.

---

### Slide 5 – Wire extract, not a mailbox
**Title:** Wire extract, not a mailbox

No process name. That was **1.1.4**.  
No attachment hash. That is **1.2.7**.  
No phishing playbook.

Encrypted submission may have no SMTP fields. That handshake was **1.2.4**.

**Speaker Notes:**  
Keep them on this log. If they name Outlook, that is host-network. If they open a hash, that is the files engine.

---

### Slide 6 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: envelope from, envelope to, subject if logged.

**Given:** outside `mailfrom`, `rcptto` a user, subject present.

A query names a **specific** pattern — `mailfrom`, `rcptto`, subject, or dest.  
Not “all `smtp` events.”

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: that client sent envelope mail from A to B with that subject. Do not name a process. Do not call it phishing.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. `mailfrom` is the attachment hash. True or false?  
2. Envelope from an outside address, `rcptto` a user, subject present. In one sentence, what occurred?  
3. A SIEM query that matches every `smtp` event is a good “specific SMTP activity” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Envelope from/to, subject, message ID, who talked to whom.  
The process and the hash are not on this event.  
A query is specific.

**Next:** **1.2.7** Files engine

**Speaker Notes:**  
1.2.7 is name, MIME, and hash of what crossed the wire. Stay off this smtp event when you get there.
