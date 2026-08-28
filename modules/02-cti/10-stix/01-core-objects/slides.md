# Module 2.10.1 – Core STIX Objects  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.10.1 – Core STIX Objects  
**Subtitle:** Label the STIX 2.1 object  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson names the eleven STIX 2.1 objects and labels them in a report. It does not teach how to write a bundle or stand up TAXII.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts share threat facts in **STIX** so another shop can reuse them.

Before you write a bundle or a narrative, name **what kind of object** each fact is.

This lesson is **identify**. Not a narrative product. Not a TAXII server.

**Speaker Notes:**  
This slide is the student intro. Hunt reads STIX later (3.4.3). Finished narrative is 2.11. Linking and TAXII are 2.10.2. Stay on labeling.

---

### Slide 3 – Indicator, Observed Data, Malware
**Title:** Indicator, Observed Data, Malware

**Indicator** — a pattern used to detect activity.  
**Observed Data** — a raw record of what was seen. Not a judgment.  
**Malware** — malicious code (family or instance). Not the hash pattern.

A hash can be Indicator or Observed Data. It depends on whether the report gives a pattern or a record.

**Speaker Notes:**  
Walk the first three names. The mix-up is the hash: pattern to find it again is Indicator; “this file was seen” is Observed Data.

---

### Slide 4 – Attack Pattern, Threat Actor, Intrusion Set, Campaign
**Title:** Attack Pattern, Threat Actor, Intrusion Set, Campaign

**Attack Pattern** — a way the adversary works (T1059.001).  
**Threat Actor** — who is believed to operate with malicious intent.  
**Intrusion Set** — grouped behaviors believed to be one actor’s set.  
**Campaign** — a time-bounded set of activity against targets.

A vendor name on a PDF is not automatically Threat Actor.

**Speaker Notes:**  
These four are easy to collapse. Keep them separate. “PRD APT” on a PDF is a vendor label. Attribution is 2.1.7.

---

### Slide 5 – Course of Action, Identity, Relationship, Sighting
**Title:** Course of Action, Identity, Relationship, Sighting

**Course of Action** — a recommended action to prevent or respond.  
**Identity** — a person, org, or system. The victim is Identity, not Threat Actor.  
**Relationship** — a typed link between two objects.  
**Sighting** — an assertion that an object was seen, often at an Identity.

**Speaker Notes:**  
WS-JLEE and DYA are Identity. A line that ties an Indicator to that host is a Sighting, not a generic Relationship. Relationship types wait for 2.10.2.

---

### Slide 6 – Label the line
**Title:** Label the line

Hash of `invoice.vbs` as a pattern — **Indicator**.  
Encoded PowerShell — **Attack Pattern**.  
**WS-JLEE** — **Identity**.  
“PRD APT” — **not** automatically Threat Actor.  
“We saw that hash on WS-JLEE” — **Sighting**.

Name the object. Do not invent a type.

**Speaker Notes:**  
These are the student-guide givens. The product is the type, not the A12 plot. If they start TAXII or writing links, that is 2.10.2.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. You may invent a STIX type if none of these eleven fits. True or false?  
2. “PRD APT” on a vendor PDF is automatically a Threat Actor object. True or false?  
3. Hash of `invoice.vbs` used as a detection pattern, vs **WS-JLEE**. Which two objects?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Eleven real STIX 2.1 types. Label the object.  
A hash pattern is Indicator. A raw observation is Observed Data.  
A victim host is Identity. A vendor name is not automatically Threat Actor.

**Next:** **2.10.2** STIX in production

**Speaker Notes:**  
2.10.2 is links, a valid classroom object, and TAXII consume. Do not open it unless scheduled.
