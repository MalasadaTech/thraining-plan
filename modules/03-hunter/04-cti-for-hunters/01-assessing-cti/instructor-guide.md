# Instructor Guide – Module 3.4.1 – Assessing CTI for Hunting Value

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.1 B / C / C ; 3.4.1.1 3c / 4c / 4d  
- SOC: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
- CTI: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Label a CTI report hunt-worthy, awareness-only, or a hand-off, and say why. Do not extract leads yet.

**Context (plain language):**

- What this lesson is for: Hunters read a CTI report and decide whether it is worth a hunt before they pull leads. A report can name an actor and still not be a hunt.
- How it hooks to the lesson before: 3.3.1 turned an external tool finding into a precise internal query.
- How it hooks to the lesson after: 3.4.2 extracts leads from reports that passed this gate.
- Why we are doing it this way: label first so you do not hunt awareness-only reports, and so you do not take work detections or IR already own.
- What we are *not* doing in this lesson: extracting TTPs or IOCs (3.4.2). Authoring STIX (3.4.3). Mapping ATT&CK coverage (3.5). Inventing a hunt ticket (3.7). No lab.
- Extra step: none.

Use the same names as the student guide: **hunt-worthy**, **awareness-only**, **hand-off**, **actionable for a hunt**, **question**, **telemetry**, **scope**, and **rapid triage**. **Gate** means this label, not a ticket. Do not say **bulletin** — the student word is **report**. The hunt-worthy given reuses classroom objects (`GET /update.exe`, HKCU Run **`Updater`**, `203.0.113.88:8080`). Do not turn it into the intro plot.

**Key Teaching Points:**
- Interesting is not a hunt.
- Actionable for a hunt is question, telemetry, and scope.
- Rapid triage is a label and one sentence why.

**Common Student Challenges:**
- Treat an interesting actor profile as hunt-worthy. Why: a named APT feels like a lead. Example: opening a hunt because the PDF named an actor and listed no object, telemetry, or scope.
- Copy every ATT&CK ID before labeling. Why: they think triage is extract. Example: a TTP table with no hunt / don’t hunt / hand off line.
- Invent a hunt ticket name. Why: they want a place to put the label. Example: writing “open HUNT-A12.” Local tickets are 3.7.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.4.1 – Assessing CTI for hunting value
- T: 3.4.1.1 – Triage a CTI report: hunt / don’t hunt / hand off, and say why

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Label first; do not extract |
| Key Concepts            | 12 min    | Three labels; question / telemetry / scope; three givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a CTI report landed, and you have to say whether it is worth a hunt.
- Write the three labels. Map them to hunt / don’t hunt / hand off.
- Walk question, telemetry, and scope. Stop there. Do not extract the lead list.
- Walk the three givens from the student guide. The product is the label and one sentence why, not a TTP table.
- If they start copying ATT&CK IDs: that is 3.4.2 and 3.5. Today is only the label.
- If they invent a hunt ticket: that is 3.7.
- If they author STIX: that is 3.4.3.

---

## Knowledge Check – Answer Key

1. **An interesting actor profile is a hunt. True or false?**  
   **Answer:** False. Awareness-only unless you can name a question, telemetry, and scope.  
   **Explanation:** A named actor is context. It is not hunt-worthy until the three pieces exist.

2. **What three things must you name before a report is actionable for a hunt?**  
   **Answer:** A hunt question. Telemetry that could answer it here. A bound scope.  
   **Explanation:** Those three are the hunter’s test. “Interesting” is not enough.

3. **Label this report and say why: `GET /update.exe` to `:8080`, HKCU Run `Updater`, registry and HTTP logs exist, no detection on that path, no open IR.**  
   **Answer:** **Hunt-worthy** — hunt. Named objects, telemetry exists, no detection covers that path, no open IR.  
   **Explanation:** You can name the question, the telemetry, and the scope. That is the task product: hunt, plus why.

---

## Additional Instructor Resources

- Next: 3.4.2 Extracting hunt leads from CTI
