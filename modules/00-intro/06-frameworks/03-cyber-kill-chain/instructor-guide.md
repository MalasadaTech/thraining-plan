# Instructor Guide – Module 0.6.3 – Cyber Kill Chain

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.3.1 A / B / C ; 0.6.3.2 2b / 3c / 4c  
- Hunter: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- CTI: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- DE: 0.6.3.1 A / B / B ; 0.6.3.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the seven Kill Chain stages and place the activity you have on one of them, so a first payload is not the whole intrusion.

**Context (plain language):**

- What this lesson is for: You often see one step of an attack. This lesson is how you name where that step sits, and refuse the previous or next stage you did not see.
- How it hooks to the lesson before: 0.6.2 Diamond organized what you know into four corners. This lesson stages the same activity in time.
- How it hooks to the lesson after: 0.7 is the tool survey — when to pick VirusTotal, AnyRun, Silent Push, or URLScan.
- Why we are doing it this way: shared floor before SOC. One staging model for every role. CTI product depth stays later.
- What we are *not* doing in this lesson: ATT&CK IDs. Diamond fill. Listing every supported stage on an intelligence product (2.7.3). Hunt planning. No lab.
- Extra step: none.

Use the same names as the student guide: **Reconnaissance**, **Weaponization**, **Delivery**, **Exploitation**, **Installation**, **Command and Control**, and **Actions on Objectives**. **Row** is the SIEM-table gloss from the student intro, not the headline word. It means the one activity in front of you.

**Key Teaching Points:**
- Seven stages, in order. Lockheed Martin Cyber Kill Chain.
- Place this activity on one stage. Reject the previous or next stage you did not see.
- Do not invent the rest of the chain.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 0.6.3.1 – Cyber Kill Chain
- T: 0.6.3.2 – Identify the Kill Chain stage of observed activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Where this step sits |
| Key Concepts            | 8 min     | Stages + one place |
| Knowledge Check         | 3 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~15 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: you often see one step of an attack, and you have to name where it sits so a first payload is not the whole intrusion.
- Write the seven stages in order. Stop there. Do not add Unified Kill Chain or ATT&CK tactics.
- Walk the given: a `.vbs` in email is Delivery. Fail Weaponization (you did not see them build it) and Exploitation (you did not see it run). Command and Control is not the next stage — it is further down the chain, and there is no callback.
- If they start mapping ATT&CK IDs: that is 0.6.1. Today is the stage, not the technique.
- If they start filling Diamond vertices: that is 0.6.2.
- If they list all seven stages on a product because “the chain must have happened”: that is 2.7.3. Today is one activity, one stage.
- DE sits this at awareness. Do not start them at CTI product depth.

---

## Knowledge Check – Answer Key

1. **What is the Cyber Kill Chain for?**  
   **Answer:** Staging attack progression. It is a staging tool, not a complete model of every intrusion.  
   **Explanation:** The chain names where a step sits in time. It does not describe every intrusion by itself.

2. **Name the seven stages in order.**  
   **Answer:** Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Actions on Objectives.  
   **Explanation:** Lockheed Martin Cyber Kill Chain. Order matters. Do not add extra stages.

3. **A user received a `.vbs` in email. Why is that Delivery, and why is it not Exploitation?**  
   **Answer:** You saw it arrive. You did not see it run. Exploitation is the next stage you do not have.  
   **Explanation:** Delivery is the weapon arriving. The previous stage you also did not see is Weaponization (building it). Do not skip to Command and Control without a callback.

---

## Additional Instructor Resources

- Next: 0.7 External tools
