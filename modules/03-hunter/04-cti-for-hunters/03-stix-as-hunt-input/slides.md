# Module 3.4.3 – STIX as Hunt Input  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.4.3 – STIX as Hunt Input  
**Subtitle:** Read the bundle. Do not author STIX.  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is hunt reading STIX as input. Spec is STIX 2.1. It is not how to author, validate, or share a bundle.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Hunters read CTI as a **report** or a **STIX** bundle.

Structured JSON looks official. It is not automatically a hunt.

Name the objects that can drive a search. Turn them into a question that can fail.

**Speaker Notes:**  
This slide is the student intro. A bundle is a wrapper that carries labeled objects as one package. Authoring is 2.10. Extract from prose is 3.4.2. Stay on identify, then seed.

---

### Slide 3 – Objects a hunter uses
**Title:** Objects a hunter uses

**indicator** — current pattern you can query.  
**attack-pattern** — a method you can search, and you have telemetry.  
**observed-data** — a recorded sample that still names something searchable.  
**malware** — a current hash or named installer, not the family slogan.  
**threat-actor** / **intrusion-set** — scope or priority. Not a search.  
**relationship** — ties those objects together (`indicates`, `uses`).

An actor name is **not** a search.

**Speaker Notes:**  
These six are the hunter list. Campaign, course-of-action, identity, and sighting exist in STIX 2.1 and may appear. Do not walk the rest of 2.10.

---

### Slide 4 – How a bundle seeds a hunt
**Title:** How a bundle seeds a hunt

A bundle **seeds** a hunt when the objects you pick can support a **question** that can fail.

Structured JSON is not automatically a hunt.  
Dumping every IPv4 **indicator** is not a seed.

You do not write STIX here.

**Speaker Notes:**  
Seed means starting input, not the hunt itself. If they start TAXII or validating objects, that is 2.10. Navigator is 3.5.

---

### Slide 5 – Identify, then seed
**Title:** Identify, then seed

Classroom bundle (**A12**):  
`indicator` `GET /update.exe` `203.0.113.88:8080`  
`attack-pattern` HKCU Run **`Updater`**  
`relationship` `uses`

**Question** — if more persistors exist, we see that Run value or that URI.  
**Not** dump every IPv4 `indicator`.

**Speaker Notes:**  
This is the student-guide given. The product is the object names plus the question. Do not retell the A12 plot and do not write a new STIX graph.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Hunters author STIX in this lesson. True or false?  
2. Name four objects a hunter actually uses.  
3. A classroom bundle has an `indicator` for `GET /update.exe` on `203.0.113.88:8080` and an `attack-pattern` for HKCU Run **`Updater`**. Name one hunt-relevant object and the lead it seeds.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Identify hunt-relevant STIX objects.  
Seed a question that can fail.  
Do not author STIX.

**Next:** **3.5.1** ATT&CK for hunt planning

**Speaker Notes:**  
3.5.1 maps this hunt onto ATT&CK. Do not open Navigator unless scheduled.
