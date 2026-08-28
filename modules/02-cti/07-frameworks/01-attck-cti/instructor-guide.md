# Instructor Guide – Module 2.7.1 – MITRE ATT&CK for CTI Analysis and Reporting

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- Hunter: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- SOC: 2.7.1 A / B / B ; 2.7.1.1 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Put ATT&CK on a report or activity set for a CTI product: tactic, technique or sub-technique, and evidence. Reject the neighbor ID.

**Context (plain language):**

- What this lesson is for: CTI analysts put ATT&CK IDs on a product so hunt and detection can reuse the same names. You extract named behaviors from a report or activity set and write only the IDs this product can support.
- How it hooks to the lesson before: 2.6.1 was DNS for enrichment and pivoting. This lesson is behavior IDs on a CTI product.
- How it hooks to the lesson after: 2.7.2 fills Diamond vertices from the same kind of report or activity set. It does not assign ATT&CK IDs.
- Why we are doing it this way: the shared floor labeled one activity. This lesson is the CTI application — a report or activity set, TTP extraction onto IDs, and a rejected neighbor. It is not a second copy of that floor lesson.
- What we are *not* doing in this lesson: hunt coverage planning (3.5). DTF pivot IDs (2.7.4). SOC alert categories (1.4.4). Which TTPs apply to this shop (2.8.2). Diamond vertices (2.7.2). Actor attribution (2.11). No lab.
- Extra step: none.

Use the same names as the student guide: **tactic**, **technique**, **sub-technique**, **evidence**, **neighbor**, **report**, **activity set**, and **TTP**. **TTP** means tactics, techniques, and procedures — named behaviors you extract onto ATT&CK IDs. A **neighbor** is a nearby ID that looks close; reject it if this product does not show it. Do not teach the Enterprise matrix as columns and cells. Do not walk hunt coverage.

**Key Teaching Points:**
- A CTI ATT&CK line is tactic, technique or sub-technique, and a cite from this product.
- Encoded PowerShell from `wscript` is Execution / T1059.001, not Command and Control.
- A GET of `/update.exe` is T1105 when the product is the download, not T1059.
- An ID with no evidence is not a map.

**Common Student Challenges:**
- Jump to Command and Control because encoded PowerShell “might beacon later.” Why: they map a later guess, not this product. Example: writing C2 on the `wscript` → `-enc` line with no callback.
- Paste a vendor T-ID list with no cite. Why: the PDF already printed IDs. Example: copying T1059.003 Windows Command Shell when the command line is PowerShell `-enc`.
- Write T1059 as the SOC queue category. Why: the ID looks like a ticket label. Example: “category = T1059” instead of Execution / T1059.001 plus a cite.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.7.1 – MITRE ATT&CK for CTI analysis and reporting
- T: 2.7.1.1 – Map activity or reports to MITRE ATT&CK

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Product-level map; why CTI writes the line |
| Key Concepts            | 12 min    | Tactic / ID / cite; two givens; reject the neighbor |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: CTI puts ATT&CK on a product so hunt and detection can reuse the same names. Extract TTPs from a report or activity set. Write only what this product can support.
- Write the four pieces: tactic (why), technique or sub-technique (how), evidence (the cite), neighbor (the nearby ID you reject). Stop. Do not teach matrix columns.
- Walk the first given: `wscript` launched encoded PowerShell. Execution / T1059.001. Cite `-enc` and the parent. Command and Control is the neighbor because there is no beacon in this product.
- Walk the second given: GET `/update.exe` on port 8080, product is the download. Command and Control / T1105. Cite the URI. T1059 is the neighbor because that ID is a command interpreter, not an HTTP GET. T1105 is a technique under Command and Control, not a second tactic.
- If they start hunt coverage or Navigator: that is 3.5.
- If they write T1059 as an alert category: that is 1.4.4. Today is a CTI mapped line.
- If they ask which IDs apply to this shop: that is 2.8.2. Today is evidence-bound mapping, not applicability.
- If they open Diamond vertices or DTF P-IDs: those are 2.7.2 and 2.7.4.

---

## Knowledge Check – Answer Key

1. **An ATT&CK ID with no cited evidence is a finished CTI map. True or false?**  
   **Answer:** False. An ID with no evidence is a slogan, not a map.  
   **Explanation:** A CTI line needs the tactic, the technique or sub-technique, and a cite from this product.

2. **What three things must a CTI ATT&CK line have?**  
   **Answer:** Tactic, technique or sub-technique, and evidence.  
   **Explanation:** That is the product hunt and detection can reuse. Rejecting the neighbor is how you finish the choice when two IDs look close.

3. **`wscript` launched encoded PowerShell (`-enc`). Name the tactic, the ID, and why it is not Command and Control.**  
   **Answer:** Execution / **T1059.001**. This product does not show a beacon.  
   **Explanation:** The parent and the `-enc` command line support PowerShell execution. Command and Control would need callback or C2 traffic in this product.

---

## Additional Instructor Resources

- Next: 2.7.2 Diamond Model for CTI
