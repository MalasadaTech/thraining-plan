# Module 2.4.4 – ANY.RUN

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.4 B / C / C ; 2.4.4.1 3c / 4c / 4c  
- Hunter: 2.4.4 A / B / B ; 2.4.4.1 2b / 3c / 4c  
- SOC: 2.4.4 A / A / B ; 2.4.4.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## How to use this platform guide

**Orientation now (about 5 minutes):** retrieve an instructor-provided result, identify the report identity, sample hash, and one process/file/network event, and state one limitation. The first pass is about finding and recording evidence.

**Application with [2.5.2](../../05-enrichment/02-file-similarity/student-guide.md):** return to the detailed concepts, worked example, and knowledge check below when studying sandbox evidence and file context. The lesson's total estimated time includes both passes; this is one lesson delivered in two parts. Complete its platform performance check during the application pass.

## Learning Objectives

By the end of this module, you will be able to:

1. Search ANY.RUN threat-intelligence data using a known IOC or relevant event field.
2. Review the linked sandbox evidence and extract process, file, registry, network, or other observations that can support analysis without treating a tag or verdict as ground truth.

**Mapped Proficiency Items:**
- K: 2.4.4 – ANY.RUN
- T: 2.4.4.1 – Search and review ANY.RUN submissions for actionable intelligence

## 1. Key Concepts

ANY.RUN combines interactive sandbox analysis with threat-intelligence lookup across sandbox research sessions.

Current ANY.RUN documentation supports single-IOC searches for values such as:
- URL;
- MD5, SHA1, SHA256;
- IP address;
- domain.

Its lookup capability can also search event fields and combine indicators/events.

References:
- [ANY.RUN Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/)
- [ANY.RUN TI Lookup Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)

### Search from evidence you already have

The safest starting point is a seed already connected to your investigation.

Examples:
- SHA256 of `sync-client.exe`;
- `198.51.100.77`;
- update domain;
- a specific process command line from reporting.

This keeps enrichment tied to the requirement instead of browsing labels until an interesting family appears.

### Review the session, not just the tag

A malware-family tag, threat name, or malicious verdict is useful metadata, but the analysis should be grounded in the session evidence.

Useful evidence can include:
- process tree and command line;
- contacted domains, IPs, and URLs;
- dropped or modified files;
- registry modifications;
- mutexes;
- Suricata/signature events;
- other recorded sandbox events.

A tag such as `lumma_stealer` is a **classification claim produced by the service**. Preserve it as provenance:

> ANY.RUN labels the session as `lumma_stealer`.

That is different from independently concluding:

> This is definitively Lumma Stealer.

### Sandbox evidence is conditional

Like any sandbox, ANY.RUN observes behavior in a particular environment and execution.

Malware can change behavior because of:
- execution path;
- network availability;
- timing;
- user interaction;
- anti-analysis checks;
- operating-system or software differences.

So the correct evidence language is:

> The analyzed session observed...

—not—

> The malware always...

### What makes an extract useful?

The best extracts are concrete enough to feed the next analytic or defensive step.

Example:

> ANY.RUN session observed `powershell.exe` launching with an encoded command.

or:

> ANY.RUN session observed a request to `/client.bin` on `sync-gateway.example`.

Those can inform:
- TTP analysis;
- infrastructure enrichment;
- hunt leads;
- further sandbox comparison.

A generic verdict such as “malicious” contains less operational detail.

### Separate classroom card — not A12

This training-only sandbox card is **not canonical A12**. A12 does not provide a recovered `update.exe` hash or a sandbox execution. Use this card only to practice session-evidence interpretation.

Search seed: SHA256 for `sync-client.exe`

Suppose the card shows:
- process: `sync-client.exe`;
- child process: `powershell.exe`;
- contacted IP: `198.51.100.77`;
- dropped file: `stage.dat`;
- no check-in POST shown.

Valid output:

> ANY.RUN session observed `sync-client.exe` spawning PowerShell and contacting `198.51.100.77`.

If a check-in POST is absent from the card:

> No check-in POST is shown on this classroom result.

Do not reconstruct one from the broader course story.

## 2. Knowledge Check

1. Why is a malware-family tag weaker evidence than a concrete process or network event from the session?
2. Name two IOC types and two event types ANY.RUN can be used to search or investigate.
3. A classroom result has no check-in POST. What can you say, and what should you avoid claiming?

## 3. Summary

Search from a known IOC or relevant event field. Review the linked sandbox evidence. Preserve service labels as attributed metadata, and base your analysis on concrete events where possible.

Sandbox output describes what happened in that session—not every possible execution.


## Supporting References

- [ANY.RUN Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/)
- [ANY.RUN TI Lookup Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)

**Next:** [2.4.5 – Silent Push](../05-silent-push/student-guide.md).
