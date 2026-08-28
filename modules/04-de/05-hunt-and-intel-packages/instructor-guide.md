# Instructor Guide – Module 4.5 – Hunt and intel packages

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.5 B / C / C ; 4.5.1 3c / 4c / 4d ; 4.5.2 3c / 4c / 4c  
- SOC: 4.5 A / A / B ; 4.5.1 1a / 1a / 2b ; 4.5.2 1a / 1a / 2b  
- Hunter: 4.5 A / B / B ; 4.5.1 1a / 2b / 3c ; 4.5.2 1a / 2b / 2b  
- CTI: 4.5 A / B / B ; 4.5.1 1a / 2b / 3c ; 4.5.2 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Treat a hunt or intel package like a nomination, pick add / change / no new rule, and reject a block list.

**Context (plain language):**

- What this lesson is for: Detection engineers review inbound work from other desks. Hunters and intel send packages — a hunt write-up or an intel report. Those are inputs, not finished detections. Review them like a nomination: confirm they are clear enough, then name one add, one change, or no new rule, and reject a block list.
- How it hooks to the lesson before: 4.4 was a tune request on a live rule from SOC. This lesson is an inbound package from hunt or intel.
- How it hooks to the lesson after: 4.6 is when to modify, retire, or leave a live rule you already own.
- Why we are doing it this way: Hunt packages and intel packages are the same kind of inbound input, not two different review jobs. “No new rule” is a finished review. Blocks stay with firewall / IA.
- What we are *not* doing in this lesson: Writing a rule (1.3). Tune requests on a live rule (4.4). Full lifecycle (4.6). No lab. No invented tickets or block lists as DE deploys.
- Extra step: none.

Use the same names as the student guide: **package**, **add**, **change**, and **no new rule**. **Report** means intel report. Treat-like-a-nomination uses the **4.3** need + pointer — the package is often the pointer. Do not re-teach the whole nomination lesson.

**Key Teaching Points:**
- Both CTI and hunters. Not a finished detection.
- Clear enough first. Then add, change, or no new rule.
- A list of IPs to block is a reject.

**Common Student Challenges:**
- Treat the package as a finished detection. Why: it looks like a hunt write-up or a report with IPs or domains. Example: deploying the package as a rule without naming add, change, or no new rule.
- Turn the package into a firewall list. Why: the package names IPs or domains. Example: “add these IPs to the firewall” as the DE product.
- Require a drafted rule before review. Why: a drafted rule is extra if they have one, not a gate. Example: sending the package back only because there is no SIGMA.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 4.5 – Hunt and intel packages
- T: 4.5.1 – Review a package: one add, one change, or no new rule
- T: 4.5.2 – Reject turning the package into a block list

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Package as inbound input, not a finished detection |
| Key Concepts            | 10 min    | Like a nomination; three products; reject a block list |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: hunters and intel send packages. Those are inputs. You review them so a package does not skip review and so extra infrastructure does not become a DE deploy.
- Name both sources: CTI and hunters. Do not split this into two review jobs.
- Restate the nomination bar in ordinary words: need plus pointer. The package is often the pointer. A drafted rule is not required. Missing need or pointer means send it back. Stop there. Do not walk accept / send back / reject as the three products — those are 4.3.
- Walk the three products: one add, one change, or no new rule. “No new rule” is still a finished review. Do not pad it with a fake add.
- If they start picking tune versus exception versus retire: that is 4.4 or 4.6. This lesson names the change, not the lifecycle call.
- If they turn the package into a firewall list: that is a block. Reject. Firewall / IA, not a DE deploy.
- If they require a drafted rule: not required. Same as 4.3.
- If they invent a ticket: review the package, not the ticket.
- If they start writing SIGMA: that is 1.3.
- Walk the three givens from the student guide before the knowledge check.

---

## Knowledge Check – Answer Key

1. **A package is a finished detection. True or false?**  
   **Answer:** False. Treat it like a nomination.  
   **Explanation:** A package is inbound material from hunt or intel. It is not a detection you can deploy.

2. **Name the three valid review products for a package.**  
   **Answer:** One add, one change, or no new rule.  
   **Explanation:** After the package is clear enough, name one of those three. “No new rule” is still a finished review.

3. **A package is a list of IPs to put on the firewall. Add a rule, or reject?**  
   **Answer:** Reject. That is a block list, not DE.  
   **Explanation:** Extra infrastructure goes to whoever blocks (firewall / IA). That is not a DE deploy.

---

## Additional Instructor Resources

- Next: 4.6 Detection lifecycle
