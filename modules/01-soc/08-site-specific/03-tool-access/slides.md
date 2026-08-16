# Module 1.8.3 – Tool Access and Requests  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.8.3 – Tool Access and Requests  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Open vs install vs entitle. Overlay site catalog if you have one.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Open the named URL
2. `SOFT-REQ` when the binary is missing
3. `ACCESS-REQ` when you get 403
4. Reject the neighbor action

**Mapped Items:**  
T: 1.8.3.1 | 1.8.3.2 | 1.8.3.3

**Speaker Notes:**  
Hunter 3-level is 3c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Harbor tool card
- Three examples
- Four access lines
- Knowledge check

**Speaker Notes:**  
1.8.4 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Export the pcap **file** (**1.8.2**)  
Where notes are saved (**1.8.4**)  
IR page / isolate (**1.8.5**)

**Key Point:** How you get *onto* the tool.

**Speaker Notes:**  
Fence.

---

### Slide 5 – URLs
**Title:** Open These

SIEM `siem.harbor.internal`  
EDR `edr.harbor.internal`  
PCAP UI `pcap.harbor.internal`  
Tickets `ticket.harbor.internal`

**Speaker Notes:**  
Task 1.

---

### Slide 6 – Two Tickets
**Title:** Missing Binary vs Missing Login

**`SOFT-REQ`** — Wireshark / editor not on the box  
**`ACCESS-REQ`** — URL works, **403** / no account

**Speaker Notes:**  
Tasks 2–3.

---

### Slide 7 – Access Line
**Title:** Four Fields

`need | open / SOFT-REQ / ACCESS-REQ | URL or ticket | rejected`

**Speaker Notes:**  
Pick one action.

---

### Slide 8 – Neighbor Fails
**Title:** Not These

Random installer  
Shared password  
`PCAP-REQ` when you cannot *log in*

**Speaker Notes:**  
Usual leads.

---

### Slide 9 – Example 1: SIEM
**Title:** Example 1 – You Have an Account

Open the URL.  
Do not outsource the query.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Mirror
**Title:** Example 2 – Wireshark Missing

`SOFT-REQ`.  
Not a random download.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: 403
**Title:** Example 3 – EDR Forbidden

`ACCESS-REQ`.  
Not `SOFT-REQ`. Not Pat’s session.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Unofficial Wireshark  
- Install ticket for a 403  
- Shared password  
- Mixing PCAP-REQ and ACCESS-REQ  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use the site catalog if posted.  
Keep: open / install / entitle.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize Ex 1–3.
2. A–D: access line.
3. No PCAP export. No IR.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. When do you just open the URL?
2. Wireshark ticket — and what not to do?
3. SIEM 403 — which ticket?
4. ACCESS-REQ vs PCAP-REQ?
5. Why not a shared password?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Open / `SOFT-REQ` / `ACCESS-REQ`.
- Reject the neighbor action.
- Next: **1.8.4** investigation notes.

**Speaker Notes:**  
Do not open 1.8.4 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Tool Access — Quick Reference

| Blocker | Action |
|---------|--------|
| Have login | Open URL |
| No binary | SOFT-REQ |
| 403 / no account | ACCESS-REQ |
| Old pcap file | 1.8.2 PCAP-REQ |

**Coming next:** Module 1.8.4 – Investigation notes

**Footer:** SOC / Hunter / CTI Training Program
