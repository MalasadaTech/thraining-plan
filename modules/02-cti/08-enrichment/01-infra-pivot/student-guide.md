# Module 2.8.1 – Identifying Additional Adversary Infrastructure

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4d  
- Hunter: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4d  
- SOC: 2.8.1 A / B / B ; 2.8.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Write a **generic hop sentence** from a seed (what you share, what you found).
2. Name a common source class for that hop — without re-teaching RDAP, SOA, or Silent Push.

**Mapped Proficiency Items:**
- K: 2.8.1 – Identifying additional adversary infrastructure from seed indicators
- T: 2.8.1.1 – Pivot from a seed indicator to additional adversary infrastructure

---

## 1. Key Concepts

CTI analysts hop from a **seed** they already have to **candidate extra infra**. The DTF *ID line* is **2.7.4**. This hour is the **sentence** without a P-code. You do **not** re-teach RDAP (**2.5**), SOA (**2.6**), or Silent Push (**0.7** / **2.9.3**).

**Hop sentence:** `seed | shared characteristic | candidate | why not coincidence`

Sources you may *name*: registration, DNS, same A, TLS cert, HTTP title. You do not operate those tools here.

**What good looks like:**

- Seed = update domain / `203.0.113.88`. Shared NS `ns1.cdn-test.net` → candidate `login-prd.net`. Why not coincidence: distinctive NS pair, not a public resolver.
- **Reject:** whole `203.0.113.0/24` — shared hosting.

---

## 2. Knowledge Check

1. This hour you must write a DTF P-ID. True or false?
2. What four parts does a hop sentence have?
3. Write the hop from the update domain to `login-prd.net` (or reject /24).

---

## 3. Summary

Seed → shared thing → candidate → why not coincidence. Shared /24 is not a hop. No P-ID required.

**Next:** **2.8.2** Applicable TTPs.

---

## 4. Related modules

- 2.7.4 – DTF ID line (previous)
- 2.8.2 – Applicable TTPs
- 2.5 / 2.6 / 0.7 – Tools you name, not re-teach
