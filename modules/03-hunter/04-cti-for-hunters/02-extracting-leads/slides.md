# Module 3.4.2 – Extracting Hunt Leads from CTI  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 3.4.2 – Extracting Hunt Leads from CTI  
**Subtitle:** Keep, drop, then the hunt question  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
3.4.1 decided whether to hunt. This lesson pulls searchable leftovers from a report that already passed that decision. It is not STIX and not ATT&CK mapping.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

A hunter does not paste a CTI report into a search.

Pull only what you can **search here**. Drop the rest. Then write one **hunt question** those leftovers can answer.

This lesson is keep, drop, and the question.

**Speaker Notes:**  
This slide is the student intro. Copying an appendix hunts slogans, expired hashes, and whole address blocks. Name keep / drop before anyone maps ATT&CK or opens STIX.

---

### Slide 3 – TTP, IOC, behavior
**Title:** Which leftovers can drive a hunt

**TTP** — how they work. Keep when it is specific and you have telemetry.  
**IOC** — a named object (hash, host, IP, URL). Keep when it is current, rare, and queryable here.  
**Behavior** — a pattern over time. Keep when it is off-baseline or scoped, not daily admin.

Copying the IOC appendix is not extract.

**Speaker Notes:**  
One line each. Telemetry means logs you can search. If they start listing every vendor ATT&CK ID, that is not a keep list yet.

---

### Slide 4 – What to drop
**Title:** What to drop

**No telemetry** — you cannot see it here. Name that visibility gap.  
**Expired IOC** — stale, or a hash with no reuse note.  
**Noise** — slogan TTP, a whole `/24`, already-blocked volume.

**Speaker Notes:**  
Walk one example each from the student guide. A 2019 hash with no reuse note is expired. “They use persistence” is noise. Do not keep a `/24` because one IP in it was bad.

---

### Slide 5 – ATT&CK IDs if printed
**Title:** Record ATT&CK IDs if the report has them

Copy the ID **only if the report printed it**.

Do not invent an ID.  
Do not open Navigator. Mapping this hunt is **3.5**.

**Speaker Notes:**  
This is outline recording, not coverage analysis. If they write T1547.001 when the page only said Run Updater, send them back to the printed text.

---

### Slide 6 – Keep, drop, then the question
**Title:** A12 slice

**Keep TTP** — HKCU Run **`Updater`** → `%TEMP%\update.exe`.  
**Keep artifacts** — `GET /update.exe` `:8080`; more `invoice.vbs`.  
**Drop** — “they use persistence”; the `203.0.113.0/24`.  
**Question** — if more A12 persistors exist, we see those.

The question must be able to come back empty.

**Speaker Notes:**  
Show this given before the knowledge check. The unique pattern is the value name Updater, not any Run key. Do not write the four-field card and do not tell the intro plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Copying the IOC appendix is extract. True or false?  
2. Name one reason to drop an object.  
3. From the A12 slice: one keep TTP, one keep artifact, and the hunt question.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Keep searchable TTPs and artifacts.  
Drop noise, expired objects, and anything you cannot see.  
One hunt question that can come back empty.

**Next:** **3.4.3** STIX as hunt input

**Speaker Notes:**  
3.4.3 reads the same leftovers in STIX. Keep / drop rules do not change. Do not open STIX unless that lesson is scheduled.
