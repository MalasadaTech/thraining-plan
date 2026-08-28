# Module 2.5.1 – RDAP and WHOIS Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.5.1 – RDAP and WHOIS  
**Subtitle:** Registration lookup for a domain or IP  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is registration lookup. It does not teach SOA, PDNS, or how to name an actor.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts look up **registration** on a domain or an IP.

Before you enrich an indicator or call it empty, read that lookup.

This lesson is that lookup.

**Speaker Notes:**  
This slide is the student intro. Registration is who holds the name or the block, not who answers the zone. File hashes were last lesson. SOA waits for the next one.

---

### Slide 3 – Same job: registration
**Title:** WHOIS and RDAP

Both look up **registration** for a domain or an IP.

Who registered the name. Who holds the block.

Not DNS SOA. Not PDNS.

**Speaker Notes:**  
Purpose first. They are two protocols for one job. If someone starts reading an SOA, that is 2.6.

---

### Slide 4 – How they differ
**Title:** RDAP first, WHOIS fallback

**RDAP** — JSON over **HTTPS**. Easier to parse.

**WHOIS** — free text on **port 43**. Layout changes by server.

Query RDAP first. Use WHOIS when RDAP has no record.

**Speaker Notes:**  
Same job, different protocol. Do not say RDAP is “WHOIS in JSON.” One difference is enough for the knowledge check later.

---

### Slide 5 – Fields you extract
**Title:** Registrar, NS, dates, block holder

**Domain** — registrar, nameservers, created / updated, registrant *if present*.

**IP** — CIDR and org. Who holds the block, not the actor.

**Redacted registrant** is a fact. Not “no intel.” Not a country.

**Speaker Notes:**  
Walk the field table. Distinctive NS is enrichment, not nation-state. Cloud org is the hosting holder, not the campaign.

---

### Slide 6 – Query it. Write what is there.
**Title:** Query the name or the IP

Update domain: extract `ns1.cdn-test.net` / `ns2.cdn-test.net`, registrar, created date.

Write **registrant redacted** if that is the lookup. Distinctive NS is not nation-state.

`203.0.113.88`: extract `203.0.113.0/24`, org **Example Cloud**. Not “theirs.”

**Speaker Notes:**  
Show both givens before the knowledge check. Sibling `login-prd.net` can be named from the same NS. Do not read SOA. Do not open Silent Push. Do not tell the intro plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A redacted registrant means you have no intelligence. True or false?  
2. Name one difference between WHOIS and RDAP.  
3. You query the update domain and see `ns1.cdn-test.net`. What did you extract, and what must you **not** claim?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

WHOIS and RDAP look up registration. Query RDAP first.  
Redacted is a fact. NS is enrichment, not attribution.  
An IP org is who holds the block, not the actor.

**Next:** **2.6.1** Advanced DNS

**Speaker Notes:**  
2.6.1 is SOA on the same name. Stay off this registration lookup when you get there.
