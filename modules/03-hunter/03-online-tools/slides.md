# Module 3.3.1 – Tool Capabilities for Hunting  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 3.3.1 – Tool Capabilities for Hunting  
**Subtitle:** From an external finding to an internal search  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
This lesson is how an external finding becomes an internal search. It is not when to pick a tool, and it is not a platform-tab class. Students work from a classroom result card. They do not log in.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Hunters take an external finding and turn it into a search they can run **here**.

A detection count, a “malicious” tag, or a screenshot does not tell you whether that activity happened on your network.

This lesson is hunt strength, hunt limit, then convert.  
No live account.

**Speaker Notes:**  
This slide is the student intro. The last lesson bounded the hunt. This one is how an external finding becomes an internal query. Do not open the when-to-pick table.

---

### Slide 3 – Hunt strength vs hunt limit
**Title:** Hunt strength vs hunt limit

**VirusTotal** — a linked host or dropped file, not a detection count.  
**AnyRun** — process or network from a detonation, not a “malicious” tag.  
**URLScan** — requested hosts on a URL, not a screenshot.  
**Silent Push** — other names on the same A or NS, not a whole `/24`.

**Speaker Notes:**  
One line each. Stop. A is an IPv4 mapping. NS is a nameserver. A `/24` is a 256-address block. Do not teach how to read the VirusTotal tabs.

---

### Slide 4 – Query, pivot, lead
**Title:** Query, pivot, lead

Work from the **classroom result card**. Write what it shows.

**Query** the seed the card already has. **Pivot** to a related object on the same card.

A **hunt lead** is a named artifact you can search here: IP, port, URI, file, hostname.

A count, a tag, or a screenshot is not a lead.

**Speaker Notes:**  
This is what good querying and pivoting look like without a live account. If they invent a sibling domain, the card did not show it. If they start a tab walkthrough, that is the platform lesson, not this one.

---

### Slide 5 – Convert to a precise query
**Title:** Convert to a precise query

**Lead:** `GET /update.exe` to `203.0.113.88:8080`.

**Query:** that IP + that port + that URI.

Not every destination. Not the `/24`.

**Speaker Notes:**  
Show this given before the knowledge check. The Zeek form is `id.resp_h`, `id.resp_p`, and `uri`. A SIEM equivalent that names the same three facts is fine. `dest=*` and `203.0.113.0/24` fail.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A VirusTotal detection count is a hunt query. True or false?  
2. Name one hunt limit for Silent Push.  
3. The classroom result card shows `GET /update.exe` to `203.0.113.88:8080`. Write one precise Zeek or SIEM query. Do not use a `/24`.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Each tool has a hunt strength and a hunt limit.  
A lead is a named artifact you can search here.  
The query names that lead — not a count, not a tag, not a screenshot, and not a whole `/24`.

**Speaker Notes:**  
CTI triage is next. Do not open hunt-worthy versus awareness-only unless that lesson is scheduled.

---

### Slide 8 – Next
**Title:** Next

**3.4.1** Assessing CTI for hunting value

**Speaker Notes:**  
3.4.1 is whether a report is hunt-worthy at all. Stay off that gate in this lesson.
