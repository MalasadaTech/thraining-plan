# Module 1.2.4 – TLS Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.4 – TLS Engine  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Handshake metadata. ssl log. Not decrypted HTTP. Not the process.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read the Zeek **`ssl`** log: the **handshake**, not the bytes inside.

It does **not** name the initiating process.  
That was **1.1.4**.

**Speaker Notes:**  
1.2.3 was the A record. This is TLS on :443.

---

### Slide 3 – SNI and the cert
**Title:** SNI, subject, issuer

**`server_name`** — hostname in the Client Hello. Empty = not logged.  
**`subject` / `issuer`** — name on the cert, and who signed it.

**Speaker Notes:**  
Outline a–b. SNI is not the cert subject.

---

### Slide 4 – JA3, version, cipher, who
**Title:** Fingerprint, version, cipher, addresses

**JA3 / JA3S** — where available. Not a malware name.  
**`version` / `cipher`** — what was negotiated.

**`id.orig_*` → `id.resp_*`** — who talked to whom.

**Speaker Notes:**  
Outline c–f. Missing JA3 = not logged.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No process name.  
No phishing catalog.  
The `conn` and `dns` rows are different extracts.

**Speaker Notes:**  
HTTP fields wait.

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: who talked to whom, SNI if present, version/cipher.

**Given:** `203.0.113.88:443`, `server_name` empty, version and cipher present.

A query names a **specific** pattern — SNI, subject, version, or dest.  
Not “all `ssl` rows.”

**Speaker Notes:**  
TLS handshake to that IP on 443. SNI not logged. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. `server_name` is the name on the server certificate. True or false?  
2. Workstation → `203.0.113.88:443`, `server_name` empty, version and cipher present. In one sentence, what occurred?  
3. A SIEM query that matches every `ssl` row is a good “specific TLS activity” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Handshake: SNI, cert, version, cipher, who talked to whom.  
JA3 only if logged.  
The process is not on this row.  
A query is specific.

**Next:** **1.2.5** HTTP engine

**Speaker Notes:**  
Cleartext HTTP fields next.
