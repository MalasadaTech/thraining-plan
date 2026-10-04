# Module 3.2.2 – Hunt Development Concepts

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.2 B / C / C ; 3.2.2.1–3.2.2.3 3c / 4c / 4d  
- SOC: 3.2.2 A / B / B ; 3.2.2.1–3.2.2.3 1a / 1a / 2b  
- CTI: 3.2.2 A / B / B ; 3.2.2.1–3.2.2.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Write a testable hunt hypothesis and define a scope that states population, time window, and telemetry.
2. Prioritize the hunt and identify a **distinctive/discriminating pattern** suitable for internal search.

## Mapped Proficiency Items

- K: 3.2.2 – Hunt development concepts
- T: 3.2.2.1 – Develop and document a hunt hypothesis
- T: 3.2.2.2 – Scope and prioritize a hunt
- T: 3.2.2.3 – Identify unique patterns or behaviors suitable for hunting

## 1. Key Concepts

A hunt becomes useful when another hunter can understand **what is being tested, where it will be tested, why it matters now, and what evidence would be meaningful**.

This course captures that in four core fields:

| Field | Purpose |
|---|---|
| **Hypothesis** | A proposition that evidence can support or fail to support. |
| **Scope** | Population, time window, telemetry, and important exclusions. |
| **Priority** | Why this hunt should consume time now. |
| **Distinctive pattern** | The behavior or artifact that makes the search selective enough to investigate. |

### Hypothesis

A good hypothesis is not a topic such as “hunt persistence.”

It connects a condition to expected evidence.

> If A12-style persistence exists on additional user workstations, we expect to observe Run-key values pointing to `update.exe` or closely related payloads in user-writable paths.

That statement can produce findings, or it can produce no findings within the tested scope.

### Scope

Scope should make a negative result interpretable.

For example:

- **Population:** managed Windows user workstations
- **Window:** previous 14 days
- **Telemetry:** registry modification + file/process telemetry
- **Exclusions:** known software-deployment systems or approved updater paths, where appropriate

“Entire enterprise, all time, every log” is not automatically better. It often makes the search expensive and the result harder to interpret.

### Priority

Useful priority factors include:

- active incident or mission need;
- strength and freshness of the lead;
- local applicability;
- available telemetry;
- likely defensive value;
- search cost and analyst capacity;
- existing detection coverage.

ATT&CK mapping can support priority later, but an ATT&CK tactic name is not a priority score by itself.

### Distinctive pattern

The curriculum calls this a “unique pattern,” but in practice **distinctive** or **discriminating** is the better idea.

`Updater` alone may be useful if rare locally. A stronger pattern can combine:

- Run-key location;
- value name;
- user-writable target path;
- uncommon parent process;
- file/signing context.

The goal is not perfect uniqueness. The goal is enough specificity to separate a manageable set of candidates from normal activity.

### Visibility comes before interpretation

A hunt that depends on registry modification data cannot produce a meaningful “not found” result on systems where registry telemetry is absent.

Document that limitation in scope.

## 2. Knowledge Check

1. Why is “hunt persistence” not a sufficient hypothesis?
2. What four core fields does this course use to develop a hunt?
3. Write a scoped A12 hypothesis using user workstations, a 14-day window, and registry/file telemetry.

## 3. Summary

Develop the hunt before running the search.

A useful hunt has a testable hypothesis, bounded scope, defensible priority, and a distinctive pattern grounded in telemetry you actually have.

**Next:** **3.3.1 – Tool Capabilities for Hunting**.
