# Instructor Guide – Module 3.1.2 – Intelligence Lifecycle

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:** CTI B/3c → C/4c → C/4c | Hunter A/1a → B/2b → B/3c | SOC A/1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on stage identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the stages of the intelligence lifecycle, the purpose and activities in each stage, and make students practice placing work in the right stage and describing the flow as a loop.

**Key Teaching Points:**
- Six stages: planning and direction, collection, processing and exploitation, analysis and production, dissemination, evaluation and feedback.
- A stage is a job, not a folder or a chat title.
- Collection yields data. Processing yields information. Analysis yields intelligence. That is the 3.1.1 path *inside* this cycle.
- The flow loops. Feedback and collection gaps are normal.
- Stay out of PIR format, intelligence types, and collection-source classes. Point forward if asked.

**Common Student Challenges:**
- Treating the cycle as a one-way checklist.
- Calling any TIP update or IOC paste “dissemination of intelligence.”
- Collapsing processing and analysis into one step.
- Starting at collection with no question, then blaming analysis when the product is unused.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard or shared doc for live stage-sorting
- Answer key (this guide)

---

## Learning Objectives

1. Name the stages of the intelligence lifecycle and state the purpose of each stage.
2. Describe typical activities that belong in each stage.
3. Identify which stage a given activity belongs to.
4. Describe the flow of the lifecycle, including loops and feedback — not a one-way pipeline.

**Mapped Items:**
- K: 3.1.2 – Intelligence lifecycle
- T: 3.1.2.1 – Identify the lifecycle stage of an activity and describe the flow

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Draw the empty cycle on the board |
| Stages of the lifecycle        | 10 min   | Six names + one-line purpose |
| Purpose and activities         | 12 min   | Table; tie to data / information / intelligence |
| Flow (loops and skips)         | 8 min    | Failures live here |
| Walkthrough Examples           | 14 min   | Interactive; students speak first |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 6 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~72 min** | Cut an example if the room is already mapping cleanly |

---

## Detailed Teaching Notes

### 1. Stages of the Intelligence Lifecycle

**Talking Points:**
- Site names vary (five vs six stages; “processing” vs “processing and exploitation”). Hold the six-stage table as the course standard.
- Do not invent a seventh sign-off stage. If someone raises “requirements definition” as its own cycle, park it under planning and direction; PIR writing is 3.1.4.
- SOC and hunt often live in collection and processing. CTI is paid to run the whole loop.

**What to emphasize:**
- Purpose first, then activities. Students who only memorize names will fail the task.
- Reuse 3.1.1: same campaign can be data, information, or intelligence depending on the stage.

**Questions to ask the class:**
- “If I dump a blog IOC list into chat, which stage did I actually do?”
- “What would have to be true before that dump is dissemination?”

### 2. Purpose and Activities in Each Stage

**Talking Points:**
- Planning and direction is a question plus “done.” It is not a project plan template.
- Processing is still information: parse, enrich, timeline. Analysis is the judgment.
- Dissemination is delivery to someone who can act. A note to yourself is not dissemination.
- Feedback is a stage, not a courtesy. Unused product is a cycle failure.

**What to emphasize:**
- Collection sources and PIR format are later. Here: collection is driven by a question.
- The “you are not done if…” column is the teaching point, not the activity list.

**Question to ask:**  
“Where does this work stop, and what is the next missing stage?”

### 3. Flow

**Talking Points:**
- Draw the loop. Add a back-arrow from analysis to collection.
- Skipping is the usual outage, not “wrong order of two valid stages.”
- A lead is an entry point, usually collection or processing.

**What to emphasize:**
- Returning to collection is not failure.
- Later polish does not repair a skipped question.

### 4. Examples

Work through all three interactively. Ask students to name stages before you read the interpretation.

**Extra point for Example 1:**  
Full loop, including feedback that changes the next collection. If they only remember one thing, make it this.

**Extra point for Example 2:**  
The word INTEL in the chat title is the trap. Same artifact as 3.1.1 Example 2, now scored as a *stage* problem (collection + fake disseminate).

**Extra point for Example 3:**  
Write-up A looks like a week of CTI work. Volume is still only collection. Force the “which stages are missing?” test.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- Review answers as a group afterward. Do not collect a grade.

**What good answers look like:**

**Summaries:**
- Example 1: All six stages for one question; feedback adds a fourth host and a new collection pass.
- Example 2: Collection (plus a fake disseminate); direction, processing, analysis, and feedback skipped; treat as a lead.
- Example 3: A is collection with no direction; B runs plan → process → analyze → disseminate → feedback.

**Stage identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Director asks about lookalike-Microsoft | Planning and direction | The question and the reason the work exists |
| Export TLS rows for three SNIs | Collection | Raw pull against the names |
| Merge vendor lists, drop duplicates, add owners | Processing and exploitation | Organizing into usable information |
| Assess two hosts; recommend isolation | Analysis and production | Judgment + “so what” |
| Send assessment in the agreed ticket form | Dissemination | Delivery to consumers who can act |
| SOC used it and still needs the certificate pair | Evaluation and feedback | Use plus a gap that should change the next loop |

Accept “collection” for the merge only if the student is clearly describing *intake* of new lists and not the cleanup. Prefer processing. Do not accept “analysis” for the merge.

**Flow (hunt sends one suspicious SNI):**

Example answer:  
Enter at **planning and direction** (or collection if the question is already “is this SNI in a known cluster?”). Collect related names, TLS, and TIP hits. Process into one picture. Analyze whether it belongs to the cluster and produce the answer. Disseminate to hunt. If analysis cannot decide, return to **collection**. Hunt’s reply is **feedback** and may start a tighter question.

Fail the answer if it is only a list of tools, or if it never mentions a return path or feedback.

---

## Knowledge Check – Answer Key

1. **Name the six stages of the intelligence lifecycle in order.**  
   **Answer:** Planning and direction; collection; processing and exploitation; analysis and production; dissemination; evaluation and feedback.  
   **Explanation:** Order is the nominal flow. Returns are allowed; skipping is not.

2. **What is the purpose of planning and direction?**  
   **Answer:** Decide what question matters, what “done” looks like, and how the effort will run.  
   **Explanation:** Without this stage, collection has no target.

3. **Why is the lifecycle not a one-way pipeline?**  
   **Answer:** Analysis often sends work back to collection, and evaluation/feedback creates a new or tighter question.  
   **Explanation:** The cycle is how the shop stays aimed at decisions, not at a folder of finished files.

4. **Identify the stage: “Normalize three vendor reports onto one indicator table and attach asset owners.”**  
   **Answer:** Processing and exploitation.  
   **Explanation:** Context and cleanup, not judgment.

5. **Identify the stage: “Brief SOC: we assess two hosts are in the campaign; hunt this certificate pair.”**  
   **Answer:** Dissemination (of an analytic product). Accept “analysis and production plus dissemination” if they split the sentence.  
   **Explanation:** The brief is delivery. The assessment itself was produced in the prior stage.

---

## Additional Instructor Resources

- Local example of a product that skipped direction or feedback (sanitize before class)
- Escalation: if students ask about PIR format, intelligence types, or OSINT vs commercial vs internal sources, park it for 3.1.4 / 3.1.3 / 3.1.8
- Next recommended module: Intelligence types (3.1.3)
