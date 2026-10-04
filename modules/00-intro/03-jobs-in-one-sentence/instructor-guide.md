# Instructor Guide – Module 0.3 – Jobs in one sentence

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.3 A / B / B  
- Hunter: 0.3 A / B / B  
- CTI: 0.3 A / B / B  
- DE: 0.3 A / B / B  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Security work often begins with an alert or a question, then involves people with different responsibilities. Knowing the purpose of each role helps you recognize who can carry the work forward and what result to expect. This lesson gives you a short description of each role used in the course.

Teach this as a shared introductory lesson using the supplied examples and discussion. Match the depth to the proficiency levels above. The focus is the mapped knowledge and task; operational procedures are developed in the later role tracks.

## Learning Objectives

1. Summarize each role’s responsibility in one sentence.
2. Identify IR and firewall / IA as supporting functions introduced for handoffs.

**Mapped Proficiency Items:**
- K: 0.3 – Jobs in one sentence

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

### 1. The roles and their responsibilities

Give each responsibility enough context to explain its purpose. A detection engineer’s output must remain useful over time, which is why testing and maintenance matter. Blocking ownership is an example of a local assignment, not a universal meaning of the term IA.

**Student-facing emphasis:** SOC investigates alerts; IR handles containment and recovery. CTI develops answers; Hunt searches for additional activity. DE maintains detections; the firewall / IA function handles authorized blocking changes.

### 2. Recognizing the work being requested

Use the requested outcome to distinguish responsibilities. Learners often identify the tool first; guide them back to whether the request needs analysis, an operational control change, or a detection. Explain that a newly discovered related domain still requires evaluation.

**Student-facing emphasis:** An RFI asks CTI for an answer. A blocking request and a detection need can arise from the same finding, but they require different work.

### 3. What the course develops

Set scope once here. A concise description is useful after learners understand the responsibility. It should be a summary of an explanation rather than a phrase they have to memorize without understanding.

**Student-facing emphasis:** The four tracks develop SOC, CTI, Hunt, and DE work. IR and firewall / IA are introduced to make the handoffs understandable.

## Knowledge Check — Answer Key

### 1. Describe each of the six roles in one sentence.

**Expected answer:** SOC investigates alerts and starts appropriate handoffs. IR coordinates containment and recovery. CTI answers intelligence questions and adds context. Hunt searches for relevant activity that alerts may have missed. DE develops, tests, and maintains detections. Firewall / IA evaluates and implements authorized blocking changes.

**Feedback and assessment:** Look for investigation and an outcome, with flexibility in wording.

### 2. Which two supporting functions are introduced for handoffs rather than developed as full tracks, and what does each contribute?

**Expected answer:** IR contributes containment and recovery. The firewall / IA function evaluates and implements authorized blocking changes.

**Feedback and assessment:** Both function names and their purpose should be present.

### 3. How does a detection engineer’s responsibility differ from a request to block a domain?

**Expected answer:** The detection engineer develops, tests, and maintains logic that identifies relevant activity. Blocking restricts access through an operational control managed by the responsible local function.

**Feedback and assessment:** Assess the difference in outcome, without requiring rule syntax or firewall procedures.

## Closing and Transition

Identify a responsibility by the work requested and the result it should produce. The six roles introduced here support connected parts of security operations; the course develops four of them in depth and explains the other two as handoff destinations.

Previous: [0.2 – What a SOC is](../02-what-a-soc-is/student-guide.md)

Next: [0.4 – How work can move](../04-how-work-moves/student-guide.md)

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.
