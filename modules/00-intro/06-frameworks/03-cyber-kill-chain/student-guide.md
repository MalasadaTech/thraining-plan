# Module 0.6.3 – Cyber Kill Chain

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.3.1 A / B / C ; 0.6.3.2 2b / 3c / 4c  
- Hunter: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- CTI: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- DE: 0.6.3.1 A / B / B ; 0.6.3.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Describe the purpose and seven stages of the Cyber Kill Chain.
2. Assign a stage to a simple observed event and explain the evidence.
3. Distinguish observed progression from unestablished activity.

**Mapped Proficiency Items:**
- K: 0.6.3.1 – Cyber Kill Chain
- T: 0.6.3.2 – Identify the Kill Chain stage of observed activity

## Why This Matters

The Cyber Kill Chain provides a way to discuss progression through an intrusion. It helps analysts place an observed event in a larger sequence and consider where defensive action could interrupt that sequence. The available evidence may show only part of the activity.

## 1. The seven stages

| Stage | What it describes |
|---|---|
| Reconnaissance | Gathering information about a target. |
| Weaponization | Preparing a malicious payload or delivery package. |
| Delivery | Transmitting the malicious material to the target. |
| Exploitation | Exploiting a vulnerability to enable the attack. |
| Installation | Establishing a malicious implant or foothold. |
| Command and Control | Communicating with infrastructure used to direct the compromised system. |
| Actions on Objectives | Carrying out the attacker's intended outcome. |

The sequence is a model for reasoning about an intrusion. Real activity can repeat stages, take different paths, or leave stages unobserved. Use the model to explain what the evidence shows while keeping those limits visible.

## 2. Placing an observed event

Suppose an email record shows that a message containing a `.vbs` attachment was delivered to a mailbox. For this example, separate analysis has established that the attachment is malicious. The email record supports **Delivery** because it shows the malicious material reaching the target.

The record does not show how the attachment was prepared, whether anyone opened it, or whether it established a foothold. Those are questions for other evidence. The `.vbs` extension alone would not establish maliciousness; the example's stated analysis supplies that context.

## 3. Explaining a stage assignment

A useful stage assignment includes the stage, the event supporting it, and any uncertainty that affects interpretation. For example: “Delivery: the email record shows the malicious attachment reached the mailbox; execution has not been established.”

ATT&CK, the Diamond Model, and the Cyber Kill Chain answer different questions. ATT&CK names behavior, the Diamond Model organizes the elements of an event, and the Kill Chain describes progression. Together they help analysts explain activity without requiring every observation to prove an entire intrusion.

## Knowledge Check

1. Name the seven Cyber Kill Chain stages and explain what the model helps analysts describe.
2. An email record confirms delivery of an attachment established as malicious. Which stage is supported, and why?
3. Does that delivery record establish exploitation or installation? What would you say in the finding?

## Summary

The Cyber Kill Chain describes intrusion progression in seven stages. Assign a stage from the observed event, explain the supporting evidence, and leave unobserved activity open for investigation.

## Course Connections

Previous: [0.6.2 – Diamond Model](../02-diamond-model/student-guide.md)

Next: [0.7 – External tools](../../07-tool-survey/01-external-tools/student-guide.md)

## References and Further Reading

- [Lockheed Martin — Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) — Original model and supporting resources.
