# Module 2.7.5 – Disseminating Intelligence to the Correct Audiences

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.5 B / C / C ; 2.7.5.1 3c / 4c / 4c ; 2.7.5.2 3c / 4c / 4d ; 2.7.5.3 3c / 4c / 4c  
- Hunter: 2.7.5 A / B / B ; 2.7.5.1 1a / 2b / 3c ; 2.7.5.2 1a / 2b / 3c ; 2.7.5.3 1a / 2b / 3c  
- SOC: 2.7.5 A / A / B ; 2.7.5.1 1a / 1a / 2b ; 2.7.5.2 1a / 1a / 2b ; 2.7.5.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Select the audience, approved dissemination method, and appropriate sharing designation/instructions for a finished product.
2. Tailor the level of detail for technical and leadership audiences without changing the underlying judgment.
3. Explain why TLP markings and organizational channel/handling rules are related but separate controls.

**Mapped Proficiency Items:**
- K: 2.7.5 – Disseminating intelligence to the correct audiences
- T: 2.7.5.1 – Select audience and method and apply correct handling markings
- T: 2.7.5.2 – Tailor products to different audiences
- T: 2.7.5.3 – Disseminate intelligence products through approved channels

## 1. Key Concepts

Dissemination is the step where a finished product reaches the people who need it through a method the organization authorizes.

Three decisions should remain separate:

1. **Audience** – Who needs the information for a decision or action?
2. **Channel / method** – Which approved system or workflow should carry it?
3. **Sharing / handling rules** – Who may receive or redistribute it?

The correct audience on an unapproved channel is still poor dissemination.

### TLP is a sharing protocol, not a classification system

The **Traffic Light Protocol (TLP) 2.0** provides standardized markings for how cybersecurity information may be shared.

Reference:
- [FIRST – Traffic Light Protocol](https://www.first.org/tlp/)
- [FIRST – TLP 2.0 Definitions and Usage Guidance](https://www.first.org/tlp/docs/tlp-a4.pdf)

TLP does **not** replace:
- classification markings;
- legal restrictions;
- contractual controls;
- privacy rules;
- organizational data-handling policy.

Use the actual local marking/handling scheme when one exists.

### Correct TLP 2.0 meanings

| Marking | Sharing boundary |
|---|---|
| **TLP:RED** | Individual recipients only; no further disclosure. |
| **TLP:AMBER+STRICT** | Need-to-know sharing **within the recipient's organization only**. |
| **TLP:AMBER** | Need-to-know sharing within the recipient's organization **and its clients**. |
| **TLP:GREEN** | Sharing within the defined community; not public channels. |
| **TLP:CLEAR** | May be shared without TLP restriction, subject to applicable rules/procedures and copyright. |

The old classroom shorthand “TLP:AMBER = organization only” is incorrect under TLP 2.0. Organization-only sharing is **TLP:AMBER+STRICT**.

FIRST also permits accompanying instructions when the originator needs to clarify or further constrain sharing.

Reference: [FIRST – TLP Use Cases](https://www.first.org/tlp/use-cases)

### Classroom handling card

For the A12 exercise, assume:

- technical incident details are **TLP:AMBER+STRICT**;
- the organization requires the product to travel through either the approved incident-management system or approved CTI channel;
- personal SMS, unapproved personal chat, and public posting are not approved dissemination methods.

These are **classroom workflow assumptions**, not live DYA or user-organization policy.

### Tailoring changes detail, not truth

The technical and leadership versions can contain different levels of detail while preserving the same key judgment and uncertainty.

**Technical / IR version**
- `WS-JLEE`
- `/update.exe`
- update domain / IP
- relevant timestamps
- evidence caveat
- next investigative need

**Leadership version**
> We assess a suspicious external domain was likely used for attempted payload delivery to a user workstation. IR has the affected host in scope; available evidence does not yet establish successful payload execution.

The leadership version removes unnecessary technical detail without changing:
- **likely**
- **attempted payload delivery**
- the unresolved execution gap

### Minimize sensitive detail when the audience does not need it

Tailoring is not only about readability.

It can also reduce unnecessary exposure of:
- hostnames;
- usernames;
- hashes;
- internal paths;
- client identifiers;
- investigative methods.

Only include detail the audience needs for its decision.

### Additional sharing instructions

A TLP marking may be accompanied by specific instructions when appropriate and authorized.

Example:

> TLP:AMBER+STRICT — Do not redistribute outside the incident-response and CTI teams without originator approval.

Local policy still governs whether and how such instructions are used.

## 2. Knowledge Check

1. Under TLP 2.0, which marking restricts sharing to the recipient's organization only?
2. Why are TLP marking and approved dissemination channel separate decisions?
3. Give one detail that belongs in the IR version of A12 but can be omitted from a leadership awareness version without changing the judgment.

## 3. Summary

Good dissemination aligns **audience, approved channel, and sharing rules**.

TLP 2.0 controls information-sharing boundaries; it is not a substitute for classification, privacy, legal, contractual, or organizational handling requirements.

Tailor detail for the audience, but preserve the judgment and uncertainty.


## Supporting References

- [FIRST – Traffic Light Protocol](https://www.first.org/tlp/)
- [FIRST – TLP 2.0 Definitions and Usage Guidance](https://www.first.org/tlp/docs/tlp-a4.pdf)
- [FIRST – TLP Use Cases](https://www.first.org/tlp/use-cases)

**Next:** [2.7 – Intelligence Production and Dissemination Summary](../summary.md).
