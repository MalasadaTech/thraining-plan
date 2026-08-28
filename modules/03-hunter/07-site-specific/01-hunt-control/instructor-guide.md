# Instructor Guide – Module 3.7.1 – Hunt control and lead management

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.1 B / C / C ; 3.7.1.1 3c / 4c / 4c  
- SOC: 3.7.1 A / A / B ; 3.7.1.1 1a / 1a / 2b  
- CTI: 3.7.1 A / A / B ; 3.7.1.1 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Obtain the local initiate / control / lead path and follow it — or write that the process is missing. Do not invent a ticket or a board.

**Context (plain language):**

- What this lesson is for: A hunter who already has a named technique still does not start searching the live environment on their own. The shop decides how a hunt is opened, who can change its scope or stop it, and where leftover findings go. That path is local. This lesson is how you obtain it and follow it.
- How it hooks to the lesson before: 3.6.3 scoped one named-technique hunt. It did not open a live ticket.
- How it hooks to the lesson after: 3.7.2 is how the hunt is written down on the site form.
- Why we are doing it this way: every site has its own hunt-control path. This course does not publish DYA tickets, boards, or policy. Obtain-and-follow is the same rule as 2.12.
- What we are *not* doing in this lesson: inventing a DYA hunt ticket, lead board, or policy. Rewriting the 3.2.2 classroom card. Documentation (3.7.2). Outputs and hand-off (3.7.3). SOC tickets (1.5). No lab.
- Extra step: none. If you overlay a real shop path, say it is overlay for the room, not DYA policy.

Use the same names as the student guide: **initiate**, **control**, **leads**, **obtain-and-follow**, and **I do not have the local process yet.** A hunt **lead** here is leftover work from a hunt that is not this hunt’s scope, not a TTP extracted from a CTI report (3.4.2).

**Key Teaching Points:**
- Initiate, control, and lead management vary by site. Obtain them. Do not invent them.
- Interesting is not permission to start.
- “I do not have the local process yet” is a passing answer.

**Common Student Challenges:**
- Invent a ticket number so the hunt looks official. Why: 3.2.2 and 3.6.3 taught writing a hunt, and this lesson asks for a process. Example: filling a made-up ticket as if it were shop policy.
- Start because the technique is interesting. Why: a named technique is not permission. Example: opening a live search after 3.6.3 without asking who initiates hunts here.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.7.1 – Hunt control and lead management
- T: 3.7.1.1 – Follow the local process for initiating and controlling a hunt

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Obtain the path; do not invent a ticket |
| Key Concepts            | 10 min    | Initiate, control, leads; obtain-and-follow |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a named technique is not permission to search live. The shop decides how a hunt is opened, who controls it, and where leftovers go.
- Walk initiate, control, and leads from the student table. Stop. Do not fill in a ticket name, a board, or a DYA path.
- A hunt lead here is leftover work from a hunt that is not this hunt’s scope. It is not 3.4.2 extraction, and it is not the 3.7.3 hand-off chart.
- Walk obtain-and-follow. If you overlay a real shop path, name it as overlay, not DYA policy.
- Walk the two products: obtain the path, or write “I do not have the local process yet.” Follow only what was shown. “Not yet” is a pass.
- If they write a made-up ticket or a classroom board as policy: that is invented. Fail that product.
- If they start a documentation form or a hand-off chart: that is 3.7.2 / 3.7.3.
- If they rewrite the 3.2.2 card: that card is training, not the site path.

---

## Knowledge Check – Answer Key

1. **You should invent a DYA hunt ticket so the exercise has a number. True or false?**  
   **Answer:** False.  
   **Explanation:** Every shop has its own path. This course does not publish DYA’s. Obtain the process; do not invent a ticket.

2. **What three path pieces does this lesson obtain?**  
   **Answer:** Initiate. Control. Lead management.  
   **Explanation:** How a hunt is opened, who may widen / pause / stop, and where leftovers are parked and who triages them.

3. **What do you write if no one has shown you the process?**  
   **Answer:** Write **I do not have the local process yet.** Do not open a hunt.  
   **Explanation:** Following the local process starts with obtaining it. “Not yet” is a pass. Inventing a ticket is not.

---

## Additional Instructor Resources

- Next: 3.7.2 Hunt documentation standards
