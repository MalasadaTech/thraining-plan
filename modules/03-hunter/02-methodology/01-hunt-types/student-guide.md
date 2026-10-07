# Module 3.2.1 – Hunt Types

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.1 B / C / C ; 3.2.1.1–3.2.1.4 3c / 4c / 4c  
- SOC: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
- CTI: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Explain the four hunt types used by this course and the **initiating signal** for each.
2. Given a seed, identify the primary hunt type and state the question or look-for it should produce.

## Mapped Proficiency Items

- K: 3.2.1 – Hunt types
- T: 3.2.1.1 – Execute an intel-driven hunt
- T: 3.2.1.2 – Execute a hypothesis-driven hunt
- T: 3.2.1.3 – Execute a reactive hunt
- T: 3.2.1.4 – Execute an anomaly-based hunt

## 1. Key Concepts

There is no single universal industry taxonomy for hunt types. This course uses four labels because they help explain **what caused the hunt to begin**.

| Course hunt type | Primary initiating signal | A12 example |
|---|---|---|
| **Intel-driven** | CTI provides a behavior, observable, indicator, or procedure worth searching locally. | CTI reports the update domain or a distinctive Run-key procedure. |
| **Hypothesis-driven** | The hunter begins with a testable proposition about what should be visible if an activity is occurring. | “If A12-style persistence exists elsewhere, we should see a Run value pointing into a user-writable Temp path.” |
| **Reactive** | A known incident or confirmed finding creates a need to determine wider scope or related activity. | After A12, search the estate for the same or related persistence and payload artifacts. |
| **Anomaly-based** | An unusual pattern or deviation from baseline becomes the starting lead. | Rare outbound `:8080` requests for `/update.exe` on hosts without an associated alert. |

### The categories can overlap

A reactive hunt can also use intelligence. An intel-driven hunt should still have a testable question. An anomaly can later be linked to a known actor.

For this course, classify the hunt by its **primary starting signal**.

That prevents a taxonomy debate from becoming more important than the hunt itself.

### Every hunt should become testable

Even when the hunt does not begin as “hypothesis-driven,” it should eventually be expressed as a question or expectation that evidence can support or fail to support.

Examples:

**Intel-driven**
> CTI reports the `Updater` Run value. Do other user workstations contain the same value/path relationship?

**Reactive**
> A12 affected one workstation. Are the same or closely related artifacts present elsewhere during the incident window?

**Anomaly-based**
> Several hosts made rare `:8080` requests for `/update.exe`. Is the pattern associated with the A12 activity set or a benign application?

### Preparation is not execution

This lesson prepares you to recognize the initiating signal, classify the primary hunt type, and form the first testable question. Those are required planning skills, but they do **not** by themselves satisfy a task whose approved verb is **execute**.

For `3.2.1.1`–`3.2.1.4`, execution means you actually run the hunt against supplied or approved telemetry and record the scope, query/search, results, gaps, and bounded finding.

Use the [Hunt Execution Practical](hunt-execution-practical.md) to demonstrate the four execution tasks. The detailed hunt-development model is taught next in 3.2.2.

## 2. Knowledge Check

1. Why can one hunt reasonably fit more than one category?
2. CTI publishes a distinctive persistence procedure and you decide to look for it locally. Which course type best describes the initiating signal?
3. An active A12 investigation asks hunting to determine whether other hosts are affected. Which type is primary, and what question would you ask?

## 3. Summary

The four course hunt types describe the **primary reason the hunt starts**.

They are useful labels, not rigid boxes. Regardless of type, the hunt should become a bounded, testable search.

**Next:** **3.2.2 – Hunt Development Concepts**.
