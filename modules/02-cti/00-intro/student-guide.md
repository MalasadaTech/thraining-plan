# Module 2.0 – Cyber Threat Intelligence: How the 2.x Block Fits Together

**Target Audience:** CTI Analyst (primary); SOC Analyst, Threat Hunter (secondary)  
**Estimated Time:** 10–15 minutes  
**Module Type:** Orientation — no proficiency mapping

## Learning Objectives

By the end of this introduction, you will be able to:

1. Explain how the reorganized 2.x CTI block moves from an intelligence question to an assessed answer.
2. Describe the role of tradecraft, frameworks, platforms, enrichment, assessment, and production in that workflow.
3. Recognize why platform results and enrichment records are inputs to analysis rather than finished intelligence.

## 1. What the CTI Block Is Building Toward

CTI begins with a question.

That question may come from leadership, a standing intelligence requirement, a SOC case, a threat hunt, or another defensive function.

The analyst's job is to turn available evidence into an answer that is:

- relevant to the requirement;
- grounded in identifiable sources;
- explicit about uncertainty;
- useful to a decision or next action.

A useful mental model for the 2.x block is:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

The analyst does more than gather information.

The analyst decides what the evidence supports.

## 2. The Eight Units

| Unit | Main question | What you learn |
|---|---|---|
| **2.1 – Intelligence Foundations and Requirements** | What question are we answering? | Data vs information vs intelligence, lifecycle, requirements, RFI intake, actionability, audience, attribution, and collection sources |
| **2.2 – Analytical Tradecraft** | How do we reason carefully about incomplete evidence? | Estimative language, structured techniques, source/information evaluation, and bias mitigation |
| **2.3 – Analytical Frameworks** | How can we organize what we know? | ATT&CK, Diamond Model, and Cyber Kill Chain as analytic structures |
| **2.4 – CTI Tools and Platforms** | Which source or platform should answer this lookup? | Internal TIP use, question-driven platform selection, VirusTotal, ANY.RUN, Silent Push, and urlscan.io |
| **2.5 – Technical Enrichment and Discovery** | What additional technical relationships can we test? | IOC lifecycle, file similarity, RDAP/WHOIS, DNS, infrastructure pivots, DTF, correlation, and link analysis |
| **2.6 – Threat Assessment and Organizational Significance** | Does this matter here? | Applicable TTPs, visibility, relevance, and plausible organizational impact |
| **2.7 – Intelligence Production and Dissemination** | How do we package and deliver the supported answer? | STIX, finished intelligence, RFI response/closure, and dissemination |
| **2.8 – Local Application** | How does this organization actually run CTI? | Local requirements, production/approval process, and dissemination channels |

Each unit answers a different part of the same intelligence requirement.

## 3. Start With the Requirement

Suppose the SOC asks CTI about A12:

> **What is known about the update domain, and does available evidence support that it delivered `update.exe` during the incident?**

That question creates a requirement.

Before searching, the analyst should understand:

- what is being asked;
- who needs the answer;
- what decision the answer will support;
- what is already known;
- what evidence would materially change the answer.

This keeps collection focused.

Without a requirement, enrichment can easily become endless browsing.

## 4. Collection Is Question-Driven

Different sources answer different questions.

For example:

- an internal TIP may show prior reports or sightings;
- VirusTotal may expose file relationships, detections, or behavior;
- ANY.RUN may show one sandbox execution;
- Silent Push may provide passive-DNS or infrastructure context;
- urlscan.io may provide a web-scan observation.

The important question is not:

> Which tools have I not checked yet?

It is:

> Which source can answer the next unresolved question?

That is why the reorganized course teaches **platform selection before deep enrichment**.

## 5. Platforms Use Two Passes

The 2.4 platform lessons introduce retrieval and interpretation boundaries.

Later 2.5 method lessons use those platforms again when the analyst needs a specific enrichment technique.

Think of the two passes as:

### First pass – Retrieve correctly

Understand:
- what object you are querying;
- what the platform can return;
- what the observation time/source means;
- what the result cannot prove.

### Second pass – Use the result analytically

Apply the result to:
- file similarity;
- infrastructure discovery;
- DNS/registration analysis;
- correlation;
- campaign tracking.

The platform is not the method.

It supports the method.

## 6. Enrichment Creates Candidate Relationships

Enrichment can reveal:

- related files;
- historical DNS;
- registration context;
- certificates;
- domains;
- IP addresses;
- infrastructure characteristics;
- behavioral artifacts.

Those findings often begin as **candidate relationships**.

For example:

> Two domains share an uncommon nameserver during overlapping periods.

That may justify further analysis.

It does not automatically prove:
- common ownership;
- common malicious control;
- a campaign;
- actor attribution.

Correlation in 2.5.7 tests whether individual findings form a stronger supported relationship.

## 7. Assessment Asks What Matters Here

Technical enrichment is not the end of CTI.

The analyst must determine whether the finding matters to the organization.

Keep these questions separate:

**Applicability**  
> Can this behavior occur in our environment?

**Visibility**  
> Can our telemetry observe it?

**Relevance**  
> Does it meaningfully intersect our mission, assets, technologies, or exposure?

**Impact**  
> If true here, what plausible consequence follows?

A finding can be applicable but not visible.

It can be visible but low relevance to the current requirement.

The distinctions keep the assessment useful.

## 8. Production Turns Analysis Into a Usable Answer

The final product should answer the original requirement.

That may include:

- a direct RFI response;
- a finished intelligence product;
- STIX objects for structured representation;
- a handoff to hunting or Detection Engineering;
- an explicit follow-up requirement when evidence remains incomplete.

The product should separate:

- supported facts;
- analytical judgments;
- confidence/uncertainty;
- unresolved gaps;
- recommended or requested next action.

The answer should be no broader than the evidence supports.

## 9. One A12 CTI Flow

A12 can move through the whole 2.x block.

### Requirement

> Did the update domain likely support payload delivery, and what related activity matters to DYA?

### Collect

Retrieve:
- internal TIP context;
- public reporting;
- file/platform observations;
- infrastructure records.

### Evaluate

Preserve:
- source;
- observation/reporting time;
- provenance;
- source reliability/information credibility;
- uncertainty.

### Enrich

Investigate:
- file relationships;
- registration;
- DNS;
- infrastructure;
- related domains/IPs.

### Correlate

Test whether the findings support:
- a candidate relationship;
- a stronger activity-set/campaign assessment;
- or only weak/shared-provider coincidence.

### Assess

Determine:
- which TTPs apply;
- whether they are visible;
- why the finding matters locally;
- plausible impact.

### Produce

Write the evidence-based answer and represent structured objects when useful.

### Disseminate

Deliver the answer to the correct audience and record closure or follow-up.

## 10. What You Need to Remember Before 2.1

You do not need to memorize every platform field or enrichment technique yet.

Remember the workflow:

> **Know the question.**  
> **Collect only what helps answer it.**  
> **Preserve provenance.**  
> **Treat pivots as candidates until tested.**  
> **Assess significance, not just technical interest.**  
> **Answer the requirement directly.**

## Orientation Check

1. Why does the reorganized track teach platform selection before deep enrichment?
2. What is the difference between a platform result and finished intelligence?
3. A shared nameserver links two domains. What can you record before stronger corroboration exists?
4. Why are applicability and visibility separate questions?
5. What should the finished product return to at the end of the workflow?

## Summary

The 2.x CTI block moves from a question to a supported answer:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

The recurring discipline is:

> **Preserve the evidence, make the judgment explicit, and answer the requirement—not the tool.**

**Next:** **2.1.1 – Difference Between Data, Information, and Intelligence**.
