# Module 2.9.4 – URLScan

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.4 B / C / C ; 2.9.4.1 3c / 4c / 4c  
- Hunter: 2.9.4 A / B / B ; 2.9.4.1 2b / 3c / 4c  
- SOC: 2.9.4 A / A / B ; 2.9.4.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what URLScan is for (what a URL served).
2. Retrieve (or treat as submitted) a result and extract intel **on the card**.

**Mapped Proficiency Items:**
- K: 2.9.4 – URLScan
- T: 2.9.4.1 – Submit or retrieve a URLScan result and extract actionable intelligence

---

## 1. Key Concepts

CTI analysts use URLScan to see **what a URL served** (title, requests, IPs, redirects). When to pick it is **0.7**. This hour is **retrieve / read**. Card only. No live submit required.

| Extract | Use |
|---------|-----|
| Page title / final URL | What the victim would have seen |
| Requested hosts / IPs | Extra infra to hop (**2.8.1**) |
| Redirect chain | How they got there |

**What good looks like:** retrieve a card for the update URL if you have one. Extract title / requested host **on the card**. Or **not on card**. Do not invent a login page. A screenshot alone is **information**.

---

## 2. Knowledge Check

1. This hour is “when to pick URLScan.” True or false?
2. Name two fields you extract from a result.
3. You have no card for the update URL. What do you write?

---

## 3. Summary

What the URL served. Extract from the card or say missing. No live submit required.

**Next:** **2.10.1** Core STIX objects.

---

## 4. Related modules

- 2.9.3 – Silent Push (previous)
- 2.10.1 – STIX objects
- 0.7 – When to pick URLScan
- 2.8.1 – Hop sentence
