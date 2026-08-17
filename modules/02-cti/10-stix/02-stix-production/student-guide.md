# Module 2.10.2 – How STIX Objects Are Used in Intelligence Production

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.10.2 B / C / C ; 2.10.2.1 3c / 4c / 4d ; 2.10.2.2 3c / 4c / 4d ; 2.10.2.3 3c / 4c / 4c  
- Hunter: 2.10.2 B / C / C ; 2.10.2.1 2b / 3c / 4c ; 2.10.2.2 2b / 3c / 4c ; 2.10.2.3 2b / 3c / 4c  
- SOC: 2.10.2 A / B / B ; 2.10.2.1 1a / 1a / 2b ; 2.10.2.2 1a / 1a / 2b ; 2.10.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Link syllabus objects with a real **relationship** type and explain the **A12** scenario those objects represent.
2. Say what **create / validate** and **TAXII consume** look like — classroom bundle only; no server.

**Mapped Proficiency Items:**
- K: 2.10.2 – How STIX objects are used in intelligence production
- T: 2.10.2.1 – Create STIX-aligned relationships and explain a threat scenario
- T: 2.10.2.2 – Create and validate STIX objects
- T: 2.10.2.3 – Use TAXII for sharing and consumption of intelligence

---

## 1. Key Concepts

CTI analysts **connect** objects so a machine (and hunt) can reuse the same story. Object *names* are **2.10.1**. The narrative product is **2.11**. This hour is **links + a valid classroom object + consume**. Do not invent relationship types. Do not stand up a TAXII server.

**Relationship (real types):** `indicates`, `based-on`, `targets`, `uses`, `related-to`, `sighting-of`.  
Example: Indicator (hash) **indicates** Attack Pattern (T1059.001). Sighting **sighting-of** that Indicator on Identity **WS-JLEE**.

**Create / validate:** required fields present (type, id, spec_version `2.1`, created). Invalid = missing type or invented type.

**TAXII:** a **collection** you consume (pull a classroom bundle). You do not run the server.

**What good looks like:** three objects + two real relationships that retell **A12**. Then: “I would pull collection X” — not “I stood up TAXII.”

---

## 2. Knowledge Check

1. You should stand up a TAXII server in this hour. True or false?
2. Name two real relationship types.
3. Write one relationship that ties the `invoice.vbs` hash to **WS-JLEE**.

---

## 3. Summary

Real relationship types. A classroom object must validate. TAXII is consume, not a server you build.

**Next:** **2.11.1** Finished intelligence products.

---

## 4. Related modules

- 2.10.1 – Core objects (previous)
- 2.11.1 – Finished products
- 2.3.1 – TIP
- 3.4.3 – Hunt STIX input
