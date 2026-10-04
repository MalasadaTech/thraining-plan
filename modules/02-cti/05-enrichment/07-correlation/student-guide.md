# Module 2.5.7 – Correlation, Link Analysis, and Campaign Tracking

**Target Audience:** CTI Analyst (primary); Threat Hunter and SOC Analyst (supporting context)  
**Proficiency Focus:**  
- CTI: 2.5.7 B / C / C ; 2.5.7.1 3c / 4c / 4d  
- Hunter: 2.5.7 B / C / C ; 2.5.7.1 1a / 2b / 3c  
- SOC: 2.5.7 A / B / B ; 2.5.7.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Combine enrichment records into evidence-backed links while testing alternative explanations.
2. Distinguish a candidate relationship, an activity-set or campaign assessment, and actor attribution.

**Mapped Proficiency Items:**
- K: 2.5.7 – Correlation, link analysis, and campaign tracking
- T: 2.5.7.1 – Link analysis and campaign tracking

## 1. Key Concepts

Enrichment produces individual observations and candidate relationships. Correlation asks whether those findings form a coherent pattern; link analysis records the relationships and the evidence behind them. Campaign tracking adds a time-bounded assessment of related activity.

Bring forward the records from file, registration, DNS, infrastructure-pivoting, and DTF lessons. Keep each original source and observation time visible as you combine them.

### A link is a claim about a relationship

Useful evidence may include a distinctive infrastructure characteristic, matching malware configuration, certificate fingerprint, co-occurrence in an incident, or a repeated temporal pattern. A shared vendor tracking name is source context; it is not, by itself, technical evidence connecting two objects.

Record each proposed link as:

`object A | relationship | object B | source and observation time | supporting evidence | alternative explanation | assessment / next check`

Two tools repeating the same upstream report do not necessarily provide two independent confirmations. Check provenance before counting corroboration.

### Combine evidence at the strength it supports

For A12, the update domain and `login-prd.net` share an uncommon nameserver and an IP during an overlapping period. This supports a candidate infrastructure relationship. The shared fields should be evaluated together with hosting context and any independent registration, certificate, or behavioral evidence.

A busy shared cloud range remains a weak link. Similar files can support a separate file-family hypothesis, but similarity alone does not establish common infrastructure control. Record file and behavioral relationships alongside infrastructure relationships without forcing them into DTF, which remains infrastructure-focused.

| Evidence state | Defensible record |
|---|---|
| One shared field with unresolved common-provider explanation | Candidate link requiring further evaluation. |
| Several distinctive, time-relevant findings with documented sources | A stronger assessed relationship, with remaining limitations stated. |
| Evidence of coordinated activity against a common objective over time | A campaign hypothesis with its scope, basis, confidence, and competing explanations. |

The third conclusion requires activity evidence. A graph of related domains alone does not establish the campaign's objective or responsible actor.

### Maintain the assessment as evidence changes

Keep the activity-set or campaign label separate from actor attribution. Record what the label covers, the time window, supporting and contradicting evidence, and why the assessment changed. Revisit stale indicators through the lifecycle decisions in [2.5.1](../01-ioc-handling/student-guide.md).

When a relationship no longer holds, update the assessment without erasing the historical observation. Use [2.1.8 – Attribution](../../01-core-intel/08-attribution/student-guide.md) when evaluating a claim of actor identity, and carry the supported findings into the organizational assessment in 2.6.

## 2. Knowledge Check

1. Two reports repeat the same upstream nameserver finding. Do they provide two independent confirmations?
2. The A12 domains share a rare NS and time-overlapping IP. What can you record, and what would justify a stronger campaign claim?
3. A similar file and a domain share a vendor actor label. Is that sufficient to link them to the same actor?

## 3. Summary

Promote relationships only as far as the evidence supports. Keep candidate links, campaign assessments, and actor attribution distinct.

## Supporting References

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

**Next:** [2.6.1 – Extracting Applicable TTPs from Intelligence Reports](../../06-assessment/01-applicable-ttps/student-guide.md).
