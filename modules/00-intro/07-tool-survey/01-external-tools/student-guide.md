# Module 0.7 – External tools

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
- Hunter: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- CTI: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- DE: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
**Estimated Time:** 20 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Describe the questions VirusTotal, ANY.RUN, Silent Push, and urlscan.io can help answer.
2. Choose a suitable service and input for a simple investigation question.
3. Explain a relevant interpretation limit and distinguish a lookup from a new submission.

**Mapped Proficiency Items:**
- K: 0.7 – External tools (VirusTotal, AnyRun, Silent Push, URLScan)
- T: 0.7.1 – Select the appropriate external tool for a given enrichment or analysis need

## Why This Matters

External analysis services can help answer questions about files, domains, IP addresses, and web pages. Choosing a useful service starts with the question you need to answer and the input you have. Their capabilities overlap, and results still need interpretation in the context of the investigation.

## 1. Matching the tool to the question

| Service | Useful starting question | Typical contribution |
|---|---|---|
| VirusTotal | What is already known about this file or indicator? | Reputation results, existing analyses, relationships, and passive DNS information where available. |
| ANY.RUN | What does this file or URL do in an interactive analysis environment? | Observed process, file, and network activity from an execution or browsing session. |
| Silent Push | What DNS history and infrastructure relationships can help investigate this domain or IP address? | DNS records, historical observations, and infrastructure pivots. |
| urlscan.io | What does this web page load or redirect to in a browser visit? | Requests, redirects, contacted hosts, and a screenshot from the scan. |

Use the input and available workflow to refine the choice. A file hash can locate an existing report, but a new sandbox execution requires an actual file or another supported input such as a URL. A URL analysis and a DNS-history lookup answer different questions even when both involve the same domain. Access to particular results or features can depend on the service and account.

## 2. Interpreting what comes back

Suppose a suspicious email links to a website. A reputation lookup can supply existing context. A browser scan may show that the page redirects to another host, while DNS history may reveal earlier infrastructure. Each result adds evidence about a different part of the question.

A detection count is a set of vendor assessments, not a final verdict. No detections may reflect limited knowledge rather than safety. A sandbox run records behavior under the conditions of that run; timing, interaction, or evasion may affect what appears. DNS relationships can reveal leads, but shared hosting does not establish common ownership or a common adversary. A browser scan captures a particular visit, and the page may behave differently for another user or at another time.

In your finding, state what the service observed and how it contributes to your question. Preserve the report reference and relevant time so another analyst can assess the result.

## 3. Choosing a suitable lookup or submission

Searching for an existing report and submitting new material are different actions. Before uploading a file or submitting a URL, follow the organization's approved process and check the workflow's visibility settings. Files can contain sensitive information, and URLs can include credentials, tokens, or internal names.

Visibility differs by service and mode. VirusTotal offers a separate private-scanning workflow; standard submissions should not be assumed private. urlscan.io distinguishes public, unlisted, and private scans, and unlisted scans remain accessible to certain vetted users. Confirm the current service documentation and your approved configuration when handling organizational material.

The appropriate choice combines the analytical question, the available input, and permission to use the service in that way.

## Knowledge Check

1. You need to see the redirects and resources loaded during a browser visit. Which service is a suitable starting point, and why?
2. You have only a file hash. Can you run a new file execution in a sandbox from that alone?
3. A domain has no detections and shares an IP address with a malicious domain. What can you conclude, and what should you check before submitting its URL?

## Summary

Choose an external service by the question, input, and available capability. Interpret results as evidence with limits, preserve their context, and use an approved submission workflow when providing new material.

## Course Connections

Previous: [0.6.3 – Cyber Kill Chain](../../06-frameworks/03-cyber-kill-chain/student-guide.md)

Next: [0.8 – Environment / signal flow](../../08-environment/01-orientation/student-guide.md)

## References and Further Reading

- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching) — Existing reports, relationships, and passive DNS searches.
- [VirusTotal — Private scanning](https://docs.virustotal.com/docs/private-scanning) — Separate private-scanning workflow.
- [ANY.RUN — Features](https://any.run/features/) — Interactive analysis capabilities and supported inputs.
- [Silent Push — Passive DNS lookups](https://help.silentpush.com/docs/perform-passive-dns-scans-and-record-specific-lookups) — DNS history and record-specific investigation.
- [urlscan.io — FAQ](https://urlscan.io/docs/faq/) — Scan behavior and visibility options.
