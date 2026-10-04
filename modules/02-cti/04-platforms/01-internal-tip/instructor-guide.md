# Instructor Guide – Module 2.4.1 – Internal Threat Intelligence Platform

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.1 B / C / C ; 2.4.1.1 3c / 4c / 4d  
- Hunter: 2.4.1 A / B / B ; 2.4.1.1 1a / 2b / 3c  
- SOC: 2.4.1 A / A / B ; 2.4.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners understand the internal TIP as the organization's intelligence workspace and use it to recover prior context without confusing a platform hit with proof or a platform miss with benign activity.

**Context:** The preceding 2.2 modules focused on analytic tradecraft. This lesson moves into a tool-supported workflow: retrieving organizational knowledge that can inform enrichment, analysis, and production.

The lesson should remain platform-agnostic. Product interfaces differ, but the reasoning is stable: search the correct object, inspect what the platform actually contains, evaluate provenance and relevance, and use the result without overstating it.

**Important distinction:** *Internal TIP* means the organization's platform, not that every object inside it came from an internal collection source. The platform may hold internal, commercial, and open-source material.

**Required materials:** The aligned student guide and slide deck. If a classroom TIP is available, use it to demonstrate the same workflow without making product-specific navigation part of the learning objective.

## Learning Objectives

By the end of this module, learners will be able to:

1. Explain the purpose and core functions of an internal TIP, including how it supports enrichment, analysis, and production.
2. Search for an indicator or report, interpret what the platform returns, and use the result to support enrichment or analysis.

**Mapped Proficiency Items:**
- K: 2.4.1 – Internal threat intelligence platform
- T: 2.4.1.1 – Search, retrieve, and use the internal TIP for enrichment or analysis

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---:|---|
| Introduction | 3 minutes | Establish the TIP as organizational knowledge, not a public lookup substitute. |
| Core functions | 4 minutes | Explain store, search/retrieve, relate, and support production. |
| Search and retrieval | 5 minutes | Show why object type and search method matter. |
| Interpreting hits and misses | 6 minutes | Separate stored context from proof and absence from benignness. |
| A12 walkthrough | 3 minutes | Apply the workflow to one domain. |
| Knowledge check | 3 minutes | Listen for correct interpretation of TIP results. |
| **Total** | **24 minutes** | Adjust demonstration time as needed. |

## Detailed Teaching Notes

### 1. Start with the analyst's problem

Ask learners what can go wrong if an analyst immediately begins public enrichment without checking what the organization already holds. Useful answers include duplicated work, missed prior reporting, missed organizational sightings, and failure to reuse earlier analysis.

Then clarify the reverse problem: finding an object in the TIP does not mean the current assessment is already settled. The platform provides context that still has to be evaluated.

### 2. Explain what “internal” means

Make the distinction explicit. The TIP is internal because it belongs to the organization or is used as its intelligence workspace. Its contents can have many source origins.

This prevents learners from confusing **repository location** with **source class**, which was taught in Module 2.1.9.

### 3. Teach the core functions as analyst actions

Use four verbs:

- **Store** — preserve intelligence objects and context.
- **Search / retrieve** — recover what is already recorded.
- **Relate** — connect objects or observations when the evidence supports the relationship.
- **Use** — incorporate supported context into enrichment, analysis, or production.

If the platform has additional features, map them back to these functions rather than expanding the syllabus into a product tour.

### 4. Teach search discipline

Give learners a domain and a hash. Ask how each should be searched.

The important lesson is that a miss is meaningful only after a valid search. A wrong object type or malformed query can produce a false negative.

When a result appears, have learners inspect:
- source or provenance;
- date or last update;
- linked reports;
- sightings or observations;
- relationships and what supports them.

### 5. Teach the difference between a hit and a conclusion

Use the A12 update domain. Imagine the TIP contains an older report linking that domain to malicious activity.

Ask: **What does that add?** It adds prior context and perhaps corroboration.

Then ask: **What does it not automatically prove?** It does not prove the domain played the same role in A12, that every historical relationship remains current, or that a vendor attribution attached to the object applies to this incident.

The learner should understand that TIP context becomes part of the evidence base; it does not replace analysis.

### 6. Teach the difference between a miss and benignness

If the correct search returns no match, record the absence accurately.

Then ask learners what explanations remain possible: the object is new to the TIP, never ingested, stored under another representation, absent from prior reporting, or simply unknown to the organization's intelligence repository.

The absence can guide further collection, but it is not a verdict on the indicator.

### 7. Connect the result to workflow

If a matching object exists, the learner should be able to state what relevant context it adds and cite or reference it appropriately.

If the current incident establishes a new observation, the learner may record or relate it according to the platform's workflow. Emphasize **when justified by evidence**; linking objects merely because they appear in the same investigation can create bad intelligence that later analysts will trust.

## Common Student Challenges

| Misunderstanding | Teaching response |
|---|---|
| Internal TIP means all content is internally sourced. | Separate repository ownership from source provenance. |
| A matching TIP object proves the current case. | Ask which relationship is actually supported by current evidence. |
| No TIP match means the indicator is benign. | Reframe the result as absence from the repository, not absence of threat. |
| Any empty search counts as a miss. | Verify the object type and search method first. |
| More links make the TIP more useful. | Explain that unsupported relationships pollute future analysis; relationships should reflect evidence. |

## Knowledge Check – Answer Key

### 1. Older TIP object for the A12 update domain

**Expected answer:** Check provenance, date, the source of the relationship, whether the prior context is still relevant, and whether current A12 evidence independently supports applying that relationship.

### 2. Correct search returns no match

**Expected answer:** The TIP did not return a matching object under the valid search. It does not establish benignness, internet-wide novelty, or absence from every internal telemetry source.

### 3. Current file hash matches a TIP object with notes and a sighting

**Expected answer:** The result can enrich the file with prior organizational context and help the analyst compare the current evidence with earlier observations. The analyst still has to determine whether those earlier notes and relationships apply to the present case.

## Summary and Transition

Close with the distinction learners should carry forward: **the TIP tells you what the organization has recorded; analysis determines what that context means for the current question.**

The next module selects a source for a defined CTI question and records what the lookup can establish.
