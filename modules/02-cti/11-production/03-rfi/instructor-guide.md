# Instructor Guide – Module 2.11.3 – Handling RFIs

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.11.3 B / C / C ; 2.11.3.1 3c / 4c / 4d  
- Hunter: 2.11.3 A / A / B ; 2.11.3.1 1a / 1a / 2b  
- SOC: 2.11.3 A / A / A ; 2.11.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Evaluate, prioritize, and answer the A12 RFI. Do not open a second incident. Do not invent a queue policy.

**Context (plain language):**

- What this lesson is for: CTI analysts answer the question another desk sent because that desk needs a fact it does not have. The RFI is that question. This lesson is how to take it, decide whether you can answer it and whether it goes first, and write the answer.
- How it hooks to the lesson before: 2.11.2 sent the finished product. This lesson is answering the RFI itself.
- How it hooks to the lesson after: 2.12.1 is obtain the local priorities card. Do not invent one here.
- Why we are doing it this way: name purpose and the three handling steps, then answer A12, before anyone opens a second case or invents a shop queue rule. The classroom queue is lesson-only, not live org policy.
- What we are *not* doing in this lesson: SOC type pick (1.5.1). Finished-product structure (2.11.1). Dissemination channels (2.11.2). Local Jira names, SLAs, or PIR lists (2.12). Sibling-domain hop (2.8.1). Nation-state paragraph. No lab.
- Extra step: none.

Use the same names as the student guide: **RFI**, **Request for Information**, **purpose**, **lifecycle**, **receive**, **evaluate**, **prioritize**, **respond**, **standing work**, **payload host**, **Zeek A record**, **A12**, and **WS-JLEE**. **RFI** means a request for information. **Zeek A record** means the name-to-IP the network sensor logged. **Standing work** means work not tied to a live case. Do not invent a DYA queue SLA.

**Key Teaching Points:**
- The RFI is the question, not a second incident.
- Evaluate, prioritize, respond. Receive starts the lifecycle; those three are the handling steps.
- A12: can answer, work now, **likely** yes. No country. No new case.

**Common Student Challenges:**
- Treat the answer as a second incident. Why: SOC sent a ticket, so it feels like a new case. Example: opening a second incident for the domain question.
- Write a country paragraph. Why: they want to add “intel value.” Example: “nation-state PRD APT” instead of answering the payload-host question.
- Invent a queue SLA. Why: they want a shop rule. Example: “all RFIs in 30 minutes” as DYA policy. That is 2.12.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.11.3 – Handling RFIs
- T: 2.11.3.1 – Evaluate, prioritize, and produce a response to an RFI

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | The RFI is the question, not a second case |
| Key Concepts            | 12 min    | Purpose and lifecycle; A12 evaluate / prioritize / respond |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: another desk needs a fact it does not have. The RFI is that question. You answer it. You do not open a second incident.
- Write purpose and the lifecycle: receive, evaluate, prioritize, respond. Stop there. The three handling steps are evaluate, prioritize, and respond. Receive is how the ask arrives.
- The classroom queue is lesson-only. If they invent a DYA SLA or Jira board, that is 2.12. Obtain it later. Do not invent it here.
- Walk the A12 given. Evaluate: bounded question, Zeek A record plus the host file, can answer. Prioritize: open incident, IR has the host, work now — not behind a blog read. Respond: **likely** yes — treat the update domain / `203.0.113.88` as the payload host. Two sentences.
- If they open a second incident: the case already exists. This product is the answer. SOC type pick was 1.5.1.
- If they write a country or “PRD APT” as proof: that is not the question. Stay on the payload host.
- If they hop to a sibling domain: that is 2.8.1. This lesson answers the seed they already have.
- If they rewrite the SOC ticket or the leadership one-liner: the question is the question. Do not invent a second one.

---

## Knowledge Check – Answer Key

1. **Answering an RFI means opening a second incident. True or false?**  
   **Answer:** False.  
   **Explanation:** The RFI sits beside the open case. It is the question, not a second incident record. SOC type pick is 1.5.1. This lesson is the answer.

2. **What three steps do you take on an RFI?**  
   **Answer:** Evaluate, prioritize, and respond.  
   **Explanation:** Those are the handling steps. Receive starts the lifecycle. If you cannot answer, say what is missing. Do not invent a second question.

3. **Write a two-sentence A12 RFI response (no country, no second case).**  
   **Answer:** Likely yes — the update domain / `203.0.113.88` is the payload host for A12. Treat it as such.  
   **Explanation:** That answers the question. A country paragraph and a new incident are both wrong products.

---

## Additional Instructor Resources

- Next: 2.12.1 Local priorities
