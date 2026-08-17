# Module 2.5.1 – RDAP and WHOIS Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.5.1 – RDAP and WHOIS  
**Subtitle:** CTI Analyst (Hunter / SOC sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Registration. Redacted is a fact. Not SOA.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Pull **registration**.

Registrar, nameservers, dates.  
Redacted registrant is not “no intel.”

**Speaker Notes:**  
Not a country. Not Silent Push.

---

### Slide 3 – WHOIS vs RDAP
**Title:** Same job, different shape

**WHOIS** — text.  
**RDAP** — structured JSON. Same fields, easier to parse.

Useful: registrar, NS, created / updated, registrant *if present*.

**Speaker Notes:**  
Outline a–c.

---

### Slide 4 – What good looks like
**Title:** Query the update domain

Extract `ns1.cdn-test.net` / `ns2.cdn-test.net`.  
Write **registrant redacted** if that is the card.

Distinctive NS is enrichment. Not nation-state.

**Speaker Notes:**  
Sibling name can be named. SOA is 2.6.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No SOA parse (**2.6**).  
No Silent Push PDNS (**0.7**).  
No nation-state from redaction (**2.1.7**).

**Speaker Notes:**  
No live-account lab.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A redacted registrant means you have no intelligence. True or false?  
2. Name one difference between WHOIS and RDAP.  
3. You query the update domain and see `ns1.cdn-test.net`. What did you extract, and what must you **not** claim?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Registration. Redacted is a fact. NS is enrichment, not attribution.

**Next:** **2.6.1** Advanced DNS

**Speaker Notes:**  
Do not open SOA unless that hour is scheduled.
