# Module 2.4.1 – Internal Threat Intelligence Platform  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.4.1 – Internal Threat Intelligence Platform  
**Subtitle:** Reuse what the organization already knows  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Introduce the TIP as the organization's intelligence workspace. The skill is not memorizing a product interface; it is retrieving and evaluating existing context so it can support the current analysis.

---

### Slide 2 – Why the TIP matters
**Title:** Before starting over, check what is already known

A TIP helps analysts recover prior:

- reporting;
- indicators;
- relationships;
- observations or sightings; and
- analyst context.

That can reduce duplicated work and reveal organizational knowledge that would otherwise be missed.

**Speaker Notes:**  
Ask learners what could be lost if every analyst starts with a fresh public lookup. Then remind them that finding prior context does not automatically settle the current case.

---

### Slide 3 – What “internal” means
**Title:** Internal platform ≠ internally sourced only

The TIP is the organization's intelligence workspace.

It may contain:

- internally produced intelligence;
- commercial reporting;
- open-source reporting; and
- imported or analyst-created objects.

The question is: **what has our organization already recorded?**

**Speaker Notes:**  
Connect this to 2.1.9. Source class and repository location are different concepts.

---

### Slide 4 – Core functions
**Title:** Store, search, relate, use

**Store** — preserve intelligence objects and context.  
**Search / retrieve** — recover what is already recorded.  
**Relate** — connect objects or observations when evidence supports the relationship.  
**Use** — incorporate supported context into enrichment, analysis, or production.

**Speaker Notes:**  
If demonstrating a live classroom TIP, map interface features back to these functions rather than turning the lesson into a vendor-specific tour.

---

### Slide 5 – Search the object you actually have
**Title:** A miss is meaningful only after a valid search

If you have a **domain**, search the domain object or correct field.  
If you have a **file hash**, search the appropriate hash or file object.

Then inspect the result:

- source / provenance;
- dates;
- linked reports;
- sightings or observations; and
- supported relationships.

**Speaker Notes:**  
A search in the wrong field can create a false miss. The learner should understand both search discipline and retrieval.

---

### Slide 6 – A hit adds context, not automatic proof
**Title:** Read what the object actually supports

Suppose the A12 update domain already exists in the TIP.

That may add prior reporting, infrastructure context, or an earlier observation.

It does **not** automatically prove that:
- the same relationship applies to A12;
- an old relationship is still current; or
- every attribution attached to the object applies now.

**Speaker Notes:**  
The TIP contributes evidence and context. The analyst still evaluates relevance to the current requirement.

---

### Slide 7 – A miss is not benign
**Title:** “Not found in TIP” has a narrow meaning

A valid search returns no matching object.

That means the TIP did not return a match.

It does **not** mean:
- benign;
- unseen everywhere internally; or
- new to the internet.

The result may identify a gap that requires another source or collection path.

**Speaker Notes:**  
Tie this back to the collection-source lesson. The next step depends on the requirement.

---

### Slide 8 – Follow one A12 lookup
**Title:** Search → retrieve → evaluate → use

1. Search the update domain using the correct object type.  
2. Retrieve the matching object, if one exists.  
3. Evaluate provenance, age, relationships, and observations.  
4. Use supported context in the A12 analysis.  
5. Record a new relationship or observation only when the evidence supports it.

**Speaker Notes:**  
This is the complete workflow for the lesson. The key is disciplined use of stored context, not the number of clicks.

---

### Slide 9 – Knowledge Check and Summary
**Title:** What does the TIP result actually tell you?

1. An older TIP object links the A12 domain to prior activity. What should you verify before applying that context now?  
2. The correct domain search returns no match. What does that mean—and what does it not mean?  
3. A current file hash matches a TIP object with notes and a sighting. How can that help without deciding the current case for you?

**Remember:** the TIP tells you what the organization has recorded. Analysis determines what that context means for the current question.


**Speaker Notes:**  
Use the instructor answer key. Listen for provenance, relevance, and appropriate interpretation of both hits and misses.

**Next:** [2.4.2 – Selecting Platforms for CTI Work](../02-platform-selection/student-guide.md).
