# Module 3.1.2 – Intelligence Lifecycle  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.1.2 – Intelligence Lifecycle  
**Subtitle:** CTI Analyst & Threat Hunter Training  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Draw an empty circle on the board. This module is the stages, the job of each stage, and the flow. Not PIR writing. Not intel types.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Name the stages and the purpose of each
2. Describe typical activities in each stage
3. Identify the stage of a given activity
4. Describe the flow as a loop, not a pipeline

**Mapped Items:**  
K: 3.1.2 | T: 3.1.2.1

**Speaker Notes:**  
CTI 3 is already at principles (B / 3c). Push them to place messy, real-looking work.

---

### Slide 3 – Agenda
**Title:** Agenda

- Six stages and their purpose
- Activities in each stage
- Flow, loops, and skips
- Three worked examples
- Stage-identification practice
- Hands-on exercise
- Knowledge check

**Speaker Notes:**  
Quick roadmap. Types and PIRs are later.

---

### Slide 4 – Six Stages
**Title:** Stages of the Intelligence Lifecycle

1. Planning and Direction  
2. Collection  
3. Processing and Exploitation  
4. Analysis and Production  
5. Dissemination  
6. Evaluation and Feedback  

**Key Point:** A stage is a job, not a folder name.

**Speaker Notes:**  
Hold this naming. If the site uses five names, the work still has to happen.

---

### Slide 5 – Purpose of Each Stage
**Title:** Why Each Stage Exists

| Stage | Purpose |
|-------|---------|
| Planning and Direction | The question and what “done” looks like |
| Collection | Raw material for that question |
| Processing and Exploitation | Usable information |
| Analysis and Production | Judgment and a product |
| Dissemination | Get it to people who can act |
| Evaluation and Feedback | Did they use it? What next? |

**Speaker Notes:**  
Stay on purpose until someone can say it without the table.

---

### Slide 6 – Same Path, Inside the Cycle
**Title:** Data / Information / Intelligence Live Here

| Stage | Usual product |
|-------|----------------|
| Collection | Data |
| Processing and Exploitation | Information |
| Analysis and Production | Intelligence |
| Dissemination | That intelligence, delivered |

**Analyst Tip:** Renaming a feed does not move you to analysis.

**Speaker Notes:**  
This is the 3.1.1 reminder. Do not reteach the three terms.

---

### Slide 7 – The Flow
**Title:** It Is a Cycle

```
Plan/Direct → Collect → Process → Analyze/Produce → Disseminate
        ↑                         ↓
        └──── Feedback ←──────────┘
              (and back to collection when analysis finds a gap)
```

**Key Point:** Returning a stage is normal. Skipping a stage is the failure.

**Speaker Notes:**  
Draw the back-arrow from analysis to collection on the board.

---

### Slide 8 – Common Skips
**Title:** Work That Never Completes the Cycle

- Blog IOC paste titled “CTI INTEL”
- 400 hashes in the TIP, no question on the ticket
- Long narrative with no recipient
- Polished brief of unprocessed indicators

**Analyst Tip:** A lead is an entry point. It is not an incident and not a finished cycle.

**Speaker Notes:**  
Ask for a local example. Then move to the three walkthroughs.

---

### Slide 9 – Example 1: Full Loop
**Title:** Example 1 – One Question, Six Jobs

**Question:** Are endpoints talking to the fake update CDN names?

- Plan the window and what “done” means
- Collect DNS/TLS and TIP hits
- Process one timeline; drop duplicates
- Assess two lab hosts vs one false overlap; recommend hunt + watch
- Disseminate hunt package and SOC brief
- Feedback: a fourth host → tighter next collection

**Interpretation:**  
The product appears after analysis. The fourth host is the cycle working.

**Speaker Notes:**  
Ask students to name each stage before you reveal the table.

---

### Slide 10 – Example 2: IOC Dump
**Title:** Example 2 – Chat Message Titled “CTI INTEL”

- Three indicators from a public blog
- “Block these now”
- No question, no processing, no analysis of *us*

**Interpretation:**  
**Collection**, then a fake **dissemination**. Treat as a **lead**. Put it back at planning or collection.

**Speaker Notes:**  
Same trap as 3.1.1. Now score it as a stage problem.

---

### Slide 11 – Example 3: Two Weeks of Work
**Title:** Example 3 – Same Topic, Two Stage Maps

**A:** 412 hashes, 60 domains, no requirement. Status: “intel updated.”  
**B:** Which families run on our image? Process three. Assess one relevant. Disseminate. Feedback changes next collection.

**Interpretation:**  
A is **collection** with no direction. B completes the **flow**.

**Speaker Notes:**  
Volume is not a lifecycle.

---

### Slide 12 – Stage Test
**Title:** Place the Work

Ask, in order:

1. Is this the question / “done”? → **Planning and Direction**
2. Is this raw intake? → **Collection**
3. Organized, not judged? → **Processing**
4. Judgment + so what? → **Analysis and Production**
5. Delivered to someone who can act? → **Dissemination**
6. Used, missed, or next question? → **Evaluation and Feedback**

If you are unsure, it is not analysis yet.

**Speaker Notes:**  
This replaces the network-log `uid` pivot from the Zeek modules. Same idea: a repeatable habit.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. One-sentence summary of each example (stages done vs skipped).
2. Identify the primary stage of the six items in the student guide (reason each).
3. Describe the **flow** for: hunt sends one suspicious SNI and asks if it is in a known cluster. Include a possible return or feedback step.

**Speaker Notes:**  
Let students work. Then review using the Instructor Guide answer key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. Name the six stages in order.
2. Purpose of planning and direction?
3. Why is this not a one-way pipeline?
4. Stage: normalize three vendor reports and attach owners.
5. Stage: brief SOC with an assessment and a hunt action.

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Six jobs: plan, collect, process, analyze, disseminate, feedback.
- Collection → data. Processing → information. Analysis → intelligence.
- The flow loops. Gaps send you back. Feedback starts the next question.
- Skipping a stage is the usual failure.
- A lead is an entry point, not a finished cycle.

**Speaker Notes:**  
Reinforce once. Do not open PIR format.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 3.1.3 – Intelligence types

**Resources:**
- Student Guide for this module
- Local production / dissemination process (unit 3.11, when published)

**Speaker Notes:**  
Park PIR, types, and collection-source questions for later units.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** Intelligence Lifecycle Quick Reference

**Stages:** Plan/Direct · Collect · Process · Analyze/Produce · Disseminate · Feedback

**Place work by the job, not the label:**
- question / done → direction
- raw pull → collection
- cleanup / timeline → processing
- judgment + action → analysis
- delivered → dissemination
- used or missing → feedback

**Core habit:**  
Name the stage first. Then do the next missing job — or go back.

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the six-stage list large enough to read
- Draw the cycle (including the back-arrow) as a visual, not only bullets
- Consistent footer with module number
- Minimal text — let the three examples teach
