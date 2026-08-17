# Module 1.8.1 – Environment Orientation  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.8.1 – Environment Orientation  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Harbor card is a stand-in. Overlay site if you have it.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Seven orientation facts
2. Which fact applies — reject the neighbor

**Mapped Items:**  
K: 1.8.1.1 | T: 1.8.1.2

**Speaker Notes:**  
CTI 3-level task is 1a.

---

### Slide 3 – Agenda
**Title:** Agenda

- Harbor card a–g
- Three examples
- Four fact + neighbor pairs
- Knowledge check

**Speaker Notes:**  
Tool access (1.8.3) is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

How to **download** PCAP (**1.8.3** if listed)  
Tool URLs (**1.8.3**)  
Zeek fields (**1.2**)  
IR containment (**1.8.5**)

**Key Point:** Where it sits. Which fact.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Egress, Segments, Email
**Title:** a–c

**a.** User/server → `fw-edge-01`. Guest → `fw-guest`.  
**b.** Users `.8`, servers `.20`, OT `.50`. No user→OT init.  
**c.** `mail-edge` → filter → `mail-int`. Not raw NAT.

**Speaker Notes:**  
Outline a–c.

---

### Slide 6 – Chokes, Third-Party, Jewels
**Title:** d–f

**d.** `fw-edge-01`, `fw-ot`, `fw-guest`  
**e.** `vpn-vendor` `.90`; payroll SaaS via `idp-corp`  
**f.** `pay-db-01`, `dc-01`, `ot-hist-01`

**Speaker Notes:**  
Outline d–f.

---

### Slide 7 – Sensors
**Title:** g — Where Packets Are Kept

`span-1` = fw-edge (internet)  
`span-2` = core (user ↔ server)  
**No** span on `fw-ot`

**Speaker Notes:**  
Outline g. Download is 1.8.2.

---

### Slide 8 – Sentence Shape
**Title:** Fact + Neighbor

`letter | fact | rejected neighbor | why`

**Speaker Notes:**  
Task.

---

### Slide 9 – Example 1: A12
**Title:** Example 1 – How Did It Leave?

Egress + **span-1**.  
Not OT. Not email.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Vendor Mail
**Title:** Example 2 – Email Path

`mail-edge` chain.  
“It went to the internet” is the wrong fact.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: OT PCAP
**Title:** Example 3 – Missing Span

No sensor on `fw-ot`.  
Do not promise span-2.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Everything is egress  
- span-2 sees OT  
- Scanner = vendor VPN  
- Opening 1.8.2 now  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use the site card if posted.  
Keep the seven outline facts.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize Ex 1–3.
2. A–D: fact + neighbor.
3. No export. No IR.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Name the seven facts.
2. Guest vs user egress?
3. Why email ≠ egress?
4. Which sensor sees OT?
5. Why is “describe the network” not enough?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Seven facts. Pick one. Reject the neighbor.
- Next: **1.8.3** tool access. Why you pull PCAP is **1.2.1**.

**Speaker Notes:**  
Do not open 1.8.2 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Harbor Orientation — Quick Reference

| Letter | Harbor |
|--------|--------|
| a | fw-edge-01 / fw-guest |
| b | .8 user / .20 server / .50 OT |
| c | mail-edge → filter → mail-int |
| d | fw-edge, fw-ot, fw-guest |
| e | vpn-vendor .90; idp-corp |
| f | pay-db-01, dc-01, ot-hist-01 |
| g | span-1, span-2, no OT span |

**Coming next:** Module 1.8.3 – Tool access

**Footer:** SOC / Hunter / CTI Training Program
