# Instructor Guide – Module 1.4.1 – Alert Context and Investigation

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.1.1 A / B / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- Hunter: 1.4.1.1 B / C / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- CTI: 1.4.1.1 A / A / B ; 1.4.1.2 1a / 1a / 2b ; 1.4.1.3 1a / 1a / 2b ; 1.4.1.4 1a / 1a / 2b ; 1.4.1.5 1a / 1a / 1a ; 1.4.1.6 1a / 1a / 1a  
**Estimated Time:** 30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

An alert is the starting point for an investigation. Before deciding what it means, establish what evidence it contains, what logic produced it, and what related records can add. This makes the eventual finding traceable to observations rather than to the alert title alone.

## Learning Objectives

1. Identify present and missing alert context, including an approved lookup of an available indicator.
2. Explain the alert configuration and trace its actual upstream detection path.
3. Select related endpoint logs and describe what they add or fail to add.
4. Select related PCAP for a network question and describe its contribution or availability limit.

**Mapped Proficiency Items:**
- K: 1.4.1.1 – Alert context and investigation
- T: 1.4.1.2 – Review an alert and identify which context is present and which is missing (include VirusTotal on a hash, IP, or domain you have)
- T: 1.4.1.3 – Review the alert configuration and explain what would fire
- T: 1.4.1.4 – Trace an alert to its upstream detection logic and name each hop
- T: 1.4.1.5 – Collect related endpoint logs and state what they add (or fail to add)
- T: 1.4.1.6 – Collect related PCAP and state what it adds versus the alert fields

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required.

Use the proficiency levels above to adjust prompting and explanation depth. The module focuses on its mapped knowledge and tasks; the linked next lesson develops the next step.

## Suggested Timing

| Section | Minutes | Focus |
|---|---|---|
| Opening | 2 | Connect the lesson to its purpose. |
| Explanation and worked example | 20 | Read the supplied evidence and demonstrate the reasoning. |
| Knowledge check and feedback | 6 | Complete the interpretation or modification tasks. |
| Summary and transition | 2 | Consolidate the result and connect the next lesson. |
| **Total** | **30** | |

## Detailed Teaching Notes

### 1. Establishing context and detection lineage

Draw only the supplied lineage. Ask learners to explain the rule’s actual predicates rather than paraphrasing its title.

**Key point to reinforce:** Record present and missing context, explain the rule, and trace the actual event-to-alert path.

### 2. Adding relevant evidence

Use the table to connect each collection action to a question. Explain that finding a record is not the same as establishing its relevance.

**Key point to reinforce:** Collect related endpoint events, approved indicator lookups, and relevant retained packets. State what each contributes.

### 3. Working through a reviewable finding

Have learners produce the present/missing and contribution statements from the examples. Use a provided sanitized lookup result if available; otherwise label it pending rather than making a live submission.

**Key point to reinforce:** Preserve evidence references and unresolved questions. Distinguish unavailable capture from an irrelevant network question.

## Knowledge Check — Answer Key

### 1. For the process example, identify what context is present and missing, then explain the SIEM rule configuration and upstream event-to-alert path.

**Expected answer:** Present are host, account, process creation, parent, and command-line pattern. Unresolved questions include decoded behavior, authorization, and related activity. The rule tests the supplied process predicates and trigger; the path is endpoint event → ingested table → SIEM rule → alert. A Suricata stage is not supplied.

### 2. You have a related hash and a file event. What should collection and a VirusTotal lookup contribute, and what would each still leave unresolved?

**Expected answer:** Preserve and correlate the file event using host, time, path, and process evidence. Look up the actual hash and record the report/time and relevant result or absence of a report. The file event does not automatically establish execution or causation, and the external lookup does not establish local behavior beyond the evidence supplied.

### 3. A network alert has IP/port only. What would you request from PCAP, and how would you document an unavailable capture?

**Expected answer:** Request the relevant flow/time/sensor to seek details such as a visible HTTP URI. Record what the packets add, or explicitly state that relevant capture is unavailable; do not invent content.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

An investigation record should explain the alert’s evidence, logic, and lineage, then show what related endpoint records, lookups, and packets contribute. Clear unresolved questions make the next decision easier to support.

Previous: [1.3.4 – SIEM Rules](../../03-detection/04-siem-rules/student-guide.md)

Next: [1.4.2 – Alert Classification](../02-classification/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching)
- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html)
