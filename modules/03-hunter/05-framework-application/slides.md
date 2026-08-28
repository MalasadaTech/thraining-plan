# Module 3.5.1 – Using MITRE ATT&CK for Hunt Planning  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 3.5.1 – Using MITRE ATT&CK for Hunt Planning  
**Subtitle:** Map this hunt, name the gap, support priority  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson maps a hunt onto ATT&CK so hunters can see holes and rank work. It is not labeling one alert, and it is not putting IDs on a CTI product.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Hunters look for activity the alerts **missed**.

They need a shared name for the **method** they will hunt, or already found.

Putting **this hunt** on ATT&CK shows whether you can see it, whether a detection covers it, and whether it is worth doing now.

**Speaker Notes:**  
This slide is the student intro. The job is map this hunt, name the gap, and use the map to support priority. Do not start with the Enterprise matrix.

---

### Slide 3 – Map this hunt
**Title:** Map this hunt

Write the method as a **tactic** (why) and a **technique** or **sub-technique** (how).

A copied report ID is not a hunt map.

Do not color every Navigator cell (the heatmap view) because a group was named.  
Do not invent an ID so the card looks complete.

**Speaker Notes:**  
Map means this hunt’s method, or this hunt’s finding. If they shade every Persistence cell, pull them back to this hunt. If they invent an ID, they name the method or say unknown.

---

### Slide 4 – Detection gap vs visibility gap
**Title:** Detection gap vs visibility gap

**Detection gap** — telemetry exists; no detection covers that technique in this scope.

**Visibility gap** — you cannot see the technique here. Name it. Do not hunt it as written.

That read of the map is **coverage analysis**.

**Speaker Notes:**  
Two holes, two products. The next slide uses the same map to support priority. Do not let them hunt a class they cannot see.

---

### Slide 5 – ATT&CK supports priority
**Title:** ATT&CK supports priority

ATT&CK **supports** priority. It does not replace scope, freshness, or an open incident.

**A12 given:** HKCU Run **`Updater`** → **TA0003** / **T1547.001**.  
Registry logs exist; no detection on `Updater` → **detection gap**.  
Priority is the open incident plus a download with no alert — not “Persistence first.”

**Speaker Notes:**  
Walk the given before the knowledge check. The map is T1547.001, not the Persistence column. Do not teach how the Run key works on disk; that is the next lesson.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Copying T1547.001 from a report is the same as mapping this hunt. True or false?  
2. What is the difference between a detection gap and a visibility gap?  
3. Map the A12 Run-**`Updater`** hunt. If registry logs exist and no detection fires on that value name, which gap is it?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Map this hunt.  
Name the gap.  
ATT&CK supports priority; it does not replace it.

**Speaker Notes:**  
Persistence recognition is next. That lesson is the mechanism in the log, not another ATT&CK map.

---

### Slide 8 – Next
**Title:** Next

**3.6.1** Persistence techniques

**Speaker Notes:**  
3.6.1 is how persistence looks in a log. Stay off remapping the hunt when you get there.
