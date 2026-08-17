# Module 2.6.1 – Advanced DNS Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.6.1 – Advanced DNS  
**Subtitle:** CTI Analyst (Hunter / SOC sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Who runs the zone. Not Zeek dns.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Read **authoritative DNS**.

SOA, NS, related names.  
Shared cloud is not “theirs.”

**Speaker Notes:**  
NS pair came from 2.5.1.

---

### Slide 3 – SOA and friends
**Title:** SOA, NS, other

**SOA** — MNAME, RNAME, serial.  
**NS** — who answers the zone.  
**Other** — MX / TXT only if the card has them.

**Speaker Notes:**  
Outline a–c.

---

### Slide 4 – What good looks like
**Title:** Interpret and pivot

SOA RNAME `hostmaster.cdn-test.net` — who runs the zone.  
Sibling `login-prd.net` — same NS, same A `203.0.113.88`.

Do **not** claim `203.0.113.0/24`.

**Speaker Notes:**  
Story bible sibling lands here.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No Zeek `dns` / DGA (**1.2.3**).  
No RDAP redo (**2.5**).  
No Silent Push PDNS (**0.7**).

**Speaker Notes:**  
ATT&CK for CTI is next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. This hour is Zeek `dns` field reading. True or false?  
2. What two SOA fields do you read first (MNAME / RNAME)?  
3. Same NS + same A on `login-prd.net` — what can you say, and what must you **not** say about `203.0.113.0/24`?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

SOA = who runs the zone. Same NS / same A can be a sibling.

**Next:** **2.7.1** ATT&CK for CTI

**Speaker Notes:**  
Do not open ATT&CK unless that hour is scheduled.
