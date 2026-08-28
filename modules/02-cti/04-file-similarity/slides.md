# Module 2.4.1 – Hashing and Similarity Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.4.1 – Hashing and Similarity Concepts  
**Subtitle:** Related samples and who claimed the file  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is similarity hashes and code-signing. It is not MD5 / SHA identity, and it is not VirusTotal Relations.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

A sample usually arrives as a file or a hash.

**SHA256** tells you that exact file. A one-byte change looks brand new.

This lesson is the **cousin** and **who claimed the binary**.

**Speaker Notes:**  
This slide is the student intro. Identity hashes were 1.2.7. Relations wait for 2.9. Stay on similarity and signing.

---

### Slide 3 – imphash, ssdeep, TLSH
**Title:** imphash, ssdeep, TLSH

**imphash** — PE import table. Related compile or packer family. Not the same file.

**ssdeep** — fuzzy bytes. Score 0–100. **Higher** is closer.

**TLSH** — locality-sensitive digest. Distance. **Lower** is closer.

**Speaker Notes:**  
imphash is PE only. Packed files can share a packer import table. Do not call that byte-identical. ssdeep and TLSH both look at bytes; they score opposite ways.

---

### Slide 4 – Classroom stand-ins, not shop policy
**Title:** Classroom stand-ins, not shop policy

This classroom treats **ssdeep 50 or higher** as related.

This classroom treats **TLSH distance 30 or lower** as related.

Those numbers are stand-ins. Do not invent a 90% cutoff as policy.

**Speaker Notes:**  
A weak ssdeep score is not related unless the shop card says otherwise. If they treat TLSH 80 as “80% similar,” stop and reverse the direction.

---

### Slide 5 – Code-signing
**Title:** Code-signing

Signer. Issuer. Validity dates. Or **unsigned**.

This is the signature **on the file**, not a TLS certificate.

Unsigned is a fact. It is not malware and not a country.

**Speaker Notes:**  
Extract the three fields as separate facts. Do not swap issuer for signer. Signed is not trusted. Do not upgrade unsigned to nation-state.

---

### Slide 6 – Related vs unsigned
**Title:** Related vs unsigned

Same **imphash** as `update.exe`, different SHA256 → related compile. Not the same file.

ssdeep **20** against `update.exe` → **not related** on the classroom card.

**Unsigned** → no signer. Do not upgrade to nation-state.

**Speaker Notes:**  
Show these givens before the knowledge check. The product is “related compile” or “not related,” plus the signing line. Do not open Relations.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Same imphash means the two files are byte-identical. True or false?  
2. What does ssdeep (or TLSH) find that SHA256 does not?  
3. You extract “unsigned” from `update.exe`. What did you learn, and what must you **not** claim?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Similarity finds cousins when SHA256 does not match.  
imphash is the import table, not the whole file.  
ssdeep high is close; TLSH distance low is close.  
Signing is who claimed the file. Unsigned is a fact.

**Next:** **2.5.1** RDAP / WHOIS

**Speaker Notes:**  
2.5.1 is registration, not another hash type. Stay off WHOIS unless that lesson is scheduled.
