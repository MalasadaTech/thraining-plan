# Module 1.2.2 – Conn Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.2.2 – Conn Engine  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
First engine. Five fields. Not the process. Not a scan course.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read the Zeek **`conn`** log: who talked to whom on the **wire**.

It does **not** name the initiating process.  
That was **1.1.4**.

**Speaker Notes:**  
1.2.1 said engines extract. This is the extract.

---

### Slide 3 – Who talked to whom
**Title:** orig and resp

**`id.orig_h` / `id.orig_p`** — who started the talk.  
**`id.resp_h` / `id.resp_p`** — who was contacted.

**Speaker Notes:**  
Outline a–d. orig is not “internal.” It is originator from Zeek’s view.

---

### Slide 4 – How it ended
**Title:** State and history

**`SF`** — established and torn down cleanly.  
**`S0`** — attempt, no reply.  
**`REJ`** — attempt refused.

**`history`** — short flags (`S` SYN, `H` SYN-ACK, `F` FIN, `R` RST).

**Speaker Notes:**  
Outline e. Do not inventory every rare state.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No process name.  
No beacon math.  
PCAP still verifies or expands (**1.2.1**).

**Speaker Notes:**  
DNS fields wait. uid-pivot is not this outline.

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: orig IP/port → resp IP/port, state.

**Given:** workstation → `203.0.113.88:443`, `conn_state` `SF`.

A query names a **specific** pattern — resp IP or port + state.  
Not “all `conn` rows.”

**Speaker Notes:**  
Completed TCP to that IP on 443. Who launched the socket is 1.1.4. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. `id.orig_h` is the destination IP. True or false?  
2. Workstation → `203.0.113.88:443`, `SF`. In one sentence, what occurred?  
3. A SIEM query that matches every `conn` row is a good “specific connection activity” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Who talked to whom, on which ports, how it ended.  
The process is not on this row.  
A query is specific.

**Next:** **1.2.3** DNS engine

**Speaker Notes:**  
Same flow can have a dns row next.
