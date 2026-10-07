# Module 2.1.9 – Collection Sources and Methods

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.9 B / C / C ; 2.1.9.1 3c / 4c / 4c ; 2.1.9.2 3c / 4c / 4d  
- Hunter: 2.1.9 A / B / B ; 2.1.9.1 1a / 1a / 2b ; 2.1.9.2 1a / 1a / 2b  
- SOC: 2.1.9 A / A / B ; 2.1.9.1 1a / 1a / 1a ; 2.1.9.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the three source classes used in this course: **OSINT**, **commercial**, and **internal**.
2. Select appropriate source classes for a requirement and build a short collection plan that identifies collection order, the first action, and reasonable limits on scope.

**Mapped Proficiency Items:**
- K: 2.1.9 – Collection sources and methods (OSINT, commercial, internal)
- T: 2.1.9.1 – Identify appropriate collection source classes for a given requirement
- T: 2.1.9.2 – Plan collection against an intelligence requirement

## 1. Key Concepts

An intelligence requirement tells the analyst **what needs to be known**. Collection planning decides **where to look for the evidence that can answer it**.

Module 2.1.2 described Collection as a lifecycle stage—the work of gathering relevant material. This lesson looks inside that stage and asks which broad class of source is most appropriate for the question.

This course uses three source classes:

| Source class | What it includes | Especially useful when the requirement asks... |
|---|---|---|
| **OSINT** | Public reporting, public repositories, public DNS and registration data, open research, public malware or security reporting | What is publicly known about the threat, infrastructure, technique, or campaign? |
| **Commercial** | Paid threat-intelligence services, premium sandboxing or enrichment, vendor reporting, licensed datasets | What additional enrichment or vendor-held context can supplement open and internal evidence? |
| **Internal** | SIEM, EDR, network telemetry, tickets, incident records, internal threat-intelligence platforms, hunt results, internal logs | What is happening in **our** environment, and what evidence do **we** have? |

The classes can be combined. A mature collection effort often uses more than one. The important question is not “Which class is best?” in the abstract. It is **which source is most likely to reduce uncertainty about this requirement, given what is already available**.

### Collection order follows the requirement

Suppose the requirement asks:

> **What role did the update domain play in the activity on WS-JLEE during A12?**

Because the question concerns activity in the organization's own environment, internal evidence should usually be an early collection priority. Relevant internal sources might include HTTP and DNS telemetry, host evidence, and incident records.

Public or commercial sources may still add useful context. They could show whether the domain has appeared in other reporting, whether it has related infrastructure, or whether vendors have seen similar activity. But that external context cannot replace the internal evidence needed to answer what happened on WS-JLEE.

Now consider a different requirement:

> **What public reporting exists about this delivery technique and the infrastructure associated with it?**

For that question, OSINT or commercial reporting may be the logical starting point. The requirement changes the collection order.

### A short collection plan

A collection plan in this lesson does not need to be a formal document. It should show that the analyst has connected the requirement to a deliberate set of collection actions.

A useful short plan includes:

1. **Requirement:** What question are you answering?
2. **Source class and order:** Which class or classes should be checked first, and why?
3. **First collection action:** What specific evidence will you seek first?
4. **Limits or stop conditions:** What will you defer, avoid, or revisit only if the first collection does not answer the requirement?

For the A12 requirement, a short plan might look like this:

- **Requirement:** Determine the update domain's role in the activity on WS-JLEE.
- **First class:** Internal, because the question is about observed activity in our environment.
- **First action:** Review the relevant HTTP, DNS, and host evidence for the A12 window.
- **Next class if needed:** OSINT or commercial sources to add external context about the domain or delivery pattern.
- **Limit:** Record unrelated infrastructure pivots, but defer them unless they help answer the current requirement or justify a follow-on requirement.

This structure prevents habitual collection. The analyst is not automatically starting with a favorite platform or collecting every available pivot.

### Source quality and access still matter

Selecting a source class is only the beginning. Within any class, sources vary in reliability, timeliness, coverage, and accessibility.

An analyst should consider:

- whether the source can actually answer the question;
- how current and complete the source is;
- whether the organization has lawful and authorized access;
- whether another source can corroborate an important claim; and
- whether the expected value of the collection justifies the time and effort.

Later modules go deeper into specific tools and local collection-request processes. In this lesson, the goal is to build the habit of selecting sources **because they answer the requirement**, not because they are familiar or convenient.

### Plan for the evidence gap, not for the tool

A weak plan says, “Open the TIP and search the domain.”

A stronger plan says, “Use internal telemetry first to determine whether WS-JLEE resolved and contacted the domain during A12; if the internal evidence leaves the domain's broader role unclear, use public or commercial reporting to add external context.”

The stronger plan explains what the collection is meant to establish. The tool can change without changing the analytical purpose.

### Use the local collection process

Carry forward the intake record from [2.1.5](../05-rfi-intake/student-guide.md). Before requesting collection or using an external service, confirm the actual approval and handling requirements described in [2.8.2](../../08-site-specific/02-local-production/student-guide.md). Do not infer authorization from the availability of a tool.

## 2. Knowledge Check

1. The Collection lifecycle stage and a collection source class are the same thing. True or false? Explain the difference.
2. A requirement asks, “What happened with this domain on our network during A12?” Which source class should usually be an early priority, and why?
3. Write a short collection plan for the A12 update-domain requirement that includes the first source class, the first collection action, one possible follow-on class, and one reasonable scope limit.

## 3. Summary

Collection planning connects an intelligence requirement to the evidence most likely to answer it. This course groups sources into OSINT, commercial, and internal classes, and those classes can be combined as needed.

The requirement determines the order. Questions about the organization's own environment usually require internal evidence early; questions about the public threat landscape may begin with OSINT or commercial reporting.

A good collection plan explains **what evidence is needed and why**, not merely which tool the analyst intends to open. It also defines reasonable limits so interesting pivots do not replace the question the team is supposed to answer.


## 4. Related Modules

- 2.1.8 – Attribution (previous)
- 2.1.2 – Intelligence lifecycle
- 2.1.4 – Intelligence requirements
- 2.8.2.1 – Local collection requests
- 0.7 / 2.4 / 2.4 – Tool survey, TIP, and platform depth

**Next:** [2.1 – Intelligence Foundations and Requirements Summary](../summary.md).
