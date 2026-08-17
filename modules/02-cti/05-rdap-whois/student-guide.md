# Module 2.5.1 – RDAP and WHOIS Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.1 B / C / C ; 2.5.1.1 3c / 4c / 4c  
- Hunter: 2.5.1 A / B / B ; 2.5.1.1 2b / 3c / 4c  
- SOC: 2.5.1 A / A / B ; 2.5.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what WHOIS and RDAP are for, and how they differ.
2. Query a domain or IP and extract fields that help enrichment — without calling redaction “no intel.”

**Mapped Proficiency Items:**
- K: 2.5.1 – RDAP and WHOIS concepts
- T: 2.5.1.1 – Query RDAP/WHOIS and interpret fields for enrichment or attribution

---

## 1. Key Concepts

CTI analysts pull **registration** so they can see registrar, nameservers, and created dates. You do **not** interpret SOA (**2.6**). You do **not** use Silent Push PDNS (**0.7**). You do **not** call a redacted registrant nation-state (**2.1.7**).

| Idea | Meaning |
|------|---------|
| **WHOIS** | Text registration record (legacy) |
| **RDAP** | Structured registration (JSON, same job, easier to parse) |
| **Useful fields** | Registrar, nameservers, created / updated, registrant *if present* |

**Redacted registrant is a fact.** It is not “no intel.” It is not a country.

**What good looks like:**

- **Query** the update domain. Extract: nameservers `ns1.cdn-test.net` / `ns2.cdn-test.net`, created date, registrar. Write **registrant redacted** if that is what the card shows.
- **Interpret:** distinctive NS is enrichment. It is **not** “this is a nation-state.” Sibling `login-prd.net` with the **same NS** is a later hop you can *name* — the SOA read is **2.6**.

---

## 2. Knowledge Check

1. A redacted registrant means you have no intelligence. True or false?
2. Name one difference between WHOIS and RDAP.
3. You query the update domain and see `ns1.cdn-test.net`. What did you extract, and what must you **not** claim?

---

## 3. Summary

RDAP/WHOIS is registration. Redacted is a fact. Distinctive NS is enrichment, not attribution.

**Next:** **2.6.1** Advanced DNS.

---

## 4. Related modules

- 2.4.1 – File similarity (previous)
- 2.6.1 – SOA / advanced DNS
- 0.7 – Silent Push survey
- 2.1.7 – Attribution
