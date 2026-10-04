# Module 3.7.3 – Hunt Outputs and Hand-off

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.3 B / C / C ; 3.7.3.1 3c / 4c / 4c  
- SOC: 3.7.3 A / A / B ; 3.7.3.1 1a / 1a / 2b  
- CTI: 3.7.3 A / A / B ; 3.7.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Locate the site's definition of a complete hunt output and the local hand-off map.
2. Produce the required package and route each finding to the locally authorized consumer.

## Mapped Proficiency Items

- K: 3.7.3 – Hunt outputs and hand-off
- T: 3.7.3.1 – Produce required hunt outputs and perform proper hand-off

## 1. Key Concepts

A hunt is not complete merely because the query finished.

The organization decides what the finished hunt must contain and which teams receive which outcomes.

### Common output categories

A local output standard may require some combination of:

- hypothesis and scope;
- queries/data sources used;
- findings and affected hosts/accounts;
- evidence and confidence/limitations;
- **detection gaps**;
- **visibility gaps**;
- reusable search logic;
- follow-on hunt leads;
- recommended hand-offs or actions.

These are examples, not a universal local checklist.

### Findings can require different consumers

A useful hand-off map may distinguish outcomes such as:

| Finding type | Possible consumer category |
|---|---|
| Active/suspected compromise | SOC / IR |
| Detection coverage gap | Detection engineering or equivalent |
| New infrastructure / intelligence question | CTI |
| Missing telemetry | Telemetry/platform owner |
| Out-of-scope investigative lead | Local lead-management process |

The actual team names, queues, and approval paths are site-specific.

### Preserve the evidence boundary

A hunt package should make clear:

- what was observed;
- what was inferred;
- what scope was searched;
- what telemetry was unavailable;
- whether additional hosts were found;
- whether a negative result is limited by visibility.

### A12 example

A finished A12 hunt might report:

- 2 additional hosts with the exact `Updater → %TEMP%\update.exe` persistence pattern;
- 18 hosts searched with complete registry visibility;
- 7 hosts without the required registry telemetry;
- no existing analytic covering the exact pattern;
- a follow-on lead involving a different Run-value name pointing to a user-writable path.

The **facts** remain the same regardless of which local team receives each part. The local hand-off map determines who owns response, detection improvement, visibility remediation, and follow-on intelligence.

### Missing local list/map

Use:

> **Local hunt output requirements / hand-off path not yet verified.**

Then identify the owner/source needed to close that onboarding gap.

## 2. Knowledge Check

1. Why is “the query finished” not enough to call the hunt complete?
2. Which two gap types should a hunt output distinguish?
3. A hunt finds active compromise, a detection gap, and missing registry telemetry. Why might those outcomes have different consumers?

## 3. Summary

A finished hunt communicates findings, scope, evidence, gaps, and follow-on work in the form required locally.

Then route each outcome through the organization's authorized hand-off map.

This completes the **3.x threat-hunting block**.

**Next track:** **4.x – Detection Engineering**.

## Reference Model

This module intentionally relies on the organization's local hunt-output and hand-off standard.
