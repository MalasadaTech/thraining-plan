# Track 0 — shared floor

This is classroom fiction, not live org policy. If a lesson and the story bible disagree, **the bible wins**. Night Owl / Harbor in a lesson means **Pink River Dolphin (PRD)** / **Dixon, Yamada, & Associates (DYA)**.

---

# Lesson 0.1 – How this course is laid out

Source: `modules/00-intro/01-course-layout/student-guide.md`

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (front door)  
**Proficiency Focus:**  
- SOC: 0.1 A / B / B  
- Hunter: 0.1 A / B / B  
- CTI: 0.1 A / B / B  
- DE: 0.1 A / B / B  
**Estimated Time:** 15 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the order of this course: front door, then shared lessons for every role, then four tracks.
2. Say that SOC ends at reporting, and that the RFI is the door into CTI.
3. Name the shared lessons that sit before SOC and apply to everyone.

**Mapped Proficiency Items:**
- K: 0.1 – How this course is laid out

---

## 1. Key Concepts

This course trains four jobs that sit next to each other. Before you sit a track, you have to know **the order of the course** — what applies to everyone, and where the four tracks sit. That is the job in this lesson: name the layout first, so you do not treat a shared lesson as SOC-only, or the SOC track as the whole program.

This lesson is **not** what a SOC is. It is **not** the jobs. It is **not** how work moves.

**Order:** this **front door** (the intro lessons everyone sits first), then **shared lessons** that also apply to every role, then four **tracks** — SOC analyst, then CTI, then hunting, then detection engineers.

| Block | What sits there |
|-------|-----------------|
| **Front door** | This intro — the first lessons everyone sits |
| **Shared lessons** | Still before SOC, and they apply to every role |
| **Four tracks** | SOC analyst, then CTI, then hunting, then detection engineers |

**Inside SOC:** you learn what detections *are* before you live in the alert queue. SOC **ends at reporting (`1.5`)**. The RFI is the door into CTI.

**Still before SOC, for everyone:** **frameworks**, **tool survey**, and **environment / signal flow**. Those are not SOC-only. Role-local hunt / CTI / DE lists come later and differ by shop. Do not invent your shop’s ticket names here.

**Fiction.** This course uses one company and one adversary as fiction, not your site’s policy. Those **names** come in the next lesson. After the lessons, a **companion story** retells the same flow as one incident. We do not write that story in this lesson.

---

## 2. Knowledge Check

1. After this front door, what comes before the four tracks?
2. Where does the SOC track end? What is the door into CTI?
3. Name two shared lessons that sit before SOC and apply to everyone.

---

## 3. Summary

Front door, then shared lessons for everyone, then four tracks: SOC analyst, CTI, hunting, detection engineers. Inside SOC, detections come before the alert queue. SOC ends at reporting. The RFI is the door into CTI. Names of the company and adversary come next.

**Next:** **0.2** What a SOC is.

---

## 4. Related modules

- 0.2 – What a SOC is
- 0.3 – Jobs in one sentence
- 0.4 – How work can move

---

# Lesson 0.2 – What a SOC is

Source: `modules/00-intro/02-what-a-soc-is/student-guide.md`

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.2 A / B / B  
- Hunter: 0.2 A / B / B  
- CTI: 0.2 A / B / B  
- DE: 0.2 A / B / B  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what a **SOC** is.
2. Say that more than one job sits in or next to it.
3. Treat **DYA** and **PRD** as course fiction, not your site’s policy.

**Mapped Proficiency Items:**
- K: 0.2 – What a SOC is

---

## 1. Key Concepts

You will work in or next to a **SOC**. Later lessons name desks and move work between them. That only works if everyone means the same thing by the word. This lesson is that shared meaning: what a SOC is, that more than one job sits nearby, and the company and adversary names this course uses.

**SOC** means Security Operations Center. Your shop may use another door sign. The job is the same.

A SOC is a place that watches for bad or suspicious activity and **starts** the response. It is not every security job in the company.

A SOC is a **team sport**: more than one job sits in or next to the SOC. Who does what is **0.3**. How work moves is **0.4**.

This course uses one company and one adversary as fiction. **DYA** is **Dixon, Yamada, & Associates**, a law firm. **PRD** is **Pink River Dolphin**, the adversary name. Those names are **fiction for this course**. They are not your site’s policy. They are not a hunt order and not your shop’s ticket names.

---

## 2. Knowledge Check

1. In one sentence, what is a SOC?
2. A SOC is a team sport. What does that mean?
3. DYA and PRD are your site’s policy. True or false?

---

## 3. Summary

A SOC watches for bad or suspicious activity and starts the response. Several jobs sit in or next to it. DYA and PRD are course fiction, not your site’s policy.

**Next:** **0.3** Jobs in one sentence.

---

## 4. Related modules

- 0.1 – How this course is laid out
- 0.3 – Jobs in one sentence
- 0.4 – How work can move

---

# Lesson 0.3 – Jobs in one sentence

Source: `modules/00-intro/03-jobs-in-one-sentence/student-guide.md`

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.3 A / B / B  
- Hunter: 0.3 A / B / B  
- CTI: 0.3 A / B / B  
- DE: 0.3 A / B / B  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name each job in **one sentence**.
2. Say which two are **neighbors** this course points at but does not train (IR, and firewall / IA).

**Mapped Proficiency Items:**
- K: 0.3 – Jobs in one sentence

---

## 1. Key Concepts

Work lands as an alert, a question, a hunt, a rule, or a block. Before you take it or send it, you have to know **whose job** it is. That is this lesson: name each desk in one sentence so you do not treat every neighbor as the same work, and so you know which two desks this course only points at.

**0.2** said a SOC is a team sport: more than one job sits in or next to it. This lesson names those jobs. How work moves between them is **0.4**. One person may do more than one job — that is **0.5**.

**RFI** means Request for Information: asking intel for more work on an alert.

| Job | One sentence |
|-----|----------------|
| **SOC analyst** | Work the alert in front of you; start the hand-offs. |
| **Incident response** | Contain and recover. This course **points at** them. It does not train IR. |
| **CTI analyst** | Answer the RFI; add context; find more of the adversary. |
| **Threat hunter** | Look for more activity the alerts missed, from a hunt package or a hypothesis. |
| **Detection engineer** | Turn what we learned into lasting rules. |
| **Firewall / IA** (Information Assurance) | Block what intel names. A **hand-off**, not a track in this course. |

Do not learn how to do each job in this lesson. One sentence each. Stop. This lesson does not name tickets.

---

## 2. Knowledge Check

1. In one sentence, what does the SOC analyst do?
2. Which two jobs does this course point at but not train?
3. What does the detection engineer do, in one sentence?

---

## 3. Summary

Six jobs, one sentence each. IR and firewall / IA are neighbors, not tracks here. How work moves is next.

**Next:** **0.4** How work can move.

---

## 4. Related modules

- 0.2 – What a SOC is
- 0.4 – How work can move
- 0.5 – Where the jobs overlap

---

# Lesson 0.4 – How work can move

Source: `modules/00-intro/04-how-work-moves/student-guide.md`

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- Hunter: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- CTI: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- DE: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name one possible path of work after an alert.
2. Say where extra infrastructure goes, and where a hunt package can go.
3. Given a step in the path, name the next hand-off and whose **product** it is.

**Mapped Proficiency Items:**
- K: 0.4 – How work can move
- T: 0.4.1 – Given a step in the flow, name the next hand-off and whose product it is

---

## 1. Key Concepts

After an alert, work has to go to the next desk. Someone sorts the alert, then they start the hand-offs — to incident response, to leadership, to intel, and later to whoever blocks, hunts, or writes rules. That is the job in this lesson: name **one possible path** those hand-offs can take, and whose product is next. It is not the only way a shop runs. It is not how your site files the ticket.

**0.3** named the jobs. This lesson is how work can move between them.

**RFI** means Request for Information: asking intel for more work on that alert.

**The path:**

1. An analyst gets an alert and **triages** it — sorts what it is and what to do next.
2. They send it to **incident response** and **notify leadership**.
3. They ask intel for more work on that alert (an **RFI**).
4. Intel works the RFI, **enriches** it (adds context), and may find more adversary infrastructure.
5. Extra infrastructure can go to whoever **blocks** (firewall / IA).
6. Intel can also hand hunters a **hunt package**.
7. That same package can go to **detection engineers** to write or tune rules (MDE, YARA, Suricata, SIGMA, and so on).

This is **one possible** path. A shop may skip a step or do two at once. Do not invent a ticket name, a PIR list, or an approval chain.

One person may wear two hats — that is **0.5**.

**What good looks like:** someone names a step. You name the **next hand-off** and **whose product** it is. You do not name how a site files the ticket.

- Given: triage is done. Next: incident response and notify leadership; and/or an RFI to intel. Products: IR contains and recovers; leadership is notified; the RFI is the ask, not intel’s finished work.
- Given: intel found extra infrastructure. Next: whoever **blocks** (firewall / IA). Product: the block. Not a hunt.
- Given: intel has a hunt package. Next: hunters, and that same package can go to detection engineers. Products: a hunt for activity the alerts missed; rules written or tuned.

Do not write the RFI. Do not write the hunt. Do not write the rule.

---

## 2. Knowledge Check

1. After triage, what two things can the analyst do with the alert besides asking intel?
2. Extra infrastructure goes to the hunt team. True or false?
3. Intel found extra infrastructure. Name the next hand-off and whose product it is.

---

## 3. Summary

Alert → triage → IR and leadership → RFI to intel → enrich. Extra infrastructure can be blocked. A hunt package can go to hunters and to detection engineers. Name the next hand-off and whose product it is.

**Next:** **0.5** Where the jobs overlap.

---

## 4. Related modules

- 0.3 – Jobs in one sentence
- 0.5 – Where the jobs overlap

---

# Lesson 0.5 – Where the jobs lightly overlap

Source: `modules/00-intro/05-where-jobs-overlap/student-guide.md`

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.5 A / B / B  
- Hunter: 0.5 A / B / B  
- CTI: 0.5 A / B / B  
- DE: 0.5 A / B / B  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that the same host, log, or domain can sit on more than one desk.
2. Name the **product** that makes each job different — even when one person fills more than one job.

**Mapped Proficiency Items:**
- K: 0.5 – Where the jobs lightly overlap

---

## 1. Key Concepts

The same host, log, or domain can sit on more than one desk. Looking at that evidence is not finishing that desk’s job. That is the job in this lesson: name the **product** you are writing — close or escalate an alert, an intel note, a hunt, or a rule — so you do not treat a look or a question as doing the next job.

Everyone may look at the same **host**, **log**, or **domain**. That does not make the jobs the same.

The **product** is the thing that job finishes. The products are different:

| Product | Whose job |
|---------|-----------|
| Close or escalate an **alert** | SOC analyst |
| An **intel note** | CTI analyst |
| A **hunt** | Threat hunter |
| A **rule** | Detection engineer |

This lesson names those products. It does not teach how to write them.

**Asking** the next desk is not doing that desk’s whole job. A **Request for Information (RFI)** is a question to intel, not the intel note. Handing over a **hunt package** is a hand-off, not the hunt.

A smaller shop may have **one person** fill more than one of these jobs (two hats). This course still names the jobs separately so each **product** stays clear — even if the same person writes two of them.

---

## 2. Knowledge Check

1. Everyone may look at the same host. Does that mean they are doing the same job?
2. Asking the next desk is doing that desk’s whole job. True or false?
3. In a smaller shop, one person may write two products. Why does this course still name the jobs separately?

---

## 3. Summary

The same evidence can sit on more than one desk. The product is what makes the jobs different. Asking is not doing the next job. One person may fill two jobs; they still finish two products.

**Next:** **0.6** Frameworks.

---

## 4. Related modules

- 0.3 – Jobs in one sentence
- 0.4 – How work can move
- 0.6 – Frameworks

---

# Lesson 0.6.1 – MITRE ATT&CK

Source: `modules/00-intro/06-frameworks/01-attck/student-guide.md`

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.1.1 A / B / C ; 0.6.1.2 2b / 3c / 4c  
- Hunter: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- CTI: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- DE: 0.6.1.1 A / B / B ; 0.6.1.2 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what ATT&CK is for, and tell a **tactic** from a **technique** (or **sub-technique**).
2. Given one line of activity, name a tactic and a technique (or sub-technique) and cite the evidence.

**Mapped Proficiency Items:**
- K: 0.6.1.1 – MITRE ATT&CK
- T: 0.6.1.2 – Map observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence

---

## 1. Key Concepts

People on different desks will look at the same host or log. They need one name for **what the adversary was trying to do** and **how**. ATT&CK is that shared language. That is the job in this lesson: label the behavior you saw, so those desks are not using four different names for the same thing.

ATT&CK is a knowledge base of adversary **behavior**. You use it to name what you saw. You do not use it to decorate a ticket.

The **Enterprise** matrix puts **tactics** as columns and **techniques** (and **sub-techniques**) as cells. You do not memorize every cell. You must know what the columns and cells are.

| Piece | What it is |
|-------|------------|
| **Tactic** | *Why* — the goal at that step (Execution, Persistence, Command and Control) |
| **Technique** | *How* — a named way (`T1059` Command and Scripting Interpreter) |
| **Sub-technique** | A more specific how (`T1059.001` PowerShell) |

A finished **map** is that label: tactic + technique or sub-technique + **one cited field**. Read the line of activity in front of you (later lessons may still say **row**; here it means that one log or event). Name the goal. Name the how. Cite one field that actually shows it, such as the command line. If two IDs fit, pick the **primary** for this line and reject the neighbor. An ID with no cited field is not a map.

**What good looks like:** someone gives you one line. You name the tactic and the technique or sub-technique. You cite the field. You do not tell the rest of the incident.

- Given: “`wscript` launched encoded PowerShell.” **Label:** Execution / `T1059.001` PowerShell. **Cite:** the encoded command line. **Not:** Command and Control — this line does not show a beacon.

This is one line of activity, not an alert queue (**1.4**). Hunt planning with ATT&CK is later (**3.5**). Putting IDs on a CTI product is later (**2.7.1**). Diamond is next (**0.6.2**).

---

## 2. Knowledge Check

1. What is a tactic, and what is a technique?
2. An ATT&CK ID with no cited field is a finished map. True or false?
3. Encoded PowerShell ran from a script. Name a tactic and a technique (or sub-technique) and what you would cite.

---

## 3. Summary

ATT&CK labels behavior. A tactic is why. A technique is how. Name both for the line in front of you and cite the field.

**Next:** **0.6.2** Diamond Model.

---

## 4. Related modules

- 0.5 – Where the jobs lightly overlap
- 0.6.2 – Diamond Model
- 0.6.3 – Cyber Kill Chain
- 2.7.1 – ATT&CK for CTI (later)
- 3.5 – Hunt planning with ATT&CK (later)

---

# Lesson 0.6.2 – Diamond Model

Source: `modules/00-intro/06-frameworks/02-diamond-model/student-guide.md`

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.2.1 A / B / C ; 0.6.2.2 2b / 3c / 4c  
- Hunter: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- CTI: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- DE: 0.6.2.1 A / B / B ; 0.6.2.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the four Diamond vertices and say what the model is for.
2. Fill the four vertices from an incident or a short set of indicators and say which vertex is weakest.

**Mapped Proficiency Items:**
- K: 0.6.2.1 – Diamond Model
- T: 0.6.2.2 – Apply the Diamond Model to an incident or set of indicators

---

## 1. Key Concepts

You get an incident or a short set of indicators: a host, a tool, a domain. Someone still wants a group name on the write-up. Before you claim who did it, put what you actually have on four corners and see which corner is empty. That is the job in this lesson: fill the Diamond from evidence, and name the weakest vertex so you do not invent the adversary.

The **Diamond Model** organizes what you know about an activity so you can see what you do **not** know. It is not a verdict. It is not attribution.

The Diamond has four **vertices** (corners):

| Vertex | What goes here |
|--------|----------------|
| **Adversary** | Who (a name only if you have evidence — not a vendor PDF title) |
| **Capability** | What they used (tool, malware, technique) |
| **Infrastructure** | What they used to talk or host (IP, domain, mailbox) |
| **Victim** | Who was hit (host, user, org) |

Fill all four from the evidence you have. Name the **weakest** vertex — the one with the least evidence. That is the next question, not a guess you write as fact. A vendor name on a PDF is not Adversary evidence. A course-fiction name is not Adversary evidence either.

**What good looks like:** encoded PowerShell on a workstation talking to a domain. Victim is that host. Capability is encoded PowerShell. Infrastructure is that domain. Adversary is weakest, because you have no actor evidence. Do not put a course-fiction name in Adversary.

This lesson does not assign ATT&CK IDs (**0.6.1**). Putting Diamond on a CTI product is later (**2.7.2**). Kill Chain is next (**0.6.3**).

---

## 2. Knowledge Check

1. Name the four Diamond vertices.
2. What do you do with the weakest vertex?
3. Encoded PowerShell on a workstation talking to a domain. Which vertex is usually weakest, and why?

---

## 3. Summary

The Diamond Model has four vertices. Fill them from the evidence you have. Name the weakest. Do not invent the adversary.

**Next:** **0.6.3** Cyber Kill Chain.

---

## 4. Related modules

- 0.6.1 – MITRE ATT&CK
- 0.6.3 – Cyber Kill Chain
- 2.7.2 – Diamond Model application in CTI (later)

---

# Lesson 0.6.3 – Cyber Kill Chain

Source: `modules/00-intro/06-frameworks/03-cyber-kill-chain/student-guide.md`

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.3.1 A / B / C ; 0.6.3.2 2b / 3c / 4c  
- Hunter: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- CTI: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- DE: 0.6.3.1 A / B / B ; 0.6.3.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the seven Kill Chain stages and say what the chain is for.
2. Place a one-line activity on one stage and say why it is not the previous or next stage.

**Mapped Proficiency Items:**
- K: 0.6.3.1 – Cyber Kill Chain
- T: 0.6.3.2 – Identify the Kill Chain stage of observed activity

---

## 1. Key Concepts

You often see **one step** of an attack: a file in email, a program that ran, a callback. Before you treat that step as the whole intrusion, you have to name **where it sits in the sequence**. That is the job in this lesson: place the activity you have on one stage, and refuse the previous or next stage you did not see.

The Lockheed Martin **Cyber Kill Chain** shows attack **progression** as a short sequence of stages. It is a staging tool, not a complete model of every intrusion.

You have one activity — one log or one-line description. In a SIEM that often shows up as a **row**. Later lessons may still say “row.” Here it means the activity in front of you.

| Stage | What this stage is |
|-------|--------------------|
| **Reconnaissance** | Researching the target |
| **Weaponization** | Building a deliverable payload |
| **Delivery** | The weapon arrives (email, web, USB) |
| **Exploitation** | It runs against a vulnerability, or as the exploit |
| **Installation** | Code or an implant is on the host |
| **Command and Control** | A callback or control channel |
| **Actions on Objectives** | The goal (theft, encryption, and so on) |

Place **this activity** on **one** stage. Say why it is not the **previous** or **next** stage. Do not invent stages you did not see.

**What good looks like:** someone gives you one line. You name the stage. You reject the neighbor you did not see. You do not fill the rest of the chain.

- Given: “A user received a `.vbs` in email.” **Delivery.** It is not **Weaponization** (you did not see them build it). It is not **Exploitation** (you did not see it run). Do not skip to Command and Control without a callback.

This lesson is **not** ATT&CK (**0.6.1**). It is **not** Diamond (**0.6.2**). Listing every supported stage on an intelligence product is later (**2.7.3**).

---

## 2. Knowledge Check

1. What is the Cyber Kill Chain for?
2. Name the seven stages in order.
3. A user received a `.vbs` in email. Why is that Delivery, and why is it not Exploitation?

---

## 3. Summary

Seven stages. Place the activity you have. Reject the previous or next stage you did not see. Do not invent the rest of the chain.

**Next:** **0.7** External tools (tool survey).

---

## 4. Related modules

- 0.6.1 – MITRE ATT&CK
- 0.6.2 – Diamond Model
- 0.7 – External tools
- 2.7.3 – Cyber Kill Chain in intelligence analysis (later)

---

# Lesson 0.7 – External tools

Source: `modules/00-intro/07-tool-survey/01-external-tools/student-guide.md`

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
- Hunter: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- CTI: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- DE: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
**Estimated Time:** 20 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say the purpose, one strength, and one weakness of VirusTotal, AnyRun, Silent Push, and URLScan.
2. Pick the first external tool for a need and say why the neighbor is the wrong first pick.

**Mapped Proficiency Items:**
- K: 0.7 – External tools (VirusTotal, AnyRun, Silent Push, URLScan)
- T: 0.7.1 – Select the appropriate external tool for a given enrichment or analysis need

---

## 1. Key Concepts

You will get a hash, a file, a domain, or a live URL. Four public tools each answer a different question. That is the job in this lesson: pick the first tool that matches the need, and say why the neighbor is the wrong first pick, so you do not detonate a file when you only needed history, or screenshot a page when you needed a hash reputation.

This is **not** how to search the internal **threat intelligence platform** (**TIP**, **2.3.1**). It is **not** how to read VirusTotal Relations, an AnyRun submission, a Silent Push record, or a URLScan result (**2.9**). You do not need a live vendor account.

**Purpose, strength, weakness.**

| Tool | Purpose | Strength | Weakness |
|------|---------|----------|----------|
| **VirusTotal** | Multi-engine look-up of a file, URL, hash, or IP | Fast reputation | What you submit is public. It is not historical **passive DNS** (past resolutions, also called **PDNS**). It is not a full sandbox story. |
| **AnyRun** | Detonate a **sample** and watch this run | Process tree and dropped files from *this* run | You need a file. Malware can detect the sandbox. It is not infrastructure history. |
| **Silent Push** | Passive DNS / infrastructure clustering | Historical resolutions and sibling domains | Not a detonation. Not a page screenshot. |
| **URLScan** | Scan a **URL / page now** | Redirects, screenshot, and hosts from *this* load | Not PDNS history. Not file behavior. |

**When to pick.**

| Need | First external tool |
|------|---------------------|
| Hash or file reputation | **VirusTotal** |
| You have a binary and need behavior | **AnyRun** |
| Domain or IP *history* or cluster | **Silent Push** |
| Live URL / how the page looks now | **URLScan** |
| “Have we seen this internally?” | **Not these** — that is the internal TIP (**2.3.1**), later |

**What good looks like:** someone gives you a need. You name the first public tool. You reject the neighbor. You do not open a vendor tab.

- Given: a file hash, and you need vendor reputation. **VirusTotal.** Reject AnyRun: you do not have a sample to detonate. Reject Silent Push: this is not a domain-history question.

Platform depth and a Relations graph are later (**2.9**). You do not need a live account in this lesson.

---

## 2. Knowledge Check

1. Give one purpose and one weakness of Silent Push.
2. When do you pick URLScan instead of Silent Push?
3. You have a hash and need reputation. Which tool, and why not AnyRun?

---

## 3. Summary

Four tools. Match the need. Reject the neighbor. Do not open the sandbox when the question is history, and do not treat a page scan as passive DNS.

**Next:** **0.8** Environment / signal flow.

---

## 4. Related modules

- 0.6.3 – Cyber Kill Chain (previous)
- 0.8 – Environment / signal flow (next)
- 2.3.1 – Internal threat intelligence platform (later)
- 2.9 – Platform depth (later)

---

# Lesson 0.8 – Environment / signal flow

Source: `modules/00-intro/08-environment/01-orientation/student-guide.md`

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.8 A / B / C ; 0.8.1 2b / 3c / 4c  
- Hunter: 0.8 B / C / C ; 0.8.1 2b / 3c / 4c  
- CTI: 0.8 A / B / B ; 0.8.1 1a / 2b / 3c  
- DE: 0.8 A / B / B ; 0.8.1 2b / 3c / 4c  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the seven kinds of environment facts every role must obtain from their shop.
2. Given a situation, say which kind applies and why it is not the adjacent kind.

**Mapped Proficiency Items:**
- K: 0.8 – Environment / signal flow
- T: 0.8.1 – Identify which kind of fact applies and why it is not the adjacent kind

---

## 1. Key Concepts

An alert, a hunt, an intel note, and a detection all look at the same host or log. Before you treat a gap as “nothing happened,” you have to know **where your site can see and where it cannot**. That is the job in this lesson: name the **kind** of environment fact you need — how traffic and logs move on this site — take the question to **your shop**, and do not invent a network, a firewall, or a sensor you were not shown. This course does not publish those answers.

**Environment / signal flow** is the site’s infrastructure and how traffic (and the logs of that traffic) move. **0.7** named outside tools. Those tools do not tell you what *this* network can see.

| Kind | What you need from your shop |
|------|------------------------------|
| **Path to the internet / egress** | How traffic leaves for the internet, and where those doors are |
| **Key network segments and data flow** | The main pieces of the network, and how data moves between them |
| **Email flow and related systems** | How mail enters and leaves, and which systems sit on that path |
| **Edge firewall / choke points** | Where the shop can block or see at the edge |
| **Trusted third-party access / federation** | Who else is trusted onto the network |
| **Crown jewel / critical assets** | Which assets are critical. Do not guess them |
| **PCAP collection points / sensors** | Where a sensor sits, and where one does not |

**PCAP / sensors** means where a collector sits. It is not how to read a Zeek log (**1.2**). It is not host-observed network (**1.1.4**) — the host logging that *this device* talked.

A **gap** is still a fact. “No sensor there” is the sensor kind. If no one has shown you the answer, write that you do not have it yet. Do not fill the blank with a classroom network, a ticket name, or the course-fiction firm’s gear.

**What good looks like:** someone gives you a situation. You name the **kind**. You say why the neighbor is the wrong kind. You do not name a firewall you were not shown.

- Given: a user clicked a link and the host talked to the internet. Question: how did that traffic leave? **Path to the internet / egress.** Not **email** — that is how a message arrived. Not **PCAP / sensors** unless the question is whether anything could have recorded that path.
- Given: you need to know whether any collector could have recorded that talk. **PCAP collection points / sensors.** Not a Zeek-field question (**1.2**). Not host-observed network (**1.1.4**).
- Given: you need to know which assets must not be guessed. **Crown jewel / critical assets.** Not **trusted third-party / federation** — that is who else is trusted onto the network.

---

## 2. Knowledge Check

1. Why must every role know where the site can see, and where it cannot?
2. A user clicked a link and the host talked to the internet. You ask how that traffic left. Which kind of fact is that, and why is it not email?
3. You need to know whether any sensor could have recorded that talk. Which kind of fact is that, and why is it not a Zeek-field question?

---

## 3. Summary

Seven kinds of questions. Obtain the answers from your shop. Name the kind that applies and reject the neighbor. A gap is a fact. Do not invent the network.

**Next:** **1.1.1** Endpoint activity (the map).

---

## 4. Related modules

- 0.7 – External tools (previous)
- 1.1.1 – Endpoint activity (next)
- 1.1.4 – Host-observed network (later)
- 1.2 – Zeek (later)
