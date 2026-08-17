# Module 3.8.2 – Applicable TTPs  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.8.2 – Extracting Applicable TTPs  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Not a 3.7.1 redo. Report TTP → apply on Harbor?

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Identify relevant TTPs in a report
2. Apply Harbor criteria
3. Extract only dual-pass IDs
4. Reject Unix/ESXi/footnote TTPs

**Mapped Items:**  
K: 3.8.2 | T: 3.8.2.1

**Speaker Notes:**  
SOC K is A/B/B. Hunter/CTI task 3c / 4c / 4d.

---

### Slide 3 – Agenda
**Title:** Agenda

- Two gates + Harbor criteria
- Three examples
- Five apply lines + product list
- Knowledge check

**Speaker Notes:**  
3.8.3 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Evidence-bound map only (**3.7.1**)  
Hunt ID skim (**2.4.2**)  
Navigator coverage (**2.5**)  
Infra hop (**3.8.1**)  
Impact / Sev (**3.8.4**)

**Key Point:** Relevant, then applicable.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Gate 1
**Title:** Relevant in the Report

Behavior + how.  
Same uncited rule as **3.7.1**.  
No invented T-IDs.

**Speaker Notes:**  
Outline a. One recap slide.

---

### Slide 6 – Gate 2
**Title:** Applicable on Harbor

Platform · Path · (Visibility is a note, not a veto)

**Speaker Notes:**  
Outline b. Lesson-only Harbor card.

---

### Slide 7 – Harbor Facts (Recap)
**Title:** Classroom Harbor

Windows users. HTTP egress.  
No Unix fleet. No ESXi. No macOS.  
Users do not initiate to OT.

**Speaker Notes:**  
From 1.8.1. Not live org policy.

---

### Slide 8 – Apply Line
**Title:** Five Fields

`T-ID | in the report because | Harbor fact | apply? | reject`

**Speaker Notes:**  
Task.

---

### Slide 9 – Example 1: Four Apply
**Title:** Example 1 – Windows / HTTP

T1059.001 · T1547.001 · T1071.001 · T1105

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Platform Miss
**Title:** Example 2 – Unix / ESXi

T1059.004 and ESXi T1486 stay out.  
Scary ≠ applicable.

**Speaker Notes:**  
Lead. 3.8.4 is impact.

---

### Slide 11 – Example 3: Footnote
**Title:** Example 3 – T1071.004

“Other campaigns use DNS C2.”  
Zeek `dns` does not rescue gate 1.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Whole vendor matrix  
- T1486 because ransomware is bad  
- Visibility as a substitute for evidence  
- Invented T-codes  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Swap in the live platform/path card.  
Keep: two gates; real IDs only.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–E: apply lines.
3. Product list for A–C.
4. No Navigator. No impact paragraph.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Different from 3.7.1?
2. Two gates?
3. Why not T1059.004?
4. Why not T1071.004 from Zeek `dns`?
5. Where is organizational impact?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Both gates, or it stays out.
- Next: **3.8.3** IOC handling.

**Speaker Notes:**  
Do not open 3.8.3 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Applicable TTPs — Quick Reference

| T-ID | Extract? |
|------|----------|
| T1059.001 / T1547.001 / T1071.001 / T1105 | yes |
| T1059.004 Unix | no |
| T1486 ESXi | no |
| T1071.004 footnote | no |

**Coming next:** Module 3.8.3 – IOC handling and enrichment concepts

**Footer:** SOC / Hunter / CTI Training Program
