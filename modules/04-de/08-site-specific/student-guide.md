# Module 4.8 – Site-Specific Detection Engineering Knowledge

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.8.1 B / C / C ; 4.8.1.1 3c / 4c / 4c ; 4.8.2 B / C / C ; 4.8.2.1 3c / 4c / 4c ; 4.8.2.2 3c / 4c / 4c  
- SOC: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1–4.8.2.2 1a / 1a / 1a  
- Hunter: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1–4.8.2.2 1a / 1a / 1a  
- CTI: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1–4.8.2.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Locate and verify the organization's current detection requirements and production standards.
2. Map the local **review → test → approve → deploy → monitor → change/retire** path, including who owns each decision.
3. Follow the verified process and clearly identify any onboarding element that has not yet been obtained.

**Mapped Proficiency Items:**
- K: 4.8.1 – Local detection requirements
- T: 4.8.1.1 – Align to the local requirements list
- K: 4.8.2 – Local review, deploy, and retire paths
- T: 4.8.2.1 – Follow the local path
- T: 4.8.2.2 – Distinguish verified local policy from an assumed or invented workflow

## 1. Key Concepts

The previous modules taught Detection Engineering tradecraft that transfers between organizations.

This module asks:

> **How does this organization actually run that work?**

The answer must come from the current local standards and process owners.

### Part 1: the local detection requirements list

A mature local standard may address categories such as:
- required metadata;
- naming/ID conventions;
- ownership;
- references;
- ATT&CK mapping;
- severity/priority;
- required data sources;
- test evidence;
- known benign/false-positive context;
- runbook/triage guidance;
- version/change information.

Those are **examples of categories**, not a field list for DYA or your organization.

For comparison, public formats such as Sigma define their own metadata and rule-status fields. See [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html). Your local organization may adopt, extend, or ignore parts of that format.

What matters in this lesson is locating the **actual local list**.

### Verify that the list is current

Capture:
- authoritative location;
- owner/maintainer;
- version/effective date;
- supersession or review cadence;
- which platforms/use cases it applies to.

A copied checklist with no owner or version may be useful background but is not enough to confidently describe current policy.

### Part 2: the local lifecycle path

Map how a detection becomes official:

| Step | Local answer |
|---|---|
| Intake / nomination | ______ |
| Engineering owner | ______ |
| Test/staging method | ______ |
| Reviewer | ______ |
| Approval authority | ______ |
| Deployment mechanism | ______ |
| Monitoring / post-deploy validation | ______ |
| Tune/change path | ______ |
| Rollback/disable authority | ______ |
| Retirement / replacement path | ______ |
| Authoritative repository / source control | ______ |

The blanks are the learning objective. Fill them from the real shop.

### Review, approval, deployment, and rollback are different decisions

One person or system may perform several of these locally, but the concepts should remain clear:

- **Review:** Is the analytic technically and analytically sound?
- **Approval:** Who is authorized to make the production decision?
- **Deployment:** How does the change reach production?
- **Rollback/disable:** Who can reverse the change when it causes a problem?
- **Retirement:** How is the old detection formally removed/superseded?

That distinction becomes important during urgent changes and production failures.

### Source control and deployment platform may be different

A detection may be authored/stored in:
- a version-controlled repository;
- a content-management platform;
- a SIEM/EDR console;
- an internal detection-as-code pipeline.

The authoritative source must be known.

Otherwise, two engineers can edit different copies and both believe they changed production.

### When local information is missing

Use precise onboarding status.

Examples:

> **Local required metadata list not yet verified.**

> **Deployment approval authority not yet verified.**

> **Rollback path not yet verified.**

This is more useful than inventing a “change board” or ticket because it tells the team exactly which operating fact still needs to be supplied.

### A12 onboarding exercise

Assume DE has built and validated an A12-related analytic.

Before production, the learner should be able to identify:

1. Which local required fields/test evidence must be present?
2. Who reviews it?
3. Who approves it?
4. How is it deployed?
5. How is post-deploy health checked?
6. Who can roll it back?
7. Where is the authoritative version stored?
8. How will future tune/retire decisions be recorded?

If those answers are not known, the analytic may be technically ready while the **production process is not yet ready**.

## 2. Knowledge Check

1. Why is a public Sigma specification not the same thing as your organization's local deployment standard?
2. Name four roles/steps you should identify in the local lifecycle path.
3. You know how to deploy a rule but do not know who can approve or roll it back. What should you record?

## 3. Summary

Site-specific DE knowledge is an **orientation and governance** skill.

Find the current requirements list, its owner and version, and the real review/deploy/change/retire path.

Follow verified local process. When a piece is missing, identify that specific onboarding gap so the organization can close it.

This completes the **4.x Detection Engineering track**.

## Supporting Reference

- [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html) – an example external rule format; not a substitute for local policy.
