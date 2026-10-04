# Instructor Guide – Module 0.7 – External tools

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
- Hunter: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- CTI: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- DE: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
**Estimated Time:** 20 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

External analysis services can help answer questions about files, domains, IP addresses, and web pages. Choosing a useful service starts with the question you need to answer and the input you have. Their capabilities overlap, and results still need interpretation in the context of the investigation.

Teach this as a shared introductory lesson using the supplied examples and discussion. Match the depth to the proficiency levels above. The focus is the mapped knowledge and task; operational procedures are developed in the later role tracks.

## Learning Objectives

1. Describe the questions VirusTotal, ANY.RUN, Silent Push, and urlscan.io can help answer.
2. Choose a suitable service and input for a simple investigation question.
3. Explain a relevant interpretation limit and distinguish a lookup from a new submission.

**Mapped Proficiency Items:**
- K: 0.7 – External tools (VirusTotal, AnyRun, Silent Push, URLScan)
- T: 0.7.1 – Select the appropriate external tool for a given enrichment or analysis need

## Preparation

Read the [student guide](student-guide.md) and use [slides.md](slides.md) to support the explanation. Review the answer key before teaching so the discussion and feedback reinforce the same concepts. This lesson uses discussion and worked examples; no lab is required.

## Suggested Timing

| Section | Time | Teaching purpose |
|---|---|---|
| Opening and purpose | 2 min | Connect this lesson to the previous topic. |
| Explanation and worked examples | 12 min | Use the three teaching sections below. |
| Knowledge check and feedback | 4 min | Ask for reasoning as well as an answer. |
| Summary and transition | 2 min | Consolidate the lesson and introduce the next topic. |
| **Total** | **20 min** | |

## Detailed Teaching Notes

### 1. Matching the tool to the question

Ask learners to state the question before naming a product. Accept overlapping choices when justified. Correct the former oversimplifications: VirusTotal includes passive DNS, and ANY.RUN supports URLs as well as files. A hash lookup and a new execution are different workflows.

**Student-facing emphasis:** VirusTotal: existing knowledge and reputation. ANY.RUN: observed file or URL behavior. Silent Push: DNS and infrastructure relationships. urlscan.io: browser requests, redirects, and page appearance.

### 2. Interpreting what comes back

Work through the suspicious-link example in order: existing context, observed web behavior, then infrastructure questions. Ask what each result adds and what it cannot establish. Avoid presenting the four services as interchangeable or requiring all four for every case.

**Student-facing emphasis:** Connect each result to the question. Reputation is an assessment; execution and browser results reflect observed conditions. Infrastructure relationships are leads to evaluate. Keep the report reference and time.

### 3. Choosing a suitable lookup or submission

Use a fictional URL containing a token to explain why submission handling matters. Do not conduct live submissions of organizational material in this introductory lesson. Explain that “unlisted” and “private” have distinct meanings in urlscan.io; consult current documentation for operational use.

**Student-facing emphasis:** Distinguish an existing-report lookup from a new submission. Check organizational approval and actual visibility settings. Choose the workflow that fits the question and the sensitivity of the input.

## Knowledge Check — Answer Key

### 1. You need to see the redirects and resources loaded during a browser visit. Which service is a suitable starting point, and why?

**Expected answer:** urlscan.io is a suitable starting point because its scans record browser requests, redirects, resource hosts, and page appearance.

**Feedback and assessment:** Accept another supported tool when the learner explains an appropriate workflow and its limitations.

### 2. You have only a file hash. Can you run a new file execution in a sandbox from that alone?

**Expected answer:** The hash may locate an existing report or an accessible sample, but it is not the file itself. A new execution needs the actual file or another supported input.

**Feedback and assessment:** Look for the distinction between finding prior analysis and generating a new run.

### 3. A domain has no detections and shares an IP address with a malicious domain. What can you conclude, and what should you check before submitting its URL?

**Expected answer:** Neither result alone establishes safety or maliciousness. Assess the relationship and other evidence. Before submission, check organizational authorization, sensitive URL content, and the workflow’s actual visibility.

**Feedback and assessment:** The answer should interpret the evidence cautiously and distinguish lookup from submission.

## Closing and Transition

Choose an external service by the question, input, and available capability. Interpret results as evidence with limits, preserve their context, and use an approved submission workflow when providing new material.

Previous: [0.6.3 – Cyber Kill Chain](../../06-frameworks/03-cyber-kill-chain/student-guide.md)

Next: [0.8 – Environment / signal flow](../../08-environment/01-orientation/student-guide.md)

## References and Further Reading

- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching) — Existing reports, relationships, and passive DNS searches.
- [VirusTotal — Private scanning](https://docs.virustotal.com/docs/private-scanning) — Separate private-scanning workflow.
- [ANY.RUN — Features](https://any.run/features/) — Interactive analysis capabilities and supported inputs.
- [Silent Push — Passive DNS lookups](https://help.silentpush.com/docs/perform-passive-dns-scans-and-record-specific-lookups) — DNS history and record-specific investigation.
- [urlscan.io — FAQ](https://urlscan.io/docs/faq/) — Scan behavior and visibility options.
