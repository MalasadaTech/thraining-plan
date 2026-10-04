# Instructor Guide – Module 1.2.8 – Weird Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.8.1 A / B / C ; 1.2.8.2 2b / 3c / 4c ; 1.2.8.3 2b / 3c / 4c  
- Hunter: 1.2.8.1 B / C / C ; 1.2.8.2 3c / 4c / 4c ; 1.2.8.3 3c / 4c / 4c  
- CTI: 1.2.8.1 A / A / A ; 1.2.8.2 1a / 1a / 1a ; 1.2.8.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

A weird record reports an unexpected condition encountered by Zeek. It is useful because it points to traffic or visibility worth examining, but its meaning depends on the named condition and the surrounding evidence.

## Learning Objectives

1. Interpret a weird type, notice flag, endpoints, and available UID.
2. Describe the reported condition from the sensor’s viewpoint.
3. Create or modify a query for a specific weird condition.

**Mapped Proficiency Items:**
- K: 1.2.8.1 – Weird engine
- T: 1.2.8.2 – Analyze a Zeek weird log and accurately describe what occurred
- T: 1.2.8.3 – Create a SIEM query to detect specific weird activity

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required. For query tasks, ask learners to write or modify the shown query and explain its predicates. Confirm the local schema if demonstrating it in an approved teaching environment.

Use the proficiency levels above to adjust prompting and explanation depth. The module focuses on its mapped knowledge and tasks; the linked next lesson develops the next step.

## Suggested Timing

| Section | Minutes | Focus |
|---|---|---|
| Opening | 2 | Connect the lesson to its purpose. |
| Explanation and worked example | 12 | Read the supplied evidence and demonstrate the reasoning. |
| Knowledge check and feedback | 6 | Complete the interpretation or modification tasks. |
| Summary and transition | 2 | Consolidate the result and connect the next lesson. |
| **Total** | **22** | |

## Detailed Teaching Notes

### 1. Reading an unexpected condition

Distinguish the weird type from its notice flag and from an incident decision. A condition can warrant a ticket under local procedure without proving compromise.

**Key point to reinforce:** Read the weird name, available endpoints/UID, and notice flag. The name describes an analysis condition.

### 2. Working through the example

Emphasize “observed” when discussing handshake progress. Ask what packet loss or midstream capture would change.

**Key point to reinforce:** Zeek reports data before observed establishment. That does not prove the endpoints skipped a handshake.

### 3. Creating a focused weird query

Have learners explain the broader scope and the correlation limits of a missing UID.

**Key point to reinforce:** Select the named condition and use available connection context to investigate its cause.

## Knowledge Check — Answer Key

### 1. What does a weird record establish?

**Expected answer:** Zeek encountered the named unexpected condition. Its cause and security significance need context.

### 2. Describe data_before_established without overstating what happened at the endpoints.

**Expected answer:** Zeek reported data before it had observed connection establishment; partial visibility may be relevant.

### 3. How would you broaden the query to that condition across all destinations, and what would you use to investigate matches?

**Expected answer:** Remove the destination filter, retain the name filter, and use available UID, endpoints, time, and related records or PCAP.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

A weird record supplies a named condition and any available connection context. Use it to ask a focused follow-up question and separate the sensor’s observation from an explanation of its cause.

Previous: [1.2.7 – Files Engine](../07-files-engine/student-guide.md)

Next: [1.3.1 – SIGMA Rules](../../03-detection/01-sigma-rules/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — weird.log and notice.log](https://docs.zeek.org/en/current/reference/logs/weird-and-notice.html)
