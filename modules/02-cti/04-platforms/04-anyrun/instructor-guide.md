# Instructor Guide – Module 2.4.4 – ANY.RUN

**Estimated Time:** 20–25 minutes

## Two-pass delivery

Spend about 5 minutes here on retrieval and evidence capture: the report identity, sample hash, and one process/file/network event. Use a supplied static result if a live account or permitted query is unavailable. Reserve the remaining stated lesson time and the knowledge check for 2.5.2, alongside sandbox evidence and file context. Do not mark the platform task complete after orientation alone.

Use the first two slides for orientation; use the remaining slides and worked example during the paired method lesson. Reuse the same result in both passes.

## Purpose

Teach learners to search ANY.RUN from known evidence and extract concrete sandbox observations rather than treating tags or verdicts as the conclusion.

## Current Capability Note

ANY.RUN TI Lookup supports IOC searches and event-field searches, including URLs, hashes, IPs, domains, processes, registry activity, and other sandbox-derived data.

References:
- [ANY.RUN TI Lookup](https://any.run/threat-intelligence-lookup/)
- [Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)

## Key Teaching Points

- Start with evidence connected to the investigation or supplied training scenario.
- Review process/network/file/registry events.
- Attribute service labels: “ANY.RUN labels...”
- Treat sandbox behavior as session-specific evidence.

## Practice-Card Boundary

The worked sandbox card used with this lesson is **separate classroom evidence, not A12**. Do not let a training hash, execution tree, or contacted IP become a fact of the recurring case.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Searches only malware-family tags. | Start from the case IOC or concrete event. |
| Treats tag as proven family identity. | Preserve the service as source of the claim. |
| Says absent event never happens. | Say not observed on this session/card. |
| Copies “malicious” as actionable output. | Ask what process, network, file, or registry evidence a defender can use. |

## Knowledge Check – Answer Key

1. A tag is a service classification; a concrete event records what the sandbox session observed.
2. IOC examples: hash, IP, domain, URL. Event examples: process, command line, registry modification, file activity, network event.
3. State that the POST is not shown in this result; do not claim the malware never uses it.

## References

- [ANY.RUN TI Lookup](https://any.run/threat-intelligence-lookup/)
- [ANY.RUN Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)
