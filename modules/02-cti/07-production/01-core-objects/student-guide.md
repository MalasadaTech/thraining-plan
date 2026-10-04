# Module 2.7.1 – Core STIX Objects

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- Hunter: 2.7.1 B / C / C ; 2.7.1.1 2b / 3c / 4c  
- SOC: 2.7.1 A / B / B ; 2.7.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Recognize the **eleven STIX 2.1 object types selected for this course** and explain what each represents.
2. Given a line from a report, choose the most appropriate course object type and explain the evidence boundary behind that choice.

**Mapped Proficiency Items:**
- K: 2.7.1 – Core STIX objects
- T: 2.7.1.1 – Identify and label common STIX objects in a report

## 1. Key Concepts

**STIX**—Structured Threat Information Expression—is a standardized language for representing cyber threat and observable information.

This course uses **STIX 2.1**, the current OASIS standard used by the curriculum.

Reference: [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

STIX contains more object types than this lesson teaches. The eleven below are a **course-selected working set**, chosen because they appear repeatedly in CTI production and the later training modules.

### The course's eleven object types

| Object | What it represents |
|---|---|
| **Indicator** | A pattern that can detect suspicious or malicious activity. |
| **Observed Data** | A record that cyber-observable data was seen during a time window. |
| **Malware** | Malicious code, whether represented as a family or an instance. |
| **Attack Pattern** | A type of adversary behavior, technique, or method. |
| **Threat Actor** | An individual, group, or organization believed to operate with malicious intent. |
| **Intrusion Set** | A grouped set of adversarial behaviors/resources believed to share common properties and often a common operator. |
| **Campaign** | A set of malicious activities occurring over a period of time against targets. |
| **Course of Action** | An action intended to prevent, mitigate, or respond to malicious activity. |
| **Identity** | A person, organization, group, system, or other entity identity. |
| **Relationship** | A typed relationship connecting STIX objects. |
| **Sighting** | An assertion that a STIX Domain Object was seen. |

Other valid STIX 2.1 types include Infrastructure, Tool, Vulnerability, Report, Note, Grouping, Location, Incident, Malware Analysis, and others. Their absence from this course list does **not** mean they are invalid STIX objects.

### Indicator is not the same as a raw observable

A common beginner mistake is to treat every hash, IP address, or domain as an **Indicator**.

STIX separates the concepts more carefully.

An **Indicator** contains a detection pattern.

Example:

`[file:hashes.'SHA-256' = 'abc123...']`

That pattern can be used to look for matching activity.

A raw file, IP address, domain, process, or registry key is represented with a **STIX Cyber-observable Object (SCO)** such as File, IPv4 Address, Domain Name, Process, or Windows Registry Key.

An **Observed Data** object can then record that one or more of those SCOs were observed during a particular time window.

So:

- **File SCO:** the file/hash value itself.
- **Observed Data:** records that the file was observed.
- **Indicator:** a pattern used to detect activity matching that file/hash.

Reference: [STIX 2.1 – Observed Data and Cyber-observable Objects](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### Sighting is another distinct concept

A **Sighting** states that a STIX Domain Object was seen.

For example, an organization may record that an Indicator was sighted in its environment.

STIX can also attach:
- **Observed Data** describing what was actually seen;
- an **Identity or Location** describing where/who saw it.

This makes Sighting different from both Observed Data and a generic Relationship.

### Identity does not mean “the attacker”

Identity is a neutral entity object.

It can represent:
- an organization;
- a person;
- a group;
- a system;
- a class of entities.

For example:

- **DYA** → Identity (organization)
- **WS-JLEE** → could be modeled as an Identity with `identity_class: system` when the production design needs a system identity

Neither is automatically a Threat Actor.

Likewise, a vendor tracking name such as **PRD APT** should not automatically become a Threat Actor object merely because the report contains a name. The analyst should first determine what the source actually claims and what object type the evidence supports.

### Threat Actor and Intrusion Set are not interchangeable

**Threat Actor** focuses on the malicious actor entity.

**Intrusion Set** focuses on a set of adversarial behaviors/resources believed to share common properties and often a common operator.

Many intelligence providers use tracking labels before real-world identity is established. Depending on the underlying evidence and modeling approach, an Intrusion Set may be more appropriate than claiming a known Threat Actor.

The lesson does not force either object when the evidence is insufficient.

### Attack Pattern represents behavior

MITRE ATT&CK techniques can be represented as **Attack Pattern** objects in STIX.

Example:

> Encoded PowerShell / T1059.001 → Attack Pattern

That object represents the behavior—not the process event, hash, or victim.

### Relationship and Sighting are STIX Relationship Objects

Most of the course list above are **STIX Domain Objects (SDOs)**.

**Relationship** and **Sighting** are **STIX Relationship Objects (SROs)**.

This distinction matters because Sighting has its own specific fields, including `sighting_of_ref`; it is not simply a Relationship with a verb such as `sighting-of`.

## 2. Knowledge Check

1. Are the eleven objects in this lesson the only valid object types in STIX 2.1? Explain.
2. A report records that a file with a particular SHA256 was seen on a host. How are the raw file, the observation, and a detection pattern conceptually different in STIX?
3. Why should a vendor tracking name not automatically become a Threat Actor object?

## 3. Summary

STIX 2.1 gives analysts a structured vocabulary for threat and observable information.

The eleven types in this module are a **course subset**, not the entire STIX object model.

Keep these three distinctions especially clear:

- observable data is not automatically an Indicator;
- Sighting is not generic Relationship;
- Identity or a vendor label is not automatically Threat Actor.


## Supporting References

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
- [STIX 2.1 Interoperability Test Document](https://docs.oasis-open.org/cti/stix-2.1-interop/v1.0/stix-2.1-interop-v1.0.html)

**Next:** [2.7.2 – How STIX Objects Are Used in Intelligence Production](../02-stix-production/student-guide.md).
