# Instructor Guide – Module 3.6.2 – Privilege Escalation Techniques

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.2 B / C / C ; 3.6.2.1 3c / 4c / 4c  
- SOC: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
- CTI: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Recognize elevation in a log. Not persistence. Not an A12 fact.

**Context (plain language):**

- What this hour is for: Hunters tell persistence apart from a privilege change, and name the indicator that proves the change.
- How it hooks to the hour before: 3.6.1 recognized the Run key as persistence.
- How it hooks to the hour after: 3.6.3 hunts **one named** technique.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–b + recognize task. Classroom elevation row is not a bible A12 event.
- What we are *not* doing this hour: Hunt TA0004. Call the Run key privesc. Invent DYA tickets. No lab.
- Extra step: none.

**Key Teaching Points:**
- Already-SYSTEM is not elevation.
- A12 Run key is persist, not privesc.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 3.6.2 ; T 3.6.2.1

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Lower → higher |
| Key Concepts            | 12 min    | Methods + A12 is not this |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write elevation vs persist. Walk token / UAC / service. Label the classroom row as classroom.

If they call Run **`Updater`** privesc: “3.6.1. Same user.”  
If they invent a Night Owl ticket: “Not a bible A12 fact. 3.7.”

---

## Knowledge Check – Answer Key

1. **Run Updater is privesc. True or false?**  
   **Answer:** False. Persistence.  
   **Explanation:** Stay-in / 3.6.1.

2. **Two methods?**  
   **Answer:** Any two of: token theft, UAC bypass, privileged-service abuse, other.  
   **Explanation:** Outline a.

3. **User parent → SYSTEM cmd, no consent?**  
   **Answer:** Token theft. Proof: parent identity vs child identity, no consent.  
   **Explanation:** Outline b / task 1.

---

## Additional Instructor Resources

- Next: 3.6.3 Hunt one named technique
