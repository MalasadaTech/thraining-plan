# Module 2.6.1 – Advanced DNS Concepts
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.6.1 – Advanced DNS  
**Subtitle:** Who runs the zone  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
2.5.1 pulled registration and named the NS pair. This lesson reads the records the zone publishes. It is not a Zeek `dns` log.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

An alert or an RFI often names a **domain**.

Before you enrich it, read the **zone**: who runs it, and who else is tied to it.

This is **authoritative DNS** — published records, not a lookup on the wire.

**Speaker Notes:**  
This slide is the student intro. CTI reads the zone so they can say who operates a name and whether another name shares that control. Wire lookups and DGA wait for 1.2.3. Do not teach Zeek fields today.

---

### Slide 3 – SOA records
**Title:** SOA records

**SOA** is the zone’s control record.

**MNAME** — primary nameserver.  
**RNAME** — responsible mailbox, written as a name. `hostmaster.cdn-test.net` means `hostmaster` at `cdn-test.net`.  
**Serial** — zone-change counter. Not a file hash.

Who runs the zone. Not a country.

**Speaker Notes:**  
Three fields. Stop. Do not collapse MNAME onto the RNAME string. If they call the serial a hash, correct it here before the pivot slide.

---

### Slide 4 – Other records of intel value
**Title:** Other records of intel value

**NS** — who answers the zone. Same pair can mean shared control.  
**MX** — who receives mail.  
**TXT** — text the operator published. A unique token can be a pivot.  
**SRV** — where a named service lives.

Who else is tied to this zone. Not a full mail class.

**Speaker Notes:**  
The NS pair `ns1.cdn-test.net` / `ns2.cdn-test.net` already came from RDAP. Here it is a DNS fact you use, not a registration re-query. Do not open SPF or MX preference as a class.

---

### Slide 5 – Interpret and pivot
**Title:** Interpret and pivot

SOA RNAME `hostmaster.cdn-test.net` — who runs the zone.  
Sibling `login-prd.net` — same NS pair, same A `203.0.113.88`.

Do **not** claim `203.0.113.0/24`. Shared cloud is not “theirs.”

**Speaker Notes:**  
Walk both products before the knowledge check. Interpret is the SOA line. Pivot is the sibling. The `/24` reject is the judgment this lesson owns. Do not write the four-slot hop sentence; that product is 2.8.1.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. The SOA serial is a file hash. True or false?  
2. What two SOA fields do you read first, and what does each one mean?  
3. Same NS + same A on `login-prd.net` — what can you say, and what must you **not** say about `203.0.113.0/24`?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

SOA = who runs the zone. Serial is not a hash.  
Same NS / same A can be a sibling.  
A shared `/24` is not theirs.

**Next:** **2.7.1** ATT&CK for CTI

**Speaker Notes:**  
ATT&CK for CTI is next. That lesson maps behavior. Stay off DNS records when you get there.
