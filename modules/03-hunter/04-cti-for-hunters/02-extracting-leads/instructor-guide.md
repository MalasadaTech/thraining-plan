# Instructor Guide – Module 3.4.2 – Extracting Hunt Leads from CTI

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.2 B / C / C ; 3.4.2.1–3.4.2.3 3c / 4c / 4d  
- SOC: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
- CTI: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Keep searchable TTPs and artifacts. Drop what you cannot hunt. State one hunt question those leftovers support.

**Context (plain language):**

- What this lesson is for: After a report is already worth hunting, hunters pull only the methods and objects they can search internally, drop the rest, and write one hunt question those leftovers can answer.
- How it hooks to the lesson before: 3.4.1 decides hunt, don’t hunt, or hand off. This lesson extracts from reports that passed that decision.
- How it hooks to the lesson after: 3.4.3 reads the same leftovers in STIX. It does not change the keep / drop rules.
- Why we are doing it this way: copying an appendix hunts slogans, expired hashes, and whole address blocks. Extract is a keep list plus a question that can come back empty.
- What we are *not* doing in this lesson: ATT&CK Navigator (3.5). Inventing ATT&CK IDs the report never printed. Authoring STIX (2.10 / 3.4.3). The full four-field hunt card (3.2.2). The course-fiction plot (DYA / PRD). No lab.
- Extra step: none.

Use the same names as the student guide: **TTP**, **IOC**, **behavior**, **telemetry**, **visibility gap**, **hunt question**, and **leftovers** (the keep list after drop). **A12** is the classroom report slice in the student guide, not a live actor. HKCU Run **`Updater`** is the unique pattern; do not widen it to “any Run key.”

**Key Teaching Points:**
- TTP, IOC, and behavior can each drive a hunt only when they are searchable here.
- Appendix dump is not extract.
- Record printed ATT&CK IDs. Do not invent them. Mapping is 3.5.
- The hunt question must be able to come back empty.

**Common Student Challenges:**
- Treat the IOC appendix as the extract. Why: the appendix looks like a product. Example: pasting every hash into hunt notes.
- Invent an ATT&CK ID the report never printed. Why: they already know the persistence technique from later mapping. Example: writing **T1547.001** when the page only said HKCU Run **`Updater`**.
- Write the full hunt card. Why: 3.2.2 taught four fields. Example: adding a 14-day workstation scope when this lesson only needs the question.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.4.2 – Extracting hunt leads from CTI
- T: 3.4.2.1 – Extract hunt-suitable TTPs from a CTI report
- T: 3.4.2.2 – Extract hunt-suitable artifacts (IOCs, patterns, behaviors)
- T: 3.4.2.3 – State the hunt question those leads support

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Keep / drop / question, after the hunt decision |
| Key Concepts            | 12 min    | Three kinds; drop list; A12 keep and question |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: after a report is worth hunting, pull only what you can search here, then write one question those leftovers can answer.
- Walk TTP, IOC, and behavior. Keep means it can drive a hunt — specific enough, and you have telemetry.
- Walk the drop list. No telemetry is a named visibility gap, not a keep. Expired means stale or unused. Noise includes slogan TTPs, a whole `/24`, and already-blocked volume.
- Record ATT&CK IDs only if the report printed them. Do not open Navigator. Mapping this hunt is 3.5.
- Walk the A12 slice from the student guide. The product is keep TTP, keep artifacts, drop lines, and one question. Do not tell the intro plot.
- If they invent **T1547.001** the report never printed: record only what is given. Mapping is 3.5.
- If they write the four-field card: that format is 3.2.2. Today is the question the leftovers support.
- If they start authoring STIX: that is 2.10. Reading a bundle is 3.4.3.

---

## Knowledge Check – Answer Key

1. **Copying the IOC appendix is extract. True or false?**  
   **Answer:** False. Extract is a keep list you can search, not the appendix dump.  
   **Explanation:** A hash list with no keep / drop decision is not hunt-suitable TTPs or artifacts.

2. **Name one reason to drop an object.**  
   **Answer:** No telemetry, an expired IOC, or noise (any one).  
   **Explanation:** No telemetry is a visibility gap you name. Expired is stale or unused. Noise is a slogan TTP, a whole `/24`, or already-blocked volume.

3. **From the A12 slice, name one keep TTP, one keep artifact, and the hunt question.**  
   **Answer:** TTP: HKCU Run **`Updater`** → `%TEMP%\update.exe`. Artifact: `GET /update.exe` to `203.0.113.88:8080`, or more `invoice.vbs`. Question: if more A12 persistors exist, we see Run **`Updater`**, `update.exe`, or another `invoice.vbs`.  
   **Explanation:** Drop “they use persistence” and the whole `203.0.113.0/24`. The question must be able to come back empty.

---

## Additional Instructor Resources

- Next: 3.4.3 STIX as hunt input
