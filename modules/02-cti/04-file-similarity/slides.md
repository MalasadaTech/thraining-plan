# Module 3.4.1 – Hashing and Similarity Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.4.1 – Hashing and Similarity  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Related vs identical. Signed vs trusted. Overlay site ssdeep cutoff if you have one.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Purpose / use case: imphash, ssdeep, TLSH
2. Related samples — which hash
3. Interpret code-signing fields

**Mapped Items:**  
K: 3.4.1 | T: 3.4.1.1 | T: 3.4.1.2

**Speaker Notes:**  
CTI 3.4.1.1 is 3c / 4d. Cert task is 3c / 4c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Three hashes + cert fields
- Three examples
- Related-lines + cert lines
- Knowledge check

**Speaker Notes:**  
3.5 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

SHA256 as the *whole* story (**1.2.7**)  
VT Relations graph (**3.9**)  
AnyRun behavior (**3.3.2**)

**Key Point:** Similar. Then who signed.

**Speaker Notes:**  
Fence.

---

### Slide 5 – imphash
**Title:** Import Table

Same APIs → possible same family / packer.  
PE only. Generic imports can collide.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – ssdeep and TLSH
**Title:** Fuzzy Similarity

**ssdeep** — classroom **≥ 50** = related.  
**TLSH** — compare TLSH to TLSH. Do not mix scores.

**Speaker Notes:**  
Outline b–c. Stand-in cutoff.

---

### Slide 7 – Identity vs Similar
**Title:** Same SHA256

That is the **same file**.  
Not an ssdeep finding.

**Speaker Notes:**  
Example 2 trap.

---

### Slide 8 – Certificates
**Title:** Signed ≠ Trusted

Signed / subject / **issuer** / validity / chain.  
“Microsoft” in subject is a string.

**Speaker Notes:**  
Outline d.

---

### Slide 9 – Example 1: Related
**Title:** Example 1 – S1 vs S2

Different SHA256. Same imphash. ssdeep 72.  
Related imports + fuzzy. Not identical.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Duplicate
**Title:** Example 2 – S1 vs S4

Same SHA256.  
Identity. Stop.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: Fake Microsoft
**Title:** Example 3 – S3 Cert

Harbor Test CA. Expired.  
Not similar to S1. Not trusted Microsoft.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- SHA256 as ssdeep  
- ssdeep 8 = related  
- Mixing TLSH and ssdeep  
- Subject = issuer  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use the site ssdeep/TLSH cutoff if posted.  
Keep: which hash + related? / issuer not subject.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–C: related-line.
3. S3, D, E: cert interpret.
4. No Relations graph.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. imphash vs SHA256?
2. ssdeep — when, and ≥ 50?
3. Why not mix TLSH and ssdeep?
4. Why not trust “Microsoft” in subject?
5. Where is behavior taught?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Related ≠ identical. Signed ≠ trusted.
- Next: **3.5** RDAP / WHOIS.

**Speaker Notes:**  
Do not open 3.5 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Similarity — Quick Reference

| Hash | Question |
|------|----------|
| SHA256 | Same bytes? |
| imphash | Same PE imports? |
| ssdeep / TLSH | Similar body? |
| Cert | Who signed / who issued / valid? |

**Coming next:** Module 3.5.1 – RDAP / WHOIS

**Footer:** SOC / Hunter / CTI Training Program
