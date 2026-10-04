# Module 0.3 – Jobs in one sentence

- Summarize each role’s responsibility in one sentence.
- Identify IR and firewall / IA as supporting functions introduced for handoffs.

**Speaker notes:** Introduce the purpose and connect it to the shared course sequence. The objectives describe the understanding learners should demonstrate by the end.

---

## Why this matters

Security work often begins with an alert or a question, then involves people with different responsibilities. Knowing the purpose of each role helps you recognize who can carry the work forward and what result to expect. This lesson gives you a short description of each role used in the course.

**Speaker notes:** Ask learners where this topic could help them understand an investigation. Use their answers to introduce the example without requiring prior operational experience.

---

## The roles and their responsibilities

SOC investigates alerts; IR handles containment and recovery.

CTI develops answers; Hunt searches for additional activity.

DE maintains detections; the firewall / IA function handles authorized blocking changes.

**Speaker notes:** Give each responsibility enough context to explain its purpose. A detection engineer’s output must remain useful over time, which is why testing and maintenance matter. Blocking ownership is an example of a local assignment, not a universal meaning of the term IA.

---

## Recognizing the work being requested

An RFI asks CTI for an answer.

A blocking request and a detection need can arise from the same finding, but they require different work.

**Speaker notes:** Use the requested outcome to distinguish responsibilities. Learners often identify the tool first; guide them back to whether the request needs analysis, an operational control change, or a detection. Explain that a newly discovered related domain still requires evaluation.

---

## What the course develops

The four tracks develop SOC, CTI, Hunt, and DE work.

IR and firewall / IA are introduced to make the handoffs understandable.

**Speaker notes:** Set scope once here. A concise description is useful after learners understand the responsibility. It should be a summary of an explanation rather than a phrase they have to memorize without understanding.

---

## Knowledge check

1. Describe each of the six roles in one sentence.
2. Which two supporting functions are introduced for handoffs rather than developed as full tracks, and what does each contribute?
3. How does a detection engineer’s responsibility differ from a request to block a domain?

**Speaker notes:** Ask learners to explain the evidence or reasoning behind each answer. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for expected responses and feedback.

---

## Summary and next step

Identify a responsibility by the work requested and the result it should produce. The six roles introduced here support connected parts of security operations; the course develops four of them in depth and explains the other two as handoff destinations.

Previous: [0.2 – What a SOC is](../02-what-a-soc-is/student-guide.md)

Next: [0.4 – How work can move](../04-how-work-moves/student-guide.md)

**Speaker notes:** Revisit any uncertainty from the knowledge check, then connect the lesson to the next topic.

---

## References and further reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.

**Speaker notes:** These linked resources support the lesson and provide a place to check definitions and service details.
