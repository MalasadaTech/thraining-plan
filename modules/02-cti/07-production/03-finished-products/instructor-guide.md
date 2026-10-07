# Instructor Guide – Module 2.7.3 – Creating Finished Intelligence Products

**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Purpose

Teach learners to turn analysis into a finished product whose judgments, evidence, uncertainty, and relevance are clear enough for another person to use.

## Standards Reference

Use [ODNI ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) as the supporting analytic-quality reference, especially for:
- source quality;
- uncertainty;
- facts vs assumptions/judgments;
- alternatives;
- customer relevance and implications;
- clear logical reasoning.

Do not present the course's five-part product structure as an official ICD template.

## Core Teaching Model

1. Requirement / question  
2. Key judgment  
3. Evidence / source basis  
4. Uncertainty / confidence  
5. Relevance / implications

### A12 correction

Preferred:

> We assess the update domain was likely used for **attempted payload delivery** in A12.

Evidence:

> `WS-JLEE` requested `/update.exe` from that destination during suspicious activity.

Gap:

> Successful download or execution is not established.

Do not simplify that to “confirmed payload host.”

## Activity / Actor Profile

Teach the learner to profile what is known:
- behavior;
- infrastructure;
- victim/targeting;
- temporal scope;
- assessments;
- attribution status;
- gaps.

An unresolved activity cluster is a legitimate profile. A nation-state is not required to make the profile complete.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Treats an IOC/TIP export as finished intelligence. | Ask what question it answers and where the judgment is. |
| Hides uncertainty to sound decisive. | Ask what evidence boundary the customer needs to know. |
| Copies vendor actor name as fact. | Preserve the source attribution and keep local attribution status separate. |
| Writes a dramatic impact statement. | Tie the implication directly to the supported judgment. |
| Treats formatting as quality. | Review analytic reasoning separately from presentation. |

## Demonstration Exercise — SILVER KITE

The SILVER KITE card is deliberately separate from A12. It exists because the approved task is **produce a threat actor profile**, while A12 correctly leaves actor identity unresolved. Do not let learners import SILVER KITE facts into A12.

### Evaluator criteria

A satisfactory profile should:

- identify SILVER KITE as the tracked actor supplied by the exercise rather than infer a sponsor or nationality;
- summarize the supported targeting pattern and information sought;
- distinguish observed behaviors from analytic judgments;
- describe KiteDoor and VPS use without turning either into unsupported ownership claims beyond the exercise evidence;
- include at least one bounded judgment with an explicit evidence basis and appropriate confidence;
- identify meaningful gaps, especially the absence of government sponsorship/nationality/legal-identity evidence;
- pass the lesson's finished-product review: requirement fit, source/evidence traceability, uncertainty, relevance, and clear reasoning.

For higher proficiency, expect tighter prioritization, more explicit alternative explanations, and cleaner explanation of why the evidence supports each judgment. Record demonstration/sign-off separately under the qualification standard.

## Knowledge Check – Answer Key

1. It contains data/observables but may lack a requirement, judgment, reasoning, uncertainty, and relevance.
2. Any four of: question, key judgment, evidence/source basis, uncertainty/confidence, relevance/implications.
3. Accept profiles that describe A12 behavior/infrastructure/victim, keep attribution unresolved, and state that successful download/execution is not established.

## References

- [ODNI – ICD 203](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)
- [ODNI – Objectivity and Analytic Standards](https://www.dni.gov/index.php/how-we-work/objectivity)
