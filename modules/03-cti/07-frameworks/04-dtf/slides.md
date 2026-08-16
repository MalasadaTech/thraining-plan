# Module 3.7.4 – DTF  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.7.4 – Defender’s ThreatMesh Framework (DTF)  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Local framework. Classroom card is lesson-only.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Purpose: pattern + prioritize
2. Mesh and score (classroom card)
3. Name the next seed — do not pivot
4. Complement ATT&CK, Diamond, Kill Chain

**Mapped Items:**  
K: 3.7.4 | T: 3.7.4.1 · 3.7.4.2 · 3.7.4.3

**Speaker Notes:**  
SOC K is A/A/B. CTI 4d on score and seed.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose, mesh, score, complement
- Three examples
- DTF lines + next seed + three sentences
- Knowledge check

**Speaker Notes:**  
3.8.1 is next, not this hour.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

ATT&CK IDs (**3.7.1**)  
Diamond vertices (**3.7.2**)  
Kill Chain stages (**3.7.3**)  
Doing the pivot (**3.8.1**)  
Applies-on-Harbor? (**3.8.2**)

**Key Point:** Cluster and rank. Name the seed. Stop.

**Speaker Notes:**  
Fence. Do not copy shared/frameworks.

---

### Slide 5 – Purpose
**Title:** Pattern, Then Prioritize

See a link across indicator + infrastructure + behavior.  
Rank what deserves the next look.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Classroom Mesh
**Title:** Four Pieces (Lesson-Only)

Indicator · Infrastructure · Behavior · Link

**Speaker Notes:**  
If the site posts a real card, swap it. Keep the obligation.

---

### Slide 7 – Classroom Score
**Title:** Mesh + Recency + Reach (0–3)

Sum. Higher total first.  
No mesh → do not prioritize.

**Speaker Notes:**  
Not live org policy.

---

### Slide 8 – DTF Line
**Title:** Five Fields

`nodes | links | scores = total | prioritize? | next seed`

**Speaker Notes:**  
Tasks 3.7.4.1–2.

---

### Slide 9 – Complements, Does Not Replace
**Title:** Four Frameworks, Four Jobs

ATT&CK = IDs  
Diamond = gaps  
Kill Chain = order  
DTF = cluster + rank

**Speaker Notes:**  
Outline e / 3.7.4.3.

---

### Slide 10 – Example 1: Harbor Mesh
**Title:** Example 1 – Night Owl Cluster

Three-node mesh. Total 8.  
Next seed: `nightowl-updates.net`.

**Speaker Notes:**  
Students first.

---

### Slide 11 – Example 2: Vendor Only
**Title:** Example 2 – Unmeshed T1486

PDF label. No Harbor nodes.  
Score 0.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Example 3: Replacement Traps
**Title:** Example 3 – Not a Substitute

No T-IDs in the score box.  
No “8 = nation-state.”  
No RDAP this hour.

**Speaker Notes:**  
Lead.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Scoring the vendor first  
- T-IDs / stages in the score  
- Total as attribution  
- Running 3.8.1 now  

**Speaker Notes:**  
Then the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–C: DTF lines.
3. Next seed for A.
4. One complement sentence each (ATT&CK / Diamond / Kill Chain).

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. DTF for?
2. DTF line besides the total?
3. Why not T1486 high?
4. High score this hour — do / don’t?
5. One complement?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Mesh. Score. Name the seed. Stop.
- Next: **3.8.1** infrastructure pivot.

**Speaker Notes:**  
Do not open 3.8.1 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Classroom DTF — Quick Reference

| Fill | Score-ish |
|------|-----------|
| PS-enc + Run + GET + domain | Mesh 3 · total 8 · prioritize |
| Next seed | `nightowl-updates.net` |
| Vendor T1486 only | 0 |
| T-ID / APT in the box | fail |

**Coming next:** Module 3.8.1 – Identifying additional adversary infrastructure

**Footer:** SOC / Hunter / CTI Training Program
