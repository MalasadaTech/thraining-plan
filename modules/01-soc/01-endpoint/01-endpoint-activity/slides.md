# Module 1.1.1 – Endpoint activity (the map)

- Recognize the five endpoint activity types.
- Classify a short description by its recorded operation.
- Explain why source and collection coverage matter when interpreting an event.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

Endpoint evidence helps you describe activity on a device. Recognizing the kind of activity first makes it easier to choose the right fields and explain what the event establishes. The next five lessons build that skill one activity type at a time.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Five kinds of endpoint activity

Classify the recorded operation: process, file, registry, host-network, or image/driver load. A log can contain many events.

**Speaker notes:** Ask learners to classify the recorded operation before discussing suspiciousness. Explain event versus log once so later lessons can use both terms naturally.

---

## Reference — Five kinds of endpoint activity

| Activity type | What the event concerns | Example |
|---|---|---|
| Process | A program starts, ends, or accesses another process. | A script interpreter launches PowerShell. |
| File | A file operation such as creation, rename, modification, reading, or deletion, where collected. | A process writes a file under Temp. |
| Registry | A Windows registry key or value changes. | A process sets a Run-key value. |
| Host-network | A connection or DNS operation observed by the endpoint. | PowerShell connects to a remote IP address. |
| Image / driver load | A module loads into a process, or a driver loads into the kernel. | A program loads a DLL. |

**Speaker notes:** Ask learners to classify the recorded operation before discussing suspiciousness. Explain event versus log once so later lessons can use both terms naturally. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Recognizing the observation

The same DLL can appear in a file-create event and an image-load event. The operation determines what each record establishes.

**Speaker notes:** Use the same DLL name in both statements and ask which verb changes the activity type. Preserve the possibility of linking both events later.

---

## Supplied example

“A file named `update.dll` was created” describes file activity. “PowerShell loaded `update.dll`” describes image-load activity. The filename is shared, but the recorded operation differs. A creation event alone leaves loading or execution unestablished.

**Speaker notes:** Use the same DLL name in both statements and ask which verb changes the activity type. Preserve the possibility of linking both events later.

---

## Understanding the source

Sysmon and MDE overlap but differ in coverage and schema. Network-sensor records add a different viewpoint.

**Speaker notes:** Contrast the sensor viewpoints, then ask what endpoint evidence adds to a network connection. Avoid promising that either product records all five types completely.

---

## Knowledge check

1. Name the five activity types and give an example of each.
2. How does a file-create event differ from an image-load event for the same DLL?
3. Why should you check the schema when moving from Sysmon to MDE?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

Identify the recorded operation, then use the fields and coverage of its source to describe it. Related events can build a fuller sequence while retaining what each observation actually establishes.

Previous: [0.8 — Environment / signal flow](../../../00-intro/08-environment/01-orientation/student-guide.md)

Next: [1.1.2 – Process Activity](../02-process-activity/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — Advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
