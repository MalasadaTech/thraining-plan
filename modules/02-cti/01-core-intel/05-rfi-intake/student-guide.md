# Module 2.1.5 – RFI Intake and Prioritization

**Target Audience:** CTI Analyst (primary); Threat Hunter and SOC Analyst (supporting context)  
**Proficiency Focus:**  
- CTI: 2.1.5 B / C / C ; 2.1.5.1 3c / 4c / 4d  
- Hunter: 2.1.5 A / A / B ; 2.1.5.1 1a / 1a / 2b  
- SOC: 2.1.5 A / A / A ; 2.1.5.1 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes

## Learning Objectives

1. Capture a bounded RFI with its decision need, scope, deadline, and handling context.
2. Evaluate answerability, identify missing evidence, and justify priority or routing using local policy.

**Mapped Proficiency Items:**
- K: 2.1.5 – RFI intake and prioritization
- T: 2.1.5.1 – Receive, evaluate, and prioritize an RFI

## 1. Key Concepts

An **RFI — Request for Information** is a request for an answer or information that another consumer needs.

The RFI is not automatically:
- a new incident;
- a Priority Intelligence Requirement;
- a new collection campaign;
- a request to write everything known about the actor.

Its first job is to define **what the requestor needs answered**.

### 1. Receive

Capture enough information to understand the request.

Useful intake fields include:

- requestor / customer;
- question;
- why the answer is needed or what decision it supports;
- needed-by time, if relevant;
- scope or time window;
- handling restrictions;
- related incident/report/reference.

Local forms and queue fields belong to site-specific policy in 2.8; the course does not invent them.

### 2. Evaluate

Ask:

- Is the question clear and bounded?
- Do we already have an answer?
- What evidence would answer it?
- What evidence do we currently have?
- What is missing?
- Is CTI the right owner, or should the request be routed elsewhere?
- Does the request duplicate an existing requirement or product?

If the question is unclear, clarification may be the correct next action.

If the question cannot yet be answered, identify the gap rather than inventing a conclusion.

### 3. Prioritize

Priority should reflect the local policy, but the analyst can recognize common drivers:

- active incident or operational decision;
- time sensitivity;
- mission/customer importance;
- dependency: another team cannot proceed without the answer;
- effort and available evidence;
- existing standing priorities.

The classroom rule is simple:

> A bounded RFI supporting an active incident normally takes precedence over routine background reading.

That is a teaching scenario, not a universal queue SLA.

### A12 intake decision

The request asks: **Was the update domain the host that successfully delivered the payload in A12?** The requester needs to distinguish an attempted transfer from a completed one.

Record the requester and needed-by time from the actual request; clarify them if missing. Scope the work to WS-JLEE, the update domain, `/update.exe`, and the A12 time window. Reference the existing case rather than opening a second incident merely because an RFI arrived.

Available evidence establishes a request for `/update.exe`, but not successful download or execution. The question is clear; the evidence is incomplete. Record the missing transfer or host-file evidence and identify the appropriate source or owner. In this classroom scenario, the active incident gives the request priority over routine background research, subject to the site's actual rules.

### Carry the requirement forward

Use a short intake record:

`requester | question | decision/use | needed-by | scope | handling | case | evidence available | gap | priority/routing rationale`

This record directs collection in [2.1.9](../09-collection-sources/student-guide.md). Keep it with the evidence through the course; you will answer the same question in [2.7.4 – RFI Responses and Closure](../../07-production/04-rfi-response/student-guide.md). Obtain actual local priorities from [2.8.1](../../08-site-specific/01-local-priorities/student-guide.md) before applying this workflow at work.

## 2. Knowledge Check

1. Why is an RFI not automatically a PIR or a new incident?
2. The A12 request asks whether delivery succeeded, but you only have a request record. What should intake record?
3. What would you clarify if the requester asks only, “Are we seeing them?”

## 3. Summary

A clear RFI establishes the question, its purpose, and its limits. Record evidence gaps and priority before collection begins.

**Next:** [2.1.6 – Ensuring Intelligence Is Actionable](../06-actionable-intelligence/student-guide.md).
