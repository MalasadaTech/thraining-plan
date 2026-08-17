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

- What this hour is for: SOC analysts need a portable way to write what to look for before they live in one SIEM’s syntax.
- How it hooks to the hour before: 1.2 closed on sensor logs. This hour turns the 1.1.2 process story into a rule.
- How it hooks to the hour after: 1.3.2 is Suricata — network rule syntax, not YAML.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c only. SOC create is 1a/2b/3c — propose, do not ship. 4.x is the service.
- What we are *not* doing this hour: Deploy. sigmac. Suricata / YARA. Alert triage (1.4). No lab.
- Extra step: none.

Use the encoded PowerShell + wscript given. Do not invent Night Owl. Do not tell the PRD plot.

**Key Teaching Points:**
- logsource + detection + condition.
- Selectors match the logsource.
- Translation is table + where + boolean.
- Broad “any PowerShell” is a poor proposal.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.3.1.1 ; T 1.3.1.2 ; T 1.3.1.3

---

## Suggested Timing

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

Walk the three blocks. Read the given YAML out loud. Translate to DeviceProcessEvents in one sentence.

If they open Suricata: “1.3.2.”  
If they want to deploy: “4.x / DE. You propose.”  
If they put `uri` on process_creation: “Wrong logsource.”

---

## Knowledge Check – Answer Key

1. **SIGMA is a SIEM product. True or false?**  
   **Answer:** False. It is a portable YAML detection format.  
   **Explanation:** Outline a.

2. **The given rule — what does it detect?**  
   **Answer:** Process create of PowerShell with `-enc` and parent wscript.  
   **Explanation:** Outline b and 1.3.2 task 1.

3. **Why is every powershell.exe a poor proposal?**  
   **Answer:** It matches helpdesk, installers, and C2. Tighten with parent or command-line token.  
   **Explanation:** Outline b / 1.3.2 task 2.

---

## Additional Instructor Resources

- Next: 1.3.2 Suricata rules
