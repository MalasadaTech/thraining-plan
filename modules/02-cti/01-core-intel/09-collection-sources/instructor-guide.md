# Instructor Guide – Module 2.1.9 – Collection Sources and Methods

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.9 B / C / C ; 2.1.9.1 3c / 4c / 4c ; 2.1.9.2 3c / 4c / 4d  
- Hunter: 2.1.9 A / B / B ; 2.1.9.1 1a / 1a / 2b ; 2.1.9.2 1a / 1a / 2b  
- SOC: 2.1.9 A / A / B ; 2.1.9.1 1a / 1a / 1a ; 2.1.9.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Teach learners to select broad source classes based on an intelligence requirement and to express that choice as a short collection plan with deliberate order, a concrete first action, and reasonable scope limits.

**Context:** Module 2.1.4 taught learners to define the question. Module 2.1.2 introduced Collection as a lifecycle stage. This lesson asks where the analyst should seek the evidence and why one class should be checked before another.

The teaching habit is **requirement-driven collection**. Avoid reducing the exercise to a list of favorite tools or a rule that one source class always comes first.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Explain the three source classes used in this course: **OSINT**, **commercial**, and **internal**.
2. Select appropriate source classes for a requirement and build a short collection plan that identifies collection order, the first action, and reasonable limits on scope.

**Mapped Proficiency Items:**
- K: 2.1.9 – Collection sources and methods (OSINT, commercial, internal)
- T: 2.1.9.1 – Identify appropriate collection source classes for a given requirement
- T: 2.1.9.2 – Plan collection against an intelligence requirement

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---|---|
| Introduction | 2 minutes | Connect the requirement to evidence selection. |
| Three source classes | 5 minutes | Define OSINT, commercial, and internal. |
| Collection order | 5 minutes | Show why the question determines what comes first. |
| A12 plan | 6 minutes | Build class, first action, follow-on, and limit. |
| Knowledge check | 4 minutes | Require a defensible plan rather than source recall only. |
| Summary | 1 minute | Reinforce requirement-driven collection. |
| **Total** | **23 minutes** | Allow minor flexibility for discussion. |

## Detailed Teaching Notes

### 1. Distinguish the Collection stage from source classes

Begin by reconnecting to Module 2.1.2. **Collection** is a lifecycle stage—the work of gathering material. **OSINT, commercial, and internal** describe broad classes of places from which that material may be obtained.

This distinction prevents learners from treating “Collection” as a fourth source class or answering a “where will you look?” question with a lifecycle label.

### 2. Explain the three classes by the questions they answer well

**OSINT** is public. It is useful for the public story: published reporting, public infrastructure context, openly available research, and public technical data.

**Commercial** is licensed or paid. It may provide proprietary enrichment, vendor assessments, premium sandboxing, or datasets not available openly.

**Internal** is the organization's own evidence: SIEM, EDR, network telemetry, tickets, incident notes, hunt output, and other internal records.

Avoid teaching that one class is inherently superior. Each has different coverage, access, latency, and evidentiary value.

### 3. Teach collection order as a function of the requirement

Use two contrasting questions.

**A12 internal question:** “What role did the update domain play in the activity on WS-JLEE?” Internal evidence is an early priority because only internal telemetry can establish what actually happened on the organization's host and network.

**Public-threat question:** “What public reporting exists about this delivery technique?” OSINT or commercial reporting may logically come first.

This comparison helps learners see that “internals first” is not a universal doctrine. It follows from the specific requirement.

### 4. Build the short collection plan

Use four fields:

1. Requirement.
2. Source class and order.
3. First collection action.
4. Limit or stop condition.

For A12, a good plan begins with relevant internal HTTP, DNS, host, or incident evidence. Public or commercial sources can follow if external context would reduce remaining uncertainty.

A scope limit might defer unrelated infrastructure pivots until the current requirement is answered or until the pivot justifies a separate requirement.

### 5. Keep the plan analytical rather than tool-centric

Compare:

- “Open the TIP and search the domain.”
- “Use internal telemetry to determine whether WS-JLEE resolved and contacted the domain during A12; then use external sources if broader context is still needed.”

The second is stronger because it states what the evidence should establish. A different tool could be substituted without changing the plan's purpose.

### 6. Introduce source quality without expanding the scope too far

Briefly discuss reliability, timeliness, coverage, authorization, corroboration, and collection cost. The objective is not to teach a complete source-evaluation framework; it is to prevent learners from treating source class alone as a quality rating.

## Common Student Challenges

| Misunderstanding | Why it occurs | Teaching response |
|---|---|---|
| Collection stage and source class are the same thing. | Both use the word “collection.” | Stage describes the work; class describes where the evidence comes from. |
| OSINT should always be first because it is easy to access. | Public search is familiar and low friction. | Ask which source can actually answer the requirement. |
| Internal should always be first. | The A12 example emphasizes internal evidence. | Contrast with a requirement that asks specifically for the public threat landscape. |
| A collection plan is a list of tools. | Tool names feel concrete. | Require the learner to state what evidence the first action is intended to establish. |
| Every discovered pivot should be collected immediately. | Analysts fear missing something important. | Record useful pivots, but tie expansion to the requirement or create a follow-on requirement. |

## Knowledge Check – Answer Key

### 1. The Collection lifecycle stage and a collection source class are the same thing. True or false? Explain.

**Expected answer:** False. Collection is the lifecycle activity of gathering evidence. OSINT, commercial, and internal are source classes from which evidence may be gathered.

### 2. “What happened with this domain on our network during A12?” Which source class should usually be an early priority, and why?

**Expected answer:** Internal, because the requirement asks about activity in the organization's environment and therefore requires internal telemetry or records.

**Teaching note:** External context can still be useful later; the answer is about order, not exclusivity.

### 3. Write a short A12 collection plan with first class, first action, follow-on class, and one scope limit.

**Expected answer:** Example: internal first; review A12 HTTP/DNS and host evidence; use OSINT or commercial reporting next if broader domain context remains useful; defer unrelated pivots unless they help answer the current requirement or justify a follow-on requirement.

**Assessment guidance:** Accept different source ordering when the learner can justify it from a clearly stated requirement.

## Summary and Transition

Close by reinforcing that collection is not “open the platform and see what is there.” It is a deliberate attempt to reduce uncertainty about a requirement. The 2.1 sequence ends here; **2.2.1 – Estimative language** moves into how analysts communicate judgments once the evidence has been collected and analyzed.
