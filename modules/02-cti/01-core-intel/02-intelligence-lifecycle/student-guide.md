# Module 2.1.2 – Intelligence lifecycle

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.2 B / C / C ; 2.1.2.1 3c / 4c / 4c  
- Hunter: 2.1.2 A / B / B ; 2.1.2.1 1a / 2b / 3c  
- SOC: 2.1.2 A / A / A ; 2.1.2.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

## Learning Objectives

By the end of this module, you will be able to:

1. Name the six stages of the intelligence lifecycle and explain the purpose of each.
2. Place a given activity in the appropriate stage and explain why the lifecycle can return to an earlier stage.

**Mapped Proficiency Items:**
- K: 2.1.2 – Intelligence lifecycle
- T: 2.1.2.1 – Identify the lifecycle stage of an activity and describe the flow

## 1. Key Concepts

The intelligence lifecycle is a way to organize the work required to turn a question into an answer that someone can use. It helps an analyst recognize what kind of work is happening now, what should happen next, and when new evidence or feedback requires another pass through part of the process.

The stages are often drawn as a circle because intelligence work rarely moves through them once and stops. An analyst may discover during analysis that an important piece of evidence is missing and return to collection. A recipient may receive an assessment and ask a follow-up question, which begins another round of planning.

This course uses six stages:

| Stage | Purpose | Typical analyst work |
|---|---|---|
| **Planning and Direction** | Define the question and determine what is needed to answer it. | Clarify the request, identify the decision or information need, and determine what evidence would be useful. |
| **Collection** | Gather material relevant to the question. | Obtain records, logs, reporting, samples, or other needed observations. |
| **Processing and Exploitation** | Prepare collected material so it can be examined and compared. | Extract, normalize, organize, translate, enrich, or store relevant material in a usable form. |
| **Analysis and Production** | Evaluate the available information and develop the answer. | Compare evidence, test interpretations, identify gaps and uncertainty, and communicate an analytic judgment. |
| **Dissemination** | Deliver the intelligence to the people who need it in a usable form. | Provide the assessment through the appropriate report, briefing, ticket, platform, or other approved channel. |
| **Evaluation and Feedback** | Determine whether the intelligence answered the need and what should happen next. | Learn how the recipient used the answer, identify remaining questions, and refine future work. |

### Connecting the lifecycle to the previous lesson

Module 2.1.1 focused on the difference between data, information, and intelligence. Those concepts help explain what happens inside parts of the lifecycle, but they are not the lifecycle stages themselves.

Collection often gives the analyst recorded observations. Processing and exploitation makes those observations easier to understand and compare. Analysis and production evaluates the available information against a question and develops an intelligence assessment. Planning, dissemination, and feedback organize the work around that analytical development.

The boundaries are useful for understanding the work, but real investigations may overlap stages. For example, an analyst may process a newly collected log and immediately notice a gap that requires another collection step.

### What “exploitation” means here

In **Processing and Exploitation**, exploitation means making collected material usable for analysis. Depending on the source, that could include extracting indicators from a report, parsing a file, translating text, normalizing timestamps, or organizing records in a threat intelligence platform (TIP). It does not refer to exploiting a computer system.

### Following one question through the lifecycle

Continue with the A12 investigation from the previous lesson. SOC asks CTI:

**What role did the update domain play in the activity on WS-JLEE?**

**Planning and Direction.** The analyst clarifies the question and identifies what would help answer it. Useful evidence might include the workstation's network activity, domain-resolution records, relevant incident notes, and any other observations that connect the destination to the suspicious activity.

**Collection.** The analyst gathers the records needed for the question. For example, the analyst obtains the relevant HTTP and DNS activity associated with WS-JLEE and the A12 time frame.

**Processing and Exploitation.** The analyst prepares the collected material for use. Relevant fields may be extracted, timestamps normalized, and the domain, IP address, request path, and source host organized so that the activity can be compared across the incident.

**Analysis and Production.** The analyst evaluates the processed information against the original question. In the A12 example, the request for `/update.exe` during the suspicious activity supports an assessment that the update domain likely played a role in attempted payload delivery, while successful download and execution remain unresolved.

**Dissemination.** The assessment is delivered to SOC in a form and channel they can use. The important point is that the recipient receives the analytic answer and its supporting limits, rather than simply receiving the raw indicators that contributed to it.

**Evaluation and Feedback.** SOC may confirm that the assessment answered the immediate question, or it may identify another need. For example, the next question could be whether the requested file actually reached the workstation or executed. That feedback gives the analyst a new or refined question and starts another pass through the lifecycle.

### Why the lifecycle loops

The lifecycle is not a one-way assembly line. Each stage can reveal something that changes the work that follows.

Suppose the analyst reaches analysis and realizes that the available records show an HTTP request but do not show whether the transfer completed. The appropriate response is to identify that evidence gap and seek additional material that could address it. The work returns to collection because the analysis has shown what is still missing.

Feedback creates the same kind of loop. A useful assessment often answers one question while revealing the next. The lifecycle gives the team a common way to describe that movement without treating every return to an earlier stage as a failure or restart.

### Recognizing the stage in practice

When classifying an activity, focus on **what work is being performed**, not the tool, team name, or folder where the work happens. Adding an indicator to a TIP could be processing if the analyst is organizing collected material. Evaluating that indicator alongside other evidence to answer a question is analysis. Sending the resulting assessment to the recipient is dissemination.

The same platform can therefore support several lifecycle stages. The stage is determined by the purpose of the activity.

## 2. Knowledge Check

1. An analyst has collected HTTP and DNS records for A12 and is extracting the domain, IP address, timestamps, and request path into a consistent format for comparison. Which lifecycle stage is this, and what makes it different from analysis?
2. During analysis, the analyst realizes the available records cannot establish whether `/update.exe` was successfully downloaded. What should happen next in the lifecycle, and why?
3. SOC receives the assessment about the update domain and asks whether the requested file executed on WS-JLEE. Which lifecycle stage produced that new need, and how does it affect the flow?

## 3. Summary

The intelligence lifecycle organizes the work required to move from a question to a useful answer. Planning defines the need, collection gathers relevant material, processing prepares it, analysis develops the assessment, dissemination delivers it, and evaluation determines whether the need was met and what comes next.

The stages provide structure, but the process is iterative. Analysis can reveal new collection needs, and feedback can create the next question. Recognizing the purpose of the work at each point helps analysts decide what should happen next.


## 4. Related Modules

- 2.1.1 – Data, information, and intelligence (previous)
- 2.1.3 – Intelligence types
- 2.1.4 – Intelligence requirements
- 2.1.7 – Tailoring output to the audience
- 2.1.9 – Collection sources
- 2.7 – Finished intelligence products

**Next:** [2.1.3 – Intelligence Types](../03-intelligence-types/student-guide.md).
