# Module 3.3.1 – Internal Threat Intelligence Platform  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.3.1 – Internal TIP  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Search, retrieve, link. Overlay live TIP if you have it.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Purpose and core functions
2. Navigate and search
3. Retrieve a relevant object
4. Enrich or analyze (sighting / link)

**Mapped Items:**  
K: 3.3.1 | T: 3.3.1.1

**Speaker Notes:**  
SOC 3-level task is 1a / 2b. CTI is 3c / 4d.

---

### Slide 3 – Agenda
**Title:** Agenda

- Harbor TIP card
- Three examples
- Retrieve + enrich
- Knowledge check

**Speaker Notes:**  
3.3.2 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

VT / AnyRun / Silent Push / URLScan (**3.3.2**)  
VT Relations depth (**3.9**)  
STIX authoring (**3.10**)  
Ticket worklog (**1.8.4**)

**Key Point:** Our store. Search and attach.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Purpose
**Title:** What the TIP Is For

Store indicators, reports, sightings, clusters.  
Answer: **have we already seen this?**

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Search
**Title:** Navigate

Search: IOC, tag, cluster.  
Filter: type, date, TLP, source.  
Open the object = retrieve.

**Speaker Notes:**  
Outline b. 403 → 1.8.3.

---

### Slide 7 – Three Uses
**Title:** Enrich · Analyze · Produce

**Enrich** — add sighting / link related IOC  
**Analyze** — read prior Harbor hits  
**Produce** — attach object ID to the draft

**Speaker Notes:**  
Outline c.

---

### Slide 8 – Two Lines
**Title:** Retrieve vs Enrich

`query | object | fields`  
`object | what you add | why`

Opening the page is only the first line.

**Speaker Notes:**  
Tasks.

---

### Slide 9 – Example 1: Retrieve
**Title:** Example 1 – SNI Search

`nightowl-updates.net` → IND-1882  
Two old sightings. No WS-JLEE yet.

**Speaker Notes:**  
Students first. Demo if you can.

---

### Slide 10 – Example 2: VT
**Title:** Example 2 – Wrong Store

VT is **3.3.2**.  
Internal question still unanswered.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: No Sighting
**Title:** Example 3 – Read-Only Fail

Opened IND-1882. Never added WS-JLEE.  
Task 2 failed.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- VT as TIP  
- Search without opening  
- No new sighting  
- Tenant-wide dump  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use the live TIP if posted.  
Keep: search / open / attach.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–B: retrieve line.
3. C–D: enrich / pull line.
4. No VT.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. TIP vs SIEM vs VT?
2. Three functions?
3. Retrieve vs enrich?
4. Why not a VT tab?
5. Notes vs TIP?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Search. Open. Link the new hit.
- Next: **3.3.2** external tools.

**Speaker Notes:**  
Do not open 3.3.2 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Harbor TIP — Quick Reference

| Need | Do |
|------|-----|
| Have we seen it? | Search + open |
| New host hit | Add sighting |
| Related hash | Link indicator |
| Draft for SOC | Pull prior hits + TLP |

URL: `tip.harbor.internal` (classroom)

**Coming next:** Module 3.3.2 – External tools

**Footer:** SOC / Hunter / CTI Training Program
