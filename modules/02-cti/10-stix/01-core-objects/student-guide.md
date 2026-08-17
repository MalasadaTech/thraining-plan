# Module 2.10.1 – Core STIX Objects

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.10.1 B / C / C ; 2.10.1.1 3c / 4c / 4c  
- Hunter: 2.10.1 B / C / C ; 2.10.1.1 2b / 3c / 4c  
- SOC: 2.10.1 A / B / B ; 2.10.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the common **STIX 2.1** objects on the syllabus.
2. Label those objects in a classroom report or bundle — do not invent types.

**Mapped Proficiency Items:**
- K: 2.10.1 – Core STIX objects
- T: 2.10.1.1 – Identify and label common STIX objects in a report

---

## 1. Key Concepts

CTI analysts label **what kind of object** they are sharing. Hunt *reads* STIX as input later (**3.4.3**). Finished narrative is **2.11**. TIP retrieve is **2.3.1**. This hour is **identify**. Classroom bundle only. Do not stand up TAXII (**2.10.2**).

Syllabus objects (STIX **2.1** — the spec, not a hunt ID): Indicator · Observed Data · Malware · Attack Pattern · Threat Actor · Intrusion Set · Campaign · Course of Action · Identity · Relationship · Sighting.

**What good looks like:**

- Hash of `invoice.vbs` = **Indicator** (or Observed Data if it is a raw observation).
- Encoded PowerShell / T1059.001 = **Attack Pattern**.
- **WS-JLEE** / DYA = **Identity** (victim), not Threat Actor.
- “PRD APT” on a PDF = **not** automatically Threat Actor — that is a label (**2.1.7**).
- A row that ties indicator to identity = **Relationship** or **Sighting**.

---

## 2. Knowledge Check

1. You may invent a STIX type if none fits. True or false?
2. Name four syllabus STIX objects.
3. Hash of `invoice.vbs` vs **WS-JLEE** — which two objects?

---

## 3. Summary

Real STIX 2.1 types only. Label the object. A vendor name is not automatically Threat Actor.

**Next:** **2.10.2** STIX in production.

---

## 4. Related modules

- 2.9.4 – URLScan (previous)
- 2.10.2 – STIX production / TAXII
- 2.3.1 – TIP retrieve
- 3.4.3 – Hunt STIX input
