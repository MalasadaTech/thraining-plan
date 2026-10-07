# Module 1.4.1 – Alert Context and Investigation

- Identify present and missing alert context, including an approved lookup of an available indicator.
- Explain the alert configuration and trace its actual upstream detection path.
- Select related endpoint logs and describe what they add or fail to add.
- Select related PCAP for a network question and describe its contribution or availability limit.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

An alert is the starting point for an investigation. Before deciding what it means, establish what evidence it contains, what logic produced it, and what related records can add. This makes the eventual finding traceable to observations rather than to the alert title alone.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Establishing context and detection lineage

Record present and missing context, explain the rule, and trace the actual event-to-alert path.

**Speaker notes:** Draw only the supplied lineage. Ask learners to explain the rule’s actual predicates rather than paraphrasing its title.

---

## Adding relevant evidence

Collect related endpoint events, approved indicator lookups, and relevant retained packets. State what each contributes.

**Speaker notes:** Use the table to connect each collection action to a question. Explain that finding a record is not the same as establishing its relevance.

---

## Reference — Adding relevant evidence

| Evidence source | How to use it | What to record |
|---|---|---|
| Related endpoint events | Select the host and relevant time, then correlate process identity, paths, account, and operation. | What each event adds and any unresolved gap. |
| VirusTotal lookup | Look up an available hash, IP, or domain through the approved workflow. | The exact indicator, report reference/time, relevant result, and interpretation limit. |
| Related PCAP | Request retained traffic for a relevant flow, time range, and sensor. | What becomes visible beyond the alert, or why the capture cannot answer the question. |

**Speaker notes:** Use the table to connect each collection action to a question. Explain that finding a record is not the same as establishing its relevance. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through a reviewable finding

Preserve evidence references and unresolved questions. Distinguish unavailable capture from an irrelevant network question.

**Speaker notes:** Have learners produce the present/missing and contribution statements from the examples. Use a provided sanitized lookup result if available; otherwise label it pending rather than making a live submission.

---

## Knowledge check

1. For the process example, identify present/missing context and explain the SIEM rule configuration and upstream event-to-alert path.
2. You have a related hash and file event. What should collection and a VirusTotal lookup contribute, and what would each still leave unresolved?
3. A network alert has IP/port only. What would you request from PCAP, and how would you document an unavailable capture?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

An investigation record should explain the alert’s evidence, logic, and lineage, then show what related endpoint records, lookups, and packets contribute. Clear unresolved questions make the next decision easier to support.

Previous: [1.3.4 – SIEM Rules](../../03-detection/04-siem-rules/student-guide.md)

Next: [1.4.2 – Alert Classification](../02-classification/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching)
- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
