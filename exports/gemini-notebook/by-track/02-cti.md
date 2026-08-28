# Track 2 — CTI

This is classroom fiction, not live org policy. If a lesson and the story bible disagree, **the bible wins**. Night Owl / Harbor in a lesson means **Pink River Dolphin (PRD)** / **Dixon, Yamada, & Associates (DYA)**.

---

# Lesson 2.1.1 – Difference between data, information, and intelligence

Source: `modules/02-cti/01-core-intel/01-data-info-intel/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.1 B / C / C ; 2.1.1.1 3c / 4c / 4c  
- Hunter: 2.1.1 A / B / B ; 2.1.1.1 1a / 2b / 3c  
- SOC: 2.1.1 A / A / A ; 2.1.1.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Define **data**, **information**, and **intelligence**, and say how a raw fact becomes a judged answer.
2. Categorize a given item as data, information, or intelligence.

**Mapped Proficiency Items:**
- K: 2.1.1 – Difference between data, information, and intelligence
- T: 2.1.1.1 – Correctly categorize examples as data, information, or intelligence

---

## 1. Key Concepts

A CTI analyst is asked to brief or hand off what landed on the desk — a hash, a log line, a feed item, a ticket question. Before you treat it as something someone should act on, you have to know **what layer** you have. That is the job in this lesson: name whether it is data, information, or intelligence, so you do not brief a raw field as a decision.

| Term | What it is | What it answers |
|------|------------|-----------------|
| **Data** | A raw fact as recorded | What was recorded? |
| **Information** | That fact with context (who / what / when / where) | What happened, in a story? |
| **Intelligence** | That story judged against a **question**, with a so-what | So what? What should someone do? |

Information describes. Intelligence **judges**. Renaming a feed “intel” does not make it so.

The path is a process, not a rename: **data → information → intelligence**. You add context, then you add a judgment against a question. The question can be informal (“is this domain the payload host for incident **A12**?”). How to write a Priority Intelligence Requirement (PIR) is **2.1.4**.

**What good looks like:** someone gives you one item. You name the layer. You do not write a finished paper.

- **Data:** `203.0.113.88`. Or the hash of Temp `invoice.vbs`. A field. No story.
- **Information:** That IP is the A record for the domain that served `update.exe`. Temp `invoice.vbs` sat on **WS-JLEE** / `jlee`. Context. No judgment.
- **Intelligence:** We assess that domain is the payload host for incident **A12**; treat it as such (block it, or keep working it). That answers a question and names a so-what. It is not a **2.11** paper.

If you are unsure, it is not intelligence yet.

You do not walk the lifecycle (**2.1.2**). You do not write a PIR (**2.1.4**). You do not write a finished product (**2.11**).

---

## 2. Knowledge Check

1. A hash with no other text is intelligence. True or false?
2. What must you add before information becomes intelligence?
3. “We assess that domain is the payload host for incident **A12**; treat it as such.” Data, information, or intelligence?

---

## 3. Summary

Data is a raw fact. Information is the story. Intelligence is a judged answer to a question. Sort the layer. Do not rename a feed.

**Next:** **2.1.2** Intelligence lifecycle.

---

## 4. Related modules

- 1.5 – Reporting
- 2.1.2 – Intelligence lifecycle
- 2.1.4 – Intelligence requirements
- 2.11 – Finished intelligence products

---

# Lesson 2.1.2 – Intelligence lifecycle

Source: `modules/02-cti/01-core-intel/02-intelligence-lifecycle/student-guide.md`

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

---

# Lesson 2.1.3 – Intelligence Types

Source: `modules/02-cti/01-core-intel/03-intelligence-types/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.3 B / C / C ; 2.1.3.1 3c / 4c / 4c  
- Hunter: 2.1.3 A / B / B ; 2.1.3.1 1a / 2b / 3c  
- SOC: 2.1.3 A / A / A ; 2.1.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the four types: **strategic**, **operational**, **tactical**, and **technical**.
2. Classify a product or requirement by type, and say why it is not the neighbor.

**Mapped Proficiency Items:**
- K: 2.1.3 – Intelligence types (strategic, operational, tactical, technical)
- T: 2.1.3.1 – Classify an intelligence product or requirement by type

---

## 1. Key Concepts

CTI analysts pick the **kind of answer** so the consumer gets a decision they can make. An alert responder needs what to do **now**. Leadership needs whether to change **posture**. If you hand the wrong kind, they cannot use it. That is the job in this lesson: name the type of the product or the requirement, and say why it is not the neighbor.

Type follows the **question**, not the file length. A **requirement** is the question you are asked to answer. A **product** is the answer you give. Both get a type. How to write a priority intelligence requirement (PIR) is **2.1.4**.

This course uses four types. **Technical** is its own type, not another word for tactical.

| Type | Question it answers | Neighbor — not this |
|------|---------------------|---------------------|
| **Strategic** | What should leadership change about risk or posture (months to years)? | **Operational** — a campaign run over days is not a program decision |
| **Operational** | How do we run this incident or hunt over days to weeks? | **Tactical** — “what do I do on this host *now*” is not the campaign picture |
| **Tactical** | What should a responder do **now** on this activity? | **Technical** — the observable is not the action |
| **Technical** | What are the observables we can detect or pivot on? | **Tactical** — a hash is not “isolate the host” |

A long PDF is not automatically strategic. Horizon (months vs days) is typical, not a substitute for the question. Type applies to **intelligence** (or the requirement that asks for it). A raw list of IPs and hashes is still **data**.

A lifecycle **stage** is not a type. You can collect technical observables in service of a tactical question. Stages are **2.1.2**. Audience format is **2.1.6**. Finished actor products are **2.11**.

**What good looks like:** someone gives you a product or a question. You name the type. You say why it is not the neighbor.

- Given: the A record `203.0.113.88` and `GET /update.exe` on port 8080 for the update domain. **Technical.** Not tactical: those are observables, not “isolate **WS-JLEE**.”
- Given: “Isolate **WS-JLEE**; treat the update domain as the **A12** payload host.” **Tactical.** Not technical: that sentence is the action now, not a hash dump.
- Given: “What should IR do now on **WS-JLEE**?” **Tactical** requirement. The question is the type, same as the product.

**Strategic** would be a posture line for leadership (no hash). **Operational** would be how the desk runs **A12** over the next days. Do not invent extra victims to fill those rows.

---

## 2. Knowledge Check

1. A long PDF is strategic because it is long. True or false?
2. Name the four types.
3. “Isolate **WS-JLEE**; treat the update domain as the **A12** payload host.” Type, and why not the neighbor?

---

## 3. Summary

Type follows the question. Strategic, operational, tactical, technical. Reject the neighbor. Length is not type. A stage is not a type.

**Next:** **2.1.4** Intelligence requirements.

---

## 4. Related modules

- 2.1.2 – Intelligence lifecycle (previous)
- 2.1.4 – Intelligence requirements
- 2.1.6 – Tailoring to audience (format, not type)
- 2.11 – Finished products

---

# Lesson 2.1.4 – Intelligence Requirements

Source: `modules/02-cti/01-core-intel/04-intelligence-requirements/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.4 B / C / C ; 2.1.4.1 3c / 4c / 4d ; 2.1.4.2 3c / 4c / 4d ; 2.1.4.3 3c / 4c / 4c  
- Hunter: 2.1.4 A / B / B ; 2.1.4.1 1a / 2b / 3c ; 2.1.4.2 1a / 2b / 3c ; 2.1.4.3 1a / 2b / 3c  
- SOC: 2.1.4 A / A / B ; 2.1.4.1 1a / 1a / 1a ; 2.1.4.2 1a / 1a / 1a ; 2.1.4.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why an intelligence requirement exists, and what a **Priority Intelligence Requirement (PIR)** is versus any other requirement.
2. Refine or translate a stakeholder question into a clear requirement, and say what collection and analysis it drives.

**Mapped Proficiency Items:**
- K: 2.1.4 – Intelligence requirements and Priority Intelligence Requirements (PIRs)
- T: 2.1.4.1 – Develop or refine intelligence requirements
- T: 2.1.4.2 – Translate stakeholder questions into clear intelligence requirements
- T: 2.1.4.3 – Explain how a given requirement drives analytic work

---

## 1. Key Concepts

CTI analysts write the **question the work exists to answer**. Without that question, collection becomes everything interesting, and analysis has no “done.” That is the job in this lesson: turn a messy ask into a requirement that names the decision, the evidence you need, and what you will not chase.

**2.1.3** named the kind of answer (strategic, operational, tactical, technical). This lesson is the question itself. You do **not** score whether a product is actionable (**2.1.5**). You do **not** pick OSINT versus commercial sources (**2.1.8**). You do **not** invent a shop PIR list (**2.12.1**).

| Idea | What it is |
|------|------------|
| **Purpose** | Focus collection and analysis on a decision someone can make |
| **PIR** | A *priority* requirement — leadership or the program ranked it |
| **Standing / ad-hoc** | Still requirements. They are not all PIRs. A **standing** requirement stays until leadership takes it off. An **ad-hoc** requirement is one-time, often from a Request for Information (**RFI**) or an incident |
| **Drives collection and analysis** | Names what you collect, what you analyze, and what you will **not** chase |

A clear requirement is a **question**, plus **whose decision**, plus **what you will not chase**. If your shop publishes PIR IDs, use those. Do not invent a PIR list for the classroom firm (**DYA**).

**What good looks like:**

- **Identify or refine:** A slogan is not a requirement. Name the decision, the object, and the window.
- **Translate:** Stakeholder: “Are we seeing them?” The desk is working **A12** — `wscript` launched encoded PowerShell on **WS-JLEE**, and an update domain is in the traffic. Refine: “Is the update domain the payload host for **A12** in this window?” Not a PIR ID you made up.
- **Drives work:** Collect the A record for that domain and the file already on the host. Analyze whether those answer the payload-host question. Do **not** chase the sibling domain on this requirement. That hop is later enrichment (**2.8**), not this question.

---

## 2. Knowledge Check

1. Every intelligence requirement is a PIR. True or false?
2. What does a PIR add that a standing or ad-hoc requirement may not have?
3. “Are we seeing them?” Translate it for **A12**, and name one thing the requirement tells you **not** to chase.

---

## 3. Summary

A requirement is the question the work exists to answer. A PIR is a ranked one. It drives what you collect, what you analyze, and what you skip. Do not invent the shop list.

**Next:** **2.1.5** Ensuring intelligence is actionable.

---

## 4. Related modules

- 2.1.3 – Intelligence types (previous)
- 2.1.5 – Actionable intelligence
- 2.1.8 – Collection source classes
- 2.12.1 – Local PIR list (obtain, do not invent)

---

# Lesson 2.1.5 – Ensuring Intelligence Is Actionable

Source: `modules/02-cti/01-core-intel/05-actionable-intelligence/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.5 B / C / C ; 2.1.5.1 3c / 4c / 4d  
- Hunter: 2.1.5 A / B / B ; 2.1.5.1 1a / 2b / 3c  
- SOC: 2.1.5 A / A / B ; 2.1.5.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name what makes intelligence **actionable**, and common reasons it fails.
2. Evaluate a piece and say **why** it is or is not actionable.

**Mapped Proficiency Items:**
- K: 2.1.5 – Ensuring intelligence is actionable
- T: 2.1.5.1 – Evaluate whether a piece of intelligence is actionable and explain why

---

## 1. Key Concepts

CTI analysts check whether a write-up lets someone **act**. An interesting finding is not enough. Someone has to be able to do a specific next step, in time, on the question the work was supposed to answer. That is the job in this lesson: say whether a piece is **actionable**, and why.

**Actionable** intelligence is a judged answer someone can use. It is not a slogan, and it is not a pile of raw facts. The **requirement** is the question the work exists to answer. This lesson scores the **product** — the write-up — against that question. **2.1.4** wrote the question. This lesson does not rewrite the product for a different audience (**2.1.6**). It does not write an actor profile (**2.11**). Whether a hunter can hunt from the report is a different test (**3.4.1**).

| Actionable when | Fails when |
|-----------------|------------|
| It **answers the named requirement** | It is interesting, but not the question |
| A **who** can act | No role is named |
| A **what** they do is specific | “Be aware” / “monitor” with no next step |
| It is still **in time** for that decision | The window already closed |
| You state **how sure** you are | A slogan with no caveat |

“Interesting” is not a pass. A hash dump with no judgment and no next step is still **data**, so it is not actionable intelligence.

**What good looks like:** someone gives you a product. You say whether it is actionable, and why. You do not rewrite it for a new reader.

- **Actionable:** “We assess the update domain is the payload host for **A12**. IR has **WS-JLEE**. Treat the domain as the payload host.” It answers the named question. It names who acts and what they do.
- **Not actionable:** “New activity in the news. Be aware.” It answers no requirement. It names no who. It gives no next step.

---

## 2. Knowledge Check

1. “Be aware” with no next step is actionable. True or false?
2. Name two reasons a product fails the actionable test.
3. “We assess the update domain is the **A12** payload host; IR has the host.” Actionable? Why?

---

## 3. Summary

Actionable intelligence answers the named question, names a who, and names a specific what. Slogans and “be aware” fail. This is not the hunt-useful test.

**Next:** **2.1.6** Tailoring output to the audience.

---

## 4. Related modules

- 2.1.4 – Intelligence requirements (previous)
- 2.1.6 – Tailoring to audience
- 2.1.1 – Data / information / intelligence
- 3.4.1 – Assessing CTI for hunt value (different test)

---

# Lesson 2.1.6 – Tailoring Output to the Audience

Source: `modules/02-cti/01-core-intel/06-tailoring-audience/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.6 B / C / C ; 2.1.6.1 3c / 4c / 4d  
- Hunter: 2.1.6 A / B / B ; 2.1.6.1 1a / 2b / 3c  
- SOC: 2.1.6 A / A / B ; 2.1.6.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why **audience analysis** matters before you write.
2. Adjust **content**, **format**, and **detail** for a named reader — same facts, different product.

**Mapped Proficiency Items:**
- K: 2.1.6 – Tailoring output to the audience
- T: 2.1.6.1 – Adjust an intelligence product for a specified audience

---

## 1. Key Concepts

CTI analysts change **how they say the same facts** so the person who will act can use them. Leadership needs a short so-what they can support. IR and SOC need host, file, and domain they can work. The assessment does not change to please the reader. That is the job in this lesson: name who is reading, then adjust **content**, **format**, and **detail**.

Type (**2.1.3**) is the kind of answer. Whether the product can be acted on is **2.1.5**. This lesson is **who is reading**. You do **not** change the judgment. You do **not** write the finished actor profile (**2.11.1.2**). You do **not** pick the SOC ticket type (**1.5**). Dissemination channels in depth are **2.11.2**.

This course uses one incident as fiction. **A12** is that case: user `jlee` on host **WS-JLEE** ran encoded PowerShell from a script. IR has the host. A file in Temp (`invoice.vbs`) and an update domain are in the case. You already have the facts. This lesson is two products from those facts, not a new plot.

**Audience analysis** is naming who will read the product and what they can do with it. Do that before you write. Leadership owns awareness and support; they cannot work a file hash. IR and SOC own the host and the next technical step; they need path and domain. If you skip that step, you send the wrong shape: a hash dump the lead cannot use, or a one-liner IR cannot work.

The people who will use the product are the **consumers**. In this lesson those two consumers are leadership and IR / SOC.

| You adjust | Meaning |
|------------|---------|
| **Content** | Which facts this person needs to act |
| **Format** | One sentence versus a short paragraph |
| **Detail** | Hash and path versus no hash |

The facts stay. The judgment stays. You cut or keep what that reader needs. Leadership gets a **one-liner**. They do **not** need the file hash. IR / SOC can have host, user, process, and Temp `invoice.vbs`.

**What good looks like:** someone names the reader. You write that product. You do not invent a second incident.

- **Leadership:** “**WS-JLEE** / `jlee` ran encoded PowerShell from a script; IR has the host.” No hash.
- **IR / SOC:** same case plus Temp `invoice.vbs` and the update domain. Same facts. More detail. Not a different plot.

Do not drop the assessment so the line sounds softer. Do not pick email versus ticket yet (**2.11.2**).

---

## 2. Knowledge Check

1. Tailoring means you change the judgment so leadership likes it. True or false?
2. What three things do you adjust for a named audience?
3. Same A12 facts: `jlee` on **WS-JLEE** ran encoded PowerShell from Temp `invoice.vbs`; IR has the host; the update domain is in the case. Write the leadership line (no hash) and what you add for IR.

---

## 3. Summary

Name who is reading before you write. Same facts. Different content, format, and detail. Leadership does not need the hash.

**Next:** **2.1.7** Attribution.

---

## 4. Related modules

- 2.1.5 – Actionable intelligence
- 2.1.7 – Attribution
- 2.11.2 – Dissemination channels
- 1.5 – SOC report types / routing

---

# Lesson 2.1.7 – Attribution

Source: `modules/02-cti/01-core-intel/07-attribution/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.7 B / C / C ; 2.1.7.1 3c / 4c / 4d  
- Hunter: 2.1.7 A / B / B ; 2.1.7.1 1a / 2b / 3c  
- SOC: 2.1.7 A / A / A ; 2.1.7.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why we attribute, why it is hard, and the difference between **activity group** and **nation-state**.
2. Assess a statement: claimed **confidence** versus the **evidence** present.

**Mapped Proficiency Items:**
- K: 2.1.7 – Attribution (purpose, confidence, types)
- T: 2.1.7.1 – Assess attribution statements for confidence and supporting evidence

---

## 1. Key Concepts

CTI analysts name **who or what cluster** sits behind activity — at a type and a confidence — so collection, hunt, and defense aim at the right cluster. That is the job in this lesson: read an attribution statement, say what type it claims, and whether the evidence earns that confidence. This is not a finished actor profile (**2.11.1.2**). Estimative wording depth is **2.2.1**. You do **not** invent a nation-state as fact.

| Idea | Meaning |
|------|---------|
| **Purpose** | Focus collection, hunt, and defense on the right cluster |
| **Challenges** | Shared hosting, false flags, vendor marketing names, one-blog claims |
| **Activity group** | A cluster of activity (infra, malware, ops). You can defend against a cluster without a country |
| **Nation-state** | A government sponsor. Needs more than a vendor label |

**Shared hosting** means more than one customer sat on the same IP or range, so that address is not “theirs.” A **false flag** is planted evidence meant to look like someone else. A vendor marketing name is a **label**, not proof. One blog is one source.

**Classroom confidence (this lesson only — not a live ODNI card):** **Low** means the evidence is thin or single-source. **Medium** means more than one independent line, and alternatives still remain. **High** means several independent lines, and alternatives are weak. If your shop publishes a confidence card, use it. Do not treat these three words as live policy.

A name on a PDF (“PRD APT”) is a **vendor label**, not proof of who they are.

**What good looks like:** someone gives you a claim. You name the type claimed, the confidence claimed, and whether the evidence present earns both.

- Given: “Vendor PDF says PRD APT, so this is a nation-state, high confidence.” **Fail.** Type claimed is nation-state. Evidence is a label. Confidence is too high. Honest read: **activity group / low** until independent evidence supports more.
- Given: incident **A12** — encoded PowerShell, an update domain, and `203.0.113.88`. Those facts can support an **activity cluster**. They do **not** by themselves prove a government.

Do not write the finished actor profile. Do not swap in likelihood words such as likely or almost certainly (**2.2.1**).

---

## 2. Knowledge Check

1. A vendor “APT” name is high-confidence nation-state attribution. True or false?
2. What is the difference between an activity group and a nation-state?
3. “Vendor PDF says PRD APT — high confidence nation-state.” Assess the claim.

---

## 3. Summary

Attribute the cluster you can defend. Name type and confidence. A vendor label is not high-confidence nation-state.

**Next:** **2.1.8** Collection sources and methods.

---

## 4. Related modules

- 2.1.6 – Tailoring to audience (previous)
- 2.1.8 – Collection sources
- 2.2.1 – Estimative language
- 2.11.1.2 – Actor profile (not this lesson)

---

# Lesson 2.1.8 – Collection sources and methods

Source: `modules/02-cti/01-core-intel/08-collection-sources/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.8 B / C / C ; 2.1.8.1 3c / 4c / 4c ; 2.1.8.2 3c / 4c / 4d  
- Hunter: 2.1.8 A / B / B ; 2.1.8.1 1a / 1a / 2b ; 2.1.8.2 1a / 1a / 2b  
- SOC: 2.1.8 A / A / B ; 2.1.8.1 1a / 1a / 1a ; 2.1.8.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the three **source classes**: OSINT, commercial, and internal.
2. Pick the class(es) for a requirement and **plan** collection: order, first action, and what you will not collect.

**Mapped Proficiency Items:**
- K: 2.1.8 – Collection sources and methods (OSINT, commercial, internal)
- T: 2.1.8.1 – Identify appropriate collection source classes for a given requirement
- T: 2.1.8.2 – Plan collection against an intelligence requirement

---

## 1. Key Concepts

CTI analysts choose **where** to collect so they can answer a requirement without skipping the logs they already have, and without treating every public blog as the first stop. A requirement names a question. This lesson names the three **source classes** — kinds of places you collect from — and what a short collection **plan** looks like.

**2.1.2** named collection as a **stage**: the lifecycle job of gathering. This lesson is **where** you gather from. You do not operate VirusTotal or a threat intelligence platform (**0.7** / **2.3** / **2.9**). You do not file the local request ticket (**2.12.2.1**). You do not rewrite the requirement (**2.1.4**).

| Class | What it is | Good for | Not enough when |
|-------|------------|----------|-----------------|
| **OSINT** (open-source intelligence) | Public reporting, public DNS, open blogs | The public story | The question is *our* presence / *our* logs |
| **Commercial** | Paid threat intelligence platform (TIP), premium sandbox, vendor intel | Packaged enrichment | You have not checked internals the question asked for |
| **Internal** | SIEM, EDR, Zeek, tickets, internal TIP, hunt output | “Are *we* seeing this?” | The question is only the public story |

Classes **stack**. You may use more than one. The **order** follows the requirement, not habit. The **method** in this lesson is that short plan: **source class**, **first action**, and **what you will not collect**.

**What good looks like:** someone gives you a requirement. You name the class(es) and write the short plan. You do not open a tool or file a ticket yet.

- Given: the classroom **A12** question — “Is this the payload host *here*?” First class: **internal**. First action: look in telemetry you already have (the Zeek A record, or the file from the host). Then OSINT or commercial if you still need the public story. Do not start with a public blog and skip internals.
- What you will **not** collect on this plan: a paid vendor account you do not have; a sibling domain the requirement did not ask for.

---

## 2. Knowledge Check

1. Collection as a lifecycle stage and a source class are the same thing. True or false?
2. Name the three source classes.
3. A requirement asks: is this the payload host *here*? Name the first class, the first action, and one thing you will not collect.

---

## 3. Summary

OSINT, commercial, and internal. Order follows the question. Internals first when the question is “are *we* seeing this?” A plan names the class, the first action, and what you will not collect.

**Next:** **2.2.1** Estimative language.

---

## 4. Related modules

- 2.1.7 – Attribution (previous)
- 2.2.1 – Estimative language
- 2.1.2 – Lifecycle collection stage
- 2.1.4 – Intelligence requirements
- 2.12.2.1 – Local collection request
- 0.7 / 2.3 / 2.9 – Tool survey / TIP / platform depth

---

# Lesson 2.2.1 – Estimative language

Source: `modules/02-cti/02-tradecraft/01-estimative-language/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.1 B / C / C ; 2.2.1.1 3c / 4c / 4c  
- Hunter: 2.2.1 A / B / B ; 2.2.1.1 1a / 2b / 3c  
- SOC: 2.2.1 A / A / A ; 2.2.1.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why estimative language exists, and use a classroom term for **likelihood**.
2. Write or interpret a judgment: the term is the likelihood, not the **confidence** from **2.1.7**.

**Mapped Proficiency Items:**
- K: 2.2.1 – Estimative language
- T: 2.2.1.1 – Use and interpret estimative language in analytic judgments

---

## 1. Key Concepts

CTI analysts write judgments that other people act on. Those people should not have to guess whether “could be” means *likely* or *remote*. That is the job in this lesson: pick a **likelihood** word so the next reader can compare products. **Confidence** (low / medium / high) is how good the evidence is (**2.1.7**). This lesson is how probable.

Estimative language exists to make uncertainty comparable. Do not hide behind “we believe.”

| Term | Meaning |
|------|---------|
| **almost certainly** | Near certain. You would be surprised if it were not so. |
| **highly likely** | Very probable. Strongly on the “is so” side. |
| **likely** | More probable than not. Clearly above even. |
| **even chance** | About as likely as not. |
| **unlikely** | More probable that it is not so. |
| **highly unlikely** | Very improbable. Strongly on the “is not” side. |
| **remote** | Almost no chance. |

These are **classroom terms for this lesson**. They are not a live ODNI (US Intelligence Community) card. If your shop publishes a term card, use that card. Do not invent percents as policy.

The estimative term is how probable the claim is. That is the uncertainty the term communicates. People sometimes call that term a **confidence level**. In this lesson that still means how probable — not the 2.1.7 evidence scale. You can write both in one line: “**likely**, medium confidence.” The first word is probability. The second is how good the sourcing is.

You do **not** assign Admiralty letters (**2.2.3**). You do **not** write the actor profile (**2.11**).

**What good looks like:** someone gives you a claim. You pick a classroom term, or you read the term that is already there. You do not leave the reader to guess.

- **Write:** “The update domain is **likely** the payload host for incident **A12**.” That is likelihood. Add confidence separately if you have it: “medium confidence.”
- **Interpret:** “It is **remote** that this is ordinary browsing.” That is very low likelihood — not “we have no idea.”
- **Fail:** “Could be PRD.” **PRD** is the course-fiction adversary, and “could be” is still not a term. The next reader cannot compare it to the next product.

---

## 2. Knowledge Check

1. “Likely” and “high confidence” mean the same thing. True or false?
2. Why does estimative language exist?
3. Write one **A12** sentence that uses a classroom term (not “could be”).

---

## 3. Summary

Pick a term. Likelihood is not confidence. “Could be” is not a term.

**Next:** **2.2.2** Structured analytic techniques.

---

## 4. Related modules

- 2.1.8 – Collection sources (previous)
- 2.2.2 – Structured analytic techniques
- 2.1.7 – Attribution confidence (not this lesson)
- 2.2.3 – Admiralty Code

---

# Lesson 2.2.2 – Structured Analytic Techniques

Source: `modules/02-cti/02-tradecraft/02-structured-techniques/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.2 B / C / C ; 2.2.2.1 3c / 4c / 4d  
- Hunter: 2.2.2 A / B / B ; 2.2.2.1 1a / 2b / 3c  
- SOC: 2.2.2 A / A / A ; 2.2.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why structured analytic techniques exist, and when to use **ACH** versus a **Key Assumptions Check**.
2. Apply one of those two to a given problem.

**Mapped Proficiency Items:**
- K: 2.2.2 – Structured analytic techniques
- T: 2.2.2.1 – Apply a structured analytic technique and select the right one for a scenario

---

## 1. Key Concepts

CTI analysts use a **named method** so a favorite story does not win by habit. A draft judgment often already has a preferred explanation. Before you publish, you pick a structured analytic technique that matches the problem and you apply it. That is the job in this lesson: slow the jump to one story, then show the work.

**2.2.1** was the likelihood word (how probable). This lesson is the **method**. It is **not** source letters (**2.2.3**). It is **not** a bias list (**2.2.4**). This lesson teaches two techniques only. Do not invent a third official technique as syllabus.

A **structured analytic technique** is a named way to test a call. You write the method down so someone else can see what you tested.

| Technique | Use when | What you do |
|-----------|----------|-------------|
| **Key Assumptions Check** | One claim is carrying the call | List the assumption. Say what would break it. |
| **Analysis of Competing Hypotheses (ACH)** | Two or more explanations are live | List the hypotheses. See which evidence **hurts** each one. |

**Purpose:** Make the jump to one story slower and inspectable. Pick the technique that matches the problem. Do not run both to fill time.

When you apply a technique in this course, the given is incident **A12** on `WS-JLEE`. You do not need the whole plot. Two facts are enough: a vendor PDF labels the cluster with an APT name, and the host fetched `update.exe` on port **8080**.

**What good looks like:**

- **Key Assumptions Check.** Given: a vendor PDF labels **A12** with an APT name, and the draft says that is who they are. **Assumption:** a vendor APT name is who they are. **Break:** the label is a PDF, not internals. You do not need a new technique to say that.
- **ACH.** Given: `GET /update.exe` on port **8080** to an update domain. **H1** = the domain is the payload host for **A12**. **H2** = ordinary browse. The `:8080` `GET /update.exe` **hurts** H2. You do not need a full matrix to name that.

Do not assign Admiralty letters. Do not name a bias. Do not write a 12-row ACH spreadsheet for this lesson.

---

## 2. Knowledge Check

1. You should always run ACH and a Key Assumptions Check on every product. True or false?
2. When do you pick a Key Assumptions Check instead of ACH?
3. For **A12**, name one assumption a Key Assumptions Check would test.

---

## 3. Summary

Use a named method. Pick **ACH** when two stories compete. Pick a **Key Assumptions Check** when one claim is carrying the call. Apply the one the problem needs.

**Next:** **2.2.3** Admiralty Code.

---

## 4. Related modules

- 2.2.1 – Estimative language (previous)
- 2.2.3 – Admiralty Code
- 2.2.4 – Cognitive biases
- 2.1.7 – Attribution

---

# Lesson 2.2.3 – Admiralty Code

Source: `modules/02-cti/02-tradecraft/03-admiralty-code/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.3 B / C / C ; 2.2.3.1 3c / 4c / 4d  
- Hunter: 2.2.3 A / B / B ; 2.2.3.1 1a / 2b / 3c  
- SOC: 2.2.3 A / A / B ; 2.2.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Rate **source reliability** (A–F) and **information credibility** (1–6).
2. Combine them into one Admiralty Code rating and say what it means.

**Mapped Proficiency Items:**
- K: 2.2.3 – Admiralty Code / source reliability and information credibility
- T: 2.2.3.1 – Assign Admiralty Code ratings and evaluate source reliability and credibility

---

## 1. Key Concepts

CTI analysts split **who said it** from **whether this piece of information checks out**. A report lands, and you have to write a letter for the source and a number for this claim. That is the job in this lesson: write both, so a reader does not treat “a shop we trust said it” as “this report is confirmed.” Estimative *likelihood* is **2.2.1**. Attribution *confidence* (low / medium / high) is **2.1.7**. This lesson is the **Admiralty Code**. You do **not** invent a shop scale. You do **not** rate a nation-state.

The **Admiralty Code** is two independent ratings written together: a **letter** for **source reliability**, and a **number** for **information credibility**.

Classroom scales (standard Admiralty). If your shop publishes a card, use it. Do not invent a new scale.

| Source reliability (letter) | Information credibility (number) |
|-----------------------------|----------------------------------|
| **A** completely reliable | **1** confirmed by other sources |
| **B** usually reliable | **2** probably true |
| **C** fairly reliable | **3** possibly true |
| **D** not usually reliable | **4** doubtful |
| **E** unreliable | **5** improbable |
| **F** reliability cannot be judged | **6** truth cannot be judged |

A rating is **letter + number** (example **B2**). The letter is the source. The number is this piece. Do not raise the number because the letter is high. Do not raise the letter because this claim looks true. **A** is not “true.” **1** is not “trusted source.”

**B2** means the source is usually reliable, and this piece is probably true. It is not confirmed, and it is not a stamp that every report from that source is true. “Probably true” on this scale is about this report, not the estimative word *likely* (**2.2.1**).

**What good looks like:**

- Given: an internal sensor log you pulled that matches other host evidence. **Assign:** source **B** (usually reliable — not **A** just because the sensor is yours). Information **1** if another source confirms the same fact, or **2** if it matches the host story but is not independently confirmed. **Explain:** usually reliable source; this piece is confirmed or probably true.
- Given: an anonymous public blog, one claim, no internals, title says INTEL. **Assign:** source **F** or **E**, information **5** or **6**. Do not write **B2** because the title said INTEL. **Explain:** you cannot judge the source (or it is unreliable); this claim is improbable or cannot be judged.

---

## 2. Knowledge Check

1. A reliable source means the information is confirmed. True or false?
2. What are the two parts of an Admiralty Code rating?
3. Anonymous blog, no internals, “block these now.” Letter + number, and why.

---

## 3. Summary

Letter is the source. Number is this piece. Write both. Do not mix them with “likely.” Do not mark a source **A1** just because it is yours.

**Next:** **2.2.4** Cognitive biases and mitigation.

---

## 4. Related modules

- 2.2.2 – Structured analytic techniques (previous)
- 2.2.4 – Cognitive biases
- 2.2.1 – Estimative language
- 2.1.7 – Attribution confidence

---

# Lesson 2.2.4 – Cognitive Biases and Mitigation

Source: `modules/02-cti/02-tradecraft/04-cognitive-biases/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.4 B / C / C ; 2.2.4.1 3c / 4c / 4d  
- Hunter: 2.2.4 A / B / B ; 2.2.4.1 1a / 2b / 3c  
- SOC: 2.2.4 A / A / A ; 2.2.4.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name common biases that warp a product, and what they do to it.
2. Spot a bias in a judgment and name a **mitigation** — a named method, not a pep talk.

**Mapped Proficiency Items:**
- K: 2.2.4 – Cognitive biases and mitigation
- T: 2.2.4.1 – Identify cognitive bias in a judgment and apply a mitigation technique

---

## 1. Key Concepts

CTI analysts write **judgments** other people act on. A first label, a favorite story, or the last incident can lock that product before the evidence has a fair look. The job in this lesson is to **name the bias** in the judgment and apply a **named method** so the product can still change. This is not Admiralty letters (**2.2.3**). It is not how to navigate a threat intelligence platform (**2.3.1**). You do **not** invent a third official method. You do **not** diagnose the author.

| Bias | What it looks like | What it does to the product |
|------|--------------------|-----------------------------|
| **Confirmation** | You keep the evidence that fits the first story | Alternatives never get a fair look |
| **Anchoring** | The first vendor name or first number sticks | Later internals cannot move the call |
| **Availability** | The last incident you remember becomes this one | A new event is treated as **A12** (this course’s classroom incident) with no shared host, malware, or infrastructure |

This lesson names **those three**. A longer psychology list is not required.

A **mitigation** is a method you run on the product. “Be more objective” is not a mitigation. Two methods this course already named (**2.2.2**) are enough here:

| Method | Use when | What you do |
|--------|----------|-------------|
| **Key Assumptions Check** | One claim is carrying the call | List the assumption; say what would break it |
| **Analysis of Competing Hypotheses (ACH)** | Two or more explanations are live | List the hypotheses; see which evidence **hurts** each one |

**What good looks like:**

- **Spot:** “Vendor PDF says PRD APT, so high nation-state.” **Anchoring** (and confirmation). **PRD APT** is a vendor label, not proof of who they are. The first label stuck.
- **Mitigate:** Key Assumptions Check — assumption: “vendor name = who they are.” That assumption breaks. You do not need a new method.

Do not tell the rest of the incident. Do not re-rate the source (**2.2.3**). Do not write an actor profile (**2.11**).

---

## 2. Knowledge Check

1. “Be more objective” is a mitigation technique. True or false?
2. Name two biases from this lesson.
3. “Vendor PDF says PRD APT, so high nation-state.” Bias, and one mitigation.

---

## 3. Summary

Name the bias in the product. Apply a method you can run. Do not pep-talk it away.

**Next:** **2.3.1** Internal threat intelligence platform.

---

## 4. Related modules

- 2.2.3 – Admiralty Code (previous)
- 2.2.2 – Structured analytic techniques (the mitigations)
- 2.3.1 – Internal TIP
- 2.1.7 – Attribution

---

# Lesson 2.3.1 – Internal Threat Intelligence Platform

Source: `modules/02-cti/03-tools/01-internal-tip/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.3.1 B / C / C ; 2.3.1.1 3c / 4c / 4d  
- Hunter: 2.3.1 A / B / B ; 2.3.1.1 1a / 2b / 3c  
- SOC: 2.3.1 A / A / B ; 2.3.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what the internal threat intelligence platform (TIP) is for, how to search it, and how it supports enrichment, analysis, and production.
2. Search, retrieve, and use it to support enrichment or analysis of an indicator or report you already have.

**Mapped Proficiency Items:**
- K: 2.3.1 – Internal threat intelligence platform
- T: 2.3.1.1 – Search, retrieve, and use the internal TIP for enrichment or analysis

---

## 1. Key Concepts

CTI analysts look up **what this organization already knows** about a hash, IP, domain, or report before they treat a public lookup as new. That store is the internal **threat intelligence platform (TIP)**. You search it so you do not miss a prior sighting, duplicate work, or invent a hit that is not there.

The TIP is **our** intel store. It is **not** VirusTotal, Silent Push, or any other public tool from **0.7**. Those tools answer a public question. This lesson is the internal check: do we already hold this? Advanced pivot is **2.9**. STIX authoring is **2.10**. The product name on the screen may differ. The jobs do not.

| Function | Job |
|----------|-----|
| **Store** | Indicators, reports, and sightings we already have |
| **Search / retrieve** | Find what we already know about a hash, IP, domain, or report |
| **Link** | Attach this observation to an existing object when one is there |

A **sighting** is a record that this organization saw the indicator.

**How to search.** You already have a value. Open the TIP. Search the field that matches that type — a hash in a hash search, a domain in a domain search. Open the object that comes back and read what is already recorded. If nothing comes back, write **not in TIP**. A search in the wrong field is not a miss.

**How the TIP supports the work.**

| Use | What it does |
|-----|----------------|
| **Enrichment** | Prior notes and related objects we already hold |
| **Analysis** | What we hold versus what a public tool would add. A miss is a **gap**, not benign. |
| **Production** | Cite the object you retrieved, or cite the miss, so the product shows internals were checked |

Do not author a STIX bundle here (**2.10**). Do not run a multi-hop pivot here (**2.9**).

**What good looks like:**

- **Search:** given a domain or file hash you already have. Write the object you **retrieved**, or **not in TIP**.
- **Use:** if a prior object exists, **link** this observation to it (a sighting) and cite it. If not, say the TIP added nothing. Do not invent a hit.

A TIP miss is a gap, not “benign.”

---

## 2. Knowledge Check

1. The internal TIP is the same as VirusTotal. True or false?
2. Name two core TIP functions.
3. You search a domain you already have. What two results can you write, and what must you not invent?

---

## 3. Summary

The internal TIP is this organization's store. Search the matching type. Retrieve the object or write **not in TIP**. Link a sighting when one exists. A miss is a gap, not benign. Do not invent a hit.

**Next:** **2.4.1** File similarity hashes.

---

## 4. Related modules

- 2.2.4 – Cognitive biases (previous)
- 2.4.1 – File similarity
- 0.7 – External tools
- 2.9 – Platform depth / pivot
- 2.10 – STIX authoring

---

# Lesson 2.4.1 – Hashing and Similarity Concepts

Source: `modules/02-cti/04-file-similarity/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.1 B / C / C ; 2.4.1.1 3c / 4c / 4d ; 2.4.1.2 3c / 4c / 4c  
- Hunter: 2.4.1 A / B / B ; 2.4.1.1 1a / 2b / 3c ; 2.4.1.2 1a / 2b / 3c  
- SOC: 2.4.1 A / A / B ; 2.4.1.1 1a / 1a / 2b ; 2.4.1.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what **imphash**, **ssdeep**, and **TLSH** are for, and use a similarity hash to name a related sample.
2. Extract and interpret **code-signing** fields from a file.

**Mapped Proficiency Items:**
- K: 2.4.1 – Hashing and similarity concepts
- T: 2.4.1.1 – Use file similarity hashes to identify related samples
- T: 2.4.1.2 – Extract and interpret certificate / code-signing information from a file

---

## 1. Key Concepts

A sample usually arrives as a file or a hash. **SHA256** tells you that exact file. A one-byte change makes MD5 / SHA look brand new. CTI still has to find a **cousin** of `update.exe` and say **who claimed the binary**. That is the job in this lesson: use a similarity hash to name a related sample, and read the code-signing fields. Cryptographic identity hashes (MD5 / SHA) are **1.2.7**. VirusTotal Relations is **2.9**. Classroom match thresholds are stand-ins, not shop policy.

| Tool | What it captures | What a match means |
|------|------------------|--------------------|
| **imphash** | The PE import table — which Windows libraries and functions the file lists. PE files only. | Same imphash → related compile or packer family. Not the same file. |
| **ssdeep** | A fuzzy digest of the file bytes. Score 0–100; **higher** is closer. | Near-duplicate when a few bytes change. |
| **TLSH** | A locality-sensitive digest of the file bytes. Distance; **lower** is closer. | Another fuzzy cousin. Do not read the number like ssdeep. |
| **Code-signing** | Signer, issuer, validity dates — or **unsigned**. | Who claimed the binary. Unsigned is a fact, not malware and not a country. |

**imphash** does not hash the whole file. Two files can share an imphash and still have different SHA256 values. Packed binaries often share the packer's import table, so the same imphash can mean the same packer, not the same family.

**ssdeep** and **TLSH** both look at bytes, not the import table. They score in **opposite** directions: a high ssdeep score is close; a low TLSH distance is close. This classroom treats **ssdeep 50 or higher** and **TLSH distance 30 or lower** as related. Those numbers are stand-ins. A weak ssdeep score is **not related** unless your shop card says otherwise. Do not invent a 90% cutoff as policy.

**Code-signing** is the signature **on the file**, not a TLS certificate (**1.2.4**). Extract signer, issuer, and valid dates as separate facts — do not swap issuer for signer. Empty signing fields means **unsigned**. Signed is not “trusted.” Unsigned is not “malware” and is not nation-state (**2.1.7**).

**What good looks like:**

- **Related sample:** given two PE files, same **imphash** as `update.exe`, different SHA256 → related compile (or packer family). Not the same file. Given ssdeep **20** against `update.exe` → **not related** on the classroom card.
- **Certificate:** extract signer / issuer / valid dates (or **unsigned**). Do not upgrade “unsigned” to nation-state (**2.1.7**).

Do not treat a SHA256 miss as “no cousin.” Do not open a Relations graph (**2.9**).

---

## 2. Knowledge Check

1. Same imphash means the two files are byte-identical. True or false?
2. What does ssdeep (or TLSH) find that SHA256 does not?
3. You extract “unsigned” from `update.exe`. What did you learn, and what must you **not** claim?

---

## 3. Summary

Similarity finds cousins when SHA256 does not match. imphash is the PE import table, not the whole file. ssdeep scores high when close; TLSH distance is low when close. Code-signing is who claimed the file. Unsigned is a fact, not attribution.

**Next:** **2.5.1** RDAP / WHOIS.

---

## 4. Related modules

- 2.3.1 – Internal TIP (previous)
- 2.5.1 – RDAP / WHOIS
- 1.2.7 – MD5 / SHA (identity hashes, not this lesson)
- 2.9 – VirusTotal Relations
- 2.1.7 – Attribution

---

# Lesson 2.5.1 – RDAP and WHOIS Concepts

Source: `modules/02-cti/05-rdap-whois/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.1 B / C / C ; 2.5.1.1 3c / 4c / 4c  
- Hunter: 2.5.1 A / B / B ; 2.5.1.1 2b / 3c / 4c  
- SOC: 2.5.1 A / A / B ; 2.5.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what WHOIS and RDAP are for, and how they differ.
2. Query a domain or IP and extract fields that help enrichment — without calling redaction “no intel.”

**Mapped Proficiency Items:**
- K: 2.5.1 – RDAP and WHOIS concepts
- T: 2.5.1.1 – Query RDAP/WHOIS and interpret fields for enrichment or attribution

---

## 1. Key Concepts

CTI analysts look up **registration** on a domain or an IP so they can see who registered the name, who holds the address block, and which nameservers and dates sit on the record. Before you add those facts to an indicator (**enrichment**) or name an actor (**attribution**), you have to read that lookup. That is the job in this lesson. **2.4.1** was file hashes. This lesson is registration. It is **not** SOA (**2.6**). It is **not** Silent Push PDNS (**0.7**).

**WHOIS** and **RDAP** both do the same job: look up registration for a **domain** or an **IP**. You are not asking DNS who runs the zone. You are asking the registry, registrar, or RIR who holds the name or the block.

| Idea | WHOIS | RDAP |
|------|-------|------|
| **Shape** | Free text. Layout changes by server. | JSON. Same fields, easier to parse. |
| **How you query** | Port 43 | HTTPS |
| **Order** | Fallback when RDAP has no record | Query RDAP first |

| Field | What you take |
|-------|----------------|
| **Registrar** | Who maintains the domain registration |
| **Nameservers** | Which NS names sit on the record. Distinctive NS is enrichment, not “this is a nation-state.” |
| **Created / updated** | When the record appeared or last changed |
| **Registrant** | Who registered the name, **if present**. **Redacted** is a fact. It is not “no intel.” It is not a country. |
| **IP CIDR / org** | The block and who holds it (often a cloud). That org is **not** the actor. |

**What good looks like:** someone gives you a domain or an IP. You query **RDAP** first. You use **WHOIS** if RDAP has no record. You write the fields that are there. You do not skip the lookup, and you do not turn redaction or a cloud org into an actor.

- Given: the update domain. Extract: nameservers `ns1.cdn-test.net` / `ns2.cdn-test.net`, created date, registrar. Write **registrant redacted** if that is what the lookup shows. Distinctive NS is enrichment. It is **not** “this is a nation-state.” Sibling `login-prd.net` with the **same NS** is a later hop you can *name* — the SOA read is **2.6**.
- Given: `203.0.113.88`. Extract: `203.0.113.0/24`, org **Example Cloud**. That is who holds the block. It is not “theirs.”
- Interpret: registration adds those fields to the indicator. It does not attribute an actor (**2.1.7**).

---

## 2. Knowledge Check

1. A redacted registrant means you have no intelligence. True or false?
2. Name one difference between WHOIS and RDAP.
3. You query the update domain and see `ns1.cdn-test.net`. What did you extract, and what must you **not** claim?

---

## 3. Summary

WHOIS and RDAP look up registration. Query RDAP first. Redacted is a fact. Distinctive NS is enrichment, not attribution. An IP org is who holds the block, not the actor.

**Next:** **2.6.1** Advanced DNS.

---

## 4. Related modules

- 2.4.1 – File similarity (previous)
- 2.6.1 – SOA / advanced DNS
- 0.7 – Silent Push survey
- 2.1.7 – Attribution

---

# Lesson 2.6.1 – Advanced DNS Concepts

Source: `modules/02-cti/06-advanced-dns/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.6.1 B / C / C ; 2.6.1.1 3c / 4c / 4d  
- Hunter: 2.6.1 B / C / C ; 2.6.1.1 2b / 3c / 4c  
- SOC: 2.6.1 A / A / B ; 2.6.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret an **SOA** record: primary nameserver, responsible mailbox, and serial.
2. Use published DNS records (SOA, NS, and related types) to enrich a name or pivot to a related one — not Zeek `dns` fields.

**Mapped Proficiency Items:**
- K: 2.6.1 – Advanced DNS concepts (SOA and other records of intel value)
- T: 2.6.1.1 – Interpret an SOA record and use advanced DNS data to enrich or pivot

---

## 1. Key Concepts

CTI analysts read **authoritative DNS** — the records a zone publishes — so they can see who runs a name and whether another name shares that control. An alert or an RFI often gives you a domain. Before you treat that domain as finished work, you read the zone: the SOA says who operates it, and the other records show who else is tied to it. That is the job in this lesson. It is **not** a Zeek `dns` log of a lookup on the wire. Wire lookups and DGA are **1.2.3**. Registration (WHOIS / RDAP) is **2.5**. Passive DNS in Silent Push is **0.7**.

**SOA** (Start of Authority) is the zone’s control record. You read three fields first.

| Field | What it is | What you take from it |
|-------|------------|------------------------|
| **MNAME** | Primary nameserver for the zone | Who is listed as the master for this zone |
| **RNAME** | Responsible mailbox, written as a DNS name | Who runs the zone. The first label is the local part, so `hostmaster.cdn-test.net` means `hostmaster` at `cdn-test.net`. That is an operator mailbox, not a country. |
| **Serial** | Zone serial — operators raise it when zone data changes | A change counter. It is **not** a file hash. |

**Other records** on the same zone show who else is tied to it. The intelligence value is “who else is tied to this zone,” not a full mail or service class.

| Record | What it names | Intel value |
|--------|---------------|-------------|
| **NS** | Who answers the zone | Same NS pair on two names can mean shared control. You already saw the pair on RDAP (**2.5**); this lesson uses it as a DNS fact. |
| **MX** | Who receives mail for the zone | Another hostname tied to the domain |
| **TXT** | Text the operator published | A unique token can be a pivot. Do not turn this into an email-security class. |
| **SRV** | Where a named service lives | Another hostname to look up |

**How this supports enrichment:** two names with the same NS pair, the same MNAME, or the same A address are candidates for related infrastructure. A distinctive TXT token can cluster names the same way. That is a pivot: you started with one name and you now have another to check. A shared cloud prefix is **not** the same thing. One A in `203.0.113.0/24` does not make the whole `/24` theirs.

**What good looks like:** someone gives you the zone records. You interpret the SOA. You name a related name only when the DNS facts support it. You do not claim shared hosting.

- **Interpret SOA.** Given: SOA on the update domain, RNAME `hostmaster.cdn-test.net`, a serial. **What that means:** the mailbox that runs the zone is `hostmaster` at `cdn-test.net`. That is who operates the zone. It is not a country. The serial is a zone-change counter, not a hash. Read MNAME as the primary nameserver; do not collapse it onto the RNAME.
- **Pivot.** Given: sibling `login-prd.net` with the **same NS pair** (`ns1.cdn-test.net` / `ns2.cdn-test.net`) and the same A `203.0.113.88`. **What you can say:** related name / sibling — same control and same address. **What you must not say:** the whole Example Cloud prefix `203.0.113.0/24` is theirs.

Do not open a Zeek `dns` log and call that this lesson (**1.2.3**). Do not re-query RDAP for registrar and created date (**2.5**). Do not use Silent Push history (**0.7**).

---

## 2. Knowledge Check

1. The SOA serial is a file hash. True or false?
2. What two SOA fields do you read first, and what does each one mean?
3. Same NS + same A on `login-prd.net` — what can you say, and what must you **not** say about `203.0.113.0/24`?

---

## 3. Summary

SOA says who runs the zone: MNAME is the primary nameserver, RNAME is the operator mailbox, and the serial is a change counter — not a hash. NS, MX, TXT, and SRV show who else is tied to the zone. Same NS and same A can be a sibling. A shared `/24` is not theirs.

**Next:** **2.7.1** ATT&CK for CTI.

---

## 4. Related modules

- 2.5.1 – RDAP / WHOIS (previous)
- 2.7.1 – ATT&CK for CTI
- 1.2.3 – Zeek DNS / DGA
- 0.7 – Silent Push
- 2.8.1 – Infrastructure pivot (later)

---

# Lesson 2.7.1 – MITRE ATT&CK for CTI Analysis and Reporting

Source: `modules/02-cti/07-frameworks/01-attck-cti/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- Hunter: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- SOC: 2.7.1 A / B / B ; 2.7.1.1 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Put ATT&CK on a **report or activity set** for a CTI product: tactic, technique or sub-technique, and the evidence that supports it.
2. Reject a **neighbor** ID that looks close but is not what this product shows.

**Mapped Proficiency Items:**
- K: 2.7.1 – MITRE ATT&CK for CTI analysis and reporting
- T: 2.7.1.1 – Map activity or reports to MITRE ATT&CK

---

## 1. Key Concepts

CTI analysts put ATT&CK IDs on a **product** so hunt and detection can reuse the same names. You extract named behaviors — tactics, techniques, and procedures (**TTPs**) — from a **report or activity set**, and you write only the IDs this product can support. That is the job in this lesson: a mapped line other desks can trust.

An **activity set** is more than one related event you are writing up together, such as a process launch and a later download. A **report** is the same idea on paper: vendor write-up, internal note, or your own product. You do not map a SOC queue category. You do not plan hunt coverage.

| Piece | What it is |
|-------|------------|
| **Tactic** | *Why* — the goal at that step (Execution, Command and Control, and so on) |
| **Technique or sub-technique** | *How* — the named way (`T1059` Command and Scripting Interpreter; `T1059.001` PowerShell) |
| **Evidence** | The field or sentence in **this** product that shows it (command line, parent, URI) |
| **Neighbor** | A nearby ID that could fit if you stretched. Reject it, and say why this product does not show it |

A finished CTI line is **tactic + technique or sub-technique + evidence**. If two IDs could fit, pick the primary for this product and reject the neighbor. An ID with no cited evidence is a slogan, not a map. Copying a vendor’s ID list without citing what *this* product shows is not a map either.

This lesson is **not** hunt coverage planning (**3.5**). It is **not** DTF pivot IDs (**2.7.4**). It is **not** a SOC alert category (**1.4.4**). It is **not** which TTPs apply to this shop (**2.8.2**). Diamond vertices are next (**2.7.2**).

**What good looks like:** someone gives you a report line or an activity set. You write the tactic, the ID, and the cite. You name the neighbor you are not using.

- **Given:** `wscript` launched encoded PowerShell (`-enc`). **Write:** Execution / **T1059.001** PowerShell. Cite `-enc` and the parent `wscript`. **Reject** Command and Control — this product does not show a beacon.
- **Given:** HTTP GET `/update.exe` on port 8080, and the product is the tool download. **Write:** Command and Control / **T1105** Ingress Tool Transfer. Cite the URI. **Reject** **T1059** — that ID is a command interpreter, not an HTTP GET.

Do not collapse the process and the download into one ID. Do not guess the next stage.

---

## 2. Knowledge Check

1. An ATT&CK ID with no cited evidence is a finished CTI map. True or false?
2. What three things must a CTI ATT&CK line have?
3. `wscript` launched encoded PowerShell (`-enc`). Name the tactic, the ID, and why it is not Command and Control.

---

## 3. Summary

Extract TTPs from a report or activity set onto ATT&CK IDs. A CTI line is tactic, technique or sub-technique, and evidence. Reject the neighbor this product does not show. Hunt planning, DTF, and SOC categories are other lessons.

**Next:** **2.7.2** Diamond Model for CTI.

---

## 4. Related modules

- 2.6.1 – Advanced DNS (previous)
- 2.7.2 – Diamond Model for CTI
- 0.6.1 – ATT&CK floor (one activity, not this product)
- 3.5 – Hunt planning with ATT&CK
- 2.8.2 – Which extracted TTPs apply here
- 1.4.4 – Alert categories

---

# Lesson 2.7.2 – Diamond Model Application in CTI

Source: `modules/02-cti/07-frameworks/02-diamond-cti/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.2 B / C / C ; 2.7.2.1 3c / 4c / 4d  
- Hunter: 2.7.2 B / C / C ; 2.7.2.1 3c / 4c / 4d  
- SOC: 2.7.2 A / B / B ; 2.7.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Fill the four Diamond vertices from a report or activity set.
2. Name the **weakest** vertex and reject a vendor-name **Adversary** fill.

**Mapped Proficiency Items:**
- K: 2.7.2 – Diamond Model application in CTI
- T: 2.7.2.1 – Apply the Diamond Model to an intelligence problem

---

## 1. Key Concepts

CTI analysts put the Diamond Model on a **report or activity set** so the product shows what they know and what they do not. Hunt and detection reuse that product. The job in this lesson is to fill the four vertices from the evidence you have, name the **weakest** vertex, and refuse to put a vendor APT name in **Adversary**. That is how this desk keeps attribution honest on the product. You do **not** write an actor profile here (**2.11**). You do **not** assign ATT&CK IDs (**2.7.1**).

The four vertices are **Adversary**, **Capability**, **Infrastructure**, and **Victim**. Fill each from the report or activity set in front of you. The weakest vertex is the one with the least evidence. On a CTI product, that gap **constrains the write-up**: you do not guess a group name to make the card look complete.

**A12** is the classroom activity set: encoded PowerShell on **WS-JLEE** (`jlee`) fetched `update.exe` from the update domain / `203.0.113.88`.

| Vertex | Fill with | A12 classroom |
|--------|-----------|----------------|
| **Adversary** | Who you can defend against — only if you have evidence | Unknown cluster — **not** a vendor label |
| **Capability** | What they used | Encoded PowerShell; `update.exe` |
| **Infrastructure** | Where they hosted it or talked through it | Update domain / `203.0.113.88` |
| **Victim** | Who was hit | **WS-JLEE** / `jlee` / DYA |

**Weakest** on A12 is **Adversary**. Internals support the other three vertices. A PDF name such as “PRD APT” does not fill Adversary. Write the unknown cluster and name Adversary as weakest.

Do not add the beacon POST to this product. That traffic is not the A12 activity set.

**What good looks like:** four fills + “weakest = Adversary.” Reject “Adversary = PRD APT.”

Kill Chain stages are the next lesson (**2.7.3**).

---

## 2. Knowledge Check

1. A vendor APT name fills the Adversary vertex. True or false?
2. Name the four vertices.
3. Fill Diamond for **A12** and name the weakest vertex.

---

## 3. Summary

Four vertices on the CTI product. Weakest named — that gap drops a who-claim. A vendor label is not Adversary.

**Next:** **2.7.3** Kill Chain for CTI.

---

## 4. Related modules

- 2.7.1 – ATT&CK for CTI (previous)
- 2.7.3 – Kill Chain for CTI
- 0.6.2 – Diamond Model
- 2.1.7 – Attribution
- 2.11 – Actor profile

---

# Lesson 2.7.3 – Cyber Kill Chain in Intelligence Analysis

Source: `modules/02-cti/07-frameworks/03-kill-chain-cti/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.3 B / C / C ; 2.7.3.1 3c / 4c / 4c  
- Hunter: 2.7.3 B / C / C ; 2.7.3.1 3c / 4c / 4c  
- SOC: 2.7.3 A / B / B ; 2.7.3.1 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use the seven Kill Chain stages to show attack **progression** on an intelligence product.
2. Identify the stage of observed or reported activity, reject the previous or next stage you did not see, and list **only supported** stages in the product.

**Mapped Proficiency Items:**
- K: 2.7.3 – Cyber Kill Chain in intelligence analysis
- T: 2.7.3.1 – Identify the Kill Chain stage of observed or reported activity

---

## 1. Key Concepts

CTI analysts put attack **progression** on a product — the write-up you issue — so the reader sees what was observed, and what was not. Hunt and IR use that list. A stage you invent becomes work on a step that is not in the evidence. That is the job in this lesson: name the stage of activity you have in a report or a set of events, and list only the stages you can cite.

The Lockheed Martin Cyber Kill Chain names seven stages of attack progression. You need those names to write the product. This lesson is **not** ATT&CK (**2.7.1**). It is **not** Diamond (**2.7.2**). It is **not** DTF (**2.7.4**). It is **not** hunt planning (**3.5**).

| Stage | Cite it when you have |
|-------|------------------------|
| **Reconnaissance** | Target research (scans, open-source lookup of the victim). Not “they must have looked.” |
| **Weaponization** | Building the payload. Victim logs almost never show this. |
| **Delivery** | The weapon arrived (mail, web, USB). |
| **Exploitation** | It executed against a vulnerability, or ran as the exploit. |
| **Installation** | Code or an implant is on the host. |
| **Command and Control** | A callback or control channel. |
| **Actions on Objectives** | The goal (theft, encryption, and so on). |

A **supported** stage is one you can cite from the report or the activity. The product lists **only** those stages. Do not fill the other five because the chain “must” have happened. Reject the previous or next stage you did not see. Reject an **unobserved** stage — Reconnaissance you did not see, Weaponization you did not see, Command and Control with no callback.

**What good looks like:** someone gives you observed or reported activity. You name the stage, say why it is not the neighbor, and the product lists only what you can cite.

- Given: `wscript.exe` (Temp `invoice.vbs`) → `powershell.exe -enc …`. **Stage:** **Installation**. Cite the process. **Not** Command and Control — there is no beacon in that activity. **Delivery** of the vbs only if the product also has it arriving.
- Given: `GET /update.exe` on port 8080. **Stage:** **Installation** of the payload, or **Command and Control** if that GET is the control channel. **Not** Reconnaissance — fetching a payload is not target research.
- Product line: list **only** stages you can cite. Do **not** write Reconnaissance because “they must have scanned.”

Do not map ATT&CK IDs (**2.7.1**). Do not fill Diamond vertices (**2.7.2**). Do not pick a DTF pivot (**2.7.4**).

---

## 2. Knowledge Check

1. You should list all seven stages on every product. True or false?
2. `GET /update.exe` on port 8080. Is that Reconnaissance? Why or why not?
3. `wscript` → `-enc`. Stage, and why not the neighbor?

---

## 3. Summary

Seven stages. Only what you can cite. Reject the previous or next stage you did not see. Do not invent Reconnaissance.

**Next:** **2.7.4** Defender’s ThreatMesh Framework (DTF).

---

## 4. Related modules

- 2.7.2 – Diamond Model application in CTI
- 2.7.4 – Defender’s ThreatMesh Framework (DTF)
- 2.7.1 – MITRE ATT&CK for CTI analysis and reporting
- 0.6.3 – Cyber Kill Chain (shared floor)

---

# Lesson 2.7.4 – MalasadaTech Defender's ThreatMesh Framework (DTF)

Source: `modules/02-cti/07-frameworks/04-dtf/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.4 B / C / C ; 2.7.4.1 3c / 4c / 4d ; 2.7.4.2 3c / 4c / 4d ; 2.7.4.3 3c / 4c / 4c  
- Hunter: 2.7.4 A / B / B ; 2.7.4.1 1a / 2b / 3c ; 2.7.4.2 1a / 2b / 3c ; 2.7.4.3 1a / 2b / 3c  
- SOC: 2.7.4 A / A / B ; 2.7.4.1 1a / 1a / 2b ; 2.7.4.2 1a / 1a / 2b ; 2.7.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why DTF exists, and pick a **real** pivot tactic (PTA) and pivot (P) ID from a known-bad seed.
2. Cite the shared characteristic, reject the weak neighbor, name the **next lookup**, and say how DTF differs from ATT&CK, Diamond, and Kill Chain.

**Mapped Proficiency Items:**
- K: 2.7.4 – Defender’s ThreatMesh Framework (DTF) for infrastructure discovery
- T: 2.7.4.1 – Apply DTF: select a pivot tactic and pivot from a seed and reject the weak neighbor
- T: 2.7.4.2 – Use a selected DTF pivot to guide the next enrichment or lookup
- T: 2.7.4.3 – Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain

---

## 1. Key Concepts

CTI analysts start from a **known-bad seed** — a domain, IP, certificate, or page they already treat as adversary infrastructure. The job is to find **more** of that infrastructure and write the pivot so another analyst can run it again. That is the job in this lesson: pick a real DTF ID, cite the shared characteristic, reject the weak neighbor, and name the next lookup. DTF does **not** score the pivot. It does **not** replace ATT&CK, Diamond, or Kill Chain.

**DTF** (Defender's ThreatMesh Framework) is MalasadaTech's **defender discovery** matrix. It is shaped like ATT&CK: **pivot tactics** are columns; **pivots** are the named cells. The job is discovery, not behavior.

| Tactic | Name | Pivot on |
|--------|------|----------|
| **PTA0001** | Domain | Registration, domain string, DNS |
| **PTA0002** | IP | Reverse lookup, proximity, AS |
| **PTA0003** | SSL | Issuer / SAN — only if a cert card exists |
| **PTA0004** | Application | HTTP title / resources — only if a page card exists |

Pivots nest. **P0101** is Registration. **P0101.010** is Registration: Name Server. Use only IDs that exist in DTF. Do not invent a `P` code. Do not teach every P-code. Do not assign ATT&CK T-IDs here (**2.7.1**). The generic hop sentence without DTF IDs is **2.8.1**.

**Seed:** the update domain and its A record `203.0.113.88`. Candidate sibling `login-prd.net`. Name server `ns1.cdn-test.net`.

DTF finds related infrastructure when the candidate **shares a characteristic** with the seed: registration, domain string, DNS, IP, SSL, or HTTP. Same name server or same A can be a take when that fact is distinctive. A whole cloud `/24` is coincidence, not a take.

| Evidence | ID | Call |
|----------|-----|------|
| Same NS | **PTA0001 / P0101.010** (Registration: Name Server) | Take if the NS is distinctive |
| Same A | **PTA0001 / P0103.003** (DNS: IP Address) | Take → sibling |
| Whole `203.0.113.0/24` | **PTA0002 / P0202** (Proximity) | **Reject** — shared cloud |
| Vendor APT / T-ID | — | **No DTF ID** |

The selected P-ID **names** the next lookup. It does not run that tool in this lesson.

| Selected pivot | Next lookup to name |
|----------------|---------------------|
| **P0101.010** Name Server | RDAP / WHOIS for that NS (**2.5**) |
| **P0103.004** DNS: SOA RName | SOA RNAME (**2.6**) |
| **P0103.003** DNS: IP Address | Passive DNS / other names on that A (**0.7** / **2.9.3**) |

**Complement:** ATT&CK labels **behavior**. Diamond shows **know / don’t-know**. Kill Chain shows **progression**. DTF records **discovery** pivots. Same matrix shape. Different job.

**What good looks like:** someone gives you a seed and a shared fact. You write the **DTF ID line**. You do not tell the rest of the incident.

`seed | PTA | P-ID | characteristic | candidate | why not coincidence`

- Given: same NS `ns1.cdn-test.net` on the update domain and `login-prd.net`. **Take:** **PTA0001 / P0101.010**. Cite the distinctive name server (not a public resolver). Candidate `login-prd.net`. Next lookup: RDAP for that NS.
- Given: both names resolve to `203.0.113.88`. **Take:** **PTA0001 / P0103.003**. Next lookup: passive DNS / other names on that A.
- Given: whole `203.0.113.0/24`. **Reject** **P0202**. Shared cloud is not “theirs.”

Do not score the line. Do not invent `P9999`. Do not write T1059 as a DTF pivot.

---

## 2. Knowledge Check

1. DTF replaces ATT&CK. True or false?
2. Same NS on the update domain and `login-prd.net`. Which PTA / P-ID, or reject?
3. Whole `203.0.113.0/24`. Take or reject, and what is the next lookup if you took same-A instead?

---

## 3. Summary

DTF is defender discovery. Use a real PTA and P ID. Cite the characteristic. Reject shared cloud. Name the next lookup. DTF does not replace ATT&CK, Diamond, or Kill Chain.

**Next:** **2.8.1** Infrastructure hop sentence.

---

## 4. Related modules

- 2.7.3 – Cyber Kill Chain in intelligence analysis (previous)
- 2.8.1 – Generic hop sentence (no P-ID)
- 2.5 / 2.6 / 0.7 – The lookups DTF names
- [Defender's ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework)

---

# Lesson 2.8.1 – Identifying additional adversary infrastructure from seed indicators

Source: `modules/02-cti/08-enrichment/01-infra-pivot/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4d  
- Hunter: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4d  
- SOC: 2.8.1 A / B / B ; 2.8.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Write a **hop sentence** from a seed: what you share, what you found, and why it is not coincidence.
2. Name a common source class for that hop — without re-teaching RDAP, SOA, Silent Push, or VirusTotal.

**Mapped Proficiency Items:**
- K: 2.8.1 – Identifying additional adversary infrastructure from seed indicators
- T: 2.8.1.1 – Pivot from a seed indicator to additional adversary infrastructure

---

## 1. Key Concepts

CTI analysts start from a **seed** they already have — a domain, an IP, or another indicator from an RFI, a report, or an incident. One seed is rarely the whole picture. The job in this lesson is to hop from that seed to other **adversary infrastructure**: write what you share, what you found, and why it is not coincidence. You **select and record** enrichment from sources already taught. You do not re-teach the tools (**0.7** / **2.9**). You do not write a DTF ID (**2.7.4**).

A **seed** is the indicator you already have. To **pivot** (also: hop) is to use a **shared characteristic** of that seed to find more infrastructure. The extra name or IP you find is a **candidate**. The product is a **hop sentence** — the four-part line you record — not a tool demo and not a DTF P-ID (the PTA/P code from **2.7.4**).

**Hop sentence:** `seed | shared characteristic | candidate | why not coincidence`

The shared characteristic has to be distinctive enough that two names sharing it is not luck. A public nameserver, a shared cloud range, or an uncited vendor label is coincidence. Stop after one cited hop. Do not turn this lesson into campaign tracking (**2.8.3**) or a TTP extract (**2.8.2**).

**Common source classes.** Name the class and what you hope to learn. You do not operate these tools here.

| Source class | What you hope to learn |
|--------------|------------------------|
| **Registration** | Nameservers, registrar, created date |
| **DNS** | Who runs the zone; other names with the same NS or A |
| **Same A** | Other names that resolved to this IP |
| **TLS certificate** | Other names on the same cert (SAN / issuer) |
| **HTTP title** | Same page title or resources on another host |

Registration was **2.5**. SOA and zone DNS were **2.6**. Silent Push and the other external tools were **0.7**; platform depth (VirusTotal Relations, Silent Push pivots) is **2.9**. This lesson names the class. It does not re-teach the lookup.

**What good looks like:** someone gives you a seed. You write the hop, or you reject the weak neighbor. You do not open a tool class.

- **Take.** Seed = update domain / `203.0.113.88`. Shared nameservers `ns1.cdn-test.net` / `ns2.cdn-test.net` → candidate `login-prd.net`. Why not coincidence: distinctive NS pair, not a public resolver. Same A on that named sibling can support the hop. You still write the four parts, not a P-ID.
- **Reject.** Whole `203.0.113.0/24` — shared hosting. The seed IP sitting in that range does not make the range theirs.

---

## 2. Knowledge Check

1. This lesson requires a DTF P-ID on the hop. True or false?
2. What four parts does a hop sentence have?
3. You have the update domain / `203.0.113.88`. Shared nameservers `ns1.cdn-test.net` / `ns2.cdn-test.net` point at `login-prd.net`. Write the hop, or say why you would reject the whole `203.0.113.0/24`.

---

## 3. Summary

Seed → shared characteristic → candidate → why not coincidence. Shared `/24` is not a hop. Name the source class. Do not re-teach the tool. No P-ID required.

**Next:** **2.8.2** Applicable TTPs.

---

## 4. Related modules

- 2.7.4 – DTF ID line (previous)
- 2.8.2 – Applicable TTPs
- 2.5 / 2.6 / 0.7 / 2.9 – Tools you name, not re-teach

---

# Lesson 2.8.2 – Extracting Applicable TTPs from Intelligence Reports

Source: `modules/02-cti/08-enrichment/02-applicable-ttps/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.2 B / C / C ; 2.8.2.1 3c / 4c / 4d  
- Hunter: 2.8.2 B / C / C ; 2.8.2.1 3c / 4c / 4d  
- SOC: 2.8.2 A / B / B ; 2.8.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Find **TTPs** in a report — behaviors with a how, not slogans or indicator lists.
2. Keep only those that **apply to this environment**, and reject the rest.

**Mapped Proficiency Items:**
- K: 2.8.2 – Extracting applicable TTPs from intelligence reports
- T: 2.8.2.1 – Extract applicable TTPs from an intelligence report

---

## 1. Key Concepts

A vendor report often arrives with a long ATT&CK table. CTI analysts do not copy that table into the shop’s notes. They pull the behaviors a defender **here** can actually detect or hunt, because a list of techniques that cannot happen on this network wastes hunt and detection time. That is the job in this lesson: find the TTPs in the report, then keep only the ones that apply to this environment.

A **TTP** (tactic, technique, or procedure) is a **behavior** — how the adversary works. It is not an IOC (a hash, IP, or domain). Putting a new ATT&CK ID on activity is **2.7.1**. Writing the “so what here” line is **2.8.4**. This lesson is extract and apply.

**This environment** in class is **DYA**: a law firm with Windows workstations. **WS-JLEE** is a user workstation already in the course. At a real shop you take platform and visibility facts from that shop (**0.8**). Do not invent OT, macOS, or a plant network for DYA.

Use **real** ATT&CK IDs only. Do not invent an ID.

| In the report | Keep as a TTP candidate? |
|---------------|--------------------------|
| A **how**: tool, command, procedure, or ATT&CK ID tied to that how | Yes — it is a relevant TTP |
| IOC appendix (hashes, IPs, domains) | No — that is an indicator, not a TTP |
| Slogan (“they use persistence”) or a vendor group name | No — no how |
| ATT&CK ID with no how | No — not a finished extract |

**Applicable** when all three are true:

| Criterion | Meaning here |
|-----------|----------------|
| **Platform** | We have that OS / stack. DYA is Windows workstations, not OT / ICS and not macOS-only. |
| **Path** | The behavior can actually happen here (on our hosts, mail, or network). |
| **Use** | A defender here could detect or hunt it. If you have no visibility and no way to get it, it is not applicable unless you **name that gap** — and you still do not list it as something a defender here can use. |

**What good looks like:** someone gives you a report. You write keep / reject lines. You do not map a neighbor ID (**2.7.1**). You do not write an impact paragraph (**2.8.4**).

- Given: encoded PowerShell in the report, printed as **T1059.001** (PowerShell). **Keep.** DYA runs Windows workstations, and **WS-JLEE** already showed encoded PowerShell. A defender here can hunt or detect it.
- Given: a report line “wipe OT historians.” **Reject.** DYA is a law firm. It does not run OT (operational technology) plant historians. Write **not applicable here** — not a crisis sentence.

Do not copy every ATT&CK ID in the PDF. Do not keep a Unix-only or ESXi ransomware ID for this Windows shop.

---

## 2. Knowledge Check

1. Every ATT&CK ID in a vendor report is applicable here. True or false?
2. What three things make a TTP applicable to this environment?
3. Encoded PowerShell (**T1059.001**) vs an OT-wipe TTP from a report — keep or reject each, and why?

---

## 3. Summary

Find TTPs that have a how. Keep what this shop can see or hunt. Reject the rest. That is not an ATT&CK mapping class and not an impact write-up.

**Next:** **2.8.3** IOC handling.

---

## 4. Related modules

- 2.8.1 – Identifying additional adversary infrastructure (previous)
- 2.8.3 – IOC handling
- 2.7.1 – ATT&CK mapping
- 2.8.4 – Relevance / impact
- 0.8 – Environment / signal flow
- 3.4.2 – Extracting hunt leads from CTI

---

# Lesson 2.8.3 – IOC Handling and Enrichment Concepts

Source: `modules/02-cti/08-enrichment/03-ioc-handling/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.3 B / C / C ; 2.8.3.1 3c / 4c / 4d ; 2.8.3.2 3c / 4c / 4d  
- Hunter: 2.8.3 B / C / C ; 2.8.3.1 3c / 4c / 4d ; 2.8.3.2 1a / 2b / 3c  
- SOC: 2.8.3 A / B / B ; 2.8.3.1 1a / 2b / 3c ; 2.8.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Treat an **IOC** as an object you **keep, expire, enrich, or link** — not a TTP.
2. Name a tool and field to enrich, and say whether two IOCs are the **same activity set**.

**Mapped Proficiency Items:**
- K: 2.8.3 – IOC handling and enrichment concepts
- T: 2.8.3.1 – Enrich and pivot on IOCs using internal and external tools
- T: 2.8.3.2 – Link analysis and campaign tracking

---

## 1. Key Concepts

CTI analysts handle **IOCs** (indicators of compromise) that land on the desk from a report, a feed, or an RFI. Each one is an **observable** — a hash, IP, domain, or similar object — that you record, enrich, or expire. You do this so the shop does not store junk, hunt a whole cloud range, or treat a behavior as if it were an object. **2.8.2** already covered TTPs (tactics, techniques, and procedures): those are **behaviors**. This lesson is the **object**.

| Action | What it means |
|--------|----------------|
| **Keep** | Cited, current, and specific enough to use. You can point at a source. |
| **Expire** | Stale, uncited, or **shared-infrastructure noise** — a range or host many unrelated tenants share, such as `203.0.113.0/24`. |
| **Enrich** | Name the tool, the field, and what you hope to learn. Do not re-teach the tool. |
| **Link** | Same **activity set** (the objects that belong to one campaign or incident chain) if they share objects you can cite. Keep them **apart** if they do not. |

**Keep** the cited current IOC. **Expire** (reject) the stale, uncited, or shared-infrastructure object. A whole `/24` that contains one bad IP is still noise.

**Enrichment** uses internal and external tools already taught. This lesson **selects and records** the lookup; it does not re-teach the tool. Name the tool, the field, and what you hope to learn — that is the product. Pivot here means look up related data from this object. It is not a rewrite of the hop sentence (**2.8.1**). It is not VirusTotal Relations depth (**2.9.1**).

**Link analysis** (also called campaign tracking) is the same-set decision. Cite the shared objects. A vendor group name on a PDF is not a link.

**What good looks like:**

- **Keep / expire:** Keep the cited update domain, `203.0.113.88`, and the hash of Temp `invoice.vbs`. Expire the whole Example Cloud range `203.0.113.0/24` as shared-infrastructure noise.
- **Enrich:** Hash of `invoice.vbs` → internal threat intelligence platform (**TIP**, **2.3.1**) first, then VirusTotal if you still need a public reputation (**0.7**). Hope to learn: seen here before, or public reputation. Not the Relations tab (**2.9.1**).
- **Link:** Update domain + `203.0.113.88` + `login-prd.net` (same nameserver pair, same A record — the IPv4 address the name resolves to) = **one activity set**. A random Example Cloud IP with no shared nameserver stays **apart**. Reject “same group because the PDF said PRD APT.”

Do not extract TTPs here (**2.8.2**). Do not write the “so what here” line (**2.8.4**). Do not write an actor profile (**2.11**).

---

## 2. Knowledge Check

1. An IOC is the same thing as a TTP. True or false?
2. Do you keep or expire a whole `/24` that contains one bad IP?
3. Update domain + sibling that share a nameserver — same activity set or apart, and why? Why is a vendor name such as “PRD APT” not a link?

---

## 3. Summary

An IOC is an observable you keep, expire, enrich, or link. A TTP is a behavior. Keep cited current IOCs. Expire shared-infrastructure noise. Name the tool and what you hope to learn; do not re-teach the tool. Link only on shared objects, not a vendor label.

**Next:** **2.8.4** Relevance and impact.

---

## 4. Related modules

- 2.8.2 – Applicable TTPs (previous)
- 2.8.4 – Relevance and impact
- 2.8.1 – Infra hop (the hop sentence, not this object)
- 2.3.1 / 0.7 / 2.9 – Tools you name, not re-teach
- 2.7.2 – Diamond / vendor name on Adversary
- 2.11 – Actor profile

---

# Lesson 2.8.4 – Threat Relevance and Organizational Impact

Source: `modules/02-cti/08-enrichment/04-relevance-impact/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.4 B / C / C ; 2.8.4.1 3c / 4c / 4d  
- Hunter: 2.8.4 B / C / C ; 2.8.4.1 2b / 3c / 4c  
- SOC: 2.8.4 A / B / B ; 2.8.4.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say whether a finding **applies here**, and **what would change** if it is true.
2. Keep that line off PIR writing, TTP extract, and attribution.

**Mapped Proficiency Items:**
- K: 2.8.4 – Threat relevance and organizational impact
- T: 2.8.4.1 – Assess threat relevance and potential impact to the organization

---

## 1. Key Concepts

CTI analysts say whether a finding **matters here**, not only whether it is technically interesting. Enrichment can leave you with an extra domain, a kept TTP, or a handled IOC. Someone still has to write the line for this shop. If you skip it, people chase reports that never touch this mission, these assets, or this platform — or they write a crisis the evidence does not support.

This lesson is those two sentences: **relevance** and **impact**. TTP applicability is **2.8.2**. Handling the IOC as an object is **2.8.3**. This lesson is the so-what that follows.

| Sentence | Meaning |
|----------|---------|
| **Relevance** | Does this finding apply to this environment: **mission** (what the shop does), **assets** (what it owns), and **platform** (what it runs)? |
| **Impact** | If the finding is true, **what would change here**? Write the change that follows from this finding. |

The classroom company is a **law firm** that runs **Windows workstations**. Judge against that environment. Do not invent a shop list of impact categories.

Relevance and impact are not the other products that sit next to them:

| Not this lesson | What that product is |
|-----------------|----------------------|
| **TTP applicability** (**2.8.2**) | Whether a behavior from a report can happen or be hunted on this platform. Keep or reject the TTP. That is not the so-what of a finding. |
| **PIR** (**2.1.4** / **2.12.1**) | A **priority intelligence requirement** — a ranked question the shop wants answered. Do not write or invent that list here. |
| **Attribution** (**2.1.7**) | Who or what cluster did it, and at what confidence. A country or a vendor “APT” name is not the impact line. |

**What good looks like:**

- **Relevant:** encoded PowerShell and an update-domain fetch on **WS-JLEE** (incident **A12**). We run Windows workstations. We already saw this on that host.
- **Impact:** IR has the host. The payload path is live on a user workstation. Not “nation-state crisis.” Not a new PIR.
- **Not relevant:** a report’s OT-wipe finding. This shop does not run that process. Impact: none here.

Do not retell the whole incident. Do not extract **T1059.001** as the product (**2.8.2**). Do not name a country (**2.1.7**).

---

## 2. Knowledge Check

1. Relevance is the same as writing a PIR. True or false?
2. What two sentences do you write?
3. Given: encoded PowerShell and an update-domain fetch on **WS-JLEE** (incident **A12**, a Windows workstation). Write one relevance sentence and one impact sentence. Do not name a country. Do not write a PIR.

---

## 3. Summary

Does this finding apply here? If it is true, what would change? Stop there. Not a PIR. Not a country. Not a TTP list.

**Next:** **2.9.1** VirusTotal Relations and Behavior.

---

## 4. Related modules

- 2.8.3 – IOC handling (previous)
- 2.9.1 – VirusTotal
- 2.8.2 – Applicable TTPs
- 2.1.4 / 2.12.1 – Requirements
- 2.1.7 – Attribution

---

# Lesson 2.9.1 – VirusTotal (Relations and Behavior)

Source: `modules/02-cti/09-platforms/01-virustotal/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.1 B / C / C ; 2.9.1.1 3c / 4c / 4d  
- Hunter: 2.9.1 B / C / C ; 2.9.1.1 3c / 4c / 4d  
- SOC: 2.9.1 A / B / B ; 2.9.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use the **Relations** tab to name additional adversary infrastructure from a seed you already have.
2. Use the **Behavior** tab to extract file, network, registry, or process events.

**Mapped Proficiency Items:**
- K: 2.9.1 – VirusTotal (Relations and Behavior tabs)
- T: 2.9.1.1 – Use VirusTotal Relations and Behavior to pivot and extract events

---

## 1. Key Concepts

CTI analysts take a **seed** they already have — a file hash, a URL, or an IP — and use VirusTotal to name more adversary infrastructure and to pull host events from a sandbox run. That is daily enrichment: you already know when to pick this tool (**0.7**). This lesson is the two **tabs** on the report. You read a **classroom result card** (a copy of a VirusTotal result this lesson provides). You do not log in. You write what the card shows. You do not invent a hit.

The hop sentence (seed, shared characteristic, candidate, why not coincidence) is **2.8.1**. File-similarity hashes are **2.4**. Applicable TTPs are **2.8.2**. Hunt conversion to a SIEM or Zeek query is **3.3.1**. None of those are this lesson.

| Tab | What it is | What you write |
|-----|------------|----------------|
| **Relations** | Linked objects for this seed: contacted domains, IPs, URLs, and dropped files | Additional **infrastructure** — a host or dropped name that is on the card |
| **Behavior** | Events from a **sandbox run** of this sample | One **process**, **file**, **registry**, or **network** event that is on the card |

**Relations** is a graph of objects you can open next. **Behavior** is what the sandbox logged this sample doing. A contacted domain can appear in both. The product still follows the tab: Relations → extra infrastructure; Behavior → the event.

A detection count is not Relations and is not Behavior. If a tab has no line, write **not on card**. Empty Behavior usually means no sandbox run was stored — not a license to invent the event.

**What good looks like:**

This lesson’s card, seed = hash of `update.exe` (SHA256 starts `6734f374…`):

| Tab | On the card | Not on the card |
|-----|-------------|-----------------|
| **Relations** | Contacted IP `203.0.113.88` | A sibling hostname you did not see |
| **Behavior** | Process: `update.exe` started. File: a write under Temp. Network: `203.0.113.88` port `8080` | Registry Run key **`Updater`** |

- **Relations:** additional infra is `203.0.113.88`. You do not write a sibling domain. You do not write a hop sentence (**2.8.1**).
- **Behavior:** extract the process, file, or network event above. You do not invent the Run key. You do not turn the network line into a SIEM query (**3.3.1**).

Given: “the card has no registry line.” **Not on card.** Do not copy the host plot onto VirusTotal.

---

## 2. Knowledge Check

1. This lesson is “when to pick VirusTotal.” True or false?
2. What does Relations give you that Behavior does not?
3. Seed hash of `update.exe`. Name one Relations result you may write from the card, and one thing you must not invent.

---

## 3. Summary

Relations names extra infrastructure from a seed. Behavior extracts process, file, registry, and network events from a sandbox run. Write what the card shows, or **not on card**. You do not invent a hit. You do not need a live account.

**Next:** **2.9.2** AnyRun.

---

## 4. Related modules

- 2.8.4 – Threat relevance and organizational impact
- 2.9.2 – AnyRun
- 0.7 – External tools (when to pick VirusTotal)
- 2.8.1 – Identifying additional adversary infrastructure

---

# Lesson 2.9.2 – AnyRun

Source: `modules/02-cti/09-platforms/02-anyrun/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.2 B / C / C ; 2.9.2.1 3c / 4c / 4c  
- Hunter: 2.9.2 A / B / B ; 2.9.2.1 2b / 3c / 4c  
- SOC: 2.9.2 A / A / B ; 2.9.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Search AnyRun submissions by tag, IP, domain, or hash.
2. Review a submission and extract **actionable** intelligence from a classroom card, or say it is not on the card.

**Mapped Proficiency Items:**
- K: 2.9.2 – AnyRun
- T: 2.9.2.1 – Search and review AnyRun submissions for actionable intelligence

---

## 1. Key Concepts

CTI analysts search **public detonations** for a seed they already have — a tag, an IP, a domain, or a hash. A public detonation is a sandbox run someone else published. They do this so they can write **who** can act and **what** they do from a run that already happened, instead of guessing from a label. When to pick AnyRun is **0.7**. This lesson is **search and review**. You work from a **classroom card** (a static submission page). You do not need a live vendor account.

| Move | Job |
|------|-----|
| **Search** | The tag, IP, domain, or hash you already have |
| **Review** | Process tree, network, and dropped files **on the card** |
| **Extract** | A who + what someone can act on (**2.1.5**) — or **not on card** |

A **tag** is a label on a public run (a family name, a short verdict, a technique name). Search the tag you already have. Do not fish for a new family.

**What good looks like:**

- Search `203.0.113.88` or the hash of `update.exe`. Those are seeds you already have, not new hunts.
- Extract a contacted URI or a dropped file name **if the card shows it**.
- If the card does not show a check-in POST (a beacon to a URL), write **not on card**. Do not invent one.
- A count of “malicious” tags is **information**, not intelligence. It has no who and no next step.

This is not when to pick AnyRun (**0.7**). It is not a VirusTotal Relations hop (**2.9.1**). A conceptual infrastructure hop is **2.8.1**. Hunt conversion to SIEM or Zeek is **3.3.1**.

---

## 2. Knowledge Check

1. A count of “malicious” tags on an AnyRun card is actionable intelligence. True or false?
2. What four things can you search AnyRun submissions by?
3. You open a classroom card for the `update.exe` hash. Name one extract that is legal if it is on the card, and one thing you must **not** invent.

---

## 3. Summary

Search the seed you already have. Review the card. Extract who and what, or say it is missing. A verdict tag is not intelligence. No live account.

**Next:** **2.9.3** Silent Push.

---

## 4. Related modules

- 2.9.1 – VirusTotal (previous)
- 2.9.3 – Silent Push
- 0.7 – When to pick AnyRun
- 2.1.5 – Actionable intelligence
- 2.8.1 – Infrastructure hop
- 3.3.1 – Hunt conversion to SIEM / Zeek

---

# Lesson 2.9.3 – Silent Push

Source: `modules/02-cti/09-platforms/03-silent-push/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.3 B / C / C ; 2.9.3.1 3c / 4c / 4d  
- Hunter: 2.9.3 A / B / B ; 2.9.3.1 2b / 3c / 4c  
- SOC: 2.9.3 A / A / B ; 2.9.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name Silent Push’s **core capabilities** and what you use it for: **passive DNS** (historical resolutions, also called PDNS) and infrastructure context around a seed you already have.
2. **Enrich** that seed from a classroom card, then **pivot** only to extra names or IPs the card shows.

**Mapped Proficiency Items:**
- K: 2.9.3 – Silent Push
- T: 2.9.3.1 – Enrich an indicator and pivot in Silent Push

---

## 1. Key Concepts

CTI analysts already have a **seed** — a domain or IP from the case. They open Silent Push to see the **passive DNS** history around that seed and any related infrastructure the product actually lists. That is the job in this lesson: enrich the seed from the **classroom result card**, then pivot only to extra names the card shows, so you do not treat shared hosting as theirs.

Silent Push is a **passive DNS / infrastructure** tool. It is **not** a sandbox detonation and **not** a page screenshot. When to pick it instead of VirusTotal, AnyRun, or URLScan is **0.7**. This lesson is what you read once you are in Silent Push.

| Capability | What you use it for |
|------------|---------------------|
| **Historical names on an A** | Which hostnames have pointed at this IPv4 address (an **A** record is that IPv4 mapping) |
| **A history for a name** | Which IPv4 addresses this hostname has resolved to |
| **Shared nameservers** | Other names that use the same **NS** (nameserver) pair — only if the card shows them |

**Enrich** means you write what the card says about the seed you already have. **Pivot** means you take one shared fact from that card (same A, or same NS pair) and name additional infrastructure. If the card does not show the extra name, write **not on the card**. Do not invent a hit.

| Move | Job |
|------|-----|
| **Enrich** | What names have pointed at `203.0.113.88`? What A records has the update domain had? |
| **Pivot** | Other names with the same NS pair — if the card shows them |

**What good looks like:**

- Given: enrich `203.0.113.88` on the classroom card. **Take** the names on that A that the card lists (the update domain, maybe `login-prd.net`).
- **Reject** treating the whole `203.0.113.0/24` as theirs. Neighboring IPs on that subnet are shared hosting, not extra adversary infrastructure.
- If a sibling is not on the card, the legal line is **not on the card**.

This is **not** an RDAP class (**2.5**) and **not** an SOA class (**2.6**). The generic hop sentence (seed, shared characteristic, candidate, why not coincidence) is **2.8.1**. Hunt conversion to SIEM or Zeek is **3.3.1**. You do **not** need a live Silent Push account.

---

## 2. Knowledge Check

1. This lesson is “when to pick Silent Push.” True or false?
2. What two jobs do you do in Silent Push?
3. Enrich `203.0.113.88`. One legal pivot, and one thing you must reject.

---

## 3. Summary

Silent Push gives passive DNS and infrastructure context for a seed you already have. Enrich that seed from the classroom card. Pivot only to names the card shows. A shared `/24` is not theirs.

**Next:** **2.9.4** URLScan.

---

## 4. Related modules

- 2.9.2 – AnyRun
- 2.9.4 – URLScan
- 0.7 – External tools
- 2.8.1 – Identifying additional adversary infrastructure

---

# Lesson 2.9.4 – URLScan

Source: `modules/02-cti/09-platforms/04-urlscan/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.4 B / C / C ; 2.9.4.1 3c / 4c / 4c  
- Hunter: 2.9.4 A / B / B ; 2.9.4.1 2b / 3c / 4c  
- SOC: 2.9.4 A / A / B ; 2.9.4.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what URLScan records on **this page load**, and what you open it to see.
2. Retrieve a result (or treat a provided result as submitted) and extract what is on it — or write that it is missing.

**Mapped Proficiency Items:**
- K: 2.9.4 – URLScan
- T: 2.9.4.1 – Submit or retrieve a URLScan result and extract actionable intelligence

---

## 1. Key Concepts

You have a live URL — often the **update domain** from the RFI. You need to see **what that URL served** on this visit: the page title, the hosts and IPs it requested, the redirect chain. URLScan records that page load. That is the job in this lesson: retrieve a result and extract what is on it, so you do not invent a page or treat a screenshot as a finished judgment. When to pick URLScan instead of Silent Push or VirusTotal is **0.7**. This lesson is how to read the result.

URLScan visits a URL in a browser sandbox and records **this page load**. That is the capability. The use case is a live URL you already have, not a file to detonate and not a domain-history question.

This lesson uses a **classroom result card** — a provided scan result. You do not need a live URLScan account. **Retrieve** means you read an existing result for that URL. **Submit** means you send the URL so URLScan visits it and builds a new result. Retrieve is enough here. You do not submit from a live account in this lesson.

| Extract | What it is for |
|---------|----------------|
| **Page title / final URL** | What the visitor would have seen |
| **Requested hosts / IPs** | Extra infrastructure the page talked to (a hop is **2.8.1**) |
| **Redirect chain** | How the browser got from the submitted URL to the final page |

A **screenshot** of the page is **information** — what the page looked like. It is not a judgment by itself (**2.1.1**).

**What good looks like:** you are given the update-domain URL. You retrieve the classroom result card if there is one. You extract the title or a requested host **that the card shows**. If there is no result, you write **not on card**. You do not invent a login page. You do not write the hop sentence (**2.8.1**). You do not turn this into a SIEM or Zeek hunt (**3.3.1**).

- Given: a result card for the update URL with a title and a requested host. **Extract** those two. Stop.
- Given: no card for that URL. **Write:** not on card. Do not fill in `login-prd.net` as a page you did not see.

---

## 2. Knowledge Check

1. This lesson is “when to pick URLScan.” True or false?
2. Name two fields you extract from a URLScan result.
3. You have no card for the update URL. What do you write?

---

## 3. Summary

URLScan records what a URL served on this page load. Retrieve a result. Extract the title, requested hosts or IPs, and redirects that are on it — or write that it is missing. A screenshot is information. No live submit is required.

**Next:** **2.10.1** Core STIX objects.

---

## 4. Related modules

- 2.9.3 – Silent Push (previous)
- 2.10.1 – Core STIX objects
- 0.7 – When to pick URLScan
- 2.8.1 – Hop sentence

---

# Lesson 2.10.1 – Core STIX Objects

Source: `modules/02-cti/10-stix/01-core-objects/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.10.1 B / C / C ; 2.10.1.1 3c / 4c / 4c  
- Hunter: 2.10.1 B / C / C ; 2.10.1.1 2b / 3c / 4c  
- SOC: 2.10.1 A / B / B ; 2.10.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the eleven **STIX 2.1** objects this lesson covers.
2. Given a line from a report, label the object. Do not invent a type.

**Mapped Proficiency Items:**
- K: 2.10.1 – Core STIX objects
- T: 2.10.1.1 – Identify and label common STIX objects in a report

---

## 1. Key Concepts

CTI analysts share threat facts in a common language so another shop — and hunt — can reuse them without guessing what each fact was. **STIX** (Structured Threat Information Expression) is that language. Version **2.1** is the spec this course uses. Before you write a bundle or a narrative, you have to name **what kind of object** each fact is. That is the job in this lesson: look at a report and label it.

Hunt *reads* STIX as input later (**3.4.3**). Finished narrative is **2.11**. TIP retrieve is **2.3.1**. Linking objects and TAXII consume are **2.10.2**. This lesson is **identify**. Classroom report or bundle only. Do not stand up a TAXII server.

This lesson uses these eleven real STIX **2.1** types. Do not invent a twelfth.

| Object | What it names |
|--------|----------------|
| **Indicator** | A pattern used to detect activity (a hash pattern, an IP pattern) |
| **Observed Data** | A raw record of what was seen (this file, this IP) — not a judgment |
| **Malware** | Malicious code: a family or an instance — not the hash pattern |
| **Attack Pattern** | A way the adversary works (for example T1059.001) |
| **Threat Actor** | Who is believed to operate with malicious intent |
| **Intrusion Set** | Grouped behaviors believed to be one actor’s set |
| **Campaign** | A time-bounded set of activity against a set of targets |
| **Course of Action** | A recommended action to prevent or respond |
| **Identity** | A person, organization, or system — including the victim. Not the attacker by default |
| **Relationship** | A typed link between two objects |
| **Sighting** | An assertion that an object was seen, often at an Identity |

A hash can be two different objects. If the report gives a pattern to find that hash again, it is an **Indicator**. If it only records that the hash was seen, it is **Observed Data**.

**Sighting** is not **Observed Data**. Observed Data is the record (“this file was on the host”). Sighting is the assertion (“we saw this Indicator / Malware here”). **Relationship** is a typed link (this Indicator *indicates* that Malware). A line that ties an Indicator to **WS-JLEE** is a **Sighting**, not a generic Relationship.

**What good looks like:** someone gives you a line from a report. You name the object. You do not write the bundle yet.

- Hash of `invoice.vbs` as a detection pattern. **Indicator.** The same hash as “this file was seen” is **Observed Data**.
- Encoded PowerShell / T1059.001. **Attack Pattern.**
- The malicious `invoice.vbs` family or instance. **Malware.**
- **WS-JLEE** / **DYA**. **Identity** (victim), not Threat Actor.
- “PRD APT” on a PDF. **Not** automatically Threat Actor. That is a vendor label. Attribution is **2.1.7**.
- “We saw that hash on WS-JLEE.” **Sighting.**
- A link that says this Indicator indicates that Malware. **Relationship.** Do not pick the link type here — **2.10.2**.
- Block the payload host, or kill the Run key. **Course of Action.**

Do not tell the rest of the incident. Do not invent a type if none of the eleven fits.

---

## 2. Knowledge Check

1. You may invent a STIX type if none of these eleven fits. True or false?
2. “PRD APT” on a vendor PDF is automatically a Threat Actor object. True or false?
3. Hash of `invoice.vbs` used as a detection pattern, vs **WS-JLEE**. Which two objects?

---

## 3. Summary

STIX 2.1 names eleven objects in this lesson. Label the object from the report. A hash pattern is an Indicator; a raw observation is Observed Data. A victim host is Identity. A vendor name is not automatically Threat Actor.

**Next:** **2.10.2** STIX in production.

---

## 4. Related modules

- 2.9.4 – URLScan (previous)
- 2.10.2 – STIX production / TAXII
- 2.3.1 – TIP retrieve
- 3.4.3 – Hunt STIX input

---

# Lesson 2.10.2 – How STIX Objects Are Used in Intelligence Production

Source: `modules/02-cti/10-stix/02-stix-production/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.10.2 B / C / C ; 2.10.2.1 3c / 4c / 4d ; 2.10.2.2 3c / 4c / 4d ; 2.10.2.3 3c / 4c / 4c  
- Hunter: 2.10.2 B / C / C ; 2.10.2.1 2b / 3c / 4c ; 2.10.2.2 2b / 3c / 4c ; 2.10.2.3 2b / 3c / 4c  
- SOC: 2.10.2 A / B / B ; 2.10.2.1 1a / 1a / 2b ; 2.10.2.2 1a / 1a / 2b ; 2.10.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Structure STIX objects for sharing and automation, and link them with real **relationship** types so the set retells a threat scenario.
2. Say what a **valid** STIX 2.1 object looks like, and what **TAXII** sharing and consumption look like — classroom collection only; no server.

**Mapped Proficiency Items:**
- K: 2.10.2 – How STIX objects are used in intelligence production
- T: 2.10.2.1 – Create STIX-aligned relationships and explain a threat scenario
- T: 2.10.2.2 – Create and validate STIX objects
- T: 2.10.2.3 – Use TAXII for sharing and consumption of intelligence

---

## 1. Key Concepts

CTI analysts **package** threat activity so other people and other tools can reuse the same story. A hash in a slide is not reusable. You connect the objects you already named, you check they are valid STIX 2.1, and you share or pull that package so a TIP, a hunt, or another shop can ingest the graph without reading a PDF. That is the job in this lesson. **2.10.1** named the object types. This lesson is the production step. It is **not** the finished narrative product (**2.11**). It is **not** TIP search (**2.3.1**). Hunt *reads* STIX later (**3.4.3**). Classroom bundle only. Do not stand up a TAXII server.

**Structuring for sharing and automation.** STIX 2.1 objects travel together in a **bundle** — a wrapper that carries the objects as one package. The bundle is the **payload**. Machines can ingest it. A PDF you email is a story for a person. It is not a STIX bundle, and it is not TAXII.

**Linking objects.** A **Relationship** is its own STIX object. It names how two objects connect. Use a real STIX 2.1 `relationship_type`. Do not invent one.

| `relationship_type` | What it says |
|---------------------|--------------|
| **indicates** | This Indicator points at that activity (Attack Pattern, Malware, and similar) |
| **based-on** | This Indicator is based on that Observed Data |
| **targets** | This actor, malware, or campaign targets that Identity |
| **uses** | This actor, malware, or campaign uses that Attack Pattern or tool |
| **related-to** | A non-specific link when no tighter type fits — do not use it to hide a guess |

**Sighting** is not a `relationship_type`. It is its own STIX object. It says something was seen. It points at the seen object with `sighting_of_ref`. Optional `where_sighted_refs` names the **Identity** that saw it (a host or org). `sighting-of` is not a STIX 2.1 relationship type.

**Create / validate.** A STIX 2.1 object needs `type`, `spec_version` (`2.1`), `id`, `created`, and `modified`. A Relationship also needs `relationship_type`, `source_ref`, and `target_ref`. An Indicator also needs a **pattern** (`pattern` and `pattern_type`). The bundle is only the wrapper; you validate the objects inside it.

Invalid: missing `type`, an invented `type` or `relationship_type`, a Relationship with no `relationship_type`, or an unearned **Threat Actor** because a PDF said “PRD APT.”

**TAXII.** **TAXII** is the **channel** — the protocol for putting STIX on the wire and taking it off. A **collection** is a named group of objects on a TAXII server. **Sharing** is publishing a valid bundle into a collection. **Consumption** is pulling objects from a collection. In this lesson you **consume**: pull the classroom collection this course names `harbor-cti`. You do not run the server.

**What good looks like:** someone gives you the classroom incident **A12** — `wscript` ran Temp `invoice.vbs` on host **WS-JLEE**, then encoded PowerShell (Attack Pattern **T1059.001**). You produce a small graph, not a report.

- Indicator (hash of `invoice.vbs`) **indicates** Attack Pattern T1059.001.
- Sighting of that Indicator, `where_sighted_refs` Identity **WS-JLEE**.
- That set retells A12: a hash indicates encoded PowerShell, and we saw it on WS-JLEE.
- Validate: those objects have `type`, `spec_version` `2.1`, `id`, `created`, `modified`; the Relationship has `relationship_type` `indicates`; the Sighting has `sighting_of_ref`.
- TAXII: “I would pull collection `harbor-cti`.” Not “I stood up TAXII.”

Do not add a Threat Actor to make the graph look complete. Do not invent a relationship type. Do not tell the rest of the narrative product (**2.11**).

---

## 2. Knowledge Check

1. You should stand up a TAXII server in this lesson. True or false?
2. Name two real STIX 2.1 relationship types.
3. Write one STIX-aligned link that ties the `invoice.vbs` hash to **WS-JLEE**.

---

## 3. Summary

A bundle packages STIX objects so machines can reuse the story. Real relationship types only; Sighting is its own object. A classroom object must validate. TAXII is the channel; you consume a collection. You do not run the server.

**Next:** **2.11.1** Finished intelligence products.

---

## 4. Related modules

- 2.10.1 – Core STIX objects
- 2.11.1 – Finished intelligence products
- 2.3.1 – Internal TIP
- 3.4.3 – STIX as hunt input

---

# Lesson 2.11.1 – Creating Finished Intelligence Products

Source: `modules/02-cti/11-production/01-finished-products/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.11.1 B / C / C ; 2.11.1.1 3c / 4c / 4d ; 2.11.1.2 3c / 4c / 4d  
- Hunter: 2.11.1 A / B / B ; 2.11.1.1 1a / 2b / 3c ; 2.11.1.2 1a / 2b / 3c  
- SOC: 2.11.1 A / A / B ; 2.11.1.1 1a / 1a / 2b ; 2.11.1.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name what a **finished product** must contain, and evaluate a draft against those standards.
2. Produce a short **actor / activity profile** that does not invent a nation-state.

**Mapped Proficiency Items:**
- K: 2.11.1 – Creating finished intelligence products
- T: 2.11.1.1 – Draft a finished product and evaluate it against standards
- T: 2.11.1.2 – Produce a threat actor profile

---

## 1. Key Concepts

CTI analysts write a **finished product** so someone can use the judged answer. Collection and notes do not help until that answer is on the page to a standard. Pasting indicators out of a **TIP** (threat intelligence platform — the shop store of indicators and reports) is not that product. This lesson is how to draft the product, check it against those standards, and write a short profile of the cluster you can actually defend.

A finished product is intelligence written down: a judged answer to a named question. It is not a hash list. It is not a machine bundle. Audience rewrite is **2.1.6**. Attribution assessment (confidence versus evidence) is **2.1.7**. STIX is **2.10**. SOC ticket types are **1.5**. Who gets the product, and on which channel, is **2.11.2**. Local approval is **2.12**. How to run an **RFI** (request for information) queue is **2.11.3**.

| Type | What it is |
|------|------------|
| **Assessment** | A judged answer to a named question (for example: is this the payload host *here*?) |
| **Profile** | A short picture of an activity cluster or actor — what they do, not a country you invented |
| **RFI response** | A finished answer to a request for information. Pick the type that matches the question. The queue itself is **2.11.3**. |

Pick **one** type that matches the requirement. Do not staple all three into one dump.

| Required element | What to write |
|------------------|---------------|
| **Question** | The requirement the product answers |
| **What you know** | Sourced facts — what you used, not everything in the TIP |
| **Judgment** | An estimative term (**likely**, **unlikely**, and the rest of the classroom set). Not “could be.” |
| **So-what** | Who can act, and on what |
| **Confidence / caveat** | How good the evidence is, and what you do not know |

**Quality and analytic standards.** A draft **passes** when it answers the named requirement, names its sources, uses an estimative term, and does not invent a country. A **hash dump** fails. A TIP paste fails. A vendor “APT” name is a **label**, not proof of a government.

**A12** is the classroom incident on workstation **WS-JLEE**: encoded PowerShell, an update domain, and a distinctive nameserver pair. Use that cluster. Do not invent a nation-state.

**What good looks like:**

- **Draft.** Given: requirement = is the payload host *here*? **Pass:** the update domain is **likely** the **A12** payload host; IR has **WS-JLEE**; medium confidence; sources = Zeek A record (the name-to-IP the network sensor logged) and the host file (this host logged the talk). **Fail:** a hash dump with no question, no judgment, and no so-what.
- **Profile:** activity cluster (encoded PowerShell, update domain, distinctive nameserver pair). Victim host **WS-JLEE**. Vendor APT name stays a label. **Not** “nation-state PRD APT.”

---

## 2. Knowledge Check

1. A TIP paste is a finished product. True or false?
2. Name three required elements of a finished product.
3. Write a three-line **A12** profile that does **not** claim a country.

---

## 3. Summary

A finished product is the judged answer: question, what you know, judgment, so-what, and a caveat. Profile the cluster you can defend. Do not invent a government. Do not paste the TIP.

**Next:** **2.11.2** Dissemination.

---

## 4. Related modules

- 2.10.2 – STIX production (previous)
- 2.11.2 – Dissemination
- 2.1.6 / 2.1.7 – Audience / attribution
- 2.12 – Local approval

---

# Lesson 2.11.2 – Disseminating intelligence to the correct audiences

Source: `modules/02-cti/11-production/02-dissemination/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.11.2 B / C / C ; 2.11.2.1 3c / 4c / 4c ; 2.11.2.2 3c / 4c / 4d ; 2.11.2.3 3c / 4c / 4c  
- Hunter: 2.11.2 A / B / B ; 2.11.2.1 1a / 2b / 3c ; 2.11.2.2 1a / 2b / 3c ; 2.11.2.3 1a / 2b / 3c  
- SOC: 2.11.2 A / A / B ; 2.11.2.1 1a / 1a / 2b ; 2.11.2.2 1a / 1a / 2b ; 2.11.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the **audience**, an **approved channel**, and a **handling marking**, and apply a **handling caveat**.
2. Tailor the same **A12** product for a technical audience and for leadership, and reject the wrong channel.

**Mapped Proficiency Items:**
- K: 2.11.2 – Disseminating intelligence to the correct audiences
- T: 2.11.2.1 – Select audience and method and apply correct handling markings
- T: 2.11.2.2 – Tailor products to different audiences (technical, leadership, etc.)
- T: 2.11.2.3 – Disseminate intelligence products through approved channels

---

## 1. Key Concepts

CTI analysts **send the finished product** to the people who can use it, on a path the shop already approved, with a label that says who else may see it. A judged answer that only lives in a private chat is not disseminated. Leadership that never sees the one-liner cannot act. That is the job in this lesson: name the audience, the approved channel, and the handling marking — then send that version.

**2.11.1** wrote the product. **2.1.6** is how you change content, format, and detail for a named reader. You do not change the judgment. This lesson is the **send**. SOC report routing is **1.5.3**. Local customer lists are **2.12.3**. The TLP labels and channels in this lesson are **classroom stand-ins** — not live org policy.

| Idea | What it is |
|------|------------|
| **Audience** | Who owns the next decision. **IR / SOC** (technical) vs **leadership** (awareness) |
| **Channel** | How it travels. **Ticket** or **approved intel channel**. Reject personal SMS, private chat, and public post |
| **Handling marking** | A label that says who may see this product |
| **Handling caveat** | An extra instruction the label does not say (for example, no hash on the leadership send) |

**Classroom card (this lesson only — not live org policy):**

| Label | Meaning in this lesson |
|-------|------------------------|
| **TLP:AMBER** | Need-to-know inside the organization. Not a public post |
| **TLP:CLEAR** | No restriction. Do not use this on a product that names a live host |

**TLP** here means Traffic Light Protocol used as a practice label. If your shop has a real marking card, use that card. Do not invent a DYA color such as `TLP-RED-DYA`.

A one-liner is still marked. Right people on the wrong path still fails.

**What good looks like:**

**Given:** the finished **A12** product from **2.11.1**. IR has **WS-JLEE** / `jlee`. The update domain is **likely** the payload host. Temp `invoice.vbs` is on the host. Same facts. Two sends.

- **Technical (IR / SOC):** audience IR + SOC. Channel: ticket. Marking: **TLP:AMBER** (classroom). Caveat: need-to-know inside the shop. Detail: host, `invoice.vbs`, update domain.
- **Leadership:** audience duty lead (awareness). Channel: approved channel. Marking: still **TLP:AMBER** (classroom). Caveat: **no hash**, no file path. One line: IR has the host; treat the update domain as the payload host.
- **Reject:** personal SMS or private chat “so leadership sees it faster.”

Do not rewrite the judgment so leadership likes it (**2.1.6**). Do not invent a customer list (**2.12.3**).

---

## 2. Knowledge Check

1. Personal SMS is fine if leadership needs it fast. True or false?
2. What three things do you name to route a product?
3. **A12** to IR vs leadership — one difference in detail, and one rejected channel.

---

## 3. Summary

Audience, approved channel, and handling marking. Same facts, different detail. A caveat can still restrict the send. No SMS. Classroom TLP is not live org policy.

**Next:** **2.11.3** Handling RFIs.

---

## 4. Related modules

- 2.11.1 – Creating finished intelligence products (previous)
- 2.11.3 – Handling RFIs
- 2.1.6 – Tailoring output to the audience
- 1.5.3 – Notification and distribution
- 2.12.3 – Local dissemination channels and customers

---

# Lesson 2.11.3 – Handling RFIs

Source: `modules/02-cti/11-production/03-rfi/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.11.3 B / C / C ; 2.11.3.1 3c / 4c / 4d  
- Hunter: 2.11.3 A / A / B ; 2.11.3.1 1a / 1a / 2b  
- SOC: 2.11.3 A / A / A ; 2.11.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what an **RFI** is for, and name how it moves (receive → evaluate → prioritize → respond).
2. Evaluate and prioritize the **A12** RFI, and write a **response** that answers the question.

**Mapped Proficiency Items:**
- K: 2.11.3 – Handling RFIs
- T: 2.11.3.1 – Evaluate, prioritize, and produce a response to an RFI

---

## 1. Key Concepts

CTI analysts **answer the question another desk sent** because that desk needs a fact it does not have. That ask is an **RFI** (Request for Information). SOC already recorded the case. They still need to know whether the update domain is the host that served the payload. That is the job in this lesson: take the question, decide whether you can answer it and whether it goes first, and write the answer. You do not open a second incident. You do not rewrite the SOC ticket.

**2.11.2** sent the finished product. SOC picking incident versus RFI as a ticket type is **1.5.1**. This lesson is the **answer**. The five-element product structure is **2.11.1**. Local queue policy is **2.12** — obtain it; do not invent it. The classroom queue in this lesson is **lesson-only**, not live org policy.

| Idea | What it is |
|------|------------|
| **Purpose** | Someone needs information they do not have. The RFI *is* the question |
| **Lifecycle** | **Receive** the question. **Evaluate.** **Prioritize.** **Respond.** Then you are done with this ask |
| **Evaluate** | Can we answer it with what we have? What is missing? Is the question bounded? |
| **Prioritize** | Does it support an open incident, or does it sit behind **standing work** (work not tied to a live case, such as a blog read)? |
| **Respond** | Answer the question. Do not rewrite the SOC ticket. Do not open a second case |

If you cannot answer, say what is missing. Do not invent a second question.

**A12** is the classroom incident on workstation **WS-JLEE**. The RFI seed is the update domain / `203.0.113.88`.

**What good looks like:**

- **Evaluate:** The question is “Is the update domain / `203.0.113.88` the **payload host** — the host that served the file — for **A12**?” You have the **Zeek A record** (the name-to-IP the network sensor logged) and the host file (this host logged the talk). The question is bounded. **You can answer.**
- **Prioritize:** An incident is open, and incident response (**IR**) already has the host. **Work now.** Do not put it behind a blog read.
- **Respond:** “**Likely** yes — the update domain / `203.0.113.88` is the payload host for **A12**. Treat it as such.” Not a nation-state paragraph. Not a new incident.

---

## 2. Knowledge Check

1. Answering an RFI means opening a second incident. True or false?
2. What three steps do you take on an RFI?
3. Write a two-sentence **A12** RFI response (no country, no second case).

---

## 3. Summary

The RFI is the question. Receive it, evaluate it, prioritize it, and answer it. Do not rewrite the SOC ticket. Do not open a second case.

**Next:** **2.12.1** Local priorities (obtain, do not invent).

---

## 4. Related modules

- 2.11.2 – Disseminating intelligence to the correct audiences (previous)
- 2.11.1 – Creating finished intelligence products
- 1.5.1 – Report types (SOC type pick)
- 2.12 – Site-specific CTI knowledge (local queue)
- 2.1.4 – Intelligence requirements

---

# Lesson 2.12.1 – Local Intelligence Requirements and Priorities

Source: `modules/02-cti/12-site-specific/01-local-priorities/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.12.1 B / C / C ; 2.12.1.1 3c / 4c / 4c  
- Hunter: 2.12.1 A / A / B ; 2.12.1.1 1a / 1a / 2b  
- SOC: 2.12.1 A / A / A ; 2.12.1.1 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Obtain the shop’s current **Priority Intelligence Requirements (PIRs)** / intelligence priorities, and say that this course does not publish that list.
2. Align analytic work only to a **stated** local requirement — or record that you **do not have the list yet**.

**Mapped Proficiency Items:**
- K: 2.12.1 – Local intelligence requirements and priorities
- T: 2.12.1.1 – Identify current local priorities and align analytic work to them

---

## 1. Key Concepts

CTI analysts obtain the shop’s **current priorities** so analysis answers what leadership already ranked, not whatever looks interesting today. That is the job in this lesson: get the list that is in force here, then say whether a piece of work belongs on it. You do **not** write the shop’s PIR list in this lesson. You do **not** invent one for the classroom firm (**DYA**).

**2.1.4** taught what a PIR *is*: a requirement leadership or the program ranked. This lesson is *this shop’s current* list. Collection planning is **2.1.8**. How a product is produced and approved is **2.12.2**.

Every organization and every section has its own list. A new analyst obtains it early. The list changes. The current one is the one in force now — not last quarter’s copy, and not a classroom ID.

| Idea | What it is |
|------|------------|
| **Current PIRs / priorities** | The ranked questions this shop wants answered *now*. You obtain them. You do not write them here. |
| **Drive analytic focus** | A stated item gets analysis. Work that is only interesting is not assigned. Without a list, you cannot claim a piece of work is aligned. |
| **Obtain-and-follow** | Ask where the current list lives (the role or place your lead names). Use the items on that list. If no one has shown you a list, write **I do not have the list yet.** |

This course does **not** publish DYA’s PIR list. If an instructor overlays a real shop list, that overlay is the list for the room. It is still not DYA policy.

**What good looks like:** someone asks what is current, and whether the desk work belongs there.

- **Identify:** “I obtain the current priority list from [the role or place the instructor names, or my lead]. The current items are the ones on that list.” If none was shown: **“I do not have the list yet.”**
- **Align:** Only to a **stated** item on a list you were shown. **A12** is an open incident on the desk. An incident is not a PIR. You do not mark A12 (or any other work) as aligned until a current local item says so. If there is no list, you do not invent a PIR ID to fill the gap.

Do not write a PIR (**2.1.4**). Do not invent a produce/approve path (**2.12.2**).

---

## 2. Knowledge Check

1. You should invent a DYA PIR list so the class has numbers. True or false?
2. What do you write if the shop has not given you the current list?
3. You have not been shown a current list. Can you mark **A12** as aligned to a local requirement?

---

## 3. Summary

Every shop has current PIRs / priorities. Obtain that list. Align only to a stated item. If you do not have the list, write that. Do not invent PIRs.

**Next:** **2.12.2** Local production and approval processes.

---

## 4. Related modules

- 2.11.3 – Handling RFIs (previous)
- 2.12.2 – Local production and approval processes
- 2.1.4 – Intelligence requirements (PIR concept)
- 2.1.8 – Collection planning

---

# Lesson 2.12.2 – Local production and approval processes

Source: `modules/02-cti/12-site-specific/02-local-production/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.12.2 B / C / C ; 2.12.2.1 3c / 4c / 4c ; 2.12.2.2 3c / 4c / 4c  
- Hunter: 2.12.2 A / A / B ; 2.12.2.1 1a / 1a / 2b ; 2.12.2.2 1a / 1a / 2b  
- SOC: 2.12.2 A / A / A ; 2.12.2.1 1a / 1a / 1a ; 2.12.2.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the local production **workflow** and the required **reviews / approval authorities**, and say how you obtain them.
2. Follow that process for a collection request or a produce/approve step, and document/archive to local standards — or record that you do not have the path yet.

**Mapped Proficiency Items:**
- K: 2.12.2 – Local production and approval processes
- T: 2.12.2.1 – Follow the local process for requesting collection or producing and approving products
- T: 2.12.2.2 – Document and archive intelligence products according to local standards

---

## 1. Key Concepts

A finished draft does not leave the desk just because you wrote it. CTI analysts follow **this shop’s** process to request extra collection, get a product reviewed and approved, and store the official copy. Every shop names the tickets, reviewers, and archive location differently. A new analyst obtains that process early. That is the job in this lesson: obtain the local process and follow it — or record that you do not have it yet.

**2.11.1** wrote the finished product. **2.1.8** is the collection *plan* (source class, first action, what you will not collect). This lesson is the local *request* and the produce / approve / archive process. Classroom channels are **2.11.2**. Local customers are **2.12.3**. This course does not publish a DYA ticket name, approval chain, or archive folder.

| Idea | What it is |
|------|------------|
| **Workflow** | The shop’s sequence from a collection request or a draft through review to an approved product |
| **Reviews** | Someone reads the draft against shop standards before it is official |
| **Approval authorities** | The role allowed to approve so the product can leave as official |

You **obtain** those names here. You do **not** invent them. A form called `INT-REQ-01`, a DYA Jira board, and a change board written as policy are invented. Do not use them.

**Requesting collection** means filing the local request so collection can happen. **Planning** collection — which class, first action, what you will not collect — is **2.1.8**. They are not the same job.

**Document and archive** means the official copy is stored and recorded to **this shop’s** standards. You obtain where that is and how it is documented. You do not invent a folder path.

| You do | You do not |
|--------|------------|
| Ask who reviews, who may approve, what the collection-request step is called here, and where the official copy is stored | Invent `INT-REQ-01`, a DYA Jira board, a change board, or a folder path as policy |
| Follow the process if the instructor overlays a real shop process (they will say it is overlay) | Treat a classroom invention as org policy |
| Write **I do not have the path yet** | Fill a made-up ticket so the class has a form |

**What good looks like:** someone asks you to request collection, or to move a finished product through approval and into the archive. You use the names on the local process you were shown. If no one has shown you the process, you write **I do not have the path yet.** You still do not invent a board, a ticket name, or an archive folder.

---

## 2. Knowledge Check

1. You should invent a DYA ticket name so the class has a form. True or false?
2. What is the local production **workflow**? What are **reviews** and **approval authorities**?
3. You have not been shown the local process. What do you write?

---

## 3. Summary

Obtain the local workflow, the required reviews and approval authorities, and the archive standard. Follow what you were shown. Write **I do not have the path yet** if you were shown none. Do not invent a ticket, a board, or a folder path. The finished draft itself is **2.11.1**.

**Next:** **2.12.3** Local dissemination channels and customers.

---

## 4. Related modules

- 2.12.1 – Local intelligence requirements and priorities (previous)
- 2.12.3 – Local dissemination channels and customers
- 2.11.1 – Creating finished intelligence products
- 2.1.8 – Collection sources and methods
- 2.11.2 – Disseminating intelligence to the correct audiences

---

# Lesson 2.12.3 – Local Dissemination Channels and Customers

Source: `modules/02-cti/12-site-specific/03-local-dissemination/student-guide.md`

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.12.3 B / C / C ; 2.12.3.1 3c / 4c / 4c  
- Hunter: 2.12.3 A / A / B ; 2.12.3.1 1a / 1a / 2b  
- SOC: 2.12.3 A / A / A ; 2.12.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name that this shop has **primary internal and external customers** and **approved dissemination channels**, and say how you **obtain** that chart.
2. Send a product using **those** names — or record that you **do not have the chart yet**. Do not invent a customer list.

**Mapped Proficiency Items:**
- K: 2.12.3 – Local dissemination channels and customers
- T: 2.12.3.1 – Disseminate a product using the correct local channels and customers

---

## 1. Key Concepts

CTI analysts send a **finished product** to the people this shop actually serves, on the path this shop already named. A classroom audience and a classroom channel are not that list. That is the job in this lesson: obtain this shop's named customers and named channels, then send using those names — or write that you do not have the chart yet. Inventing recipients sends the product to the wrong people, or on the wrong path.

**Dissemination** here means sending the finished product. The draft itself is **2.11.1**. Local produce / approve / archive is **2.12.2**. Classroom audience, approved-channel idea, and handling marking (TLP-style) are **2.11.2**. Those classroom names are lesson stand-ins. They are not this organization's customer list, and they are not this organization's channel list.

| Idea | What it is |
|------|------------|
| **Internal customers** | Named recipients **inside** this organization. Obtain the names. Do not guess them. |
| **External customers** | Named recipients **outside** this organization, if the chart includes them. If it does not, do not add a row. |
| **Approved channel / method** | The path this shop named for that send. Obtain that name too. |

**Primary** means the main recipients on the chart, not everyone who might like a copy.

You **obtain** the customer / channel chart from the role or place your lead names. You use the names **on that chart**. You do **not** invent a DYA roster or a DYA distro so the product has somewhere to go. Environment and sensors are **0.8** — not a customer list.

Missing the chart does not authorize an unofficial path. Personal SMS and private chat still fail (**2.11.2**).

**What good looks like:** someone asks you to send the **A12** product. You name how the send is done here, or you say the chart is missing. You do not invent recipients.

- Chart shown: use the customer names and the channel name **on that chart** for **A12**. Do not add a person the chart does not name.
- No chart: **I do not have the chart yet.** Do not invent a distro to complete the send.

This closes **2.x** CTI. Hunt is **3.x**.

---

## 2. Knowledge Check

1. You should invent a DYA customer list so the product has recipients. True or false?
2. How does this lesson differ from **2.11.2**?
3. You have not been shown a chart. What do you write, and what channel do you still **reject**?

---

## 3. Summary

Obtain this shop's customer and channel chart. Use those names. Or write that you do not have it yet. Do not invent recipients. Classroom TLP and classroom channels stay in **2.11.2**. CTI `2.x` ends. Hunt is `3.x`.

**Next:** **3.1** Purpose of threat hunting.

---

## 4. Related modules

- 2.12.2 – Local production and approval (previous)
- 2.11.2 – Classroom dissemination (audience, channel, TLP / marking)
- 2.11.1 – Finished products
- 0.8 – Environment / signal flow
- 3.1 – Purpose of threat hunting
