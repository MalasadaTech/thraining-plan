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
Write hypothesis, scope, priority, unique pattern. No invented ticket.

**Context (plain language):**

- What this hour is for: Hunters bound the search before they query.
- How it hooks to the hour before: 3.2.1 was the type.
- How it hooks to the hour after: 3.3.1 is hunt use of external tools.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d. Card = four lines.
- What we are *not* doing this hour: Local template. SIEM session. “Hunt persistence.” No lab.
- Extra step: none.

**Key Teaching Points:**
- Unique = `Updater`, not any Run key.
- Priority = open incident + FN, not a blog.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 3.2.2 ; T 3.2.2.1–3.2.2.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Bound the search |
| Key Concepts            | 12 min    | Four lines |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the four pieces. Walk A12 card. Fail “any malware” and “any Run key.”

If they invent a Jira: “3.7.”

---

## Knowledge Check – Answer Key

1. **Search everything. True or false?**  
   **Answer:** False. Bounded card.  
   **Explanation:** Outline b.

2. **Four pieces?**  
   **Answer:** Hypothesis, scope, priority, unique pattern.  
   **Explanation:** Outline a–d.

3. **A12 hypothesis + pattern?**  
   **Answer:** If persistors exist, Run `Updater` → Temp `update.exe`. Pattern = value name `Updater` (not any Run key).  
   **Explanation:** Tasks 1 and 3.

---

## Additional Instructor Resources

- Next: 3.3.1 Hunt tool capabilities
