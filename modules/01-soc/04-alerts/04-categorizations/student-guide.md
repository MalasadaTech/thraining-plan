# Module 1.4.4 – Common Alert Categorizations

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.4.1 A / B / C ; 1.4.4.2 2b / 3c / 4c  
- Hunter: 1.4.4.1 B / C / C ; 1.4.4.2 2b / 3c / 4c  
- CTI: 1.4.4.1 A / A / A ; 1.4.4.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Describe the syllabus activity categories and their local use.
2. Assign a supported category to a supplied event.
3. Explain why a plausible adjacent category is less supported.

**Mapped Proficiency Items:**
- K: 1.4.4.1 – Common alert categorizations
- T: 1.4.4.2 – Assign a category to an alert and justify why it is not the adjacent category

## Why This Matters

An activity category tells the next analyst what kind of behavior or access the evidence supports. It serves a different purpose from TP/FP classification, which evaluates a detection result. Clear category reasoning helps avoid overstating an attacker’s access.

## 1. Using the course categories

These are the syllabus categories, not a universal taxonomy. Use the definitions and labels adopted by your organization when applying them at work.

| Category | Evidence that supports it | Useful distinction |
|---|---|---|
| Scanning / reconnaissance | Probing intended to discover hosts, services, or other information. | Compare discovery activity with a failed access attempt. |
| Root-level access | Evidence of privileged control, such as root, SYSTEM, or relevant elevated administrative execution. | A service account or service process is not automatically privileged. |
| User-level access | Evidence of activity within a standard or non-elevated user execution context. | A suspicious command does not itself establish elevation. |
| Unsuccessful activity | Evidence that an access or exploitation attempt failed. | Distinguish the attempted action from a discovery probe. |
| Other (local) | An applicable category defined by the organization. | Use its actual definition rather than inventing a local label. |

Activities may be mixed or incompletely observed. Choose the category supported for the described activity and explain uncertainty or additional categories according to local practice.

## 2. Comparing similar cases

The course PowerShell example runs under `jlee` with a recorded Medium integrity, non-elevated context. That supports user-level activity for this event. It does not prove that the account lacks every administrative membership or that no privileged activity occurred elsewhere.

If another supplied event establishes SYSTEM execution, privileged activity is supported for that event. A process name or “service” label alone is insufficient to make that change.

A pattern of probing many ports with no supplied authentication attempt supports scanning/reconnaissance. A documented failed login supports unsuccessful access activity. An HTTP 401 alone can be part of normal authentication, so corroborate an actual failed access attempt before categorizing a sequence on that basis.

## 3. Writing a justified category

Write the category, cite the supporting operation or privilege evidence, and explain why a plausible alternative is less supported. For example: “User-level activity: this process ran in the supplied non-elevated user context. The event supplies no privileged execution supporting root-level access.”

This comparison is a reasoning check. It does not require all possible categories to be mutually exclusive. An ATT&CK mapping may add a behavior description, while the local activity category continues to serve its own reporting purpose.

## Knowledge Check

1. Name the four syllabus categories and explain how Other is used.
2. Categorize the supplied non-elevated jlee event and explain why root-level is unsupported.
3. How would you distinguish a port sweep from a failed login, and why is HTTP 401 alone insufficient?

## Summary

Choose an activity category from the observed behavior and access context. Explain the evidence and a plausible alternative, and use local definitions for mixed activity or additional categories.

## Course Connections

Previous: [1.4.3 – Common False Positive Causes](../03-false-positive-causes/student-guide.md)

Next: [1.4.5 – SLA / Response Time Goals](../05-sla-response-times/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)
