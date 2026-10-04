# Module 0.4 – How work can move

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- Hunter: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- CTI: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- DE: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Describe one possible workflow after an alert is triaged.
2. Explain how intelligence findings can support blocking, hunting, and detection work.
3. Given a step in the workflow, identify the receiving role and the product it owns.

**Mapped Proficiency Items:**
- K: 0.4 – How work can move
- T: 0.4.1 – Given a step in the flow, name the next hand-off and whose product it is

## Why This Matters

An investigation can create several kinds of follow-on work. Some work addresses the incident already in progress, while other work improves understanding or future detection. Following one possible workflow helps you identify who receives a request and what they are expected to produce.

## 1. From an alert to response and a question

An analyst begins by triaging an alert: reviewing the available evidence, determining its significance, and deciding what handling it needs. In the course example, the finding warrants an incident-response handoff and leadership notification. The analyst also identifies a question for CTI and sends an RFI.

These activities may proceed in parallel. Immediate response does not have to wait for every intelligence question to be answered. Which findings require escalation and who must be notified are matters for the organization's own procedures.

## 2. How the intelligence work branches

CTI evaluates the question, adds relevant context, and develops an answer. That work may identify related infrastructure or behaviors worth examining elsewhere.

| Finding or product | Recipient and intended result |
|---|---|
| Infrastructure supported for blocking consideration | The firewall / IA function evaluates a blocking change under local procedures. |
| An intelligence package with a question and searchable leads | Hunters search for relevant activity and report their findings and gaps. |
| That same package with useful detection opportunities | DE assesses whether existing detections meet the need and whether a rule should be written or tuned. |

Related infrastructure is initially a candidate to evaluate. Its relationship to a known indicator supplies a lead; the evidence and operational context determine whether a blocking recommendation is justified. The same infrastructure may also be useful in a hunt, depending on the question and available telemetry.

## 3. Naming the next handoff

When given a point in this workflow, describe the receiving role and the work it owns. For example, a hunt team receiving a package owns the search and the resulting findings. DE receiving that package owns the assessment of detection coverage and any resulting rule work. Depending on the environment, that work may involve Microsoft Defender for Endpoint (MDE) analytics or rule formats such as Sigma, YARA, and Suricata.

An effective handoff makes the requested outcome understandable. The course introduces that responsibility before teaching the detailed formats. Your site's processes determine where the request is recorded, who accepts it, and how the result is returned.

## Knowledge Check

1. In the escalated course example, what can the analyst do after triage while CTI works on an RFI?
2. CTI has evidence supporting consideration of a domain block. Who receives that work, and what product does that function own?
3. The same intelligence package goes to Hunt and DE. What result should each produce?

## Summary

A single alert can lead to response, notification, intelligence analysis, hunting, and detection work. Identify each handoff by its purpose and the product the receiving role owns. The example explains how the responsibilities connect while leaving local routing and approval procedures to the organization.

## Course Connections

Previous: [0.3 – Jobs in one sentence](../03-jobs-in-one-sentence/student-guide.md)

Next: [0.5 – Where the jobs lightly overlap](../05-where-jobs-overlap/student-guide.md)

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.
