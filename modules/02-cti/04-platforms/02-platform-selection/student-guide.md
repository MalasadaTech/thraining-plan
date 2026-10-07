# Module 2.4.2 – Selecting Platforms for CTI Work

**Target Audience:** CTI Analyst (primary); Threat Hunter and SOC Analyst (supporting context)  
**Proficiency Focus:**  
- CTI: 2.4.2 B / C / C ; 2.4.2.1 3c / 4c / 4d  
**Estimated Time:** 10–15 minutes

## Learning Objectives

1. Select a source for a defined CTI question and explain what the lookup can establish.
2. Capture an evidence record that preserves the object, source, time, result, and limitation.

**Mapped Proficiency Items:**
- K: 2.4.2 – Selecting platforms for CTI work
- T: 2.4.2.1 – Select a source and record a question-driven CTI lookup

## 1. Key Concepts

The introductory tool survey explained what the external tools are for. Here you choose a source for a specific intelligence question and carry its result into an evidence record.

Start with the requirement from 2.1 and an existing case value. Check what the internal TIP already holds, then use another source when it can answer a remaining question. Local handling restrictions determine whether a value can be submitted outside the organization; retrieving an existing public report and uploading an internal file are different actions.

| Question | Useful starting point | Record |
|---|---|---|
| What do we already know about this value? | Internal TIP | Linked reports, sightings, provenance, and time. |
| What does a known sample relate to, and what behavior was observed? | VirusTotal; ANY.RUN for available sandbox reports | Exact object/report, relationships or events, report time, and limitations. |
| What infrastructure associations were observed over time? | Silent Push; registration sources for registration questions | Record type, returned relationship, observation window, and source. |
| What did a recorded browser visit load or contact? | urlscan.io | Scan context, redirects, requests, destinations, and relevant time. |

### Official platform references

Use these pages to confirm platform capabilities and terminology. Local handling rules still determine whether a case value may be submitted to an external service.

- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching)
- [ANY.RUN — Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/)
- [Silent Push — DNS Data](https://help.silentpush.com/docs/dns-data)
- [urlscan.io — Quickstart](https://docs.urlscan.io/guides/quickstart)

A tool result answers a narrower question than “Is everything related malicious?” A sandbox record describes the observed execution; a recorded browser visit describes that visit; a missing result reflects the queried source's coverage.

### First pass through the platforms

For 2.4.3–2.4.6, retrieve a provided report or use an instructor-supplied static result. Identify the object, the report or observation time, one relevant field, and one limitation. Record:

`question | seed/object | source/report | query/observation time | result | meaning | next question`

Detailed interpretation returns with the method lessons. Work through VirusTotal and ANY.RUN evidence with file and behavioral analysis, Silent Push with DNS and infrastructure methods, and urlscan.io with web-infrastructure relationships. This keeps platform familiarity ahead of the exercise while putting interpretation beside the concepts it requires.

### Stop when the question is answered

Do not visit every platform by default. Continue when a specific uncertainty could change the assessment. Preserve a result even when it is inconclusive, and explain what the next source is expected to add.

## 2. Knowledge Check

1. How does a CTI lookup differ from simply checking every available tool?
2. Which source would you start with for historical domain-to-IP observations, and what time context would you retain?
3. Why does access to an external platform not automatically authorize uploading a case file?

## 3. Summary

Choose a source for a defined question, preserve provenance and time, and continue only when another lookup can improve the answer.

**Next:** [2.4.3 – VirusTotal Relations and Behavior](../03-virustotal/student-guide.md).
