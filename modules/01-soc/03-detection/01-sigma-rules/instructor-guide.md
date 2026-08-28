# Instructor Guide – Module 1.3.1 – SIGMA Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.1.1 A / B / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 1a / 2b / 3c  
- Hunter: 1.3.1.1 B / C / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 2b / 3c / 4c  
- CTI: 1.3.1.1 A / B / B ; 1.3.1.2 1a / 2b / 3c ; 1.3.1.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a SIGMA rule and propose a basic create or modify. Do not deploy it.

**Context (plain language):**

- What this lesson is for: An alert comes from a detection. SOC analysts read that write-up and propose a basic create or modify. SIGMA is how you write what to look for once, in YAML, when the shop may not all use the same SIEM.
- How it hooks to the lesson before: 1.2 closed on sensor logs (last child 1.2.8). This lesson turns the 1.1.2 process story into a portable rule.
- How it hooks to the lesson after: 1.3.2 is Suricata — network rule syntax, not YAML.
- Why we are doing it this way: this unit is rule syntax and a first read/write. SOC proposes a basic rule. Detection engineering reviews and deploys. How detections run as a service is 4.x.
- What we are *not* doing in this lesson: Deploy. Run a converter. Suricata, YARA, or SIEM authorship. Alert triage (1.4). No lab.
- Extra step: none.

Use the same names as the student guide: **SIGMA**, **logsource**, **detection**, **condition**, and **selector** (a field test). The given is the same process story as 1.1.2 (script host, encoded PowerShell). Do not turn it into the intro plot.

**Key Teaching Points:**
- A rule needs title, logsource, and detection (named selections plus a condition).
- Selectors must match the logsource.
- Translation is table + where + boolean, in words. Not a converter lab.
- Broad “any PowerShell” is a poor proposal. SOC proposes; detection engineering reviews.

**Common Student Challenges:**
- Treat SIGMA as a SIEM product. Why: the YAML looks like a saved search. Example: asking which SIEM this SIGMA rule is already running in.
- Put a field on the wrong logsource. Why: they remember a Zeek or HTTP field. Example: putting `uri` on `process_creation`.
- Propose every `powershell.exe`. Why: they stop at the image name. Example: a rule whose only selector is `Image|endswith: '\powershell.exe'`.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.3.1.1 – SIGMA rules
- T: 1.3.1.2 – Analyze an existing SIGMA rule and describe what it detects
- T: 1.3.1.3 – Create or modify a basic SIGMA rule

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Propose, do not deploy |
| Key Concepts            | 16 min    | Structure, selectors, translate |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert comes from a detection. You read what it would fire on, and you propose a basic create or modify. You do not push it to production.
- Walk title, logsource, and detection. Condition lives inside detection. Stop there. Do not add status, level, or false-positive notes as required blocks.
- Selectors are field tests. Names must match the logsource. `Image` / `CommandLine` / `ParentImage` on `process_creation` are the process-create fields from 1.1.2.
- Translate in one sentence: logsource → table, selections → where, condition → and/or/not. Do not run a converter.
- Walk the given YAML. One sentence: encoded PowerShell from a script host. SIEM shape is DeviceProcessEvents or Sysmon 1 with those three predicates.
- Tightening “any powershell.exe” by adding parent or `-enc` is a modify. That is what good looks like for the create/modify task.
- If they open Suricata: that is 1.3.2.
- If they want to deploy: that is 4.x / detection engineering. Today you propose.
- If they put `uri` on `process_creation`: wrong logsource.
- If they start the intro plot: stay on the three selectors.

---

## Knowledge Check – Answer Key

1. **SIGMA is a SIEM product. True or false?**  
   **Answer:** False. It is a portable YAML detection format.  
   **Explanation:** You write what to look for once. A person or a converter turns it into a SIEM query. The SIGMA file is not itself a SIEM.

2. **A `process_creation` rule matches `powershell.exe`, CommandLine `-enc`, and parent `wscript`. In one sentence, what does it detect?**  
   **Answer:** Encoded PowerShell launched from a script host (process create: `powershell.exe` with `-enc`, parent `wscript`).  
   **Explanation:** The three tests sit in one selection, so they all must match. Same process story as 1.1.2.

3. **Why is a rule that matches every `powershell.exe` a poor proposal?**  
   **Answer:** It matches ordinary helpdesk and installer use as well as anything malicious. Tighten with a parent or a command-line token such as `-enc`.  
   **Explanation:** A basic create or modify still has to be specific. Image name alone is not a detection.

---

## Additional Instructor Resources

- Next: 1.3.2 Suricata rules
