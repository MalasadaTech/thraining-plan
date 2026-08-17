# Module 3.10.1 – Core STIX Objects

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.10.1 A / B / B · 3.10.1.1 1a / 1a / 2b  
- Hunter: 3.10.1 B / C / C · 3.10.1.1 2b / 3c / 4c  
- CTI: 3.10.1 B / C / C · 3.10.1.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the **eleven** core STIX 2.1 objects this hour signs off.
2. **Label** a span in a report with the correct type.
3. **Reject** the neighbor type (especially Indicator vs Observed Data, Attack Pattern vs Campaign, vendor name vs Threat Actor).
4. Leave hunt-lead extract and bundle authoring for their own hours.

**Mapped Proficiency Items:**
- K: 3.10.1 – Core STIX objects
- T: 3.10.1.1 – Identify and label common STIX objects in a report

---

## 1. Key Concepts

**2.4.3** taught which objects a *hunter* keeps. This hour is the **full inventory** for CTI production: label what the report *is*, not whether it is hunt-worthy. Linking, validating, and TAXII are **3.10.2**. A finished narrative product is **3.11**.

Use **real STIX 2.1 types**. Do not invent `apt-group` or `ioc`.

**Classroom type card (lesson-only properties — not a JSON schema dump):**

| Type | Question | Night Owl fill | Neighbor to reject |
|------|----------|----------------|--------------------|
| **indicator** | Pattern to *look for* later | `[domain-name:value = 'nightowl-updates.net']` | The Zeek *row* you already saw |
| **observed-data** | What was *seen* (a sample) | HTTP GET `update.exe` :8080 on WS-JLEE | The reusable detection pattern |
| **malware** | Family or sample | `update.exe` / `invoice.vbs` | The domain it called |
| **attack-pattern** | *How* (technique) | T1059.001 encoded PowerShell | A campaign name |
| **threat-actor** | Who is directing this | **Empty** unless *this* report earns a who | Vendor “Night Owl APT” |
| **intrusion-set** | Named activity set | Classroom cluster only if you say it is *unattributed* | Nation-state (**3.1.7**) |
| **campaign** | A time-bounded operation | Empty unless the report names one | One technique |
| **course-of-action** | What defenders should *do* | Block `nightowl-updates.net` at `fw-edge-01` | The sighting itself |
| **identity** | Who/what was acted on | Harbor / `BUILDINGC\jlee` | The malware sample |
| **relationship** | Link between two objects | Exists; you **draw** it in **3.10.2** | A type name used as a fact |
| **sighting** | Someone *saw* an object | WS-JLEE sighted the domain indicator | The indicator pattern itself |

**Label line:**  
`span | STIX type | not the neighbor because`

| This lesson | Other |
|-------------|-------|
| Label all eleven | Hunt-relevant slice only — **2.4.3** |
| Not draw the graph | **3.10.2** |
| Not write the narrative product | **3.11** |
| Not fill Adversary from a vendor name | **3.7.2** / **3.1.7** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Domain pattern = indicator | Zeek row labeled indicator |
| T1059.001 = attack-pattern | T1059.001 = campaign |
| Vendor APT ≠ threat-actor | Empty threat-actor treated as a fail |

---

## 2. Detailed Walkthrough / Examples

**Classroom report excerpt (Night Owl):**

> WS-JLEE launched `wscript` then `powershell -enc`. HKCU Run `Updater` → `%TEMP%\update.exe`. Zeek HTTP GET `update.exe` on 8080 to `nightowl-updates.net`. Vendor PDF calls the cluster “Night Owl APT” and lists T1486. No encryption was observed here.

### Example 1: Four Honest Labels (Expected)

| Span | Type | Not |
|------|------|-----|
| `nightowl-updates.net` as a *look-for* | **indicator** | observed-data — that is the GET *row* |
| The GET row on WS-JLEE | **observed-data** | indicator |
| `update.exe` | **malware** | indicator (the hash *pattern* would be) |
| `powershell -enc` / T1059.001 | **attack-pattern** | campaign |

### Example 2: Vendor APT as Threat Actor (Lead)

**Draft:** Threat Actor = Night Owl APT (nation-state).

**Fail.** Same empty-Adversary rule as **3.7.2**. Label **threat-actor** only if *this* report earns a who.  
**Lead:** Vendor cluster name is not a STIX type fill.

### Example 3: Sighting vs Indicator (Lead)

**Draft:** “WS-JLEE saw the domain” = another **indicator**.

**Fail.** The pattern is the indicator. The *seeing* is a **sighting**.  
**Lead:** Neighbor types.

---

## 3. Hands-On Exercise

**Objective:** Label spans. Reject neighbor types and vendor-name Threat Actor.

**Use only real STIX 2.1 types from the card.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Label** (task): write a **label line** for each.

   - A. Domain `nightowl-updates.net` as something to query later.  
   - B. The Zeek GET row.  
   - C. Vendor sentence “Night Owl is a nation-state APT.”  
   - D. T1059.001 / encoded PowerShell.  
   - E. “WS-JLEE was seen using that domain.”  
   - F. “Block `nightowl-updates.net` on `fw-edge-01`.”  
   - G. `BUILDINGC\jlee` as the user acted on.

3. Do not draw relationships (**3.10.2**). Do not write hunt leads (**2.4.3**). Do not write a **3.11** product. Do not invent types.
4. Empty **threat-actor** / **campaign** is allowed.

**Expected Outcome:**
- Three example summaries
- Seven label lines (C = no threat-actor)
- No graph, no hunt card, no narrative product

---

## 4. Knowledge Check

1. What is the difference between an **indicator** and **observed-data**?
2. When is **threat-actor** allowed to be empty?
3. Why is T1059.001 not a **campaign**?
4. What is a **sighting** pointing *at*?
5. Where do you **link** these objects into a scenario?

---

## 5. Summary

- Eleven real types. Label the span. Reject the neighbor. Empty who is honest.
- Next: **3.10.2** STIX in production (relationships, validate, TAXII).

---

## 6. References & Further Reading

- Related modules:
  - 3.9.4 – URLScan (previous unit)
  - 2.4.3 – STIX as hunt input
  - 3.10.2 – STIX production (next)
  - 3.11 – Finished intelligence products
- STIX 2.1 object types (lookup — do not invent cells)
- Classroom type card in this guide (lesson-only)
