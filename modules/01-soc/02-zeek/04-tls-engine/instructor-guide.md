# Instructor Guide – Module 1.2.4 – TLS Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.4.1 A / B / C ; 1.2.4.2 2b / 3c / 4c ; 1.2.4.3 2b / 3c / 4c  
- Hunter: 1.2.4.1 B / C / C ; 1.2.4.2 3c / 4c / 4c ; 1.2.4.3 3c / 4c / 4c  
- CTI: 1.2.4.1 A / A / B ; 1.2.4.2 1a / 1a / 2b ; 1.2.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

TLS can conceal application content while leaving some handshake information visible. Reading that information carefully helps describe the observed session without treating a hostname, certificate, or fingerprint as a verdict.

## Learning Objectives

1. Interpret SNI, certificate information, optional fingerprints, version, cipher, and endpoints.
2. Describe TLS activity using the observed establishment state.
3. Create or modify a query for specific TLS activity.

**Mapped Proficiency Items:**
- K: 1.2.4.1 – TLS engine
- T: 1.2.4.2 – Analyze a Zeek TLS log and accurately describe what occurred
- T: 1.2.4.3 – Create a SIEM query to detect specific TLS activity

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

### 1. Reading TLS evidence

Distinguish client-indicated name, certificate identity, and fingerprint. Explain why unavailable fields can reflect encryption or collection.

**Key point to reinforce:** Read visible SNI, certificate information, optional fingerprints, version, cipher, and establishment state.

### 2. Working through the example

Compare the example with the established field removed. Ask learners to revise their sentence accordingly.

**Key point to reinforce:** Established=true supports the example’s session-state claim. Missing SNI leaves the requested name unavailable.

### 3. Creating a focused TLS query

Explain that a populated-field search has a visibility prerequisite. A blank field cannot be filled by choosing a more complex query.

**Key point to reinforce:** A hostname query only matches records with that visible, populated field. Preserve the visibility limit.

## Knowledge Check — Answer Key

### 1. How does SNI differ from the certificate subject?

**Expected answer:** SNI is the client-indicated server name when visible; the subject is identity information in the certificate.

### 2. What supports calling the example an established TLS session?

**Expected answer:** The supplied established=true field, together with the endpoint and handshake context. Version and cipher alone are insufficient for that statement.

### 3. Modify the query to search for visible SNI update.example and explain a blind spot.

**Expected answer:** Use `server_name =~ "update.example"`. Records without visible or populated SNI will not match, even if related communication occurred.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

TLS records describe the visible handshake and session state. State which names, certificate details, and fingerprints are available, and keep encrypted application behavior separate from those observations.

Previous: [1.2.3 – DNS Engine](../03-dns-engine/student-guide.md)

Next: [1.2.5 – HTTP Engine](../05-http-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — ssl.log](https://docs.zeek.org/en/current/reference/logs/ssl.html)
- [Zeek — x509.log](https://docs.zeek.org/en/current/reference/logs/x509.html)
