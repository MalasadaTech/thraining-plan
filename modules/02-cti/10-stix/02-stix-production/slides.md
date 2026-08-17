# Module 2.10.2 – STIX in Production  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.10.2 – STIX in Production  
**Subtitle:** CTI Analyst (Hunter / SOC sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Links + valid object + consume. No TAXII server.

---

### Slide 2 – What this hour is
**Title:** What this hour is

**Connect** objects.

Explain the **A12** scenario those links tell.  
Pull a classroom collection. Do not build a server.

**Speaker Notes:**  
Object names were 2.10.1.

---

### Slide 3 – Relationships and validate
**Title:** Real types only

`indicates` · `based-on` · `targets` · `uses` · `related-to` · `sighting-of`

Validate: type, id, spec_version `2.1`, created.

**Speaker Notes:**  
Outline a–b. Tasks 1–2.

---

### Slide 4 – What good looks like
**Title:** A12 links + TAXII

Indicator (hash) **indicates** Attack Pattern.  
Sighting **sighting-of** that Indicator on Identity **WS-JLEE**.

TAXII: **pull collection X**. Not “I stood up TAXII.”

**Speaker Notes:**  
Task 3.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No invented types.  
No TAXII server.  
No narrative product (**2.11**).  
No lumped 2.10.3.

**Speaker Notes:**  
Finished products next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. You should stand up a TAXII server in this hour. True or false?  
2. Name two real relationship types.  
3. Write one relationship that ties the `invoice.vbs` hash to **WS-JLEE**.

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Real links. Valid objects. TAXII is consume.

**Next:** **2.11.1** Finished intelligence products

**Speaker Notes:**  
Do not open 2.11 unless scheduled.
