# Instructor Guide – Module 2.7.3 – Cyber Kill Chain in Intelligence Analysis

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.3 B / C / C ; 2.7.3.1 3c / 4c / 4c  
- Hunter: 2.7.3 B / C / C ; 2.7.3.1 3c / 4c / 4c  
- SOC: 2.7.3 A / B / B ; 2.7.3.1 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Put attack progression on an intelligence product. Name the stage, reject the neighbor, and list only supported stages.

**Context (plain language):**

- What this lesson is for: CTI analysts put attack progression on a product so the reader sees what was observed, and what was not. Hunt and IR use that list. A stage you invent becomes work on a step that is not in the evidence.
- How it hooks to the lesson before: 2.7.2 used Diamond to show what you know and do not know on four vertices. This lesson is progression — where in the chain the activity sits.
- How it hooks to the lesson after: 2.7.4 is DTF discovery pivots, not Kill Chain stages.
- Why we are doing it this way: this is CTI application of the seven names, not a recopy of the shared-floor staging lesson. The product lists only stages you can cite.
- What we are *not* doing in this lesson: ATT&CK IDs (2.7.1). Diamond fill (2.7.2). DTF (2.7.4). Hunt planning (3.5). No lab.
- Extra step: none.

Use the same names as the student guide: **progression**, **stage**, **product** (the write-up you issue), **supported** (you can cite it), **unobserved**, and the seven stages. **Command and Control** is the stage name; **C2** is the same thing after you have said it once. The givens use course-fiction names (`invoice.vbs`, `-enc`). Do not turn them into the intro plot.

**Key Teaching Points:**
- Seven stage names, used on a CTI product — not a template to fill all seven.
- Encoded PowerShell is Installation, not Command and Control, unless you have a callback.
- `GET /update.exe` is not Reconnaissance.
- The product lists only supported stages.

**Common Student Challenges:**
- List all seven because “they must have done recon.” Why: people complete the chain in their heads. Example: writing Reconnaissance on a product that only has a process create.
- Call encoded PowerShell Command and Control. Why: later stages feel like the “real” intrusion. Example: writing C2 from `wscript` → `-enc` with no callback.
- Call `GET /update.exe` Reconnaissance. Why: any outbound HTTP looks like “looking around.” Example: listing Reconnaissance because the host fetched a file.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.7.3 – Cyber Kill Chain in intelligence analysis
- T: 2.7.3.1 – Identify the Kill Chain stage of observed or reported activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Progression on the product |
| Key Concepts            | 12 min    | Seven names; two givens; only supported stages |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: CTI puts progression on the product so hunt and IR see what was observed and what was not.
- Write the seven names. Stop. Do not teach ATT&CK IDs or Diamond vertices.
- A supported stage is one you can cite. The product is not a form with seven blanks.
- Walk the first given: `wscript.exe` (Temp `invoice.vbs`) → `powershell.exe -enc …`. Installation. Cite the process. Not Command and Control — there is no beacon. Delivery of the vbs only if arrival is in the evidence.
- Walk the second given: `GET /update.exe` on port 8080. Installation of the payload, or Command and Control if that GET is the control channel. Not Reconnaissance.
- If they list all seven: the product lists only what they can cite. Invented Reconnaissance is an unobserved stage.
- If they write C2 on the process given: there is no callback in that activity.
- If they start mapping T1059: that is 2.7.1.
- If they start a DTF pivot: that is 2.7.4.
- If they start the intro plot (Run key, vendor APT name): stay on the stage of the given activity.

---

## Knowledge Check – Answer Key

1. **You should list all seven stages on every product. True or false?**  
   **Answer:** False. List only supported stages — stages you can cite.  
   **Explanation:** The product is not a template. An unobserved stage (Reconnaissance you did not see, Weaponization you did not see) stays off the list.

2. **`GET /update.exe` on port 8080. Is that Reconnaissance? Why or why not?**  
   **Answer:** No. Fetching a payload is not target research.  
   **Explanation:** That GET is Installation of the payload, or Command and Control if that GET is the control channel. Reconnaissance is the unobserved neighbor people write anyway.

3. **`wscript` → `-enc`. Stage, and why not the neighbor?**  
   **Answer:** **Installation**. Cite the process. Not Command and Control — there is no beacon in that activity. Delivery of the vbs only if the product also has it arriving.  
   **Explanation:** The process is code on the host. A later stage with no callback is the neighbor to reject.

---

## Additional Instructor Resources

- Next: 2.7.4 Defender’s ThreatMesh Framework (DTF)
