# Instructor Guide – Module 1.6 – SOC Analyst Section Summary

**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led synthesis and discussion  
**Module Type:** Section summary — no proficiency mapping

## Purpose

Close the 1.x SOC block by reconnecting the lessons into one evidence-to-handoff workflow.

This is **not** a compressed reteaching of all 26 instructional modules.

The learner should demonstrate that the major distinctions and handoffs now fit together.

Keep the original 1.0 model visible:

**Endpoint evidence → Network evidence → Detection logic → Alert investigation → Reporting / handoff**

or:

**Observe → Detect → Investigate → Communicate**

## Learning Outcomes

By the end of the summary, learners should be able to:

1. Explain how 1.1–1.5 combine into one SOC workflow.
2. Walk A12 from raw evidence through assessment and handoff.
3. Preserve the most important conceptual boundaries from the SOC block.
4. Identify which 1.x unit to revisit when a skill remains weak.
5. Explain how a SOC RFI can become an input to CTI.

## Suggested Timing

| Part | Time |
|---|---:|
| Revisit the 1.0 model | 2 min |
| 1.x at a glance | 3 min |
| A12 end-to-end walkthrough | 6–7 min |
| Important distinctions | 3 min |
| Integrated review / CTI transition | 3–4 min |

## Teaching Strategy

### Do not reteach every field

Avoid turning this into:
- another Sysmon lecture;
- another Zeek field review;
- another Sigma syntax lesson;
- another TP/FP quiz.

Instead, ask learners to explain **where each piece belongs in the workflow**.

If they cannot, point them back to the source unit.

### Use A12 as the spine

Walk one scenario from start to finish.

Ask in order:

1. What does the endpoint evidence establish?
2. What does the network evidence add?
3. What caused the detection to match?
4. What still needs investigation?
5. Which labels describe detection correctness versus activity type?
6. What remains uncertain?
7. What report or request moves the work forward?

The scenario is more valuable than six disconnected review questions.

## Important Distinctions to Reinforce

### Observation vs conclusion

Require learners to state observations before conclusions.

### Endpoint vs network visibility

Ask:

> Can Zeek tell you that `wscript.exe` opened the socket?

Expected answer:

> Not from ordinary Zeek wire telemetry alone; correlate endpoint telemetry.

### Detection match vs maliciousness

Ask:

> If a Sigma or SIEM condition matches, what has been proven?

Expected answer:

> The rule condition matched the event; maliciousness still requires context.

### Classification vs category

Ask for one example of each:
- TP/FP/TN/FN
- user/root/scan/unsuccessful/local category

### False positive vs cause

Ask:

> “False positive because backup software ran PowerShell” contains which two ideas?

Expected answer:
- classification = false positive;
- cause = benign activity matched the logic, with the actual cause/tuning explanation determined from evidence.

### Timing distinctions

Ask which clock applies:
- alert first-touch / close-escalate;
- incident-report submit;
- RFI submit;
- blocked-for-more-info escalation.

The exact classroom minutes are secondary to identifying the correct clock.

### Incident report vs RFI

Use:

> A12 is already an incident. You need CTI to work the update domain.

Expected answer:

> RFI beside the existing incident; not a second incident report.

## Integrated Review Exercise – Expected Shape

Evidence card:

- `WS-JLEE`
- `jlee`
- `wscript.exe` → encoded PowerShell
- external request for `/update.exe`
- detection fires on encoded PowerShell
- successful download/execution not established

A strong learner response should contain:

**Host evidence**
> Endpoint telemetry observed `wscript.exe` launch encoded PowerShell under the identified user context.

**Network evidence**
> Network telemetry observed the host request `/update.exe` from external infrastructure.

**Detection**
> The analytic matched the encoded-PowerShell condition.

**Assessment**
> Suspicious activity warrants incident handling / continued investigation; the evidence should be phrased according to the case context rather than assuming the payload executed.

**Remaining gap**
> Successful download and execution of `/update.exe` are not established.

**Handoff**
> Preserve the incident record and issue a bounded RFI if CTI context is needed.

Do not require identical wording. Require preserved evidence boundaries.

## SOC Readiness Check

Use the checklist as a diagnostic.

If a learner cannot:
- identify process/file/registry/network evidence → revisit **1.1**;
- explain wire evidence → revisit **1.2**;
- explain why a rule matches → revisit **1.3**;
- separate investigation/classification/category/cause → revisit **1.4**;
- select and route the correct output → revisit **1.5**.

## Transition to CTI

The handoff should feel natural:

> SOC has local observations and an unanswered intelligence question.

Then:

> CTI determines what outside/contextual information can answer that question, evaluates the evidence, and produces an assessed answer.

This prepares learners for **2.x – Cyber Threat Intelligence**.

## Instructor Closing

Finish with the same principle used in 1.0:

> **Describe what the evidence shows first. Then decide what it means.**

The learner should now understand why that principle supports every downstream function in the course.
