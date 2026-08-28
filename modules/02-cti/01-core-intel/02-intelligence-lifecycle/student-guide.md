# Module 2.1.2 – Intelligence lifecycle

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.2 B / C / C ; 2.1.2.1 3c / 4c / 4c  
- Hunter: 2.1.2 A / B / B ; 2.1.2.1 1a / 2b / 3c  
- SOC: 2.1.2 A / A / A ; 2.1.2.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the six stages of the intelligence lifecycle and the job of each.
2. Put a given activity in a stage, and say that the flow **loops**.

**Mapped Proficiency Items:**
- K: 2.1.2 – Intelligence lifecycle
- T: 2.1.2.1 – Identify the lifecycle stage of an activity and describe the flow

---

## 1. Key Concepts

CTI analysts name **which job they are in** so a question becomes a used answer — and so they know when to collect again instead of briefing a guess. That is daily intel work: a request for information (RFI) lands, and you have to say whether you are still gathering material, turning it into something usable, judging it, or delivering the answer. **2.1.1** taught the layer: data, information, intelligence. This lesson is the **loop** around that path. It is **not** how to write a priority intelligence requirement, or **PIR** (**2.1.4**). It is **not** source classes such as OSINT (**2.1.8**). It is **not** a finished paper (**2.11**).

Shops rename stages. This course uses six. The work still has to happen even if your shop collapses two names into one.

| Stage | Purpose | What you actually do |
|-------|---------|----------------------|
| **Planning and Direction** | Decide the question and what “done” looks like | Take the RFI. Say what evidence would answer it. Do not write PIR format here. |
| **Collection** | Gather the raw material against that question | Pull the record, sample, or log the question needs. Not every source class. |
| **Processing and Exploitation** | Turn raw intake into usable information | Normalize, extract, store (for example in a threat intelligence platform, or **TIP**). No judgment yet. This is not exploiting a host. |
| **Analysis and Production** | Judge what it means and write the answer | Assess against the question. Write the so-what. This is intelligence. |
| **Dissemination** | Get the answer to someone who can act | Deliver it to the consumer who asked. A chat title is not delivery. |
| **Evaluation and Feedback** | Learn whether it was used and what to do next | Did they act? Was it enough? That answer becomes the next question. |

**Collection** gathers **data**. **Processing and Exploitation** turns that data into **information**. **Analysis and Production** produces **intelligence**. Planning, dissemination, and evaluation are jobs around that path, not extra layers.

A stage is a **job**, not a folder. Putting a hash in a TIP is processing, not analysis. A chat titled “INTEL” is not dissemination.

The flow **loops**. Analysis can send you back to collection. Feedback opens the next question. It is not a one-way pipeline.

**What good looks like:**

- **Stage:** SOC’s RFI “is this the payload host for campaign **A12**?” is **Planning and Direction**. Pulling the A record for the update domain is **Collection**. Storing that IP in the TIP is **Processing and Exploitation**. Writing “we assess it is; treat it as such” is **Analysis and Production**. Getting that sentence to SOC is **Dissemination**.
- **Flow:** If analysis has no A record yet, you go **back to Collection**. You do not skip to dissemination of a guess. After SOC uses (or ignores) the answer, **Evaluation and Feedback** opens the next question.

Do not pick OSINT vs commercial vs internal here (**2.1.8**). Do not rewrite the answer for a different audience (**2.1.6**). Do not classify type (strategic / tactical) (**2.1.3**).

---

## 2. Knowledge Check

1. Dissemination is the last stage and the work stops. True or false?
2. Name the six stages of the intelligence lifecycle in order (the loop can still return).
3. “Pull the A record for the update domain against the **A12** RFI.” Which stage?

---

## 3. Summary

Six jobs in a loop. Name the stage. If you are missing material, collect again. Do not rename a folder and call it done.

**Next:** **2.1.3** Intelligence types.

---

## 4. Related modules

- 2.1.1 – Data, information, and intelligence (previous)
- 2.1.3 – Intelligence types
- 2.1.4 – Intelligence requirements
- 2.1.6 – Tailoring output to the audience
- 2.1.8 – Collection sources
- 2.11 – Finished products / dissemination depth
