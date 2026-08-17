# Instructor Guide – Module 1.1.1 – Endpoint activity (the map)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 2b / 2b  
- Hunter: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 1a / 2b  
- CTI: 1.1.1.1 A / A / A ; 1.1.1.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the five kinds of host rows so the next hours can stay on one kind each.

**Context (plain language):**

- What this hour is for: An alert will point at a host. Before you describe a row, you need to know which kind of row it is. This hour is that map.
- How it hooks to the hour before: 0.5 laid out the course. This is the start of the SOC analyst block.
- How it hooks to the hour after: 1.1.2 is the process row — who ran what.
- Why we are doing it this way: You wanted a front door for 1.1 so process / file / registry / host-network / image-load are named before we read one.
- What we are *not* doing this hour: Process fields. Sysmon install. Zeek. The PRD plot. No lab.
- Extra step: none.

Say **row**, **process**, **file**, **registry**, **host-network**, and **image/driver load** the way the student guide does. **Host-network** means the endpoint logged a talk, not a Zeek protocol lesson.

**Key Teaching Points:**
- Five kinds. One map.
- Sysmon and MDE encode the same activities.
- Name the kind. Do not describe the event yet.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.1.1.1 ; T 1.1.1.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | After 0.5 |
| Key Concepts            | 10 min    | Five kinds; three givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the five kinds. Stop. Walk the three “given” lines.

If they start Event IDs: “1.1.2. Today is the kind.”  
If they say host-network is Zeek: “The host logged it. Zeek is 1.2.”  
If they tell the PRD story: “Not this hour.”

---

## Knowledge Check – Answer Key

1. **Sysmon and MDE are two different stories. True or false?**  
   **Answer:** False. Two encodings of the same activities.  
   **Explanation:** Outline b.

2. **“A program started on the host.” Which type?**  
   **Answer:** Process.  
   **Explanation:** Outline a and 1.1.1.1 task 1.

3. **“This host connected to an IP and port.” Process or host-network?**  
   **Answer:** Host-network.  
   **Explanation:** Outline a and d. The process *started* it; the row that logged the talk is host-network.

---

## Additional Instructor Resources

- Next: 1.1.2 Process activity
