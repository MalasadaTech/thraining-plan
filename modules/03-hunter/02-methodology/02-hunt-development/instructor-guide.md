# Instructor Guide – Module 3.2.2 – Hunt Development Concepts

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.2 B / C / C ; 3.2.2.1–3.2.2.3 3c / 4c / 4d  
- SOC: 3.2.2 A / B / B ; 3.2.2.1–3.2.2.3 1a / 1a / 2b  
- CTI: 3.2.2 A / B / B ; 3.2.2.1 1a / 2b / 3c ; 3.2.2.2 1a / 2b / 3c ; 3.2.2.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Write a hunt card — hypothesis, scope, priority, and unique pattern — so the search is bounded. Do not invent a ticket.

**Context (plain language):**

- What this lesson is for: Hunters bound a search before they query. The product is a short hunt card: what you are looking for, where, why now, and which pattern is specific enough to search internally.
- How it hooks to the lesson before: 3.2.1 named the hunt types. This lesson is the write-up.
- How it hooks to the lesson after: 3.3.1 is hunt use of external tools.
- Why we are doing it this way: write the four pieces before anyone opens a query, so the search has a bound.
- What we are *not* doing in this lesson: local hunt template or ticket (3.7). SIEM session (3.3.1). “Hunt persistence” (3.6.3). No lab.
- Extra step: none.

Use the same names as the student guide: **hunt card**, **hypothesis**, **scope**, **priority**, and **unique pattern**. The hunt card is the four-line classroom write-up, not the site form. **HKCU Run `Updater`** → `%TEMP%\update.exe` is the A12 persistence beat. The missed `GET /update.exe` download is a **false negative**, not a fired alert they dislike.

**Key Teaching Points:**
- Unique means the value name `Updater`, not any Run key.
- Priority is the open A12 incident plus the missed download, not a blog.
- Four lines. Not a query. Not a ticket.

**Common Student Challenges:**
- Write an unbounded card. Why: hunt feels like “look for evil.” Example: “search everything for malware.”
- Name the tactic instead of the pattern. Why: the class is easier to say than the artifact. Example: “any Run key” instead of value name `Updater`.
- Invent a ticket. Why: writing it down feels like opening work. Example: making up a Jira key. That is 3.7.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.2.2 – Hunt development concepts
- T: 3.2.2.1 – Develop and document a hunt hypothesis
- T: 3.2.2.2 – Scope and prioritize a hunt
- T: 3.2.2.3 – Identify unique patterns or behaviors suitable for hunting

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Bound the search before the query |
| Key Concepts            | 12 min    | Four lines; A12 card |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: hunters write the bound before they query. The hunt card is hypothesis, scope, priority, and unique pattern.
- Walk the four pieces. A hypothesis is if/then, not a topic. Scope is hosts, time, and telemetry. Priority is why now. Unique pattern is searchable internally.
- Walk the A12 card from the student guide. One set of four lines. Stop.
- If they write “search everything for malware” or “hunt persistence”: that is not a card. Persistence as a class is 3.6.3.
- If they write “any Run key”: the unique pattern is the value name `Updater`.
- If they open a SIEM: that is 3.3.1. This lesson does not write the query.
- If they invent a Jira or a board: that is 3.7.

---

## Knowledge Check – Answer Key

1. **A hunt card is “search everything for malware.” True or false?**  
   **Answer:** False. A hunt card bounds the search.  
   **Explanation:** “Search everything for malware” has no hypothesis, no scope, and no unique pattern.

2. **What four pieces does the hunt card have?**  
   **Answer:** Hypothesis, scope, priority, unique pattern.  
   **Explanation:** Those four lines are the classroom card. They are not a site ticket.

3. **Write a one-line A12 hypothesis and one unique pattern (not “any Run key”).**  
   **Answer:** If A12 persistors exist elsewhere, we see HKCU Run `Updater` → `%TEMP%\update.exe`. Unique pattern is the value name `Updater`, not any Run key.  
   **Explanation:** The if/then is testable. The value name is specific enough to search internally.

---

## Additional Instructor Resources

- Next: 3.3.1 Hunt tool capabilities
