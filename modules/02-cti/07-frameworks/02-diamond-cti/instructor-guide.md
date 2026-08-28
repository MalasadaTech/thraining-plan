# Instructor Guide – Module 2.7.2 – Diamond Model Application in CTI

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.2 B / C / C ; 2.7.2.1 3c / 4c / 4d  
- Hunter: 2.7.2 B / C / C ; 2.7.2.1 3c / 4c / 4d  
- SOC: 2.7.2 A / B / B ; 2.7.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Fill four Diamond vertices from a report or activity set. Name the weakest. Reject a vendor-name Adversary fill.

**Context (plain language):**

- What this lesson is for: CTI analysts put Diamond on a report or activity set so the product shows what they know and what they do not. They name the weakest vertex and refuse to put a vendor APT name in Adversary.
- How it hooks to the lesson before: 2.7.1 put ATT&CK on a report. This lesson puts Diamond on that same kind of product.
- How it hooks to the lesson after: 2.7.3 is Kill Chain stages on a report.
- Why we are doing it this way: the shared Diamond lesson already named the vertices. This lesson is CTI application — the intel card — not a second floor lecture.
- What we are *not* doing in this lesson: ATT&CK IDs (2.7.1). Kill Chain stages (2.7.3). Actor profile (2.11). Attribution types and confidence cards (2.1.7). Hunt planning (3.5). The beacon POST (not the A12 activity set). No lab. Do not re-teach 0.6.2.
- Extra step: none.

Use the same names as the student guide: **Adversary**, **Capability**, **Infrastructure**, **Victim**, **weakest**, **vendor label**. **A12** is the classroom activity set in the student table. “PRD APT” is a vendor label, not Adversary evidence.

**Key Teaching Points:**
- Diamond on a CTI product (report or activity set), not a group name from a PDF.
- Fill all four vertices from evidence you have.
- Name the weakest vertex. That constraint drops a who-claim.
- Reject “Adversary = PRD APT.”

**Common Student Challenges:**
- Put a vendor APT name in Adversary. Why: the PDF title looks like a who. Example: writing “Adversary = PRD APT” with no internals that name the cluster.
- Fill the weakest vertex with a guess. Why: an empty who feels unfinished. Example: inventing a group so the card has four “answers.”
- Add the beacon POST to A12. Why: extra classroom rows reuse the same names. Example: putting a `checkin` POST on Infrastructure when the activity set is the GET `update.exe` chain.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.7.2 – Diamond Model application in CTI
- T: 2.7.2.1 – Apply the Diamond Model to an intelligence problem

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | CTI product: know / do not know |
| Key Concepts            | 12 min    | Four fills; weakest; reject vendor name |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: CTI puts Diamond on a report or activity set so hunt and detection see what is known and what is not.
- Name the four vertices. Fill them from the evidence in front of you. Do not re-teach the shared floor as if they had never seen Diamond.
- Walk A12 from the student table. Capability, Infrastructure, and Victim have internals. Adversary does not. Weakest is Adversary.
- Fail “Adversary = PRD APT.” A vendor label is not Adversary evidence. The product writes unknown cluster and names Adversary as weakest.
- If they add the beacon POST: that row is not the A12 activity set. Stay on encoded PowerShell, `update.exe`, the update domain / `203.0.113.88`, and **WS-JLEE** / `jlee`.
- If they start assigning ATT&CK IDs: that was 2.7.1. This lesson is Diamond on the product.
- If they start listing Kill Chain stages: that is 2.7.3.
- If they write an actor profile or a nation-state: that is 2.11 / 2.1.7. This lesson stops at the honest Adversary vertex.

---

## Knowledge Check – Answer Key

1. **A vendor APT name fills the Adversary vertex. True or false?**  
   **Answer:** False. A vendor APT name is a label on a PDF, not Adversary evidence.  
   **Explanation:** The task is to reject that fill. Write unknown cluster and name Adversary as weakest until internals support a cluster you can defend against.

2. **Name the four vertices.**  
   **Answer:** Adversary, Capability, Infrastructure, Victim.  
   **Explanation:** Those are the four fills on the CTI product. This lesson applies them to a report or activity set; it does not invent a fifth corner.

3. **Fill Diamond for A12 and name the weakest vertex.**  
   **Answer:** Capability = encoded PowerShell / `update.exe`. Infrastructure = update domain / `203.0.113.88`. Victim = **WS-JLEE** / `jlee` / DYA. Adversary = unknown cluster. Weakest = Adversary.  
   **Explanation:** Three vertices have internals from the activity set. Adversary does not. “PRD APT” does not change that.

---

## Additional Instructor Resources

- Next: 2.7.3 Kill Chain for CTI
