# Module 1.4.3 – Common False Positive Causes  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.4.3 – Common False Positive Causes  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Already an FP. Class + change. Do not deploy.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Name cause classes **a** and **b**
2. Given an FP: class **and** what you would change

**Mapped Items:**  
K: 1.4.3.1 | T: 1.4.3.2

**Speaker Notes:**  
CTI is 1a / 1a / 2b.

---

### Slide 3 – Agenda
**Title:** Agenda

- Fence with 1.4.2
- Two classes
- Three worked examples
- Four FPs
- Knowledge check

**Speaker Notes:**  
1.4.4 is later.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Re-arguing TP vs FP (**1.4.2**)  
Shipping SIGMA/Suricata (**1.3**)  
Scan / root / user (**1.4.4**)  
“Tune it” with no selector

**Key Point:** Class + one concrete change.

**Speaker Notes:**  
Fence.

---

### Slide 5 – After the Label
**Title:** Starts After FP

1.4.2 already said **FP**.  
Now: **why that class** + **what changes**.

**Speaker Notes:**  
Do not reopen the 2×2.

---

### Slide 6 – Class a
**Title:** Analyst or Tool Activity

Lab replay, hunter sample download,  
DE testing a **live** rule, owned scanner.

**Change:** exclude range / window / identity.  
Do not delete the production detection.

**Speaker Notes:**  
Outline a.

---

### Slide 7 – Class b
**Title:** Untuned or Overly Broad Logic

Any PowerShell. Raw TCP `GET`. MZ-only YARA on an alert.

**Change:** add a second selector; bind a buffer; raise a threshold.

**Speaker Notes:**  
Outline b.

---

### Slide 8 – Other
**Title:** Other — Not a/b

Clock skew, bad intel, etc.  
Say **other — not a/b**. Still name a change.  
Do not invent a third official class.

**Speaker Notes:**  
One beat.

---

### Slide 9 – Example 1: Replay
**Title:** Example 1 – Packet Replay

- Lab replay of GET update.exe
- **a** + tag/exclude broker

**Interpretation:**  
Keep the sid. Stop the page.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Any PS
**Title:** Example 2 – Get-Help

- **b** + require `-enc` and script-host parent

**Interpretation:**  
Propose the 1.3.1 Ex 1 shape. Do not publish.

**Speaker Notes:**  
Concrete selector.

---

### Slide 11 – Example 3: Both Stories
**Title:** Example 3 – 3-level Tested Live Rule

- Event in front of you = the test → primary **a**
- Export path may also be **b** (second ticket)

**Interpretation:**  
Primary class = this row.

**Speaker Notes:**  
Don’t force a tie.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Relitigating TP  
- Live user called “analyst”  
- “Tune it”  
- Full YAML deploy  
- Categories  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Change Lines
**Title:** What a Change Looks Like

Good: “Add `http.uri` + GET.”  
Good: “Allow-list scanner 10.10.8.90.”  
Bad: “Tune the rule.”  

**Speaker Notes:**  
Leave up.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–D: class + one change.
3. No TP. No category.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Two cause classes?
2. Why not classify again?
3. What makes a change acceptable?
4. When “other — not a/b”?
5. Who deploys?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- After FP: class + change.
- **a** analyst/tool. **b** broad/untuned.
- Next: categories (**1.4.4**).

**Speaker Notes:**  
Do not open 1.4.4 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** FP Causes — Quick Reference

| Class | Change toward |
|-------|----------------|
| a | Exclude lab / replay / scanner identity |
| b | Second selector / buffer / threshold |
| other | Say so; still name a change |

**Coming next:** Module 1.4.4 – Common alert categorizations

**Footer:** SOC / Hunter / CTI Training Program
