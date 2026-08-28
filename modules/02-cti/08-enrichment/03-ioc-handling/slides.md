# Module 2.8.3 – IOC Handling and Enrichment Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.8.3 – IOC Handling  
**Subtitle:** Keep, expire, enrich, or link the object  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is the IOC as an object. The last lesson was which TTPs apply here. Do not start extracting techniques today.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts handle **IOCs** that land on the desk.

Each one is an **observable** you keep, expire, enrich, or link.  
A TTP is a **behavior**. This lesson is the **object**.

**Speaker Notes:**  
Reports dump more hashes and IPs than the shop should store. If they treat a range as a keep, or a vendor name as a link, hunters get noise. Stay on the object. Impact is the next lesson.

---

### Slide 3 – IOC versus TTP
**Title:** Observable versus behavior

**IOC** — a hash, IP, domain, or similar object you record, enrich, or expire.

**TTP** — a behavior: how they operate, not the object you stored.

Do not write a technique ID when the thing on the desk is a hash.

**Speaker Notes:**  
If they start listing T1059.001, that work already happened. Point them back to the object. Actor profile is later.

---

### Slide 4 – Keep or expire
**Title:** Keep cited. Expire noise.

**Keep** — cited, current, specific enough to use.

**Expire** — stale, uncited, or shared-infrastructure noise.

A whole `/24` that contains one bad IP is still noise.  
Keep `203.0.113.88`. Expire `203.0.113.0/24`.

**Speaker Notes:**  
Walk the Example Cloud range. One cited host does not make the subnet theirs. Expire means reject for handling: do not store it as a current IOC.

---

### Slide 5 – Name the enrichment
**Title:** Name the tool. Do not re-teach it.

This lesson **selects and records** the lookup.

Name the **tool**, the **field**, and **what you hope to learn**.

**Given:** hash of Temp `invoice.vbs` → TIP first, then VirusTotal if still needed.  
Hope to learn: seen here, or public reputation. Not the Relations tab.

**Speaker Notes:**  
Tools are already taught. The product is the enrich line, not a live lookup. If they open Relations, that is the VirusTotal lesson. If they rewrite a hop sentence, that is the infrastructure-pivot lesson.

---

### Slide 6 – Same activity set or apart
**Title:** Cite shared objects. Not a vendor name.

**Same set** — update domain + `203.0.113.88` + `login-prd.net` (same nameserver, same A record).

**Apart** — a random Example Cloud IP with no shared nameserver.

**Not a link:** “same group because the PDF said PRD APT.”

**Speaker Notes:**  
Link analysis is this same-set decision. Campaign tracking is the same job. Fail the vendor-name link out loud. A PDF label is not an object you can cite.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. An IOC is the same thing as a TTP. True or false?  
2. Do you keep or expire a whole `/24` that contains one bad IP?  
3. Update domain + sibling that share a nameserver — same activity set or apart, and why? Why is a vendor name such as “PRD APT” not a link?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

An IOC is an observable. A TTP is a behavior.  
Keep cited IOCs. Expire shared noise.  
Name the enrich. Link on objects, not labels.

**Next:** **2.8.4** Relevance and impact

**Speaker Notes:**  
2.8.4 is whether the finding applies here and what would change. Do not open that line unless that lesson is scheduled.
