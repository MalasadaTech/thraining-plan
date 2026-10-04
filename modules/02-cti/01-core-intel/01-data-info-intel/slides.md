# Module 2.1.1 – Difference between data, information, and intelligence  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.1.1 – Data, information, and intelligence  
**Subtitle:** From recorded observations to an analytic assessment  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Introduce the lesson as a practical distinction analysts use when deciding what an item actually tells them. The goal is not simply to memorize three definitions; learners should be able to explain what context or analysis is present and what work still remains.

---

### Slide 2 – Why the distinction matters
**Title:** What does this item actually tell you?

Analysts receive indicators, logs, incident notes, and reports in many forms.

The format alone does not tell you how much understanding the item contains. A report can include individual observations, descriptions of events, and analytic judgments in different places.

The useful question is: **what work has already been done with the evidence, and what is still needed?**

**Speaker Notes:**  
Connect this to material learners have already seen in the SOC track. The distinction matters because an analyst needs to recognize whether an item is merely recorded, placed in context, or evaluated against a question. Keep the discussion focused on the content of the statement rather than the label of the source or platform it came from.

---

### Slide 3 – Three layers of understanding
**Title:** Data, information, and intelligence

| Layer | What it contains | What the analyst contributes |
|---|---|---|
| **Data** | Individual recorded values or observations | Identifies what was recorded and where it came from |
| **Information** | Observations organized and placed in context | Connects relevant observations to describe an event or situation |
| **Intelligence** | An assessment that evaluates information against a relevant question | Explains what the evidence means, why the conclusion is supported, and what uncertainty remains |

**Speaker Notes:**  
Walk the table slowly. Emphasize that the distinction is about the work contained in the item as presented. A full log entry can provide contextual information even though an IP address extracted from that same log is only one data value.

---

### Slide 4 – Context changes what you can say
**Title:** From a recorded value to a meaningful description

`203.0.113.88`

By itself, the address tells you very little about why it matters.

Now add context:
- it appears in the A12 incident records;
- WS-JLEE communicated with that destination; and
- the HTTP log records a request for `/update.exe`.

You can now describe an observed event: **WS-JLEE requested a file from that destination during A12.**

**Speaker Notes:**  
Use the example to show what context contributes. The added relationships let the learner describe who did what, when, and where. Also point out the limit: the request does not by itself establish that the file was successfully delivered or executed.

---

### Slide 5 – Analysis answers a question
**Title:** Information becomes useful intelligence through evaluation

The investigator asks:

**What role did the update domain play in the activity on WS-JLEE?**

To answer, the analyst must do more than repeat the log. The analyst evaluates the request alongside the suspicious activity already associated with A12 and considers which interpretation the evidence supports.

A useful assessment makes three things visible:
1. **Observations** — what the evidence shows.
2. **Interpretation** — what those observations likely mean.
3. **Limits** — what the evidence does not yet establish.

**Speaker Notes:**  
Explain that the question gives the analysis a purpose. The judgment is not created by a phrase such as “we assess.” The reasoning that connects the observations to the conclusion is what matters.

---

### Slide 6 – Follow the A12 progression
**Title:** One case, three different levels of understanding

**Data**  
`203.0.113.88`

**Information**  
WS-JLEE requested `/update.exe` from the update domain during A12.

**Intelligence**  
We assess that the update domain was likely used for attempted payload delivery in A12. The request occurred during the suspicious activity, which supports examining the domain's delivery role. The available observations do not establish that the requested file was successfully downloaded or executed.

**Speaker Notes:**  
Trace the progression without treating it as a mechanical rename. Each step adds something substantive: first context, then evaluation against the investigator's question. Keep the evidence boundary clear; a request for a file is evidence of the request, not proof of delivery or execution.

---

### Slide 7 – Uncertainty does not make an assessment useless
**Title:** A useful assessment can still have open questions

The evidence can support a judgment while leaving some outcomes unresolved.

In A12:
- the request supports investigating a possible delivery role;
- successful download remains unconfirmed; and
- execution remains a separate question.

Stating those limits helps the recipient decide **what evidence to seek next**.

**Speaker Notes:**  
Learners may think a professional assessment must be certain. Use this example to show that clearly expressed uncertainty makes an assessment more usable, not less. A recommendation can be useful when supported, but a command or action statement is not what turns information into intelligence.

---

### Slide 8 – Knowledge Check
**Title:** Knowledge Check

1. You receive only the address `203.0.113.88`. How would you categorize it, and what context would you seek to understand its relevance?  
2. A log shows that WS-JLEE requested `/update.exe` from the update domain during A12. Explain why this is information and identify one conclusion the request alone cannot establish.  
3. Review the A12 assessment. What analysis does it add to the observations, and how does its uncertainty affect the investigator's next step?

**Speaker Notes:**  
Use the answer key in the instructor guide. Listen for reasoning, not just the selected label. A learner should be able to identify the context or analytic work that makes the example data, information, or intelligence.

---

### Slide 9 – Summary
**Title:** Recognize the work contained in the item

**Data** gives you recorded observations.  
**Information** connects those observations so you can describe a situation.  
**Intelligence** evaluates that information against a relevant question and explains its significance and limits.

When you review an item, ask: **What does this let me say, and what still needs to be established?**


**Speaker Notes:**  
Close by tracing the A12 example once more in ordinary language: address, contextualized request, assessment of the domain's likely role. Then transition to the next lesson, which places this analytical work within the wider intelligence process.

**Next:** [2.1.2 – Intelligence lifecycle](../02-intelligence-lifecycle/student-guide.md).
