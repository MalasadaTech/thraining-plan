# Module 2.10.2 – How STIX Objects Are Used in Intelligence Production  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.10.2 – How STIX objects are used in intelligence production  
**Subtitle:** Link, validate, and share the graph  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
2.10.1 named the object types. This lesson is the production step: link those objects, check they are valid, and consume a classroom collection. It is not how to write the finished narrative, and it is not how to stand up a TAXII server.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

A hash in a slide is not reusable.

CTI analysts **connect** the objects, **validate** them, and **share or pull** the package so other tools can ingest the same story.

This lesson is that production step.

**Speaker Notes:**  
This slide is the student intro. The job is a reusable graph, not a PDF. Stay off the finished product and off TIP search. Object names were last lesson.

---

### Slide 3 – Bundle for sharing and automation
**Title:** Structure it as a bundle

A **bundle** is the wrapper that carries STIX objects together.

That package is what machines ingest.  
A PDF you email is not a STIX bundle.

The bundle is the **payload**. TAXII is the **channel**.

**Speaker Notes:**  
This is why production uses STIX instead of a slide. Name the wrapper here. Leave TAXII details for the later slide so the channel and the payload stay distinct.

---

### Slide 4 – Real relationship types
**Title:** Link objects with real types

**indicates** · **based-on** · **targets** · **uses** · **related-to**

A Relationship names how two objects connect.  
Do not invent a `relationship_type`.

**Sighting** is its own object. It is not `sighting-of`.  
It uses `sighting_of_ref`. Optional `where_sighted_refs` is the Identity that saw it.

**Speaker Notes:**  
Walk the five types. Stop on Sighting so they do not mint `sighting-of`. related-to is real and weak. If they ask about custom spec terms, this course still uses only the real types on this slide.

---

### Slide 5 – A12 graph, then validate
**Title:** Retell the scenario. Then validate.

**A12:** Indicator (hash of `invoice.vbs`) **indicates** Attack Pattern T1059.001.  
Sighting of that Indicator on Identity **WS-JLEE**.

That set retells the scenario. It is not a report.

Validate: `type`, `spec_version` `2.1`, `id`, `created`, `modified`.  
A Relationship also needs `relationship_type`, `source_ref`, `target_ref`.  
An unearned Threat Actor fails.

**Speaker Notes:**  
Show this given before TAXII and before the knowledge check. Two real links. Do not add PRD APT. Do not open 2.11. The bundle wrapper is not what you validate; the objects inside it are.

---

### Slide 6 – TAXII is the channel
**Title:** TAXII is the channel

**Share** — publish a valid bundle into a **collection**.  
**Consume** — pull objects from a collection.

This lesson: pull the classroom collection `harbor-cti`.  
Do not stand up a server.

**Speaker Notes:**  
Sharing and consumption are both TAXII. The classroom move is consume. If they say they built a server, send them back to this slide. Emailing a PDF is still not TAXII.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. You should stand up a TAXII server in this lesson. True or false?  
2. Name two real STIX 2.1 relationship types.  
3. Write one STIX-aligned link that ties the `invoice.vbs` hash to **WS-JLEE**.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

A bundle packages the objects. Real relationship types only.  
Sighting is its own object. A classroom object must validate.  
TAXII is consume, not a server you build.

**Next:** **2.11.1** Finished intelligence products

**Speaker Notes:**  
2.11.1 is the narrative product on the same incident. Stay off this graph when you get there. Do not open 2.11 unless it is scheduled.
