# Module 3.8.3 – IOC Handling  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.8.3 – Handle the IOCs  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Not the hop sentence. File the objects.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. IOC ≠ TTP
2. Keep / expire / reject
3. Record the next enrichment
4. Link objects, not names

**Mapped Items:**  
K: 3.8.3 | T: 3.8.3.1 | T: 3.8.3.2

**Speaker Notes:**  
CTI 4d on both tasks.

---

### Slide 3 – Agenda
**Title:** Agenda

- Handle + enrich + link
- Three examples
- Exercise
- Knowledge check

**Speaker Notes:**  
3.8.4 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Hop sentence (**3.8.1**)  
TTP apply (**3.8.2**)  
Tool labs (**3.5 / 3.6 / 3.9**)  
Impact (**3.8.4**)  
Actor profile (**3.11**)

**Key Point:** Handle the tray.

**Speaker Notes:**  
Fence.

---

### Slide 5 – IOC vs TTP
**Title:** Observable vs Behavior

Domain, hash, Run key  
Not “they use PowerShell”

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Keep / Expire / Reject
**Title:** Handling Rules

Keep = cited, current, distinctive  
Expire = stale  
Reject = uncited / shared / not an IOC

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Enrich Line
**Title:** Name the Next Lookup

IOC | known tool | field | hope to learn

**Speaker Notes:**  
Do not run it. Do not write the hop.

---

### Slide 8 – Link Line
**Title:** Same Set?

Shared cite on this card.  
Not a vendor name.

**Speaker Notes:**  
Outline d. 4d lives here.

---

### Slide 9 – Classroom Tray
**Title:** Tray

Domain + hash + Run + A = cited  
2019 IP / /24 / evil-c2 / “APT” = not keep

**Speaker Notes:**  
Leave up.

---

### Slide 10 – Example 1
**Title:** Expected — One Set

Keep four. Enrich the domain. Link by host + A.

**Key Point:** Product shape.

**Speaker Notes:**  
Students write first.

---

### Slide 11 – Example 2
**Title:** Lead — Keep the Noise

2019 IP, /24, uncited name.

**Key Point:** Fail.

**Speaker Notes:**  
Expire vs reject.

---

### Slide 12 – Example 3
**Title:** Lead — APT as Glue

A label is not a link.

**Key Point:** Fail.

**Speaker Notes:**  
Park 3.11.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Rewrite 3.8.1  
- Open VT  
- Keep the /24  
- Glue with “APT”  

**Speaker Notes:**  
Park all four.

---

### Slide 14 – Hands-On Exercise
**Title:** Exercise

Handle A–E. Enrich A/B. Link the set. Reject E as glue.

**Speaker Notes:**  
C expire. D/E reject.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. IOC vs TTP?  
2. Expire vs reject?  
3. Enrich line?  
4. Same set?  
5. Why not the APT name?

**Speaker Notes:**  
Answers in the instructor guide.

---

### Slide 16 – Summary
**Title:** Summary

Handle. Record the lookup. Link objects.

**Coming next:** Module 3.8.4 – Relevance and impact

**Speaker Notes:**  
So what *here*.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Three Lines

`IOC | type | keep/expire/reject | why`  
`IOC | tool | field | hope to learn`  
`objects | same set? | cite | not a name`

**Speaker Notes:**  
Leave up during the exercise.
