# Instructor Guide – Module 1.2.6 – SMTP Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.6.1 A / B / C ; 1.2.6.2 2b / 3c / 4c ; 1.2.6.3 2b / 3c / 4c  
- Hunter: 1.2.6.1 B / C / C ; 1.2.6.2 3c / 4c / 4c ; 1.2.6.3 3c / 4c / 4c  
- CTI: 1.2.6.1 A / A / B ; 1.2.6.2 1a / 1a / 2b ; 1.2.6.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

SMTP records describe mail transactions visible to a network sensor. They help identify envelope addresses and selected headers while leaving mailbox delivery, user action, and attachment behavior to other evidence.

## Learning Objectives

1. Interpret SMTP envelope addresses, subject, Message-ID, and endpoints.
2. Describe a transaction without assuming delivery or user action.
3. Create or modify a query for specific SMTP activity.

**Mapped Proficiency Items:**
- K: 1.2.6.1 – SMTP engine
- T: 1.2.6.2 – Analyze a Zeek SMTP log and accurately describe what occurred
- T: 1.2.6.3 – Create a SIEM query to detect specific SMTP activity

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

### 1. Reading a mail transaction

Use two distinct sender identities to illustrate envelope versus header. Explain that neither alone proves authenticity.

**Key point to reinforce:** Envelope sender and recipients differ from message headers. Message-ID supplies context rather than a file hash.

### 2. Working through the example

Ask what would support “delivered” or “opened.” Learners should name additional evidence, not assume it from the subject.

**Key point to reinforce:** The observed transaction contains the supplied addresses and subject. Delivery and user action need additional evidence.

### 3. Creating a focused SMTP query

Discuss why array and string recipient searches differ. Keep the worked query on verified scalar fields.

**Key point to reinforce:** Search the chosen sender and subject; confirm recipient data types before writing a membership test.

## Knowledge Check — Answer Key

### 1. How does mailfrom differ from a displayed From header?

**Expected answer:** mailfrom is the SMTP envelope sender; the displayed header is a separate message field and can differ.

### 2. Describe the example without claiming mailbox delivery.

**Expected answer:** Zeek observed the transaction with the specified envelope addresses, subject, and Message-ID. Successful delivery and user action remain unestablished.

### 3. Modify the query for the same sender regardless of subject.

**Expected answer:** Remove the subject predicate and keep the sender filter; retain subject and recipient output to assess the broader results.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

SMTP evidence describes the observed mail transaction and selected headers. Use it to develop a precise lead while keeping delivery, user action, and attachment behavior tied to their own evidence.

Previous: [1.2.5 – HTTP Engine](../05-http-engine/student-guide.md)

Next: [1.2.7 – Files Engine](../07-files-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — smtp.log](https://docs.zeek.org/en/current/reference/logs/smtp.html)
