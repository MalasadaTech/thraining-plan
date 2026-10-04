# Instructor Guide – Module 1.2.2 – Conn Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.2.1 A / B / C ; 1.2.2.2 2b / 3c / 4c ; 1.2.2.3 2b / 3c / 4c  
- Hunter: 1.2.2.1 B / C / C ; 1.2.2.2 3c / 4c / 4c ; 1.2.2.3 3c / 4c / 4c  
- CTI: 1.2.2.1 A / A / B ; 1.2.2.2 1a / 1a / 2b ; 1.2.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

A connection record gives you a network-level starting point: the endpoints, transport, and progress Zeek observed. That description helps you select the related protocol records without assigning a purpose to the traffic too early.

## Learning Objectives

1. Interpret connection endpoints, state, history, and identifiers.
2. Describe a connection using the supplied evidence.
3. Create or modify a query for specific connection activity.

**Mapped Proficiency Items:**
- K: 1.2.2.1 – Conn engine
- T: 1.2.2.2 – Analyze a Zeek conn log and accurately describe what occurred
- T: 1.2.2.3 – Create a SIEM query to detect specific connection activity

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

### 1. Reading connection fields

Read endpoint pairs together and use the case of history letters to distinguish direction. Keep state explanations grounded in the TCP example.

**Key point to reinforce:** Read originator, responder, transport, state, history, and UID. Originator is a connection role, not a synonym for internal.

### 2. Working through the example

Have learners cite proto before calling it TCP. Ask what evidence would be needed to name an application or process.

**Key point to reinforce:** The example records TCP to 203.0.113.88:443 with normal establishment and termination. CTrain1 is the connection pivot.

### 3. Creating a focused connection query

Use SF and S0 to show that changing a predicate changes the question. Explain sensor visibility as a possible limit.

**Key point to reinforce:** Select destination, transport, and state. S0 means no response observed; it does not explain why.

## Knowledge Check — Answer Key

### 1. How do originator and responder differ from internal and external?

**Expected answer:** They describe the connection roles observed by Zeek, not ownership or network location.

### 2. Describe the supplied record and name the pivot identifier.

**Expected answer:** TCP from 192.0.2.10:51000 to 203.0.113.88:443 with normal establishment and termination; use uid CTrain1 for related Zeek records.

### 3. Modify the query for unanswered attempts and explain the limit.

**Expected answer:** Change conn_state to S0. This means no reply was observed, which does not alone prove blocking or that the server was unavailable.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

A connection finding describes the endpoints, transport, and observed progress. Use the connection identifier to seek related records and keep explanations of purpose or failure tied to additional evidence.

Previous: [1.2.1 – Zeek Concepts](../01-concepts/student-guide.md)

Next: [1.2.3 – DNS Engine](../03-dns-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html)
