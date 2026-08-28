# Module 3.4.3 – STIX as Hunt Input

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.3 B / C / C ; 3.4.3.1 3c / 4c / 4c ; 3.4.3.2 3c / 4c / 4d  
- SOC: 3.4.3 A / A / B ; 3.4.3.1 1a / 1a / 2b ; 3.4.3.2 1a / 1a / 2b  
- CTI: 3.4.3 A / B / B ; 3.4.3.1 1a / 2b / 3c ; 3.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the STIX objects a hunter actually uses in a report or bundle.
2. Turn those objects into hunt leads — you do **not** author STIX here.

**Mapped Proficiency Items:**
- K: 3.4.3 – STIX as hunt input
- T: 3.4.3.1 – Identify hunt-relevant objects in a report or bundle
- T: 3.4.3.2 – Turn those objects into hunt leads

---

## 1. Key Concepts

Hunters read CTI that arrives as a **report** or as a **STIX** package. **STIX** (Structured Threat Information Expression) is the language CTI uses to label threat facts as objects. Version **2.1** is the spec this course uses. A **bundle** is a wrapper that carries those objects as one package. Structured JSON looks official. It is not automatically a hunt. Your job is to name the objects that can actually drive a search, then turn those objects into a hunt question that can fail. That is the job in this lesson.

You do **not** author, validate, or share STIX here (**2.10**). Extracting leads from prose is **3.4.2**. Mapping this hunt onto ATT&CK is **3.5**. Classroom bundle only. Do not stand up a TAXII server.

These are the objects a hunter actually uses. The name in the first column is the STIX **2.1** `type` you see in the bundle.

| Object | Hunt-relevant when |
|--------|--------------------|
| **indicator** | It is a current pattern you can query (hash, host, IP, URL) |
| **attack-pattern** | It names a method specific enough to search, and you have telemetry |
| **observed-data** | It is a recorded sample that still names something searchable |
| **malware** | It gives a current hash or named installer — not the family slogan |
| **threat-actor** / **intrusion-set** | It is a scope or priority hook. It is not a search by itself |
| **relationship** | It ties the other objects together (`indicates`, `uses`) |

**Campaign**, **course-of-action**, **identity**, and **sighting** exist in STIX **2.1**. Hunters may see them in a bundle. They are not the objects this lesson asks you to use as hunt input.

A bundle **seeds** a hunt when the objects you pick can support a question that can fail. An actor name is not a search. Dumping every IPv4 **indicator** into a block list is not a seed.

**What good looks like:** someone gives you a classroom bundle for incident **A12**. You name the hunt-relevant objects. You write the lead. You do not write STIX.

- **Identify:** `indicator` for `GET /update.exe` to `203.0.113.88:8080`; `attack-pattern` for HKCU Run **`Updater`**; `relationship` `uses`.
- **Seed:** if more persistors exist, we see that Run value or that URI.
- **Not a seed:** dump every IPv4 `indicator` into a block list.

Do not author the bundle (**2.10**). Do not open Navigator (**3.5**).

---

## 2. Knowledge Check

1. Hunters author STIX in this lesson. True or false?
2. Name four objects a hunter actually uses.
3. A classroom bundle has an `indicator` for `GET /update.exe` on `203.0.113.88:8080` and an `attack-pattern` for HKCU Run **`Updater`**. Name one hunt-relevant object and the lead it seeds.

---

## 3. Summary

Identify hunt-relevant STIX objects. Seed a question that can fail. Do not author STIX. Structured JSON is not automatically a hunt.

**Next:** **3.5.1** ATT&CK for hunt planning.

---

## 4. Related modules

- 3.4.2 – Extract leads (previous)
- 3.5.1 – ATT&CK map
- 2.10.1 – STIX types (label)
- 2.10.2 – STIX production (author / TAXII)
