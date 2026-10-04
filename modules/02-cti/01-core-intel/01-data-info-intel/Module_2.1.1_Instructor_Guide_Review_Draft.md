# Instructor Guide – Module 2.1.1 – Difference between data, information, and intelligence

**Status:** Review draft — aligned with the approved student guide  
**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**
- CTI: 2.1.1 B / C / C ; 2.1.1.1 3c / 4c / 4c
- Hunter: 2.1.1 A / B / B ; 2.1.1.1 1a / 2b / 3c
- SOC: 2.1.1 A / A / A ; 2.1.1.1 1a / 1a / 1a

**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners distinguish data, information, and intelligence by recognizing the context and analysis each contains. By the end, they should be able to explain their classification and identify what further work would make an item more useful to its recipient.

**Context (plain language):**

Learners have encountered logs, indicators, and reporting during the SOC material. This lesson introduces the CTI analyst's responsibility to evaluate those inputs and explain their significance. An address, a description of a workstation's activity, and an assessment of a domain's role can all contribute to the same investigation. The distinction becomes useful when learners can explain what each contributes and what remains unknown. Use the A12 example to make the progression visible: first establish context, then examine how the observations support an answer to the investigator's question. This prepares learners for the intelligence lifecycle in 2.1.2 and intelligence requirements in 2.1.4.

**Lesson scope:** This is a conceptual lesson on classification and reasoning. Use the supplied example and three knowledge-check questions. Formal likelihood and confidence terminology belongs in the later tradecraft lessons; acknowledge those connections briefly when they arise.

**Required materials:** The approved student guide and this instructor draft. The existing slide deck still reflects the earlier lesson and needs alignment before delivery with this revision. The lesson can be reviewed directly from the student guide.

## Learning Objectives

By the end of this module, learners will be able to:

1. Define data, information, and intelligence, and explain how context and analysis develop recorded observations into an assessment.
2. Categorize an example as data, information, or intelligence and explain their reasoning.

**Mapped Proficiency Items:**
- K: 2.1.1 – Difference between data, information, and intelligence
- T: 2.1.1.1 – Correctly categorize examples as data, information, or intelligence

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---|---|
| Introduction | 2 minutes | Connect the distinction to material analysts receive at work. |
| Definitions and context | 4 minutes | Explain what changes when observations are connected. |
| Assessment and A12 example | 7 minutes | Walk through the evidence, interpretation, and remaining gaps. |
| Uncertainty and classification | 3 minutes | Explain how a useful assessment can retain uncertainty. |
| Knowledge check and feedback | 5 minutes | Listen for reasoning and address misunderstandings. |
| Summary and transition | 1 minute | Connect this lesson to the intelligence lifecycle. |
| **Total** | **22 minutes** | Allow a few minutes of flexibility for discussion. |

## Detailed Teaching Notes

### 1. Introduce the practical problem

Begin with the situation in the student guide: an analyst receives indicators, logs, incident notes, and reports. Explain that the form of an item does not tell the analyst how much work has already been done with it. A report may contain recorded values, descriptions of events, and assessments in different paragraphs.

The practical reason for learning the terms is to recognize what an item contributes to a question. A learner who can explain that contribution will be better prepared to decide whether more context or analysis is needed.

### 2. Explain how context develops information

Use `203.0.113.88` as the starting point. It is a recorded address. Explain how knowing where it came from changes what the learner can say about it. An address extracted from an incident's connection records has a different context from the same address copied from an unrelated report.

Then connect the address to WS-JLEE and the request for `/update.exe` in A12. The learner can now describe an observed activity involving a particular workstation and destination. Emphasize how each added relationship contributes to understanding the event.

The three terms are a teaching model for examining the work contained in a statement. A label applies to the item as presented. For instance, a full log record may already provide enough context to describe an event, even though the IP address extracted from it is only one data value.

### 3. Make the analytic judgment visible

Return to the question in the student guide: **What role did the update domain play in the activity on WS-JLEE?** This gives the analysis a purpose. Explain that a useful answer requires evaluating how the request relates to the suspicious process activity in the incident.

Walk through the assessment in three parts. First, identify the observations: the workstation requested `/update.exe` from the domain during the suspicious activity. Second, explain the interpretation: the destination likely played a role in attempted payload delivery. Third, identify the limits: those observations alone do not establish that the file was successfully downloaded or executed.

The inference is plausible because the request is being considered in its incident context. Its support would be weaker if the same filename appeared in an ordinary software-maintenance session. That alternative helps learners understand why an address or filename alone cannot carry the assessment.

Keep the evidence boundary clear. A reference to a file in a request is evidence of the request. Establishing delivery or execution would require additional supporting evidence. This distinction lets the instructor explain what analysis contributes without quietly adding facts to A12.

### 4. Explain uncertainty and decision support

Learners may believe they must choose between a firm conclusion and saying nothing. Explain how the worked assessment offers a useful interpretation while identifying the questions that remain open. It gives the investigator a reason to examine the destination's delivery role and seek evidence of what happened after the request.

Clarify that an intelligence assessment can improve understanding, guide collection, or support prioritization. A recommendation may be useful when supported, but adding a command such as “block it” does not by itself make a statement intelligence.

Use the phrase “we assess” to point out where the author is expressing a judgment. The recipient should still be able to identify the evidence and reasoning behind that judgment. Explaining uncertainty is part of making the assessment usable.

### 5. Listen for understanding

During the knowledge check, listen for the work learners identify in each example: a recorded observation, added context, or an interpretation tied to a question. Accept equivalent explanations in ordinary language. If a learner selects a label without explaining it, ask them to identify the context or reasoning that supports the choice as feedback on that same question.

## Common Student Challenges

| Misunderstanding | Why it occurs | Teaching response |
|---|---|---|
| More detail automatically makes information intelligence. | The information example is richer than the original address, so the learner may equate detail with analysis. | Point to what the added details establish, then show how the assessment interprets the domain's role against the investigator's question. |
| “We assess” is what makes a statement intelligence. | The phrase is an easy visual cue in the example. | Have the learner explain the evidence-to-conclusion connection in their own words. The phrase signals a judgment; the reasoning supports it. |
| Uncertainty means the assessment is not ready to be useful. | Learners may associate a professional answer with certainty. | Use A12 to show how the investigator can act on a supported interpretation while seeking evidence of delivery and execution. |
| Intelligence must contain a prescribed action. | The recipient's decision and the analyst's assessment can look like the same task. | Explain how identifying a likely delivery role helps the recipient decide what to examine next. The assessment supports that decision without needing to prescribe a block. |

## Knowledge Check – Answer Key

### 1. You receive only the address `203.0.113.88`. How would you categorize it, and what context would you seek to understand its relevance?

**Expected answer:** Data. Useful context includes the source of the address, when it was observed, the associated host or domain, and what activity involved it.

**Reasoning:** The address is an individual recorded value. Connecting it to an event or situation would allow the analyst to explain its relevance.

**Acceptable response:** The learner identifies it as data and names at least one relevant context item, explaining how that item would help. They do not need to recite every possible field.

### 2. A log shows that WS-JLEE requested `/update.exe` from the update domain during A12. Explain why this is information and identify one conclusion the request alone cannot establish.

**Expected answer:** The statement connects a workstation, request, destination, and incident, so it describes an observed event. It does not by itself establish successful delivery, execution, or maliciousness of the requested file.

**Reasoning:** The statement provides context for what was observed. Determining the domain's role or the outcome of the request requires further evidence and evaluation.

**Acceptable response:** The learner identifies the contextual relationships and gives one defensible limit. If they infer execution merely because a filename appears in the request, revisit the difference between requesting a file and establishing what subsequently happened.

### 3. Review the assessment in the worked example. What analysis does it add to the observations, and how does its uncertainty affect the investigator's next step?

**Expected answer:** It interprets the update domain as likely involved in attempted payload delivery by considering the request alongside the suspicious activity. Because successful delivery and execution remain unresolved, the investigator should seek additional evidence addressing those outcomes.

**Reasoning:** The assessment answers a relevant question about the domain's role, explains its basis, and identifies a useful limit. That combination helps the recipient choose the next investigative step.

**Acceptable response:** The learner explains the inferred role, connects it to the supplied context, and identifies a next evidence need. Examples include supporting transfer records, relevant file events, or process evidence. These are proposed evidence sources to seek; their existence or contents have not been established in this example.

**Assessment guidance:** Use these criteria to judge the existing classification objective. Feedback should address the learner's reasoning. These discussion responses do not establish practical proficiency in conducting an investigation or producing a complete intelligence product.

## Summary and Transition

Close by tracing the development in ordinary language: the address provides a recorded value; connecting it to the workstation and request describes an event; evaluating that event against the investigator's question supports an assessment of the destination's role. The assessment remains useful because it explains both its reasoning and its limits.

The next lesson, **2.1.2 — Intelligence lifecycle**, places this analytical work within the wider process of developing and delivering intelligence.

## Instructor References

- [ODNI, ICD 203 — Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf). See the standards on expressing uncertainty and distinguishing underlying information from assumptions and judgments. Use these to explain why the lesson separates observations, interpretation, and remaining gaps. The directive supports those practices; the three-part classroom model is not presented as a quoted ODNI definition.
- **Approved student guide, Module 2.1.1.** Use its definitions, worked example, and three knowledge-check questions as the common teaching reference.
- **Module 2.2.1 — Estimative language.** This is the later curriculum connection for explaining likelihood terminology in more detail.
