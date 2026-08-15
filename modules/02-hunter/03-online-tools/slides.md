# Module 2.3.1 – Tool Capabilities for Hunting  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.3.1 – Tool Capabilities for Hunting  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Ask what a VirusTotal score proves about *this* network. This lesson is enrich → lead → internal query. Not a live malware lab. Not 2.4 report extract.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. State strengths and limits of VT, AnyRun, URLScan, Silent Push
2. Query and pivot on named objects
3. Extract an actionable hunting lead
4. Convert the lead into a precise SIEM / Zeek query

**Mapped Items:**  
K: 2.3.1 | T: 2.3.1.1–2.3.1.3

**Speaker Notes:**  
Hunter 3 is already at principles (B / 3c). Push a teammate-ready chain.

---

### Slide 3 – Agenda
**Title:** Agenda

- Four tools: strengths and limits
- Pivot, lead, internal query
- Three worked examples
- Identification practice
- Hands-on enrichment card
- Knowledge check

**Speaker Notes:**  
2.2 was card + type. 2.4 is CTI extract. Stay here.

---

### Slide 4 – Not Enrichment
**Title:** Scores Are Not Hits

“VirusTotal 12/72 — hunt it.”  
“AnyRun said malicious — we are breached.”  
“Silent Push ASN — hunt all 443.”

**Key Point:** External tools answer what is *known*. Internal queries answer what *we* saw.

**Speaker Notes:**  
Leave the slogans up. Kill them in Examples 2 and 3. No private uploads.

---

### Slide 5 – Four Tools
**Title:** What Each Tool Is For

| Tool | Hunt job | Hard limit |
|------|----------|------------|
| **VirusTotal** | Relations / file-URL-domain-IP views | Score ≠ presence; upload can leak |
| **AnyRun** | Process tree + hosts from *that* run | One VM; banner ≠ estate |
| **URLScan** | Redirects, requested hosts, similar scans | Scanner path ≠ victim |
| **Silent Push** | Passive DNS / infra cluster / first-seen | Coverage ≠ your DNS; CDNs lie |

**Analyst Tip:** Comments and sandbox tags are not a **2.4** CTI product.

**Speaker Notes:**  
One student names a strength; another names the limit.

---

### Slide 6 – Pivot
**Title:** Follow Named Objects

Hash → contacted hosts / dropped files  
AnyRun task → hosts / files / command line from *your* hash  
URLScan → redirect and requested hostnames  
Silent Push → first-seen and listed lookalikes

**Key Point:** If you only have a number or a color, you have not pivoted.

**Speaker Notes:**  
Wrong-object AnyRun tasks get discarded.

---

### Slide 7 – Lead
**Title:** Actionable Hunting Lead

**Lead:** named object or rare behavior you can search internally  
**Not a lead:** detection count, red banner, “any 443,” whole ASN

**Analyst Tip:** Same bar as unique patterns in **2.2.2**. Do not rewrite the whole card here.

**Speaker Notes:**  
Ask: would this query return half the company?

---

### Slide 8 – Convert
**Title:** Precise Internal Query

Name all five:

1. Data (DNS, TLS, EDR, …)
2. Field (`query`, `server_name`, hash, …)
3. Object
4. Window
5. Population / exclusions

**Key Point:** “Hunt the domain” is not converted. No DNS on lab → lab is out of scope, not clean.

**Speaker Notes:**  
Write one converted line on the board from Example 1.

---

### Slide 9 – Example 1: Complete Chain
**Title:** Example 1 – Hash to DNS/TLS

- VT Relations → bulletin lookalike CDN name
- URLScan / Silent Push agree the **name** is the object
- Query: `dns.query` or TLS `server_name`; finance; 7 days; **not lab**
- VT score is not a hit

**Interpretation:**  
Converted. Y can fail internally. Lab is a visibility gap.

**Speaker Notes:**  
Students score the card before you reveal the interpretation.

---

### Slide 10 – Example 2: Banner vs Extract
**Title:** Example 2 – AnyRun

**A:** Malicious. Hunt all 443. Incident.  
**B:** Same hash’s network tab → host + `wscript` / rare script. Query those. Do not re-upload.

**Interpretation:**  
A is not enrichment. B is the extract.

**Speaker Notes:**  
If the public task is not their hash, throw the C2 list away.

---

### Slide 11 – Example 3: Shared Infra
**Title:** Example 3 – ASN vs Name

**A:** Shares ASN with a major CDN. Hunt 443 to that ASN.  
**B:** First-seen lookalike names. Query those hostnames in DNS. Not the ASN.

**Interpretation:**  
A is daily traffic. B is a searchable object list.

**Speaker Notes:**  
Force: ASN-only Silent Push → park or pivot, do not query the ASN.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Score or banner as the lead
- Uploading a private sample
- Internal query = any 443 / whole ASN
- Pivoting a different AnyRun task
- Re-teaching the 2.2.2 card or a 2.4 TTP dump

**Speaker Notes:**  
Ask for a local rejected enrichment paste. Then the exercise.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide (reason each).
3. Write one enrichment card: start, pivot, lead, internal query.

**Speaker Notes:**  
No private upload. Park execute blocks and CTI extracts. Review with the Instructor Guide key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. One VT strength and one limit?
2. Why is AnyRun “malicious” not an internal hit?
3. What makes an external finding a hunt lead?
4. Convert a hostname — which bounds?
5. Huge CDN ASN on Silent Push — what do you not query?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Four tools, four jobs, four hard limits.
- Pivot named objects, not scores.
- Leads are internally searchable and not daily traffic.
- Convert = data + field + object + window + population.
- Card / execute → **2.2**. CTI extract → **2.4**.

**Speaker Notes:**  
Do not open 2.4 report labs.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 2.4 – CTI for hunters

**Resources:**
- Student Guide for this module
- Module 2.2.2 – Hunt development
- Local sample-upload / acceptable-use rules

**Speaker Notes:**  
Park STIX, ATT&CK, persistence.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** Enrichment Quick Reference

**VT:** Relations, not the ratio  
**AnyRun:** artifacts from *this* run, not the banner  
**URLScan:** requested hosts, not the scanner IP  
**Silent Push:** listed names / first-seen, not the CDN ASN  

**Test:**  
- score / banner only → not ready  
- any 443 / whole ASN → not ready  
- no field / window / population → not converted  

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the four-field enrichment card large enough to read
- Visually reject 12/72, red banner, any-443, ASN
- Consistent footer with module number
- Minimal text — let the three examples teach
