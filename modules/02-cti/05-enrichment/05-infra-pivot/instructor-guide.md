# Instructor Guide – Module 2.5.5 – Identifying Additional Adversary Infrastructure from Seed Indicators

**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Purpose

Teach learners to turn a shared infrastructure characteristic into a **candidate relationship** and record the reasoning in a concise hop sentence.

This lesson establishes the reasoning used in an infrastructure pivot. Learners preserve the hop record for 2.5.6, where they will add DTF classifications and a framework-guided next lookup.

Reference: [Defender's ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework).

## Learning Objectives

1. Pivot from a known seed to a candidate infrastructure object and write the four-part hop sentence.
2. Judge whether the characteristic is distinctive enough to pursue and identify the source class for the next enrichment step.

## Suggested Timing

| Part | Time |
|---|---:|
| Seed and candidate | 4 min |
| Hop sentence | 5 min |
| Distinctiveness | 6 min |
| A12 walkthrough | 5 min |
| Knowledge check | 4 min |

## Detailed Teaching Notes

### Start with candidate language

A shared value should normally produce:

> candidate related infrastructure

—not—

> confirmed sibling / adversary-owned infrastructure.

Ask what an unrelated tenant could also share.

### Teach distinctiveness

Compare:
- same Cloudflare nameserver;
- same rare self-hosted nameserver pair;
- same shared-cloud IP;
- same rare NS pair plus same IP plus similar registration timing.

The second and fourth cases deserve more weight because coincidence is less plausible.

### Keep the hop separate from the tool

The learner should name the source class or next lookup without turning the lesson into RDAP, passive-DNS, or certificate-tool instruction.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Treats a pivot as proof. | Ask what alternative explanation could produce the shared value. |
| Takes an entire cloud `/24`. | Ask whether the hosting range is shared by unrelated tenants. |
| Adds DTF IDs. | Remind them that 2.5.6 adds PTA/P notation to this same record. |
| Lets tool navigation replace reasoning. | Use the paired walkthrough to produce a hop sentence and a testable next question. |

## Knowledge Check – Answer Key

1. Seed, shared characteristic, candidate, why the relationship is worth pursuing.
2. No. A common provider is weak by itself. Add distinctive shared features, timing, or corroborating records.
3. A broad shared range has a high coincidence rate; multiple distinctive shared features provide a narrower, more discriminating relationship.

## References

- [Defender's ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework)
- [ICANN RDAP guidance](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en)
- [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html)

## Paired application

Complete the application portion of 2.4.5 and 2.4.6 with this lesson. Use the retained DNS result and a supplied browser-scan result to propose one infrastructure hop. Separate page-controlled or distinctive features from common third-party services. Record the seed, shared characteristic, candidate, reason to pursue, and next lookup. Use the existing platform-guide answer key for its knowledge check. Account for the remaining platform time separately from this method lesson; do not repeat the orientation.
