# Module 2.8.3 – IOC Handling and Enrichment Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.3 B / C / C ; 2.8.3.1 3c / 4c / 4d ; 2.8.3.2 3c / 4c / 4d  
- Hunter: 2.8.3 B / C / C ; 2.8.3.1 3c / 4c / 4d ; 2.8.3.2 1a / 2b / 3c  
- SOC: 2.8.3 A / B / B ; 2.8.3.1 1a / 2b / 3c ; 2.8.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Treat an IOC as an object you **keep, expire, enrich, or link** — not a TTP.
2. Name a tool/field to enrich, and say whether two IOCs are the **same activity set**.

**Mapped Proficiency Items:**
- K: 2.8.3 – IOC handling and enrichment concepts
- T: 2.8.3.1 – Enrich and pivot on IOCs using internal and external tools
- T: 2.8.3.2 – Link analysis and campaign tracking

---

## 1. Key Concepts

CTI analysts handle **observables**. A TTP is a behavior (**2.8.2**). This hour is the **object**. You do **not** re-teach VT or RDAP. You **select** the tool and say what you hope to learn. You do **not** fill Adversary with a vendor name (**2.7.2**).

| Rule | Meaning |
|------|---------|
| **Keep** | Cited, current, specific enough to hunt |
| **Expire** | Stale, uncited, or shared-infra noise (`203.0.113.0/24`) |
| **Enrich** | Name tool + field + what you hope to learn |
| **Link** | Same activity set if they share objects you can cite |

**What good looks like:**

- **Enrich:** hash of `invoice.vbs` → TIP first (**2.3.1**), then VT if still needed (**0.7**). Hope to learn: seen here before / reputation. Not Relations depth (**2.9.1**).
- **Link:** update domain + `203.0.113.88` + `login-prd.net` (same NS / same A) = **one set**. A random Example Cloud IP with no shared NS = **apart**. Reject “same group because the PDF said PRD APT.”

---

## 2. Knowledge Check

1. An IOC is the same thing as a TTP. True or false?
2. Name keep vs expire for a whole /24.
3. Update domain + sibling same NS — same set or apart, and why? What vendor name is **not** a link?

---

## 3. Summary

Keep cited current IOCs. Expire shared noise. Name the enrich. Link only on shared objects.

**Next:** **2.8.4** Relevance and impact.

---

## 4. Related modules

- 2.8.2 – Applicable TTPs (previous)
- 2.8.4 – Relevance / impact
- 2.3.1 / 0.7 / 2.9 – Tools you name
- 2.7.2 – Diamond / vendor name
