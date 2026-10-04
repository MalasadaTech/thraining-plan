# Instructor Guide – Module 2.7.1 – Core STIX Objects

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- Hunter: 2.7.1 B / C / C ; 2.7.1.1 2b / 3c / 4c  
- SOC: 2.7.1 A / B / B ; 2.7.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview

**Purpose:** Give learners a practical STIX vocabulary before they build relationships or exchange objects.

Reference: [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### Important framing

The eleven types in the lesson are a **selected course subset**.

Do not tell learners that STIX 2.1 contains only eleven types. STIX also defines Infrastructure, Tool, Vulnerability, Report, Note, Incident, Location, Grouping, Malware Analysis, and other objects.

The goal is recognition of the types this curriculum uses most often.

## Learning Objectives

1. Recognize the eleven STIX 2.1 object types selected for this course.
2. Label report facts with the most appropriate course type while respecting evidence limits.

## Suggested Timing

| Part | Time |
|---|---:|
| STIX model overview | 3 min |
| Eleven course objects | 8 min |
| Indicator / SCO / Observed Data | 5 min |
| Identity / Threat Actor / Intrusion Set | 4 min |
| Knowledge check | 4 min |

## Detailed Teaching Notes

### Indicator vs observable vs Observed Data

This is the most important correction to the older lesson.

Do not teach “hash seen = Observed Data” as if the hash itself were the Observed Data object.

Teach the layers:

1. **File SCO** contains the file/hash.
2. **Observed Data** records that the observable was seen.
3. **Indicator** contains a detection pattern.

Reference: [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### Sighting

Sighting states that an SDO was seen.

It may reference:
- the sighted SDO;
- Observed Data describing what was actually observed;
- Identity/Location for where or by whom it was seen.

### Identity

Identity is neutral. The STIX open vocabulary includes `system`, so a host can be represented as a system Identity when that modeling choice is useful.

### Vendor names

A provider tracking label is source context, not automatic object typing.

Ask:
- Is this a real-world malicious entity?
- Is this better modeled as an Intrusion Set/activity cluster?
- Is the evidence too weak to create either?

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| “STIX has only these eleven types.” | Call them the course subset and point to the standard. |
| Raw IP/hash = Indicator. | Ask whether there is a detection pattern or merely an observable value. |
| Observed Data = the raw file. | Explain SCO versus observation container. |
| Victim Identity = Threat Actor. | Identity is neutral. |
| Tracking name = known actor. | Preserve provenance and avoid stronger object typing than the evidence supports. |

## Knowledge Check – Answer Key

1. No. The lesson covers a selected working set.
2. File SCO = raw observable; Observed Data = observation record; Indicator = detection pattern.
3. A vendor tracking name may represent a provider-defined cluster, alias, or attribution claim; object selection should reflect the underlying evidence.

## References

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
- [STIX 2.1 Interoperability Test Document](https://docs.oasis-open.org/cti/stix-2.1-interop/v1.0/stix-2.1-interop-v1.0.html)
