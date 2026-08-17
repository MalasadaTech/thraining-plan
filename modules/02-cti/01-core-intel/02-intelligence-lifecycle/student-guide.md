# Module 3.1.2 – Intelligence Lifecycle

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- CTI: 3-level (B/3c) → 5-level (C/4c) → 7-level (C/4c)  
- Hunter: A/1a → B/2b → B/3c  
- SOC: awareness only (A / 1a)  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the stages of the intelligence lifecycle and state the purpose of each stage.
2. Describe typical activities that belong in each stage.
3. Identify which stage a given activity belongs to.
4. Describe the flow of the lifecycle, including loops and feedback — not a one-way pipeline.

**Mapped Proficiency Items:**
- K: 3.1.2 – Intelligence lifecycle
- T: 3.1.2.1 – Identify the lifecycle stage of an activity and describe the flow

---

## 1. Key Concepts

### 1.1 Stages of the Intelligence Lifecycle

The lifecycle is how a question becomes a used answer. It is the process around the data → information → intelligence path you already know. That path lives mainly in processing and analysis. The lifecycle is the whole loop.

Shops name the stages slightly differently. This course uses six stages. If your site collapses two names, the work still has to happen.

| Stage | Purpose (why it exists) |
|-------|-------------------------|
| **Planning and Direction** | Decide what question matters, what “done” looks like, and how the effort will run |
| **Collection** | Gather the raw material needed to answer that question |
| **Processing and Exploitation** | Turn raw intake into usable information |
| **Analysis and Production** | Judge what it means and write the answer |
| **Dissemination** | Get the answer to the people who can act |
| **Evaluation and Feedback** | Learn whether it was used, what was missing, and what to do next |

**Most critical distinction for daily work:**  
A stage is a *job*, not a folder name. Putting indicators in a TIP is not analysis. Sending a chat titled “INTEL” is not dissemination of intelligence.

### 1.2 Purpose and Activities in Each Stage

| Stage | What you add | Typical activities | You are not done if… |
|-------|----------------|--------------------|----------------------|
| **Planning and Direction** | A question, scope, and priority | Accept or refine a requirement; set time window, sources, and the decision the product must support | You are collecting “whatever looks interesting” |
| **Collection** | Raw observations against the question | Pull logs, TIP records, tickets, vendor or public reporting, hunt output | You collected a pile with no tie to the question |
| **Processing and Exploitation** | Usable information | Parse, normalize, enrich, deduplicate, translate, build a timeline | You still have raw files, unreadable dumps, or unmerged copies of the same indicator |
| **Analysis and Production** | Judgment and a product | Compare alternatives, state confidence, answer the question, name the “so what” | You only restated the timeline |
| **Dissemination** | Delivery to a consumer who can act | Brief, ticket, TIP entry, hunt package, watchlist — to the right people | The product sits in your notes |
| **Evaluation and Feedback** | A check on use and gaps | Ask what the consumer did; record misses; open or revise the next requirement | You never learn whether anyone used it |

How this maps to terms from the last module:

| Lifecycle stage | Usual product |
|-----------------|---------------|
| Collection | **Data** |
| Processing and Exploitation | **Information** |
| Analysis and Production | **Intelligence** |
| Dissemination | That intelligence, delivered |
| Evaluation and Feedback | Whether it worked, and the next question |

Collection sources (OSINT vs commercial vs internal) and how to write a PIR are later modules. Here you only need: collection is driven by a question, and the question is set in planning and direction.

### 1.3 Flow of the Lifecycle

The picture is a cycle, not a slide deck that you walk through once.

```
Planning and Direction
        ↓
    Collection  ←——————— more collection if analysis finds a gap
        ↓
Processing and Exploitation
        ↓
Analysis and Production
        ↓
    Dissemination
        ↓
Evaluation and Feedback ———→ back to Planning and Direction
```

| Rule | What it means in practice |
|------|---------------------------|
| It loops | Feedback creates a new or tighter question. That is success, not rework. |
| You can return a stage | Analysis often sends you back to collection. That is still the same cycle. |
| Skipping a stage fails | Collecting and pasting is not a product. Analyzing with no question is not direction. |
| Later stages do not fix earlier skips | A polished brief of unprocessed IOCs is still not intelligence. |

Common failure: people treat the first four stages as optional and start at dissemination.

| What they did | Stage they actually performed | What they skipped |
|---------------|-------------------------------|-------------------|
| Forwarded a blog IOC list as “CTI INTEL” | Collection (then a leaky disseminate) | Direction, processing, analysis, feedback |
| Enriched 40 hashes and stopped | Processing | Analysis against a requirement |
| Wrote a long narrative with no recipient | Analysis / production | Dissemination and feedback |
| Scraped feeds all week with no question | Collection | Planning and direction |

A lead is permission to *enter* the cycle (usually at collection or processing). It is not an incident and it is not a finished product.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (One Question, Full Loop)

**Requirement (already given):** Are any endpoints talking to the “fake update CDN” names from this week’s report?

| Stage | What happened |
|-------|----------------|
| Planning and Direction | CTI accepts the question. Scope: last 7 days, internal DNS/TLS plus the report’s names. Done means: which hosts, if any, and what SOC/hunt should do. |
| Collection | Pull DNS and TLS for those names. Export matching TIP hits. Request the original report indicators. |
| Processing and Exploitation | Build one timeline. Tag asset owners. Drop duplicate hashes. Mark one name as a known CDN overlap. |
| Analysis and Production | Assess two lab VLANs as likely testing the domain, one finance host as a false overlap. Moderate confidence. Recommend hunt of the remaining names and a 24-hour SOC watch. |
| Dissemination | Hunt package to hunt; watchlist + two-paragraph brief to SOC. |
| Evaluation and Feedback | SOC finds a fourth host the next shift. CTI tightens the window and adds that host’s JA3 to the next collection pass. |

**Interpretation:**  
Same campaign question, six jobs. The useful product appears only after analysis. The fourth host is not a failure of the first pass — it is the cycle working. Do not brief the raw DNS hits from the collection step and call the job done.

### Example 2: IOC Dump Sent as Finished Intel (Lead)

A chat message to hunt and SOC:

> CTI INTEL: New APT activity. Block these now.  
> `45.76.12.88`  
> `update.not-a-real-cdn.example`  
> `6734f37431670b3ab4292b8f60f29984`  
> Source: public blog, posted today.

**Interpretation:**  
This activity sits in **collection** (raw intake) and then jumps to a fake **dissemination**. There is no stated question, no processing into one picture, and no analysis of relevance here. “Block these now” is an instruction, not a judged answer. Treat it as a **lead**: put it at planning (“does this report apply to us?”) or collection, then run the rest of the cycle. Shipping the paste trains consumers to think the cycle has only one stage.

### Example 3: Two Weeks of Work, Two Different Stages (Lead)

**Write-up A**

> Spent the week pulling every ransomware blog. 412 hashes and 60 domains are in the TIP. No requirement on the ticket. Status: “intel updated.”

**Write-up B**

> Requirement: which of this week’s ransomware families can run on our Windows 10 image?  
> Processed the three families that name that image. We assess Family R is relevant (packaged installer matches our software shop); Families S and T are not.  
> Disseminated a one-page note to IR and detections. Feedback: detections asked for the installer hash only — next collection will ignore the rest of the dump.

**Interpretation:**  
A is **collection** with no direction. Volume is not a lifecycle. B starts at **planning and direction**, moves through processing and analysis, **disseminates**, and uses **feedback** to change the next collection. Same topic area, only B completed the flow.

---

## 3. Hands-On Exercise

**Objective:** Practice naming stages and describing the flow.

**Instructions:**

1. Review the three examples above and write a one-sentence summary for each (which stages were done, and which were skipped).
2. Identify the **primary stage** for each activity below. Give one reason.
   - A director asks: “Are we seeing the lookalike-Microsoft campaign?”
   - You export every TLS row for three SNIs from the last 48 hours
   - You merge three vendor lists, drop duplicates, and add asset owners
   - You assess two hosts are likely in that campaign and recommend isolation
   - You send the assessment to SOC and hunt in the agreed ticket form
   - SOC replies that the product was used and they still need the certificate pair
3. In four sentences or fewer, describe the **flow** for this situation: hunt sends you a single suspicious SNI and asks whether it is part of a known cluster. Start at the stage you enter, name the next stages, and say what would send you backward.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six stage identifications with a reason each
- A flow description that is a loop (includes a possible return to collection or a feedback step), not a one-way list of file names

---

## 4. Knowledge Check

1. Name the six stages of the intelligence lifecycle in order.
2. What is the purpose of planning and direction?
3. Why is the lifecycle not a one-way pipeline?
4. Identify the stage: “Normalize three vendor reports onto one indicator table and attach asset owners.”
5. Identify the stage: “Brief SOC: we assess two hosts are in the campaign; hunt this certificate pair.”

---

## 5. Summary

- The lifecycle is six jobs: plan/direct, collect, process, analyze/produce, disseminate, evaluate/feedback.
- Each stage has a purpose. Collection makes data. Processing makes information. Analysis makes intelligence. Dissemination delivers it. Feedback starts the next loop.
- The flow is a cycle. Analysis may send you back to collection. Feedback should change the next question.
- Skipping a stage is the usual failure: a paste is not a product.
- A lead is an entry point. It is not an incident and it is not a finished cycle.

---

## 6. References & Further Reading

- Related modules:
  - 3.1.1 – Data, information, and intelligence (previous)
  - 3.1.3 – Intelligence types (next)
  - 3.1.4 – Intelligence requirements
  - 3.1.8 – Collection sources and methods
- Internal production and dissemination process (when published; depth is unit 3.11)
- Joint / ODNI primers on the intelligence cycle (use the local copies)
