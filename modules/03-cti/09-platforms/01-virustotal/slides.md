# Module 3.9.1 – VirusTotal Relations and Behavior  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.9.1 – VirusTotal Relations and Behavior  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Not a 3.3.2 redo. Two tabs. Classroom cards.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Relations → additional infra
2. Behavior → four event classes
3. Cite the edge
4. Reject unlabeled nodes and Detection dumps

**Mapped Items:**  
K: 3.9.1 | T: 3.9.1.1

**Speaker Notes:**  
SOC K is A/B/B. Hunter/CTI 3c / 4c / 4d.

---

### Slide 3 – Agenda
**Title:** Agenda

- Two tabs
- Three examples
- Relations lines + Behavior line
- Knowledge check

**Speaker Notes:**  
3.9.2 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

When to pick VT (**3.3.2**)  
SIEM/Zeek query (**2.3.1**)  
AnyRun review (**3.9.2**)  
Applicable TTP product (**3.8.2**)

**Key Point:** Cite the edge. Extract the events.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Relations
**Title:** Graph Edges, Not a Dump

Contacted domain / IP = infra.  
Communicating file = another sample.  
Community “related” = not enough.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Behavior
**Title:** Four Classes

Process · File · Registry · Network

**Speaker Notes:**  
Outline b. Not Detection.

---

### Slide 7 – Classroom Seed
**Title:** `6734f374…` / `update.exe`

Contacted: `nightowl-updates.net`, `login-nightowl.net`, `203.0.113.88`.

**Speaker Notes:**  
Lesson-only card.

---

### Slide 8 – Lines
**Title:** Two Lines

Relations: `seed | edge | infra | why`  
Behavior: `process | file | registry | network`

**Speaker Notes:**  
Tasks.

---

### Slide 9 – Example 1
**Title:** Example 1 – Cited Hops

Two names + the IP. In the product.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2
**Title:** Example 2 – File ≠ Infra

`88aa9911…` is a sample.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3
**Title:** Example 3 – Wrong Tab

Detection T-IDs ≠ Behavior.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- 12-node paste  
- Related file as a domain  
- Detection as Behavior  
- Opening Silent Push  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Same edges on a live VT page.  
Keep: cite the edge; four Behavior classes.

**Speaker Notes:**  
Do not require a login this hour.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–D: Relations lines.
3. One Behavior line.
4. No SIEM query.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Relations vs Behavior?
2. Relations line besides the name?
3. Why not the communicating file as infra?
4. Why not Detection T-IDs?
5. Where is the Zeek/SIEM query?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Cite the edge. Four event classes.
- Next: **3.9.2** AnyRun.

**Speaker Notes:**  
Do not open 3.9.2 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** VT Tabs — Quick Reference

| Edge / row | Take |
|------------|------|
| Contacted domain/IP | additional infra |
| Communicating file | sample, not infra |
| Community related | reject |
| Behavior | process / file / reg / net |

**Coming next:** Module 3.9.2 – AnyRun

**Footer:** SOC / Hunter / CTI Training Program
