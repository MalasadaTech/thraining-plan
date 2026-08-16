# Module 1.5.3 – Cyber Kill Chain  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.5.3 – Cyber Kill Chain  
**Subtitle:** SOC / Hunter / CTI Training  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Seven stages. Sequence, not a matrix. Closes 1.5.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Purpose of the Kill Chain
2. Seven stages in order
3. Identify the stage and reject previous or next

**Mapped Items:**  
K: 1.5.3.1 | T: 1.5.3.2

**Speaker Notes:**  
Hunter/CTI start at B / 3c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose
- Seven stages
- Progression
- Three examples
- Four cases
- Knowledge check — close 1.5

**Speaker Notes:**  
1.6 is next unit.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

ATT&CK tactics (**1.5.1**)  
Diamond vertices (**1.5.2**)  
1.4.4 categories as a substitute  
Everything is Actions on Objectives

**Key Point:** One row, one primary stage.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Purpose
**Title:** What the Kill Chain Is For

Place activity on an intrusion **sequence**.  
Describe progression.  
Not a blocking-architecture class.

**Speaker Notes:**  
Outline a, c.

---

### Slide 6 – Stages 1–4
**Title:** Recon → Exploitation

1 Reconnaissance — probe  
2 Weaponization — pair exploit+payload (**rarely logged**)  
3 Delivery — payload arrives  
4 Exploitation — trigger / first exec  

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Stages 5–7
**Title:** Installation → Actions

5 Installation — foothold / persist  
6 Command and Control — channel  
7 Actions on Objectives — why they came  

Do not assume 7.

**Speaker Notes:**  
Finish the strip.

---

### Slide 8 – Weaponization
**Title:** Often Empty

Builder is off-network.  
Write **not observed**.  
Do not invent a kit.

**Speaker Notes:**  
Say twice.

---

### Slide 9 – Example 1: Delivery
**Title:** Example 1 – GET update.exe

**Delivery.**  
Not Exploitation (no trigger).  
Not Installation (no persist yet).

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Installation
**Title:** Example 2 – HKCU Run

**Installation.**  
Not C2 (no channel).  
Not Delivery (file already there).

**Speaker Notes:**  
Autorun = foothold.

---

### Slide 11 – Example 3: Recon
**Title:** Example 3 – Port Sweep

**Reconnaissance.**  
Not Actions on Objectives.  
Weaponization not observed.

**Speaker Notes:**  
POST beacon = C2, not Delivery.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Everything is stage 7  
- C2 on a process-create  
- Delivery vs Installation mixed  
- T-IDs instead of stages  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Sentence Shape
**Title:** Three Lines

Stage: …  
Not previous because …  
Not next because …

**Speaker Notes:**  
Leave up.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize Ex 1–3.
2. A–D: stage + not previous + not next.
3. No ATT&CK. No Diamond.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Purpose?
2. Seven stages in order?
3. Why is Weaponization often empty?
4. Why reject previous/next?
5. Stage vs ATT&CK tactic?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Seven stages. One primary per row.
- Reject neighbors. Weaponization often empty.
- Unit **1.5** ends. Next unit: **1.6** Reporting.

**Speaker Notes:**  
Do not open reporting unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Kill Chain — Quick Reference

1 Recon · 2 Weaponize · 3 Deliver  
4 Exploit · 5 Install · 6 C2 · 7 Actions  

**Coming next:** Module 1.6 – Reporting

**Footer:** SOC / Hunter / CTI Training Program
