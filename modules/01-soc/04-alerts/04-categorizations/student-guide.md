# Module 1.4.4 – Common Alert Categorizations

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.4.1 A / B / C ; 1.4.4.2 2b / 3c / 4c  
- Hunter: 1.4.4.1 B / C / C ; 1.4.4.2 2b / 3c / 4c  
- CTI: 1.4.4.1 A / A / A ; 1.4.4.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the syllabus categories: scanning / reconnaissance, root-level access, user-level access, unsuccessful activity, and **other** as your shop uses it.
2. Assign a category and **justify why it is not the adjacent category**.

**Mapped Proficiency Items:**
- K: 1.4.4.1 – Common alert categorizations
- T: 1.4.4.2 – Assign a category to an alert and justify why it is not the adjacent category

---

## 1. Key Concepts

SOC analysts put a **site bucket** on a working alert so the next desk can see what kind of activity it was. You pick one category and say why the **neighbor** is wrong. You do **not** re-argue TP vs FP (**1.4.2**). You do **not** name an FP cause (**1.4.3**). You do **not** write an ATT&CK ID as the category (**0.6**).

| Category | Use when | Adjacent — not this |
|----------|----------|---------------------|
| **Scanning / reconnaissance** | Wide, unauthenticated probing (many ports or hosts; no login or exploit attempt) | **Unsuccessful** — a failed login is an access *attempt*, not a sweep |
| **Root-level access** | SYSTEM, admin, or service-level control on the host | **User-level** — same command as a standard user token is not root |
| **User-level access** | Activity as a normal user token (Medium `jlee`) | **Root-level** — encoded or “looks like malware” does not upgrade the token |
| **Unsuccessful activity** | An access or exploit *attempt* that failed (denied logon; 401 burst on one app) | **Scanning** — failed auth is not a port sweep |
| **Other (your shop)** | A name your site already uses | Say the local name and which neighbor you rejected. Do not invent ATT&CK tactics as buckets |

The adjacent pairs are **scan ↔ unsuccessful** and **user ↔ root**. The task is two sentences: **category** and **not the neighbor because …**.

**What good looks like:**

- **User-level, not root:** Alert `Encoded PowerShell from script host`, `wscript` + `-enc` as Medium `jlee` (**1.4.1**). Category **user-level**. Not root: the token is a standard user. Encoded does not change the bucket. (Same command as **SYSTEM** after a service start would be **root**, not user.)
- **Scanning, not unsuccessful:** Given: many unanswered SYN to 150 ports in two minutes, no login. Category **scanning / reconnaissance**. Not unsuccessful: nothing was presented as credentials or an exploit — it is a sweep.

Do not invent a DYA category list here. If you need **other**, use a name your real shop already has.

---

## 2. Knowledge Check

1. This hour is for deciding TP vs FP. True or false?
2. Name the four syllabus categories plus **other**.
3. Alert: `wscript` + `-enc` as Medium `jlee`. Category, and why not the adjacent one?

---

## 3. Summary

Site bucket + rejected neighbor. Scan is not failed auth. User token is not root. Other is a name your shop already uses.

**Next:** **1.4.5** Service Level Agreements / Response Time Goals.

---

## 4. Related modules

- 1.4.3 – Common false positive causes (previous)
- 1.4.5 – SLA / response time goals
- 1.4.2 – Alert classification
- 0.6 – Frameworks (ATT&CK is not a category)
