# Module 3.9.2 – AnyRun  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.9.2 – AnyRun Search and Review  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Classroom cards. No live detonation.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Search by tag, IP, domain, or hash
2. Review a run for actionable intel
3. Reject tag-only hits
4. Reject unlabeled ATT&CK tags

**Mapped Items:**  
K: 3.9.2 | T: 3.9.2.1

**Speaker Notes:**  
SOC K is A/A/B. Task ends at 4c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Search + review
- Three examples
- Search lines + R1 review
- Knowledge check

**Speaker Notes:**  
3.9.3 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

When to pick AnyRun (**3.3.2**)  
VT Behavior tab (**3.9.1**)  
SIEM/Zeek query (**2.3.1**)  
Applicable TTP product (**3.8.2**)

**Key Point:** Events from the run you kept.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Search
**Title:** Four Query Types

Hash · Domain · IP · Tag  
Tag last, not first.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Review
**Title:** Actionable vs Not

Tree / drop / C2 = take.  
Score / MITRE tag / random tagged run = leave.

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Classroom Runs
**Title:** R1 Keep · R2 Reject

R1 = Harbor events.  
R2 = miner + tag `nightowl`.

**Speaker Notes:**  
Lesson-only.

---

### Slide 8 – Lines
**Title:** Two Lines

Search: `type | query | run kept | why`  
Review: `tree | dropped | C2 | will not take`

**Speaker Notes:**  
Tasks.

---

### Slide 9 – Example 1
**Title:** Example 1 – Domain → R1

Extract tree, drop, C2.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2
**Title:** Example 2 – Tag `apt`

First hit is not Night Owl.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3
**Title:** Example 3 – T1486 Tag

No encrypt event. Out.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Tag-first search  
- Keeping R2  
- AnyRun matrix paste  
- Calling VT Behavior “AnyRun”  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Do not detonate unknown USBs in class.  
Keep: events over tags.

**Speaker Notes:**  
Lesson-only cards.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–D: search lines.
3. Review R1; reject R2.
4. No live submit.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Four search types?
2. What is actionable?
3. Why not tag `apt` first?
4. Why not the T1486 tag?
5. When VT Behavior instead?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Keep the run whose events match.
- Next: **3.9.3** Silent Push.

**Speaker Notes:**  
Do not open 3.9.3 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** AnyRun — Quick Reference

| Query | Keep |
|-------|------|
| Hash / domain / IP | R1 |
| Tag `apt` | none |
| R1 extract | tree + drop + C2 |
| R2 | reject |

**Coming next:** Module 3.9.3 – Silent Push

**Footer:** SOC / Hunter / CTI Training Program
