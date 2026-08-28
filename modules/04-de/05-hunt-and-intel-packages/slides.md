# Module 4.5 – Hunt and intel packages  
## Slide Deck Content

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 15–20 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 4.5 – Hunt and intel packages  
**Subtitle:** Inputs from hunt and intel, not finished detections  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
4.4 was a tune on a live rule. This lesson is a package from hunt or intel. It is not a finished detection.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Detection engineers get **packages** from hunters and from intel.

Those are inputs, not finished detections.

Treat the package like a **nomination**. Then name one **add**, one **change**, or **no new rule**. Not a **block** list.

**Speaker Notes:**  
This slide is the student intro. Packages are regular inbound work from those two desks. You review them so they do not skip review, and so extra infrastructure does not become a DE deploy.

---

### Slide 3 – Both desks send packages
**Title:** Packages from CTI and hunters

**CTI** and **hunters** both send packages.

A package is a hunt write-up or an intel **report**.  
It is inbound material to review.

It is not a tune on a live rule. It is not a finished detection.

**Speaker Notes:**  
Both sources are the same kind of input. Do not invent a second review job for intel. A tune request is 4.4 — a live rule already on the desk.

---

### Slide 4 – Treat it like a nomination
**Title:** Not a finished detection

Clear enough to review: the **need**, and a **pointer**.  
The package is often the pointer.

A drafted rule if they have one — not required.  
Missing need or pointer? **Send it back.**

**Speaker Notes:**  
Same bar as 4.3. Restate need plus pointer in ordinary words. Do not walk the whole nomination lesson. Do not invent a form.

---

### Slide 5 – Three products
**Title:** Add, change, or no new rule

One **add** — a new detection this package supports.  
One **change** — a live rule should change because of this package.  
**No new rule** — still a finished review.

Name one. Do not write the rule.

**Speaker Notes:**  
Name one product. Do not pad a “no new rule” with a fake add. If they start picking tune versus retire, that is 4.4 or 4.6.

---

### Slide 6 – Not a block list
**Title:** Reject a block list

A list of IPs or domains to put on the firewall is a **block**.

Firewall / IA. Not a DE deploy.

**Reject** that product.

**Speaker Notes:**  
Walk the three student-guide givens if you need them. Hunt package with a gap → add. Already covered → no new rule. IPs for the firewall → reject.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A package is a finished detection. True or false?  
2. Name the three valid review products for a package.  
3. A package is a list of IPs to put on the firewall. Add a rule, or reject?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

CTI and hunters both send packages.  
Treat like a nomination.  
Add, change, or no new rule.  
A block list is not DE.

**Next:** **4.6** Detection lifecycle

**Speaker Notes:**  
4.6 is modify, retire, or leave on a live rule you already own. Stay off package review when you get there.
