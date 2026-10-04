# Module 0.7 – External tools

- Describe the questions VirusTotal, ANY.RUN, Silent Push, and urlscan.io can help answer.
- Choose a suitable service and input for a simple investigation question.
- Explain a relevant interpretation limit and distinguish a lookup from a new submission.

**Speaker notes:** Introduce the purpose and connect it to the shared course sequence. The objectives describe the understanding learners should demonstrate by the end.

---

## Why this matters

External analysis services can help answer questions about files, domains, IP addresses, and web pages. Choosing a useful service starts with the question you need to answer and the input you have. Their capabilities overlap, and results still need interpretation in the context of the investigation.

**Speaker notes:** Ask learners where this topic could help them understand an investigation. Use their answers to introduce the example without requiring prior operational experience.

---

## Matching the tool to the question

VirusTotal: existing knowledge and reputation.

ANY.RUN: observed file or URL behavior.

Silent Push: DNS and infrastructure relationships.

urlscan.io: browser requests, redirects, and page appearance.

**Speaker notes:** Ask learners to state the question before naming a product. Accept overlapping choices when justified. Correct the former oversimplifications: VirusTotal includes passive DNS, and ANY.RUN supports URLs as well as files. A hash lookup and a new execution are different workflows.

---

## Interpreting what comes back

Connect each result to the question.

Reputation is an assessment; execution and browser results reflect observed conditions.

Infrastructure relationships are leads to evaluate.

Keep the report reference and time.

**Speaker notes:** Work through the suspicious-link example in order: existing context, observed web behavior, then infrastructure questions. Ask what each result adds and what it cannot establish. Avoid presenting the four services as interchangeable or requiring all four for every case.

---

## Choosing a suitable lookup or submission

Distinguish an existing-report lookup from a new submission.

Check organizational approval and actual visibility settings.

Choose the workflow that fits the question and the sensitivity of the input.

**Speaker notes:** Use a fictional URL containing a token to explain why submission handling matters. Do not conduct live submissions of organizational material in this introductory lesson. Explain that “unlisted” and “private” have distinct meanings in urlscan.io; consult current documentation for operational use.

---

## Knowledge check

1. You need to see the redirects and resources loaded during a browser visit. Which service is a suitable starting point, and why?
2. You have only a file hash. Can you run a new file execution in a sandbox from that alone?
3. A domain has no detections and shares an IP address with a malicious domain. What can you conclude, and what should you check before submitting its URL?

**Speaker notes:** Ask learners to explain the evidence or reasoning behind each answer. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for expected responses and feedback.

---

## Summary and next step

Choose an external service by the question, input, and available capability. Interpret results as evidence with limits, preserve their context, and use an approved submission workflow when providing new material.

Previous: [0.6.3 – Cyber Kill Chain](../../06-frameworks/03-cyber-kill-chain/student-guide.md)

Next: [0.8 – Environment / signal flow](../../08-environment/01-orientation/student-guide.md)

**Speaker notes:** Revisit any uncertainty from the knowledge check, then connect the lesson to the next topic.

---

## References and further reading

- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching) — Existing reports, relationships, and passive DNS searches.
- [VirusTotal — Private scanning](https://docs.virustotal.com/docs/private-scanning) — Separate private-scanning workflow.
- [ANY.RUN — Features](https://any.run/features/) — Interactive analysis capabilities and supported inputs.
- [Silent Push — Passive DNS lookups](https://help.silentpush.com/docs/perform-passive-dns-scans-and-record-specific-lookups) — DNS history and record-specific investigation.
- [urlscan.io — FAQ](https://urlscan.io/docs/faq/) — Scan behavior and visibility options.

**Speaker notes:** These linked resources support the lesson and provide a place to check definitions and service details.
