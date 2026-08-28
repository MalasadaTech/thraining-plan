# Instructor Guide – Module 0.6.1 – MITRE ATT&CK

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.1.1 A / B / C ; 0.6.1.2 2b / 3c / 4c  
- Hunter: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- CTI: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- DE: 0.6.1.1 A / B / B ; 0.6.1.2 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Give every role one language for what the adversary was trying to do and how, and show what a labeled line with a cited field looks like.

**Context (plain language):**

- What this lesson is for: People on different desks will look at the same host or log. They need one name for what the adversary was trying to do and how. This lesson is that shared language, and what a labeled line with a cited field looks like.
- How it hooks to the lesson before: 0.5 said the same evidence can sit on more than one desk, and the product is different. This lesson is a shared label for behavior, not a product.
- How it hooks to the lesson after: 0.6.2 Diamond is four vertices and the weakest one. Kill Chain is 0.6.3.
- Why we are doing it this way: Frameworks sit before SOC so hunt, CTI, and DE are not learning ATT&CK as a SOC-only trick. Hunt planning and CTI products stay later.
- What we are *not* doing in this lesson: Hunt planning (3.5). CTI product mapping (2.7.1). Diamond vertices. Kill Chain stages. Alert categories (1.4). Actor profiles (2.11). DTF (2.7.4). No lab.
- Extra step: none.

Use the same names as the student guide: **tactic**, **technique**, **sub-technique**, **map**, and **cited field**. A **map** is the label: tactic + technique or sub-technique + one cited field. **Row** is the outline word for the line of activity; here it means the log or event in front of you, not a SIEM table. The official tactic name is **Command and Control**, not C2, unless you gloss it after the student-guide word.

**Key Teaching Points:**
- ATT&CK labels behavior. Tactic is why. Technique or sub-technique is how.
- A map is tactic + ID + name + one cited field.
- If two IDs fit, pick the primary for this line and reject the neighbor.
- An ID with no cited field is not a map.

**Common Student Challenges:**
- Swap tactic and technique. Why: both are ATT&CK words. Example: calling Execution a technique.
- Write Command and Control because it might beacon later. Why: they label the next stage, not this line. Example: `T1059.001` written as Command and Control with no callback field.
- Treat an ID with no cited field as finished. Why: the ID looks official. Example: writing `T1059.001` with no command line.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 0.6.1.1 – MITRE ATT&CK
- T: 0.6.1.2 – Map observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Shared language, not a product |
| Key Concepts            | 10 min    | Structure + one map |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: four desks can look at the same host, and they still need one name for the goal and the how.
- Write tactic = why, technique = how. Sub-technique is a more specific how. Use `T1059` and `T1059.001`. Do not memorize the matrix.
- Enterprise matrix: columns are tactics, cells are techniques and sub-techniques.
- Walk the given: `wscript` launched encoded PowerShell. Execution / `T1059.001` PowerShell. Cite the encoded command line.
- If they write Command and Control: there is no beacon in this line. That ID has no cited field.
- If they start hunt coverage or Navigator: that is 3.5.
- If they start putting IDs on a report or activity set: that is 2.7.1.
- If they start Diamond vertices: that is 0.6.2.
- DE sits this at awareness. Do not start them at hunt-planning depth.

---

## Knowledge Check – Answer Key

1. **What is a tactic, and what is a technique?**  
   **Answer:** A tactic is the goal (why). A technique is a named how.  
   **Explanation:** Columns are tactics. Cells are techniques. A sub-technique is a more specific how (`T1059` / `T1059.001`).

2. **An ATT&CK ID with no cited field is a finished map. True or false?**  
   **Answer:** False. An ID with no cited field is not a map.  
   **Explanation:** A finished map is tactic + technique or sub-technique + one field that actually shows it.

3. **Encoded PowerShell ran from a script. Name a tactic and a technique (or sub-technique) and what you would cite.**  
   **Answer:** Execution / `T1059.001` (or `T1059`). Cite the encoded command line. Not Command and Control.  
   **Explanation:** This line shows a scripting interpreter. It does not show a beacon.

---

## Additional Instructor Resources

- Next: 0.6.2 Diamond Model
