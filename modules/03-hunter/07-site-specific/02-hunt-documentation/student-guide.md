# Module 3.7.2 – Hunt Documentation Standards

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.2 B / C / C ; 3.7.2.1 3c / 4c / 4c  
- SOC: 3.7.2 A / A / B ; 3.7.2.1 1a / 1a / 2b  
- CTI: 3.7.2 A / A / B ; 3.7.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Locate the local hunt documentation standard and authoritative repository.
2. Document a hunt using the required local fields, evidence/query retention rules, and versioning method.

## Mapped Proficiency Items

- K: 3.7.2 – Hunt documentation standards
- T: 3.7.2.1 – Document a hunt according to local standards

## 1. Key Concepts

The 3.2.2 hunt card teaches the **reasoning needed to develop a hunt**.

The organization's hunt record answers a different question:

> What must be preserved so another analyst can understand, reproduce, review, and close this hunt here?

### Learn the local documentation map

| Question | Local answer |
|---|---|
| What fields are mandatory? | ______ |
| Where is the authoritative hunt record stored? | ______ |
| How are hypothesis/scope changes recorded? | ______ |
| How are queries or notebooks retained? | ______ |
| What evidence/results must be attached or linked? | ______ |
| How are data sources and time windows recorded? | ______ |
| How are gaps and limitations captured? | ______ |
| How are revisions/version history handled? | ______ |
| What status/closure fields are required? | ______ |

These are orientation questions, not a substitute template.

### Reproducibility matters

A future analyst should be able to answer:

- What was the hypothesis?
- What population and time window were searched?
- Which telemetry was available?
- Which query/version was run?
- What exclusions or filters were applied?
- What findings were reviewed?
- What limitations affect the result?

A screenshot of a dashboard rarely provides all of that.

### Separate scratch work from the official record

Personal notes can help an analyst think. The local standard decides what must become part of the authoritative hunt record.

The official record should preserve enough evidence and reasoning to support:
- review;
- hand-off;
- follow-on hunting;
- detection engineering;
- later lessons learned.

### Missing standard

Use:

> **Local hunt documentation standard not yet verified.**

Then identify the missing repository/form/process owner.

## 2. Knowledge Check

1. How does the 3.2.2 hunt card differ from the local official hunt record?
2. Name four things that support reproducibility.
3. What should you record if you do not know the authoritative hunt repository?

## 3. Summary

Document hunts where the organization says the authoritative record lives.

Preserve the hypothesis, scope, telemetry, query/evidence, findings, limitations, and version history required by the local standard.

**Next:** **3.7.3 – Hunt Outputs and Hand-off**.

## Reference Model

This module intentionally relies on the organization's local hunt documentation and records standard.
