# Module 2.2.1 – Hunt Types  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.2.1 – Hunt Types  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Ask for hunt types before definitions. This lesson is types + first execute move. Not hypothesis writing. Not tool labs.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Name the four hunt types and the input that starts each
2. Separate a reactive hunt from SOC work on an alert
3. Separate hypothesis-driven from anomaly-based
4. Execute by type: first search and hand-back

**Mapped Items:**  
K: 2.2.1 | T: 2.2.1.1–2.2.1.4

**Speaker Notes:**  
Hunter 3 is already at principles (B / 3c). Push classification from the input.

---

### Slide 3 – Agenda
**Title:** Agenda

- Four hunt types
- Execute by type (and traps)
- Three worked examples
- Identification practice
- Hands-on exercise
- Knowledge check

**Speaker Notes:**  
2.2.2 (develop / scope / prioritize) is next. Point forward if they go there.

---

### Slide 4 – Type Follows Input
**Title:** Hunt Type Is the Start, Not the Title

Name the type from **what started the work**.

**Key Point:** The label in the hunt channel is not the type.

**Speaker Notes:**  
Leave this sentence up. Same label-vs-job trap as 2.1.

---

### Slide 5 – Four Types
**Title:** The Four Hunt Types

| Type | Starts from |
|------|-------------|
| **Intel-driven** | Report / IOC / named TTP set |
| **Hypothesis-driven** | If/then you can test (see Y) |
| **Reactive** | Spark that is not finished SOC work |
| **Anomaly-based** | Baseline + deviation detections ignore |

**Analyst Tip:** Changing type mid-hunt is allowed if you say so.

**Speaker Notes:**  
Have students fill “starts from” before you reveal the column.

---

### Slide 6 – First Execute Move
**Title:** Execute (This Lesson)

1. **Type** — from the input
2. **First search** — what, where, how long
3. **Quiet** — only where you could see
4. **Hand-back** — lead, gap, or bounded quiet

**Key Point:** A lead is not an incident. This is not a 2.2.2 hunt plan.

**Speaker Notes:**  
SOC/CTI only need to recognize the four sentences, not run the hunt.

---

### Slide 7 – Traps
**Title:** These Are Not Types

- High queue with a new title → **SOC**, not reactive
- Report title, no search → not intel-driven
- “I hypothesize scheduled tasks” and no Y → not hypothesis-driven yet
- “Looks weird” and no baseline → not anomaly-based
- Broader if/then still labeled intel → **type changed**; say it

**Speaker Notes:**  
Stay here until reactive ≠ queue is solid.

---

### Slide 8 – Sorting Habit
**Title:** What Started This?

1. Named objects from intel? → **Intel-driven**
2. If/then with a searchable Y? → **Hypothesis-driven**
3. Spark, looking for unalerted related activity? → **Reactive**
4. Baseline + deviation? → **Anomaly-based**
5. Already-raised alerts? → **Not a hunt**

**Speaker Notes:**  
This is the habit slide. Same job as 2.1’s gap sort.

---

### Slide 9 – Example 1: Intel-Driven
**Title:** Example 1 – Bulletin Names

- Bulletin: `update.not-a-real-cdn.example`
- DNS/TLS, 7 days, user + finance
- `10.10.22.17` for 14 nights; no ticket
- Lab DNS still dark

**Interpretation:**  
**Intel-driven** execute. Lead + **detection gap**. Do not claim lab is clean.

**Speaker Notes:**  
Students name the type before you reveal the interpretation.

---

### Slide 10 – Example 2: “Reactive”
**Title:** Example 2 – Two Morning Messages

**A:** Re-pull High EDR; close the queue.  
**B:** IR host from last week; hunt **unalerted peers** for the same parent / JA3.

**Interpretation:**  
A is **SOC**. B is a **reactive hunt**. The spark is the IR host, not the queue.

**Speaker Notes:**  
Same bait as 2.1’s “morning hunt.”

---

### Slide 11 – Example 3: Anomaly vs Slogan
**Title:** Example 3 – Two Write-ups

**A:** Anomaly hunt: attackers use scheduled tasks. Zero hits. Clean.  
**B:** 30-day baseline = no new tasks on Building C servers. Overnight two SYSTEM tasks on `SRVpay02`. Lab has no process logs.

**Interpretation:**  
A has no baseline and no Y. B is **anomaly-based** execute.

**Speaker Notes:**  
Force the sentence: no baseline, not this type.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Hunt type = tool name
- Reactive = extra triage
- Anomaly = “weird”
- Hypothesis = a slogan
- Writing a full priority memo when asked for the first search

**Speaker Notes:**  
Ask for a local mislabeled hunt. Then move to the exercise.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide (reason each).
3. Four-sentence execute for one intel-driven and one anomaly-based item.

**Speaker Notes:**  
Park 2.2.2-style plans. Review with the Instructor Guide key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. Four types and the input for each?
2. Why is last night’s queue not reactive?
3. Hypothesis-driven vs anomaly-based?
4. Bulletin names in DNS/TLS — type and hand-back if rows and no alert?
5. New SYSTEM tasks vs a 30-day none baseline — type, and a dark segment?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Four types. Type follows the input.
- Execute = type + first search + honest quiet + hand-back.
- Reactive ≠ SOC. Anomaly needs a baseline. Hypothesis needs a Y.
- Changing type is allowed if you say so.
- Writing / scope / priority → **2.2.2**.

**Speaker Notes:**  
Do not open development concepts.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 2.2.2 – Hunt development concepts

**Resources:**
- Student Guide for this module
- Module 2.1 – Purpose of Threat Hunting

**Speaker Notes:**  
Park VT, STIX, ATT&CK, persistence.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** Hunt Types Quick Reference

| Type | Input | First move |
|------|--------|------------|
| Intel-driven | Objects / named TTPs | Search the objects |
| Hypothesis-driven | If X then Y | Search for Y |
| Reactive | Spark, not the queue | Unalerted related activity |
| Anomaly-based | Baseline + deviation | Peers vs baseline |

**Test:** already alerted → SOC, not a type

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the four-type table large enough to read
- Visually separate reactive from SOC
- Consistent footer with module number
- Minimal text — let the three examples teach
