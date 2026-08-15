# Instructor Guide – Module 3.1.1 – Data, Information, and Intelligence

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:** CTI B/3c → C/4c → C/4c | Hunter A/1a → B/2b → B/3c | SOC A/1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on categorization

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the distinction between data, information, and intelligence, and make students practice categorizing real-looking products. This is the foundation for every later 3.1 item.

**Key Teaching Points:**
- The three terms are not synonyms.
- Data = raw fact. Information = context. Intelligence = analysis against a requirement plus a usable “so what.”
- You cannot rename a feed and call it intelligence.
- Leads are not incidents and not finished products.
- Stay out of the lifecycle, PIR writing, and attribution. Point forward if asked.

**Common Student Challenges:**
- Calling any CTI-looking artifact “intel.”
- Thinking a vendor report is automatically intelligence for *this* organization.
- Adding adjectives (“actionable intel”) instead of adding analysis.
- Jumping to containment language without a requirement or a judgment.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard or shared doc for live categorization
- Answer key (this guide)

---

## Learning Objectives

1. Define data, information, and intelligence and state how they differ.
2. Explain how raw data becomes information and then intelligence.
3. Correctly categorize examples as data, information, or intelligence.
4. Spot products that are labeled “intel” but are still only data or information.

**Mapped Items:**
- K: 3.1.1 – Difference between data, information, and intelligence
- T: 3.1.1.1 – Correctly categorize examples as data, information, or intelligence

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Write the three words on the board |
| Definitions and distinctions   | 12 min   | Table first, then the TLS-row example |
| How data becomes intelligence  | 10 min   | Process, not a rename |
| Walkthrough Examples           | 14 min   | Interactive; students speak first |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~66 min** | Stretch examples if the room is quiet |

---

## Detailed Teaching Notes

### 1. Definitions and Distinctions

**Talking Points:**
- SOC and hunt live in data and information all day. CTI is paid for the third layer.
- Information can be excellent and still not be intelligence.
- Intelligence can be short. Length is not the test. Judgment plus a requirement is the test.

**What to emphasize:**
- “So what?” and “what should we do?”
- Do not invent a fourth term (wisdom, knowledge) as a sign-off item. If someone raises DIKW, acknowledge it and return to these three.

**Questions to ask the class:**
- “If I forward you a hash, what did I give you?”
- “What would I have to add before you would put it in a brief to a director?”

### 2. How Raw Data Becomes Intelligence

**Talking Points:**
- Parsing a log is not analysis.
- Enrichment (VT count, WHOIS, asset owner) is still usually information.
- The requirement can be informal (“are we hit by this campaign?”) but it must exist.
- PIR format, lifecycle stages, and collection planning are the *next* modules. Do not teach them here.

**What to emphasize:**
- The failure mode is stopping at information.
- A lead is permission to work, not a conclusion.

**Question to ask:**  
“Where does this product stop — data, information, or intelligence — and what is the next missing step?”

### 3. Examples

Work through all three interactively. Ask students to categorize before you read the interpretation.

**Extra point for Example 1:**  
Same session, three artifacts. If they only remember one thing, make it this.

**Extra point for Example 2:**  
The word INTEL in the chat title is the trap. Ask who has sent or received a message like this. Then ask what they would do *instead of* briefing it.

**Extra point for Example 3:**  
Write-up A has more technical fields. Students will try to call it intelligence because it looks like work. Force the requirement / judgment / decision test.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- Review answers as a group afterward. Do not collect a grade.

**What good answers look like:**

**Summaries:**
- Example 1: One activity shown as data, then information, then intelligence — only the last answers a requirement.
- Example 2: A public IOC paste is data (with a claim), not intelligence; treat it as a lead.
- Example 3: A is information; B is intelligence because it judges and recommends against a stated requirement.

**Categorizations:**

| Item | Answer | Why |
|------|--------|-----|
| SHA-256 only | Data | Raw fact, no context |
| Three hosts resolved a lookalike domain in a time window | Information | Organized story; no judgment or action |
| Assess phishing session; disable accounts and hunt | Intelligence | Requirement-shaped judgment + decision |
| Unreviewed vendor STIX bundle | Data (or unevaluated information) | Import is not analysis; “data” is the safer classroom answer |
| SOC timeline of mixed events | Information | Context and sequence, no “so what” |
| Priority is low; no detection work this week | Intelligence | Judgment against relevance + a decision |

Accept “information” for the STIX bundle only if the student says it arrived already structured *and* they still deny it is intelligence. Do not accept “intelligence.”

**Transformation (Example 1 row → information / intelligence):**

Information (example):  
Internal workstation 10.10.50.23 opened a short TLS 1.3 session to `www.example.com` with matching SNI and certificate.

Intelligence (example):  
We assess this host is **not** part of the lookalike-Microsoft activity; SNI and certificate agree on a legitimate name. No isolate. Continue the review only if the user remains on the phishing target list.

---

## Knowledge Check – Answer Key

1. **What is the difference between data and information?**  
   **Answer:** Data is a raw, unprocessed fact. Information is data that has been organized or given context (who / what / when / where).  
   **Explanation:** A field value vs. a rewritten story of the same event.

2. **What must be present before information becomes intelligence?**  
   **Answer:** Analysis against a requirement, plus a usable implication or decision (the “so what”).  
   **Explanation:** More fields or a nicer slide do not complete the step.

3. **Why is a public IOC list not intelligence by itself?**  
   **Answer:** It is raw or lightly described indicators with no analysis of relevance, confidence, or action for this environment.  
   **Explanation:** It is a lead at best.

4. **Categorize: “Host 10.10.50.88 presented a self-signed certificate for a Microsoft lookalike SNI at 19:41.”**  
   **Answer:** Information.  
   **Explanation:** Context and a story; no assessment or recommended action.

5. **Categorize: “We assess that host is in a phishing session; isolate it and hunt the same certificate pair.”**  
   **Answer:** Intelligence.  
   **Explanation:** Judgment + decision tied to an implied requirement (is this phishing?).

---

## Additional Instructor Resources

- Local examples of a good vs. weak CTI product (sanitize before class)
- Escalation: if students ask about lifecycle stages, types (strategic / tactical), or PIRs, park it for 3.1.2 / 3.1.3 / 3.1.4
- Next recommended module: Intelligence lifecycle (3.1.2)
