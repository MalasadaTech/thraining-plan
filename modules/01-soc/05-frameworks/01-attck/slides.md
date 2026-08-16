# Module 1.5.1 – MITRE ATT&CK  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.5.1 – MITRE ATT&CK  
**Subtitle:** SOC / Hunter / CTI Training  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Shared floor. Not hunt planning (2.5). Not Diamond/Kill Chain.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Purpose and matrix structure
2. Tactics vs techniques vs sub-techniques
3. Map activity: tactic + ID + cite + rejected neighbor

**Mapped Items:**  
K: 1.5.1.1 | T: 1.5.1.2

**Speaker Notes:**  
Hunter/CTI start at B / 3c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose and structure
- Mapping method
- Three worked examples
- Four cases
- Knowledge check

**Speaker Notes:**  
1.5.2 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Hunt coverage / Navigator (**2.5**)  
Copying IDs from a PDF (**2.4.2**)  
Alert categories scan/user/root (**1.4.4**)  
Diamond / Kill Chain  
Five IDs on one row

**Key Point:** Map the row you have.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Purpose
**Title:** What ATT&CK Is For

Shared language for **behavior**.  
SOC, hunt, and CTI can point at the same cell.

Not a guilt label. Not a hunt plan.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Structure
**Title:** Matrix = Tactics × Techniques

**Tactic** (column) = *why* / goal  
**Technique** (cell) = *how* (`T1059`)  
**Sub-technique** = more specific (`T1059.001`)

**Speaker Notes:**  
Outline b–c.

---

### Slide 7 – Mapping Steps
**Title:** How to Map

1. What did telemetry show?  
2. What goal? → tactic  
3. What named how? → technique  
4. Cite one field  
5. Reject the neighbor tactic  

**Speaker Notes:**  
Outline d.

---

### Slide 8 – Example 1: Execution
**Title:** Example 1 – powershell -enc

**Execution / T1059.001**  
Cite: `-enc` + wscript parent  
Reject: C2 (no network row)

**Speaker Notes:**  
Students first.

---

### Slide 9 – Example 2: Neighbor
**Title:** Example 2 – “Looks like C2”

Same process row is still **Execution**.  
C2 only if you cite POST `/api/v1/beacon`.

**Speaker Notes:**  
Two rows, two maps.

---

### Slide 10 – Example 3: T1105
**Title:** Example 3 – GET update.exe

**T1105** Ingress Tool Transfer  
Cite: GET `.exe`  
Reject: **Impact**. Staging ≠ ransomware.

**Speaker Notes:**  
Initial Access only if it is the foothold.

---

### Slide 11 – Common Mistakes
**Title:** Common Mistakes

- C2 without a connect  
- ID with no cite  
- Category instead of tactic  
- Navigator hour  
- Persistence on a file create with no Run key  

**Speaker Notes:**  
Then the exercise.

---

### Slide 12 – IDs You May Look Up
**Title:** Look Up Is Allowed

The skill is the **map**, not reciting numbers.  
Use attack.mitre.org in class if needed.

**Speaker Notes:**  
SOC 3 may use a cheat strip.

---

### Slide 13 – Sentence Shape
**Title:** One Primary Map

“Tactic … / T…. …  
Evidence: …  
Not … because …”

**Speaker Notes:**  
Leave up.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize Ex 1–3.
2. Map A–D: tactic, ID, cite, neighbor.
3. No Navigator. No Diamond.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Purpose / what is the matrix?
2. Tactic vs technique vs sub?
3. Four parts of a map?
4. Why not hunt coverage this hour?
5. Why not “looks like C2”?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Why + how + cite. Reject the neighbor.
- Map this row. Hunt planning is **2.5**.
- Next: Diamond Model (**1.5.2**).

**Speaker Notes:**  
Do not open Diamond unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** ATT&CK — Quick Reference

| Need | Write |
|------|--------|
| Why | Tactic |
| How | T-ID + name |
| Proof | One field |
| Fence | Reject neighbor |

**Coming next:** Module 1.5.2 – Diamond Model

**Footer:** SOC / Hunter / CTI Training Program
