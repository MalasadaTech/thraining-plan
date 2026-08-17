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

- What this hour is for: Packages from CTI and hunters. Same bar as a nomination. Add, change, or no new rule. Not a block list.
- How it hooks to the hour before: 4.4 was a tune on a live rule. This hour is an inbound package, not a noisy alert.
- How it hooks to the hour after: 4.6 is when to modify, retire, or leave a live rule.
- Why we are doing it this way: You wanted both hunt and intel packages as inputs. “No new rule” is a real product. Blocks stay with firewall / IA.
- What we are *not* doing this hour: Writing a rule (1.3). Tune inbox (4.4). Full lifecycle (4.6). No lab. No DYA tickets or block lists.
- Extra step: none.

Say **package**, **add**, **change**, and **no new rule** the way the student guide does. **Report** means intel report. Treat-like-a-nomination uses the **4.3** need + pointer — the package is often the pointer.

**Key Teaching Points:**
- Both CTI and hunters. Not a finished detection.
- Clear enough first. Then add, change, or no new rule.
- A list of IPs to block is a reject.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 4.5 ; T 4.5.1 ; T 4.5.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | After 4.4 tunes |
| Key Concepts            | 10 min    | Like a nomination; three products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write: both inputs; treat like 4.3; three products; not a block list. Walk the three “given” lines.

If they turn IOCs into a firewall list: “That is a block. Reject.”  
If they require a drafted rule: “Not required. Same as 4.3.”  
If they invent a ticket: “Review the package, not the ticket.”  
If they start writing SIGMA: “That is 1.3.”

---

## Knowledge Check – Answer Key

1. **A package is a finished detection. True or false?**  
   **Answer:** False. Treat it like a nomination.  
   **Explanation:** Outline d.

2. **Three valid review products?**  
   **Answer:** One add, one change, or no new rule.  
   **Explanation:** Outline b–c and 4.5.1 task 1.

3. **IPs for the firewall — add a rule or reject?**  
   **Answer:** Reject. That is a block list, not DE.  
   **Explanation:** 4.5.1 task 2.

---

## Additional Instructor Resources

- Next: 4.6 Detection lifecycle
