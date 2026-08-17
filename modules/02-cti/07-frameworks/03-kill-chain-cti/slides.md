# Module 3.7.3 – Cyber Kill Chain in CTI  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.7.3 – Cyber Kill Chain in Intelligence Analysis  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Not a 0.6.3 redo. Report → stages → product list.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Kill Chain on an intelligence problem
2. Identify the stage; reject previous / next
3. Place the set; list only supported stages
4. Reject an unobserved stage

**Mapped Items:**  
K: 3.7.3 | T: 3.7.3.1

**Speaker Notes:**  
SOC K is A/B/B. Hunter/CTI task 3c / 4c / 4c (not 4d).

---

### Slide 3 – Agenda
**Title:** Agenda

- Advanced place + product use
- Three examples
- Five stage lines + product list
- Knowledge check

**Speaker Notes:**  
3.7.4 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Single-row stage (**0.6.3**)  
ATT&CK IDs (**3.7.1**)  
Diamond vertices (**3.7.2**)  
Alert categories (**1.4.4**)  
Actor profile (**3.11**)

**Key Point:** Evidence-bound stages in the product.

**Speaker Notes:**  
Fence. Do not copy shared/frameworks.

---

### Slide 5 – Advanced Use
**Title:** Place · Reject · Stack · Omit · Report

One span, one primary stage.  
Reject previous and next.  
List only stages this excerpt earns.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Seven Stages (Recap Only)
**Title:** Same Seven, In Order

Recon → Weaponization → Delivery → Exploitation → Installation → C2 → Actions on Objectives

**Speaker Notes:**  
One slide. Do not re-teach 0.6.3.

---

### Slide 7 – Stage Line
**Title:** Four Fields

`evidence | stage | not previous | not next`

**Speaker Notes:**  
Task.

---

### Slide 8 – Product List
**Title:** Not “They Reached Stage 7”

`Delivery, Exploitation, Installation`  
Weaponization / Actions on Objectives stay out.

**Speaker Notes:**  
Chain order, not excerpt order.

---

### Slide 9 – Example 1: Excerpt
**Title:** Example 1 – Night Owl Story

GET = Delivery. PS-enc = Exploitation. Run = Installation.  
Three supported stages.

**Speaker Notes:**  
Students first. GET is the drop, not a beacon.

---

### Slide 10 – Example 2: Stage 7 Dump
**Title:** Example 2 – Uncited Actions

Vendor T1486 ≠ Actions on Objectives.  
Stays out of *this* product.

**Speaker Notes:**  
Lead. Same uncited rule as 3.7.1 / 3.7.2.

---

### Slide 11 – Example 3: Invented Weaponization
**Title:** Example 3 – Off-Net Builder

“They packed the VBS” is not a stage you saw.  
**Not observed.**

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Whole set → Actions on Objectives  
- Invented Weaponization  
- GET labeled C2 because of T1071.001  
- ATT&CK IDs on the stage line  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use the Lockheed Martin seven stages.  
Keep: cite + reject neighbor + supported list only.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–E: stage lines.
3. Product stage list for A–C.
4. No ATT&CK IDs. No Diamond.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Advanced vs 0.6.3?
2. Stage line besides the stage?
3. Why not vendor T1486 as Actions?
4. Why is Weaponization usually empty?
5. ATT&CK tactic ≠ Kill Chain stage?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Place each span. List only supported stages.
- Next: **3.7.4** DTF.

**Speaker Notes:**  
Do not open 3.7.4 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** CTI Kill Chain — Quick Reference

| Evidence | Stage |
|----------|-------|
| GET `update.exe` | Delivery |
| `powershell -enc` | Exploitation |
| HKCU Run | Installation |
| Vendor T1486 / “they built it” | none |

**Coming next:** Module 3.7.4 – MalasadaTech Defender’s ThreatMesh Framework (DTF)

**Footer:** SOC / Hunter / CTI Training Program
