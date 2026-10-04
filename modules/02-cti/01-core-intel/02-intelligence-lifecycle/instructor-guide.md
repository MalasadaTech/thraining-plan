# Instructor Guide – Module 2.1.2 – Intelligence lifecycle

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.2 B / C / C ; 2.1.2.1 3c / 4c / 4c  
- Hunter: 2.1.2 A / B / B ; 2.1.2.1 1a / 2b / 3c  
- SOC: 2.1.2 A / A / A ; 2.1.2.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners understand the intelligence lifecycle as a set of related kinds of work that move a question toward a usable answer. Learners should be able to recognize the purpose of each stage, classify an activity by the work being performed, and explain why analysis or feedback may send the process back to an earlier stage.

**Context:** Module 2.1.1 introduced the distinction between recorded observations, contextualized information, and an intelligence assessment. This lesson places that analytical development inside the wider workflow that begins with a need and continues through delivery and feedback.

Use the A12 question throughout the lesson so the lifecycle is experienced as one connected process rather than six definitions to memorize. The learner should see what changes from stage to stage: the question is clarified, evidence is gathered and prepared, an assessment is developed, the answer is delivered, and the recipient's use of that answer creates feedback.

**Lesson scope:** Teach the purpose of the six stages and the iterative flow among them. Later modules add detail about intelligence requirements, collection source classes, audience tailoring, and finished products. Mention those later connections only when they help explain the current stage.

**Terminology note:** In **Processing and Exploitation**, *exploitation* means preparing collected material for analytical use. It does not mean exploiting a computer system.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Name the six stages of the intelligence lifecycle and explain the purpose of each.
2. Place a given activity in the appropriate stage and explain why the lifecycle can return to an earlier stage.

**Mapped Proficiency Items:**
- K: 2.1.2 – Intelligence lifecycle
- T: 2.1.2.1 – Identify the lifecycle stage of an activity and describe the flow

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---|---|
| Introduction | 2 minutes | Connect the lifecycle to the data-information-intelligence lesson. |
| Six stages | 6 minutes | Explain the purpose and characteristic work of each stage. |
| A12 walkthrough | 7 minutes | Follow one question through all six stages. |
| Iteration and overlap | 3 minutes | Show why analysis and feedback can return the process to earlier work. |
| Knowledge check and feedback | 4 minutes | Classify activities and listen for the learner's reasoning. |
| Summary and transition | 1 minute | Reinforce purpose-based classification and the iterative flow. |
| **Total** | **23 minutes** | Allow minor flexibility for discussion. |

## Detailed Teaching Notes

### 1. Start with the purpose of the lifecycle

Connect directly to Module 2.1.1. The previous lesson asked what an item contains: a recorded observation, contextualized information, or an analytic assessment. This lesson asks a different question: **what kind of work is happening right now, and what work should happen next?**

Explain that the lifecycle gives analysts and consumers a shared way to describe how a question becomes a delivered answer. The six stages are useful because each has a different purpose. Learners do not need to imagine perfectly separated handoffs between departments; one analyst or one platform may support several stages.

### 2. Explain the six stages as changes in purpose

Walk the stages in order, but describe the work each stage contributes.

**Planning and Direction** gives the effort a purpose. The analyst clarifies what the recipient needs to know and what evidence would be useful.

**Collection** obtains material relevant to that need. The important distinction is that the analyst is gathering evidence, not yet evaluating its meaning as the answer.

**Processing and Exploitation** makes collected material usable. Extraction, normalization, translation, organization, and storage can all belong here when their purpose is to prepare material for analysis.

**Analysis and Production** evaluates the available information against the question. This is where the analyst develops and communicates the judgment, including the reasoning and remaining uncertainty introduced in Module 2.1.1.

**Dissemination** places the assessment in the hands of the intended recipient through an appropriate form and channel. The purpose is successful delivery and use, not merely moving a file or copying an indicator.

**Evaluation and Feedback** asks whether the product answered the need and what remains unresolved. Feedback can close the immediate requirement, refine it, or create the next question.

### 3. Follow A12 through the lifecycle

Use the student guide's question: **What role did the update domain play in the activity on WS-JLEE?**

For Planning and Direction, ask learners what evidence could help answer that question. Accept several defensible answers rather than requiring one exact list.

For Collection, identify the act of obtaining the relevant HTTP, DNS, and incident records.

For Processing and Exploitation, focus on preparing those records so the analyst can compare them: extracting the domain, IP, timestamps, request path, and source host; normalizing fields; and organizing the observations.

For Analysis and Production, connect to the assessment from 2.1.1. The analyst interprets the request in the context of the suspicious activity and identifies the limits of what the evidence establishes.

For Dissemination, emphasize that SOC needs the assessment and its limits in a usable channel. A raw indicator list may contribute to the response, but it does not substitute for the analytic answer to the question.

For Evaluation and Feedback, use SOC's possible follow-up: **Did the requested file actually execute?** This demonstrates that feedback is not merely a satisfaction survey; it can reveal the next intelligence need.

### 4. Make the loop visible

The lifecycle is often shown as a circle, but learners may still imagine a rigid sequence. Give them two reasons the work loops.

First, **analysis can expose an evidence gap**. If the HTTP request is visible but transfer completion is not, the analyst can identify what evidence would address that gap and return to collection.

Second, **feedback can refine the question**. Once SOC understands the domain's likely delivery role, its operational need may shift to execution evidence. That begins another planning and collection effort.

Explain that returning to an earlier stage is normal analytical work. The value of the lifecycle is that it helps the team recognize why they are going back and what they need to accomplish there.

### 5. Classify by purpose, not by tool

Learners may try to classify the stage by where an activity happens. Use the TIP example to break that habit. Storing an extracted indicator may be processing. Comparing that indicator with other evidence to answer the question is analysis. Publishing the finished assessment through the same platform could be dissemination.

Ask, **What is the analyst trying to accomplish with this action?** That question usually identifies the stage more reliably than the tool name.

## Common Student Challenges

| Misunderstanding | Why it occurs | Teaching response |
|---|---|---|
| The six stages are a rigid one-way sequence. | Diagrams and ordered lists can look like a pipeline. | Use the missing-download-evidence example to show analysis creating a new collection need. |
| A tool or repository determines the lifecycle stage. | Learners associate certain platforms with “intel work.” | Classify the activity by its purpose: organize evidence, evaluate it, or deliver the assessment. |
| Processing and analysis are the same because both involve working with data. | Both stages can happen at the same workstation or in the same platform. | Contrast preparing the records for comparison with deciding what those records mean for the question. |
| Dissemination ends the lifecycle. | Delivery feels like completion. | Show how the recipient's use of the answer produces evaluation and may create a refined question. |
| Returning to collection means the first pass failed. | Learners may expect all evidence to be gathered before analysis starts. | Explain that analysis often reveals which missing evidence matters most. |

## Knowledge Check – Answer Key

### 1. An analyst has collected HTTP and DNS records for A12 and is extracting the domain, IP address, timestamps, and request path into a consistent format for comparison. Which lifecycle stage is this, and what makes it different from analysis?

**Expected answer:** Processing and Exploitation. The analyst is preparing collected material so it can be compared and examined. Analysis would evaluate that prepared information against the question and develop a judgment about what it means.

**Reasoning:** The purpose of the activity is organization and usability, not interpretation of the domain's role.

**Acceptable response:** The learner identifies Processing and Exploitation and explains the difference in terms of preparing versus evaluating the material. Exact wording is not required.

### 2. During analysis, the analyst realizes the available records cannot establish whether `/update.exe` was successfully downloaded. What should happen next in the lifecycle, and why?

**Expected answer:** The process should return to Planning and/or Collection to identify and obtain evidence that could address the gap. The analysis has shown what is still missing.

**Reasoning:** The lifecycle is iterative. A gap discovered during analysis can create a specific collection need rather than forcing the analyst to guess or stop.

**Acceptable response:** A learner may say “go back to Collection” if they clearly explain that additional evidence is needed. Stronger answers may mention refining the collection need before gathering it.

### 3. SOC receives the assessment about the update domain and asks whether the requested file executed on WS-JLEE. Which lifecycle stage produced that new need, and how does it affect the flow?

**Expected answer:** Evaluation and Feedback. The recipient's follow-up shows that the original assessment created or revealed a new intelligence need, which begins another cycle of planning, collection, processing, and analysis as appropriate.

**Reasoning:** Feedback tells the analyst whether the answer was sufficient and what question should be addressed next.

**Acceptable response:** The learner identifies Evaluation and Feedback and explains that the lifecycle loops into a new or refined question.

**Assessment guidance:** Evaluate whether learners can explain the purpose of the stage, not merely recall its name. For the task objective, a correct label with a defensible explanation of why the activity belongs there is stronger evidence of understanding than rote ordering alone.

## Summary and Transition

Close by following the change in purpose across the A12 example: define the question, gather the evidence, prepare it, interpret it, deliver the assessment, and learn what the recipient still needs. Then remind learners that the process can revisit earlier stages whenever analysis or feedback reveals a new requirement.

The next lesson, **2.1.3 — Intelligence types**, introduces the course's strategic, operational, tactical, and technical categories. Those types describe the kind of intelligence being requested or produced; they are not lifecycle stages.
