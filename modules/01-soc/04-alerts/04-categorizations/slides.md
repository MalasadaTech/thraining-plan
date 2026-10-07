# Module 1.4.4 – Common Alert Categorizations

- Describe the syllabus activity categories and their local use.
- Assign a supported category to a supplied event.
- Explain why a plausible adjacent category is less supported.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

An activity category tells the next analyst what kind of behavior or access the evidence supports. It serves a different purpose from TP/FP classification, which evaluates a detection result. Clear category reasoning helps avoid overstating an attacker’s access.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Using the course categories

Use scanning, root-level, user-level, unsuccessful, or an actual local category according to its definition.

**Speaker notes:** Explain that the course taxonomy is preserved for syllabus alignment. Focus on evidence, not assumptions about account names.

---

## Reference — Using the course categories

| Category | Evidence that supports it | Useful distinction |
|---|---|---|
| Scanning / reconnaissance | Probing intended to discover hosts, services, or other information. | Compare discovery activity with a failed access attempt. |
| Root-level access | Evidence of privileged control, such as root, SYSTEM, or relevant elevated administrative execution. | A service account or service process is not automatically privileged. |
| User-level access | Evidence of activity within a standard or non-elevated user execution context. | A suspicious command does not itself establish elevation. |
| Unsuccessful activity | Evidence that an access or exploitation attempt failed. | Distinguish the attempted action from a discovery probe. |
| Other (local) | An applicable category defined by the organization. | Use its actual definition rather than inventing a local label. |

**Speaker notes:** Explain that the course taxonomy is preserved for syllabus alignment. Focus on evidence, not assumptions about account names. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Comparing similar cases

Execution context supports privilege conclusions. A suspicious command or service label does not establish elevation.

**Speaker notes:** Use the same command under two explicitly different execution contexts. Ask learners to change only the conclusion supported by that difference.

---

## Supplied example

A separate classroom PowerShell example (not A12) runs under `labuser` with a recorded Medium integrity, non-elevated context. That supports user-level activity for this event. It does not prove that the account lacks every administrative membership or that no privileged activity occurred elsewhere.

**Speaker notes:** Use the same command under two explicitly different execution contexts. Ask learners to change only the conclusion supported by that difference.

---

## Writing a justified category

State the category, evidence, and why a plausible alternative is less supported.

**Speaker notes:** Require a plausible alternative and a concrete reason. Permit uncertainty when the supplied facts do not establish an attempt or privilege level.

---

## Knowledge check

1. Name the four syllabus categories and explain how Other is used.
2. Categorize the supplied non-elevated labuser event and explain why root-level is unsupported.
3. How would you distinguish a port sweep from a failed login, and why is HTTP 401 alone insufficient?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

Choose an activity category from the observed behavior and access context. Explain the evidence and a plausible alternative, and use local definitions for mixed activity or additional categories.

Previous: [1.4.3 – Common False Positive Causes](../03-false-positive-causes/student-guide.md)

Next: [1.4.5 – SLA / Response Time Goals](../05-sla-response-times/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
