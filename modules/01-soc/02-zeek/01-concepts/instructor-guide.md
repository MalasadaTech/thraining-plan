# Instructor Guide – Module 1.2.1 – Zeek Concepts

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.1.1 A / B / C  
- Hunter: 1.2.1.1 B / C / C  
- CTI: 1.2.1.1 A / B / B  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Network-sensor evidence describes traffic visible at an observation point. Zeek turns that traffic into structured records that analysts can search and connect. Understanding how those records are produced helps you choose the right log and recognize when additional evidence is needed.

## Learning Objectives

1. Explain Zeek’s purpose and the role of analyzers and scripts.
2. Distinguish network-sensor records from endpoint evidence.
3. Explain when PCAP can verify or expand a logged observation.

**Mapped Proficiency Items:**
- K: 1.2.1.1 – Zeek concepts

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required.

Use the proficiency levels above to adjust prompting and explanation depth. The module focuses on its mapped knowledge and tasks; the linked next lesson develops the next step.

## Suggested Timing

| Section | Minutes | Focus |
|---|---|---|
| Opening | 2 | Connect the lesson to its purpose. |
| Explanation and worked example | 8 | Read the supplied evidence and demonstrate the reasoning. |
| Knowledge check and feedback | 6 | Complete the interpretation or modification tasks. |
| Summary and transition | 2 | Consolidate the result and connect the next lesson. |
| **Total** | **18** | |

## Detailed Teaching Notes

### 1. How traffic becomes a log

Explain analyzer versus logging script without introducing a scripting course. Use conn, DNS, and files as examples of different record purposes.

**Key point to reinforce:** Analyzers interpret traffic; scripts use events to produce structured records. Different logs expose different observations.

### 2. Relating Zeek to endpoint evidence

Ask what makes two records plausibly related and what could break the association, such as address translation or time differences.

**Key point to reinforce:** Correlate sensor and endpoint evidence using supported identity, timing, and flow details. Account for visibility.

### 3. When packet capture helps

Compare an IP-and-port alert with a cleartext request. Then change only the visibility to encrypted traffic and ask how the possible answer changes.

**Key point to reinforce:** Retained PCAP can add headers or visible content. Missing, partial, or encrypted capture may leave the question unresolved.

## Knowledge Check — Answer Key

### 1. How do analyzers and scripts contribute to Zeek logs?

**Expected answer:** Analyzers interpret observed traffic and generate events; scripts use those events to create structured records and other outputs.

### 2. What can endpoint evidence add to a Zeek connection record?

**Expected answer:** It may identify the operating-system process associated with the network activity, subject to a supported correlation.

### 3. When would PCAP add information, and when might it not?

**Expected answer:** It may reveal retained headers or visible payload omitted from a log. Missing, incomplete, or encrypted captures may not answer the question.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Zeek supplies structured observations from network traffic. Choose a log according to the question, account for the sensor’s view, and use retained PCAP when it can add relevant evidence.

Previous: [1.1.6 – Image and Driver Load Activity](../../01-endpoint/06-image-driver-load/student-guide.md)

Next: [1.2.2 – Conn Engine](../02-conn-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — Log files](https://docs.zeek.org/en/master/reference/zeekscript/log-files.html)
- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html)
