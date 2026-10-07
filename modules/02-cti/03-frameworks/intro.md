# 2.3 – Analytical Frameworks: Introduction

**Module Type:** Subunit advance organizer — no new proficiency mapping  
**Estimated Time:** 5–10 minutes  

## Why This Subunit Matters

Analytical frameworks help you organize evidence so that another analyst can understand **what happened, how the pieces relate, and where the activity fits in a larger intrusion**. They are most useful when they make reasoning easier to inspect—not when they replace the evidence or make a conclusion sound stronger than the source material supports.

In the previous subunit, Analytical Tradecraft, you focused on how to evaluate information, express uncertainty, structure analysis, and reduce bias. This subunit builds on that discipline by giving you three different ways to organize the evidence you have already evaluated.

The important question is not, “Which framework is best?” It is:

> **Which framework helps answer the analytical question in front of me?**

## What You Will Learn

The three frameworks in this subunit look at different aspects of the same activity.

| Lesson | Main question | What the framework contributes |
|---|---|---|
| **2.3.1 – MITRE ATT&CK for CTI** | What behavior does the evidence demonstrate? | A shared vocabulary for mapping observed or reported behavior to supported tactics, techniques, and sub-techniques. |
| **2.3.2 – Diamond Model** | What entities and relationships make up this intrusion event? | A way to organize Adversary, Capability, Infrastructure, and Victim while keeping uncertain vertices visible. |
| **2.3.3 – Cyber Kill Chain** | Where does the supported activity fit in attack progression? | A way to describe progression while leaving unsupported stages unresolved. |

You may use more than one framework on the same evidence because each one answers a different question.

## Connect to What You Already Know

From **2.2 Analytical Tradecraft**, you already have several habits that matter here:

- evaluate the quality and credibility of the information before relying on it;
- separate what the evidence directly supports from what you infer;
- use estimative language when a judgment is probabilistic;
- make uncertainty visible rather than hiding it;
- watch for analytical shortcuts and cognitive bias.

Those habits continue to apply when a framework gives you convenient labels or boxes. A framework can organize a judgment, but it does not create evidence that was not present before.

## What to Watch For

As you work through the three lessons, pay particular attention to these ideas.

### The analytical question should drive the framework

ATT&CK, the Diamond Model, and the Cyber Kill Chain are not interchangeable. Each highlights a different dimension of the activity. Start with the question you need to answer, then select the framework that helps organize that question.

### A framework label does not strengthen weak evidence

A technique ID, Diamond vertex, or Kill Chain stage can make an analysis look precise. The precision is useful only when the underlying evidence supports it.

### Unknown or unresolved is a valid analytical result

You do not need to fill every Diamond vertex, assign every Kill Chain stage, or map every plausible ATT&CK technique. An unresolved field can tell the reader exactly where the evidence becomes thin.

### The same evidence can support different views without becoming different evidence

For example, a PowerShell process can be:

- mapped to an ATT&CK behavior;
- described as part of the Capability vertex in a Diamond;
- considered in the context of attack progression for the Kill Chain.

Those are different analytical views of the same underlying observation.

## Expected End State

By the end of this subunit, you should be able to:

- select a framework based on the analytical question you are trying to answer;
- map observed or reported behavior to ATT&CK while preserving the supporting evidence;
- populate a Diamond Model event without filling uncertain vertices with guesses;
- assign Cyber Kill Chain stages only when the surrounding evidence supports the stage;
- explain how the three frameworks complement one another without treating any of them as proof by themselves.

## How to Preview This Subunit

Before reading the individual lessons closely:

1. read this introduction;
2. read the **2.3 Analytical Frameworks Summary**;
3. skim the headings, tables, examples, and emphasized terms in the three lessons.

Try to predict which framework you would use for each kind of analytical question. Then return to the summary after the detailed reading and check whether your answers have become more precise.
