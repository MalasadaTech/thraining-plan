# Instructor Guide – Module 2.1.7 – Tailoring Output to the Audience

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.7 B / C / C ; 2.1.7.1 3c / 4c / 4d  
- Hunter: 2.1.7 A / B / B ; 2.1.7.1 1a / 2b / 3c  
- SOC: 2.1.7 A / A / B ; 2.1.7.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Teach learners to shape the same supported assessment for different consumers by changing content emphasis, format, and level of detail while keeping the evidence and analytic judgment consistent.

**Context:** Module 2.1.6 asked whether a product is usable. This lesson adds the audience dimension: usable for **whom**, and for **what decision**?

Use leadership and IR / SOC as contrasting consumers because they make the tradeoff visible. Leadership needs the implication, owner, and decision-relevant uncertainty. IR and SOC need enough technical context to investigate and respond.

**Teaching principle:** Tailoring is not “make it shorter for executives.” It is matching the product to the consumer's decision and knowledge needs.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Explain why **audience analysis** should happen before an intelligence product is written or delivered.
2. Adjust the **content**, **format**, and **level of detail** of an intelligence product for a specified audience while preserving the underlying facts and analytic judgment.

**Mapped Proficiency Items:**
- K: 2.1.7 – Tailoring output to the audience
- T: 2.1.7.1 – Adjust an intelligence product for a specified audience

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---|---|
| Introduction | 2 minutes | Connect actionability to a specific consumer. |
| Audience analysis | 5 minutes | Consumer, decision, prior knowledge, needed evidence. |
| Content / format / detail | 4 minutes | Explain what can change and what must remain stable. |
| A12 two-audience exercise | 7 minutes | Compare leadership and IR / SOC versions. |
| Knowledge check | 4 minutes | Require learner-produced tailoring choices. |
| Summary | 1 minute | Reinforce same judgment, different presentation. |
| **Total** | **23 minutes** | Allow minor flexibility for discussion. |

## Detailed Teaching Notes

### 1. Start with the consumer's decision

Ask learners why one product might fail even when its facts are correct. Guide the discussion toward mismatch: the reader cannot use the shape or depth of the product for the decision they own.

Use four audience-analysis questions:

- Who is the consumer?
- What decision or action do they own?
- What do they already know?
- What facts, caveats, and details do they need to use the assessment correctly?

This makes tailoring a reasoning task rather than a formatting exercise.

### 2. Explain what changes and what does not

Three adjustable elements are:

- **Content:** which facts and implications are foregrounded;
- **Format:** how the product is structured or presented;
- **Level of detail:** how much technical evidence and context is included.

The underlying evidence and analytic judgment should remain consistent. The wording can change substantially as long as the assessment remains traceable to the same evidence and caveats.

### 3. Compare leadership and IR / SOC

Use the A12 assessment from the student guide.

For leadership, emphasize:
- what happened at a high level;
- why it matters;
- who owns the response;
- what important uncertainty remains.

For IR / SOC, retain or add:
- WS-JLEE;
- `/update.exe` and the update domain;
- relevant process/network/file context;
- the evidence gap and next investigative step.

Ask learners why each detail belongs in one version or both. Avoid reducing the exercise to “leadership gets one sentence, IR gets everything.” The right amount of detail depends on the decision.

### 4. Teach the two failure modes

**Overloading the reader:** Technical detail can obscure the decision point. A leadership product can be technically correct and still be poor if the implication is buried.

**Under-informing the reader:** A technical team may receive a polished summary that omits the host, behavior, or evidence needed to act.

The target is relevance plus sufficiency.

### 5. Separate tailoring from channel selection

Learners may jump to email, ticket, chat, or briefing. Acknowledge that delivery channel matters, but keep this lesson focused on what the product contains and how it is presented. Later dissemination material addresses the route in more detail.

## Common Student Challenges

| Misunderstanding | Why it occurs | Teaching response |
|---|---|---|
| Tailoring means changing the judgment for the audience. | Learners confuse persuasion with adaptation. | Compare the two A12 versions and identify the same judgment and uncertainty in both. |
| Leadership should receive no technical facts. | “Executive summary” is overgeneralized into “remove all evidence.” | Keep enough concrete context to support the implication without burying the decision. |
| IR should receive every raw artifact. | More detail feels safer. | Ask which details directly support investigation or response and which can remain in an appendix or source record. |
| Tailoring is only about length. | Short vs long is easy to visualize. | Use content, format, and detail as separate dimensions. |
| Choosing the delivery channel completes the exercise. | Dissemination and tailoring occur together in practice. | Return to the consumer's information need before discussing the route. |

## Knowledge Check – Answer Key

### 1. Tailoring means changing the analytic judgment so that it is more acceptable to leadership. True or false? Explain.

**Expected answer:** False. Tailoring changes presentation, emphasis, and detail, not the supported conclusion.

### 2. What three elements of a product can you adjust for a specified audience?

**Expected answer:** Content, format, and level of detail.

### 3. Using the A12 assessment, write one short leadership version and list two additional details for IR / SOC.

**Expected answer:** Leadership should preserve the core assessment, owner, and key uncertainty without unnecessary technical detail. IR / SOC should retain or add items such as WS-JLEE, `/update.exe`, the update domain, process/network context, or the specific evidence gap.

**Assessment guidance:** There is no single required sentence. Evaluate whether the learner preserved the supported judgment and made defensible audience choices.

## Summary and Transition

Close with the idea that good intelligence is not one canonical paragraph sent to everyone. The analysis stays stable; the presentation changes so each consumer can use it. The next lesson, **2.1.8 – Attribution**, shifts from how the assessment is presented to how strongly analysts can support claims about the actor or activity cluster behind it.
