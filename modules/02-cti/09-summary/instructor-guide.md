# Instructor Guide – Module 2.9 – Cyber Threat Intelligence Section Summary

**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led synthesis and discussion  
**Module Type:** Section summary — no proficiency mapping

## Purpose

Close the reorganized 2.x CTI block by reconnecting the lessons into the workflow introduced in 2.0:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

This is not a compressed reteaching of every CTI technique.

The learner should demonstrate that the requirement, evidence, assessment, product, and handoff now fit together.

## Learning Outcomes

By the end of the summary, learners should be able to:

1. Explain how 2.1–2.8 combine into one intelligence workflow.
2. Walk the A12 RFI from intake to evidence-based response.
3. Preserve the most important evidence and judgment boundaries.
4. Identify which 2.x unit to revisit when a CTI skill remains weak.
5. Explain how a finished intelligence answer becomes a hunt input.

## Suggested Timing

| Part | Time |
|---|---:|
| Return to the 2.0 workflow | 2 min |
| 2.x at a glance | 3 min |
| A12 RFI end to end | 7 min |
| Important distinctions | 3 min |
| Readiness / hunt transition | 3–4 min |

## Teaching Strategy

### Do not turn this into another platform tour

Avoid:
- checking every platform again;
- reteaching every framework;
- producing a large IOC list;
- reviewing STIX syntax in detail.

Instead, ask learners:

> What did this evidence change about the answer to the requirement?

### Use one A12 RFI as the spine

Ask in order:

1. Who is the customer?
2. What is the exact question?
3. What evidence is already known?
4. Which remaining question determines collection?
5. Which source/platform can answer it?
6. What did enrichment reveal?
7. Which relationships are candidates versus assessed?
8. Which TTPs apply locally?
9. What is visible?
10. Why does it matter?
11. What does the final answer support?
12. What remains unresolved?
13. Is the RFI closed or followed by a new requirement?

## Important Distinctions to Reinforce

### Data / information / intelligence

Require learners to identify which level their statement represents.

### Requirement / collection

Ask:

> Is “search VirusTotal” an intelligence requirement?

Expected answer:

> No. It is a collection action. The requirement is the question being answered.

### Reliability / credibility

Require source and information evaluation to remain distinct.

### Platform result / assessment

Ask:

> ANY.RUN shows a behavior. What can you say?

Expected:

> The behavior occurred in that sandbox execution; broader/local conclusions require additional evidence.

### Pivot / relationship

A shared field supports a candidate lead first.

### Relationship / campaign / attribution

Require increasing evidence for increasingly strong claims.

### DTF boundary

DTF applies to infrastructure pivots. File and behavioral relationships remain separate evidence tracks.

### Applicability / visibility / relevance / impact

Use one behavior and ask all four questions.

### RFI intake / closure

Return to the exact original question at the end.

## Integrated Review – Expected Shape

A strong answer should include:

**Requirement**  
> Define the A12 domain/payload question directly.

**Evidence**  
> Preserve sandbox, DNS/RDAP, internal, and reporting provenance.

**Relationship**  
> Shared uncommon NS + overlapping IP may support a candidate/assessed infrastructure relationship depending corroboration; do not leap to attribution.

**Applicability**  
> Windows behavior applies to the environment.

**Visibility**  
> Partial visibility on one endpoint population remains a gap.

**Relevance/impact**  
> Finding matters because affected technology is present and activity was observed; plausible workstation compromise/IR consequences should stay proportional to evidence.

**Judgment**  
> State what evidence supports about attempted delivery/association.

**Gap**  
> Successful execution remains unproven.

**Closure**  
> Close if the requirement was answered at the agreed level; otherwise define the next requirement rather than endlessly expanding the original RFI.

## CTI Readiness Diagnostic

If a learner cannot:
- define requirement/customer → revisit **2.1**;
- reason about uncertainty/source quality → revisit **2.2**;
- use frameworks appropriately → revisit **2.3**;
- select/retrieve from platforms → revisit **2.4**;
- enrich/correlate technical evidence → revisit **2.5**;
- assess local significance → revisit **2.6**;
- answer/produce/disseminate → revisit **2.7**;
- identify local process → revisit **2.8**.

## Transition to Threat Hunting

Use:

> CTI has answered what the evidence means. What if the next question is whether the same behavior exists elsewhere internally?

Then:

> Threat hunting turns that intelligence into a bounded search against local telemetry.

## Instructor Closing

Finish with:

> **The value of CTI is the supported answer—not the number of tools, indicators, or pivots used to reach it.**
