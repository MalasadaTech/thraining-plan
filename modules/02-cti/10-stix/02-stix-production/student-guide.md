# Module 3.10.2 – STIX in Intelligence Production

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.10.2 A / B / B · 3.10.2.1 1a / 1a / 2b · 3.10.2.2 1a / 1a / 2b · 3.10.2.3 1a / 1a / 2b  
- Hunter: 3.10.2 B / C / C · 3.10.2.1 2b / 3c / 4c · 3.10.2.2 2b / 3c / 4c · 3.10.2.3 2b / 3c / 4c  
- CTI: 3.10.2 B / C / C · 3.10.2.1 3c / 4c / 4d · 3.10.2.2 3c / 4c / 4d · 3.10.2.3 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. **Structure** a small bundle so it can be shared and automated — not a 3.11 narrative.
2. **Link** objects with **real** STIX relationship types and **explain** the scenario.
3. **Create and validate** classroom objects (required fields present; reject invalid fills).
4. Use **TAXII** as the *channel* to publish or consume a bundle.

**Mapped Proficiency Items:**
- K: 3.10.2 – How STIX objects are used in intelligence production
- T: 3.10.2.1 – Create STIX-aligned relationships and explain a threat scenario
- T: 3.10.2.2 – Create and validate STIX objects
- T: 3.10.2.3 – Use TAXII for sharing and consumption of intelligence

---

## 1. Key Concepts

**3.10.1** labeled the types. This hour **produces**: links, valid objects, TAXII. Hunt-lead extract is **2.4.3**. A finished *prose* product is **3.11**. TIP *search* is **3.3.1**.

Use **real** STIX 2.1 `relationship_type` values. Classroom set: `indicates`, `based-on`, `uses`, `attributed-to`, `targets`, `mitigates`. Do not invent `connects-to`.

**Structure for sharing and automation (outline a):** a **bundle** is objects + relationships a machine can ingest. TAXII is *how* the bundle moves (publish / consume a **collection**). Emailing a PDF is not TAXII.

**Linking (outline b) + 3.10.2.1:** every link is  
`source | relationship_type | target`

**Create and validate (3.10.2.2) — classroom required fields (lesson-only, not the full spec):**

| Type | Must have | Invalid if |
|------|-----------|------------|
| **indicator** | `pattern`, `pattern_type` | Empty pattern; type `ioc` |
| **relationship** | `source_ref`, `target_ref`, `relationship_type` | Missing type; invented type |
| **threat-actor** | Evidence of a *who* | Vendor “Night Owl APT” only |
| **sighting** | `sighting_of_ref` | A sighting with no object |

**TAXII (3.10.2.3) — classroom collection `harbor-cti` (lesson-only). Do not stand up a server.**

| Move | Meaning | Not |
|------|---------|-----|
| **Publish** | Push *this* bundle to `harbor-cti` | Email the PDF; TIP keyword search |
| **Consume** | Pull the bundle from `harbor-cti` | Browse VirusTotal |

**Relationship line:** `source | relationship_type | target`  
**Validate line:** `object | valid or invalid | why`  
**TAXII line:** `publish or consume | collection | what moves | not this channel`  
**Scenario sentence:** one line that walks the graph (not a 3.11 product).

**Classroom graph (Night Owl):**

| Source | Type | Target |
|--------|------|--------|
| indicator `nightowl-updates.net` | **indicates** | malware `update.exe` |
| malware `update.exe` | **uses** | attack-pattern T1059.001 |
| sighting WS-JLEE | **sighting_of** | indicator `nightowl-updates.net` |
| course-of-action block domain | **mitigates** | attack-pattern T1059.001 / the indicator |
| malware | **targets** | identity `jlee` / Harbor |

No `attributed-to` threat-actor — that vertex is empty (**3.10.1**).

| This lesson | Other |
|-------------|-------|
| Graph + validate + TAXII channel | Label types only — **3.10.1** |
| Not hunt leads | **2.4.3** |
| Not the narrative product | **3.11** |
| Not TIP search | **3.3.1** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Four real relationship types | `connects-to` invented |
| Valid indicator pattern | threat-actor from the vendor PDF |
| Publish bundle to `harbor-cti` | Email PDF = TAXII |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Graph + Scenario (Expected)

**Links:** indicates / uses / sighting_of / mitigates (table above).  
**Scenario:** “Harbor `jlee` / WS-JLEE was *sighted* using indicator `nightowl-updates.net`, which *indicates* malware `update.exe` that *uses* T1059.001; CoA is block the domain.”  
**Not:** a two-page actor profile.

### Example 2: Invalid Object (Lead)

**Draft A:** `relationship` with no `relationship_type`.  
**Draft B:** `threat-actor` name = Night Owl APT.

**Fail.** A is invalid. B is an unearned who (**3.10.1** / **3.7.2**).  
**Lead:** Validate before you publish.

### Example 3: PDF as TAXII (Lead)

**Draft:** Email the Harbor PDF to the intel DL and call it TAXII.

**Fail.** TAXII publishes/consumes a **STIX bundle** on a **collection**. The PDF may be **3.11** dissemination — different channel.  
**Lead:** Structure vs transport vs prose.

---

## 3. Hands-On Exercise

**Objective:** Link, validate, TAXII. Reject invented types and PDF-as-TAXII.

**Use only real relationship types from the card.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Link** (3.10.2.1): write **relationship lines** for A–C, then one **scenario sentence**.

   - A. Domain indicator → `update.exe`.  
   - B. `update.exe` → T1059.001.  
   - C. WS-JLEE saw the domain.

3. **Validate** (3.10.2.2):

   - D. Indicator with pattern `[domain-name:value = 'nightowl-updates.net']`, `pattern_type` = stix.  
   - E. Relationship missing `relationship_type`.  
   - F. Threat-actor “Night Owl APT” only.

4. **TAXII** (3.10.2.3):

   - G. Publish *this* bundle to `harbor-cti`.  
   - H. “Email the PDF — that’s TAXII.”

5. Do not write hunt leads (**2.4.3**). Do not write a **3.11** product. Do not invent relationship types. Do not stand up a server.

**Expected Outcome:**
- Three example summaries
- Three relationship lines + one scenario sentence
- Three validate lines (E and F invalid)
- Two TAXII lines (H fail)
- No hunt card, no narrative product

---

## 4. Knowledge Check

1. What is a STIX **bundle** *for* in production?
2. Give one **real** `relationship_type` and what it links in the Night Owl graph.
3. Name one thing that makes a classroom object **invalid**.
4. What is **TAXII**, versus the bundle itself?
5. Where do you write the finished **prose** product?

---

## 5. Summary

- Link with real types. Validate. Publish/consume the bundle on TAXII — not a PDF email.
- This closes unit **3.10**. Next: **3.11** Intelligence Production & Dissemination.

---

## 6. References & Further Reading

- Related modules:
  - 3.10.1 – Core STIX objects (previous)
  - 2.4.3 – STIX as hunt input
  - 3.11 – Finished products (next)
  - 3.3.1 – Internal TIP
- STIX 2.1 relationship types and TAXII 2.1 collections (lookup)
- Classroom graph and `harbor-cti` collection (lesson-only)
