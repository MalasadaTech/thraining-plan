# Instructor Guide – Module 3.4.3 – STIX as Hunt Input

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.3 B / C / C ; 3.4.3.1 3c / 4c / 4c ; 3.4.3.2 3c / 4c / 4d  
- SOC: 3.4.3 A / A / B ; 3.4.3.1 1a / 1a / 2b ; 3.4.3.2 1a / 1a / 2b  
- CTI: 3.4.3 A / B / B ; 3.4.3.1 1a / 2b / 3c ; 3.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Identify hunt-relevant STIX objects in a report or bundle and seed a hunt lead. Do not author STIX.

**Context (plain language):**

- What this lesson is for: Hunters read CTI that arrives as a report or a STIX bundle. Structured JSON is not automatically a hunt. This lesson names the objects a hunter actually uses, then turns those objects into a hunt question that can fail.
- How it hooks to the lesson before: 3.4.2 extracted hunt leads from prose. This lesson is the same job when the facts arrive as STIX objects.
- How it hooks to the lesson after: 3.5.1 maps this hunt onto ATT&CK.
- Why we are doing it this way: hunters consume STIX; authoring, validating, and TAXII already live in 2.10. Stay on identify, then seed.
- What we are *not* doing in this lesson: author, validate, or share STIX (2.10). Standing up a TAXII server. Navigator. Extract-from-prose keep/drop as a second lesson. No lab.
- Extra step: none.

Use the same names as the student guide: **indicator**, **attack-pattern**, **observed-data**, **malware**, **threat-actor** / **intrusion-set**, and **relationship**. **STIX** is the shared language; **2.1** is the spec; a **bundle** is the wrapper. **Seed** means the bundle is starting input for a hunt question, not the hunt itself. The given uses course-fiction names (A12, `203.0.113.88:8080`, Run **`Updater`**). Do not turn it into the intro plot.

**Key Teaching Points:**
- Six objects a hunter uses. An actor name is not a search.
- A bundle seeds a hunt only when objects become a question that can fail. Structured JSON is not automatically a hunt.

**Common Student Challenges:**
- Treat the threat-actor name as a search. Why: it looks like the most important object in the bundle. Example: querying the vendor nickname instead of the Run value or the URI.
- Dump every IPv4 indicator. Why: the bundle already labeled them `indicator`. Example: loading every IPv4 pattern into a block list and calling that a hunt.
- Start authoring or validating STIX. Why: they already sat 2.10. Example: writing `spec_version` or standing up TAXII.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.4.3 – STIX as hunt input
- T: 3.4.3.1 – Identify hunt-relevant objects in a report or bundle
- T: 3.4.3.2 – Turn those objects into hunt leads

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Read the bundle. Do not author |
| Key Concepts            | 12 min    | Six objects; A12 identify and seed |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: CTI arrives as a report or a STIX bundle. Structured JSON is not automatically a hunt. Name the objects that can drive a search, then seed a question that can fail.
- Write the six objects. Stop on threat-actor / intrusion-set: scope or priority, not a query.
- Campaign, course-of-action, identity, and sighting may appear. They are not the hunter list this lesson asks for. Do not walk the rest of 2.10.
- Walk the A12 given: `indicator` for `GET /update.exe` to `203.0.113.88:8080`; `attack-pattern` for HKCU Run **`Updater`**; `relationship` `uses`. Product is the object names plus the question, not a new STIX graph.
- If they invent a STIX type: stay on real STIX 2.1 types. Do not add a shop nickname as a type.
- If they dump every IPv4 indicator: that is a block-list hand-off, not a seed.
- If they start authoring, validating, or TAXII: that is 2.10. Today is read, not write.
- If they open Navigator or map coverage: that is 3.5.

---

## Knowledge Check – Answer Key

1. **Hunters author STIX in this lesson. True or false?**  
   **Answer:** False. Authoring is 2.10.  
   **Explanation:** This lesson is identify and seed. Hunters read a report or bundle. They do not write STIX here.

2. **Name four objects a hunter actually uses.**  
   **Answer:** Any four of: indicator, attack-pattern, observed-data, malware, threat-actor / intrusion-set, relationship.  
   **Explanation:** Those six are the hunter list. Campaign, course-of-action, identity, and sighting may appear; they are not the list this lesson asks for.

3. **A classroom bundle has an `indicator` for `GET /update.exe` on `203.0.113.88:8080` and an `attack-pattern` for HKCU Run `Updater`. Name one hunt-relevant object and the lead it seeds.**  
   **Answer:** Either object is enough. Example: `indicator` for `/update.exe` on `:8080` → search that IP + port + URI. Or Run **`Updater`** `attack-pattern` → search that value.  
   **Explanation:** Identify names the object. Seed is the question those objects can fail: if more persistors exist, we see that Run value or that URI. Dumping every IPv4 indicator is not a seed.

---

## Additional Instructor Resources

- Next: 3.5.1 ATT&CK for hunt planning
