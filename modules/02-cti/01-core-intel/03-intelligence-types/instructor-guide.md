# Instructor Guide – Module 3.1.3 – Intelligence Types

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:** CTI B/3c → C/4c → C/4c | Hunter A/1a → B/2b → B/3c | SOC A/1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on classification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the four intelligence types (strategic, operational, tactical, technical) and make students practice classifying products and requirements by the decision they support.

**Key Teaching Points:**
- Type follows the question / decision, not length, threat-actor fame, or the cover title.
- Strategic = posture. Operational = how to run the body of work. Tactical = what to do now. Technical = observables.
- Types stack on one campaign. They are not lifecycle stages.
- A hash dump is not tactical. A long APT PDF is not automatically strategic.
- Stay out of PIR format, “actionable” criteria, and audience rewrite. Point forward if asked.

**Common Student Challenges:**
- Equating “nation-state” or “executive slide” with strategic.
- Collapsing tactical and technical.
- Treating operational as a synonym for tactical.
- Classifying the *label* instead of the *decision*.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard or shared doc for live classification
- Answer key (this guide)

---

## Learning Objectives

1. Define strategic, operational, tactical, and technical intelligence.
2. State what question each type is built to answer and who usually consumes it.
3. Correctly classify an intelligence product or requirement by type.
4. Spot a product that is labeled as one type but is actually another.

**Mapped Items:**
- K: 3.1.3 – Intelligence types (strategic, operational, tactical, technical)
- T: 3.1.3.1 – Classify an intelligence product or requirement by type

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Write the four types on the board |
| Four types, four jobs          | 10 min   | Table first; type ≠ stage |
| Strategic and operational      | 10 min   | Horizon and consumer |
| Tactical and technical         | 10 min   | Action vs observables |
| Walkthrough Examples           | 14 min   | Interactive; students speak first |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 6 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~72 min** | Cut Example 3 if the room is already classifying cleanly |

---

## Detailed Teaching Notes

### 1. Four Types, Four Jobs

**Talking Points:**
- Ask “what decision does this unlock?” before you let anyone use a type name.
- Reuse 3.1.1: type applies to intelligence (and to the requirement). Raw IOCs are still data.
- Reuse 3.1.2: stage is *where you are in the loop*. Type is *what kind of answer*. Do not let them merge the two.

**What to emphasize:**
- All four types are legitimate CTI work. Technical is not “lesser.”
- Do not invent a fifth sign-off type (operational-technical, cyber, etc.). If someone raises a local name, map it onto these four.

**Questions to ask the class:**
- “If I send a director three hashes, what type did I actually produce?”
- “What would I have to add before that is strategic?”

### 2. Strategic and Operational

**Talking Points:**
- Strategic changes posture, investment, or accepted risk. It is not a longer tactical note.
- Operational sequences a campaign, hunt series, or incident window. Hunt leads live here a lot.
- “Nation-state” is a subject, not a type.

**What to emphasize:**
- Horizon (months/years vs days/weeks) is a clue, not the whole test. A one-page strategic memo can be short.
- PIR writing is 3.1.4. Here you only classify a requirement by type.

**Question to ask:**  
“Is this about *whether we change the program* or *how we run this week’s work*?”

### 3. Tactical and Technical

**Talking Points:**
- Tactical names an action on activity in front of you.
- Technical names mechanics you can detect or pivot on.
- A clean, analyzed hash/JA3 note can be technical intelligence. An unreviewed STIX import is still data.

**What to emphasize:**
- Operators need both. Shipping only technical and calling it tactical is the usual miss.
- Actionable-intelligence criteria are the next module. Do not open that checklist.

### 4. Examples

Work through all three interactively. Ask students to classify before you read the interpretation.

**Extra point for Example 1:**  
Same campaign, four products. If they only remember one thing, make it this.

**Extra point for Example 2:**  
The word STRATEGIC on the slide is the trap. Same IOC paste family as 3.1.1 / 3.1.2, now scored as a *type* problem.

**Extra point for Example 3:**  
Force two classifications: the requirement and the product. They do not match. That is the teaching point.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- Review answers as a group afterward. Do not collect a grade.

**What good answers look like:**

**Summaries:**
- Example 1: One campaign shown as all four types — each product unlocks a different decision.
- Example 2: Cover says strategic; content is technical data (plus a claim); treat as a lead.
- Example 3: A is a strategic requirement, B is tactical; the shipped write-up is a technical dump that answers neither.

**Classifications:**

| Item | Answer | Why |
|------|--------|-----|
| Fund east-west DNS logging this year | Strategic | Posture / investment |
| Hunt lab first, then finance; IR takes victims | Operational | How to run the week’s body of work |
| Isolate 10.10.22.17 and hunt that JA3 this shift | Tactical | Immediate action |
| Hashes / JA3 / SNI / port, no action | Technical | Observables only (intelligence if analyzed; say so) |
| Keep accepting last year’s phishing loss rate? | Strategic | Requirement about accepted risk |
| Unreviewed vendor STIX bundle | Data (not a type yet) | Import is not intelligence; do not force a type |

Accept “technical data” for the hash page if they deny it is tactical. Do not accept “strategic” for the STIX bundle.

**Transformation (Example 1 technical row → tactical / strategic):**

Tactical (example):  
We assess 10.10.22.17 is likely in the fake-update cluster; isolate it and hunt that JA3/SNI pair this shift.

Strategic (example):  
We assess this cluster will keep using weak TLS to finance-adjacent hosts this quarter; fund the extra TLS sensor now rather than wait for the next budget cycle.

---

## Knowledge Check – Answer Key

1. **What question does strategic intelligence answer that tactical intelligence does not?**  
   **Answer:** What should leadership change about risk, investment, or posture (long horizon). Tactical answers what to do now on this activity.  
   **Explanation:** Same campaign can need both; they are not interchangeable.

2. **What is the difference between tactical intelligence and technical intelligence?**  
   **Answer:** Tactical judges an immediate action. Technical describes observables for detect/pivot.  
   **Explanation:** A JA3 note is technical. “Isolate this host and hunt that JA3” is tactical.

3. **Why is a long “APT” PDF not automatically strategic?**  
   **Answer:** Type follows the decision the product supports, not length or actor fame. Many such PDFs are technical reporting or unanalyzed information.  
   **Explanation:** Classify the content, not the cover.

4. **Classify: “Run a 10-day hunt series on the fake-update cluster; IR owns victims.”**  
   **Answer:** Operational.  
   **Explanation:** Sequences a body of work; not a single-host action and not a posture change.

5. **Classify: “SNI `update.not-a-real-cdn.example`, JA3 `a0e9f5…`, port 8443.”**  
   **Answer:** Technical (and only intelligence if those observables were analyzed for use).  
   **Explanation:** No action, no campaign plan, no posture judgment.

---

## Additional Instructor Resources

- Local examples of a product that was mis-typed (sanitize before class)
- Escalation: if students ask about PIR format, actionable criteria, or audience rewrite, park it for 3.1.4 / 3.1.5 / 3.1.6
- Next recommended module: Intelligence requirements (3.1.4)
