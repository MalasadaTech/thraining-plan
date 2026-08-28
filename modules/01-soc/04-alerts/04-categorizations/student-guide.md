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

SOC analysts put a **category** on an alert so the next desk can see what kind of activity it was. A true-positive or false-positive label only says whether the detection was right. A category says whether this was a scan, a failed attempt, or access as a user versus as an administrator. You pick one name and say why the **adjacent category** — the neighbor people mix it up with — is wrong. You do **not** re-argue true positive versus false positive (**1.4.2**). You do **not** name a false-positive cause (**1.4.3**). You do **not** write an ATT&CK technique ID as the category (**0.6**).

| Category | Use when | Adjacent — not this |
|----------|----------|---------------------|
| **Scanning / reconnaissance** | Wide, unauthenticated probing (many ports or hosts; no login or exploit attempt) | **Unsuccessful** — a failed login is an access *attempt*, not a sweep |
| **Root-level access** | SYSTEM, admin, or service-level control on the host | **User-level** — the same command as a standard user is not root |
| **User-level access** | Activity as a normal user account (Windows Medium integrity — `jlee`) | **Root-level** — encoded or “looks like malware” does not upgrade the account |
| **Unsuccessful activity** | An access or exploit *attempt* that failed (denied logon; HTTP 401 burst on one app) | **Scanning** — failed authorization is not a port sweep |
| **Other (your shop)** | A name your site already uses | Say the local name and which neighbor you rejected. Do not invent ATT&CK tactics as categories |

The adjacent pairs are **scan ↔ unsuccessful** and **user ↔ root**. The task is two sentences: **category**, then **not the neighbor because …**.

**What good looks like:**

- **User-level, not root:** Alert `Encoded PowerShell from script host`, `wscript` + `-enc` as Medium `jlee` (**1.4.1**). Category **user-level**. Not root: the account is a standard user. Encoded does not change the category. (The same command as **SYSTEM** after a service start would be **root**, not user.)
- **Scanning, not unsuccessful:** Given: many unanswered SYN to 150 ports in two minutes, no login. Category **scanning / reconnaissance**. Not unsuccessful: nothing was presented as credentials or an exploit — it is a sweep.

Do not invent a DYA category list here. If you need **other**, use a name your real shop already has.

---

## 2. Knowledge Check

1. A category is the same thing as a true-positive or false-positive label. True or false?
2. Name the four syllabus categories plus **other**.
3. Alert: `wscript` + `-enc` as Medium `jlee`. Category, and why not the adjacent one?

---

## 3. Summary

A category names the kind of activity and rejects the neighbor. A scan is not failed authorization. A user account is not root. Other is a name your shop already uses.

**Next:** **1.4.5** Service Level Agreements / Response Time Goals.

---

## 4. Related modules

- 1.4.3 – Common false positive causes (previous)
- 1.4.5 – SLA / response time goals
- 1.4.2 – Alert classification
- 0.6 – Frameworks (ATT&CK is not a category)
