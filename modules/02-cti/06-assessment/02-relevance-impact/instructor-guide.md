# Instructor Guide – Module 2.6.2 – Threat Relevance and Organizational Impact

**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Purpose

Teach learners to translate technical findings into local relevance and plausible organizational consequence without collapsing relevance, applicability, visibility, requirements, or attribution into one judgment.

## Key Teaching Distinctions

**Applicability:** Can the behavior occur here?  
**Visibility:** Can we observe it?  
**Relevance:** Does the finding matter to this mission/environment?  
**Impact:** What plausible consequence follows if it is true here?

These can move independently.

## A12 Walkthrough

Finding:
- encoded PowerShell;
- update-domain request;
- `WS-JLEE`;
- Windows environment.

Good relevance:
> Relevant because Windows workstations are present and the behavior was observed on a local asset.

Good impact:
> If the domain was used for payload delivery, the workstation may require containment and examination for transfer/execution evidence.

The wording preserves the unresolved download/execution question.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Treats relevance as “is the report interesting?” | Tie it to mission, assets, technology, exposure, or observed evidence. |
| Treats no visibility as no relevance. | Re-establish visibility as a separate telemetry question. |
| Writes maximum theoretical impact. | Ask what consequence follows from the evidence actually present. |
| Turns the answer into attribution. | Remove actor/country claims unless they are needed and separately supported. |
| Lets a relevant side lead replace the current requirement. | Preserve it as follow-on while answering the requirement first. |

## Knowledge Check – Answer Key

1. Applicability asks whether the behavior can occur here; relevance asks whether the finding meaningfully intersects the organization's mission/environment and current context.
2. No. It can remain relevant and applicable while creating a visibility gap.
3. Accept answers that tie A12 to the Windows workstation and describe a conditional host/IR consequence without claiming unproven execution or enterprise compromise.
