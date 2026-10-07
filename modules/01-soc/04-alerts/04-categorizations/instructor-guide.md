# Instructor Guide – Module 1.4.4 – Common Alert Categorizations

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.4.1 A / B / C ; 1.4.4.2 2b / 3c / 4c  
- Hunter: 1.4.4.1 B / C / C ; 1.4.4.2 2b / 3c / 4c  
- CTI: 1.4.4.1 A / A / A ; 1.4.4.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

An activity category tells the next analyst what kind of behavior or access the evidence supports. It serves a different purpose from TP/FP classification, which evaluates a detection result. Clear category reasoning helps avoid overstating an attacker’s access.

## Learning Objectives

1. Describe the syllabus activity categories and their local use.
2. Assign a supported category to a supplied event.
3. Explain why a plausible adjacent category is less supported.

**Mapped Proficiency Items:**
- K: 1.4.4.1 – Common alert categorizations
- T: 1.4.4.2 – Assign a category to an alert and justify why it is not the adjacent category

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required.

Use the proficiency levels above to adjust prompting and explanation depth. The module focuses on its mapped knowledge and tasks; the linked next lesson develops the next step.

## Suggested Timing

| Section | Minutes | Focus |
|---|---|---|
| Opening | 2 | Connect the lesson to its purpose. |
| Explanation and worked example | 12 | Read the supplied evidence and demonstrate the reasoning. |
| Knowledge check and feedback | 6 | Complete the interpretation or modification tasks. |
| Summary and transition | 2 | Consolidate the result and connect the next lesson. |
| **Total** | **22** | |

## Detailed Teaching Notes

### 1. Using the course categories

Explain that the course taxonomy is preserved for syllabus alignment. Focus on evidence, not assumptions about account names.

**Key point to reinforce:** Use scanning, root-level, user-level, unsuccessful, or an actual local category according to its definition.

### 2. Comparing similar cases

Use the same command under two explicitly different execution contexts. Ask learners to change only the conclusion supported by that difference.

**Key point to reinforce:** Execution context supports privilege conclusions. A suspicious command or service label does not establish elevation.

### 3. Writing a justified category

Require a plausible alternative and a concrete reason. Permit uncertainty when the supplied facts do not establish an attempt or privilege level.

**Key point to reinforce:** State the category, evidence, and why a plausible alternative is less supported.

**Teaching boundary:** the non-elevated `labuser` PowerShell record is a separate classroom example, not A12.

## Knowledge Check — Answer Key

### 1. Name the four syllabus categories and explain how Other is used.

**Expected answer:** Scanning/reconnaissance, root-level access, user-level access, and unsuccessful activity; Other uses an actual local category and definition.

### 2. Categorize the supplied non-elevated labuser event and explain why root-level is unsupported.

**Expected answer:** User-level activity for this event, based on the supplied execution context. No privileged execution is established by the encoding argument.

### 3. How would you distinguish a port sweep from a failed login, and why is HTTP 401 alone insufficient?

**Expected answer:** A discovery sweep supports scanning; a verified failed access attempt supports unsuccessful activity. A 401 may be part of normal authentication rather than evidence of a completed failed attack.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Choose an activity category from the observed behavior and access context. Explain the evidence and a plausible alternative, and use local definitions for mixed activity or additional categories.

Previous: [1.4.3 – Common False Positive Causes](../03-false-positive-causes/student-guide.md)

Next: [1.4.5 – SLA / Response Time Goals](../05-sla-response-times/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)
