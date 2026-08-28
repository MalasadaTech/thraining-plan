# Module 2.9.4 – URLScan  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.9.4 – URLScan  
**Subtitle:** What a URL served on this page load  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
2.9.3 was Silent Push. This lesson is URLScan: retrieve a result and extract what is on it. It is not the 0.7 survey and not a live submit.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

You have a live URL. You need to see **what that URL served**.

URLScan records **this page load**. This lesson is retrieve and read.

When to pick URLScan is **0.7**.

**Speaker Notes:**  
This slide is the student intro. They already know when to pick URLScan. Today they read a result so they do not invent a page. Do not re-teach the four-tool survey.

---

### Slide 3 – What URLScan records
**Title:** This page load

URLScan visits the URL and records **this page load**.

**Retrieve** — read an existing result.  
**Submit** — send the URL so URLScan visits it.

This lesson uses a **classroom result card**. Retrieve is enough. No live account.

**Speaker Notes:**  
Name retrieve and submit so the task is complete. Do not walk a live submit. If they ask about public scans or alerting the site operator, say that is why this classroom does not submit.

---

### Slide 4 – What you extract
**Title:** Title, requests, redirects

**Page title / final URL** — what the visitor would have seen.  
**Requested hosts / IPs** — extra infrastructure the page talked to.  
**Redirect chain** — how the browser got there.

A **screenshot** is **information**, not a judgment.

**Speaker Notes:**  
Those three fields are the extract. A hop from a requested host is 2.8.1 — extract the host, do not write the hop sentence. Screenshot is the 2.1.1 layer, not a recap of that lesson.

---

### Slide 5 – Extract or say missing
**Title:** Extract or say missing

Given a result card for the update URL: extract the title or requested host **on the card**.

Given no card: write **not on card**. Do not invent a login page.

**Speaker Notes:**  
Walk the two givens before the knowledge check. Fail `login-prd.net` as a page they did not see. That name was a Silent Push hop, not a URLScan result unless the card shows it.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. This lesson is “when to pick URLScan.” True or false?  
2. Name two fields you extract from a URLScan result.  
3. You have no card for the update URL. What do you write?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

URLScan records what a URL served on this page load.  
Retrieve a result. Extract what is on it, or write that it is missing.  
A screenshot is information. No live submit.

**Next:** **2.10.1** Core STIX objects

**Speaker Notes:**  
2.9 ends here. Do not open STIX unless that lesson is scheduled.
