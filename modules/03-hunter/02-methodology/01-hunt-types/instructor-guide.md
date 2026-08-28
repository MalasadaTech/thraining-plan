# Instructor Guide – Module 3.2.1 – Hunt Types

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.1 B / C / C ; 3.2.1.1–3.2.1.4 3c / 4c / 4c  
- SOC: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
- CTI: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the four hunt types and what execute looks like for each. No lab. No hunt card format.

**Context (plain language):**

- What this lesson is for: Hunters pick a type so the search has a reason. This lesson names the type, the seed, and the look-for.
- How it hooks to the lesson before: 3.1 said why hunting exists — missed activity and gaps.
- How it hooks to the lesson after: 3.2.2 is the written hypothesis, scope, priority, and unique pattern.
- Why we are doing it this way: name the four starts and what execute looks like before anyone writes a hunt card.
- What we are *not* doing in this lesson: hunt card format. SIEM session. Invented ticket. Extracting TTPs. ATT&CK remapping. Persistence as a category. No lab.
- Extra step: none.

Use the same names as the student guide: **intel-driven**, **hypothesis-driven**, **reactive**, **anomaly-based**, **execute**, **seed**, and **look-for**. Stay on **A12**. **Execute** is the product line (type + seed + look-for), not a live query. Reactive is more of a known incident on other hosts, not a rewrite of the **WS-JLEE** process alert.

**Key Teaching Points:**
- Four starts. The start is the type.
- Execute is type plus look-for, not a SIEM session and not the hunt card.
- Hypothesis is not intel-driven. Reactive is not re-working the SOC alert.

**Common Student Challenges:**
- Call every hunt intel-driven because CTI already worked **A12**. Why: a report is nearby. Example: labeling “if they persist, we should see Run **`Updater`**” as intel-driven.
- Treat a reactive hunt as re-working the SOC ticket. Why: **A12** is already in the queue. Example: rewriting the **WS-JLEE** process alert instead of looking for more `invoice.vbs` on other hosts.
- Write the hunt card in this lesson. Why: execute sounds like a write-up. Example: filling hypothesis / scope / priority instead of naming type and look-for.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.2.1 – Hunt types
- T: 3.2.1.1 – Execute an intel-driven hunt
- T: 3.2.1.2 – Execute a hypothesis-driven hunt
- T: 3.2.1.3 – Execute a reactive hunt
- T: 3.2.1.4 – Execute an anomaly-based hunt

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Why this search has a type |
| Key Concepts            | 12 min    | Four types; A12 execute lines |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: hunters pick a type so the search has a reason, and the start decides the type.
- Write the four types and their starts. Stop. Do not open the hunt card.
- Walk the **A12** execute lines from the student guide. The product is type plus look-for, not a SIEM session.
- Walk Run **`Updater`** as hypothesis-driven: the start is the if/then, not the CTI report.
- Walk the CTI domain / file as intel-driven: the start is a fact CTI already handed you.
- If they write the card: that is 3.2.2.
- If they open a SIEM: execute is the product line in this lesson, not a live query.
- If they rewrite the **WS-JLEE** alert: that is SOC work, not a reactive hunt.
- If they hunt “persistence”: that is not this lesson. 3.6.3 is one named technique.

---

## Knowledge Check – Answer Key

1. **All four types start from a CTI report. True or false?**  
   **Answer:** False. Intel-driven starts from a CTI fact. The other three start from an if/then, a known incident, or an odd pattern.  
   **Explanation:** A nearby report does not make every hunt intel-driven. Hypothesis can be *informed* by CTI and still start from the if/then.

2. **Name the four types.**  
   **Answer:** Intel-driven, hypothesis-driven, reactive, anomaly-based.  
   **Explanation:** Those are the four types this course uses. Name them; then name the start.

3. **“If they persist, we should see Run `Updater` on more hosts.” Which type, and what do you search?**  
   **Answer:** **Hypothesis-driven.** Search HKCU Run **`Updater`** on other hosts.  
   **Explanation:** The start is the if/then, not a CTI domain. Execute is that look-for, not the written card.

---

## Additional Instructor Resources

- Next: 3.2.2 Hunt development
