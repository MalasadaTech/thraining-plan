# Module 2.1.6 – Ensuring Intelligence Is Actionable

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.6 B / C / C ; 2.1.6.1 3c / 4c / 4d  
- Hunter: 2.1.6 A / B / B ; 2.1.6.1 1a / 2b / 3c  
- SOC: 2.1.6 A / A / B ; 2.1.6.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the characteristics that make intelligence **actionable** for a recipient and common reasons a product fails that test.
2. Evaluate a piece of intelligence and explain whether the recipient can use it to make a timely decision or take a meaningful next step.

**Mapped Proficiency Items:**
- K: 2.1.6 – Ensuring intelligence is actionable
- T: 2.1.6.1 – Evaluate whether a piece of intelligence is actionable and explain why

## 1. Key Concepts

Intelligence becomes actionable when the recipient can **use the assessment to make a decision or take a meaningful next step**. The standard is not simply whether the product is interesting, accurate, or technically detailed. The question is whether it helps the intended recipient do something useful in the context of the requirement.

Actionability depends on the relationship among the requirement, the assessment, the recipient, and the timing. A useful way to evaluate a product is to ask five questions:

| Question | What to look for |
|---|---|
| **Does it answer the requirement?** | The product addresses the question the work was intended to answer. |
| **Is the recipient clear?** | The person or team who can use the answer is identifiable. |
| **Is the next decision or action specific enough?** | The product gives the recipient enough information to decide what to investigate, contain, prioritize, collect, or monitor. |
| **Is it timely?** | The answer arrives while the decision can still be made or influenced. |
| **Are the judgment and limits clear?** | The recipient can distinguish what the evidence supports from what remains uncertain. |

These are not a universal five-box policy. They are a practical test for this course: can the intended consumer use the intelligence responsibly and in time?

### Actionable does not always mean “issue a command”

An intelligence product can be actionable without telling the recipient exactly which button to press. Sometimes the useful next step is to investigate, collect additional evidence, change a priority, or decide that no immediate response is warranted.

For example, an assessment that the update domain likely supported attempted payload delivery could be actionable if it gives IR a reason to preserve relevant evidence and examine whether the file transfer completed. The value comes from improving the decision, not from adding a directive for its own sake.

### Why products fail the test

Common failure modes include:

- **The product answers a different question.** The reporting may be interesting but unrelated to the requirement.
- **The recipient cannot tell what the significance is.** A list of indicators may be useful data, but without context or judgment it may not tell anyone what to do with it.
- **The language is too vague.** “Be aware” or “monitor” may sound cautious but can leave the recipient without a meaningful next step.
- **The answer arrives too late.** A correct assessment can lose operational value after the relevant decision window closes.
- **The product hides uncertainty.** A recipient may act too aggressively or too cautiously if the limits of the judgment are unclear.

### Compare two A12 products

Consider the requirement from the previous lesson:

**What role did the update domain play in the activity on WS-JLEE during A12?**

A product such as this gives the recipient something useful:

> We assess that the update domain likely supported attempted payload delivery during A12. WS-JLEE requested `/update.exe` from that destination during the suspicious activity. IR should preserve and review the associated network, file, and process evidence to determine whether the transfer completed and whether the file executed.

Why is this actionable?

- It answers the requirement by explaining the domain's likely role.
- It identifies IR as a recipient who can use the answer.
- It gives a concrete next investigative step.
- It preserves the uncertainty around successful delivery and execution.

Now compare:

> New malicious activity has been reported. Be aware and monitor as needed.

That statement does not identify the relevant requirement, environment, evidence, or meaningful next decision. The problem is not that the wording is short; the problem is that the recipient cannot tell what the statement means for their situation.

### Actionability depends on the recipient and requirement

A product that is actionable for IR may not be actionable for leadership. IR can work host, file, and process details; leadership may need the risk implication, priority, and decision point instead. Module 2.1.7 addresses that tailoring in more detail.

Likewise, “actionable for a hunter” is a narrower question addressed later in the hunting curriculum. A product can support an IR decision even if it does not contain everything a hunter would need to build a hunt.

## 2. Knowledge Check

1. “Be aware and monitor as needed” is actionable intelligence because it tells the recipient to monitor. True or false? Explain.
2. Name three questions you can ask when evaluating whether an intelligence product is actionable.
3. Review the A12 assessment above. Identify the requirement it answers, the recipient who can act, the next step it supports, and one uncertainty the recipient still needs to keep in mind.

## 3. Summary

Actionable intelligence helps a specific recipient make a timely decision or take a meaningful next step. It should answer the requirement, make the significance clear, provide enough specificity for use, arrive in time, and communicate the limits of the judgment.

A product does not become actionable merely because it contains indicators or an instruction. The important test is whether the recipient can use the assessment responsibly in the situation the requirement was meant to address.


## 4. Related Modules

- 2.1.4 – Intelligence requirements
- 2.1.7 – Tailoring output to the audience
- 2.1.1 – Data, information, and intelligence
- 3.4.1 – Assessing CTI for hunt value

**Next:** [2.1.7 – Tailoring Output to the Audience](../07-tailoring-audience/student-guide.md).
