# Instructor Guide – Module 1.1.1 – Endpoint activity (the map)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 2b / 2b  
- Hunter: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 1a / 2b  
- CTI: 1.1.1.1 A / A / A ; 1.1.1.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Endpoint evidence helps you describe activity on a device. Recognizing the kind of activity first makes it easier to choose the right fields and explain what the event establishes. The next five lessons build that skill one activity type at a time.

## Learning Objectives

1. Recognize the five endpoint activity types.
2. Classify a short description by its recorded operation.
3. Explain why source and collection coverage matter when interpreting an event.

**Mapped Proficiency Items:**
- K: 1.1.1.1 – Endpoint activity (the map)
- T: 1.1.1.2 – Given a one-line description, name the activity type

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required.

Use the proficiency levels above to adjust prompting and explanation depth. The module focuses on its mapped knowledge and tasks; the linked next lesson develops the next step.

## Suggested Timing

| Section | Minutes | Focus |
|---|---|---|
| Opening | 2 | Connect the lesson to its purpose. |
| Explanation and worked example | 8 | Read the supplied evidence and demonstrate the reasoning. |
| Knowledge check and feedback | 6 | Complete the interpretation or modification tasks. |
| Summary and transition | 2 | Consolidate the result and connect the next lesson. |
| **Total** | **18** | |

## Detailed Teaching Notes

### 1. Five kinds of endpoint activity

Ask learners to classify the recorded operation before discussing suspiciousness. Explain event versus log once so later lessons can use both terms naturally.

**Key point to reinforce:** Classify the recorded operation: process, file, registry, host-network, or image/driver load. A log can contain many events.

### 2. Recognizing the observation

Use the same DLL name in both statements and ask which verb changes the activity type. Preserve the possibility of linking both events later.

**Key point to reinforce:** The same DLL can appear in a file-create event and an image-load event. The operation determines what each record establishes.

### 3. Understanding the source

Contrast the sensor viewpoints, then ask what endpoint evidence adds to a network connection. Avoid promising that either product records all five types completely.

**Key point to reinforce:** Sysmon and MDE overlap but differ in coverage and schema. Network-sensor records add a different viewpoint.

## Knowledge Check — Answer Key

### 1. Name the five activity types and give an example of each.

**Expected answer:** Process, file, registry, host-network, and image/driver load; examples should identify the operation shown in the table.

### 2. How does a file-create event differ from an image-load event for the same DLL?

**Expected answer:** Creation records a file operation; image load records the module loading into a process. One does not establish the other.

### 3. Why should you check the schema when moving from Sysmon to MDE?

**Expected answer:** They have overlapping capabilities but different field names, event types, and collection coverage.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Identify the recorded operation, then use the fields and coverage of its source to describe it. Related events can build a fuller sequence while retaining what each observation actually establishes.

Previous: [0.8 — Environment / signal flow](../../../00-intro/08-environment/01-orientation/student-guide.md)

Next: [1.1.2 – Process Activity](../02-process-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — Advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables)
