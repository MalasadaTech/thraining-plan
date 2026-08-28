# Instructor Guide – Module 3.5.1 – Using MITRE ATT&CK for Hunt Planning

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 3c / 4c / 4d  
- SOC: 3.5.1 A / B / B ; 3.5.1.1–3.5.1.2 1a / 2b / 3c ; 3.5.1.3 1a / 1a / 2b  
- CTI: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Map this hunt to ATT&CK. Name detection vs visibility gaps. Use that map to support priority.

**Context (plain language):**

- What this lesson is for: Hunters look for activity the alerts missed. Before they search, they need a shared name for the method they will hunt, or for the method they already found. ATT&CK is that name. Putting this hunt on it shows whether you can see that method, whether a detection already covers it, and whether this hunt is worth doing now.
- How it hooks to the lesson before: 3.4.3 turned STIX objects into hunt leads. Those leads still need a hunt map.
- How it hooks to the lesson after: 3.6.1 is how persistence looks in a log — the mechanism, not the ATT&CK map.
- Why we are doing it this way: map this hunt, then name the hole and support priority. Do not re-teach labeling one alert. Do not re-teach putting IDs on a CTI product.
- What we are *not* doing in this lesson: whole-enterprise Navigator layer. Scoring model. How the Run key works on disk (3.6.1). Hunt-card format (3.2.2). No lab.
- Extra step: none.

Use the same names as the student guide: **map**, **tactic**, **technique**, **sub-technique**, **detection gap**, **visibility gap**, and **priority**. **Coverage analysis** is reading that map for holes. **ATT&CK Navigator** is the heatmap view, not a second product. The given uses course-fiction names (A12, HKCU Run **`Updater`**). Do not turn it into the intro plot, and do not teach how the Run key works.

**Key Teaching Points:**
- A copied ID is not a hunt map. Map the method this hunt will search, or the finding it already has.
- A visibility gap is not a hunt as written.
- ATT&CK supports priority. It does not replace scope, freshness, or an open incident.

**Common Student Challenges:**
- Copy a report ID and call it a hunt map. Why: the report already printed the ID. Example: writing T1547.001 on the card because the report listed it, without mapping this hunt’s method.
- Hunt a visibility gap. Why: the technique is on the matrix, so they search it. Example: hunting Run keys on a host class with no registry logging.
- Rank by tactic color. Why: the heatmap looks like priority. Example: “Persistence is always first” while an open incident and a download with no alert sit next to a mapped technique you can see.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.5.1 – Using MITRE ATT&CK for hunt planning and coverage analysis
- T: 3.5.1.1 – Map a hunt plan or hunt findings to MITRE ATT&CK
- T: 3.5.1.2 – Use ATT&CK to identify detection or visibility gaps
- T: 3.5.1.3 – Use ATT&CK to support hunt prioritization

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | This hunt, not the whole matrix |
| Key Concepts            | 12 min    | Map, two gaps, priority, A12 |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: hunters look for missed activity, and they need a shared name for the method before they search.
- Write map: method you will search, or method you found, as tactic plus technique (or sub-technique). Stop. Do not color the whole matrix.
- A report ID is a label from the report. It is not this hunt’s map until you write the method this hunt will search or already found.
- Walk detection vs visibility. If they cannot see the technique in this scope, they name the visibility gap and they do not hunt it as written.
- ATT&CK supports priority. “The tactic is red” is not a reason.
- Walk the given: HKCU Run **`Updater`** → **TA0003** / **T1547.001**. Registry logs exist and no detection on that value name is a detection gap. Priority is the open incident plus the download with no alert, not “Persistence first.”
- If they shade every Persistence cell: this hunt only.
- If they invent an ID: do not. Name the method or say unknown.
- If they start how the Run key works on disk: that is 3.6.1.

---

## Knowledge Check – Answer Key

1. **Copying T1547.001 from a report is the same as mapping this hunt. True or false?**  
   **Answer:** False. Copying a printed ID is a label from the report, not a hunt map.  
   **Explanation:** A hunt map is the method this hunt will search, or the finding this hunt already has, written as a tactic and a technique.

2. **What is the difference between a detection gap and a visibility gap?**  
   **Answer:** Detection gap: you can see the technique; no detection covers it in this scope. Visibility gap: you cannot see the technique here.  
   **Explanation:** Name a visibility gap. Do not hunt it as written.

3. **Map the A12 Run-`Updater` hunt. If registry logs exist and no detection fires on that value name, which gap is it?**  
   **Answer:** **TA0003** Persistence / **T1547.001** Registry Run Keys / Startup Folder. Registry logs exist and no detection on `Updater` is a **detection gap**.  
   **Explanation:** The method is a current-user Run value. Telemetry exists, so this is not a visibility gap.

---

## Additional Instructor Resources

- Next: 3.6.1 Persistence techniques
