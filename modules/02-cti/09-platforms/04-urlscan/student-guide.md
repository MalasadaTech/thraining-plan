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

1. Say what URLScan records on **this page load**, and what you open it to see.
2. Retrieve a result (or treat a provided result as submitted) and extract what is on it — or write that it is missing.

**Mapped Proficiency Items:**
- K: 2.9.4 – URLScan
- T: 2.9.4.1 – Submit or retrieve a URLScan result and extract actionable intelligence

---

## 1. Key Concepts

You have a live URL — often the **update domain** from the RFI. You need to see **what that URL served** on this visit: the page title, the hosts and IPs it requested, the redirect chain. URLScan records that page load. That is the job in this lesson: retrieve a result and extract what is on it, so you do not invent a page or treat a screenshot as a finished judgment. When to pick URLScan instead of Silent Push or VirusTotal is **0.7**. This lesson is how to read the result.

URLScan visits a URL in a browser sandbox and records **this page load**. That is the capability. The use case is a live URL you already have, not a file to detonate and not a domain-history question.

This lesson uses a **classroom result card** — a provided scan result. You do not need a live URLScan account. **Retrieve** means you read an existing result for that URL. **Submit** means you send the URL so URLScan visits it and builds a new result. Retrieve is enough here. You do not submit from a live account in this lesson.

| Extract | What it is for |
|---------|----------------|
| **Page title / final URL** | What the visitor would have seen |
| **Requested hosts / IPs** | Extra infrastructure the page talked to (a hop is **2.8.1**) |
| **Redirect chain** | How the browser got from the submitted URL to the final page |

A **screenshot** of the page is **information** — what the page looked like. It is not a judgment by itself (**2.1.1**).

**What good looks like:** you are given the update-domain URL. You retrieve the classroom result card if there is one. You extract the title or a requested host **that the card shows**. If there is no result, you write **not on card**. You do not invent a login page. You do not write the hop sentence (**2.8.1**). You do not turn this into a SIEM or Zeek hunt (**3.3.1**).

- Given: a result card for the update URL with a title and a requested host. **Extract** those two. Stop.
- Given: no card for that URL. **Write:** not on card. Do not fill in `login-prd.net` as a page you did not see.

---

## 2. Knowledge Check

1. This lesson is “when to pick URLScan.” True or false?
2. Name two fields you extract from a URLScan result.
3. You have no card for the update URL. What do you write?

---

## 3. Summary

URLScan records what a URL served on this page load. Retrieve a result. Extract the title, requested hosts or IPs, and redirects that are on it — or write that it is missing. A screenshot is information. No live submit is required.

**Next:** **2.10.1** Core STIX objects.

---

## 4. Related modules

- 2.9.3 – Silent Push (previous)
- 2.10.1 – Core STIX objects
- 0.7 – When to pick URLScan
- 2.8.1 – Hop sentence
