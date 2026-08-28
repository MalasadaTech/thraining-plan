# Module 1.2.4 – TLS Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.4 – TLS Engine  
**Subtitle:** The handshake Zeek saw  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.2.3 was the DNS extract. This lesson is TLS. It is the handshake, not decrypted HTTP, and not the initiating process.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read **TLS** events to see the **handshake** when the payload is encrypted.

Who talked to whom. SNI. Certificate. Version and cipher.

Not decrypted HTTP. Not the initiating process.

**Speaker Notes:**  
This slide is the student intro. Encrypted traffic still needs a description. Do not teach HTTP fields today. Do not name a process from this log.

---

### Slide 3 – SNI and the certificate
**Title:** SNI, subject, issuer

**`server_name`** — hostname in the Client Hello. Empty means not sent or not logged.

**`subject` / `issuer`** — name on the certificate, and who signed it.

SNI is not the certificate subject.

**Speaker Notes:**  
Walk SNI first, then the certificate names. If they treat `server_name` as the cert, stop: Client Hello versus what the certificate presents.

---

### Slide 4 – JA3, version, cipher, who
**Title:** Fingerprint, version, cipher, addresses

**JA3 / JA3S** — where the shop logs them. Not a malware name. Missing means not logged, not “no TLS.”

**`version` / `cipher`** — what was negotiated.

**`id.orig_*` → `id.resp_*`** — originator to responder.

**Speaker Notes:**  
JA3 is how the client spoke TLS. Do not invent a value. Originator started the talk from Zeek’s view.

---

### Slide 5 – How it shows up
**Title:** The ssl log

Zeek writes TLS to the **`ssl`** log. The name is historical.

One event per handshake Zeek saw.

This is the **extract**. PCAP still verifies or expands (**1.2.1**).

The initiating process is not on this log. That is host-observed network (**1.1.4**).

**Speaker Notes:**  
Keep them on this engine. HTTP fields wait for 1.2.5. If they ask about SIEM tables, a TLS log line is an event; in a SIEM it often shows up as a row.

---

### Slide 6 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: who talked to whom, SNI if present, version/cipher.

**Given:** `203.0.113.88:443`, `server_name` empty, version and cipher present.

A query names a **specific** pattern — SNI, subject, version, or dest.  
Not every `ssl` event.

**Speaker Notes:**  
Show this given before the knowledge check. Handshake to that IP on 443. SNI not logged. Do not tell the intro plot. Do not name a process.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. `server_name` is the name on the server certificate. True or false?  
2. Workstation → `203.0.113.88:443`, `server_name` empty, version and cipher present. In one sentence, what occurred?  
3. A SIEM query that matches every `ssl` event is a good “specific TLS activity” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Handshake: SNI, certificate, version, cipher, who talked to whom.  
JA3 only if logged.  
The process is not on this log.  
A query is specific.

**Next:** **1.2.5** HTTP engine

**Speaker Notes:**  
1.2.5 is cleartext HTTP fields on the same wire. Stay off this handshake when you get there.
