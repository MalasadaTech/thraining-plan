# Module 3.4.3 – STIX as Hunt Input

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.3 B / C / C ; 3.4.3.1 3c / 4c / 4c ; 3.4.3.2 3c / 4c / 4d  
- SOC: 3.4.3 A / A / B ; 3.4.3.1 1a / 1a / 2b ; 3.4.3.2 1a / 1a / 2b  
- CTI: 3.4.3 A / B / B ; 3.4.3.1 1a / 2b / 3c ; 3.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Identify STIX objects and references that can supply hunt-relevant evidence.
2. Convert STIX content into a local hunt lead without assuming that every object—or every object in the same Bundle—is directly searchable.

## Mapped Proficiency Items

- K: 3.4.3 – STIX as hunt input
- T: 3.4.3.1 – Identify hunt-relevant objects in a report or bundle
- T: 3.4.3.2 – Turn those objects into hunt leads

## 1. Key Concepts

STIX gives CTI a structured way to represent threat and observable information. Hunters consume that structure; they do not need to author it in this lesson.

Reference: [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### Objects with direct hunt value

| STIX content | Hunt use |
|---|---|
| **Indicator** | Parse the pattern into observable fields/values that local telemetry can search. Check validity and context. |
| **Observed Data + referenced SCOs** | Identify the file, IP, domain, process, registry key, or other observable that was actually recorded. |
| **Attack Pattern** | Use the named behavior as a hunt seed when locally applicable and visible. |
| **Sighting** | Understand that an SDO was reported as seen; inspect `observed_data_refs` and where it was sighted when available. |
| **Relationship** | Preserve why objects are connected (`indicates`, `uses`, `based-on`, etc.) so the lead keeps its analytic context. |

### Context objects are useful without being direct queries

**Malware**, **Threat Actor**, **Intrusion Set**, and **Campaign** can help prioritize or group a hunt, but the object name itself may not be searchable in local telemetry.

A STIX Malware object does **not inherently contain a file hash**. File hashes are represented through cyber-observable objects or Indicator patterns/observations linked to the malware.

That distinction prevents a hunter from expecting every `malware` object to produce an IOC automatically.

### Bundle membership has no semantic meaning

Two objects are not related merely because they appear in the same STIX Bundle.

Use explicit Relationships, Sightings, embedded references, and object properties to understand the graph.

### A12 example

Suppose a classroom package contains:

- `indicator` pattern for `203.0.113.88`;
- `attack-pattern` for T1547.001;
- `observed-data` referencing a File and Process;
- `relationship` tying the Indicator to Malware;
- a `sighting` with supporting Observed Data.

A hunter can derive:

> Search internal network telemetry for the IP during the relevant window, and search registry/file telemetry for the T1547.001 procedure described by the related report/observations.

The actor or malware name can help prioritize the search. The actual local query comes from the observable pattern and behavior.

## 2. Knowledge Check

1. Why does a STIX Malware object not automatically give you a file hash?
2. Which STIX object is most likely to contain a machine-readable detection pattern?
3. Why should a hunter inspect Relationships rather than assume objects in the same Bundle are connected?

## 3. Summary

Use STIX structure to preserve **what the lead is and why it is related**.

Indicator patterns and observed cyber-observables often provide direct query material. Attack Patterns provide behavior. Context objects provide scope and priority.

**Next:** **3.5.1 – Using MITRE ATT&CK for Hunt Planning**.

## Supporting Reference

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
