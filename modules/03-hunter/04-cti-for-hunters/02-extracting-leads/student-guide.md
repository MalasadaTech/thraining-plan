# Module 3.4.2 – Extracting Hunt Leads from CTI

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.2 B / C / C ; 3.4.2.1–3.4.2.3 3c / 4c / 4d  
- SOC: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
- CTI: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Extract hunt-suitable procedures, behaviors, observables, and indicators from a CTI report.
2. Evaluate each candidate lead for provenance, applicability, distinctiveness, validity, and local visibility, then state the hunt question it supports.

## Mapped Proficiency Items

- K: 3.4.2 – Extracting hunt leads from CTI
- T: 3.4.2.1 – Extract hunt-suitable TTPs from a CTI report
- T: 3.4.2.2 – Extract hunt-suitable artifacts (IOCs, patterns, behaviors)
- T: 3.4.2.3 – State the hunt question those leads support

## 1. Key Concepts

A CTI report becomes hunt input only after the hunter translates it into **searchable local evidence**.

### What to extract

**Procedures / behaviors**
- Run-key persistence pointing into a user-writable path;
- encoded PowerShell spawned by a script interpreter;
- scheduled task creation with an unusual action;
- HTTP request to a campaign-specific path.

**Observables / indicators**
- hash;
- domain/IP/URL;
- filename/path;
- registry value;
- certificate;
- user-agent or protocol trait.

**Context**
- platform;
- time period;
- target population;
- parent/child relationship;
- expected role in the intrusion.

Context often determines whether the lead is useful.

### Evaluate each candidate lead

Ask:

1. **Provenance** – Where did the claim/value come from?
2. **Local applicability** – Can this exist in our environment?
3. **Distinctiveness** – Will it reduce normal activity to a reviewable set?
4. **Validity / timeliness** – Is the relationship still relevant to the question?
5. **Visibility** – Do we have telemetry that can test it?

### Old does not automatically mean expired

A SHA256 from 2019 does not become invalid merely because it is old. A file hash can remain useful for retrospective search indefinitely.

An indicator should be treated as expired/invalid when its source or context says its useful validity ended, ownership changed, the pattern no longer represents the threat, or a defined validity window ended.

Age affects priority and expected yield. It is not an automatic expiration rule.

### Missing telemetry is a gap, not a reason to erase the lead

If a report provides a strong persistence procedure but the environment lacks registry telemetry:

- keep the procedure as relevant intelligence;
- mark it **not currently executable as a hunt lead**;
- record the **visibility gap**.

That preserves the defensive requirement.

### A12 extraction

**Keep procedure**
> HKCU Run value `Updater` → `%TEMP%\update.exe`

**Keep observable**
> `GET /update.exe` to `203.0.113.88:8080`

**Keep context**
> Windows user workstations; incident time window

**Weak/broad candidate**
> Entire `203.0.113.0/24` without evidence of common control

**Hunt question**
> Are A12-related persistence or payload-delivery artifacts present on additional Windows user workstations during the scoped time window?

## 2. Knowledge Check

1. Why is a 2019 hash not automatically “expired”?
2. What should you do with a strong CTI procedure that is locally applicable but not observable with current telemetry?
3. From the A12 slice, give one procedure, one observable, and one hunt question.

## 3. Summary

Extract more than IOC lists. Preserve procedures, observables, and the context that makes them meaningful.

Evaluate leads for applicability, distinctiveness, validity, and visibility. If visibility is missing, record the gap rather than deleting the intelligence.

**Next:** **3.4.3 – STIX as Hunt Input**.
