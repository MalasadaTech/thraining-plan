# Module 1.2.5 – HTTP Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.5 – HTTP Engine  
**Subtitle:** Request and response on the wire  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.2.4 was the TLS handshake. This lesson is HTTP that Zeek parsed. It is not the process on the host and not the file extract.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read Zeek **`http`** logs to see a request and response on the wire.

Method, host, URI, User-Agent, status, who talked to whom.  
Not the initiating process. Not the body.

**Speaker Notes:**  
This is daily alert work: describe the HTTP event. Process and file extract wait for other lessons.

---

### Slide 3 – Method, host, URI
**Title:** Method, host, URL

**`method`** — GET, POST, PUT, …  
**`host`** — the Host header, not the destination IP. Empty means not logged.  
**`uri`** — path and query.

**URL** = host + URI. There is often no single `url` field.

**Speaker Notes:**  
Walk method, host, and URI first. Do not invent a Host header if the log does not have one.

---

### Slide 4 – UA, status, who
**Title:** User-Agent, status, addresses

**`user_agent`** — what the client claimed. Can lie. Empty means not logged.  
**`status_code`** — 200 is not benign. 404 is not safe.

**`id.orig_*` → `id.resp_*`** — who talked to whom. Destination IP is `id.resp_h`, not `host`.

**Speaker Notes:**  
Status is the protocol answer, not a verdict. orig and resp are the addresses on this log.

---

### Slide 5 – Metadata, not body or process
**Title:** Metadata, not body or process

You usually do **not** get the body. File extract is **1.2.7**.  
This log does **not** name the initiating process. That is **1.1.4**.  
Encrypted HTTPS often has no `http` log (**1.2.4**).

**Speaker Notes:**  
Stay on this engine. If they open TLS SNI, that is a different log. SMTP is next.

---

### Slide 6 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: method, host+URI, status, dest.

**Given:** `GET /update.exe` → `203.0.113.88:8080`, `200`, User-Agent empty.

A query names a **specific** pattern — method, host, URI, User-Agent, or dest.  
Not every `http` log.

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: GET of `/update.exe` from that IP on 8080, status 200. User-Agent not logged. Do not tell the intro plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. `host` is the destination IP. True or false?  
2. `GET /update.exe` to `203.0.113.88:8080`, status `200`, User-Agent empty. In one sentence, what occurred?  
3. A SIEM query that matches every `http` log is a good “specific HTTP activity” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Method, host+URI, User-Agent, status, who talked to whom.  
The process is not on this log.  
A query is specific.

**Next:** **1.2.6** SMTP engine

**Speaker Notes:**  
1.2.6 is SMTP on the same wire telemetry. Stay off this HTTP log when you get there.
