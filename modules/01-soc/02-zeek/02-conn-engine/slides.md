# Module 1.2.2 – Conn Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 1.2.2 – Conn Engine  
**Subtitle:** Who talked to whom on the wire  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.2.1 said engines extract protocol data. This lesson is the `conn` extract. It is not the initiating process, and it is not a scan course.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read the Zeek **`conn`** log to see who talked to whom on the **wire**.

Originator. Responder. How the connection ended.  
It does **not** name the initiating process. That is **1.1.4**.

**Speaker Notes:**  
This slide is the student intro. Daily alert work is to describe the connection, not to name a process or open DNS yet.

---

### Slide 3 – Originator and responder
**Title:** Originator and responder

**`id.orig_h` / `id.orig_p`** — originator IP and port. Who started the talk from Zeek’s view.

**`id.resp_h` / `id.resp_p`** — responder IP and port. Who was contacted.

Originator is not automatically an internal host. It is not the destination.

**Speaker Notes:**  
Walk source as originator and destination as responder. If they treat orig as “our network,” correct it here before state.

---

### Slide 4 – How it ended
**Title:** State and history

**`SF`** — established and torn down cleanly.  
**`S0`** — attempt, no reply.  
**`REJ`** — attempt refused.

**`history`** — short flags of what was seen (`S` SYN, `H` SYN-ACK, `F` FIN, `R` RST).

If you see another state, say what the field shows.

**Speaker Notes:**  
These three states are enough to start. Do not inventory every rare `conn_state`. History is the flag string, not a second story.

---

### Slide 5 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: originator IP/port → responder IP/port, state.

**Given:** workstation → `203.0.113.88:443`, `conn_state` `SF`.

A query names a **specific** pattern — responder IP or port + state.  
Not every connection.

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: that host completed a TCP connection to that IP on 443. Who launched the socket is 1.1.4. Do not tell the course-fiction plot.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. `id.orig_h` is the destination IP. True or false?  
2. Workstation → `203.0.113.88:443`, `SF`. In one sentence, what occurred?  
3. A SIEM query that matches every connection is a good “specific connection activity” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Who talked to whom, on which ports, how it ended.  
The process is not on this log.  
A query is specific.

**Next:** **1.2.3** DNS engine

**Speaker Notes:**  
1.2.3 is the DNS extract on the same wire telemetry. Stay off `conn` fields when you get there.
