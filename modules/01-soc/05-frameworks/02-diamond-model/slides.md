# Module 1.5.2 – Diamond Model  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.5.2 – Diamond Model  
**Subtitle:** SOC / Hunter / CTI Training  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Four vertices. Unknown adversary is OK. Not a profile. Hunter/CTI 7 is 4d.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Purpose of the Diamond Model
2. Four vertices: Adversary, Capability, Infrastructure, Victim
3. Fill all four and name the weakest

**Mapped Items:**  
K: 1.5.2.1 | T: 1.5.2.2

**Speaker Notes:**  
SOC 3 is A / 2b.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose
- Four vertices
- Attribution = don’t invent
- Three examples
- Three cards
- Knowledge check

**Speaker Notes:**  
1.5.3 next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

ATT&CK IDs (**1.5.1**)  
Kill Chain stages (**1.5.3**)  
Actor profile (**3.11**)  
Naming an APT from one IP

**Key Point:** Honest four-box fill.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Purpose
**Title:** What Diamond Is For

Organize **know / don’t know**.  
See the relationship among four features.  
Supports analysis and later attribution.

**Speaker Notes:**  
Outline a, c.

---

### Slide 6 – Four Vertices
**Title:** A / C / I / V

**Adversary** — who directs  
**Capability** — method / tool  
**Infrastructure** — systems they use  
**Victim** — who/what is acted on  

**Speaker Notes:**  
Outline b. Draw the diamond.

---

### Slide 7 – Empty Is Honest
**Title:** Weakest Vertex

Empty box = weak.  
Circle it.  
Next look is SOC-sized (log/PCAP), not a CTI paper.

**Speaker Notes:**  
Task.

---

### Slide 8 – Attribution
**Title:** IP ≠ Actor

Infrastructure can be full.  
Adversary can still be **unknown**.  
One dest IP is not a group name.

**Speaker Notes:**  
Outline c.

---

### Slide 9 – Example 1: Beacon Story
**Title:** Example 1 – Encoded PS + POST

A unknown  
C `-enc` + POST beacon  
I nightowl / 203.0.113.88  
V jlee / WS-JLEE  

**Weakest:** Adversary.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Over-Fill
**Title:** Example 2 – IP Only

Do not write “Night Owl gang.”  
Victim may be only `10.10.22.17`.

**Speaker Notes:**  
Invented adversary is the lead.

---

### Slide 11 – Example 3: No Wire
**Title:** Example 3 – Run Key Only

Capability: Run persist + drop.  
Infrastructure: **empty**.  
Weakest: Infrastructure (or Adversary).

**Speaker Notes:**  
Next: 1.1.3 / 1.2, not a name.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- APT from IP  
- Skipping empty boxes  
- Capability = “malware”  
- ATT&CK instead of vertices  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Card Shape
**Title:** Four Boxes + Weakest

A: …  
C: …  
I: …  
V: …  
Weakest: …

**Speaker Notes:**  
Leave up.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize Ex 1–3 (weakest).
2. Fill A/C/I/V for cases A–C; circle weakest.
3. No group names. No Kill Chain.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Purpose?
2. Four vertices and their questions?
3. Why “unknown” on Adversary?
4. What is the weakest vertex for?
5. Why not an actor profile?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Four vertices. Empty is honest.
- Weakest vertex drives the next look.
- Next: Cyber Kill Chain (**1.5.3**).

**Speaker Notes:**  
Do not open Kill Chain unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Diamond — Quick Reference

| Vertex | Question |
|--------|----------|
| Adversary | Who directs? |
| Capability | What method? |
| Infrastructure | What systems? |
| Victim | Who is acted on? |

**Coming next:** Module 1.5.3 – Cyber Kill Chain

**Footer:** SOC / Hunter / CTI Training Program
