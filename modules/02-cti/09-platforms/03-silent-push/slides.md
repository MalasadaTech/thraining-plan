# Module 2.9.3 – Silent Push  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.9.3 – Silent Push  
**Subtitle:** Passive DNS and infrastructure context  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
2.9.2 was the AnyRun sandbox card. This lesson is Silent Push on a classroom card. It is not when to pick the tool, and it is not a live account.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts already have a **seed** — a domain or IP from the case.

They open Silent Push for **passive DNS** history and related infrastructure.

Enrich the seed. Pivot only to names the **classroom card** shows.

**Speaker Notes:**  
This slide is the student intro. They already chose Silent Push in 0.7. Today they read the card so they do not treat shared hosting as theirs. Do not start a four-tool survey.

---

### Slide 3 – Core capabilities
**Title:** What Silent Push is for

**Historical names on an A** — which hostnames pointed at this IPv4 address.  
**A history for a name** — which IPv4 addresses this hostname resolved to.  
**Shared nameservers** — other names with the same NS pair, if the card shows them.

Not a sandbox. Not a page screenshot.

**Speaker Notes:**  
These are the capabilities. When to pick Silent Push versus URLScan stays in 0.7. If they ask about SOA or RDAP, that is 2.6 or 2.5.

---

### Slide 4 – Enrich and pivot
**Title:** Enrich the seed. Pivot only what the card shows.

**Enrich** — what names have pointed at `203.0.113.88`? What A records has the update domain had?

**Pivot** — other names with the same NS pair, if the card shows them.

If it is not on the card, write **not on the card**. Do not invent a hit.

**Speaker Notes:**  
Enrich is the seed you already have. Pivot is extra infrastructure. The next slide is the take and the reject on this given.

---

### Slide 5 – Take versus reject
**Title:** Take versus reject

**Take** — `203.0.113.88` → the update domain / `login-prd.net` **on the card**.

**Reject** — the whole `203.0.113.0/24`. Neighboring IPs are shared hosting.

**Speaker Notes:**  
Show this given before the knowledge check. Names on that A are a take only if the card lists them. Do not tell the intro plot.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. This lesson is “when to pick Silent Push.” True or false?  
2. What two jobs do you do in Silent Push?  
3. Enrich `203.0.113.88`. One legal pivot, and one thing you must reject.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Passive DNS and infrastructure context.  
Enrich the seed. Pivot only what the card shows.  
A shared `/24` is not theirs.

**Next:** **2.9.4** URLScan

**Speaker Notes:**  
URLScan is the page-scan card. Stay off that product unless that lesson is scheduled.
