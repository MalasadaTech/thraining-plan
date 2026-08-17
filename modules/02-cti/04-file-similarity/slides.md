# Module 2.4.1 – Hashing and Similarity Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.4.1 – Hashing and Similarity Concepts  
**Subtitle:** CTI Analyst (Hunter / SOC sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Cousins, not SHA256. Not VT Relations.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Find a **related sample** when the SHA256 does not match.

Read a **code-signing** field.  
Unsigned is a fact, not a country.

**Speaker Notes:**  
Identity hashes were 1.2.7.

---

### Slide 3 – Four tools
**Title:** imphash, ssdeep, TLSH, signing

**imphash** — PE imports. Related compile.  
**ssdeep / TLSH** — fuzzy cousins.  
**Code-signing** — signer, issuer, dates — or unsigned.

**Speaker Notes:**  
Outline a–d. No invented cutoff as policy.

---

### Slide 4 – What good looks like
**Title:** Related vs unsigned

Same **imphash** as `update.exe` → related compile. Not the same file.  
**Unsigned** → no signer. Do not upgrade to nation-state.

**Speaker Notes:**  
Tasks 1–3.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No MD5 / SHA identity (**1.2.7**).  
No VT Relations (**2.9**).  
No invented shop threshold.

**Speaker Notes:**  
RDAP is next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Same imphash means the two files are byte-identical. True or false?  
2. What does ssdeep (or TLSH) find that SHA256 does not?  
3. You extract “unsigned” from `update.exe`. What did you learn, and what must you **not** claim?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Similarity finds cousins. Signing is who claimed the file.

**Next:** **2.5.1** RDAP / WHOIS

**Speaker Notes:**  
Do not open RDAP unless that hour is scheduled.
