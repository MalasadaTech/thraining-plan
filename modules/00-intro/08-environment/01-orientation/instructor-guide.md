# Instructor Guide – Module 0.8 – Environment / signal flow

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.8 A / B / C ; 0.8.1 2b / 3c / 4c  
- Hunter: 0.8 B / C / C ; 0.8.1 2b / 3c / 4c  
- CTI: 0.8 A / B / B ; 0.8.1 1a / 2b / 3c  
- DE: 0.8 A / B / B ; 0.8.1 2b / 3c / 4c  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

An event becomes easier to interpret when you understand where it occurred and how activity normally moves through the organization. Environment orientation connects a host or account to its role, its access paths, and the evidence available along those paths.

Teach this as a shared introductory lesson using the supplied examples and discussion. Match the depth to the proficiency levels above. The focus is the mapped knowledge and task; operational procedures are developed in the later role tracks.

## Learning Objectives

1. Describe the seven environment areas used for orientation.
2. Identify which areas are relevant to a simple investigation question.
3. Distinguish the environment area relevant to a question from a related area, including traffic paths versus sensor coverage.

**Mapped Proficiency Items:**
- K: 0.8 – Environment / signal flow
- T: 0.8.1 – Identify which kind of fact applies and why it is not the adjacent kind

## Preparation

Read the [student guide](student-guide.md) and use [slides.md](slides.md) to support the explanation. Review the answer key before teaching so the discussion and feedback reinforce the same concepts. This lesson uses discussion and worked examples; no lab is required.

## Suggested Timing

| Section | Time | Teaching purpose |
|---|---|---|
| Opening and purpose | 2 min | Connect this lesson to the previous topic. |
| Explanation and worked examples | 10 min | Use the three teaching sections below. |
| Knowledge check and feedback | 4 min | Ask for reasoning as well as an answer. |
| Summary and transition | 2 min | Consolidate the lesson and introduce the next topic. |
| **Total** | **18 min** | |

## Detailed Teaching Notes

### 1. Building a useful environment picture

Walk through all seven areas without inventing local architecture. Explain crown jewels in terms of business impact, and PCAP as packet capture. Identity federation is a trust arrangement for authentication or identity; it does not automatically imply a direct network tunnel.

**Student-facing emphasis:** Orient around seven areas: egress; segments and data flow; email; edge controls; third-party access and federation; crown jewels; PCAP and sensors. For each, identify its role and the evidence it can provide.

### 2. Tracing an event through the environment

Ask learners to explain the difference between a network path and evidence about traffic on that path. Use conditional language because the course provides no confirmed DYA topology. A sensor’s existence does not guarantee the needed record exists.

**Student-facing emphasis:** Example: workstation → expected egress path → relevant observation point. Check three things: possible path, sensor coverage, and available records for the event time.

### 3. Recording useful gaps and next questions

Keep the task at orientation: identify the environment areas relevant to a question and explain why. A useful answer can name an owner or document to consult when the design is unknown. It need not invent a topology or propose a sensor deployment.

**Student-facing emphasis:** Record the known path, available evidence, and visibility gaps. Connect the affected system to its purpose and importance. Identify the owner or documentation needed for the next question.

## Knowledge Check — Answer Key

### 1. Which environment areas would help you investigate a workstation contacting an external domain?

**Expected answer:** The workstation’s segment and expected data flow, egress path, relevant firewall or chokepoint, and sensor or packet-capture coverage. Its business role can help establish priority.

**Feedback and assessment:** Accept a focused selection from the seven areas with an explanation of why each matters.

### 2. You know the expected egress path but need to determine whether packet-level evidence exists. Which environment area should you check, and how does it differ from egress?

**Expected answer:** Check PCAP and sensor coverage, including retention and access for the relevant time. Egress describes how traffic leaves; PCAP and sensors describe where and how it can be observed. Knowing the route does not establish that a capture exists.

**Feedback and assessment:** Look for a reasoned distinction between the path and the available observation, rather than treating the categories as interchangeable.

### 3. How do third-party access and crown jewels help orient an investigation?

**Expected answer:** Third-party access identifies authorized access methods, scope, and responsible owners. Crown jewels identify high-impact systems or information that influence priority.

**Feedback and assessment:** Accept federation as an identity trust arrangement; do not require or assume a direct network connection.

## Closing and Transition

Environment orientation helps you connect an event to expected paths, organizational importance, and available evidence. Use the seven areas to ask focused questions, verify the actual environment, and make visibility gaps clear.

Previous: [0.7 – External tools](../../07-tool-survey/01-external-tools/student-guide.md)

Next: [0.9 – Common Initial Access Paths](../../09-initial-access/student-guide.md).

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.
