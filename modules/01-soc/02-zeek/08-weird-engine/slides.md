# Module 1.2.8 – Weird Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.8 – Weird Engine  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Last 1.2 hour. Lead, not verdict. Not notice.log.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read the Zeek **`weird`** log: protocol behavior that is off-spec or uncommon.

A row is a **lead**, not a verdict.

**Speaker Notes:**  
1.2.7 was the file. This is “the session looked off.”

---

### Slide 3 – Type and notice
**Title:** Name, notice flag

**`name`** — the weird type. The string you query.

**`notice`** — whether *this* type was also raised as a notice.  
Not a `notice.log` course.

**Speaker Notes:**  
Outline a. Do not memorize the catalog.

---

### Slide 4 – Who, and the UID
**Title:** Addresses and UID

**`id.orig_*` → `id.resp_*`** — who talked to whom.

**`uid`** — same join as `conn` / `http` / `files`.  
Empty → write “no uid.” Use IP/port/time.

**Speaker Notes:**  
Outline b–c.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No process name.  
No Zeek script authoring.  
No “all weird is bad.”

**Speaker Notes:**  
1.3 is rule syntax.

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: Zeek flagged this `name` between these IPs.

**Given:** `data_before_established`, dest `203.0.113.88:8080`, `uid` present.

A query names a **specific** `name` (or dest).  
Not “all `weird` rows.”

**Speaker Notes:**  
Data before handshake on the same dest as the HTTP GET. Look at conn. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A single `weird` row is an incident. True or false?  
2. `name` `data_before_established`, dest `203.0.113.88:8080`, `uid` present. In one sentence, what occurred?  
3. A SIEM query that matches every `weird` row is a good “specific weird activity” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Type, two endpoints, UID.  
A lead, not a verdict.  
A query names a specific type.

**Next:** **1.3.1** SIGMA rules

**Speaker Notes:**  
1.2 is done. Detection syntax next. 4.x is how detections run as a service.
