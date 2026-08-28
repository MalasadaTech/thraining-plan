# Instructor Guide – Module 2.3.1 – Internal Threat Intelligence Platform

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.3.1 B / C / C ; 2.3.1.1 3c / 4c / 4d  
- Hunter: 2.3.1 A / B / B ; 2.3.1.1 1a / 2b / 3c  
- SOC: 2.3.1 A / A / B ; 2.3.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the internal threat intelligence platform as this organization's store, then search it, retrieve what it holds or write that it does not, and use that result to support enrichment or analysis.

**Context (plain language):**

- What this lesson is for: CTI analysts look up what this organization already knows about a hash, IP, domain, or report before they treat a public lookup as new. That store is the internal TIP.
- How it hooks to the lesson before: 2.2.4 closed tradecraft (bias). This lesson is the store.
- How it hooks to the lesson after: 2.4.1 is similarity hashes, not TIP navigation.
- Why we are doing it this way: the public tool survey already lives in 0.7. This lesson stays on purpose, search, and use of the internal store.
- What we are *not* doing in this lesson: VirusTotal, Silent Push, or other 0.7 tools as the subject. Platform depth / pivot (2.9). STIX authoring (2.10). Invented product names or tickets. No lab.
- Extra step: none.

Use the same names as the student guide: **TIP**, **store**, **search / retrieve**, **link**, **sighting**, and **not in TIP**. Classroom product names are stand-ins. If a live classroom TIP is available, overlay those screens as the same three jobs. Do not treat a classroom URL as shop policy.

**Key Teaching Points:**
- The TIP is our store, not a public lookup.
- Store, search/retrieve, and link.
- Search the matching type. Retrieve the object or write **not in TIP**.
- A miss is a gap, not benign. Do not invent a hit.

**Common Student Challenges:**
- Treat the TIP as VirusTotal. Why: both look up a hash or domain. Example: pasting the hash into VirusTotal first and calling that the internal check.
- Invent a hit when the search is empty. Why: an empty result feels like the task failed. Example: writing an actor name that is not in the object.
- Call a miss benign. Why: nothing in the store is taken as already cleared. Example: “not in TIP, so the domain is clean.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.3.1 – Internal threat intelligence platform
- T: 2.3.1.1 – Search, retrieve, and use the internal TIP for enrichment or analysis

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Our store, not a public tool |
| Key Concepts            | 12 min    | Functions; type-matched search; retrieve or miss |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: look up what we already know before a public tool.
- Write store, search/retrieve, and link. Stop. Do not open VirusTotal.
- Walk type-matched search. A hash goes in a hash search. A domain goes in a domain search. An empty result is **not in TIP**. A search in the wrong field is not a miss.
- Walk the given: a domain or file hash you already have. The product is the object you retrieved or **not in TIP**. If an object exists, link this observation and cite it. If not, say the TIP added nothing.
- If they open VirusTotal: that is 0.7. This lesson is our store.
- If they write a STIX bundle: that is 2.10.
- If they invent a product URL or ticket name: classroom names are stand-ins, not shop policy.

---

## Knowledge Check – Answer Key

1. **The internal TIP is the same as VirusTotal. True or false?**  
   **Answer:** False. The TIP is this organization's store. VirusTotal is a public lookup.  
   **Explanation:** Public tools are 0.7. This lesson is whether we already hold something.

2. **Name two core TIP functions.**  
   **Answer:** Any two of store, search/retrieve, and link.  
   **Explanation:** Those are the jobs of the internal platform. The product name on the screen may differ.

3. **You search a domain you already have. What two results can you write, and what must you not invent?**  
   **Answer:** A prior object you retrieved, or **not in TIP**. Do not invent a hit.  
   **Explanation:** A miss is a gap, not benign. Inventing a hit is not retrieval.

---

## Additional Instructor Resources

- Next: 2.4.1 File similarity hashes
