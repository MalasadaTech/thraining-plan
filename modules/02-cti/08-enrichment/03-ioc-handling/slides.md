# Module 2.8.3 – IOC Handling  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.8.3 – IOC Handling  
**Subtitle:** CTI Analyst (Hunter / SOC sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Keep, expire, enrich, link. Not a TTP.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Handle the **observable**.

Keep or expire. Name an enrich.  
Same set only if objects are shared.

**Speaker Notes:**  
TTPs were last hour.

---

### Slide 3 – Four actions
**Title:** Keep, expire, enrich, link

**Keep** — cited, current, specific.  
**Expire** — stale, uncited, /24 noise.  
**Enrich** — tool + field + what you hope to learn.  
**Link** — shared objects, not a vendor name.

**Speaker Notes:**  
Outline a–d.

---

### Slide 4 – What good looks like
**Title:** Enrich and link

**Enrich** — hash → TIP, then VT. Not Relations.  
**Link** — update domain + `login-prd.net` (same NS).  
**Apart** — random cloud IP. **Not a link:** “PRD APT.”

**Speaker Notes:**  
Tasks 1–2.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No TTP extract (**2.8.2**).  
No VT Relations class (**2.9.1**).  
No actor profile (**2.11**).

**Speaker Notes:**  
Impact is next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. An IOC is the same thing as a TTP. True or false?  
2. Name keep vs expire for a whole /24.  
3. Update domain + sibling same NS — same set or apart? What vendor name is **not** a link?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Keep cited IOCs. Expire shared noise. Link on objects, not labels.

**Next:** **2.8.4** Relevance and impact

**Speaker Notes:**  
Do not open impact unless scheduled.
