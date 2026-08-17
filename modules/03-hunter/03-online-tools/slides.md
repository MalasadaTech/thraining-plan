# Module 3.3.1 – Hunt Tool Capabilities  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC, CTI sit this too  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.3.1 – Tool Capabilities for Hunting  
**Subtitle:** Threat Hunter (SOC / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Convert a lead to an internal query. Not 0.7.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Use the tool to **seed a search here**.

Strength vs limit.  
Lead → precise SIEM or Zeek query.

**Speaker Notes:**  
Card only.

---

### Slide 3 – Four tools
**Title:** Strength vs limit

**VT** — Relations/Behavior, not a count.  
**AnyRun** — process/network, not a tag.  
**URLScan** — requested hosts, not a screenshot.  
**Silent Push** — names on an A, not a /24.

**Speaker Notes:**  
Outline a–d.

---

### Slide 4 – What good looks like
**Title:** Convert

Lead: `GET /update.exe` to `203.0.113.88:8080`.  
Query: that IP + port + URI.  
**Not** `dest=*`. **Not** the /24.

**Speaker Notes:**  
Task 3.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No 0.7 survey.  
No 2.9 tab class.  
No live account.

**Speaker Notes:**  
CTI triage next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A VirusTotal detection count is a hunt query. True or false?  
2. Name one hunt limit for Silent Push.  
3. Turn the `:8080` `/update.exe` lead into one precise Zeek or SIEM query.

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Hunt limit per tool. Lead → precise internal query.

**Next:** **3.4.1** Assessing CTI for hunting value

**Speaker Notes:**  
Do not open triage unless scheduled.
