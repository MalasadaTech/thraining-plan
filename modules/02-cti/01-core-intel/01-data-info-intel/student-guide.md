# Module 2.1.1 – Difference between data, information, and intelligence

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.1 B / C / C ; 2.1.1.1 3c / 4c / 4c  
- Hunter: 2.1.1 A / B / B ; 2.1.1.1 1a / 2b / 3c  
- SOC: 2.1.1 A / A / A ; 2.1.1.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Define data, information, and intelligence, and explain how context and analysis develop recorded observations into an assessment.
2. Categorize an example as data, information, or intelligence and explain your reasoning.

**Mapped Proficiency Items:**
- K: 2.1.1 – Difference between data, information, and intelligence
- T: 2.1.1.1 – Correctly categorize examples as data, information, or intelligence

## 1. Key Concepts

CTI analysts work with material in many forms: individual indicators, logs, incident notes, and published reports. Each can contribute to an investigation, but they provide different kinds of understanding. Recognizing what a piece of material tells you helps you decide what work is still needed before you can use it to answer someone's question.

In this lesson, we use three terms to explain that development: **data**, **information**, and **intelligence**.

| Term | Meaning in this lesson | What the analyst contributes |
|---|---|---|
| **Data** | Individual recorded values or observations, such as an IP address, a timestamp, or a file hash. | Identifies what was recorded and where it came from. |
| **Information** | Data organized and placed in context so that it describes an event or situation. | Connects relevant observations to explain who did what, when, and where. |
| **Intelligence** | An assessment developed by evaluating information to answer a relevant question and support a decision. | Explains what the evidence means, why that conclusion is supported, and what uncertainty remains. |

### Adding context

An IP address by itself gives you very little to work with. You need to know where it appeared and what was happening at the time. It might identify the destination of a workstation's connection, an address returned by a DNS lookup, or an indicator copied from a report.

As you establish those relationships, you develop information that describes the situation. For example, connecting an address to a particular workstation, request, and incident gives another analyst enough context to understand why you are examining it.

### Developing an assessment

Analysis begins with the question you need to answer. You examine the relevant information, consider how reliable and complete it is, and decide which explanation the evidence supports. That conclusion is an **analytic judgment**. Explaining the reasoning allows the recipient to understand how you reached it and how much weight to place on it.

Intelligence can help someone decide what to investigate, what to prioritize, or whether a threat matters to their organization. It may include a recommended action, but its value also comes from improving the recipient's understanding of the situation.

### Following one example

Consider the course's A12 incident. The question is: **What role did the update domain play in the activity on WS-JLEE?** A payload host is a server used to deliver a file involved in the attack.

**Start with data.** You encounter the address `203.0.113.88`. On its own, the address tells you neither what the workstation did nor how the address relates to the incident.

**Develop information.** The incident records connect WS-JLEE to that address, and the HTTP log records a request to the update domain for `/update.exe`. You can now describe the observed activity: the workstation requested a file from that destination during the incident. This is useful context, although the request alone does not establish that the file was successfully delivered or executed.

**Develop intelligence.** You evaluate that request alongside the suspicious process activity already associated with A12. You consider whether the destination served a role in delivering the payload and explain the limits of that interpretation:

> We assess that the update domain was likely used for attempted payload delivery in A12. The workstation requested `/update.exe` from that destination during the suspicious activity. These observations support investigating the domain's delivery role, but they do not establish that the requested file was successfully downloaded or executed.

The assessment adds an explanation of the domain's likely role and identifies what still needs to be established. That helps the investigator decide what evidence to seek next. The reasoning behind the conclusion is what makes this an assessment; the phrase “we assess” simply signals that a judgment is being expressed.

### Communicating uncertainty

You will often need to provide an assessment before every question has been resolved. Explain what the evidence supports and where it leaves room for other explanations. In the example, the request supports a possible delivery role, while successful delivery and execution remain separate questions.

Being clear about those limits helps the recipient use the assessment appropriately. Later lessons develop the language used to express likelihood and confidence.

### Recognizing the difference in practice

When reviewing an item, ask what work it contains. Does it present a recorded value, connect observations into a meaningful description, or evaluate evidence to answer a question? Look for the context and reasoning that support your choice. A single report may contain all three, so classify the particular statement you are examining.

## 2. Knowledge Check

1. You receive only the address `203.0.113.88`. How would you categorize it, and what context would you seek to understand its relevance?
2. A log shows that WS-JLEE requested `/update.exe` from the update domain during A12. Explain why this is information and identify one conclusion the request alone cannot establish.
3. Review the assessment in the worked example. What analysis does it add to the observations, and how does its uncertainty affect the investigator's next step?

## 3. Summary

Data provides the recorded observations from which you begin. Adding context develops information that describes a situation. Evaluating that information against a relevant question produces an intelligence assessment that explains the evidence's significance and supports a decision. A useful assessment makes its reasoning and remaining uncertainty clear enough for another person to use.


## 4. Related Modules

- 1.5 – Reporting
- 2.1.2 – Intelligence lifecycle
- 2.1.4 – Intelligence requirements
- 2.2.1 – Estimative language
- 2.7 – Finished intelligence products

## Supporting Reference

[ODNI, ICD 203 — Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf): supports the guidance on distinguishing evidence from judgments and explaining uncertainty. The three-part teaching model and classroom example above are instructional explanations, not quoted definitions from the directive.

**Next:** [2.1.2 – Intelligence lifecycle](../02-intelligence-lifecycle/student-guide.md).
