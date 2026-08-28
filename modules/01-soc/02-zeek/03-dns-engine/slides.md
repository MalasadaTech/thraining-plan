# Module 1.2.3 – DNS Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.3 – DNS Engine  
**Subtitle:** The name that was asked, and what answered  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.2.2 was the connection on the wire. This lesson is the DNS extract. It is not DGA, and it is not the initiating process.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read Zeek **`dns`** logs to see a name lookup on the **wire**.

Who asked. Which name. Which type. What came back.

Not the initiating process. That was **1.1.4**.  
Not TLS.

**Speaker Notes:**  
This slide is the student intro. Daily alert work: describe the lookup. The connection was 1.2.2. Do not teach TLS or HTTP fields today.

---

### Slide 3 – Question and answer
**Title:** Query and answers

**`query`** — the name that was asked.  
**`answers`** — what came back (an address, another name, or empty).

Empty means this log does not show a returned record.

**Speaker Notes:**  
Walk question and answer before types. Do not start an NXDOMAIN hunt from an empty answers list. Do not invent a DGA lecture.

---

### Slide 4 – Record types
**Title:** Record types

**A** — IPv4 address.  
**AAAA** — IPv6 address.  
**MX** — mail exchanger.  
**CNAME** — another name, not an address.  
**NS** — name server.  
**TXT** — text data.

**Speaker Notes:**  
These are the types this lesson names. CNAME is the usual mix-up: it is another name, not an address. Other types can wait until they appear in a log.

---

### Slide 5 – Who asked which DNS server
**Title:** Who asked which DNS server

**`id.orig_h`** — who asked.  
**`id.resp_h`** — the DNS server that was asked.

That server is often a resolver.  
It is **not** the A record. The A, when present, is in **`answers`**.

**Speaker Notes:**  
This is the trap. People write the resolver IP as “what the name resolved to.” Stop them. The TCP connection to that A is a different log (1.2.2).

---

### Slide 6 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: who asked, which name, which type, what answered.

**Given:** workstation, type `A`, answers `["203.0.113.88"]`.

A query names a **specific** pattern — `query`, type, or `answers`.  
Not every `dns` event.

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: that host asked for that name and got A 203.0.113.88. Do not name a process. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. `id.resp_h` on a `dns` log is the IP the name resolved to. True or false?  
2. Workstation queries a hostname, type `A`, answers `["203.0.113.88"]`. In one sentence, what occurred?  
3. A SIEM query that matches every `dns` log is a good “specific DNS activity” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Question, type, answer, who asked which DNS server.  
The process is not on this log.  
A query is specific.

**Next:** **1.2.4** TLS engine

**Speaker Notes:**  
1.2.4 is SNI and certificate on the same wire. Stay off this dns log when you get there.
