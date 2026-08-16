# Module 3.10.1 – Core STIX Objects  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.10.1 – Core STIX Objects  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Full inventory. Not hunt-relevant slice. Real STIX 2.1 types.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Name the eleven types
2. Label a report span
3. Reject the neighbor type
4. Leave graphs and products for later

**Mapped Items:**  
K: 3.10.1 | T: 3.10.1.1

**Speaker Notes:**  
SOC K is A/B/B. Task ends at 4c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Eleven types
- Three examples
- Seven label lines
- Knowledge check

**Speaker Notes:**  
3.10.2 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Hunt-relevant slice (**2.4.3**)  
Draw the graph / TAXII (**3.10.2**)  
Narrative product (**3.11**)  
Vendor name as Adversary (**3.7.2**)

**Key Point:** Label. Do not invent types.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Patterns vs Seen vs Sample
**Title:** Indicator · Observed Data · Malware

Look-for · was-seen · the file.

**Speaker Notes:**  
a–c.

---

### Slide 6 – How vs Who vs When
**Title:** Attack Pattern · Actor · Set · Campaign

How ≠ who ≠ time-bounded op.  
Empty who is honest.

**Speaker Notes:**  
d–g.

---

### Slide 7 – Defend · Victim · Link · Saw
**Title:** CoA · Identity · Relationship · Sighting

You draw the link next hour.

**Speaker Notes:**  
h–k.

---

### Slide 8 – Label Line
**Title:** Three Fields

`span | STIX type | not the neighbor because`

**Speaker Notes:**  
Task.

---

### Slide 9 – Example 1
**Title:** Example 1 – Four Honest Labels

Domain = indicator. GET row = observed-data.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2
**Title:** Example 2 – Not a Threat Actor

“Night Owl APT” stays empty.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3
**Title:** Example 3 – Sighting ≠ Indicator

WS-JLEE *saw* the pattern.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Invented types (`ioc`, `apt`)  
- Log row as indicator  
- Technique as campaign  
- Vendor name as actor  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Same eleven types on a live TIP bundle.  
Keep: real types; empty who is honest.

**Speaker Notes:**  
Do not invent org schema.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–G: label lines.
3. No graph. No hunt card.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Indicator vs observed-data?
2. When is threat-actor empty?
3. Why not campaign for T1059.001?
4. Sighting points at?
5. Where do you link them?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Eleven types. Reject the neighbor.
- Next: **3.10.2** production.

**Speaker Notes:**  
Do not open 3.10.2 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** STIX Types — Quick Reference

| Span | Type |
|------|------|
| Domain to query | indicator |
| Zeek row | observed-data |
| `update.exe` | malware |
| T1059.001 | attack-pattern |
| Vendor APT | none |
| WS-JLEE saw it | sighting |

**Coming next:** Module 3.10.2 – STIX in production

**Footer:** SOC / Hunter / CTI Training Program
