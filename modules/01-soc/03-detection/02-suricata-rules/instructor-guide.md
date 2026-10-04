# Instructor Guide – Module 1.3.2 – Suricata Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.2.1 A / B / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 1a / 2b / 3c  
- Hunter: 1.3.2.1 B / C / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 2b / 3c / 4c  
- CTI: 1.3.2.1 A / B / B ; 1.3.2.2 1a / 2b / 3c ; 1.3.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Suricata rules express conditions to inspect in network traffic. Reading the protocol, direction, and inspection buffer helps explain why a signature matched and whether its meaning agrees with the analyst’s description.

## Learning Objectives

1. Interpret rule action, header, options, and text/hex/regex matching.
2. Describe a rule’s traffic and match conditions.
3. Create or modify a basic rule and relate a hit to other network evidence.

**Mapped Proficiency Items:**
- K: 1.3.2.1 – Suricata rules
- T: 1.3.2.2 – Analyze an existing Suricata rule and describe what it detects
- T: 1.3.2.3 – Create or modify a basic Suricata rule

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required. Learners should produce the requested basic modification and explain a match and nonmatch. Operational deployment follows the later Detection Engineering track and local change procedures.

Use the proficiency levels above to adjust prompting and explanation depth. The module focuses on its mapped knowledge and tasks; the linked next lesson develops the next step.

## Suggested Timing

| Section | Minutes | Focus |
|---|---|---|
| Opening | 2 | Connect the lesson to its purpose. |
| Explanation and worked example | 17 | Read the supplied evidence and demonstrate the reasoning. |
| Knowledge check and feedback | 6 | Complete the interpretation or modification tasks. |
| Summary and transition | 2 | Consolidate the result and connect the next lesson. |
| **Total** | **27** | |

## Detailed Teaching Notes

### 1. Understanding header and options

Explain the variables from actual configuration or label their values unspecified. Distinguish text, hex, and regex as matching representations.

**Key point to reinforce:** Read action, header, variables, flow, and buffer-specific tests. Actual variable values determine network scope.

### 2. Reading a basic proposal

Read the rule by action, header, flow, method, then URI. Emphasize that bsize on the method and a substring on the URI have different effects.

**Key point to reinforce:** The example matches GET and a URI containing /update.exe. A longer URI can also match.

### 3. Modifying the matching scope

Use exact path, longer path, and query-string cases to evaluate the change. Production deployment and packet replay are outside this worked discussion.

**Key point to reinforce:** Adding URI bsize:11 requires the exact-length URI. Explain whether query strings should be included.

## Knowledge Check — Answer Key

### 1. What do the header and sticky buffer each control?

**Expected answer:** The header scopes protocol, addresses, ports, and direction. The sticky buffer selects the parsed content inspected by subsequent tests.

### 2. Does the example match /folder/update.exe? Explain.

**Expected answer:** Yes. The URI content test searches for the substring /update.exe; it is not anchored to the whole URI.

### 3. Modify the URI test for exactly /update.exe and name an excluded request.

**Expected answer:** Add bsize:11 after that content test. A longer URI such as /update.exe?id=1 is excluded.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

A clear Suricata proposal identifies the traffic scope and the exact buffer and pattern inspected. Explain what matches, what does not, and what related network evidence could add.

Previous: [1.3.1 – SIGMA Rules](../01-sigma-rules/student-guide.md)

Next: [1.3.3 – YARA Rules](../03-yara-rules/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Suricata — Rule format](https://docs.suricata.io/en/latest/rules/intro.html)
- [Suricata — HTTP keywords](https://docs.suricata.io/en/latest/rules/http-keywords.html)
