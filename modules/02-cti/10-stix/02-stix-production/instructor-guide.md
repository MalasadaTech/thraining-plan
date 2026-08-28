# Instructor Guide – Module 2.10.2 – How STIX Objects Are Used in Intelligence Production

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.10.2 B / C / C ; 2.10.2.1 3c / 4c / 4d ; 2.10.2.2 3c / 4c / 4d ; 2.10.2.3 3c / 4c / 4c  
- Hunter: 2.10.2 B / C / C ; 2.10.2.1 2b / 3c / 4c ; 2.10.2.2 2b / 3c / 4c ; 2.10.2.3 2b / 3c / 4c  
- SOC: 2.10.2 A / B / B ; 2.10.2.1 1a / 1a / 2b ; 2.10.2.2 1a / 1a / 2b ; 2.10.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Link named STIX objects with real relationship types, check a classroom object is valid STIX 2.1, and consume a TAXII collection. Do not stand up a server.

**Context (plain language):**

- What this lesson is for: CTI analysts package threat activity so other people and other tools can reuse the same story. They connect the objects they already named, check those objects are valid STIX 2.1, and share or pull that package so a TIP, a hunt, or another shop can ingest the graph without reading a PDF.
- How it hooks to the lesson before: 2.10.1 named the common STIX 2.1 object types. This lesson is how those objects are linked, validated, and moved.
- How it hooks to the lesson after: 2.11.1 is the finished narrative product. The graph is not that paper.
- Why we are doing it this way: name the objects first, then teach the production step — structure, links, validate, TAXII consume — without a live server or a lab.
- What we are *not* doing in this lesson: invented types. Finished narrative (2.11). TIP search (2.3.1). Hunt reading STIX as input (3.4.3). Standing up a TAXII server. No lab.
- Extra step: none.

Use the same names as the student guide: **bundle**, **payload**, **channel**, **relationship_type**, **Sighting**, `sighting_of_ref`, `where_sighted_refs`, **collection**, **TAXII**, and **validate**. `harbor-cti` is the classroom collection name, not a live org server. **A12**, **WS-JLEE**, and Temp `invoice.vbs` are the course-fiction given. Do not turn them into the intro plot.

**Key Teaching Points:**
- The bundle is the payload. TAXII is the channel. A PDF is neither.
- Real `relationship_type` values only. Sighting is its own object, not `sighting-of`.
- A classroom object must validate. An unearned Threat Actor fails.
- Consume the classroom collection. Do not run the server.

**Common Student Challenges:**
- Invent a relationship type. Why: shops sometimes mint local verbs, and the spec allows custom terms; this course does not. Example: writing `sighting-of` or `seen-on` as `relationship_type`.
- Treat TAXII as a server you build. Why: TAXII is a channel to a named collection. Example: “I stood up TAXII” instead of “I would pull collection `harbor-cti`.”
- Add a Threat Actor to make the graph look complete. Why: a vendor name on a PDF is a label, not an earned object. Example: Threat Actor “PRD APT” with no evidence.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.10.2 – How STIX objects are used in intelligence production
- T: 2.10.2.1 – Create STIX-aligned relationships and explain a threat scenario
- T: 2.10.2.2 – Create and validate STIX objects
- T: 2.10.2.3 – Use TAXII for sharing and consumption of intelligence

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Package the story; no server |
| Key Concepts            | 12 min    | Bundle, links, A12 graph, validate, TAXII |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a hash in a slide is not reusable. Connect the objects, validate them, and move the package.
- Draw the split: bundle is the payload, TAXII is the channel, a PDF is a human story. Stop there. Do not teach TIP screens.
- Walk the relationship table. Stop on Sighting: it is its own object with `sighting_of_ref`, not a `relationship_type` called `sighting-of`.
- Walk the A12 given from the student guide. The product is two real links that retell the scenario, not a 2.11 paper.
- Validate on the same objects: `type`, `spec_version` `2.1`, `id`, `created`, `modified`. A Relationship also needs `relationship_type`, `source_ref`, and `target_ref`.
- If they invent a type: use the table. Do not allow custom verbs in this course.
- If they add Threat Actor “PRD APT”: that is unearned. Identity **WS-JLEE** is the victim host, not an actor.
- If they say they stood up TAXII: consume collection `harbor-cti`. Sharing means publish into a collection. This lesson’s classroom move is pull. No server.

---

## Knowledge Check – Answer Key

1. **You should stand up a TAXII server in this lesson. True or false?**  
   **Answer:** False. Consume a collection.  
   **Explanation:** TAXII is the channel. The classroom move is pull `harbor-cti`. You do not run the server.

2. **Name two real STIX 2.1 relationship types.**  
   **Answer:** Any two of: `indicates`, `based-on`, `targets`, `uses`, `related-to`.  
   **Explanation:** Those are specification-defined types this lesson uses. `sighting-of` is not one of them.

3. **Write one STIX-aligned link that ties the `invoice.vbs` hash to WS-JLEE.**  
   **Answer:** A Sighting of the Indicator (hash of `invoice.vbs`), `where_sighted_refs` Identity **WS-JLEE**.  
   **Explanation:** Sighting is the object that says we saw that Indicator on that host. `indicates` is Indicator → Attack Pattern or Malware, not host. Do not write `relationship_type` `sighting-of`.

---

## Additional Instructor Resources

- Next: 2.11.1 Finished intelligence products
