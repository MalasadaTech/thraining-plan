# Module 2.4.1 – Internal Threat Intelligence Platform

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.1 B / C / C ; 2.4.1.1 3c / 4c / 4d  
- Hunter: 2.4.1 A / B / B ; 2.4.1.1 1a / 2b / 3c  
- SOC: 2.4.1 A / A / B ; 2.4.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Starting point

Use an existing case object to learn retrieval, provenance, and relationships. Select the correct object type using the TIP's labels; detailed STIX object construction is taught later in [2.7.1–2.7.2](../../07-production/01-core-objects/student-guide.md). Confirm the site's access and handling rules before a live lookup.

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose and core functions of an internal threat intelligence platform (TIP), including how it supports enrichment, analysis, and production.
2. Search for an indicator or report, interpret what the platform returns, and use the result to support enrichment or analysis.

**Mapped Proficiency Items:**
- K: 2.4.1 – Internal threat intelligence platform
- T: 2.4.1.1 – Search, retrieve, and use the internal TIP for enrichment or analysis

## 1. Key Concepts

A threat intelligence platform helps an organization organize the intelligence it already holds so analysts can find prior reporting, indicators, relationships, and observations before starting the same work again.

The word **internal** describes the organization's platform or workspace. It does not mean every item inside it came from an internal source. A TIP may contain material produced by the organization alongside commercial reporting, open-source reporting, imported indicators, and analyst-created relationships. The practical question is: **what has our organization already recorded about this object or topic?**

That makes the TIP useful at several points in the intelligence workflow.

| Function | What it helps the analyst do |
|---|---|
| **Store** | Preserve indicators, reports, notes, relationships, and sightings or observations. |
| **Search and retrieve** | Find existing objects and prior context related to a hash, IP address, domain, report, or other intelligence object. |
| **Relate** | Connect an observation or report to objects already in the platform when the evidence supports that relationship. |
| **Support production** | Reuse relevant internal context and cite what the organization already knows in an assessment or report. |

### Search the object you actually have

A useful TIP search begins with the value and object type in front of you. If you have a domain, search for that domain as a domain object. If you have a file hash, search the appropriate hash value or file object.

This sounds simple, but it matters. An empty result only means something if the search was performed correctly. Searching the wrong object type, using a partial value when the platform expects an exact value, or overlooking alternate representations can create a false impression that the TIP contains nothing.

When a matching object exists, open it and examine the context already attached to it. Useful questions include:

- Where did this object come from?
- When was it added or last updated?
- What reports or observations are linked to it?
- Has the organization recorded a sighting or other relevant observation?
- What relationships are explicitly supported?
- Is any of the information stale, superseded, or source-limited?

The goal is not merely to find a hit. It is to understand what the hit actually tells you.

### A hit adds context; it does not automatically prove the current case

Suppose you search the A12 update domain and find an existing TIP object. The object may contain a prior report, a related IP address, or an earlier organizational observation.

That information can enrich the current analysis, but the analyst still has to determine whether the older context applies to the present activity. A prior association is evidence to consider, not automatic proof that the same relationship still holds.

This is especially important when the object contains older reporting, vendor attribution, or relationships created for a different incident.

### A miss is also information—but only about the TIP

If the search returns no matching object, record that result accurately: **no matching object found in the TIP** or **not found in TIP**, depending on local practice.

That result means the platform did not return a match under the search you performed. It does **not** mean the indicator is benign, new to the internet, or absent from every organizational data source.

A TIP miss may identify an intelligence gap or simply show that the platform has not yet captured the relevant context. The next step depends on the requirement: the analyst may need to check internal telemetry, an external source, or another collection path.

### How the TIP supports enrichment, analysis, and production

**Enrichment** uses the platform to recover context already held by the organization: prior reporting, relationships, notes, source information, or observations.

**Analysis** compares that context with the current evidence. The analyst asks whether the existing relationships still fit the current case, whether the TIP adds useful corroboration, and what remains unresolved.

**Production** incorporates relevant TIP context into the finished assessment with enough provenance that another analyst can understand where the information came from. If the TIP search produced no match, that can also be recorded when it matters to the analytic story.

### Following one A12 lookup

Assume you are examining the update domain from A12.

1. **Search:** Query the domain using the correct object type or field.
2. **Retrieve:** Open the matching object if one exists and review its sources, dates, relationships, and observations.
3. **Evaluate:** Decide which of that context is relevant to the A12 question and which relationships still require independent support.
4. **Use:** Incorporate supported context into the analysis, or record that no matching object was found.
5. **Relate when justified:** If the current evidence establishes a new observation or relationship, record it according to the platform's workflow rather than creating unsupported links.

A TIP is most useful when it helps the analyst reuse organizational knowledge without confusing **stored context** with **proven fact**.

## 2. Knowledge Check

1. You find an older TIP object for the A12 update domain that links it to a prior report. What should you check before treating that relationship as relevant to the current incident?
2. You search the correct domain object and the TIP returns no match. What does that result tell you, and what does it *not* tell you?
3. A file hash appears in a current investigation and the TIP contains a matching object with prior notes and a sighting. Explain how the TIP result can support enrichment and analysis without automatically deciding the current case.

## 3. Summary

The internal TIP is the organization's intelligence workspace for preserving and reusing context. Search the object you actually have, inspect the provenance and relationships behind any match, and use only the context that the evidence supports.

A TIP hit adds context; it does not automatically prove the current assessment. A TIP miss means no matching object was returned—it does not mean benign. Used carefully, the platform reduces duplicated work and makes prior organizational knowledge available to enrichment, analysis, and production.


## 4. Related Modules

- 2.2.4 – Cognitive biases and mitigation
- 2.5.2 – File similarity and hashing techniques
- 0.7 – External tool survey
- 2.4 – Platform enrichment and pivoting
- 2.7 – STIX / structured intelligence authoring

**Next:** [2.4.2 – Selecting Platforms for CTI Work](../02-platform-selection/student-guide.md).
