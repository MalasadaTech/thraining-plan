# Module 3.7.1 – MITRE ATT&CK for CTI  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.7.1 – ATT&CK for CTI Analysis and Reporting  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Not a 1.5.1 redo. Report → IDs → product line.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. ATT&CK in CTI analysis and reporting
2. Extract TTPs onto real IDs
3. Cite evidence; reject the neighbor
4. List only supported IDs in the product

**Mapped Items:**  
K: 3.7.1 | T: 3.7.1.1

**Speaker Notes:**  
SOC K is A/B/B. Hunter/CTI task 3c / 4c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Advanced extract + report use
- Three examples
- Five map lines + product list
- Knowledge check

**Speaker Notes:**  
3.7.2 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Alert mapping floor (**1.5.1**)  
Hunt coverage / Navigator (**2.5**)  
Applies-on-Harbor? (**3.8.2**)  
Diamond / Kill Chain / DTF (**3.7.2–3.7.4**)

**Key Point:** Evidence-bound IDs in the product.

**Speaker Notes:**  
Fence. Do not copy shared/frameworks.

---

### Slide 5 – Advanced Use
**Title:** Extract · Map · Cite · Reject · Report

Behavior, not a group name.  
Real T-ID. Evidence span. Neighbor ID.  
Product: only those IDs.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Classroom IDs
**Title:** Use These (Real)

T1059.001 PowerShell — not .003  
T1547.001 Run key — not startup folder  
T1071.001 Web / T1105 ingress — not T1071.004 unless DNS  
No ID for “APT”

**Speaker Notes:**  
Do not invent cells.

---

### Slide 7 – Map Line
**Title:** Six Fields

`evidence | tactic | T-ID | name | rejected | why`

**Speaker Notes:**  
Task.

---

### Slide 8 – Product Line
**Title:** Not the Whole Matrix

`T1059.001, T1547.001, T1071.001, T1105`  
No 14-tactic dump.

**Speaker Notes:**  
Reporting use.

---

### Slide 9 – Example 1: Excerpt
**Title:** Example 1 – Night Owl Story

PS-enc, Run key, HTTP GET.  
Four supported IDs. T1486 not seen.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: APT
**Title:** Example 2 – No Behavior

“Financially motivated APT” ≠ TA0040.  
No T-ID.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: Vendor Dump
**Title:** Example 3 – Uncited T1486

Vendor listed it. Harbor excerpt did not.  
Stays out of *this* product.

**Speaker Notes:**  
Lead. 3.8.2 is later.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Invented T-codes  
- Motive as a tactic  
- Vendor matrix paste  
- Stopping at T1059 when .001 is in the log  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use ATT&CK for lookup.  
Keep: cite + reject + supported list only.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–E: map lines.
3. Product ID list for A–C.
4. No Navigator. No invented IDs.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Advanced vs 1.5.1?
2. Map line besides the ID?
3. Why not vendor T1486 here?
4. Why not “APT” → tactic?
5. Where is Harbor applicability?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Cite. Reject the neighbor. List only supported IDs.
- Next: **3.7.2** Diamond in CTI.

**Speaker Notes:**  
Do not open 3.7.2 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** CTI ATT&CK — Quick Reference

| Evidence | ID |
|----------|-----|
| `powershell -enc` | T1059.001 |
| HKCU Run | T1547.001 |
| HTTP GET payload | T1071.001 / T1105 |
| Name / motive only | none |

**Coming next:** Module 3.7.2 – Diamond Model in CTI

**Footer:** SOC / Hunter / CTI Training Program
