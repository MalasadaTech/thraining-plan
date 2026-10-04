# Instructor Guide – Module 1.2.3 – DNS Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.3.1 A / B / C ; 1.2.3.2 2b / 3c / 4c ; 1.2.3.3 2b / 3c / 4c  
- Hunter: 1.2.3.1 B / C / C ; 1.2.3.2 3c / 4c / 4c ; 1.2.3.3 3c / 4c / 4c  
- CTI: 1.2.3.1 A / B / B ; 1.2.3.2 1a / 2b / 3c ; 1.2.3.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

DNS evidence connects a question about a name to the response observed on the network. Distinguishing the resolver from the returned address helps prevent a common error when moving from a lookup to a connection investigation.

## Learning Objectives

1. Interpret DNS question, response, record type, and endpoints.
2. Describe a DNS observation and distinguish it from later communication.
3. Create or modify a query for specific DNS activity.

**Mapped Proficiency Items:**
- K: 1.2.3.1 – DNS engine
- T: 1.2.3.2 – Analyze a Zeek DNS log and accurately describe what occurred
- T: 1.2.3.3 – Create a SIEM query to detect specific DNS activity

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

### 1. Reading a DNS transaction

Use a resolver address different from the returned address. Ask learners to describe what each address does.

**Key point to reinforce:** Separate querying endpoint, resolver, requested name/type, and answer. Review the response code when interpreting missing answers.

### 2. Working through the example

Point out that the query type asks a question while the answer and response code describe the observed reply.

**Key point to reinforce:** The client asks 192.0.2.53 for update.example and receives 203.0.113.88. A later connection needs separate evidence.

### 3. Creating a focused DNS query

Have learners explain why adding AAAA broadens record types without broadening the requested domain.

**Key point to reinforce:** Query the name and record type. Adding AAAA broadens the question to IPv6 records for the same name.

## Knowledge Check — Answer Key

### 1. Where do you find the DNS server and the returned address?

**Expected answer:** The contacted DNS server is id.resp_h; returned addresses, when present, are in answers.

### 2. Describe the example and explain whether it proves a connection to the answer.

**Expected answer:** The client queried the resolver for update.example’s A record and received 203.0.113.88. It does not establish a subsequent connection.

### 3. Modify the query for both IPv4 and IPv6 questions for the same name.

**Expected answer:** Use `qtype_name in ("A", "AAAA")` while retaining the query-name predicate.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

A DNS description identifies the observed client, resolver, question, type, and response. It supplies a lead for subsequent activity rather than proving that the client contacted the returned address.

Previous: [1.2.2 – Conn Engine](../02-conn-engine/student-guide.md)

Next: [1.2.4 – TLS Engine](../04-tls-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — dns.log](https://docs.zeek.org/en/current/reference/logs/dns.html)
