# Instructor Guide – Module 2.1.7 – Attribution

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.7 B / C / C ; 2.1.7.1 3c / 4c / 4d  
- Hunter: 2.1.7 A / B / B ; 2.1.7.1 1a / 2b / 3c  
- SOC: 2.1.7 A / A / A ; 2.1.7.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Assess an attribution statement: type claimed versus evidence, and whether confidence is earned.

**Context (plain language):**

- What this lesson is for: CTI analysts name a cluster they can defend, at a type and a confidence, so collection, hunt, and defense aim at the right cluster. They assess a statement against the evidence. They do not invent a country they cannot prove.
- How it hooks to the lesson before: 2.1.6 was how you say it for a named audience. This lesson is who you claim.
- How it hooks to the lesson after: 2.1.8 is where you collect. Not the actor profile.
- Why we are doing it this way: after audience tailoring, name the type and the classroom confidence so an analyst can assess a claim against evidence before anyone writes a finished actor profile or a likelihood word.
- What we are *not* doing in this lesson: Estimative word list (2.2.1). Actor profile (2.11.1.2). Invent a nation-state. Collection source classes. No lab.
- Extra step: none.

Use the same names as the student guide: **purpose**, **challenges**, **activity group**, **nation-state**, and classroom **low / medium / high**. The givens use course-fiction names (**PRD APT**, **A12**, `203.0.113.88`). Do not tell the intro plot as proof of a government.

**Key Teaching Points:**
- Purpose is the cluster you can defend, not a country you cannot prove.
- Activity group is not a nation-state.
- Low / medium / high is classroom confidence. High needs several independent lines.
- A vendor label is not high-confidence nation-state.

**Common Student Challenges:**
- Treat a vendor APT name as a country. Why: the name sounds like a government unit. Example: “PRD APT is on the PDF, so this is a nation-state, high confidence.”
- Jump from one incident’s internals to a government. Why: malware and an IP feel like a complete story. Example: “encoded PowerShell and `203.0.113.88`, so this is a nation-state.”
- Use likely / almost certainly as the confidence word. Why: those words feel like certainty. Example: writing “likely a nation-state” when the task is type plus low / medium / high.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.1.7 – Attribution (purpose, confidence, types)
- T: 2.1.7.1 – Assess attribution statements for confidence and supporting evidence

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Cluster you can defend |
| Key Concepts            | 12 min    | Type + confidence; PDF fail |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: name who or what cluster sits behind activity, at a type and a confidence, so defense aims at the right cluster.
- Walk purpose and challenges. Shared hosting is not “theirs.” A false flag is planted. A vendor name is a label. One blog is one source.
- Write the two types. Activity group is a cluster you can defend. Nation-state is a government sponsor and needs more than a vendor label.
- Write classroom low / medium / high. High needs several independent lines. This is not a live ODNI card.
- Walk the vendor-PDF claim as a fail. Type over-claimed. Confidence too high. Evidence is a label.
- Walk the A12 given. Encoded PowerShell, an update domain, and `203.0.113.88` can support an activity cluster. They do not prove a government.
- If they write a country: ask what evidence is present.
- If they write the actor profile: that is 2.11.1.2. Stay on type and confidence.
- If they argue likely / almost certainly: that is 2.2.1. This lesson is low / medium / high.

---

## Knowledge Check – Answer Key

1. **A vendor “APT” name is high-confidence nation-state attribution. True or false?**  
   **Answer:** False. It is a label.  
   **Explanation:** A marketing or tracking name is not proof of a government sponsor, and it does not earn high confidence.

2. **What is the difference between an activity group and a nation-state?**  
   **Answer:** An activity group is a cluster of activity (infra, malware, ops). A nation-state is a government sponsor. You can defend a cluster without a country.  
   **Explanation:** Nation-state needs more than a vendor label.

3. **“Vendor PDF says PRD APT — high confidence nation-state.” Assess the claim.**  
   **Answer:** Type over-claimed. Confidence too high. Evidence is a label. Activity group / low is the honest read until independent evidence supports more.  
   **Explanation:** The task is to name type claimed, confidence claimed, and whether the evidence present earns both.

---

## Additional Instructor Resources

- Next: 2.1.8 Collection sources and methods
