# Module 2.3.1 – Internal Threat Intelligence Platform  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.3.1 – Internal Threat Intelligence Platform  
**Subtitle:** What this organization already knows  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is the internal store. It is not VirusTotal and not a shop product URL. Tradecraft closed in the lesson before this. Similarity hashes are next.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts look up **what this organization already knows**.

That store is the internal **TIP**. Search it before you treat a public lookup as new.

This lesson is that store: purpose, search, and how it supports the work.

**Speaker Notes:**  
This slide is the student intro. Name why they search internals before anyone opens a public tool. Do not teach 0.7 here.

---

### Slide 3 – Store, search, link
**Title:** Store, search, link

**Store** — indicators, reports, and sightings we already have.  
**Search / retrieve** — what we already know about a hash, IP, domain, or report.  
**Link** — attach this observation to an existing object when one is there.

The product name on the screen may differ. The jobs do not.

**Speaker Notes:**  
These are the core functions. A sighting is a record that we saw the indicator. Stop before VirusTotal. If a live classroom TIP is up, overlay it as these same three jobs.

---

### Slide 4 – How to search
**Title:** How to search

You already have a value.

**Match the type** — hash in a hash search, domain in a domain search.  
**Open the result** — read what is already recorded.  
**Empty is a result** — write **not in TIP**. Do not invent a hit.

A search in the wrong field is not a miss.

**Speaker Notes:**  
This is navigation without a vendor walkthrough. Type-matched search is the skill. An empty result is still a retrieve: not in TIP.

---

### Slide 5 – Enrich, analyze, produce
**Title:** Enrich, analyze, produce

**Enrich** — prior notes and related objects we already hold.  
**Analyze** — what we hold versus a public lookup. A miss is a gap, not benign.  
**Produce** — cite the object you retrieved, or cite the miss.

**Given:** a domain or file hash you already have.  
Write what you retrieved, or **not in TIP**. If an object exists, attach this observation. Do not invent a hit.

**Speaker Notes:**  
Show this given before the knowledge check. The product is the object you retrieved or not in TIP. Then you link the observation or cite the gap. Public tools are 0.7. STIX authoring is 2.10. Pivot depth is 2.9.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. The internal TIP is the same as VirusTotal. True or false?  
2. Name two core TIP functions.  
3. You search a domain you already have. What two results can you write, and what must you not invent?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

The TIP is our store.  
Search the matching type. Retrieve or write **not in TIP**.  
A miss is a gap, not benign. Do not invent a hit.

**Speaker Notes:**  
Similarity hashes are next. That lesson is cousins of a file, not TIP navigation.

---

### Slide 8 – Next
**Title:** Next

**2.4.1** File similarity hashes

**Speaker Notes:**  
2.4.1 is imphash, ssdeep, TLSH, and code-signing. Stay off the TIP when you get there.
