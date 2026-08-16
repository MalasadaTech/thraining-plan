# Module 3.10.2 – STIX in Production  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.10.2 – STIX in Intelligence Production  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Links, validate, TAXII. Not a 3.10.1 redo.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Structure a shareable bundle
2. Link with real relationship types
3. Create and validate objects
4. Publish or consume via TAXII

**Mapped Items:**  
K: 3.10.2 | T: 3.10.2.1 · 3.10.2.2 · 3.10.2.3

**Speaker Notes:**  
CTI 4d on graph and validate. TAXII is 4c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Structure, links, validate, TAXII
- Three examples
- Lines + scenario sentence
- Knowledge check

**Speaker Notes:**  
Closes 3.10. 3.11 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Label types only (**3.10.1**)  
Hunt leads (**2.4.3**)  
Narrative product (**3.11**)  
TIP keyword search (**3.3.1**)

**Key Point:** Real types. Valid objects. TAXII ≠ PDF.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Bundle + TAXII
**Title:** Payload and Channel

Bundle = objects + links.  
TAXII = publish/consume a collection.

**Speaker Notes:**  
Outline a. Classroom `harbor-cti`.

---

### Slide 6 – Real Relationship Types
**Title:** indicates · uses · targets · mitigates

No `connects-to`.  
No `attributed-to` without a who.

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Validate
**Title:** Required Fields

Pattern + type.  
Source + target + relationship_type.  
Unearned threat-actor = invalid.

**Speaker Notes:**  
3.10.2.2.

---

### Slide 8 – Lines
**Title:** Three Lines + One Sentence

`source | relationship_type | target`  
`object | valid or invalid | why`  
`publish or consume | collection | what moves`  
Plus a one-line scenario.

**Speaker Notes:**  
Tasks.

---

### Slide 9 – Example 1
**Title:** Example 1 – Night Owl Graph

indicates / uses / sighting_of / mitigates.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2
**Title:** Example 2 – Invalid

Missing type. Vendor APT actor.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3
**Title:** Example 3 – Not TAXII

Emailing the PDF is 3.11 dissemination.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Invented relationship types  
- attributed-to a PDF name  
- PDF email as TAXII  
- Scenario sentence becomes a profile  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Same types on a live TAXII collection.  
Keep: validate before publish. Do not stand up a server this hour.

**Speaker Notes:**  
`harbor-cti` is lesson-only.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–C links + scenario.
3. D–F validate.
4. G–H TAXII.
5. No hunt card. No 3.11 product.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Bundle for?
2. One real relationship_type?
3. What makes an object invalid?
4. TAXII vs the bundle?
5. Where is the prose product?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Link. Validate. Publish the bundle.
- Next unit: **3.11** production and dissemination.

**Speaker Notes:**  
Do not open 3.11 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Production — Quick Reference

| Move | Take |
|------|------|
| indicates | domain → malware |
| uses | malware → T1059.001 |
| Validate | pattern + relationship_type |
| TAXII | publish/consume `harbor-cti` |
| PDF email | not TAXII |

**Coming next:** Module 3.11.1 – Creating finished intelligence products

**Footer:** SOC / Hunter / CTI Training Program
