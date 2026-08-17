# Module 3.4.3 – STIX as Hunt Input
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC, CTI sit this too  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.4.3 – STIX as Hunt Input  
**Subtitle:** Threat Hunter (SOC / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Read the bundle. Do not author. Spec is STIX 2.1.

---

### Slide 2 – What this hour is
**Title:** What this hour is

**Identify** hunt-relevant objects.

**Seed** a question. Do not write STIX.

**Speaker Notes:**  
2.10 is author. This hour is input.

---

### Slide 3 – Objects a hunter uses
**Title:** Six objects

**indicator** · **attack-pattern** · **observed-data**  
**malware** · **threat-actor** / **intrusion-set** · **relationship**

Actor name is **not** a search.

**Speaker Notes:**  
Outline a. Other STIX types may appear; not the sign-off list.

---

### Slide 4 – What good looks like
**Title:** Seed

`indicator` `:8080` `/update.exe` + Run **`Updater`** `attack-pattern`.  
**Question** — if more persistors exist, we see those.  
**Not** dump every IPv4 `indicator`.

**Speaker Notes:**  
Tasks 1–2.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No authoring (**2.10**).  
No TAXII.  
No Navigator (**3.5**).

**Speaker Notes:**  
ATT&CK map next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Hunters author STIX in this hour. True or false?  
2. Name four objects a hunter actually uses.  
3. From the A12 bundle: one hunt-relevant object and the lead it seeds.

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Identify. Seed. Do not author.

**Next:** **3.5.1** ATT&CK for hunt planning

**Speaker Notes:**  
Do not open Navigator unless scheduled.
