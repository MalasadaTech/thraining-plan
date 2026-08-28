# Instructor Guide – Module 2.9.2 – AnyRun

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.2 B / C / C ; 2.9.2.1 3c / 4c / 4c  
- Hunter: 2.9.2 A / B / B ; 2.9.2.1 2b / 3c / 4c  
- SOC: 2.9.2 A / A / B ; 2.9.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Search and review an AnyRun classroom card. Extract who and what, or say it is not on the card. No live account.

**Context (plain language):**

- What this lesson is for: CTI analysts search public detonations for a seed they already have, then write who can act and what they do from that run — or say the fact is missing.
- How it hooks to the lesson before: 2.9.1 was VirusTotal Relations and Behavior on a classroom card.
- How it hooks to the lesson after: 2.9.3 is Silent Push — domain and IP history, not a sandbox run.
- Why we are doing it this way: search and review from a static card so nobody needs a live vendor account. When to pick AnyRun is already 0.7.
- What we are *not* doing in this lesson: the 0.7 survey. A conceptual infrastructure hop (2.8.1). Hunt conversion to SIEM or Zeek (3.3.1). File-similarity hashes (2.4). Applicable TTPs (2.8.2). Detonating a sample. No lab.
- Extra step: none.

Use the same names as the student guide: **public detonation**, **classroom card**, **search**, **review**, **extract**, **not on card**. A **tag** is a label on a public run. **Actionable** means who + what (**2.1.5**). The given uses course-fiction seeds (`203.0.113.88`, `update.exe`). Do not turn it into the intro plot, and do not plant a check-in POST unless the card shows it.

**Key Teaching Points:**
- Search by the seed you already have: tag, IP, domain, or hash.
- Review only what is on the card: process tree, network, dropped files.
- Extract who and what, or write **not on card**. A “malicious” tag is information.

**Common Student Challenges:**
- Treat a “malicious” tag as intelligence. Why: the card labeled the run. Example: writing “treat as C2” from a tag count with no URI.
- Invent a network event the card does not show. Why: they already know the companion story. Example: writing a check-in POST when the card shows only a GET, or nothing.
- Redo “when to pick AnyRun.” Why: 0.7 used the same product name. Example: answering “I pick AnyRun because I have a binary” instead of searching the hash they already have.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.9.2 – AnyRun
- T: 2.9.2.1 – Search and review AnyRun submissions for actionable intelligence

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Public detonation; classroom card |
| Key Concepts            | 12 min    | Four search keys; review; extract or missing |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: you already have a seed. You search public detonations. You write who and what from the card, or you say it is missing.
- Name the four search keys: tag, IP, domain, hash. You search what you already have. A tag is a label, not a new hunt.
- Review process tree, network, and dropped files on the card only.
- Walk the given: search `203.0.113.88` or the `update.exe` hash. A contacted URI or dropped name is legal if present. **Not on card** is legal.
- A count of “malicious” tags has no who and no next step. That is information, not intelligence.
- If they redo 0.7: when to pick is done. This lesson is search and review.
- If they invent a check-in POST: not unless the card shows it.
- If they open Silent Push or a live vendor tab: that is not this lesson.

---

## Knowledge Check – Answer Key

1. **A count of “malicious” tags on an AnyRun card is actionable intelligence. True or false?**  
   **Answer:** False. It is information.  
   **Explanation:** Actionable intelligence names a who and a what (**2.1.5**). A verdict tag has neither.

2. **What four things can you search AnyRun submissions by?**  
   **Answer:** Tag, IP, domain, or hash.  
   **Explanation:** Those are the four search keys for this lesson. You search a seed you already have.

3. **You open a classroom card for the `update.exe` hash. Name one extract that is legal if it is on the card, and one thing you must not invent.**  
   **Answer:** Legal: a contacted URI or a dropped file name on the card, or **not on card**. Do not invent a check-in POST.  
   **Explanation:** Extract only what the card shows. Missing is a legal product. Inventing a beacon is not.

---

## Additional Instructor Resources

- Next: 2.9.3 Silent Push
