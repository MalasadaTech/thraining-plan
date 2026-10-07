# Authoring Standard – Skim-First / Advance-Organizer Design

## Purpose

The training plan should support learners who preview material before they read it closely. A learner should be able to skim a meaningful instructional unit and quickly understand what it is about, why it matters, how it connects to what they already know, what they should pay attention to, and what they should understand or be able to do by the end.

This design combines three related ideas:

- **Advance organizers** give the learner a mental framework before the details arrive.
- **Metacognitive previewing** encourages the learner to compare new material with what they already know and predict what they expect to learn.
- **Signaling** uses headings, tables, emphasis, and recurring callouts to make the structure visible during a skim.

The intended learning cycle is:

**Preview → Predict → Read → Confirm**

The learner first previews the structure, predicts what they expect to learn, reads the material with that structure in mind, and then uses the summary to confirm and organize what they learned.

---

## 1. Apply the Design at Meaningful Instructional Levels

A meaningful instructional grouping that contains multiple learner lessons should normally have:

1. an **introduction**;
2. the instructional content;
3. a **summary**.

Apply this recursively when the directory represents a real learning unit rather than merely a filesystem convenience.

For example:

**Part III – Cyber Threat Intelligence**

→ CTI Introduction

→ **2.3 Analytical Frameworks Introduction**

→ MITRE ATT&CK

→ Diamond Model

→ Cyber Kill Chain

→ **2.3 Analytical Frameworks Summary**

→ additional CTI subunits

→ CTI Section Summary

The same principle applies throughout Shared Foundations, SOC, CTI, Threat Hunting, and Detection Engineering.

A wrapper is usually appropriate when a directory contains multiple learner lessons that answer a shared question or build toward a shared capability. Examples include `01-soc/02-zeek`, `02-cti/01-core-intel`, and `00-intro/06-frameworks`.

A wrapper is usually unnecessary for:

- `assets/` and other non-instructional folders;
- a directory that exists only for organization and does not represent a learner concept;
- a single lesson, unless that lesson itself functions as a major section;
- a nested directory where another intro and summary would merely repeat the parent wrapper.

The rule is therefore **instructional hierarchy, not filesystem hierarchy**. Stop adding wrappers when the next layer would not give the learner a new mental model.

---

## 2. Introductions Function as Advance Organizers

An introduction should do more than announce the topic. It should help the learner construct a mental map before reading the details.

A strong introduction answers four questions.

### Why does this matter?

Explain why the learner needs this material and where it fits in defensive cyber operations.

### What should I already know?

Briefly activate prior knowledge that the new unit builds on. Do not reteach the earlier material.

For example:

> Earlier, you learned how analysts distinguish observations from conclusions. This unit builds on that discipline by introducing frameworks that help organize evidence and relationships without allowing the framework to substitute for the evidence itself.

### What am I about to learn?

Give a concise map of the major concepts, decisions, or tasks the learner will encounter.

For example:

> In this unit, you will work with three analytical frameworks: MITRE ATT&CK, the Diamond Model, and the Cyber Kill Chain. Each organizes a different aspect of adversary activity and is useful for different analytical questions.

### What should I watch for while reading?

Point out the distinctions, decisions, or recurring ideas that deserve attention.

For example:

> As you read, pay attention to the question each framework helps answer. The important skill is not memorizing framework terminology; it is recognizing which structure helps you reason about the evidence in front of you.

The introduction should also preview the expected end state so the learner can compare **what I already know** with **what I should know or be able to do after this unit**.

---

## 3. Summaries Function as End-State Checks

A summary should not merely repeat the introduction or condense the chapter paragraph by paragraph.

Its central question is:

> **What should I understand or be able to do now that I have completed this unit?**

Where appropriate, use an explicit section such as:

### By this point, you should be able to:

- explain the major concepts introduced in the unit;
- distinguish concepts that are easily confused;
- perform the principal analytical or technical tasks introduced;
- recognize important evidence boundaries;
- apply the material to a realistic problem;
- explain how the unit connects to the larger defensive workflow.

The summary should surface the few ideas that matter most rather than reproduce every subsection.

For example:

> By this point, you should be able to explain how ATT&CK, the Diamond Model, and the Cyber Kill Chain organize different aspects of adversary activity. You should also be able to select a framework based on the analytical question rather than forcing every problem into the same model.

This gives the learner a concrete standard against which to compare their understanding.

---

## 4. Design the Main Content for Productive Skimming

A learner should be able to skim a chapter before reading it closely and still see its intellectual structure.

### Headings

Headings should describe meaningful concepts, questions, decisions, or workflow stages. Where reasonable, the headings alone should reveal the progression of the lesson.

Prefer:

**Selecting a Framework Based on the Analytical Question**

rather than:

**Framework Selection**

### Tables

Use tables when they make relationships easier to understand at a glance. Good uses include comparison, decision criteria, inputs and outputs, evidence types, workflow stages, tool/platform differences, and framework strengths.

Tables should clarify structure rather than simply compress prose.

### Bold text

Use bold deliberately to signal important concepts, decision points, workflow stages, evidence categories, artifacts, and terms the learner should recognize later.

If everything is emphasized, nothing is emphasized.

### Italics

Use italics sparingly for meaningful emphasis, introduced terminology, or distinctions where typography genuinely improves comprehension.

### Lists

Use lists when the information represents an actual set, sequence, criteria, or collection of parallel ideas. Explanatory reasoning should normally remain prose.

---

## 5. Use Consistent Learner Callouts

Recurring callouts help the learner recognize the kind of information they are seeing.

Recommended labels include:

**Key Point**  
A concept that deserves particular attention.

**Evidence Boundary**  
Clarifies what available evidence supports and where uncertainty remains.

**Example**  
Shows the concept in practice.

**A12 Case Study**  
Connects the lesson to the recurring course scenario.

**Remember**  
Reactivates an important concept from earlier material.

**Knowledge Check**  
Prompts the learner to retrieve or apply what they just learned.

These callouts are tools, not quotas. Use them when they improve comprehension.

---

## 6. Preserve an Evidence-First Teaching Voice

Skim-first design should reinforce the course's broader analytical principle:

> **Describe what the evidence shows first. Then decide what it means.**

Introductions, headings, examples, and summaries should model:

**Evidence → Reasoning → Bounded Conclusion → Action**

The learner voice should sound like an experienced analyst coaching a junior analyst. Use explanatory prose and natural connective reasoning. Explain why a distinction matters rather than relying on a prohibition or slogan to carry the lesson.

Prefer:

> The alert tells you that the analytic matched. Investigation determines what the matching activity means in context.

rather than:

> Alert ≠ malicious.

Prefer positive teaching guidance over repeated `Do not...`, `This is not...`, and `X is not Y` constructions. Negative boundaries are still appropriate when they prevent a real analytical mistake, but explain the reasoning around them.

Specification files, matrices, outlines, and maintainer checklists may remain terse. **Their maintenance voice is not a model for learner-facing prose.**

---

## 7. Scale the Wrapper to the Level

The same pattern can exist at several levels, but the amount of detail should scale with the size of the instructional unit.

### Course or role section

Use a substantial introduction and summary to explain the complete learning arc.

### Subunit

Use a shorter introduction and summary to frame the group of lessons and the shared capability they build.

### Nested lesson group

Use a compact wrapper that explains why the lessons belong together and what the learner should gain from the group.

### Individual lesson

Use the normal lesson components: purpose, learning objectives, main instruction, worked example where useful, knowledge check, and summary.

Each layer answers a different question:

- **Part:** Where are we going overall?
- **Subunit:** What problem are we learning to solve here?
- **Lesson group:** How do these related concepts fit together?
- **Lesson:** What exactly am I learning and practicing now?

Avoid repeating the same wording at every layer.

---

## 8. Perform the Skim Test

Before considering learner-facing content complete, review only:

- the introduction;
- headings;
- tables;
- intentionally bolded concepts;
- callouts;
- the summary.

Then ask:

1. Can I tell what this unit is trying to teach?
2. Can I see how the material is organized?
3. Can I identify the important concepts, decisions, or tasks?
4. Can I tell what I am expected to know or do afterward?
5. Does the summary give me a meaningful way to check my understanding?
6. Does the structure prepare me for the detailed reading rather than merely summarize it?
7. Does the skim reveal reasoning and evidence boundaries, not just vocabulary?

If the answer is no, improve the instructional structure before adding more content.

---

## 9. Desired Learner Experience

The curriculum should intentionally support this reading pattern:

1. Read the introduction.
2. Think about what you already know.
3. Form an expectation about what you are going to learn.
4. Read the summary before the main content if that helps you set an end state.
5. Skim the headings, tables, emphasized terms, and callouts.
6. Build a preliminary mental model of the unit.
7. Read the lesson closely.
8. Return to the summary and compare the expected end state with your actual understanding.

The material should work for a linear reader as well, but it should not assume that every learner begins with the first paragraph and reads straight through.

---

## 10. Authoring and QA Integration

This standard applies to:

- student-guide authoring;
- module-generation guidance;
- subunit introductions and summaries;
- slide organization where the same preview/end-state pattern improves comprehension;
- ebook manuscript generation;
- learner-facing curriculum QA.

The standard works alongside the voice standard:

- **Voice:** how the material explains.
- **Skim-first design:** how the material is structured so the learner can anticipate, organize, and confirm what they are learning.

When creating or revising a lesson, use the normal lesson template. When creating a wrapper around multiple lessons, use the subunit introduction and summary templates. Introductory and summary wrappers are synthesis/navigation material and should not invent new proficiency requirements.
