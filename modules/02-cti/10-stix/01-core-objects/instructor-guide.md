# Instructor Guide – Module 2.10.1 – Core STIX Objects

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.10.1 B / C / C ; 2.10.1.1 3c / 4c / 4c  
- Hunter: 2.10.1 B / C / C ; 2.10.1.1 2b / 3c / 4c  
- SOC: 2.10.1 A / B / B ; 2.10.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the eleven STIX 2.1 objects this lesson covers, and label them in a classroom report. Do not invent types.

**Context (plain language):**

- What this lesson is for: CTI analysts share threat facts in STIX so another shop can reuse them. Before they write a bundle or a narrative, they have to name what kind of object each fact is. This lesson is that labeling job.
- How it hooks to the lesson before: 2.9.4 closed the platform block (URLScan). This is the start of the STIX unit.
- How it hooks to the lesson after: 2.10.2 is linking objects, creating a valid classroom object, and TAXII consume.
- Why we are doing it this way: name the objects before anyone writes a relationship or stands up TAXII.
- What we are *not* doing in this lesson: authoring a bundle. TAXII server. Actor profile. Hunt-as-input. Finished narrative. No lab.
- Extra step: none.

Use the same names as the student guide: **Indicator**, **Observed Data**, **Malware**, **Attack Pattern**, **Threat Actor**, **Intrusion Set**, **Campaign**, **Course of Action**, **Identity**, **Relationship**, and **Sighting**. **STIX** is the shared language; **2.1** is the spec. The givens use course-fiction names (`invoice.vbs`, **WS-JLEE**, **DYA**, “PRD APT”). Do not turn them into the intro plot.

**Key Teaching Points:**
- Eleven real STIX 2.1 types. Do not invent a twelfth.
- Indicator is a pattern. Observed Data is a raw record. Sighting is the assertion that something was seen.
- Identity (victim) is not Threat Actor. A vendor name is not automatically Threat Actor.

**Common Student Challenges:**
- Call the victim host a Threat Actor. Why: both are names of “who.” Example: labeling **WS-JLEE** as Threat Actor.
- Treat a vendor nickname as a Threat Actor object. Why: the PDF already printed a name. Example: “PRD APT” on a report becomes Threat Actor with no other work.
- Mix Indicator and Observed Data. Why: both can carry a hash. Example: labeling a raw “hash was seen” line as Indicator.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.10.1 – Core STIX objects
- T: 2.10.1.1 – Identify and label common STIX objects in a report

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Label the object, not a bundle |
| Key Concepts            | 12 min    | Eleven names; labeling lines |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: STIX is the shared language. This lesson names the object so sharing does not guess.
- Walk the eleven names. Stop on the three mix-ups: Indicator vs Observed Data, Identity vs Threat Actor, Sighting vs Relationship.
- Walk the given lines from the student guide. The product is the type, not a story of the incident.
- If they invent a type: stay on the eleven. Do not add Tool, Infrastructure, or a shop nickname as a STIX type.
- If they start TAXII or writing relationship types: that is 2.10.2.
- If they write an actor profile: that is 2.11 / 2.1.7. “PRD APT” on a PDF is a vendor label, not a Threat Actor object.
- If they start the DYA / PRD plot: the names are labels in a report. They are not this lesson’s story.

---

## Knowledge Check – Answer Key

1. **You may invent a STIX type if none of these eleven fits. True or false?**  
   **Answer:** False. Use the real STIX 2.1 types this lesson names.  
   **Explanation:** Stay on the eleven. A fact that is not one of them stays unlabeled here. Do not make up a type.

2. **“PRD APT” on a vendor PDF is automatically a Threat Actor object. True or false?**  
   **Answer:** False. That is a vendor label, not proof of a Threat Actor object.  
   **Explanation:** Attribution is 2.1.7. If you do not have a Threat Actor object, leave it empty.

3. **Hash of `invoice.vbs` used as a detection pattern, vs WS-JLEE. Which two objects?**  
   **Answer:** Indicator vs Identity.  
   **Explanation:** A hash used as a pattern is Indicator. The same hash as a raw “this file was seen” line would be Observed Data. **WS-JLEE** is Identity (victim), not Threat Actor.

---

## Additional Instructor Resources

- Next: 2.10.2 STIX in production
