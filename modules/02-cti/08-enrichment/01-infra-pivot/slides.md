# Module 3.8.1 – Infra Pivot from a Seed  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.8.1 – Additional Infrastructure from a Seed  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
3.7.4 wrote the DTF ID line. This hour writes the hop sentence.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Explain a pivot
2. Pick a data source
3. Cite additional infra
4. Reject a weak or uncited hop

**Mapped Items:**  
K: 3.8.1 | T: 3.8.1.1

**Speaker Notes:**  
SOC K is A/B/B. Hunter/CTI task 3c / 4c / 4d.

---

### Slide 3 – Agenda
**Title:** Agenda

- Pivot + sources
- Three examples
- Five pivot lines + product hop
- Knowledge check

**Speaker Notes:**  
3.8.2 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

How to read RDAP / SOA (**3.5** / **3.6**)  
Silent Push vs VT (**3.3.2**)  
Applicable TTPs (**3.8.2**)  
VT Relations depth (**3.9**)  
Actor profile (**3.11**)

**Key Point:** Do the hop. Cite it.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Pivot
**Title:** Seed · Shared Property · Additional Infra

Start with `nightowl-updates.net`.  
Follow NS / MNAME / A.  
Name another domain or IP.

**Speaker Notes:**  
Outline a. Not a group name.

---

### Slide 6 – Sources (Recap Only)
**Title:** Four Sources, Not a Catalog

RDAP → NS  
SOA → MNAME + NS  
PDNS → historical A  
TIP → Harbor sighting

**Speaker Notes:**  
Outline b. VT Relations is 3.9.

---

### Slide 7 – Pivot Line
**Title:** Five Fields

`seed | source | shared property | additional infra | why not coincidence`

**Speaker Notes:**  
Task.

---

### Slide 8 – Classroom Cards
**Title:** Lesson-Only Results

Sibling `login-nightowl.net`: same MNAME+NS **and** A `203.0.113.88`.  
Cloud /24 has many tenants.

**Speaker Notes:**  
Not live PDNS.

---

### Slide 9 – Example 1: Sibling
**Title:** Example 1 – Cited Hop

`login-nightowl.net`  
Two properties. In the product.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Weak Hop
**Title:** Example 2 – Cloud /24 or Public NS

Hosting ≠ theirs.  
Need a distinctive stack.

**Speaker Notes:**  
Lead. 4d.

---

### Slide 11 – Example 3: Uncited Name
**Title:** Example 3 – Vendor `evil-c2.net`

No shared property on the card.  
Stays out.

**Speaker Notes:**  
Lead. Same uncited rule as 3.7.x.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Entire cloud CIDR as infra  
- Shared Cloudflare NS  
- PDF domain with no link  
- Opening VT Relations  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use the same hop logic on live RDAP / PDNS.  
Keep: cite the shared property; reject the weak hop.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–E: pivot lines.
3. Product hop for A/C.
4. No TTP extract. No profile.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. What is a pivot?
2. Two sources + properties?
3. Why not the cloud /24?
4. Why not the vendor domain?
5. Where are Harbor-applicable TTPs?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Cite the hop. Reject the weak one.
- Next: **3.8.2** applicable TTPs.

**Speaker Notes:**  
Do not open 3.8.2 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Infra Pivot — Quick Reference

| Seed / hop | Result |
|------------|--------|
| `nightowl-updates.net` | → `login-nightowl.net` |
| Shared | MNAME+NS **and** A `203.0.113.88` |
| Cloud /24 | reject |
| Vendor name only | reject |

**Coming next:** Module 3.8.2 – Extracting applicable TTPs from intelligence reports

**Footer:** SOC / Hunter / CTI Training Program
