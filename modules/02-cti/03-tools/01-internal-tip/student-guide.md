# Module 2.3.1 – Internal Threat Intelligence Platform

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.3.1 B / C / C ; 2.3.1.1 3c / 4c / 4d  
- Hunter: 2.3.1 A / B / B ; 2.3.1.1 1a / 2b / 3c  
- SOC: 2.3.1 A / A / B ; 2.3.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what the internal TIP is for, and what it is **not**.
2. Search, retrieve, and use it to support enrichment or analysis of an indicator you already have.

**Mapped Proficiency Items:**
- K: 2.3.1 – Internal threat intelligence platform
- T: 2.3.1.1 – Search, retrieve, and use the internal TIP for enrichment or analysis

---

## 1. Key Concepts

CTI analysts look up **what this shop already holds** before they open a public tool. The TIP is the **intel store**. You do **not** re-teach VirusTotal (**0.7** / **2.9**). You do **not** author STIX (**2.10**). You do **not** invent a Harbor URL as policy. If your shop has a real TIP, use those screens.

| Function | Job |
|----------|-----|
| **Store** | Indicators, reports, sightings, cluster labels *we* already have |
| **Search / retrieve** | Find what we already know about a hash, IP, or domain |
| **Link** | Attach a new sighting to an existing object — or record **not in TIP** |

**What good looks like:**

- **Search:** the update domain or the hash of Temp `invoice.vbs` (**A12**). Write what you **retrieved** (a prior sighting, a cluster label) or **not in TIP**.
- **Use:** if a prior object exists, **link** this RFI as a sighting. If not, say the TIP added nothing. Do not invent a hit.

A TIP miss is a gap, not “benign.”

---

## 2. Knowledge Check

1. The internal TIP is the same as VirusTotal. True or false?
2. Name two core TIP jobs.
3. You search the update domain for **A12**. What two results can you write, and what must you **not** invent?

---

## 3. Summary

Search what we already hold. Retrieve it or say it is missing. Link a sighting. Do not invent a hit.

**Next:** **2.4.1** File similarity hashes.

---

## 4. Related modules

- 2.2.4 – Cognitive biases (previous)
- 2.4.1 – File similarity
- 0.7 / 2.9 – External tools / Relations
- 2.10 – STIX authoring
