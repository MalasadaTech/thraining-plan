# Module 3.7.2 – Diamond Model in CTI  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.7.2 – Diamond Model Application in CTI  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Not a 0.6.2 redo. Report → vertices → product constraint.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Diamond on an intelligence problem
2. Fill four vertices from evidence
3. Weakest vertex constrains the product
4. Reject vendor-name Adversary and uncited Capability

**Mapped Items:**  
K: 3.7.2 | T: 3.7.2.1

**Speaker Notes:**  
SOC K is A/B/B. Hunter/CTI task 3c / 4c / 4d.

---

### Slide 3 – Agenda
**Title:** Agenda

- Advanced fill + product use
- Three examples
- Five Diamond lines + product sentence
- Knowledge check

**Speaker Notes:**  
3.7.3 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Incident / indicator card (**0.6.2**)  
ATT&CK IDs (**3.7.1**)  
Kill Chain stage (**3.7.3**)  
Confidence / types lecture (**3.1.7**)  
Actor profile (**3.11**)

**Key Point:** Evidence-bound vertices; weakest limits the claim.

**Speaker Notes:**  
Fence. Do not copy shared/frameworks.

---

### Slide 5 – Advanced Use
**Title:** Fill · Empty · Weakest · Constrain · Reject

Facts under A / C / I / V.  
Blank is honest. Circle the weakest.  
That vertex drops a product claim.

**Speaker Notes:**  
Outline a. 4d is the constraint sentence.

---

### Slide 6 – Four Vertices (Recap Only)
**Title:** Same Four Questions

Adversary — who is directing this?  
Capability — what can they do?  
Infrastructure — what systems?  
Victim — who/what is acted on?

**Speaker Notes:**  
One slide. Do not re-teach 0.6.2.

---

### Slide 7 – Diamond Line
**Title:** Six Fields

`A | C | I | V | weakest | cannot claim`

**Speaker Notes:**  
Task.

---

### Slide 8 – Product Sentence
**Title:** Not a Profile

C / I / V observed. Adversary unattributed.  
No four-paragraph actor write-up.

**Speaker Notes:**  
3.11 is later.

---

### Slide 9 – Example 1: Excerpt
**Title:** Example 1 – Night Owl Story

C / I / V filled. Adversary unknown.  
Product cannot name a group.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Vendor APT
**Title:** Example 2 – Label ≠ Adversary

“Night Owl APT (nation-state)” stays out.  
No who until *this* set supports it.

**Speaker Notes:**  
Lead. 3.1.7 is types/confidence, not this fill.

---

### Slide 11 – Example 3: Uncited Capability
**Title:** Example 3 – Vendor T1486

Vendor listed ransomware. Harbor excerpt did not.  
Stays off *this* diamond.

**Speaker Notes:**  
Lead. ATT&CK IDs are 3.7.1.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Vendor cluster name in Adversary  
- Uncited T1486 in Capability  
- One host → “all of Harbor”  
- Writing the 3.11 profile on the card  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use Diamond to organize what you know.  
Keep: empty is honest; weakest constrains the product.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–E: Diamond lines.
3. Product sentence for A.
4. No ATT&CK IDs. No profile.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Advanced vs 0.6.2?
2. Diamond line besides the four fills?
3. Why not vendor “APT” in Adversary?
4. Why not vendor T1486 as Capability?
5. Where is the actor profile?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Empty is honest. Weakest limits the product.
- Next: **3.7.3** Kill Chain in CTI.

**Speaker Notes:**  
Do not open 3.7.3 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** CTI Diamond — Quick Reference

| Evidence | Vertex |
|----------|--------|
| `powershell -enc` / Run / GET payload | Capability |
| `nightowl-updates.net` / `203.0.113.88` | Infrastructure |
| `jlee` / `WS-JLEE` | Victim |
| Vendor “APT” / no who | Adversary = none |

**Coming next:** Module 3.7.3 – Cyber Kill Chain in CTI

**Footer:** SOC / Hunter / CTI Training Program
