# Module 1.2.8 – Weird Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.8 – Weird Engine  
**Subtitle:** Protocol behavior that is off-spec or uncommon  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.2.7 was the file on the wire. This lesson is the last 1.2 engine: the protocol looked off. It is not `notice.log` and not a process event.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read the Zeek **weird** log when the protocol looked off-spec or uncommon.

A **weird** event is a **lead**, not a verdict.  
It does not name the process.

**Speaker Notes:**  
This slide is the student intro. Daily alert work: say what Zeek flagged, who talked to whom, and which connection to open. Do not call it malware today.

---

### Slide 3 – Type and notice
**Title:** Type and notice

**`name`** — the weird type. The string you query.

**`notice`** — a boolean: whether *this* type was also raised as a notice.  
This is not a `notice.log` lesson.

Do not memorize the catalog. Describe the `name` you have.

**Speaker Notes:**  
This slide is the type. The field `notice` lives on this log. If they open the notices table, bring them back. Many names fire on noisy or broken traffic. The next slide is who talked and the connection ID.

---

### Slide 4 – Who talked, and the UID
**Title:** Who talked, and the UID

**`id.orig_*` → `id.resp_*`** — who talked to whom.

**`uid`** — the same join as other Zeek logs (`conn`, `http`, `files`).  
If `uid` is empty, write “no uid.” Use IP, port, and time if they are logged.

**Speaker Notes:**  
A weird event often belongs to a connection. Copy the uid and open conn. If uid is missing, you still have the type and whatever addresses were logged.

---

### Slide 5 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: Zeek flagged this `name` between these IPs.

**Given:** `name` `data_before_established`, dest `203.0.113.88:8080`, `uid` present.

A query names a **specific** `name` (or dest).  
Not every **weird** event.

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: data before the handshake finished to that dest. Open conn on the uid. Do not name a process. Do not tell the course fiction plot.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A single **weird** event is an incident. True or false?  
2. `name` `data_before_established`, dest `203.0.113.88:8080`, `uid` present. In one sentence, what occurred?  
3. A SIEM query that matches every **weird** event is a good “specific weird activity” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

A **weird** event is a type, two endpoints, and a UID.  
It is a lead, not a verdict.  
A query names a specific type.

**Speaker Notes:**  
SIGMA is next. Stay off this engine when you get there. How detections run as a service is 4.x.

---

### Slide 8 – Next
**Title:** Next

**1.3.1** SIGMA rules

**Speaker Notes:**  
1.2 is done. Detection syntax is next. Do not start writing SIGMA on this weird event today.
