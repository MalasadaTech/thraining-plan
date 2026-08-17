# Module 3.5.1 – RDAP and WHOIS Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.5.1 – RDAP / WHOIS  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Query + interpret. Overlay a live RDAP lookup if you can.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Purpose of WHOIS and RDAP
2. Key differences; RDAP first
3. Query a domain or IP
4. Interpret fields — including redaction

**Mapped Items:**  
K: 3.5.1 | T: 3.5.1.1

**Speaker Notes:**  
Hunter 3-level task is 2b. CTI is 3c / 4c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose, differences, fields
- Three examples
- Query + interpret
- Knowledge check

**Speaker Notes:**  
3.6 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Historical A / siblings (**3.3.2** Silent Push)  
SOA / advanced DNS (**3.6**)  
Nation-state from a privacy flag (**3.1.7**)

**Key Point:** Registration data. Then what you may claim.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Purpose
**Title:** Why Look This Up

WHOIS — legacy registration text.  
RDAP — structured registration (HTTPS + JSON).  
Who *registered* the name or *holds* the IP block.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Differences
**Title:** RDAP First

Structured vs free text.  
HTTPS vs port 43.  
Privacy is labeled, not a surprise.

No RDAP for that TLD → WHOIS and say so.

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Fields
**Title:** What You Still Have When Redacted

Created / updated / expiry  
Registrar · nameservers · status · abuse  
IP: CIDR, org, country, allocation date

**Speaker Notes:**  
Outline c.

---

### Slide 8 – Two Lines
**Title:** Query · Interpret

`object | RDAP or WHOIS | why`  
`fields | enrich | attribution support | do not claim`

**Speaker Notes:**  
Task.

---

### Slide 9 – Example 1: Domain
**Title:** Example 1 – Young + NS

14 days old. `cdn-test.net` NS. Registrant redacted.  
Cluster support. Not a person. Not a country.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Skip
**Title:** Example 2 – Privacy ≠ Empty

Redacted is expected.  
You still queried. You still have fields.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: Cloud
**Title:** Example 3 – Org ≠ Actor

Example Cloud LLC / US / 2019.  
Hosting enrichment. Not Night Owl Inc.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Skip when redacted  
- Cloud org as the actor  
- WHOIS-only when RDAP exists  
- PDNS / SOA in this hour  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use the site RDAP/WHOIS tool if posted.  
Keep: RDAP first + interpret, don’t over-claim.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–C: query line.
3. A, B, D/E: interpret.
4. No Silent Push. No SOA.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Why do WHOIS and RDAP exist?
2. Two differences — which first?
3. Four fields when redacted?
4. Why not the cloud org as actor?
5. Where is historical DNS taught?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- RDAP first. Redacted ≠ empty.
- Enrich. Do not crown a country.
- Next: **3.6** advanced DNS.

**Speaker Notes:**  
Do not open 3.6 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** RDAP — Quick Reference

| Object | Keep | Do not claim |
|--------|------|----------------|
| Domain | created, registrar, NS | Person / country from privacy |
| IP | CIDR, org, country | Org = the adversary |

**Coming next:** Module 3.6.1 – Advanced DNS

**Footer:** SOC / Hunter / CTI Training Program
