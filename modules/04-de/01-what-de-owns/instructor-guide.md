# Instructor Guide – Module 4.1 – What DE owns

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.1 B / C / C ; 4.1.1 3c / 4c / 4c  
- SOC: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
- Hunter: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
- CTI: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name what DE owns, and sort a piece of work to DE, a nominator, 1.3, or a block.

**Context (plain language):**

- What this lesson is for: Detection engineers turn what the other desks learned into lasting rules. That only works if you know which work is yours. Sort: DE, nominator, 1.3, or a block. Then own the set.
- How it hooks to the lesson before: Hunt is done. The shared intro named the job in one sentence and said a hunt package can go to DE. This is the start of the Detection Engineering track.
- How it hooks to the lesson after: 4.2 is making a detection sound and meeting shop requirements.
- Why we are doing it this way: name what the desk owns before anyone writes, tests, or reviews a nomination, so later lessons can stay on one kind of work.
- What we are *not* doing in this lesson: how to write a rule (1.3). How to test (4.2). How to accept or send back a nomination (4.3). Lifecycle after a block (4.6). No lab. No ticket names or field lists.
- Extra step: none.

Use the same names as the student guide: **new**, **change**, **retire**, **deploy**, **nominate**, **1.3**, and **block**. **Nominator** means SOC, hunt, or CTI asking DE to look. **1.3** means how a rule works (syntax, a first read or write), not how we run detections. **Block** means firewall / IA, not a DE deploy.

**Key Teaching Points:**
- Own new, change, retire, deploy.
- Rough nominations are still DE’s to review.
- 1.3 is syntax. Detection Engineering is the service.
- A block request is not a deploy.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 4.1 – What DE owns
- T: 4.1.1 – Sort work to DE, nominator, 1.3, or block

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Start of the DE track |
| Key Concepts            | 10 min    | Own the set; sort three givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: before you write or ship a detection, you have to know whether the work is yours.
- Write new, change, retire, and deploy. Stop there. Do not teach how to do any of the four.
- Walk the three “given” lines from the student guide. The product is the kind of work, not a ticket.
- If they start writing SIGMA, Suricata, YARA, or a SIEM rule: that is 1.3. Today is only the sort.
- If they treat a rough ask as not DE’s problem: a sketch is still DE’s to review.
- If they treat a block request as a deploy: firewall / IA blocks; DE does not.
- If they invent a ticket name or a field list: those wait for 4.8.
- If they start fire / must-not-fire tests: that is 4.2.
- If they start accept / send back / reject: that is 4.3.

---

## Knowledge Check – Answer Key

1. **What four things does DE own on the set of detections?**  
   **Answer:** New, change, retire, deploy.  
   **Explanation:** Those four are the set. This lesson names them. It does not teach how to do them.

2. **A rough nomination is not DE’s problem. True or false?**  
   **Answer:** False. The draft need not be perfect. Rough is still DE’s to review.  
   **Explanation:** SOC, hunt, and CTI nominate. A sketch is still work on this desk.

3. **Someone asks you to block an IP at the firewall. Is that DE, a nominator, 1.3, or a block?**  
   **Answer:** A block (firewall / IA). Not a DE deploy.  
   **Explanation:** Extra infrastructure from intel is a block. DE does not run the firewall.

---

## Additional Instructor Resources

- Next: 4.2 Making a detection sound and meeting shop requirements
