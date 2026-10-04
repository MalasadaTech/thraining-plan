# Instructor Guide – Module 1.2.5 – HTTP Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.5.1 A / B / C ; 1.2.5.2 2b / 3c / 4c ; 1.2.5.3 2b / 3c / 4c  
- Hunter: 1.2.5.1 B / C / C ; 1.2.5.2 3c / 4c / 4c ; 1.2.5.3 3c / 4c / 4c  
- CTI: 1.2.5.1 A / B / B ; 1.2.5.2 1a / 2b / 3c ; 1.2.5.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

An HTTP record helps explain what a client requested and what response status the sensor observed. Separating request details, server response, and any transferred content makes the resulting account more precise.

## Learning Objectives

1. Interpret HTTP method, host, URI, User-Agent, response status, and endpoints.
2. Describe the request and response without inventing content or execution.
3. Create or modify a query for specific HTTP activity.

**Mapped Proficiency Items:**
- K: 1.2.5.1 – HTTP engine
- T: 1.2.5.2 – Analyze a Zeek HTTP log and accurately describe what occurred
- T: 1.2.5.3 – Create a SIEM query to detect specific HTTP activity

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required. For query tasks, ask learners to write or modify the shown query and explain its predicates. Confirm the local schema if demonstrating it in an approved teaching environment.

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

### 1. Reading HTTP fields

Explain why Host plus URI can still leave scheme or port uncertain. Emphasize that User-Agent is a claim made by the client.

**Key point to reinforce:** Read method, Host, URI, User-Agent, response status, endpoints, and transaction context.

### 2. Working through the example

Ask what evidence would establish file contents and what would establish execution. Preserve the distinction between the two.

**Key point to reinforce:** GET /update.exe receives status 200. That establishes neither the returned file’s identity nor its execution.

### 3. Creating a focused HTTP query

Compare exact path, path-plus-query, and a different path containing the same filename. Have learners explain their intended scope.

**Key point to reinforce:** Exact URI and path-plus-query matching return different results. Choose and explain the intended comparison.

## Knowledge Check — Answer Key

### 1. How do the Host header, destination IP, and URI differ?

**Expected answer:** Host identifies the requested host name as recorded in the header; the IP identifies the network destination; URI identifies the requested resource.

### 2. What does the example establish, and does it prove update.exe ran?

**Expected answer:** It establishes the observed GET request and 200 response. It does not establish the content’s identity, saving to disk, or execution.

### 3. Would uri == "/update.exe" match /update.exe?id=1? How could you broaden it?

**Expected answer:** No. A scoped alternative such as `uri == "/update.exe" or uri startswith "/update.exe?"` includes the exact path with a query string without matching every occurrence of the name.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

An HTTP finding connects the request, response status, and endpoints. Preserve missing headers and distinguish a requested path from transferred content or endpoint execution.

Previous: [1.2.4 – TLS Engine](../04-tls-engine/student-guide.md)

Next: [1.2.6 – SMTP Engine](../06-smtp-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
