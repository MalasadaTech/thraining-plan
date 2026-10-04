# Instructor Guide – Module 0.2 – What a SOC is

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.2 A / B / B  
- Hunter: 0.2 A / B / B  
- CTI: 0.2 A / B / B  
- DE: 0.2 A / B / B  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

A Security Operations Center, or **SOC**, is an organizational function that monitors for suspicious activity, investigates what it finds, and coordinates the start of a response. Understanding that purpose gives you a common starting point for the roles and handoffs in this course.

Teach this as a shared introductory lesson using the supplied examples and discussion. Match the depth to the proficiency levels above. The focus is the mapped knowledge and task; operational procedures are developed in the later role tracks.

## Learning Objectives

1. Explain the purpose of a SOC.
2. Explain why several roles contribute to security operations.
3. Identify DYA and PRD as the course setting and distinguish that setting from local procedures.

**Mapped Proficiency Items:**
- K: 0.2 – What a SOC is

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

### 1. What a SOC contributes

Explain the purpose before discussing tools or job titles. An alert is a starting point for assessment. Avoid describing every alert as a confirmed incident, because that would remove the reason for investigation.

**Student-facing emphasis:** The SOC monitors, investigates, and coordinates response. Analysts turn observations and alerts into findings that others can use.

### 2. How a team supports that purpose

If learners associate SOC with a room of monitors, broaden that picture to the function being performed. The specific reporting structure varies. This prepares learners to understand responsibilities without assuming every organization uses identical team names.

**Student-facing emphasis:** Security operations depends on several connected roles. Teams can work together across organizational or physical boundaries.

### 3. The setting used in this course

Introduce the full names once and use the abbreviations consistently. Explain the difference between knowing a story’s cast and having evidence within an investigation. This supports later lessons on attribution without trying to teach that entire topic here.

**Student-facing emphasis:** DYA is the fictional law firm. PRD is the fictional adversary name. Use the evidence supplied in each example and obtain real procedures from your site.

## Knowledge Check — Answer Key

### 1. What does a SOC contribute after a security tool produces an alert?

**Expected answer:** It reviews the evidence, assesses what the activity means, and coordinates appropriate handling or response.

**Feedback and assessment:** The answer should describe human assessment and routing, not only watching screens.

### 2. Why can several roles contribute to a SOC investigation even if they belong to different teams?

**Expected answer:** Their responsibilities depend on shared evidence and connected products, such as incident response actions, intelligence answers, and detection improvements.

**Feedback and assessment:** Accept a clear explanation of collaboration; the learner does not yet need a complete handoff sequence.

### 3. What are DYA and PRD, and where should you obtain the procedures used at your workplace?

**Expected answer:** DYA is Dixon, Yamada, & Associates, the fictional law firm; PRD is Pink River Dolphin, the fictional adversary name. Workplace procedures come from the actual organization.

**Feedback and assessment:** Check that learners distinguish the teaching setting from real local policy.

## Closing and Transition

A SOC monitors and investigates activity so the organization can respond appropriately. Several roles contribute to that purpose, and their arrangement varies by organization. DYA and PRD provide a consistent fictional setting for learning how the work connects.

Previous: [0.1 – How this course is laid out](../01-course-layout/student-guide.md)

Next: [0.3 – Jobs in one sentence](../03-jobs-in-one-sentence/student-guide.md)

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.
