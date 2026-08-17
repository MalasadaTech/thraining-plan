# Module 3.1.3 – Intelligence Types  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.1.3 – Intelligence Types  
**Subtitle:** CTI Analyst & Threat Hunter Training  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Write the four types on the board. This module is the types and the classify task. Not PIR writing. Not “actionable” checklists.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Define the four intelligence types
2. State the question and consumer for each
3. Classify a product or requirement by type
4. Spot a mislabeled product

**Mapped Items:**  
K: 3.1.3 | T: 3.1.3.1

**Speaker Notes:**  
CTI 3 is already at principles (B / 3c). Push them to sort messy, real-looking products.

---

### Slide 3 – Agenda
**Title:** Agenda

- Four types, four jobs
- Strategic and operational
- Tactical and technical
- Three worked examples
- Classification practice
- Hands-on exercise
- Knowledge check

**Speaker Notes:**  
Quick roadmap. Requirements and “actionable” are later.

---

### Slide 4 – Four Types
**Title:** Type Follows the Decision

| Type | Unlocks |
|------|---------|
| **Strategic** | Posture, investment, accepted risk |
| **Operational** | How to run the campaign / hunt / incident |
| **Tactical** | What to do *now* |
| **Technical** | What we can detect or pivot on |

**Key Point:** A long PDF is not automatically strategic.

**Speaker Notes:**  
Stay on this table until someone can give the distinction without reading it.

---

### Slide 5 – Not a Lifecycle Stage
**Title:** Type ≠ Stage

- Lifecycle = where you are in the loop (collect, analyze, disseminate…)
- Type = what kind of answer you are producing
- You can collect technical data for a strategic question

**Analyst Tip:** Type applies to intelligence (and to the requirement). A raw IOC list is still data.

**Speaker Notes:**  
One reminder of 3.1.1 / 3.1.2. Do not reteach the cycle.

---

### Slide 6 – Strategic vs Operational
**Title:** Strategic vs Operational

**Strategic:** Should we change risk, funding, or posture?  
**Operational:** How do we run *this* body of work for days to weeks?

| Clue | Strategic | Operational |
|------|-----------|-------------|
| Consumer | Exec / program owner | IR, hunt, CTI lead |
| Horizon | Months to years | Days to weeks |
| Output | Implication for the mission | Sequencing and focus |

**Speaker Notes:**  
“Nation-state” is a subject, not a type.

---

### Slide 7 – Tactical vs Technical
**Title:** Tactical vs Technical

**Tactical:** What should SOC/hunt/IR do about this activity tonight?  
**Technical:** What are the observables we can detect or pivot on?

| Item | Type |
|------|------|
| Isolate host; hunt this cluster | Tactical |
| JA3 + SNI + port, no action | Technical |
| Unreviewed hash paste | Data, not a type yet |

**Analyst Tip:** A hash dump is not tactical intelligence.

**Speaker Notes:**  
Operators need both. Shipping only technical is the usual miss.

---

### Slide 8 – Classification Test
**Title:** What Decision Does This Unlock?

1. Posture / investment / accepted risk? → **Strategic**
2. How to run the week’s campaign or hunt? → **Operational**
3. Immediate action on this activity? → **Tactical**
4. Detect / pivot mechanics? → **Technical**

If it is still a raw fact, it is not a type yet.

**Speaker Notes:**  
This replaces the network-log `uid` pivot from the Zeek modules. Same idea: a repeatable habit.

---

### Slide 9 – Example 1: One Campaign, Four Products
**Title:** Example 1 – Same Cluster, Four Types

- **Strategic:** fund the extra TLS sensor this quarter
- **Operational:** 10-day hunt; lab first, then finance
- **Tactical:** isolate 10.10.22.17; hunt the SNI/cert pair
- **Technical:** SNI + TLS 1.0/RC4/8443 + JA3

**Interpretation:**  
Four decisions. Do not send the JA3 row to a director.

**Speaker Notes:**  
Ask students to label each product before you reveal the table.

---

### Slide 10 – Example 2: Mislabeled Brief
**Title:** Example 2 – Slide Titled “STRATEGIC INTEL”

- Three indicators from a public blog
- “Block these now”
- Nation-state name on the cover

**Interpretation:**  
**Technical data** (plus a claim). Classify what it is, not the title. Treat as a **lead**.

**Speaker Notes:**  
Same paste trap as 3.1.1 / 3.1.2. Now score it as a type problem.

---

### Slide 11 – Example 3: Two Requirements
**Title:** Example 3 – Same Indicators, Two Questions

**A:** Buy extra EDR this quarter, or accept the ransomware risk?  
**B:** What do we hunt and isolate tonight?  
**Shipped:** three hashes, TIP updated.

**Interpretation:**  
A is **strategic**. B is **tactical**. The product is a **technical** dump. Requirement and product do not match.

**Speaker Notes:**  
Force two classifications. That mismatch is the point.

---

### Slide 12 – Daily Sorting Habit
**Title:** Daily Sorting Habit

| You received | First label | Next step |
|--------------|-------------|-----------|
| Executive risk question | Strategic requirement | Produce a posture answer |
| “How do we run this hunt week?” | Operational | Sequence the work |
| “What do we do to this host?” | Tactical | Judge an action |
| Hash / JA3 / SNI only | Technical (or data) | Analyze, then decide if action is needed |

**Speaker Notes:**  
Starting points only. PIR format is the next module.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. One-sentence summary of each example (claimed type vs actual).
2. Classify the six items in the student guide (reason each).
3. From the Example 1 technical row, write one **tactical** sentence and one **strategic** sentence.

**Speaker Notes:**  
Let students work. Then review using the Instructor Guide answer key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. What question does strategic answer that tactical does not?
2. Tactical vs technical?
3. Why is a long APT PDF not automatically strategic?
4. Classify the 10-day hunt series.
5. Classify the SNI / JA3 / port row.

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Four types: strategic, operational, tactical, technical.
- Type follows the decision, not the filename.
- Same campaign can produce all four. Types are not stages.
- A labeled “strategic brief” of indicators is still technical data.
- Classify the requirement and the product separately.

**Speaker Notes:**  
Reinforce once. Do not open PIR format.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 3.1.4 – Intelligence requirements

**Resources:**
- Student Guide for this module
- Local product catalog / naming (when published)

**Speaker Notes:**  
Park PIR, actionable, and audience questions for later units.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** Intelligence Types Quick Reference

**Test:** posture → **strategic** · how we run the work → **operational** · do this now → **tactical** · detect/pivot → **technical**

**Classify only when you can say:**
- the decision this unlocks
- who acts on it
- whether it is still only data

**Core habit:**  
Name the type first. Then write the product that matches the question.

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the four-type table large enough to read
- Visually separate Strategic / Operational / Tactical / Technical (one color each is enough)
- Consistent footer with module number
- Minimal text — let the three examples teach
