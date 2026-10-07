# Module 2.4.3 – VirusTotal Relations and Behavior

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.3 B / C / C ; 2.4.3.1 3c / 4c / 4d  
- Hunter: 2.4.3 B / C / C ; 2.4.3.1 3c / 4c / 4d  
- SOC: 2.4.3 A / B / B ; 2.4.3.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## How to use this platform guide

**Orientation now (about 5 minutes):** retrieve an instructor-provided result, identify the retrieved file/report identity, report time, and one relationship or observed event, and state one limitation. The first pass is about finding and recording evidence.

**Application with [2.5.2](../../05-enrichment/02-file-similarity/student-guide.md):** return to the detailed concepts, worked example, and knowledge check below when studying file relationships and sandbox behavior. The lesson's total estimated time includes both passes; this is one lesson delivered in two parts. Complete its platform performance check during the application pass.

## Learning Objectives

By the end of this module, you will be able to:

1. Use VirusTotal relationship data to identify objects connected to a seed and select candidates for further enrichment.
2. Use VirusTotal behavior reports to extract sandbox-observed process, file, registry, and network activity while preserving the difference between an observed event and an analytic conclusion.

**Mapped Proficiency Items:**
- K: 2.4.3 – VirusTotal Relations and Behavior
- T: 2.4.3.1 – Use Relations and Behavior to pivot and extract events

## 1. Key Concepts

VirusTotal organizes information around **objects** such as files, URLs, domains, and IP addresses. It also records **relationships** between objects—for example, a file related to a URL, a domain related to URLs, or a file related to other files.

Reference: [VirusTotal – Relationships](https://docs.virustotal.com/reference/relationships)

The course uses the familiar **Relations** view and **Behavior** view. The important distinction is analytical:

- **Relations** answers: *what other objects are linked to this seed in VirusTotal?*
- **Behavior** answers: *what did one or more sandbox reports observe this file doing?*

Neither answer automatically means “confirmed adversary infrastructure” or “confirmed behavior in our environment.”

### Relations: linked objects, not automatic ownership

A relationship can expose useful candidates such as:

- contacted domains or IPs;
- URLs associated with a file;
- dropped or related files;
- other objects connected through VirusTotal's dataset.

VirusTotal's API documentation describes relationships as links or dependencies between objects.

A useful analyst statement is:

> VirusTotal relates the seed file to `198.51.100.77`; investigate whether that relationship is relevant to A12.

That is stronger than:

> `198.51.100.77` is adversary infrastructure because VirusTotal shows it.

The second statement skips the required contextual evaluation.

### Behavior: sandbox observations

VirusTotal can contain multiple behavior reports for a file from sandbox systems. Behavior data may include:

- processes;
- files opened, created, or written;
- registry activity;
- network activity;
- loaded modules;
- ATT&CK technique associations.

Reference: [VirusTotal – File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)

A behavior report describes what that sandbox observed under its particular environment and execution conditions. Malware may behave differently across sandboxes, operating systems, time periods, network conditions, or execution paths.

So:

> Sandbox report observed `sync-client.exe` contacting `198.51.100.77:8080`.

is evidence.

It is not the same as:

> Every execution of `sync-client.exe` will contact that address.

### Different sandboxes can produce different observations

If VirusTotal contains multiple behavior reports, compare them rather than assuming one report is complete.

A behavior absent from one sandbox report may be:
- genuinely absent;
- dependent on environment or timing;
- gated by anti-analysis logic;
- missed because execution ended early.

“Not observed” is narrower than “does not occur.”

### Separate classroom card — not A12

This training-only card is **not canonical A12**. A12 does not provide a recovered `update.exe` sample, a SHA256, or VirusTotal behavior. The supplied values below exist only to practice Relations/Behavior interpretation.

Seed: SHA256 for `sync-client.exe`

The classroom card shows:

**Relations**
- contacted IP: `198.51.100.77`

**Behavior**
- process: `sync-client.exe` started;
- file: write under a Temp path;
- network: connection to `198.51.100.77:8080`;
- no registry Run-key event shown.

Defensible outputs:

> **Relationship candidate:** VirusTotal links the file to `198.51.100.77`.

> **Sandbox observation:** the behavior report recorded a connection to `198.51.100.77:8080`.

> **Registry:** no Run-key event is shown on this card.

Do not add `login-prd.net` or an `Updater` Run key unless the card actually contains it.

### Detection labels are context, not the lesson output

Vendor detection counts and labels can be useful context, but they are not substitutes for Relations or Behavior evidence.

This lesson focuses on:
- linked objects;
- sandbox-observed events;
- evidence boundaries.

## 2. Knowledge Check

1. VirusTotal relates a file to an IP. What does that establish, and what still needs analysis?
2. A Behavior report does not show a registry persistence event. Can you conclude the file never uses registry persistence? Why or why not?
3. From the separate classroom card, write one valid Relations finding and one valid Behavior finding.

## 3. Summary

VirusTotal Relations provides linked objects that can become enrichment candidates. Behavior reports provide sandbox observations.

Treat both as evidence with provenance. A relationship is not automatic adversary ownership, and a sandbox event is not automatically universal behavior.


## Supporting References

- [VirusTotal – Relationships](https://docs.virustotal.com/reference/relationships)
- [VirusTotal – File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)

**Next:** [2.4.4 – ANY.RUN](../04-anyrun/student-guide.md).
