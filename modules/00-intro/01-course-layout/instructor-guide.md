# Instructor Guide – Module 0.1 – How this course is laid out

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (front door)  
**Proficiency Focus:**  
- SOC: 0.1 A / B / B  
- Hunter: 0.1 A / B / B  
- CTI: 0.1 A / B / B  
- DE: 0.1 A / B / B  
**Estimated Time:** 15 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

This course follows the work of SOC analysts, CTI analysts, threat hunters, and detection engineers. Understanding its structure will help you see why a topic appears where it does and how the later lessons build on what you have already learned. Everyone begins with the same introductory material so that the four roles share a common vocabulary.

Teach this as a shared introductory lesson using the supplied examples and discussion. Match the depth to the proficiency levels above. The focus is the mapped knowledge and task; operational procedures are developed in the later role tracks.

## Learning Objectives

1. Describe the course sequence and explain why the shared lessons come first.
2. Explain why detections precede alert investigation and identify where the SOC track ends.
3. Explain how an RFI connects the course example to the CTI track.

**Mapped Proficiency Items:**
- K: 0.1 – How this course is laid out

## Preparation

Read the [student guide](student-guide.md) and use [slides.md](slides.md) to support the explanation. Review the answer key before teaching so the discussion and feedback reinforce the same concepts. This lesson uses discussion and worked examples; no lab is required.

## Suggested Timing

| Section | Time | Teaching purpose |
|---|---|---|
| Opening and purpose | 2 min | Connect this lesson to the previous topic. |
| Explanation and worked examples | 7 min | Use the three teaching sections below. |
| Knowledge check and feedback | 4 min | Ask for reasoning as well as an answer. |
| Summary and transition | 2 min | Consolidate the lesson and introduce the next topic. |
| **Total** | **15 min** | |

## Detailed Teaching Notes

### 1. How the course progresses

Walk through the sequence as a learning path. Explain that the earlier tracks supply context for the later ones, even when the learner already works in one of those roles. The order describes this course; it does not establish an organization chart.

**Student-facing emphasis:** Everyone completes the introduction and shared topics first. The role tracks follow in order: SOC → CTI → Hunt → Detection Engineering.

### 2. Why detections come before alert work

Use the learner’s experience of receiving an alert to explain the ordering. Understanding what a rule looks for helps the learner interpret its output. Expand RFI when you first say it, then explain that the course will develop the request and answer in later lessons.

**Student-facing emphasis:** Detections help explain why an alert appeared. SOC reporting concludes at 1.5. An RFI connects the course example to CTI work.

### 3. Using the shared examples

Explain why the names are deferred to the next lesson: learners first need the route through the course. Present the companion story as a way to connect the products they will learn about. Local procedures remain matters to obtain from the actual organization.

**Student-facing emphasis:** A shared fictional setting connects the lessons. The companion story brings the incident together after the individual lessons.

## Knowledge Check — Answer Key

### 1. What do learners complete before the four role tracks, and why are those topics shared?

**Expected answer:** The introductory lessons, then frameworks, external tools, and environment / signal flow. All four roles use these concepts to interpret evidence and coordinate their work.

**Feedback and assessment:** Look for both the order and a reason the material applies across roles.

### 2. Why does the SOC track teach detections before alert investigation, and where does that track end?

**Expected answer:** Knowing what a detection is intended to identify helps explain the alert. The SOC track ends with reporting in module 1.5.

**Feedback and assessment:** Accept an explanation that connects a detection to the alert it produces, followed by the reporting endpoint.

### 3. How does an RFI connect the SOC and CTI parts of this course?

**Expected answer:** An RFI states a question that needs an intelligence answer. In the course sequence, a question arising from alert work introduces the CTI track.

**Feedback and assessment:** The learner should describe a request and the need for an answer, rather than treating RFI as another name for an incident report.

## Closing and Transition

The course begins with shared foundations and then follows SOC, CTI, Hunt, and Detection Engineering. Its ordering helps you understand the evidence and products that later work depends on. The fictional setting and companion story connect the lessons, while local procedures are introduced where they are needed.

Next: [0.2 – What a SOC is](../02-what-a-soc-is/student-guide.md)
