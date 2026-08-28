# Module 3.4.1 – Assessing CTI for Hunting Value  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.4.1 – Assessing CTI for Hunting Value  
**Subtitle:** Label the report before you hunt  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
3.3.1 turned an external finding into a precise query. This lesson is the hunter’s first read of a CTI report: decide whether a hunt starts. Do not extract leads today.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

A CTI report usually names an actor, a method, or indicators.

Before you hunt from it, know whether it is worth a hunt at all.

Hunters do **not** hunt every report.

**Speaker Notes:**  
This slide is the student intro. Label first so you do not hunt awareness-only reports, and so you do not take work detections or IR already own. Extracting leads waits for 3.4.2.

---

### Slide 3 – Three labels
**Title:** Hunt-worthy, awareness-only, hand-off

**Hunt-worthy** — question, telemetry, and a bound scope. Task product: **hunt**.  
**Awareness-only** — useful context. No hunt from this report. Task product: **don’t hunt**.  
**Hand-off** — detections or IR already own it. Task product: **hand off**.

**Speaker Notes:**  
Write the three labels, then the three task words. Students mix “interesting” with hunt-worthy. Keep the product to a label and why.

---

### Slide 4 – Actionable for a hunt
**Title:** Question, telemetry, scope

**Actionable for a hunt** means you can name three things:

A **question** the hunt would answer.  
**Telemetry** that could answer it here.  
A bound **scope**.

“Interesting” is not a hunt.

**Speaker Notes:**  
CTI’s own actionable test is 2.1.5 — a who and a next step. This lesson is the hunter’s test: can you hunt from the report. Do not extract the objects yet.

---

### Slide 5 – Label it and say why
**Title:** Rapid triage

Rapid triage is a **label and one sentence why**.

**Hunt-worthy** — `GET /update.exe` to `:8080` and Run **`Updater`**; logs exist; no detection; no open IR.  
**Awareness-only** — “This APT exists.”  
**Hand-off** — IR already has the same `update.exe` hash.

**Speaker Notes:**  
Walk the three givens before the knowledge check. One sentence each. Do not copy ATT&CK IDs. Do not invent a hunt ticket.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. An interesting actor profile is a hunt. True or false?  
2. What three things must you name before a report is actionable for a hunt?  
3. Label this report and say why: `GET /update.exe` to `:8080`, HKCU Run **`Updater`**, registry and HTTP logs exist, no detection on that path, no open IR.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Hunt, don’t hunt, or hand off — plus why.  
Actionable for a hunt is question, telemetry, and scope.  
Interesting is not a hunt.

**Next:** **3.4.2** Extracting hunt leads from CTI

**Speaker Notes:**  
3.4.2 pulls leads from reports that passed this gate. Stay on the label until that lesson.
