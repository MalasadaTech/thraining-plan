# Instructor Guide – Module 2.3.3 – Cyber Kill Chain in Intelligence Analysis

**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Purpose

Teach learners to use the Cyber Kill Chain as an evidence-backed progression model.

References:
- [Lockheed Martin – Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
- [Overview PDF](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf)

## Key Correction

Do not equate a generic execution event with **Installation**. Kill Chain stage depends on the event's role in the intrusion.

Use clearer examples:
- arrival of malicious attachment/payload → Delivery
- triggering malicious code → Exploitation
- implant/persistence established → Installation
- control channel → Command and Control
- mission effect → Actions on Objectives

## Suggested Timing

| Part | Time |
|---|---:|
| Seven stages | 6 min |
| Evidence vs inference | 6 min |
| A12 examples | 6 min |
| Knowledge check | 4 min |
| Summary | 2 min |

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Fills all seven stages. | Ask for the evidence citation for each stage. |
| Calls every code execution Installation. | Ask whether anything was actually installed or established. |
| Calls any outbound traffic C2. | Ask what shows control/command communication. |
| Calls payload download Installation. | Separate transmission into the environment from installation/foothold establishment. |

## Knowledge Check – Answer Key

1. Only supported stages belong in the product; unobserved stages are evidence gaps.
2. A confirmed external download best supports **Delivery**; **Installation** needs evidence the payload was installed/established.
3. PowerShell execution establishes execution behavior, but the Kill Chain role depends on surrounding context; the process alone does not prove installation.

## Instructor References

- [Lockheed Martin – Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
- [Cyber Kill Chain overview PDF](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf)
