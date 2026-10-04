# Instructor Guide – Module 0.6.3 – Cyber Kill Chain

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.3.1 A / B / C ; 0.6.3.2 2b / 3c / 4c  
- Hunter: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- CTI: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- DE: 0.6.3.1 A / B / B ; 0.6.3.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

The Cyber Kill Chain provides a way to discuss progression through an intrusion. It helps analysts place an observed event in a larger sequence and consider where defensive action could interrupt that sequence. The available evidence may show only part of the activity.

Teach this as a shared introductory lesson using the supplied examples and discussion. Match the depth to the proficiency levels above. The focus is the mapped knowledge and task; operational procedures are developed in the later role tracks.

## Learning Objectives

1. Describe the purpose and seven stages of the Cyber Kill Chain.
2. Assign a stage to a simple observed event and explain the evidence.
3. Distinguish observed progression from unestablished activity.

**Mapped Proficiency Items:**
- K: 0.6.3.1 – Cyber Kill Chain
- T: 0.6.3.2 – Identify the Kill Chain stage of observed activity

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

### 1. The seven stages

Read the stages in order with a brief explanation of each. Emphasize that unobserved stages remain unknown. Execution of a program does not automatically demonstrate vulnerability exploitation, and a file on disk does not by itself establish installation of a foothold.

**Student-facing emphasis:** Reconnaissance → Weaponization → Delivery → Exploitation → Installation → Command and Control → Actions on Objectives. Use the stages to describe progression and opportunities to interrupt it.

### 2. Placing an observed event

Keep the example anchored to the delivery record. If learners choose Weaponization, ask what evidence shows preparation. If they choose Exploitation or Installation, ask what happened on the endpoint and whether any such event was supplied.

**Student-facing emphasis:** Observed: email with an established malicious attachment reaches a mailbox. Supported stage: Delivery. Evidence: the email delivery record. Opening, exploitation, and installation remain unestablished.

### 3. Explaining a stage assignment

Use the three framework purposes as a brief synthesis. Learners should explain their stage choice, not reconstruct an unseen attack. Discuss one plausible interruption point, such as preventing delivery, without turning this introduction into a control-design lesson.

**Student-facing emphasis:** State the stage and supporting event. Identify what remains unknown. ATT&CK: behavior. Diamond: event elements. Kill Chain: progression.

## Knowledge Check — Answer Key

### 1. Name the seven Cyber Kill Chain stages and explain what the model helps analysts describe.

**Expected answer:** The stages are Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, and Actions on Objectives. They describe progression through an intrusion and opportunities to interrupt it.

**Feedback and assessment:** Accept a plain-language explanation that acknowledges evidence may cover only part of the sequence.

### 2. An email record confirms delivery of an attachment established as malicious. Which stage is supported, and why?

**Expected answer:** Delivery, because the record shows the malicious material reaching the mailbox.

**Feedback and assessment:** Require the event-based reason, not just the stage name.

### 3. Does that delivery record establish exploitation or installation? What would you say in the finding?

**Expected answer:** No. The finding should identify Delivery and state that endpoint execution, exploitation, and installation have not been established by this record.

**Feedback and assessment:** Look for a distinction between an observed stage and possible later activity.

## Closing and Transition

The Cyber Kill Chain describes intrusion progression in seven stages. Assign a stage from the observed event, explain the supporting evidence, and leave unobserved activity open for investigation.

Previous: [0.6.2 – Diamond Model](../02-diamond-model/student-guide.md)

Next: [0.7 – External tools](../../07-tool-survey/01-external-tools/student-guide.md)

## References and Further Reading

- [Lockheed Martin — Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) — Original model and supporting resources.
