# Module 0.6.2 – Diamond Model

- Describe the four Diamond Model vertices.
- Organize a simple event using the available evidence.
- Identify the weakest-supported vertex and explain the evidence gap.

**Speaker notes:** Introduce the purpose and connect it to the shared course sequence. The objectives describe the understanding learners should demonstrate by the end.

---

## Why this matters

The Diamond Model helps you organize what is known about an intrusion event and identify useful questions about what is missing. Its four vertices keep the activity, the systems involved, and the responsible party visible in one view.

**Speaker notes:** Ask learners where this topic could help them understand an investigation. Use their answers to introduce the example without requiring prior operational experience.

---

## The four vertices

Adversary: responsible party.

Capability: tools or techniques.

Infrastructure: enabling systems or services.

Victim: targeted or affected entity.

**Speaker notes:** Introduce each vertex as a question analysts can answer from evidence. Explain that a partially filled model is useful because it makes uncertainty visible. Avoid implying that every investigation can identify the adversary.

---

## Organizing a small example

Capability: observed PowerShell execution.

Infrastructure: contacted domain; role still under assessment.

Victim: observed workstation.

Adversary: unknown from these events.

**Speaker notes:** Trace each entry to its source. Ask what the network event proves: contact occurred. Then ask what remains uncertain: ownership, purpose, and relevance. This distinction prevents the diagram from making an inference appear established.

---

## Using gaps to guide a question

Identify the weakest-supported vertex.

Explain what evidence is missing.

Choose the next question according to the investigation’s purpose.

**Speaker notes:** Ask learners to distinguish the largest evidence gap from the highest-priority next step. Vendor research can supply evidence; a label without its basis cannot resolve attribution. Keep the discussion at the four-vertex level.

---

## Knowledge check

1. Name the four Diamond Model vertices and what each describes.
2. How would you organize the PowerShell and domain-contact example?
3. Which vertex is weakest in the example, and must it be resolved first?

**Speaker notes:** Ask learners to explain the evidence or reasoning behind each answer. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for expected responses and feedback.

---

## Summary and next step

The Diamond Model organizes an event around adversary, capability, infrastructure, and victim. Populate it from evidence, mark uncertainty, and use the gaps to develop questions that matter to the investigation.

Previous: [0.6.1 – MITRE ATT&CK](../01-attck/student-guide.md)

Next: [0.6.3 – Cyber Kill Chain](../03-cyber-kill-chain/student-guide.md)

**Speaker notes:** Revisit any uncertainty from the knowledge check, then connect the lesson to the next topic.

---

## References and further reading

- [Sergio Caltagirone — The Diamond Model](https://www.activeresponse.org/the-diamond-model/) — Author resource for the model introduced by Caltagirone, Pendergast, and Betz in 2013.

**Speaker notes:** These linked resources support the lesson and provide a place to check definitions and service details.
