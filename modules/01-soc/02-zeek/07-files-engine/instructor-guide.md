# Instructor Guide – Module 1.2.7 – Files Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.7.1 A / B / C ; 1.2.7.2 2b / 3c / 4c ; 1.2.7.3 2b / 3c / 4c  
- Hunter: 1.2.7.1 B / C / C ; 1.2.7.2 3c / 4c / 4c ; 1.2.7.3 3c / 4c / 4c  
- CTI: 1.2.7.1 A / A / B ; 1.2.7.2 1a / 1a / 2b ; 1.2.7.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Zeek file analysis connects observed network content to the flow that carried it. It can help explain a download or attachment, while the available fields also show whether hashes or extracted bytes exist for further examination.

## Learning Objectives

1. Interpret file names, MIME types, hashes, direction, and connection identifiers.
2. Describe observed file content without assuming endpoint creation.
3. Create or modify a query using the file-log schema actually available.

**Mapped Proficiency Items:**
- K: 1.2.7.1 – Files engine
- T: 1.2.7.2 – Analyze a Zeek files log and accurately describe what occurred
- T: 1.2.7.3 – Create a SIEM query to detect specific file transfer activity

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

### 1. Reading file-analysis records

Compare the two schema representations rather than teaching old fields as universal. Keep file identity, connection identity, hash, and extracted object distinct.

**Key point to reinforce:** Distinguish file FUID, connection UID, hash, and extracted object. Current and legacy direction fields differ.

### 2. Working through the example

Ask learners to determine sender from is_orig and explain the missing endpoint-path claim. Use the related HTTP record only for what it actually adds.

**Key point to reinforce:** With is_orig=false, the responder supplies the content. A network observation does not establish a host Temp path.

### 3. Creating a focused file-analysis query

Confirm that learners change both direction and the sender-address field. Do not require nonexistent legacy columns in a current feed.

**Key point to reinforce:** Query content type and supported sender/direction fields. Preserve completeness and extraction limitations.

## Knowledge Check — Answer Key

### 1. How do fuid and uid differ?

**Expected answer:** fuid identifies the analyzed file object; uid identifies the associated connection. Legacy conn_uids can hold connection identifiers.

### 2. Who supplied the content when is_orig=false in the example, and does it establish a Temp file on the host?

**Expected answer:** The responder, 203.0.113.88, supplied it. The network observation does not establish an endpoint path or file creation.

### 3. Modify the query for files supplied by the originator and identify the legacy equivalent.

**Expected answer:** Use is_orig=true and an id.orig_h predicate for the desired sender. In a legacy schema, search that sender in tx_hosts and use conn_uids for the pivot.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

File-analysis records describe observed network content and its connection context. Check the schema, direction, completeness, and available hashes or extracted bytes before choosing the next pivot.

Previous: [1.2.6 – SMTP Engine](../06-smtp-engine/student-guide.md)

Next: [1.2.8 – Weird Engine](../08-weird-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — files.log](https://docs.zeek.org/en/current/reference/logs/files.html)
