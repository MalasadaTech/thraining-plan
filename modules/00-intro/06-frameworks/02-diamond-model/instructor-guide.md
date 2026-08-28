# Instructor Guide – Module 0.6.2 – Diamond Model

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.2.1 A / B / C ; 0.6.2.2 2b / 3c / 4c  
- Hunter: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- CTI: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- DE: 0.6.2.1 A / B / B ; 0.6.2.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Organize what you know about an incident into four vertices and name the weakest, so you do not invent the adversary.

**Context (plain language):**

- What this lesson is for: You get an incident or a short set of indicators. Before you claim who did it, put what you actually have on four corners and name the empty one. That is how every desk keeps the write-up honest.
- How it hooks to the lesson before: 0.6.1 labeled the behavior. This lesson organizes who, with what, through what, and against whom.
- How it hooks to the lesson after: 0.6.3 stages the same activity in time.
- Why we are doing it this way: this is the shared floor before SOC. Every role fills four vertices from evidence. CTI product depth stays in 2.7.2. Actor profiles stay in 2.11.
- What we are *not* doing in this lesson: ATT&CK IDs (0.6.1). Kill Chain stages (0.6.3). Naming PRD as a fact. Actor profiles. A CTI product write-up (2.7.2). No lab.
- Extra step: none.

Use the same names as the student guide: **Adversary**, **Capability**, **Infrastructure**, **Victim**, **vertex** (corner), and **weakest**. Do not treat a vendor PDF title or a course-fiction name as Adversary evidence.

**Key Teaching Points:**
- Four vertices. The model shows what you do not know. It is not a verdict.
- Weakest means least evidence. That is the next question, not a guess.
- A vendor name or a course-fiction name is not Adversary evidence.

**Common Student Challenges:**
- Fill Adversary with a vendor or course-fiction name. Why: a PDF title feels like a who. Example: writing PRD or “PRD APT” when the activity is a host, encoded PowerShell, and a domain.
- Guess the empty vertex so the Diamond looks complete. Why: an empty corner feels unfinished. Example: writing an actor name with no actor evidence.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 0.6.2.1 – Diamond Model
- T: 0.6.2.2 – Apply the Diamond Model to an incident or set of indicators

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Four corners and the empty one |
| Key Concepts            | 8 min     | Four vertices + one fill |
| Knowledge Check         | 3 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~15 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an incident or a short set of indicators, and a temptation to write a group name. Fill four corners first.
- Write the four vertices. Stop. Do not map ATT&CK IDs.
- Walk the given: encoded PowerShell on a workstation talking to a domain. Victim = that host. Capability = encoded PowerShell. Infrastructure = that domain. Adversary = weakest.
- If they put PRD or a vendor APT name in Adversary: that is not evidence. Name Adversary as weakest.
- If they start a CTI product paragraph about the gap: that is 2.7.2. Today is the four fills and the weakest name.
- DE sits this at awareness. Do not start them at CTI product depth.

---

## Knowledge Check – Answer Key

1. **Name the four Diamond vertices.**  
   **Answer:** Adversary, Capability, Infrastructure, Victim.  
   **Explanation:** Those are the four corners. A name goes in Adversary only when you have evidence for who.

2. **What do you do with the weakest vertex?**  
   **Answer:** Name it as the one with the least evidence. That is the next question, not a guess you write as fact.  
   **Explanation:** The model is for seeing what you do not know. Filling the empty corner from a PDF title is a guess.

3. **Encoded PowerShell on a workstation talking to a domain. Which vertex is usually weakest, and why?**  
   **Answer:** Adversary. You have victim, capability, and infrastructure. You have no actor evidence.  
   **Explanation:** The host, the encoded PowerShell, and the domain fill three vertices. A course-fiction name does not fill the fourth.

---

## Additional Instructor Resources

- Next: 0.6.3 Cyber Kill Chain
