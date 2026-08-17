# Module 1.2.3 – DNS Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.3 – DNS Engine  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
DNS extract. Question and answer. Not DGA. Not the process.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read the Zeek **`dns`** log: the name that was asked, and what answered.

It does **not** name the initiating process.  
That was **1.1.4**.

**Speaker Notes:**  
1.2.2 was the conn to 203.0.113.88. This is the lookup next to that flow.

---

### Slide 3 – Question and answer
**Title:** Query and answers

**`query`** — the name that was asked.  
**`answers`** — what came back. Empty means Zeek did not get a record.

**Speaker Notes:**  
Outline a–b. Do not invent a DGA lecture.

---

### Slide 4 – Type, who asked whom
**Title:** Record type, source, dest

**`qtype_name`** — **A**, **AAAA**, **MX**, **CNAME**, **NS**, **TXT**, and the rest when you see them.

**`id.orig_h`** — who asked.  
**`id.resp_h`** — which resolver. Not the A record.

**Speaker Notes:**  
Outline c–d. CNAME is another name, not an address.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No process name.  
No tunneling / DGA methodology.  
The `conn` to `:443` is a different row (**1.2.2**).

**Speaker Notes:**  
PCAP still verifies or expands.

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: who asked, which name, which type, what answered.

**Given:** workstation, type `A`, answers `["203.0.113.88"]`.

A query names a **specific** pattern — `query`, type, or `answers`.  
Not “all `dns` rows.”

**Speaker Notes:**  
That host asked for that name and got A 203.0.113.88. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. `id.resp_h` on a `dns` row is the IP the name resolved to. True or false?  
2. Workstation queries a hostname, type `A`, answers `["203.0.113.88"]`. In one sentence, what occurred?  
3. A SIEM query that matches every `dns` row is a good “specific DNS activity” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Question, type, answer, who asked which resolver.  
The process is not on this row.  
A query is specific.

**Next:** **1.2.4** TLS engine

**Speaker Notes:**  
SNI and cert next. Not DNS.
