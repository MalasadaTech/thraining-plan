# Module 2.11.1 – Creating Finished Intelligence Products

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.11.1 B / C / C ; 2.11.1.1 3c / 4c / 4d ; 2.11.1.2 3c / 4c / 4d  
- Hunter: 2.11.1 A / B / B ; 2.11.1.1 1a / 2b / 3c ; 2.11.1.2 1a / 2b / 3c  
- SOC: 2.11.1 A / A / B ; 2.11.1.1 1a / 1a / 2b ; 2.11.1.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name what a **finished product** must contain, and evaluate a draft against those standards.
2. Produce a short **actor / activity profile** that does not invent a nation-state.

**Mapped Proficiency Items:**
- K: 2.11.1 – Creating finished intelligence products
- T: 2.11.1.1 – Draft a finished product and evaluate it against standards
- T: 2.11.1.2 – Produce a threat actor profile

---

## 1. Key Concepts

CTI analysts ship a **finished product** — the judged answer, not a TIP paste. Audience rewrite floor is **2.1.6**. Attribution assessment is **2.1.7**. STIX is **2.10**. SOC ticket types are **1.5**. Local approval is **2.12**.

| Need | Meaning |
|------|---------|
| **Types** | Assessment, profile, RFI response — pick one |
| **Structure** | Question, what you know, judgment, so-what, confidence / caveat |
| **Standards** | Answers the requirement; sourced; estimative term; no invented country |

**What good looks like:**

- **Draft (A12):** Requirement = payload host *here*? Judgment = **likely** the update domain is. So-what = IR has **WS-JLEE**. Confidence = medium. Sources = Zeek A + host file. That **passes**. A hash dump **fails**.
- **Profile:** activity cluster (encoded PS, update domain, sibling NS). **Not** “nation-state PRD APT.” Vendor name stays a label.

---

## 2. Knowledge Check

1. A TIP paste is a finished product. True or false?
2. Name three required elements of a finished product.
3. Write a three-line **A12** profile that does **not** claim a country.

---

## 3. Summary

Question, judgment, so-what, caveat. Profile the cluster. Do not invent a government.

**Next:** **2.11.2** Dissemination.

---

## 4. Related modules

- 2.10.2 – STIX production (previous)
- 2.11.2 – Dissemination
- 2.1.6 / 2.1.7 – Audience / attribution
- 2.12 – Local approval
