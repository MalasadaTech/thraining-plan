# Module 3.4.1 – Assessing CTI for Hunting Value

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.1 B / C / C ; 3.4.1.1 3c / 4c / 4d  
- SOC: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
- CTI: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Evaluate whether a CTI report can support a useful local hunt.
2. Classify the next step as **hunt**, **awareness/monitor**, or **coordinate/hand off**, and explain the reason.

## Mapped Proficiency Items

- K: 3.4.1 – Assessing CTI for hunting value
- T: 3.4.1.1 – Triage a CTI report: hunt / don't hunt / hand off, and say why

## 1. Key Concepts

A report is hunt-worthy when it can produce a **local, testable question with enough visibility and enough incremental value to justify the search**.

Five quick checks help:

1. **Applicability** – Does the environment contain the relevant platform, service, user population, or exposure?
2. **Testability** – Does the report contain a behavior, procedure, artifact, or relationship that can become a question?
3. **Visibility** – Do we have telemetry capable of testing that question?
4. **Scope** – Can the search be bounded to a reasonable population and time window?
5. **Incremental value** – Will hunting add something beyond work already adequately covered by an active response or existing analytic?

### Three practical dispositions

| Disposition | When it fits |
|---|---|
| **Hunt** | A relevant, testable question exists; telemetry and scope are sufficient; broader discovery can add value. |
| **Awareness / monitor** | The report is useful context but does not currently support a useful local search. |
| **Coordinate / hand off** | The immediate next action belongs to IR, SOC, DE, or another function; hunting may still support later if a broader search question remains. |

The third category is not “IR touched the hash, therefore hunting stops.”

During an active incident, a reactive hunt can be especially valuable for finding additional affected systems. Coordination matters because containment and evidence preservation may take priority over an independent search on the same hosts.

### A12 examples

**Hunt**
> Report describes Run-key persistence and `/update.exe`; registry and HTTP telemetry exist; the question is whether related artifacts exist on additional workstations.

**Awareness / monitor**
> Report describes a platform the organization does not operate, with no applicable procedure elsewhere in the report.

**Coordinate / hand off**
> A specific endpoint shows confirmed active compromise requiring containment. IR owns immediate response. Hunting coordinates with IR and may run an estate-wide search for related behavior.

### Hunt-worthiness is not the same as “interesting”

Actor reputation, severity language, or a long ATT&CK appendix do not create a hunt by themselves.

The hunter needs a test.

## 2. Knowledge Check

1. What five checks help determine hunt-worthiness?
2. Why does an active IR case not automatically mean “do not hunt”?
3. A report gives a locally applicable Run-key procedure, registry telemetry exists, and no detection covers it. Which disposition fits and why?

## 3. Summary

Assess CTI for **local testability and value**, not just threat severity.

Hunt when a bounded question and visibility exist. Monitor when the report cannot support a useful local search. Coordinate when another operational function owns the immediate action.

**Next:** **3.4.2 – Extracting Hunt Leads from CTI**.
