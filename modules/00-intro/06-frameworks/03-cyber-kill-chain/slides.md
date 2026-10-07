# Module 0.6.3 – Cyber Kill Chain

- Describe the purpose and seven stages of the Cyber Kill Chain.
- Assign a stage to a simple observed event and explain the evidence.
- Distinguish observed progression from unestablished activity.

**Speaker notes:** Introduce the purpose and connect it to the shared course sequence. The objectives describe the understanding learners should demonstrate by the end.

---

## Why this matters

The Cyber Kill Chain provides a way to discuss progression through an intrusion. It helps analysts place an observed event in a larger sequence and consider where defensive action could interrupt that sequence. The available evidence may show only part of the activity.

**Speaker notes:** Ask learners where this topic could help them understand an investigation. Use their answers to introduce the example without requiring prior operational experience.

---

## The seven stages

Reconnaissance → Weaponization → Delivery → Exploitation → Installation → Command and Control → Actions on Objectives.

Use the stages to describe progression and opportunities to interrupt it.

**Speaker notes:** Read the stages in order with a brief explanation of each. Emphasize that unobserved stages remain unknown. Execution of a program does not automatically demonstrate vulnerability exploitation, and a file on disk does not by itself establish installation of a foothold.

---

## Placing an observed event

**Scenario status: Separate classroom example — not A12.**

Observed: an email containing established-malicious `shipping-notice.js` reaches a mailbox.

Supported stage: Delivery.

Evidence: the email delivery record.

Opening, exploitation, and installation remain unestablished.

**Speaker notes:** Keep the example separate from A12. If learners choose Weaponization, ask what evidence shows preparation. If they choose Exploitation or Installation, ask what happened on the endpoint and whether any such event was supplied.

---

## Explaining a stage assignment

State the stage and supporting event.

Identify what remains unknown.

ATT&CK: behavior. Diamond: event elements. Kill Chain: progression.

**Speaker notes:** Use the three framework purposes as a brief synthesis. Learners should explain their stage choice, not reconstruct an unseen attack. Discuss one plausible interruption point, such as preventing delivery, without turning this introduction into a control-design lesson.

---

## Knowledge check

1. Name the seven Cyber Kill Chain stages and explain what the model helps analysts describe.
2. An email record confirms delivery of an attachment established as malicious. Which stage is supported, and why?
3. Does that delivery record establish exploitation or installation? What would you say in the finding?

**Speaker notes:** Ask learners to explain the evidence or reasoning behind each answer. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for expected responses and feedback.

---

## Summary and next step

The Cyber Kill Chain describes intrusion progression in seven stages. Assign a stage from the observed event, explain the supporting evidence, and leave unobserved activity open for investigation.

Previous: [0.6.2 – Diamond Model](../02-diamond-model/student-guide.md)

Next: [0.7 – External tools](../../07-tool-survey/01-external-tools/student-guide.md)

**Speaker notes:** Revisit any uncertainty from the knowledge check, then connect the lesson to the next topic.

---

## References and further reading

- [Lockheed Martin — Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) — Original model and supporting resources.

**Speaker notes:** These linked resources support the lesson and provide a place to check definitions and service details.
