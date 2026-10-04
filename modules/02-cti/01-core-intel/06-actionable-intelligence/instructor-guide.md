# Instructor Guide – Module 2.1.6 – Ensuring Intelligence Is Actionable

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.6 B / C / C ; 2.1.6.1 3c / 4c / 4d  
- Hunter: 2.1.6 A / B / B ; 2.1.6.1 1a / 2b / 3c  
- SOC: 2.1.6 A / A / B ; 2.1.6.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners evaluate whether an intelligence product gives its intended recipient enough relevant, timely, and appropriately qualified understanding to make a decision or take a meaningful next step.

**Context:** Module 2.1.4 defined the question the work exists to answer. This lesson evaluates the resulting product against that need. The focus is not whether the reporting is interesting or detailed; it is whether the intended consumer can use it.

Teach actionability as a relationship among **requirement, recipient, decision, timing, and uncertainty**. Avoid turning the lesson into a rigid compliance checklist or implying that every actionable product must issue a direct command.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Explain the characteristics that make intelligence **actionable** for a recipient and common reasons a product fails that test.
2. Evaluate a piece of intelligence and explain whether the recipient can use it to make a timely decision or take a meaningful next step.

**Mapped Proficiency Items:**
- K: 2.1.6 – Ensuring intelligence is actionable
- T: 2.1.6.1 – Evaluate whether a piece of intelligence is actionable and explain why

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---|---|
| Introduction | 2 minutes | Define actionability as usable decision support. |
| Evaluation questions | 6 minutes | Requirement, recipient, specificity, timing, limits. |
| Failure modes | 4 minutes | Explain why “interesting” and “be aware” are insufficient. |
| A12 comparison | 6 minutes | Evaluate a usable assessment and a vague one. |
| Knowledge check | 4 minutes | Require explanation, not pass/fail only. |
| Summary | 1 minute | Reinforce recipient-centered evaluation. |
| **Total** | **23 minutes** | Allow minor flexibility for discussion. |

## Detailed Teaching Notes

### 1. Define actionability in practical terms

Open by asking what a recipient should be able to do after reading an intelligence product. Useful answers include decide what to investigate, prioritize a response, seek more evidence, change posture, or decide not to act.

This makes the core point visible: actionability is about **usable decision support**, not simply the presence of a recommendation or IOC list.

### 2. Walk the five evaluation questions

Use the student guide's five questions as a diagnostic framework:

1. Does it answer the requirement?
2. Is the intended recipient clear?
3. Is the next decision or action specific enough?
4. Is it timely?
5. Are the judgment and limits clear?

Make clear that this is a course heuristic, not an invented local policy form.

For “specific enough,” explain that the product may support investigation or prioritization rather than prescribing a direct response. “Collect transfer evidence” can be actionable if that is the next decision-relevant step.

### 3. Explain the common failure modes

A product can fail because it answers the wrong question, because it gives the recipient facts without significance, because the next step is vague, because it arrives after the decision window, or because uncertainty is hidden.

Use “be aware and monitor” as an example of ambiguous language. Ask what the recipient is supposed to monitor, where, for what behavior, and in support of what decision. The exercise should show why specificity matters without teaching that the word “monitor” is inherently wrong.

### 4. Evaluate the A12 product

Use the requirement: **What role did the update domain play in the activity on WS-JLEE during A12?**

Walk the assessment in the student guide:

- It answers the requirement by assessing the domain's likely delivery role.
- It identifies IR as a recipient who can act.
- It supports a concrete evidence-preservation and investigation step.
- It makes clear that transfer completion and execution remain unresolved.

Then compare the generic “new malicious activity” statement. Ask learners which elements are missing and why the absence matters to the recipient.

### 5. Keep actionability separate from adjacent questions

Actionability is recipient- and requirement-dependent. Module 2.1.7 will show how the same underlying assessment changes shape for different readers.

Similarly, hunt value is a specialized downstream test. A product can be actionable for IR while lacking the observables or telemetry detail needed for a threat hunt. Do not let the hunting rubric replace the actionability question in this lesson.

## Common Student Challenges

| Misunderstanding | Why it occurs | Teaching response |
|---|---|---|
| Actionable means “contains an imperative verb.” | Direct commands are easy to recognize. | Ask whether the product actually improves the recipient's decision and whether the command is supported. |
| IOC-heavy reporting is automatically actionable. | Indicators look concrete and operational. | Ask what the indicators mean for this requirement and what decision they enable. |
| “Monitor” always fails. | Learners overlearn the vague-language example. | Explain that monitoring can be actionable when the target, behavior, owner, and decision purpose are clear. |
| More certainty makes a product more actionable. | Strong wording feels decisive. | Emphasize that honest limits improve decision quality; false certainty can make a product less usable. |
| Hunt value and actionability are the same test. | Both ask whether someone can use intelligence. | Identify the actual consumer and decision before evaluating the product. |

## Knowledge Check – Answer Key

### 1. “Be aware and monitor as needed” is actionable intelligence because it tells the recipient to monitor. True or false? Explain.

**Expected answer:** False as written. It does not identify what to monitor, why, in what environment, or what decision the monitoring supports.

**Teaching note:** Do not imply that monitoring can never be actionable. The failure is lack of specificity and context.

### 2. Name three questions you can ask when evaluating whether a product is actionable.

**Expected answer:** Any three of the course questions: requirement relevance, clear recipient, specific next decision/action, timeliness, or clear judgment and limits.

### 3. Review the A12 assessment. Identify the requirement, recipient, next step, and one remaining uncertainty.

**Expected answer:** Requirement: determine the update domain's role in A12. Recipient: IR. Next step: preserve/review network, file, and process evidence for transfer and execution. Uncertainty: whether `/update.exe` was successfully downloaded or executed.

**Assessment guidance:** Credit equivalent explanations that connect the product to a real decision or next investigative step.

## Summary and Transition

Close by reminding learners that “actionable” is not a synonym for “interesting,” “detailed,” or “commanding.” It means the intended consumer can use the product, in time, with a clear understanding of what the evidence supports. The next lesson, **2.1.7 – Tailoring output to the audience**, shows how the same assessment is shaped for different consumers.
