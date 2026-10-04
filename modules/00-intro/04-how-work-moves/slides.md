# Module 0.4 – How work can move

- Describe one possible workflow after an alert is triaged.
- Explain how intelligence findings can support blocking, hunting, and detection work.
- Given a step in the workflow, identify the receiving role and the product it owns.

**Speaker notes:** Introduce the purpose and connect it to the shared course sequence. The objectives describe the understanding learners should demonstrate by the end.

---

## Why this matters

An investigation can create several kinds of follow-on work. Some work addresses the incident already in progress, while other work improves understanding or future detection. Following one possible workflow helps you identify who receives a request and what they are expected to produce.

**Speaker notes:** Ask learners where this topic could help them understand an investigation. Use their answers to introduce the example without requiring prior operational experience.

---

## From an alert to response and a question

Triage establishes what attention the alert requires.

In this example, IR receives the incident, leadership is notified, and CTI receives an RFI.

**Speaker notes:** Walk learners from evidence to the reason for each handoff. The example is an escalated case; it does not imply every alert requires IR or leadership notification. Emphasize that responding to harm and answering an intelligence question can happen at the same time.

---

## How the intelligence work branches

CTI develops an answer and supporting context.

Findings can support blocking review, a hunt, and detection work.

The same intelligence package can serve Hunt and DE.

**Speaker notes:** Explain the branches by the outcome expected. A domain can appear in more than one product. The reason for a blocking handoff is an evaluated control need, not merely discovering another name. Keep the same-package relationship between Hunt and DE explicit.

---

## Naming the next handoff

Name the recipient, the requested outcome, and the product they own.

Hunt returns findings and gaps. DE assesses coverage and develops or tunes detections.

**Speaker notes:** Ask learners to explain what the recipient still has to do. Receiving a package does not mean the hunt or rule is already complete. Tool names illustrate possible downstream implementations and are not requirements to author anything in this lesson.

---

## Knowledge check

1. In the escalated course example, what can the analyst do after triage while CTI works on an RFI?
2. CTI has evidence supporting consideration of a domain block. Who receives that work, and what product does that function own?
3. The same intelligence package goes to Hunt and DE. What result should each produce?

**Speaker notes:** Ask learners to explain the evidence or reasoning behind each answer. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for expected responses and feedback.

---

## Summary and next step

A single alert can lead to response, notification, intelligence analysis, hunting, and detection work. Identify each handoff by its purpose and the product the receiving role owns. The example explains how the responsibilities connect while leaving local routing and approval procedures to the organization.

Previous: [0.3 – Jobs in one sentence](../03-jobs-in-one-sentence/student-guide.md)

Next: [0.5 – Where the jobs lightly overlap](../05-where-jobs-overlap/student-guide.md)

**Speaker notes:** Revisit any uncertainty from the knowledge check, then connect the lesson to the next topic.

---

## References and further reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.

**Speaker notes:** These linked resources support the lesson and provide a place to check definitions and service details.
