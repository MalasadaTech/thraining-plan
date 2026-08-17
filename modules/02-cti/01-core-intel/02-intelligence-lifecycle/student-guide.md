# Module 2.1.2 – Intelligence Lifecycle

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.2 B / C / C ; 2.1.2.1 3c / 4c / 4c  
- Hunter: 2.1.2 A / B / B ; 2.1.2.1 1a / 2b / 3c  
- SOC: 2.1.2 A / A / A ; 2.1.2.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the six stages and the job of each.
2. Put a given activity in a stage, and say that the flow **loops**.

**Mapped Proficiency Items:**
- K: 2.1.2 – Intelligence lifecycle
- T: 2.1.2.1 – Identify the lifecycle stage of an activity and describe the flow

---

## 1. Key Concepts

CTI analysts run a **loop** so a question becomes a used answer. **2.1.1** was the layer (data / information / intelligence). This hour is **which job you are in**. You do **not** write a PIR (**2.1.4**). You do **not** pick OSINT vs commercial (**2.1.8**). You do **not** write the finished paper (**2.11**).

Shops rename stages. This course uses six. The work still has to happen even if your shop collapses two names.

| Stage | Job |
|-------|-----|
| **Planning and Direction** | Decide the question and what “done” looks like |
| **Collection** | Gather the raw material against that question |
| **Processing and Exploitation** | Turn raw intake into usable information |
| **Analysis and Production** | Judge what it means and write the answer |
| **Dissemination** | Get the answer to someone who can act |
| **Evaluation and Feedback** | Learn whether it was used and what to do next |

A stage is a **job**, not a folder. Putting a hash in a TIP is not analysis. A chat titled “INTEL” is not dissemination.

The flow **loops**. Analysis can send you back to collection. Feedback opens the next question. It is not a one-way slide.

**What good looks like:**

- **Stage:** SOC’s RFI “is this the payload host for **A12**?” is **Planning and Direction**. Pulling the A record for the update domain is **Collection**. Writing “we assess it is; treat it as such” is **Analysis and Production**.
- **Flow:** If analysis has no A record yet, you go **back to Collection**. You do not skip to dissemination of a guess.

---

## 2. Knowledge Check

1. Dissemination is the last stage and the work stops. True or false?
2. Name the six stages in order (the loop can still return).
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
- 2.1.8 – Collection sources
- 2.11 – Finished products / dissemination depth
