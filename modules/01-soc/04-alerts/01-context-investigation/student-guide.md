# Module 1.4.1 – Alert Context and Investigation

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.1.1 A / B / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- Hunter: 1.4.1.1 B / C / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- CTI: 1.4.1.1 A / A / B ; 1.4.1.2 1a / 1a / 2b ; 1.4.1.3 1a / 1a / 2b ; 1.4.1.4 1a / 1a / 2b ; 1.4.1.5 1a / 1a / 1a ; 1.4.1.6 1a / 1a / 1a  
**Estimated Time:** 30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Identify present and missing alert context, including an approved lookup of an available indicator.
2. Explain the alert configuration and trace its actual upstream detection path.
3. Select related endpoint logs and describe what they add or fail to add.
4. Select related PCAP for a network question and describe its contribution or availability limit.

**Mapped Proficiency Items:**
- K: 1.4.1.1 – Alert context and investigation
- T: 1.4.1.2 – Review an alert and identify which context is present and which is missing (include VirusTotal on a hash, IP, or domain you have)
- T: 1.4.1.3 – Review the alert configuration and explain what would fire
- T: 1.4.1.4 – Trace an alert to its upstream detection logic and name each hop
- T: 1.4.1.5 – Collect related endpoint logs and state what they add (or fail to add)
- T: 1.4.1.6 – Collect related PCAP and state what it adds versus the alert fields

## Why This Matters

An alert is the starting point for an investigation. Before deciding what it means, establish what evidence it contains, what logic produced it, and what related records can add. This makes the eventual finding traceable to observations rather than to the alert title alone.

## 1. Establishing context and detection lineage

For the course process alert, record the host, account, event time, alert time, rule name/version, and the matched process fields. Separate facts already present from questions still open. The example shows `wscript.exe` launching PowerShell with an encoded-command argument as `jlee`; the decoded behavior and authorization are not yet supplied.

Read the configuration and explain what would fire: the process-created event must satisfy the image, parent, and command-line predicates, together with the rule's trigger settings. Trace the actual upstream path. A SIEM-only example is endpoint event → ingested table → SIEM rule → alert. A network example could be Suricata signature → Suricata alert ingested into the SIEM → correlation rule → SIEM alert. Use rule IDs and source references to establish which path applies.

## 2. Adding relevant evidence

| Evidence source | How to use it | What to record |
|---|---|---|
| Related endpoint events | Select the host and relevant time, then correlate process identity, paths, account, and operation. | What each event adds and any unresolved gap. |
| VirusTotal lookup | Look up an available hash, IP, or domain through the approved workflow. | The exact indicator, report reference/time, relevant result, and interpretation limit. |
| Related PCAP | Request retained traffic for a relevant flow, time range, and sensor. | What becomes visible beyond the alert, or why the capture cannot answer the question. |

A file event for `invoice.vbs` may add a path and initiating process; its mere proximity in time does not establish causation. A lookup with no known detections or no report does not establish safety. Keep public submission handling consistent with module 0.7.

For a process-only alert, first determine whether a related network question and flow exist. Distinguish “not relevant to the current question,” “not collected or retained,” and “searched but no related packets found.” These are different outcomes. Encryption may leave application content unavailable even when a capture exists.

## 3. Working through a reviewable finding

For the supplied classroom process alert, a useful initial record could state:

- **Present:** host `WS-JLEE`, account `jlee`, the creation event, Script Host parent, and encoded-command argument.
- **Logic:** the SIEM rule selects that three-field pattern; the lineage is endpoint event → table → rule → alert.
- **Added endpoint evidence:** a supplied file event records `invoice.vbs` at a Temp path. Its relationship to the launch should be supported by the path and process context.
- **Lookup:** if a hash or IP becomes available, record the actual lookup result or that the lookup is still pending. No real service result is supplied by this example.
- **PCAP:** no related flow is supplied yet, so identify the network question before requesting traffic.
- **Still open:** decoded command behavior, authorization, and any related execution or communication.

For a separate network example, retained cleartext HTTP packets can add `/update.exe` when the alert contained only IP and port. Record that contribution and the packet/time reference. The result should show how the additional evidence changes understanding.

## Knowledge Check

1. For the process example, name what is present and two unresolved questions.
2. Explain the configuration and upstream path for the SIEM-only alert.
3. You have a related hash and a file event. What should collection and a VirusTotal lookup contribute?
4. A network alert has IP/port only. What would you request from PCAP, and how would you document an unavailable capture?

## Summary

An investigation record should explain the alert’s evidence, logic, and lineage, then show what related endpoint records, lookups, and packets contribute. Clear unresolved questions make the next decision easier to support.

## Course Connections

Previous: [1.3.4 – SIEM Rules](../../03-detection/04-siem-rules/student-guide.md)

Next: [1.4.2 – Alert Classification](../02-classification/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching)
- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html)
