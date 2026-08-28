# Module 2.8.4 – Threat Relevance and Organizational Impact  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.8.4 – Threat Relevance and Organizational Impact  
**Subtitle:** Does this finding apply here, and what would change  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is the so-what of a finding. It is not a PIR, not a TTP extract, and not a country. VirusTotal tabs wait for the next lesson.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts say whether a finding **matters here**, not only whether it is technically interesting.

Someone still has to write the line for this shop.

This lesson is two sentences: **relevance** and **impact**.

**Speaker Notes:**  
This slide is the student intro. Enrichment can leave a domain, a TTP, or a handled IOC. The job here is whether it applies to this shop, and what would change if it is true. Do not start a PIR or a country.

---

### Slide 3 – Relevance and impact
**Title:** Relevance and impact

**Relevance** — does this finding apply to this **mission**, these **assets**, and this **platform**?

**Impact** — if it is true, **what would change here**?

Write the change that follows from this finding. Do not invent a shop list of impact categories.

**Speaker Notes:**  
These are the two sentences. Mission, assets, and platform are the relevance test, not a catalog to fill. Impact is concrete change, not “how bad.” The not-those-three fence is the next slide.

---

### Slide 4 – Not those three products
**Title:** Not a TTP list, a PIR, or a country

Not **TTP applicability** (**2.8.2**) — keep or reject a behavior. That is not the so-what.

Not a **PIR** (**2.1.4** / **2.12.1**) — a ranked question. Do not write that list here.

Not **attribution** (**2.1.7**) — who or what cluster. A country is not the impact line.

**Speaker Notes:**  
Name the three neighbors so they do not become the product. If they write T1059.001, that is 2.8.2. If they write PIR-01, that is 2.1.4. If they write a nation-state, that is 2.1.7.

---

### Slide 5 – What good looks like
**Title:** Two sentences for A12

**Given:** encoded PowerShell and an update-domain fetch on **WS-JLEE**.

**Relevant** — Windows workstation shop; we already saw it on that host.

**Impact** — IR has the host; the payload path is live on a user workstation.

**Not relevant** — an OT-wipe finding. This shop does not run that process. Impact: none here.

**Speaker Notes:**  
Walk the given before the knowledge check. Two sentences. No country. No PIR. The OT line is the reject, not a second plot. Do not invent OT as something this shop runs.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Relevance is the same as writing a PIR. True or false?  
2. What two sentences do you write?  
3. Encoded PowerShell and an update-domain fetch on **WS-JLEE** (**A12**). One relevance sentence and one impact sentence. No country. No PIR.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Does this finding apply here?  
If it is true, what would change?  
Stop there.

Not a PIR. Not a country. Not a TTP list.

**Speaker Notes:**  
VirusTotal Relations and Behavior is next. That lesson is a tool tab. Stay off the so-what when you get there.

---

### Slide 8 – Next
**Title:** Next

**2.9.1** VirusTotal Relations and Behavior

**Speaker Notes:**  
2.9.1 is the Relations tab and the Behavior tab. Do not open VirusTotal unless that lesson is scheduled.
