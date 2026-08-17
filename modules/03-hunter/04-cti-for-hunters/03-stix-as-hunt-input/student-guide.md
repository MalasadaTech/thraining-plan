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

You **read** STIX after the **3.4.1** gate. How to **author** STIX is **2.10**. Keep / drop rules are still **3.4.2**. This hour is **identify, then seed**. Classroom bundle only. Do not stand up TAXII.

| Object | Hunt-relevant when |
|--------|--------------------|
| **indicator** | Current pattern you can query (hash, host, IP, URL) |
| **attack-pattern** | A method specific enough to search, and you have telemetry |
| **observed-data** | A recorded sample that still names something searchable |
| **malware** | A current hash or named installer — not the family slogan |
| **threat-actor** / **intrusion-set** | Scope or priority hook. Not a search by itself |
| **relationship** | Ties leftovers together (`indicates`, `uses`) |

Campaign, course-of-action, identity, and sighting exist in STIX **2.1**. Hunters may see them. They are **not** the sign-off objects this hour.

A bundle **seeds** a hunt when objects → leftovers → a question that can fail. Structured JSON is not automatically a hunt.

**What good looks like:**

- **Identify:** `indicator` for `:8080` `/update.exe`; `attack-pattern` for HKCU Run **`Updater`**; `relationship` `uses`.
- **Seed:** if more persistors exist, we see that Run value or that URI.
- **Not a seed:** dump every IPv4 `indicator` into a block list.

---

## 2. Knowledge Check

1. Hunters author STIX in this hour. True or false?
2. Name four objects a hunter actually uses.
3. From the A12 bundle, name one hunt-relevant object and the lead it seeds.

---

## 3. Summary

Identify hunt-relevant STIX objects. Seed a question. Do not author.

**Next:** **3.5.1** ATT&CK for hunt planning.

---

## 4. Related modules

- 3.4.2 – Extract leads (previous)
- 3.5.1 – ATT&CK map
- 2.10.1 – STIX types (author / label)
