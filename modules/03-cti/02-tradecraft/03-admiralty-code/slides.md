# Module 3.2.3 – Admiralty Code  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.2.3 – Admiralty Code  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Assign + explain. Overlay the site card if you have one.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Source reliability A–F
2. Information credibility 1–6
3. Combine letter + number
4. Assign a code and explain one

**Mapped Items:**  
K: 3.2.3 | T: 3.2.3.1

**Speaker Notes:**  
SOC 3-level task is 1a / 2b. CTI is 3c / 4d.

---

### Slide 3 – Agenda
**Title:** Agenda

- Two scales + combine
- Three examples
- Four assigns + two explains
- Knowledge check

**Speaker Notes:**  
3.2.4 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

*Likely* / *even chance* (**3.2.1**)  
ACH / KAC (**3.2.2**)  
Attribution **medium** (**3.1.7**)  
Bias names (**3.2.4**)

**Key Point:** Source letter. Report number.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Source A–F
**Title:** Reliability of the Reporter

**A** completely reliable · **B** usually  
**C** fairly · **D** not usually  
**E** unreliable · **F** cannot judge

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Information 1–6
**Title:** This Claim

**1** independently confirmed · **2** probably  
**3** possibly · **4** doubtful  
**5** improbable · **6** cannot judge

**Speaker Notes:**  
Outline b.

---

### Slide 7 – Combine
**Title:** Two Sentences

**B2** = source usually reliable. This report probably true.  
**F1** and **B3** are legal. **A1** is rare.

**Speaker Notes:**  
Outline c.

---

### Slide 8 – Split Claims
**Title:** One Paragraph, Two Codes

Hash seen in Zeek + EDR ≠  
“therefore China.”

Rate the **hash fact** and the **label** apart.

**Speaker Notes:**  
Usual fail.

---

### Slide 9 – Example 1: B3
**Title:** Example 1 – Known Zeek, One SNI

Source **B**. Claim **3**.  
Need a second line for a 1 or 2.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Not A1
**Title:** Example 2 – Vendor Blog

First-time blog + country flag.  
**F6** (or F5) on that sentence.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: F1
**Title:** Example 3 – Anonymous but Confirmed

Paste is **F**.  
Hash already in two internals → **1** on *that* fact.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- A1 vanity  
- Throwing away F  
- One code for hash + country  
- Using B as *likely*  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use the site card if posted.  
Keep: letter + number, two axes.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–D: assign.
3. E–F: explain C4 and F1.
4. Split two-claim paragraphs.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Letter vs number?
2. When F or 6?
3. Why can F1 be correct?
4. Why not A1 on a vendor PDF?
5. B2 vs likely / medium?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Letter = source. Number = this report.
- F and 6 are honest. A1 is rare.
- Next: **3.2.4** cognitive biases.

**Speaker Notes:**  
Do not open 3.2.4 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Admiralty — Quick Reference

| | 1 confirmed | 3 possible | 6 unknown |
|--|-------------|------------|-----------|
| **B** usually | B1 | B3 | B6 |
| **F** unknown | F1 | F3 | F6 |

**Coming next:** Module 3.2.4 – Cognitive biases

**Footer:** SOC / Hunter / CTI Training Program
