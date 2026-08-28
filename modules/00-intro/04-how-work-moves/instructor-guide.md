# Instructor Guide – Module 0.4 – How work can move

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- Hunter: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- CTI: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- DE: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name one possible path of work after an alert, and whose product is next.

**Context (plain language):**

- What this lesson is for: After an alert, work has to go to the next desk. This lesson names one possible path those hand-offs can take, and whose product is next.
- How it hooks to the lesson before: 0.3 named each job in one sentence. This lesson is the path between those desks.
- How it hooks to the lesson after: 0.5 is overlap — same evidence, different product, and one person may wear two hats.
- Why we are doing it this way: desks first, then one possible path, so later lessons sit on a shared sequence. It is not every shop’s policy.
- What we are *not* doing in this lesson: How to triage, write an RFI, hunt, or write a rule. No lab. No DYA ticket names, PIR lists, or approval chains. Not the companion story.
- Extra step: none.

Use the same names as the student guide: **triage**, **RFI**, **enrich**, **hunt package**, **block**, **hand-off**, and **product**. **RFI** is Request for Information. **Flow** in the task name is this path.

**Key Teaching Points:**
- One possible path, not every shop.
- Extra infrastructure → block (firewall / IA). Hunt package → hunters and detection engineers.
- Name the next hand-off and whose product it is. Do not invent a ticket path.
- Two hats is 0.5, not this lesson.

**Common Student Challenges:**
- Send extra infrastructure to the hunt team. Why: both hand-offs come after intel. Example: “hunt these IPs” when the next hand-off is whoever blocks (firewall / IA).
- Invent a ticket name. Why: shops file work differently. Example: naming a DYA Jira queue or a PIR.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 0.4 – How work can move
- T: 0.4.1 – Given a step in the flow, name the next hand-off and whose product it is

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | One possible path after an alert |
| Key Concepts            | 14 min    | Steps a–g; two products on a given |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~23 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: after an alert, work has to go to the next desk. This lesson names one possible path, not the only way a shop runs.
- Walk the seven steps. Stop. Do not teach how to triage, write an RFI, hunt, or write a rule.
- Extra infrastructure goes to whoever blocks (firewall / IA). A hunt package goes to hunters, and that same package can go to detection engineers. Those are different hand-offs.
- Walk the “given” lines from the student guide. The product is the next hand-off and whose work it is, not a ticket name.
- If they ask “what if I am both SOC and intel?”: that is 0.5. The path is the same.
- If they start a DYA ticket path, a PIR list, or an approval chain: this lesson does not invent those.

---

## Knowledge Check – Answer Key

1. **After triage, what two things can the analyst do with the alert besides asking intel?**  
   **Answer:** Send it to incident response and notify leadership.  
   **Explanation:** After triage, the analyst can send the alert to IR and notify leadership. The RFI to intel is the other ask, not these two.

2. **Extra infrastructure goes to the hunt team. True or false?**  
   **Answer:** False. Extra infrastructure can go to whoever blocks (firewall / IA). Hunters get a hunt package.  
   **Explanation:** Those are two later hand-offs, not the same one.

3. **Intel found extra infrastructure. Name the next hand-off and whose product it is.**  
   **Answer:** Whoever blocks (firewall / IA). Product: the block. Not a hunt.  
   **Explanation:** Extra infrastructure is a block hand-off. A hunt package is a different product.

---

## Additional Instructor Resources

- Next: 0.5 Where the jobs overlap
