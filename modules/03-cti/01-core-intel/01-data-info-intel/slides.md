# Module 3.1.1 – Data, Information, and Intelligence  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.1.1 – Data, Information, and Intelligence  
**Subtitle:** CTI Analyst & Threat Hunter Training  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Write the three words on the board. Say they are not synonyms. This module is only the distinction and the categorization task.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Define data, information, and intelligence
2. Explain how raw data becomes intelligence
3. Categorize examples correctly
4. Spot “intel” that is still only data or information

**Mapped Items:**  
K: 3.1.1 | T: 3.1.1.1

**Speaker Notes:**  
CTI 3 is already at principles (B / 3c). Push them to sort messy, real-looking products.

---

### Slide 3 – Agenda
**Title:** Agenda

- Definitions and distinctions
- How data becomes intelligence
- Three worked examples
- Categorization practice
- Hands-on exercise
- Knowledge check

**Speaker Notes:**  
Quick roadmap. Lifecycle and PIRs are later.

---

### Slide 4 – Three Terms
**Title:** Data vs Information vs Intelligence

| Term | Answers | Typical form |
|------|---------|--------------|
| **Data** | What was recorded? | Log field, hash, IP, timestamp |
| **Information** | Who / what / when / where? | Timeline, parsed alert, related indicators |
| **Intelligence** | So what? What should we do? | Assessment + decision |

**Key Point:** Information describes. Intelligence judges.

**Speaker Notes:**  
Stay on this table until someone can give the distinction without reading it.

---

### Slide 5 – Same Event, Three Layers
**Title:** Same Event, Three Layers

- **Data:** a TLS log row (`id.orig_h`, `server_name`, timestamp)
- **Information:** which host, which user, what name, how long, what else happened
- **Intelligence:** we assess this is / is not the campaign; here is the action

**Analyst Tip:** Briefing the raw row is not producing intelligence.

**Speaker Notes:**  
This is the Example 1 preview. Come back to it in the walkthrough.

---

### Slide 6 – The Path
**Title:** How Raw Data Becomes Intelligence

```
Data  →  Information  →  Intelligence
 raw      context         judgment + decision
```

| Step | You add | You still lack |
|------|---------|----------------|
| Data → information | Time, asset, correlation | Meaning for the mission |
| Information → intelligence | Analysis against a requirement | A product, if you skip this |

**Key Point:** This is a process, not a rename.

**Speaker Notes:**  
Requirement = the question the work exists to answer. Do not teach PIR format here.

---

### Slide 7 – Common Mistakes
**Title:** Labeled “Intel,” Still Not Intelligence

- Pasted IOC list from a blog
- “12 vendors detect this hash”
- Headline: new ransomware family this morning
- Unreviewed vendor STIX import
- A closed ticket that only restates the alert

**Analyst Tip:** A lead is something to work. It is not an incident and not a finished product.

**Speaker Notes:**  
Ask for a local example. Then move to the three walkthroughs.

---

### Slide 8 – Example 1: Normal Path
**Title:** Example 1 – One Session, Three Products

**Data:** TLS row to `www.example.com`  
**Information:** finance workstation, matching SNI/cert, 8 seconds, quiet host  
**Intelligence:** not part of this morning’s phishing requirement; no containment

**Interpretation:**  
Only the last sentence is intelligence.

**Speaker Notes:**  
Ask students to label each layer before you reveal the interpretation.

---

### Slide 9 – Example 2: IOC Dump
**Title:** Example 2 – Chat Message Titled “CTI INTEL”

- Three indicators from a public blog
- “Block these now”
- No relevance, no confidence, no “so what for us”

**Interpretation:**  
**Data** (plus a claim). Treat as a **lead**. Do not brief it as finished intelligence.

**Speaker Notes:**  
The title is the trap. Volume is not insight.

---

### Slide 10 – Example 3: Two Write-ups
**Title:** Example 3 – Same Alert, Two Products

**A:** Fields + “JA3 on two malware lists.” Ticket closed as suspicious TLS.  
**B:** Answers “are we talking to the fake update CDN?” Judges C2/update likely. Names isolate + hunt. Moderate confidence.

**Interpretation:**  
A is **information**. B is **intelligence**. Extra fields did not promote A.

**Speaker Notes:**  
Force the test: requirement, judgment, decision.

---

### Slide 11 – Categorization Test
**Title:** Three Questions, In Order

1. Still a raw fact? → **data**
2. Organized or given context, not judged? → **information**
3. Answers a requirement with analysis and an implication? → **intelligence**

If you are unsure, it is not intelligence yet.

**Speaker Notes:**  
This replaces the network-log `uid` pivot from the Zeek modules. Same idea: a repeatable habit.

---

### Slide 12 – Sorting Habit
**Title:** Daily Sorting Habit

| You received | First label | Next step |
|--------------|-------------|-----------|
| Hash / IP / domain only | Data | Enrich and put in context |
| Timeline or parsed alert | Information | Analyze against a question |
| Assessment + action | Intelligence | Deliver or challenge it |
| Vendor bundle, unread | Data | Review before you forward |

**Speaker Notes:**  
Starting points only. Local TIP workflow is a later module.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. One-sentence summary of each example.
2. Categorize the six items in the student guide (reason each).
3. From the Example 1 TLS row, write one **information** sentence and one **intelligence** sentence that answers: *Is this host part of the lookalike-Microsoft activity?*

**Speaker Notes:**  
Let students work. Then review using the Instructor Guide answer key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. Difference between data and information?
2. What must be present before information becomes intelligence?
3. Why is a public IOC list not intelligence by itself?
4. Categorize the self-signed lookalike sentence.
5. Categorize the “isolate and hunt” sentence.

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Data = raw record. Information = organized story. Intelligence = judged answer.
- You cannot rename a feed and call it intelligence.
- Path: add context, then add analysis and a decision.
- A lead is not an incident and not a finished product.
- If you cannot name the question and the action, you are not done.

**Speaker Notes:**  
Reinforce once. Do not reopen lifecycle.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 3.1.2 – Intelligence lifecycle

**Resources:**
- Student Guide for this module
- Local assessment style guide (when published)

**Speaker Notes:**  
Park PIR, types, and attribution questions for later units.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** Data / Information / Intelligence Quick Reference

**Test:** raw fact → **data** · context only → **information** · judgment + decision → **intelligence**

**Promote a product only when you can say:**
- the question you answered
- what you think is true
- what someone should do

**Core habit:**  
Label it first. Then decide whether to enrich, analyze, or deliver.

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the three-term table large enough to read
- Visually separate Data / Information / Intelligence (one color each is enough)
- Consistent footer with module number
- Minimal text — let the three examples teach
