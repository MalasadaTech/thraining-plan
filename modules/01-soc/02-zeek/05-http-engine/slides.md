# Module 1.2.5 – HTTP Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.5 – HTTP Engine  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
HTTP metadata. Not the body. Not the process.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read the Zeek **`http`** log: method, host, URI, User-Agent, status.

It does **not** name the initiating process.  
That was **1.1.4**.

**Speaker Notes:**  
1.2.4 was TLS on :443. This is HTTP Zeek still parsed.

---

### Slide 3 – Method, host, URI
**Title:** Method, host, URL

**`method`** — GET, POST, PUT, …  
**`host`** — Host header.  
**`uri`** — path and query.

**URL** = host + URI.

**Speaker Notes:**  
Outline a–c. There is often no single `url` field.

---

### Slide 4 – UA, status, who
**Title:** User-Agent, status, addresses

**`user_agent`** — what the client claimed. Can lie. Empty = not logged.  
**`status_code`** — 200 is not benign. 404 is not safe.

**`id.orig_*` → `id.resp_*`** — who talked to whom.

**Speaker Notes:**  
Outline d–f.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No process name.  
No body dump. File extract is **1.2.7**.  
Encrypted HTTPS often has no `http` row (**1.2.4**).

**Speaker Notes:**  
SMTP next.

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: method, host+URI, status, dest.

**Given:** `GET /update.exe` → `203.0.113.88:8080`, `200`, UA empty.

A query names a **specific** pattern — method, host, URI, UA, or dest.  
Not “all `http` rows.”

**Speaker Notes:**  
GET of update.exe from that IP on 8080, 200. UA not logged. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. `host` is the destination IP. True or false?  
2. `GET /update.exe` to `203.0.113.88:8080`, status `200`, UA empty. In one sentence, what occurred?  
3. A SIEM query that matches every `http` row is a good “specific HTTP activity” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Method, host+URI, UA, status, who talked to whom.  
The process is not on this row.  
A query is specific.

**Next:** **1.2.6** SMTP engine

**Speaker Notes:**  
Mail from / rcpt to next.
