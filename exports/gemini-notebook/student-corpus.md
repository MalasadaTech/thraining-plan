# Student corpus — Gemini Notebook source

This file is an export for a Gemini Notebook. It is not the syllabus. Do not edit a lesson here. Edit the source file, then rebuild this export in the same change.

This course uses classroom fiction, not live org policy. If a lesson and the story bible disagree, **the bible wins**.

Lessons may still say **Night Owl** and **Harbor**. Those names are **Pink River Dolphin (PRD)** and **Dixon, Yamada, & Associates (DYA)** until the rename pass. Treat “PRD APT” / “Night Owl APT” as a vendor label, not proof of who they are.

Do not invent DYA hunt tickets, PIR lists, approval chains, or a site architecture card. Extra adversary infrastructure is a **block** for firewall / IA (`0.3 f`), not a Detection Engineering job.

Teach order in this file: story bible → shared floor (`0`) → SOC (`1`) → CTI (`2`) → hunt (`3`) → DE (`4`) → companion story.

The companion story is a re-read of the same incident after the lessons. It is not a second plot.

---

# Story bible

Source: `docs/story-bible.md`

Living cheat sheet for the classroom fiction. Lessons and any later companion story must stay consistent with this file. If they disagree, **this file wins**. Add a fact here first, then use it in a lesson.

This is not real org policy. Site-specific lessons still say: hunt tickets, PIR lists, and approval paths vary by site — do not invent those here.

Lessons still say **Night Owl** and **Harbor** until we rename them. Old names are listed so we can find-and-replace later.

---

## Names

| Role | Canonical | Short | Old name in lessons (replace later) |
|------|-----------|-------|-------------------------------------|
| Adversary | Pink River Dolphin | **PRD** | Night Owl, “Night Owl APT” |
| Company | Dixon, Yamada, & Associates | **DYA** | Harbor |
| Company type | Law firm | | Harbor was a generic company with OT / payroll |

“Night Owl APT” stays a **vendor label**, not proof of who they are. After the rename, treat “PRD APT” the same way: a name on a PDF, not a fact unless this bible says otherwise.

---

## People and hosts we are keeping

| Who / what | Fact |
|------------|------|
| User | `jlee` / `BUILDINGC\jlee` |
| Workstation | `WS-JLEE` (`10.10.8.40`) |
| Building C | A DYA office building (was sitting next to “Harbor” with no rule) |

Do not invent first names for Dixon or Yamada unless we add them here on purpose.

---

## Main incident (the plot)

This is the one chain that is “what happened.” Other classroom examples can reuse the names; they are **not** the plot unless we promote them here.

1. `wscript` runs `invoice.vbs` from Temp on **WS-JLEE**.
2. That launches hidden encoded PowerShell (`powershell -enc`).
3. PowerShell sets HKCU Run **`Updater`** → `%TEMP%\update.exe`.
4. The host GET `update.exe` on port **8080** to the PRD update domain / `203.0.113.88`.

SOC flavor already in lessons (keep, rename Harbor/Night Owl later):

- Incident **A12** on WS-JLEE
- RFI to intel on the update domain
- IR **Sam** has the host
- Changeover: outgoing lead **Pat**, incoming lead **Riley**, **Jordan** owns the RFI

---

## Infrastructure (intended vs still in lessons)

| Intended (PRD / DYA) | Still in lessons | Notes |
|----------------------|------------------|-------|
| `prd-updates.net` | `nightowl-updates.net` | Main C2 / payload host |
| `login-prd.net` | `login-nightowl.net` | Sibling: same NS + same A |
| `203.0.113.88` | same | A record for both names |
| `ns1.cdn-test.net`, `ns2.cdn-test.net` | same | Distinctive NS pair |
| `hostmaster.cdn-test.net` | same | SOA RNAME |
| Example Cloud `203.0.113.0/24` | same | Shared hosting — not “theirs” |
| SHA256 of `update.exe` starts `6734f374…` | same | See mismatches |
| First-pass VT on Temp `invoice.vbs` hash | — | **Not in VT**. Classroom result for **1.4.1**. Not Relations. Do not invent the hash string. Not the `update.exe` prefix `6734f374…`. |

Not part of the main plot until we say so: `checkin.nightowl-updates.net` and POST `/api/v1/beacon` (Diamond card only).

---

## DYA site map (from the old Harbor card)

Reuse the numbers. They are classroom stand-ins.

| Fact | Value |
|------|--------|
| User VLAN | `10.10.8.0/24` (WS-JLEE) |
| Servers | `10.10.20.0/24` |
| Management | `10.10.1.0/24` |
| Internet egress | `fw-edge-01` NAT `198.51.100.0/28` |
| Guest Wi-Fi | `fw-guest` (separate door) |
| Mail | `mail-edge` → `mail-filter` → `mail-int` |
| Domain controller | `dc-01` `10.10.20.10` |
| PCAP | `span-1` on fw-edge; `span-2` on user↔server |

**Decided (law firm vs old Harbor map):**

- **OT** (`10.10.50.0/24`, `fw-ot`, `ot-hist-01`, no span on OT) is **not** DYA plot. A law firm does not run that plant network. Do not use OT in the companion story. Leftover classroom examples may still say OT until a rename pass; they are not architecture policy.
- **`pay-db-01`** is **not** this incident. A law firm can have payroll; it is not A12.
- Vendor VPN and payroll SaaS via SAML are **not** this incident.

Do not invent those as DYA policy. Environment questions still go to **your shop** (**0.8**).

---

## Not in this bible

Do not add:

- DYA hunt ticket names or Jira boards
- DYA PIR / priority lists
- DYA approval chains or “who stamps a report”

Those stay “ask your real site.”

---

## Mismatches to clean up when we rename

- Lessons say Night Owl and Harbor; this file says PRD and DYA.
- Building C and Harbor were never one company. Building C is now a DYA building.
- File hash prefix `6734f374…` also appears as a JA3 in the TLS lesson. Easy to mix up. Split them when we touch that lesson.
- `checkin.nightowl-updates.net` / beacon POST is not the main GET `update.exe` chain.
- Side examples (SYSTEM scheduled task, `helpdesk.exe`, Word → `helper.dll`) use the same user/host. They are extra examples, not the plot.

---

## When each fact appears

One chain. Each lesson plants or reads a beat. The **alert** is not the whole incident. The **notification** is not the whole investigation. CTI and hunt add facts the SOC product did not owe.

Do not invent a second plot. Extra classroom examples (`helpdesk.exe`, Word → `helper.dll`) stay off this table.

| Beat (already in “Main incident”) | First teach / plant | First *use* in the flow | Do **not** dump it in |
|-----------------------------------|---------------------|-------------------------|------------------------|
| `wscript` → hidden `powershell -enc` on **WS-JLEE** / `jlee` | **1.1.2** process | **1.4** the alert (this is what fired) | — |
| `invoice.vbs` in Temp (file event, hash) | **1.1.3** file | **1.4.1** investigation; **1.5** notify / escalate (path + hash we have) | Leadership one-liner does not need the hash |
| First-pass VT on that `invoice.vbs` hash: not in VT | **0.7** survey | **1.4.1** first pass | Relations tab; leadership one-liner |
| HKCU Run **`Updater`** → `%TEMP%\update.exe` | **1.1.5** registry | **3.x** hunt (more hosts the alert missed) | Not in the first alert. Not required on the leadership notify |
| Host GET `update.exe` :8080 to PRD domain / `203.0.113.88` | **1.1.4** host-network + **1.2** Zeek | **1.4.1** if they pull PCAP/Zeek; **2.11.3** RFI seed (the domain) | Not all of this in the leadership notify |
| Sibling `login-prd.net`, same NS, same A, SOA | **2.5** / **2.6** / **2.8** | **2.x** enrichment; extra infra → **block** (0.3 f) | Not a SOC notify field |
| Hunt package: look for `Updater` / `update.exe` / more `invoice.vbs` | **3.x** | Hunt product; same package can go to **4.x** DE | Not a rewrite of the SOC ticket |
| Nomination / tune / new rule | **4.x** | After the hunt or SOC “we keep missing this” | Not invented in 1.1 |

**Alert (1.4):** only what a detection would fire on first — the process create (`wscript` → encoded PowerShell).

**Notify / escalate (1.5):** what SOC knows at hand-off — host, user, process chain, the `.vbs` they pulled. One sentence for leadership. The RFI asks intel to work the domain / file, not to rewrite the notify.

**CTI:** more infrastructure and “so what.” **Hunt:** activity the alerts missed. **DE:** lasting rule. Same evidence can sit on more than one desk (**0.4**); the *product* is different.

When we revise a 1.1 / 1.2 / 1.4 / 1.5 lesson, plant or read only that lesson’s beat. Do not retell the whole chain.

---

## Companion story

Written. It retells **this table** from more than one desk. Same facts. Not a different plot.

Spine: SOC gets the alert → triages → IR + leadership notify → RFI to intel → enrich / extra infra to block → hunt package → DE.

Files: [companion-story/](companion-story/). Do not add new plot there until it is in this bible.

---

## How to update this file

When training grows:

1. Add or change the fact here (date it in the git commit; no need for a changelog in the page).
2. Then change the lesson (or the companion story).
3. If you are unsure whether a classroom example is “plot” or “extra example,” leave it off the main incident list.


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


---

# Lesson 1.1.1 – Endpoint activity (the map)

Source: `modules/01-soc/01-endpoint/01-endpoint-activity/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 2b / 2b  
- Hunter: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 1a / 2b  
- CTI: 1.1.1.1 A / A / A ; 1.1.1.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the five kinds of **host activity** this unit will teach.
2. Given a one-line description, say whether it is **process**, **file**, **registry**, **host-network**, or **image/driver load**.

**Mapped Proficiency Items:**
- K: 1.1.1.1 – Endpoint activity (the map)
- T: 1.1.1.2 – Given a one-line description, name the activity type

---

## 1. Key Concepts

An alert usually names a **host** — a laptop, server, or other device. Something on that host generated a log. Before you describe what happened, you have to know **what kind of activity** the log is about. That is the job in this lesson: name the kind first, so you do not mix process, file, and network details into one write-up.

A host generates **logs** when something happens on it. Each log is one **event**. In a SIEM, that event usually shows up as a **row** in a table. Later lessons may still say “row.” Here it means the same thing as the log.

| Kind | What happened |
|------|----------------|
| **Process** | A program ran, ended, or touched another program |
| **File** | A file was created, moved, changed, read, or deleted |
| **Registry** | A key or value was set, deleted, or renamed |
| **Host-network** | This host talked (IP, port, domain) — the *process* started it |
| **Image / driver load** | A DLL or driver was loaded |

**Host-network** means the *host* logged that this device talked. It is not a Zeek lesson. Zeek watches the wire and does not name the process that opened the socket.

**Sysmon** and **MDE** (Microsoft Defender for Endpoint) are two tools that record those **same** five kinds of activity. They use different field names. They are not two different sets of facts. This course uses both as examples. This is **not** how to install Sysmon.

You will learn **one activity type at a time** after this lesson. This lesson only names the five kinds. The next lessons each cover one kind in detail.

This is **endpoint** telemetry: logs from the host itself. Protocol deep-dive is Zeek (**1.2**).

**What good looks like:** someone gives you one line. You name the kind. You do not describe fields yet.

- Given: “A program started on the host.” **Process.**
- Given: “A file appeared in Temp.” **File.**
- Given: “This host connected to an IP and port.” **Host-network.**

Do not tell the rest of the incident. Do not try to read process fields yet (**1.1.2**).

---

## 2. Knowledge Check

1. Sysmon and MDE are two different stories. True or false?
2. “A program started on the host.” Which activity type is that?
3. “This host connected to an IP and port.” Process, or host-network?

---

## 3. Summary

There are five kinds of host activity. Sysmon and MDE record the same kinds with different field names. Name the kind before you describe the event. Zeek is later.

**Next:** **1.1.2** Process activity.

---

## 4. Related modules

- 0.1 – How this course is laid out
- 1.1.2 – Process activity
- 1.2 – Zeek


---

# Lesson 1.1.2 – Process Activity

Source: `modules/01-soc/01-endpoint/02-process-activity/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.2.1 A / B / C ; 1.1.2.2 2b / 3c / 4c ; 1.1.2.3 2b / 3c / 4c  
- Hunter: 1.1.2.1 A / B / B ; 1.1.2.2 1a / 2b / 3c ; 1.1.2.3 1a / 2b / 3c  
- CTI: 1.1.2.1 A / A / A ; 1.1.2.2 1a / 1a / 1a ; 1.1.2.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a process event: create / terminate, parent-child, command line, user, hashes, and process access.
2. Describe what a Sysmon or MDE process event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.2.1 – Process activity concepts
- T: 1.1.2.2 – Analyze a process event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.2.3 – Create a SIEM query to detect specific process activity

---

## 1. Key Concepts

SOC analysts read **process** events on a host to see who ran what. That is daily alert work: an alert names a host, and you have to say which program started, ended, or touched another — from whom, and as whom. **1.1.1** named the five kinds of host activity. This lesson is the **process** kind. It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Process activity** is endpoint telemetry about a running program: it **started**, it **ended**, or one process **touched** another. In a SIEM, that event usually shows up as a row in a process table.

| Idea | What to read |
|------|----------------|
| **Create / terminate** | Sysmon **1** / **5**. MDE create is `ActionType` **ProcessCreated**. Terminate is Sysmon 5 — do not assume `ProcessTerminated` on this table. |
| **PID, name, command line** | `ProcessId`, image/name, `CommandLine` / `ProcessCommandLine`. The image name can be fake. The command line is often what actually ran. |
| **Parent-child** | PPID, parent name, parent command line; MDE `InitiatingProcess*` |
| **Integrity / user** | Integrity level; `User` / account (where logged). Empty is a gap, not “not admin.” |
| **Hash / original filename** | SHA256; `OriginalFileName` (PE resource — can disagree with the on-disk name) |
| **Process access** | Sysmon **10**: source → target (who touched whom). Not a create. |

**How this shows up:** Sysmon **1** / **5** / **10**; MDE `DeviceProcessEvents` (`ActionType`, `InitiatingProcess*`, `ProcessCommandLine`, SHA256). On MDE, the **initiating** process is the parent. Same activity, different field names.

MDE `ActionType` values on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **ProcessCreated** | A process launched | Event **1** |
| **OpenProcess** | A process opened a handle to another (who touched whom) | Event **10** |

The full set is in the Defender portal schema. Do not invent a value. **Terminate** is Sysmon **5**. Do not assume a `ProcessTerminated` event in `DeviceProcessEvents`.

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — who ran what, from whom, as whom. Create, terminate, or access. Do not jump to file, DNS, or registry (**1.1.3**–**1.1.5**).
- Given: `wscript.exe` (Temp `invoice.vbs`) → `powershell.exe -enc …` as `jlee`. **What occurred:** script host launched hidden encoded PowerShell. The hash of `powershell.exe` can still be fine. The parent and command line are what you write down.
- Query: names a **specific** pattern (parent + command-line fragment), not “all processes.”

File, host-network, registry, and image-load events are the next **1.1** lessons.

---

## 2. Knowledge Check

1. Sysmon Event 10 is a process start. True or false?
2. `wscript.exe` (Temp `.vbs`) creates `powershell.exe -enc …`. In one sentence, what occurred?
3. A SIEM query that matches every process is a good “specific process activity” query. True or false?

---

## 3. Summary

A process event tells you who ran what, from whom, as whom. That is a create, a terminate, or an access. Command line and parent are what you trust. A query names a specific pattern.

**Next:** **1.1.3** File system activity.

---

## 4. Related modules

- 1.1.1 – Endpoint activity (the map)
- 1.1.3 – File system activity
- 1.1.4 – Network activity (endpoint)
- 1.2 – Zeek


---

# Lesson 1.1.3 – File System Activity

Source: `modules/01-soc/01-endpoint/03-file-system-activity/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.3.1 A / B / C ; 1.1.3.2 2b / 3c / 4c ; 1.1.3.3 2b / 3c / 4c  
- Hunter: 1.1.3.1 A / B / B ; 1.1.3.2 1a / 2b / 3c ; 1.1.3.3 1a / 2b / 3c  
- CTI: 1.1.3.1 A / A / A ; 1.1.3.2 1a / 1a / 1a ; 1.1.3.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a file event: create / rename-move / delete / modify / read, path, hash, and who touched the file.
2. Describe what a Sysmon or MDE file event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.3.1 – File system activity concepts
- T: 1.1.3.2 – Analyze a file event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.3.3 – Create a SIEM query to detect specific file operations

---

## 1. Key Concepts

SOC analysts read **file** events on a host to see what happened to a file, where, and by which process. That is daily alert work: an alert names a host, and you have to say whether a file was created, renamed or moved, deleted, changed, or read — from which path, and by whom. **1.1.1** named the five kinds of host activity. This lesson is the **file** kind. It is **not** Zeek (`files` / `conn`) (**1.2**). It is **not** how to install Sysmon. It is **not** a process-create write-up (**1.1.2**).

**File system activity** is endpoint telemetry about a file: it was **created**, **renamed or moved**, **deleted**, **modified**, or **read** (where that action is logged). In a SIEM, that event usually shows up as a row in a file table.

| Idea | What to read |
|------|----------------|
| **Create / rename-move / delete / modify / read** | Create = a file appeared. Rename-move = same object, new name or folder. Delete = it is gone. Modify / read = where logged. |
| **Path, name, extension** | Sysmon `TargetFilename`; MDE `FolderPath` + `FileName`. Path is where. Name and extension can lie (`invoice.pdf.exe`). |
| **Hashes** | SHA256 when the event carries it. Empty ≠ clean. Sysmon **11** often has no hash. |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*`. Who did this **to the file**. Not a process-create parent-child write-up (**1.1.2**). |

**How this shows up:** Sysmon **11** (create), **23** (delete, archived), **26** (delete detected); MDE `DeviceFileEvents` (`ActionType`, `FolderPath`, `FileName`, SHA256, `InitiatingProcess*`). Same activity, different field names.

MDE `ActionType` values on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **FileCreated** | A file appeared or was overwritten | Event **11** |
| **FileRenamed** | Same object, new name or folder | Not 11 / 23 / 26 |
| **FileDeleted** | The file is gone | Event **23** / **26** |
| **FileModified** | Content changed — where logged | Not 11 / 23 / 26 |

The full set is in the Defender portal schema. Do not invent a value. **Read** is where that action is logged. Do not assume a `FileRead` event in `DeviceFileEvents`. If your Sysmon feed is only 11 / 23 / 26, rename / modify / read will not be there. Write “not logged,” not “did not happen.”

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — what happened to which file, by whom. Create, rename-move, delete, modify, or read. Do not jump to a process create (**1.1.2**) or Zeek (**1.2**).
- Given: Sysmon **11**, `Image` `wscript.exe`, `TargetFilename` Temp `update.exe`, no hash. **What occurred:** script host created `update.exe` under Temp. Hash not logged. The process create of `wscript` is a different event.
- Query: names a **specific** pattern (initiator + path + extension), not “all file events.”

Host-network, registry, and image-load events are the next **1.1** lessons.

---

## 2. Knowledge Check

1. Sysmon Event 11 is a rename. True or false?
2. `wscript.exe` creates Temp `update.exe` (Sysmon 11, no hash). In one sentence, what occurred?
3. A SIEM query that matches every file event is a good “specific file operation” query. True or false?

---

## 3. Summary

A file event tells you what happened to which file, by whom. Path and initiator are what you trust. A missing hash is a gap. A query names a specific pattern.

**Next:** **1.1.4** Network activity (endpoint).

---

## 4. Related modules

- 1.1.2 – Process activity
- 1.1.4 – Network activity (endpoint)
- 1.1.5 – Registry activity
- 1.2 – Zeek


---

# Lesson 1.1.4 – Network Activity (Endpoint)

Source: `modules/01-soc/01-endpoint/04-network-activity/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.4.1 A / B / C ; 1.1.4.2 2b / 3c / 4c ; 1.1.4.3 2b / 3c / 4c  
- Hunter: 1.1.4.1 A / B / B ; 1.1.4.2 1a / 2b / 3c ; 1.1.4.3 1a / 2b / 3c  
- CTI: 1.1.4.1 A / A / A ; 1.1.4.2 1a / 1a / 1a ; 1.1.4.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a host-network event: IP/port, protocol, direction, domain/URL when logged, and which process talked.
2. Describe what a Sysmon or MDE endpoint network event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.4.1 – Network activity (endpoint) concepts
- T: 1.1.4.2 – Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.4.3 – Create a SIEM query to detect specific endpoint network activity

---

## 1. Key Concepts

SOC analysts read **host-network** events on a host to see which process on this device talked, and to where. That is daily alert work: an alert names a host, and you have to say who opened the socket — to which IP and port, or which name. **1.1.1** named the five kinds of host activity. This lesson is the **host-network** kind. The point of this lesson versus Zeek is the **initiating process**. Zeek watches the wire and does not name the process that opened the socket. It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Network activity (endpoint)** is host telemetry that a process **connected** (or tried to) or issued a **DNS query** (when that is logged here). In a SIEM, that event usually shows up as a row in a network table.

| Idea | What to read |
|------|----------------|
| **Source / dest IP and port, protocol, direction** | Sysmon `Source*` / `Destination*`, `Protocol`, `Initiated`. MDE `Local*` / `Remote*`, `Protocol`. `Initiated=true` = this process started the connection. |
| **Domain / URL when logged** | Sysmon 3 `DestinationHostname`; Sysmon **22** `QueryName` if 22 is in the feed; MDE `RemoteUrl`. Empty ≠ “no DNS happened.” |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*`. **Who talked.** A Zeek `conn` log will not give you this field. |

**How this shows up:** Sysmon **3** (connect) and **22** (DNS, if logged here); MDE `DeviceNetworkEvents` (`ActionType`, `InitiatingProcess*`, `RemoteUrl`, `Local*` / `Remote*`). Same activity, different field names. This is **host-observed** activity. Protocol deep-dive is **1.2**.

MDE `ActionType` values on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **ConnectionSuccess** | This process completed a connection | Event **3** (`Initiated` tells direction) |

The full set is in the Defender portal schema. Do not invent a value. **DNS** on the endpoint is Sysmon **22** when that event is in the feed. If Event **22** is not in the Sysmon feed, write “DNS not logged on the endpoint,” not “no DNS happened.”

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — which process talked, to which IP/port (or which name), which direction. Do not jump to a process create (**1.1.2**), a file drop (**1.1.3**), or a Zeek `conn` / `dns` field (**1.2**).
- Given: MDE `ConnectionSuccess`, `powershell.exe -enc …` → `203.0.113.88:443`, `RemoteUrl` empty. **What occurred:** hidden encoded PowerShell successfully connected outbound TCP/443 to that IP. URL not logged. The process create is a different event.
- Query: names a **specific** pattern (initiator + dest port or remote IP), not “all connections.”

Registry and image-load events are the next **1.1** lessons.

---

## 2. Knowledge Check

1. A Zeek `conn` log names the initiating process. True or false?
2. `powershell.exe -enc …` has `ConnectionSuccess` to `203.0.113.88:443` and no `RemoteUrl`. In one sentence, what occurred?
3. A SIEM query that matches every endpoint network event is a good “specific endpoint network activity” query. True or false?

---

## 3. Summary

A host-network event tells you which process talked, and to where. Direction and initiator tell the story. A missing name is a gap. Zeek does not name the process. A query names a specific pattern.

**Next:** **1.1.5** Registry activity.

---

## 4. Related modules

- 1.1.3 – File system activity
- 1.1.5 – Registry activity
- 1.1.2 – Process activity
- 1.2 – Zeek


---

# Lesson 1.1.5 – Registry Activity

Source: `modules/01-soc/01-endpoint/05-registry-activity/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.5.1 A / B / C ; 1.1.5.2 2b / 3c / 4c ; 1.1.5.3 2b / 3c / 4c  
- Hunter: 1.1.5.1 A / B / B ; 1.1.5.2 1a / 2b / 3c ; 1.1.5.3 1a / 2b / 3c  
- CTI: 1.1.5.1 A / A / A ; 1.1.5.2 1a / 1a / 1a ; 1.1.5.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a registry event: hive, key → value, set / delete / rename, and who changed it.
2. Describe what a Sysmon or MDE registry event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.5.1 – Registry activity concepts
- T: 1.1.5.2 – Analyze a registry event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.5.3 – Create a SIEM query to detect specific registry operations

---

## 1. Key Concepts

SOC analysts read **registry** events on a host to see what changed in a key or value, and which process changed it. That is daily alert work: an alert names a host, and you have to say which hive and key were set, deleted, or renamed — and by whom. **1.1.1** named the five kinds of host activity. This lesson is the **registry** kind. It is **not** a persistence catalog (**3.6**). It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Registry activity** is endpoint telemetry about a **key or value** that was **set**, **deleted**, or **renamed**. In a SIEM, that event usually shows up as a row in a registry table.

| Idea | What to read |
|------|----------------|
| **Hive and key → value** | Hive (`HKLM` / `HKCU`, or `\REGISTRY\MACHINE\` / `\REGISTRY\USER\`). The **key** is the path. The **value** is the named slot plus **data**. Sysmon often writes `HKU\<SID>` for the user hive — that is the same tree as HKCU. |
| **Set / delete / rename** | Set = something was written. Delete = it is gone. Rename = same object, new name. |
| **Example locations** | Run / RunOnce; `...\Services\<name>`. Places you will see. Not a persistence catalog (**3.6**). |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*`. Who changed the key. Not a process-create write-up (**1.1.2**). |

**How this shows up:** Sysmon **12** (create/delete key or value), **13** (SetValue), **14** (rename); MDE `DeviceRegistryEvents` (`ActionType`, `RegistryKey`, `RegistryValueName`, `RegistryValueData`, `InitiatingProcess*`). Same activity, different field names.

MDE `ActionType` values on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **RegistryValueSet** | Data was written to a named value | Event **13** |
| **RegistryKeyCreated** | A key appeared | Event **12** |
| **RegistryKeyDeleted** / **RegistryValueDeleted** | The key or value is gone | Event **12** |
| **RegistryKeyRenamed** | Same key, new name | Event **14** |

The full set is in the Defender portal schema. Do not invent a value. Sysmon **14** also logs value rename. Do not assume an MDE `RegistryValueRenamed` ActionType on this table.

If value data is empty, write “data not logged,” not “empty on purpose.” If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — what happened to which key/value, by whom. Set, delete, or rename. Name Run or Services as a **location** if that is where it sat. Do not deliver a persistence hunt (**3.6**).
- Given: Sysmon **13**, `powershell.exe`, `\REGISTRY\USER\…\Run\Updater` = Temp `update.exe`. **What occurred:** PowerShell set HKCU Run value `Updater` to that Temp path. The file create of `update.exe` is a different event (**1.1.3**).
- Query: names a **specific** pattern (initiator + key path), not “all registry events.”

Image and driver load is the last **1.1** child.

---

## 2. Knowledge Check

1. A Run-key event is a finished persistence hunt. True or false?
2. `powershell.exe` SetValue on HKCU `Run\Updater` = Temp `update.exe`. In one sentence, what occurred?
3. A SIEM query that matches every registry event is a good “specific registry operation” query. True or false?

---

## 3. Summary

A registry event tells you what changed in the hive, by whom. That is a set, a delete, or a rename. Key, value, and initiator are what you write down. Run and Services are locations, not a hunt course. A query names a specific pattern.

**Next:** **1.1.6** Image and driver load.

---

## 4. Related modules

- 1.1.1 – Endpoint activity (the map)
- 1.1.3 – File system activity
- 1.1.4 – Network activity (endpoint)
- 1.1.6 – Image and driver load
- 1.2 – Zeek
- 3.6.1 – Persistence techniques (later)


---

# Lesson 1.1.6 – Image and Driver Load Activity

Source: `modules/01-soc/01-endpoint/06-image-driver-load/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.6.1 A / B / C ; 1.1.6.2 2b / 3c / 4c ; 1.1.6.3 2b / 3c / 4c  
- Hunter: 1.1.6.1 A / B / B ; 1.1.6.2 1a / 2b / 3c ; 1.1.6.3 1a / 2b / 3c  
- CTI: 1.1.6.1 A / A / A ; 1.1.6.2 1a / 1a / 1a ; 1.1.6.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read an image or driver load event: user-mode image vs kernel driver, path, hash, signed vs unsigned (where logged), and who loaded it.
2. Describe what a Sysmon or MDE image or driver load event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.6.1 – Image and driver load activity concepts
- T: 1.1.6.2 – Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.6.3 – Create a SIEM query to detect specific image or driver load activity

---

## 1. Key Concepts

SOC analysts read **image and driver load** events on a host to see that a module entered a process, or that a driver entered the kernel. That is daily alert work: an alert names a host, and you have to say what was loaded, into whom (or into the kernel), from where, and whether it was signed if that is logged. **1.1.1** named the five kinds of host activity. This lesson is the **image / driver load** kind. It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Image and driver load activity** is endpoint telemetry that a **user-mode image** (usually a DLL) was mapped into a process, or that a **kernel driver** was loaded. In a SIEM, that event usually shows up as a row in a table.

| Idea | What to read |
|------|----------------|
| **User-mode vs kernel** | User-mode = a process loaded a module (Sysmon **7** / MDE). Kernel = a driver entered the kernel (Sysmon **6**). Not a process start. |
| **Path, hashes, signed vs unsigned** | Path is where it loaded from (Sysmon `ImageLoaded`; MDE `FolderPath` + `FileName`). Hashes of the loaded bytes when present (SHA256; MDE often carries SHA1 instead). `Signed` / signature fields **where logged**. Empty is a gap, not “unsigned.” |
| **Initiating process** | Sysmon 7 `Image` is the process; `ImageLoaded` is the module. MDE `InitiatingProcess*` is the process that loaded the module. Event **6** is kernel-wide — it has no user-mode parent field. Do not invent one. |

**How this shows up:** Sysmon **6** (driver) / **7** (image load); MDE `DeviceImageLoadEvents`. Same activity, different field names. Event **7** is noisy and often sampled or off. If you have no 7 / no `DeviceImageLoadEvents`, write “image load not logged.” Do not invent a load from a file-create event (**1.1.3**).

MDE `ActionType` on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **ImageLoaded** | A process loaded a module | Event **7** |

`DeviceImageLoadEvents` is DLL load activity. Driver load on the endpoint is Sysmon **6**. Do not treat a `.sys` path on this MDE table as a kernel driver load, and do not invent a driver `ActionType` here. The full set is in the Defender portal schema.

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — what was loaded, into whom (or into the kernel), from where, signed or not if logged. Do not jump to a file create (**1.1.3**) or a persistence / BYOVD write-up.
- Given: Sysmon **7**, `Image` `powershell.exe`, `ImageLoaded` Temp `update.dll`, `Signed=false`. **What occurred:** PowerShell loaded an unsigned DLL from Temp. The file create of that DLL, if you have one, is a different event.
- Query: names a **specific** pattern (process + path, or Event **6** + driver path), not every image or driver load.

This is the last **1.1** host-activity lesson. Protocol deep-dive is **1.2**.

---

## 2. Knowledge Check

1. Sysmon Event 6 is a DLL load into a process. True or false?
2. `powershell.exe` loads Temp `update.dll` (`Signed=false`). In one sentence, what occurred?
3. A SIEM query that matches every image or driver load event is a good “specific image or driver load” query. True or false?

---

## 3. Summary

An image or driver load event is a module entering a process, or a driver entering the kernel. Path and initiator tell the story. Signed empty is a gap. A file create is not a load. A query names a specific pattern.

**Next:** **1.2.1** Zeek concepts.

---

## 4. Related modules

- 1.1.1 – Endpoint activity (the map)
- 1.1.5 – Registry activity
- 1.1.3 – File system activity
- 1.2.1 – Zeek concepts


---

# Lesson 1.2.1 – Zeek Concepts

Source: `modules/01-soc/02-zeek/01-concepts/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.1.1 A / B / C  
- Hunter: 1.2.1.1 B / C / C  
- CTI: 1.2.1.1 A / B / B  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what Zeek is, and what an engine does.
2. Say why you pull PCAP when you already have a Zeek log.

**Mapped Proficiency Items:**
- K: 1.2.1.1 – Zeek concepts

---

## 1. Key Concepts

An alert can name traffic on the **wire**, not only a host. A network sensor generated a log. Before you describe that traffic, you have to know what **Zeek** is: a framework that watched the wire and wrote structured fields. That is the job in this lesson: say what Zeek is, what an engine does, and why you still pull PCAP.

**1.1** was host and endpoint activity — logs from the host. This unit is **network-sensor** telemetry. Zeek watches the wire and writes structured logs. It does **not** name the initiating process. That field is host-network activity (**1.1.4**).

**Zeek** is a network analysis framework. It is not primarily a signature IDS. It classifies traffic and writes logs you query in a SIEM.

**Engines** (scripts / analyzers) look at a flow, decide what protocol it is, and **extract** the fields for that protocol. That is how applications and protocols **surface** (show up) as logs you can query. Conn, DNS, TLS, HTTP, SMTP, files, and weird are later lessons. This lesson is only that they exist and that they surface applications and protocols as logs.

**PCAP** is a packet capture — the usual next artifact. A Zeek log is an **extract**: the fields an engine already wrote. You pull PCAP to **verify** that extract, or to **expand** what the log does not carry. This is not a PCAP analysis course. This lesson does not teach Wireshark or the site download path.

**What good looks like:** you can say Zeek is the sensor log, an engine extracted the protocol, and PCAP is how you check or fill a gap. You do not open `conn` fields yet (**1.2.2**).

---

## 2. Knowledge Check

1. Zeek is primarily a signature-based IDS. True or false?
2. What does an engine do?
3. You already have a Zeek log. Why pull PCAP?

---

## 3. Summary

Zeek writes structured logs from the wire. Engines extract protocol. PCAP verifies or expands the extract. The process name is on the host log, not here.

**Next:** **1.2.2** Conn engine.

---

## 4. Related modules

- 1.1.6 – Image and driver load (previous)
- 1.1.4 – Network activity (endpoint)
- 1.2.2 – Conn engine


---

# Lesson 1.2.2 – Conn Engine

Source: `modules/01-soc/02-zeek/02-conn-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.2.1 A / B / C ; 1.2.2.2 2b / 3c / 4c ; 1.2.2.3 2b / 3c / 4c  
- Hunter: 1.2.2.1 B / C / C ; 1.2.2.2 3c / 4c / 4c ; 1.2.2.3 3c / 4c / 4c  
- CTI: 1.2.2.1 A / A / B ; 1.2.2.2 1a / 1a / 2b ; 1.2.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `conn` event: originator and responder IP and port, and how the connection ended.
2. Describe what a `conn` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.2.1 – Conn engine
- T: 1.2.2.2 – Analyze a Zeek conn log and accurately describe what occurred
- T: 1.2.2.3 – Create a SIEM query to detect specific connection activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`conn`** log to see who talked to whom on the **wire**, and how the connection ended. That is daily alert work: an alert names an IP or a connection, and you have to say which address started the talk, which address was contacted, on which ports, and whether the attempt completed, sat unanswered, or was refused. **1.2.1** taught that Zeek engines extract protocol data from the wire. This lesson is the **`conn`** extract. It does **not** name the initiating process. That is host-network telemetry (**1.1.4**).

The **`conn`** log is one **event** per connection Zeek saw. In a SIEM, that event usually shows up as a **row** in a table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **Source IP** | `id.orig_h` — **originator** IP. Who started the talk from Zeek’s view. Not automatically an internal host. |
| **Source port** | `id.orig_p` — originator port |
| **Destination IP** | `id.resp_h` — **responder** IP. Who was contacted. |
| **Destination port** | `id.resp_p` — responder port |
| **Connection state / history** | `conn_state` / `history`. How it ended, and a short flag string of what was seen (`S` SYN, `H` SYN-ACK, `F` FIN, `R` RST) |

**States you will use:** **`SF`** = established and torn down cleanly. **`S0`** = attempt, no reply. **`REJ`** = attempt refused. If you see another state, say what the field shows. Do not invent a story the flags do not support.

`id.orig_h` is the originator, not the destination. Originator is not a synonym for “our network.” Zeek labels the side that started the talk, wherever that address lives.

This is the **extract**. PCAP still verifies or expands (**1.2.1**). Do not open DNS or TLS fields yet.

**What good looks like:**

- Describe: one sentence — originator IP/port → responder IP/port, state. Do not name a process. Do not call it C2 from port 443 alone.
- Given: `id.orig_h` a workstation, `id.resp_h` `203.0.113.88`, `id.resp_p` `443`, `conn_state` `SF`. **What occurred:** that host completed a TCP connection to `203.0.113.88:443`. Who launched the socket is on the **host** (**1.1.4**).
- Query: names a **specific** pattern (responder IP or port + state), not every connection.

DNS fields are the next Zeek lesson (**1.2.3**).

---

## 2. Knowledge Check

1. `id.orig_h` is the destination IP. True or false?
2. Workstation → `203.0.113.88:443`, `conn_state` `SF`. In one sentence, what occurred?
3. A SIEM query that matches every connection is a good “specific connection activity” query. True or false?

---

## 3. Summary

A `conn` event is who talked to whom, on which ports, and how it ended. State and history are on the wire. The process is not. A query names a specific pattern.

**Next:** **1.2.3** DNS engine.

---

## 4. Related modules

- 1.2.1 – Zeek concepts
- 1.2.3 – DNS engine
- 1.1.4 – Host-observed network


---

# Lesson 1.2.3 – DNS Engine

Source: `modules/01-soc/02-zeek/03-dns-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.3.1 A / B / C ; 1.2.3.2 2b / 3c / 4c ; 1.2.3.3 2b / 3c / 4c  
- Hunter: 1.2.3.1 B / C / C ; 1.2.3.2 3c / 4c / 4c ; 1.2.3.3 3c / 4c / 4c  
- CTI: 1.2.3.1 A / B / B ; 1.2.3.2 1a / 2b / 3c ; 1.2.3.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `dns` log: question, answer, record type, and who asked which DNS server.
2. Describe what a `dns` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.3.1 – DNS engine
- T: 1.2.3.2 – Analyze a Zeek DNS log and accurately describe what occurred
- T: 1.2.3.3 – Create a SIEM query to detect specific DNS activity

---

## 1. Key Concepts

SOC analysts read Zeek **`dns`** logs to see a name lookup on the **wire**. That is daily alert work: an alert names a domain or a lookup, and you have to say who asked, for which name, which type, and what came back. **1.2.2** was the connection. This lesson is the **DNS** extract. It does **not** name the initiating process. That was **1.1.4**. It is **not** TLS (**1.2.4**).

The DNS engine writes the **`dns`** log. Each log is one **event** for a query (and the response Zeek saw). In a SIEM, that event usually shows up as a **row** in a dns table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **Query (question)** | `query` — the name that was asked |
| **Response (answer)** | `answers` — what came back (an address, another name, or empty) |
| **Record type** | `qtype_name` — **A**, **AAAA**, **MX**, **CNAME**, **NS**, **TXT**, and the rest when you see them |
| **Source / dest** | `id.orig_h` = who asked. `id.resp_h` = the DNS server that was asked |

`id.resp_h` is often a recursive resolver. It is **not** the address the name resolved to. That value, when present, is in `answers`.

| `qtype_name` | What was asked for |
|--------------|-------------------|
| **A** | IPv4 address |
| **AAAA** | IPv6 address |
| **MX** | Mail exchanger |
| **CNAME** | Another name (canonical name), not an address |
| **NS** | Name server |
| **TXT** | Text data |

A **CNAME** answer is another name, not an address. An empty `answers` list means this log does not show a returned record — say that. Do not invent NXDOMAIN hunting or DGA methodology here.

This is the **extract**. PCAP still verifies or expands (**1.2.1**). Do not open TLS or HTTP fields yet.

**What good looks like:**

- Describe: one sentence — who asked, for which name, which type, what answered. Do not name a process. Do not call it C2 from a single A record.
- Given: `id.orig_h` a workstation, `query` a hostname, `qtype_name` `A`, `answers` `["203.0.113.88"]`. **What occurred:** that host asked for that name and got **A** `203.0.113.88`. The TCP connection to `:443` is a different log (**1.2.2**). Who launched the lookup is on the **host** (**1.1.4**).
- Query: names a **specific** pattern (`query`, `qtype_name`, or `answers`), not every `dns` event.

---

## 2. Knowledge Check

1. `id.resp_h` on a `dns` log is the IP the name resolved to. True or false?
2. Workstation queries a hostname, type `A`, answers `["203.0.113.88"]`. In one sentence, what occurred?
3. A SIEM query that matches every `dns` log is a good “specific DNS activity” query. True or false?

---

## 3. Summary

A `dns` log is the question, the type, the answer, and who asked which DNS server. The process is not on this log. A query names a specific pattern.

**Next:** **1.2.4** TLS engine.

---

## 4. Related modules

- 1.2.2 – Conn engine (previous)
- 1.2.4 – TLS engine
- 1.1.4 – Host-observed network


---

# Lesson 1.2.4 – TLS Engine

Source: `modules/01-soc/02-zeek/04-tls-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.4.1 A / B / C ; 1.2.4.2 2b / 3c / 4c ; 1.2.4.3 2b / 3c / 4c  
- Hunter: 1.2.4.1 B / C / C ; 1.2.4.2 3c / 4c / 4c ; 1.2.4.3 3c / 4c / 4c  
- CTI: 1.2.4.1 A / A / B ; 1.2.4.2 1a / 1a / 2b ; 1.2.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a TLS event: SNI, certificate subject and issuer, JA3 where logged, version, cipher, and who talked to whom.
2. Describe what a Zeek TLS log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.4.1 – TLS engine
- T: 1.2.4.2 – Analyze a Zeek TLS log and accurately describe what occurred
- T: 1.2.4.3 – Create a SIEM query to detect specific TLS activity

---

## 1. Key Concepts

SOC analysts read Zeek **TLS** events to see the **handshake** when the payload is encrypted. That is daily alert work: traffic on 443 still needs a description — who talked to whom, which hostname the client asked for, what name is on the certificate, and which version and cipher were negotiated. This lesson is the **TLS** engine. Zeek writes it to the **`ssl`** log (the name is historical). It is **not** decrypted HTTP. It does **not** name the initiating process. That is host-observed network (**1.1.4**).

Each handshake Zeek saw is one **event** in that log. In a SIEM, that event usually shows up as a **row**. Later lessons may still say “row.” Here it means the same thing as the TLS log.

| Idea | What to read |
|------|----------------|
| **SNI** | `server_name` — the hostname in the Client Hello. Empty means it was not sent or not logged. |
| **Subject / issuer** | `subject` / `issuer` — the name on the certificate, and who signed it. SNI is not the certificate subject. |
| **JA3 / JA3S** | Client / server TLS fingerprints **where the shop logs them**. Missing means not logged, not “no TLS.” |
| **Version / cipher** | `version`, `cipher` — what was negotiated |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` — originator to responder |

JA3 is how the client spoke TLS, not a malware name. Do not treat a JA3 value as a verdict. Do not invent a JA3 value. If the field is empty, say so.

This is the **extract**. PCAP still verifies or expands (**1.2.1**). Do not open HTTP fields yet (**1.2.5**).

**What good looks like:**

- Describe: one sentence — who talked to whom, SNI if present, subject/issuer, version/cipher, JA3 only if logged. Do not name a process. Do not call it phishing from one SNI and subject mismatch.
- Given: `id.resp_h` `203.0.113.88`, `id.resp_p` `443`, `server_name` empty, `version` / `cipher` present. **What occurred:** that host completed a TLS handshake to `203.0.113.88:443`. SNI was not logged.
- Query: names a **specific** pattern (SNI, subject, version, or dest IP/port), not every `ssl` event.

---

## 2. Knowledge Check

1. `server_name` is the name on the server certificate. True or false?
2. Workstation → `203.0.113.88:443`, `server_name` empty, version and cipher present. In one sentence, what occurred?
3. A SIEM query that matches every `ssl` event is a good “specific TLS activity” query. True or false?

---

## 3. Summary

A TLS event is the handshake: SNI, certificate, version, cipher, and who talked to whom. JA3 only if logged. The process is not on this log. A query names a specific pattern.

**Next:** **1.2.5** HTTP engine.

---

## 4. Related modules

- 1.2.3 – DNS engine (previous)
- 1.2.5 – HTTP engine
- 1.2.2 – Conn engine
- 1.1.4 – Host-observed network


---

# Lesson 1.2.5 – HTTP Engine

Source: `modules/01-soc/02-zeek/05-http-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.5.1 A / B / C ; 1.2.5.2 2b / 3c / 4c ; 1.2.5.3 2b / 3c / 4c  
- Hunter: 1.2.5.1 B / C / C ; 1.2.5.2 3c / 4c / 4c ; 1.2.5.3 3c / 4c / 4c  
- CTI: 1.2.5.1 A / B / B ; 1.2.5.2 1a / 2b / 3c ; 1.2.5.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `http` log: method, host, URI, User-Agent, status, and who talked to whom.
2. Describe what an `http` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.5.1 – HTTP engine
- T: 1.2.5.2 – Analyze a Zeek HTTP log and accurately describe what occurred
- T: 1.2.5.3 – Create a SIEM query to detect specific HTTP activity

---

## 1. Key Concepts

SOC analysts read Zeek **HTTP** logs to see a request and response on the **wire**. That is daily alert work: an alert names a web request, and you have to say which method, host, and URI were used, what status came back, and who talked to whom. **1.2.4** was the TLS handshake. This lesson is **HTTP**. It does **not** name the initiating process. That is host telemetry (**1.1.4**). It is **not** the file extract (**1.2.7**).

The **`http`** log is one **event** for a request/response pair Zeek parsed. In a SIEM, that event usually shows up as a row in an HTTP table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **Method** | `method` — GET, POST, PUT, HEAD, and the rest when you see them |
| **Host** | `host` — the Host header. Empty means it was not logged. This is not the destination IP. |
| **URI / URL** | `uri` is the path and query. **Host + URI** is the URL you describe. There is often no single `url` field. |
| **User-Agent** | `user_agent` — what the client claimed. It can lie. Empty means it was not logged. |
| **Status** | `status_code` — 200 is not “benign.” 404 is not “safe.” |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` |

**How this shows up:** Zeek `http` (`method`, `host`, `uri`, `user_agent`, `status_code`, `id.orig_*`, `id.resp_*`).

You usually do **not** get the body. File extract is **1.2.7**. Encrypted HTTPS often has no `http` log — that is the `ssl` extract (**1.2.4**).

If a field is empty, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — method, host+URI, status, User-Agent if logged, orig → resp. Do not name a process. Do not invent the body.
- Given: `GET`, `uri` `/update.exe`, `id.resp_h` `203.0.113.88`, `id.resp_p` `8080`, `status_code` `200`, `user_agent` empty. **What occurred:** the originator requested **GET** `/update.exe` from `203.0.113.88` on port **8080** and received status **200**. User-Agent was not logged. Do not mix this with a TLS handshake (**1.2.4**).
- Query: names a **specific** pattern (method, host, URI, User-Agent, or dest), not every `http` log.

---

## 2. Knowledge Check

1. `host` is the destination IP. True or false?
2. `GET /update.exe` to `203.0.113.88:8080`, status `200`, User-Agent empty. In one sentence, what occurred?
3. A SIEM query that matches every `http` log is a good “specific HTTP activity” query. True or false?

---

## 3. Summary

An `http` log is method, host+URI, User-Agent, status, and who talked to whom. The process is not on this log. A query names a specific pattern.

**Next:** **1.2.6** SMTP engine.

---

## 4. Related modules

- 1.2.4 – TLS engine (previous)
- 1.2.6 – SMTP engine
- 1.2.7 – Files engine
- 1.1.4 – Host-observed network


---

# Lesson 1.2.6 – SMTP Engine

Source: `modules/01-soc/02-zeek/06-smtp-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.6.1 A / B / C ; 1.2.6.2 2b / 3c / 4c ; 1.2.6.3 2b / 3c / 4c  
- Hunter: 1.2.6.1 B / C / C ; 1.2.6.2 3c / 4c / 4c ; 1.2.6.3 3c / 4c / 4c  
- CTI: 1.2.6.1 A / A / B ; 1.2.6.2 1a / 1a / 2b ; 1.2.6.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `smtp` log: mail from, rcpt to, subject, message ID, and who talked to whom.
2. Describe what an `smtp` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.6.1 – SMTP engine
- T: 1.2.6.2 – Analyze a Zeek SMTP log and accurately describe what occurred
- T: 1.2.6.3 – Create a SIEM query to detect specific SMTP activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`smtp`** log to see a mail transaction on the **wire**. That is daily alert work: an alert names a session, and you have to say who the session claimed mail was from and to, what subject was logged, and which hosts talked. It is **not** a mailbox. It is **not** the attachment bytes — those are **1.2.7**. It does **not** name the initiating process. That was **1.1.4**.

**SMTP activity** is network-sensor telemetry about a mail transaction Zeek parsed: envelope sender, envelope recipients, a few headers, and who talked to whom. In a SIEM, that event usually shows up as a row in an `smtp` table.

| Idea | What to read |
|------|----------------|
| **Mail from** | `mailfrom` — envelope MAIL FROM. Who the *session* claimed as sender. Not the From header. |
| **Rcpt to** | `rcptto` — envelope RCPT TO (can be more than one address) |
| **Subject** | `subject` — the Subject header. Empty = not logged. Easy to spoof. |
| **Message ID** | `msg_id` — Message-ID when logged. Not a file hash. |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` (often 25 / 587) |

Zeek watches the wire and writes this log. Encrypted submission may have no SMTP fields — that handshake was **1.2.4**. Empty `subject` or `msg_id` means not logged, not “no mail.” Do not invent a mail-gateway name.

**What good looks like:**

- Describe: one sentence — envelope from, envelope to, subject if logged, orig → resp. Do not name a process. Do not declare phishing.
- Given: `mailfrom` an outside address, `rcptto` a user, `subject` present, `msg_id` present. **What occurred:** that client sent envelope mail from A to B with that subject.
- Query: names a **specific** pattern (`mailfrom`, `rcptto`, subject, or dest), not “all `smtp` events.”

---

## 2. Knowledge Check

1. `mailfrom` is the attachment hash. True or false?
2. Envelope from an outside address, `rcptto` a user, subject present. In one sentence, what occurred?
3. A SIEM query that matches every `smtp` event is a good “specific SMTP activity” query. True or false?

---

## 3. Summary

An `smtp` log is envelope from/to, subject, message ID, and who talked to whom. The process and the attachment hash are not on this event. A query names a specific pattern.

**Next:** **1.2.7** Files engine.

---

## 4. Related modules

- 1.2.5 – HTTP engine (previous)
- 1.2.7 – Files engine
- 1.2.4 – TLS engine
- 1.1.4 – Host-observed network


---

# Lesson 1.2.7 – Files Engine

Source: `modules/01-soc/02-zeek/07-files-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.7.1 A / B / C ; 1.2.7.2 2b / 3c / 4c ; 1.2.7.3 2b / 3c / 4c  
- Hunter: 1.2.7.1 B / C / C ; 1.2.7.2 3c / 4c / 4c ; 1.2.7.3 3c / 4c / 4c  
- CTI: 1.2.7.1 A / A / B ; 1.2.7.2 1a / 1a / 2b ; 1.2.7.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek **files** event: name, MIME type, hash, who sent and received it, and the connection UID that joins other Zeek logs.
2. Describe what a `files` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.7.1 – Files engine
- T: 1.2.7.2 – Analyze a Zeek files log and accurately describe what occurred
- T: 1.2.7.3 – Create a SIEM query to detect specific file transfer activity

---

## 1. Key Concepts

SOC analysts read the Zeek **files** log to see a file on the **wire**. An alert may name a download, an attachment, or a hash. The job in this lesson is to say what moved: the name if the protocol gave one, the MIME type, the hash if Zeek calculated it, who sent it, and who received it. **1.2.1** said engines extract protocol. This lesson is the **files** engine. It is **not** host file activity (**1.1.3**). It is **not** YARA (**1.3**).

The **files** log is one **event** for a file Zeek analyzed on the wire. In a SIEM, that event usually shows up as a **row** in a files table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **File name** | `filename` — when the protocol gave one. It can lie. Empty means not logged. |
| **MIME type** | `mime_type` — what Zeek thinks the bytes are (for a Windows executable, often `application/x-dosexec`). It can disagree with the name. |
| **Hash** | `md5` / `sha1` / `sha256` when calculated. Empty is not “clean.” Do not invent a hash. |
| **Source / dest** | `tx_hosts` sent the bytes. `rx_hosts` received them. These are not `id.orig_h` / `id.resp_h`. |
| **Connection UID** | `conn_uids` — those values *are* the `uid` on `conn` / `http` / `smtp`. Copy one and search. |

This is the **extract**. Zeek does not have to write the bytes to disk. The host may or may not create a file. A Temp path on the host is a different sensor (**1.1.3**).

**What good looks like:**

- Describe: one sentence — name if logged, MIME, hash if logged, who sent to whom. Then say which `uid` you would open on `conn` or `http`. Do not describe a Sysmon 11.
- Given: `filename` `update.exe`, `mime_type` `application/x-dosexec`, `sha256` present, `tx_hosts` `203.0.113.88`, `rx_hosts` a workstation, `conn_uids` present. **What occurred:** that IP sent `update.exe` (executable MIME, hash logged) to that host on the wire. Copy `conn_uids` and search the other Zeek logs. The Temp file-create is **1.1.3**.
- Query: names a **specific** pattern (name, MIME, hash, or tx/rx), not every `files` event.

---

## 2. Knowledge Check

1. A Zeek `files` event is the same thing as a Sysmon 11 file create. True or false?
2. `update.exe`, MIME `application/x-dosexec`, hash logged, from `203.0.113.88` to a workstation. In one sentence, what occurred?
3. A SIEM query that matches every `files` event is a good “specific file transfer” query. True or false?

---

## 3. Summary

A `files` event is a transfer on the wire: name, MIME, hash, who sent and received. `conn_uids` joins `conn` / `http` / `smtp`. The host file event is a different sensor.

**Next:** **1.2.8** Weird engine.

---

## 4. Related modules

- 1.2.6 – SMTP engine (previous)
- 1.2.5 – HTTP engine
- 1.2.8 – Weird engine
- 1.1.3 – File system activity (host)


---

# Lesson 1.2.8 – Weird Engine

Source: `modules/01-soc/02-zeek/08-weird-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.8.1 A / B / C ; 1.2.8.2 2b / 3c / 4c ; 1.2.8.3 2b / 3c / 4c  
- Hunter: 1.2.8.1 B / C / C ; 1.2.8.2 3c / 4c / 4c ; 1.2.8.3 3c / 4c / 4c  
- CTI: 1.2.8.1 A / A / A ; 1.2.8.2 1a / 1a / 1a ; 1.2.8.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek **weird** log: the type, who talked to whom, and the UID that joins other Zeek logs.
2. Describe what a **weird** log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.8.1 – Weird engine
- T: 1.2.8.2 – Analyze a Zeek weird log and accurately describe what occurred
- T: 1.2.8.3 – Create a SIEM query to detect specific weird activity

---

## 1. Key Concepts

SOC analysts read the Zeek **weird** log when the sensor saw protocol behavior that is off-spec or uncommon. That is daily alert work: a log names a type, two endpoints, and often a connection ID, and you have to say what Zeek flagged — not whether it is an incident. A **weird** event is a **lead**, not a verdict. It does **not** name the initiating process. That was **1.1.4**.

Zeek watches the **wire**. Each **weird** log is one **event**. In a SIEM, that event usually shows up as a **row** in a table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **Type / notice** | `name` — the weird type (the string you query). `notice` is a boolean: whether *this* type was also raised as a notice. This is **not** a `notice.log` lesson. |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` |
| **Connection UID** | `uid` — the same join as `conn`, `http`, and `files`. Empty → write “no uid” and use IP, port, and time if they are logged. |

Do not memorize the Zeek catalog. Describe the `name` you have. Do not invent a story from the word “weird.” Many types fire on noisy, broken, or mid-stream traffic.

This lesson only reads the **weird** log. It is not a PCAP analysis lesson. Detection rule syntax is **1.3**.

**What good looks like:**

- Describe: one sentence — Zeek flagged this `name` between these IPs/ports. Then say which `uid` you would open on `conn`. Do not call it malware.
- Given: `name` `data_before_established`, `id.resp_h` `203.0.113.88`, `id.resp_p` `8080`, `uid` present. **What occurred:** Zeek saw data before the TCP handshake finished to `203.0.113.88:8080`. Open `conn` on that `uid`. Do not name a process.
- Query: names a **specific** `name` (or dest), not every **weird** event.

---

## 2. Knowledge Check

1. A single **weird** event is an incident. True or false?
2. `name` `data_before_established`, dest `203.0.113.88:8080`, `uid` present. In one sentence, what occurred?
3. A SIEM query that matches every **weird** event is a good “specific weird activity” query. True or false?

---

## 3. Summary

A **weird** event is a type, two endpoints, and a UID. It is a lead. The process is not on this log. A query names a specific type.

**Next:** **1.3.1** SIGMA rules.

---

## 4. Related modules

- 1.2.7 – Files engine (previous)
- 1.2.2 – Conn engine
- 1.1.4 – Host-observed network
- 1.3.1 – SIGMA rules


---

# Lesson 1.3.1 – SIGMA Rules

Source: `modules/01-soc/03-detection/01-sigma-rules/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.1.1 A / B / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 1a / 2b / 3c  
- Hunter: 1.3.1.1 B / C / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 2b / 3c / 4c  
- CTI: 1.3.1.1 A / B / B ; 1.3.1.2 1a / 2b / 3c ; 1.3.1.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a SIGMA rule: purpose, structure, field tests (selectors), and how it becomes a SIEM query.
2. Describe what an existing rule detects, and say what a **basic** create or modify looks like.

**Mapped Proficiency Items:**
- K: 1.3.1.1 – SIGMA rules
- T: 1.3.1.2 – Analyze an existing SIGMA rule and describe what it detects
- T: 1.3.1.3 – Create or modify a basic SIGMA rule

---

## 1. Key Concepts

An alert comes from a **detection**. Someone wrote what to look for. SOC analysts **read** that write-up and **propose** a basic create or modify so detection engineering can review it. The shop may not all use the same SIEM, so **SIGMA** lets you write the idea once in YAML. A person or a converter turns it into that SIEM's query. You do **not** deploy the rule. How detections run as a service is **4.x**.

This lesson is SIGMA. It is not Suricata, YARA, or a saved SIEM rule (**1.3.2**–**1.3.4**).

**SIGMA** is a generic detection format. You write what to look for once. A converter or a person turns it into a SIEM query.

| Idea | What to read |
|------|----------------|
| **Purpose / structure** | `title`, `logsource` (which telemetry), `detection` (named selections plus a `condition`). Without those, it is not a detection. |
| **Fields / selectors** | Field tests: `endswith`, `contains`, a list, `re`. Field names must match the logsource. `Image` / `CommandLine` on `process_creation` are process-create fields (**1.1.2**). Tests in one selection are typically **and**. A list under one field is typically **or**. |
| **To SIEM** | `logsource` → table or event type. Selections → `where`. `condition` → and / or / not. Write that in words or a SIEM-shaped sentence. Running a converter is not this lesson. |

**What good looks like:**

- Analyze: name logsource, selectors, condition, and what would fire. Do not invent a Zeek field on a Windows process rule.
- Given:

```yaml
title: Encoded PowerShell from Script Host
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\powershell.exe'
    CommandLine|contains: '-enc'
    ParentImage|endswith: '\wscript.exe'
  condition: selection
```

**What it detects:** process create — PowerShell with `-enc` and parent `wscript`. Same story as **1.1.2**. SIEM shape: `DeviceProcessEvents` / Sysmon 1, those three predicates.

- Modify / create: a **basic** rule with title, logsource, one selection, and a condition. Tightening “any `powershell.exe`” by adding parent or `-enc` is a modify. SOC **proposes**. Detection engineering reviews.

---

## 2. Knowledge Check

1. SIGMA is a SIEM product. True or false?
2. A `process_creation` rule matches `powershell.exe`, CommandLine `-enc`, and parent `wscript`. In one sentence, what does it detect?
3. Why is a rule that matches every `powershell.exe` a poor proposal?

---

## 3. Summary

SIGMA is portable YAML: logsource, selectors, condition. It becomes a SIEM query. You read it and propose a basic one. You do not deploy it.

**Next:** **1.3.2** Suricata rules.

---

## 4. Related modules

- 1.2.8 – Weird engine (previous)
- 1.1.2 – Process activity
- 1.3.2 – Suricata rules
- 1.3.4 – SIEM rules
- 4.x – How detections run as a service


---

# Lesson 1.3.2 – Suricata Rules

Source: `modules/01-soc/03-detection/02-suricata-rules/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.2.1 A / B / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 1a / 2b / 3c  
- Hunter: 1.3.2.1 B / C / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 2b / 3c / 4c  
- CTI: 1.3.2.1 A / B / B ; 1.3.2.2 1a / 2b / 3c ; 1.3.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name action, header, and options on a Suricata rule, and say how a hit relates to a Zeek log of the same session.
2. Read an existing rule and say what it detects; propose a **basic** create or modify.

**Mapped Proficiency Items:**
- K: 1.3.2.1 – Suricata rules
- T: 1.3.2.2 – Analyze an existing Suricata rule and describe what it detects
- T: 1.3.2.3 – Create or modify a basic Suricata rule

---

## 1. Key Concepts

SOC analysts read a **network signature** to see what on the wire would fire. That is daily alert work: an alert names a Suricata rule, and you have to say what it matches — protocol, direction, and the string or buffer it looks for — and whether that match is specific. **1.3.1** was portable YAML for host logs (SIGMA). This lesson is **Suricata**: packets and streams. You do **not** deploy it. How detections run as a service is **4.x**. It is **not** YARA (**1.3.3**).

**Suricata** inspects packets and streams and can **alert** when a signature matches. This lesson uses `alert` only — not drop or reject.

```
alert proto src_ip src_port -> dst_ip dst_port ( options )
```

| Idea | What to read |
|------|----------------|
| **Action, header, options** | Action = `alert`. Header = protocol, addresses, ports, and `->`. Options = `msg`, `sid`, `rev`, and the match keywords |
| **Common options** | `content:"..."`. HTTP buffers: `http.uri`, `http.method`, `http.user_agent`. TLS: `tls.sni` (the name the client asked for). `flow:established,to_server` means an established connection, client to server |
| **ASCII / hex / regex** | ASCII = `content:"/update.exe"`. Hex = `content:"\|4d 5a\|"` (the two bytes `MZ` that start a Windows executable). Regex = `pcre:"/update\\.(exe\|dll)/i"`. Regex is easy to over-match. Do not paste exploit payloads |
| **Vs Zeek** | Zeek writes parsed fields for the session (method, URI, who talked). Suricata writes that this signature matched. The same session can produce both. Join them with time plus the **5-tuple** (source IP, source port, destination IP, destination port, protocol). Do not put Zeek field names (`uri`, `id.orig_h`, `uid`) in the Suricata rule |

`$HOME_NET` means our network. `$EXTERNAL_NET` means not our network. Both are **site variables**. Do not invent the address range.

**What good looks like:**

- Analyze: name action, header, options, and what would fire. A raw `content:"GET"` on `tcp any any` is too broad — those three bytes match anywhere in any TCP session.
- Given:

```
alert http $HOME_NET any -> $EXTERNAL_NET any (
  msg:"GET /update.exe";
  flow:established,to_server;
  http.method; content:"GET";
  http.uri; content:"/update.exe";
  sid:1000001; rev:1;)
```

**What it detects:** outbound HTTP GET whose URI contains `/update.exe`. A matching session should also have a Zeek `http` log of that GET.

- Modify / create: a **basic** `alert` with a header, `msg`, `sid`, `rev`, and one specific `content` in the right buffer. Tightening “any GET” by adding `http.uri` is a modify. SOC **proposes**. Detection Engineering reviews.

---

## 2. Knowledge Check

1. Suricata and Zeek do the same job on a session. True or false?
2. The given rule above — what does it detect, in one sentence?
3. Why is `content:"GET"` on `tcp any any` a poor proposal?

---

## 3. Summary

A Suricata rule is action, header, and options. Put the match in the right buffer. ASCII, hex, and regex are techniques. Zeek tells you the session; Suricata tells you the signature matched. You propose. You do not deploy.

**Next:** **1.3.3** YARA rules.

---

## 4. Related modules

- 1.3.1 – SIGMA rules (previous)
- 1.2.5 – HTTP engine
- 1.3.3 – YARA rules
- 4.x – How detections run as a service


---

# Lesson 1.3.3 – YARA Rules

Source: `modules/01-soc/03-detection/03-yara-rules/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.3.1 A / B / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 1a / 2b / 3c  
- Hunter: 1.3.3.1 B / C / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 2b / 3c / 4c  
- CTI: 1.3.3.1 A / B / B ; 1.3.3.2 1a / 2b / 3c ; 1.3.3.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what a YARA rule is for, name its blocks, and when it runs on a file vs memory.
2. Read an existing rule and say what it detects; propose a **basic** create or modify.

**Mapped Proficiency Items:**
- K: 1.3.3.1 – YARA rules
- T: 1.3.3.2 – Analyze an existing YARA rule and describe what it detects
- T: 1.3.3.3 – Create or modify a basic YARA rule

---

## 1. Key Concepts

SOC analysts match **byte patterns** on a file they already have, or on memory the shop already scans. A log can name a file, a hash, or a URI. It does not show the bytes inside. That is the job in this lesson: read a **YARA** rule so you can say what would hit those bytes, and propose a basic create or modify. **1.3.2** was Suricata on the wire. This lesson is the file (or memory). You do **not** deploy the rule. You do **not** dump memory. How detections run as a service is **4.x**.

**YARA** matches **byte patterns** in a file or in process memory. It is not SIGMA and not Suricata. It is not a SIEM query language.

```
rule RuleName
{
    meta:
        description = "..."
    strings:
        $a = "..."
    condition:
        $a
}
```

| Idea | What to read |
|------|----------------|
| **Purpose / structure** | `rule` name, `meta` (notes, not the match), `strings`, `condition`. A strings block with no real condition is not a useful proposal. |
| **Strings and condition** | Named patterns plus boolean (`and`, `or`, `filesize`, `uint16(0) == 0x5A4D`, `#s >= 2`). `$mz at 0` is the same *idea* as that `uint16` check: MZ at the start of the file. |
| **ASCII / hex / regex** | ASCII = `"update.exe" ascii nocase`. Hex = `{ 4D 5A }` (`MZ`) — not Suricata `content:"\|4d 5a\|"`. Regex = `/update\.(exe\|dll)/ nocase`. Regex is easy to over-match. |
| **Files vs memory** | **File** — disk or a saved extract. `at 0` and `filesize` can apply. **Memory** — a process the shop already scans. Drop `filesize` (it does not apply there, so the rule will not match). Drop `at 0` for a PE header; the image may not sit at the start of the region. If your shop does not scan memory, say so and stay on files. |

**What good looks like:**

- Analyze: name the strings, the condition, file vs memory, and what would fire. `{ 4D 5A } at 0` alone matches every PE, including Notepad.
- Given:

```
rule Train_UpdateExe
{
    meta:
        description = "PE that contains update.exe"
    strings:
        $mz = { 4D 5A }
        $name = "update.exe" ascii nocase
    condition:
        $mz at 0 and $name and filesize < 5MB
}
```

**What it detects:** a **file** that starts with MZ and contains `update.exe`, under 5 MB. That can fit a PE extract of `update.exe` (**1.2.7**) **if you scan those bytes**. It does not match a `files` log line. It is not a conviction.

- Modify / create: a **basic** file rule with one distinctive string **and** a header or size check. Tightening “MZ only” by adding `update.exe` is a modify. SOC **proposes**. DE reviews.

---

## 2. Knowledge Check

1. YARA is a SIEM query language. True or false?
2. The given rule above — what does it detect, in one sentence?
3. Why is `{ 4D 5A } at 0` alone a poor proposal?

---

## 3. Summary

YARA is meta + strings + condition. ASCII, hex, and regex. File rules may use `at 0` and `filesize`. Memory often must not. You propose. You do not deploy.

**Next:** **1.3.4** SIEM rules.

---

## 4. Related modules

- 1.3.2 – Suricata rules (previous)
- 1.2.7 – Files engine
- 1.3.4 – SIEM rules
- 4.x – How detections run as a service


---

# Lesson 1.3.4 – SIEM Rules

Source: `modules/01-soc/03-detection/04-siem-rules/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.4.1 A / B / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 1a / 2b / 3c  
- Hunter: 1.3.4.1 B / C / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 2b / 3c / 4c  
- CTI: 1.3.4.1 A / B / B ; 1.3.4.2 1a / 2b / 3c ; 1.3.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the pieces of a SIEM detection, and how log fields (or a SIGMA rule) become one.
2. Read an existing SIEM rule and say what it detects; propose a **basic** create from fields or from SIGMA.

**Mapped Proficiency Items:**
- K: 1.3.4.1 – SIEM rules
- T: 1.3.4.2 – Analyze an existing SIEM rule and describe what it detects
- T: 1.3.4.3 – Create a basic SIEM detection rule from log fields or a SIGMA rule

---

## 1. Key Concepts

SOC analysts **read** a saved detection and **propose** a basic one. That is daily work: an alert names a rule, and you have to say what that rule looks at — which table, which fields, which match — before you treat the alert as a fact. This lesson is that saved rule. It is **not** opening the alert (**1.4**). It is **not** how detections run as a service (**4.x**). You **propose**. You do **not** deploy.

A **SIEM rule** is named logic that runs on ingested logs and can fire an alert. Shops also call this an **analytics rule** or a **correlation search**. Here those names mean the saved detection, not a requirement to join events.

| Idea | What to read |
|------|----------------|
| **Structure** | **Name**, **table** (which log store), **logic** (the filter), **window** (how far back / how often), **output** fields. A table with no filter is not a detection. A join or count across events in a window is extra. A basic rule can be a filter on one table. |
| **Fields → detection** | Name the table. Pick fields that exist on that table (`FileName`, `ProcessCommandLine` on process events). Add a parent, token, or destination so it is not “all PowerShell.” |
| **Wildcards / regex** | **Wildcard** or substring when a path or fixed token is enough (`*\\Temp\\*`, `-enc`). **Regex** when the token itself varies (`-e` / `-enc` / `-EncodedCommand`). Do not regex an empty field into existence. |

**From SIGMA (second create path):** SIGMA is a portable detection: you write what to look for once. Turn it into a SIEM rule by mapping **logsource** (which telemetry) → table, **selectors** (field tests) → logic, **condition** (and / or / not) → how those tests combine. Then name it, give it a window, and list output fields. You are not required to run a converter.

**What good looks like:**

- Analyze: name table, logic, window, and what would fire.
- Given:

```
Name: Encoded PowerShell from script host
Source: DeviceProcessEvents
Window: 5 minutes
Logic:
  FileName =~ "powershell.exe"
  and ProcessCommandLine has "-enc"
  and InitiatingProcessFileName == "wscript.exe"
Output: Timestamp, DeviceName, ProcessCommandLine, InitiatingProcessCommandLine
```

**What it detects:** a process create of PowerShell with `-enc` in the command line, parent `wscript`.

If you started from SIGMA, the same three tests were `Image` / `CommandLine` / `ParentImage` on `process_creation`. The SIEM wrap is the name, table, window, and outputs.

- Create: a **basic** proposed rule from those fields **or** from that SIGMA mapping. An unfiltered `DeviceProcessEvents` is not a create. SOC **proposes**. Detection engineering reviews.

---

## 2. Knowledge Check

1. A SIEM table with no filter is a detection. True or false?
2. The given rule above — what does it detect, in one sentence?
3. When do you use a wildcard instead of a regex?

---

## 3. Summary

A SIEM rule is named logic on a table, in a window, with outputs. Build it from fields you know, or translate SIGMA. You propose. You do not deploy.

**Next:** **1.4.1** Alert context and investigation.

---

## 4. Related modules

- 1.3.1 – SIGMA rules
- 1.3.3 – YARA rules
- 1.1.2 – Process activity
- 1.4.1 – Alert context and investigation
- 4.x – How detections run as a service


---

# Lesson 1.4.1 – Alert Context and Investigation

Source: `modules/01-soc/04-alerts/01-context-investigation/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.1.1 A / B / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- Hunter: 1.4.1.1 B / C / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- CTI: 1.4.1.1 A / A / B ; 1.4.1.2 1a / 1a / 2b ; 1.4.1.3 1a / 1a / 2b ; 1.4.1.4 1a / 1a / 2b ; 1.4.1.5 1a / 1a / 1a ; 1.4.1.6 1a / 1a / 1a  
**Estimated Time:** 30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Review an alert: name the context that is present and missing (including a VirusTotal lookup of a hash, IP, or domain you have), say what the configuration would fire, and name each hop upstream.
2. Say what related endpoint logs and PCAP **add** — or fail to add — versus the alert fields.

**Mapped Proficiency Items:**
- K: 1.4.1.1 – Alert context and investigation
- T: 1.4.1.2 – Review an alert and identify which context is present and which is missing (include VirusTotal on a hash, IP, or domain you have)
- T: 1.4.1.3 – Review the alert configuration and explain what would fire
- T: 1.4.1.4 – Trace an alert to its upstream detection logic and name each hop
- T: 1.4.1.5 – Collect related endpoint logs and state what they add (or fail to add)
- T: 1.4.1.6 – Collect related PCAP and state what it adds versus the alert fields

---

## 1. Key Concepts

SOC analysts work the **alert that fired** — the object in the queue — before they label it true or false. A detection created that alert. Before you classify it, you have to say what it already shows, what it does not, what the rule would fire on, how it reached the queue, and what related host logs or a packet capture add. That is the job in this lesson: gather that context so you do not treat a gap as benign or invent a hop that is not there.

**1.3** taught how to read and propose a detection. This lesson you do **not** write a new rule. You do **not** classify TP/FP (**1.4.2**).

The first alert in this course is the **process create**: `wscript` → encoded PowerShell as `jlee`. That is what the **1.3.4** SIEM rule keys on.

| Idea | What to do |
|------|------------|
| **Context** | Two lists: **present** and **missing**. Typical present fields are host, user, time, rule name, and the field the rule keys on. If you have a **hash**, **IP**, or **domain**, look it up on **VirusTotal** (**0.7**). Write what VT adds or fails to add (reputation, or “not in VT”). That is gathering context, not opening Relations or a pivot graph (**2.9**). Missing is a **gap**, not “benign.” Do not invent a command line or a VT hit. |
| **Configuration** | Read the detection behind the alert. One sentence: **what would fire**. Use the same field language as **1.3**. |
| **Upstream hops** | Name each hop from detection logic to the alert. Classroom pattern: Suricata rule → SIEM correlation search → SIEM alert. Some alerts are SIEM-only. Do not invent a Suricata hop. |
| **Endpoint logs** | Pull related **1.1** host events for that host and time window. State what they **add** or **fail to add**. Opening the table is not the task. A file event for Temp `invoice.vbs` can add the dropper path. The Run key is **not** required on this first pass (hunt is **3.x**). |
| **PCAP** | For a **network** alert: state what the capture adds versus the alert fields (URI, SNI, payload). Why you pull PCAP is **1.2.1**. Where sensors sit is **0.8**. If the alert is process-only and no capture exists, write **PCAP not applicable**. Do not invent a download path. |

**What good looks like:**

- **Context:** Present = host, user, rule, `powershell -enc`, parent `wscript`. Missing until you pull more = dest IP, URI, file hash. After a file event adds Temp `invoice.vbs` (or you have `203.0.113.88`), look that hash or IP up on **VirusTotal**. Write the one-line result. Do not open Relations.
- **Config:** “PowerShell with `-enc` and parent `wscript` fires.”
- **Hops:** SIEM rule → SIEM alert (no Suricata unless the given includes a Suricata rule).
- **Endpoint logs:** A Sysmon 11 / `DeviceFileEvents` file event **adds** Temp `invoice.vbs`. If the tenant has no process parent, the logs **fail to add** it — say so.
- **PCAP:** On a `:8080` GET, PCAP can **add** the URI `/update.exe` if the alert only had IP:port. On this process alert, PCAP is **not applicable** until you have a flow.

---

## 2. Knowledge Check

1. The alert context is missing a parent process. That means the activity was benign. True or false?
2. Name the hops for a SIEM-only process alert.
3. You have the hash of Temp `invoice.vbs` and IP `203.0.113.88`. What do you look up on VirusTotal, and what is **not** this lesson?

---

## 3. Summary

Present versus missing. A hash, IP, or domain you have goes to **VirusTotal**. Say what the configuration would fire. Name each hop. Endpoint logs and PCAP must **add** something — or you say they failed to. You do not classify, and you do not write the rule.

**Next:** **1.4.2** Alert classification.

---

## 4. Related modules

- 1.3.4 – SIEM rules (previous)
- 1.4.2 – Alert classification
- 1.1.2 – Process activity
- 1.1.3 – File system activity
- 1.2.1 – Zeek concepts (why pull PCAP)
- 0.7 – External tools (VirusTotal)
- 0.8 – Environment / signal flow


---

# Lesson 1.4.2 – Alert Classification

Source: `modules/01-soc/04-alerts/02-classification/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.2.1 A / B / C ; 1.4.2.2 2b / 3c / 4c  
- Hunter: 1.4.2.1 B / C / C ; 1.4.2.2 2b / 3c / 4c  
- CTI: 1.4.2.1 A / A / B ; 1.4.2.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Define **True Positive (TP)**, **False Positive (FP)**, **True Negative (TN)**, and **False Negative (FN)**.
2. Classify a given case and **cite the evidence**, including at least one miss as FN.

**Mapped Proficiency Items:**
- K: 1.4.2.1 – Alert classification (TP/FP/TN/FN)
- T: 1.4.2.2 – Classify given cases as TP, FP, TN, or FN and cite the evidence

---

## 1. Key Concepts

After you have looked at a case, you still have to **classify** it. A classification says whether the detection was right — a real hit, a noisy fire, ordinary activity that correctly stayed quiet, or a miss. You also **cite the evidence**: a short pointer to the field or log that proves the label. That is the job in this lesson. Without a label, the next person cannot tell a real hit from a miss. Without a cite, “malicious” is a slogan.

**1.4.1** gathered context on a fired alert. This lesson is the four labels. It is **not** why a false positive fired (**1.4.3**). It is **not** scan / root / user (**1.4.4**).

Fired alerts sit in an **alert queue** — the list waiting for an analyst. True negatives and false negatives usually are **not** in that list, because nothing fired.

| Label | Detection said | Reality |
|-------|----------------|---------|
| **True Positive (TP)** | Bad | Bad — a fired alert, and the activity is what the rule is for |
| **False Positive (FP)** | Bad | Benign — a fired alert, authorized or expected activity |
| **True Negative (TN)** | Not bad | Benign — **no alert**, ordinary activity |
| **False Negative (FN)** | Not bad | Bad — **no alert**, activity that should have been detected |

A **false negative is not a fired alert you dislike.** It is a **miss**. You find it in related logs, in a hunt, or after an incident — not as a fired alert in the queue.

**Evidence** is a short cite: parent plus `-enc`, destination plus URI, “no alert on that GET.” A slogan (“malicious”) is not evidence.

**What good looks like:** someone gives you a case. You name TP, FP, TN, or FN. You point at the field or log that proves it.

- **TP:** Alert `Encoded PowerShell from script host`. Cite: `wscript` plus `-enc` is the activity the rule is for, and it happened (**1.4.1**).
- **FP:** Alert on any PowerShell; logs show interactive `Get-Help`. Cite: PowerShell ran; it is ordinary help, not encoded script-host. *Why* the rule is broad is **1.4.3**.
- **TN:** No alert on ordinary browser activity. Cite: expected browse, no matching bad pattern. Do not invent an alert so you can classify it.
- **FN:** HTTP shows `GET /update.exe` to `203.0.113.88:8080`, **no** alert in the queue. Cite: the download occurred; nothing fired. That is a miss.

Do not pick a category yet (**1.4.4**). Do not explain why the false-positive rule is noisy (**1.4.3**).

---

## 2. Knowledge Check

1. FN is a bad alert sitting in the queue. True or false?
2. Alert `Encoded PowerShell from script host`, `wscript` + `-enc` confirmed. Classify and cite.
3. `GET /update.exe` to `203.0.113.88:8080`, no alert. Classify and cite.

---

## 3. Summary

Four labels. A true negative and a false negative usually have **no** alert in the queue. Classify the case and cite the evidence. Why a false positive fired is next.

**Next:** **1.4.3** Common false positive causes.

---

## 4. Related modules

- 1.4.1 – Alert context and investigation (previous)
- 1.4.3 – Common false positive causes
- 1.1.2 – Process activity
- 1.2.5 – HTTP engine


---

# Lesson 1.4.3 – Common False Positive Causes

Source: `modules/01-soc/04-alerts/03-false-positive-causes/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.3.1 A / B / C ; 1.4.3.2 2b / 3c / 4c  
- Hunter: 1.4.3.1 B / C / C ; 1.4.3.2 2b / 3c / 4c  
- CTI: 1.4.3.1 A / A / B ; 1.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two cause classes: analyst or tool activity, and untuned or overly broad detection logic.
2. Given a false positive, pick the class and say **what you would change**.

**Mapped Proficiency Items:**
- K: 1.4.3.1 – Common false positive causes
- T: 1.4.3.2 – Given a false positive, identify the cause class and what you would change

---

## 1. Key Concepts

SOC analysts still have work after they call an alert a **false positive**. That fire already used queue time, and the same benign activity will fire again unless someone says why it matched and what would stop it. That is the job in this lesson: pick a **cause class** and name **one change**. You do not decide true positive versus false positive again. You do not deploy the change.

A false positive is a fired alert on authorized or expected activity. Classification (**1.4.2**) already put that label on the case. This lesson is the **cause** of that fire, not the label. Categories such as scan, root, or user are **1.4.4**.

| Cause class | What it looks like | Change you can name |
|-------------|--------------------|---------------------|
| **Analyst or tool activity** | A security analyst downloaded or tested a rule that is already live; packet replay into production; a scanner the shop owns | Exclude the lab, replay, or scanner identity; test in a lab window. Do not delete a good signature |
| **Untuned or overly broad detection logic** | Any PowerShell; `content:"GET"` on any TCP; MZ-only YARA wired to an alert | Add a second selector (parent and `-enc`); bind an HTTP buffer; raise a threshold |

Those two classes are the ones this lesson teaches. If neither fits, say **other — not analyst/tool or overly broad** and still name a change. Do not invent a third official class.

A change is one concrete sentence: “Require parent `wscript` and `-enc`.” “Tune it” is not a change. You name the change. Detection engineering deploys it (**1.3** / **4.x**).

**What good looks like:**

- **Overly broad:** False positive on any-PowerShell / `Get-Help` (**1.4.2**). Class: untuned or overly broad detection logic. Change: require `-enc` and a script-host parent. Hand it to detection engineering.
- **Analyst or tool:** False positive because an analyst replayed yesterday’s `GET /update.exe` packet capture into production. Class: analyst or tool activity. Change: exclude the replay window or interface. Do not delete the `/update.exe` signature.

---

## 2. Knowledge Check

1. This lesson is for deciding true positive versus false positive. True or false?
2. What are the two cause classes?
3. False positive: any-PowerShell on `Get-Help`. Name the class and one change sentence.

---

## 3. Summary

After a false positive: **class + change**. Analyst or tool activity versus untuned or overly broad logic. Name the change. You do not deploy it.

**Next:** **1.4.4** Common alert categorizations.

---

## 4. Related modules

- 1.4.2 – Alert classification (previous)
- 1.4.4 – Common alert categorizations
- 1.3.1 – SIGMA rules
- 4.x – How detections run as a service


---

# Lesson 1.4.4 – Common Alert Categorizations

Source: `modules/01-soc/04-alerts/04-categorizations/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.4.1 A / B / C ; 1.4.4.2 2b / 3c / 4c  
- Hunter: 1.4.4.1 B / C / C ; 1.4.4.2 2b / 3c / 4c  
- CTI: 1.4.4.1 A / A / A ; 1.4.4.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the syllabus categories: scanning / reconnaissance, root-level access, user-level access, unsuccessful activity, and **other** as your shop uses it.
2. Assign a category and **justify why it is not the adjacent category**.

**Mapped Proficiency Items:**
- K: 1.4.4.1 – Common alert categorizations
- T: 1.4.4.2 – Assign a category to an alert and justify why it is not the adjacent category

---

## 1. Key Concepts

SOC analysts put a **category** on an alert so the next desk can see what kind of activity it was. A true-positive or false-positive label only says whether the detection was right. A category says whether this was a scan, a failed attempt, or access as a user versus as an administrator. You pick one name and say why the **adjacent category** — the neighbor people mix it up with — is wrong. You do **not** re-argue true positive versus false positive (**1.4.2**). You do **not** name a false-positive cause (**1.4.3**). You do **not** write an ATT&CK technique ID as the category (**0.6**).

| Category | Use when | Adjacent — not this |
|----------|----------|---------------------|
| **Scanning / reconnaissance** | Wide, unauthenticated probing (many ports or hosts; no login or exploit attempt) | **Unsuccessful** — a failed login is an access *attempt*, not a sweep |
| **Root-level access** | SYSTEM, admin, or service-level control on the host | **User-level** — the same command as a standard user is not root |
| **User-level access** | Activity as a normal user account (Windows Medium integrity — `jlee`) | **Root-level** — encoded or “looks like malware” does not upgrade the account |
| **Unsuccessful activity** | An access or exploit *attempt* that failed (denied logon; HTTP 401 burst on one app) | **Scanning** — failed authorization is not a port sweep |
| **Other (your shop)** | A name your site already uses | Say the local name and which neighbor you rejected. Do not invent ATT&CK tactics as categories |

The adjacent pairs are **scan ↔ unsuccessful** and **user ↔ root**. The task is two sentences: **category**, then **not the neighbor because …**.

**What good looks like:**

- **User-level, not root:** Alert `Encoded PowerShell from script host`, `wscript` + `-enc` as Medium `jlee` (**1.4.1**). Category **user-level**. Not root: the account is a standard user. Encoded does not change the category. (The same command as **SYSTEM** after a service start would be **root**, not user.)
- **Scanning, not unsuccessful:** Given: many unanswered SYN to 150 ports in two minutes, no login. Category **scanning / reconnaissance**. Not unsuccessful: nothing was presented as credentials or an exploit — it is a sweep.

Do not invent a DYA category list here. If you need **other**, use a name your real shop already has.

---

## 2. Knowledge Check

1. A category is the same thing as a true-positive or false-positive label. True or false?
2. Name the four syllabus categories plus **other**.
3. Alert: `wscript` + `-enc` as Medium `jlee`. Category, and why not the adjacent one?

---

## 3. Summary

A category names the kind of activity and rejects the neighbor. A scan is not failed authorization. A user account is not root. Other is a name your shop already uses.

**Next:** **1.4.5** Service Level Agreements / Response Time Goals.

---

## 4. Related modules

- 1.4.3 – Common false positive causes (previous)
- 1.4.5 – SLA / response time goals
- 1.4.2 – Alert classification
- 0.6 – Frameworks (ATT&CK is not a category)


---

# Lesson 1.4.5 – SLA / Response Time Goals

Source: `modules/01-soc/04-alerts/05-sla-response-times/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.5.1 A / B / C ; 1.4.5.2 2b / 3c / 4c ; 1.4.5.3 2b / 3c / 4c  
- Hunter: 1.4.5.1 A / B / B ; 1.4.5.2 1a / 2b / 3c ; 1.4.5.3 1a / 2b / 3c  
- CTI: 1.4.5.1 A / A / A ; 1.4.5.2 1a / 1a / 1a ; 1.4.5.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two clocks: time to **begin** investigation, and time to **close or escalate**.
2. Given timestamps, say **which clock is at risk**.
3. Close or escalate and **record it against the correct clock**.

**Mapped Proficiency Items:**
- K: 1.4.5.1 – Service Level Agreements / Response Time Goals
- T: 1.4.5.2 – Given timestamps, identify whether the start clock or the close/escalate clock is at risk
- T: 1.4.5.3 – Close or escalate an alert and record it against the correct clock

---

## 1. Key Concepts

SOC analysts keep an alert from sitting untouched, and from sitting open with no close or escalate. That is the job in this lesson: name **which** response-time goal is at risk, then record closed or escalated against it. “Work faster” is not the task.

A **service-level agreement (SLA)** here is a **response-time goal**: the maximum time allowed for a step. This lesson uses two **clocks** — the short word for those goals.

| Clock | What it measures | Classroom goal |
|-------|------------------|----------------|
| **Start** | Alert **created** → first touch (`started`) | **15 minutes** |
| **Close / escalate** | First touch → `closed` or `escalated` | **45 minutes** |

The 15-minute and 45-minute figures are **this lesson only**. They are not a live shop policy. If your real shop uses different minutes, use those. The obligation is **two clocks**, not 15 and 45.

If nobody has touched the alert, only the **start** clock exists. Close/escalate has no origin until a first touch. After a first touch, start is already met (or already breached); the remaining clock is **close/escalate**.

This is **not** re-investigating the alert (**1.4.1**). It is **not** true-positive / false-positive or a category (**1.4.2**, **1.4.4**). It is **not** a report, and it is **not** the report clocks in **1.5**.

**Record** is one classroom line: **closed** or **escalated**, **which clock**, and the **time**. If you have not touched the alert yet, the first line is **started** against the **start** clock. Do not close an untouched alert to “meet SLA.” This is a classroom line, not a ticketing-product class.

**What good looks like:**

- **Start at risk:** Created `14:00`. No `started`. Now `14:18`. Clock: **start** (18 minutes, past 15). Close/escalate has no origin. Record: `started | start (breached) | 14:18`. Then investigate. Do not write `closed` yet.
- **Close/escalate at risk:** An alert first touched at `13:28` is still open at `14:20`. Clock: **close/escalate** (52 minutes since start, past 45). Start already met. Record: `escalated | close-escalate (breached) | 14:20` — or `closed` if the investigation is actually done.

---

## 2. Knowledge Check

1. If nobody has touched the alert, which clock can be at risk?
2. What are the two clocks, and when does each start?
3. An alert was first touched at `13:28` and is still open at `14:20`. Which clock is at risk, and what do you record?

---

## 3. Summary

Two clocks: **start** from created; **close/escalate** from first touch. Name the clock. Record closed or escalated against it.

**Next:** **1.5.1** Report types. This closes unit **1.4**.

---

## 4. Related modules

- 1.4.4 – Common alert categorizations (previous)
- 1.5.1 – Report types
- 1.4.1 – Alert context and investigation
- 1.5.2 – Reporting timeline requirements (not these alert clocks)


---

# Lesson 1.5.1 – Report Types

Source: `modules/01-soc/05-reporting/01-report-types/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C ; 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C ; 1.5.1.2 2b / 3c / 4c  
- CTI: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the three kinds of report: **incident report**, **RFI**, and **other** as your shop uses it.
2. Given a situation, pick the type and say why it is not the **adjacent** type.

**Mapped Proficiency Items:**
- K: 1.5.1.1 – Report types
- T: 1.5.1.2 – Identify the correct report type for a given situation and why it is not the adjacent type

---

## 1. Key Concepts

After you decide an alert is a case, or that you need another desk's help, you pick the **kind of record**. The next desk needs a **case** or a **question**, not both mixed in one product. That is the job in this lesson: name the type first, and say why the next-closest wrong type is wrong. That next-closest wrong type is the **adjacent** type (the **neighbor**).

| Type | What it is | Next-closest wrong type |
|------|------------|-------------------------|
| **Incident report** | Records a security incident (or a strongly supported suspected one) that needs a case / IR handoff | **RFI** — you already have enough to record the case; asking a question is a different product |
| **RFI** (Request for Information) | Asks another desk (CTI, hunt, IT, a vendor) for information so you can continue | **Incident** — an RFI can sit **beside** a case; it is the question, not a second case record |
| **Other (your shop)** | A name your site already uses | Say the local name and which neighbor you rejected. Do not invent a type. Do not park a finished intel paper here (**2.11**) |

The pair that gets mixed up is **incident ↔ RFI**. An RFI can sit beside an incident. It is not a second case. The RFI is the door into CTI.

**What good looks like:** two sentences — the **type**, and **not the neighbor because …**. You do not write the body yet.

- **Incident, not RFI:** First record for **A12** — `WS-JLEE` / `jlee`, `wscript` → `-enc`, Temp `invoice.vbs`. Type **incident report**. Not RFI: you are recording the case for IR, not asking a question. (A later RFI on the domain is a second product.)
- **RFI, not incident:** **A12** already exists. You want CTI to work the update domain / file. Type **RFI**. Not incident: the case is already open; this product is the question.

Do not invent a type list for this course's company. If you need **other**, use a name your real shop already has.

This lesson only names the type. Due clocks are **1.5.2**. Recipients and channel are **1.5.3**.

---

## 2. Knowledge Check

1. An RFI is a second incident case. True or false?
2. What is an incident report for, versus an RFI?
3. **A12** already exists. You want CTI to work the update domain. Type, and why not the adjacent one?

---

## 3. Summary

An incident report records the case. An RFI asks a question — and is the door into CTI. Other is a name your shop already uses. Name the type and reject the neighbor.

**Next:** **1.5.2** Reporting timeline requirements.

---

## 4. Related modules

- 1.4.5 – SLA / response time goals (previous — alert clocks, not report clocks)
- 1.5.2 – Reporting timeline requirements
- 1.5.3 – Notification and distribution
- 2.11 – Intelligence production (not a 1.5 type)


---

# Lesson 1.5.2 – Reporting Timeline Requirements

Source: `modules/01-soc/05-reporting/02-reporting-timelines/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C ; 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 A / B / B ; 1.5.2.2 2b / 3c / 4c  
- CTI: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two kinds of report clock: **submit** (by type) and **escalate-for-more-info**.
2. Given timestamps, say **which clock applies** and whether it is **at risk**.

**Mapped Proficiency Items:**
- K: 1.5.2.1 – Reporting timeline requirements
- T: 1.5.2.2 – Given timestamps, identify which report timeline applies and whether it is at risk

---

## 1. Key Concepts

SOC analysts watch **report** clocks so a case record and a CTI question leave the desk on time, and so a blocker is escalated instead of sitting. **1.5.1** already named the type — **incident report** (the case record) or **RFI** (the question to another desk). This lesson is **which clock** applies to that type, and whether it is **at risk**. It is **not** the alert 15 / 45 clocks (**1.4.5**). It is **not** who gets the report (**1.5.3**).

**Classroom numbers (this lesson only — not a live shop policy):**

| Clock | From | Classroom |
|-------|------|-----------|
| **Submit — incident** | Decision that an **incident report** is required | **30 minutes** |
| **Submit — RFI** | The **question** arises | **60 minutes** |
| **Escalate-for-more-info** | You become **blocked** (cannot finish without another desk) | **15 minutes** |

If your shop uses different minutes, use those. The obligation is **submit-by-type** plus **blocked → escalate**, not 30 / 60 / 15. If your shop has an **other** type, that type has its own submit number — do not invent one here.

**At risk** means the named clock will miss if you wait, or it is already past. “Late” with no clock name is not the task.

Two clocks can be live. When you are blocked, name **escalate-for-more-info** first. Submit is still running.

**What good looks like:**

- **Submit — RFI, at risk:** **A12** exists. Question to CTI on the update domain at `13:30`. Still unsent. Now `14:40`. Clock: **submit — RFI** (70 minutes, past 60). Not the 30-minute incident clock. Not the alert-close clock.
- **Escalate-for-more-info, at risk:** **A12** incident decision `14:00`. At `14:10` you cannot finish without another desk. Still blocked. Now `14:28`. Clock: **escalate-for-more-info** (18 minutes, past 15). Submit-incident is still running (28 of 30) — act on the blocker.

---

## 2. Knowledge Check

1. This lesson uses the same 15 / 45 clocks as **1.4.5**. True or false?
2. When does the **escalate-for-more-info** clock start?
3. RFI question at `13:30`, still unsent at `14:40`. Which clock, and is it at risk?

---

## 3. Summary

Submit by type. When blocked, escalate. Name the clock. These are not the alert SLA clocks.

**Next:** **1.5.3** Notification and distribution.

---

## 4. Related modules

- 1.5.1 – Report types (previous)
- 1.5.3 – Notification and distribution
- 1.4.5 – SLA / response time goals (alert clocks, not these)


---

# Lesson 1.5.3 – Notification and Distribution

Source: `modules/01-soc/05-reporting/03-notification-distribution/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C ; 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 A / B / B ; 1.5.3.2 2b / 3c / 4c  
- CTI: 1.5.3.1 B / C / C ; 1.5.3.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a notification chart: **who** receives the report, whether **leadership** gets awareness, and which **channel** is approved.
2. Route a report: name recipients, whether leadership gets awareness, the approved channel, and **reject the wrong channel**.

**Mapped Proficiency Items:**
- K: 1.5.3.1 – Notification and distribution
- T: 1.5.3.2 – Route a report: name recipients, leadership awareness, and the approved channel

---

## 1. Key Concepts

SOC analysts put the case record and the CTI question on an **approved path** so IR and leadership actually see them. An incident that only lives in a private chat is not a handoff. An RFI sent as a text is not a request the CTI desk can work. **1.5.1** named the type. **1.5.2** named the clock. This lesson is **who** receives the report, whether **leadership** gets awareness, and **which channel** is approved. You do **not** pick the type again. You do **not** score the 30 / 60. You do **not** write the body. **1.7** is retired — it is not a 1.5 channel.

A **notification chart** (sometimes called a **matrix**) is a table that says which teams receive which report type, whether leadership gets awareness, and which channel is approved.

**Classroom chart (this lesson only — not a live shop matrix):**

| Type | Recipients | Leadership awareness | Approved channel |
|------|------------|----------------------|------------------|
| **Incident** | SOC queue + **IR** | **Yes** — duty SOC lead | **Ticket** (the case system) |
| **RFI** | The **named team** (CTI, hunt, or IT) | **No**, unless they asked or the chart says so | **Ticket** or **approved RFI form** |

If your shop has a real chart, use it. The obligation is **who + leadership yes/no + approved channel**, not these names. If your shop has an **other** type, it has its own row — do not invent one here.

**Leadership awareness** is a yes or no on the chart. It is not “email the CEO.” The duty SOC lead counts. The leadership product is a short awareness flag, not the file hash.

**Approved** (classroom): ticket, approved RFI form.  
**Not approved** (classroom): personal SMS, private chat, personal mail off-domain.

Right people on the **wrong path** still fails.

The route is four facts: **recipients**, **leadership yes/no**, **channel**, **rejected channel**.

**What good looks like:**

- **Incident, ticket:** First IR handoff for **A12** (`WS-JLEE` / `jlee`, `wscript` → `-enc`, Temp `invoice.vbs`). Recipients **SOC + IR**. Leadership **yes**. Channel **ticket**. Reject: personal email or chat to the IR analyst only.
- **RFI, not SMS:** **A12** exists. Ask CTI to work the update domain. Recipients **CTI**. Leadership **no**. Channel **ticket or RFI form**. Reject: texting a CTI friend. Right team, wrong path.

---

## 2. Knowledge Check

1. This lesson is when the report is due. True or false?
2. What three things does the notification chart tell you?
3. First IR handoff for **A12**. Recipients, leadership yes/no, channel, and one rejected channel?

---

## 3. Summary

The chart names who, leadership, and channel. Reject the unofficial path. This closes **1.5**. SOC reporting ends here.

**Next:** **2.1.1** Data, information, and intelligence. The RFI is the door into CTI.

---

## 4. Related modules

- 1.5.2 – Reporting timeline requirements (previous)
- 1.5.1 – Report types
- 2.1.1 – Data, information, and intelligence
- 2.11 – Intelligence production (not a 1.5 route)


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


---

# Lesson 3.1 – Purpose of Threat Hunting

Source: `modules/03-hunter/01-purpose/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.1.1 B / C / C ; 3.1.1.1 3c / 4c / 4c ; 3.1.1.2 3c / 4c / 4d  
- SOC: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
- CTI: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain why threat hunting exists in the security program: find **missed** activity, and name **detection and visibility gaps**.
2. Name examples of activity that existing controls can miss.

**Mapped Proficiency Items:**
- K: 3.1.1 – Purpose of Threat Hunting
- T: 3.1.1.1 – Explain the purpose of threat hunting in the context of the security program
- T: 3.1.1.2 – Identify examples of activity that existing controls might miss

---

## 1. Key Concepts

SOC analysts work the **alert queue** — the list of detections that already fired. CTI answers requests for more context on those cases. Some malicious or suspicious activity never appears in that list. Hunters look for that missed activity, and they name the holes that let it hide: a detection that never fired, or telemetry that was never collected. That is the job in this lesson. Hunting exists because the queue and the intel note still leave coverage unexamined.

**0.3** named the hunter in one sentence: look for more activity the alerts missed. This lesson is *why* that job exists in the program — next to SOC tickets and detections, not instead of them.

| Job | Meaning |
|-----|---------|
| **Missed activity** | Malicious or suspicious activity that happened with **no** fired alert. That is a **false negative** (**1.4.2**). |
| **Detection gap** | The logs exist, but no detection (rule or analytic) would have caught it. |
| **Visibility gap** | You cannot see it even if you look — the telemetry is not there. |

A false negative is not a fired alert you dislike. It is activity that should have been detected and was not. You find it in related logs, in a hunt, or after an incident.

The hunt **product** is a **package**: more hosts, a named gap, something detection engineering can take (**0.4**). It is **not** a rewrite of the SOC ticket. SOC still owns the incident they already labeled.

This lesson does **not** pick a hunt type (**3.2.1**). It does **not** write a hunt card (**3.2.2**). It does **not** invent a hunt ticket (**3.7**). Mapping a hunt onto ATT&CK is later (**3.5.1**).

**What good looks like:** someone asks why hunting exists. You name missed activity and gaps. Someone asks for an example. You name something existing controls did not catch, and something a hunt would look for that the first alert did not require.

Incident **A12** is the process alert already taught: `wscript` launched encoded PowerShell on **WS-JLEE**. That alert fired. It did **not** require the registry Run key.

- **Missed activity:** HTTP shows `GET /update.exe` to `203.0.113.88:8080`, and **no** alert fired. That is a false negative (**1.4.2**), not a noisy item in the queue.
- **Look for (not on the first alert):** HKCU Run value **`Updater`** pointing at `%TEMP%\update.exe`; `update.exe` or another `invoice.vbs` on **other** hosts.
- **Detection gap:** registry logs show **`Updater`**, but no detection fired on that value. The telemetry is there; the rule is not.
- **Visibility gap:** if those hosts have no registry telemetry, a hunt for **`Updater`** cannot see it. Name the hole. Do not pretend the hunt ran.

---

## 2. Knowledge Check

1. Threat hunting rewrites the SOC ticket with a better story. True or false?
2. What two jobs does hunting exist to do in the security program?
3. HTTP shows `GET /update.exe` to `203.0.113.88:8080`, and no alert fired. The first process alert did not require the HKCU Run value `Updater`. Name the missed activity, and name one thing a hunt should look for that was not on that first alert.

---

## 3. Summary

Hunting finds activity the alerts missed, and it names detection and visibility gaps. The product is a package, not a rewritten SOC ticket.

**Next:** **3.2.1** Hunt types.

---

## 4. Related modules

- 0.3 – Jobs in one sentence
- 0.4 – How work can move
- 1.4.2 – Alert classification
- 2.12.3 – Local dissemination channels (previous track)
- 3.2.1 – Hunt types


---

# Lesson 3.2.1 – Hunt Types

Source: `modules/03-hunter/02-methodology/01-hunt-types/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.1 B / C / C ; 3.2.1.1–3.2.1.4 3c / 4c / 4c  
- SOC: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
- CTI: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the four hunt types.
2. Given a seed, name the type and the look-for. That is what **execute** means in this lesson.

**Mapped Proficiency Items:**
- K: 3.2.1 – Hunt types
- T: 3.2.1.1 – Execute an intel-driven hunt
- T: 3.2.1.2 – Execute a hypothesis-driven hunt
- T: 3.2.1.3 – Execute a reactive hunt
- T: 3.2.1.4 – Execute an anomaly-based hunt

---

## 1. Key Concepts

Hunters pick a **type** so the search has a reason. After **A12**, you might search because CTI named a domain, because you expect a persistence key, because the incident already happened, or because a download never alerted. Those are four different starts. Mix them and you look for the wrong thing. That is the job in this lesson: name the type, the seed, and what you look for.

**3.1** said why hunting exists: missed activity and gaps. This lesson is **which kind of hunt** you are running. The written hunt card (hypothesis, scope, priority, pattern) is **3.2.2**. Local hunt tickets are **3.7**. This lesson is not a SIEM session.

| Type | Starts from | Execute looks like (**A12**) |
|------|-------------|------------------------------|
| **Intel-driven** | A CTI fact (domain, hash, or named behavior already in a CTI product) | Search hosts for the update domain or file CTI already worked |
| **Hypothesis-driven** | An if/then: “If they persist, we should see X” | Search HKCU Run **`Updater`** because persistors leave that key |
| **Reactive** | A known incident | After **A12**, look for more `invoice.vbs` or `update.exe` on other hosts |
| **Anomaly-based** | An odd pattern, with no intel naming it yet | Hosts with GET `:8080` `/update.exe` that **never** alerted |

**Execute** means you name the type, the seed, and the look-for. It is that product line, not a live query in this lesson.

The start is the type. A CTI domain is **intel-driven**, not an if/then. “If they persist, we should see Run **`Updater`**” is **hypothesis-driven**, even if you first heard about persistence in a report. After **A12**, more `invoice.vbs` on other hosts is **reactive**. Rewriting the **WS-JLEE** process alert is SOC work, not a reactive hunt. GET `:8080` `/update.exe` with no alert and no intel yet is **anomaly-based**.

**What good looks like:** someone gives you a seed. You name the type and the look-for. You do not write the card yet. You do not invent a ticket.

- Given: CTI already worked the update domain / file. **Intel-driven.** Search hosts for that domain / file.
- Given: “If they persist, we should see Run **`Updater`** on more hosts.” **Hypothesis-driven.** Search HKCU Run **`Updater`**.
- Given: GET `:8080` `/update.exe` on hosts that never alerted, and no intel named it yet. **Anomaly-based.**

Do not extract TTPs from a report here (**3.4.2**). Do not map the hunt to ATT&CK (**3.5**). Do not hunt “persistence” as a category (**3.6.3** is one named technique).

---

## 2. Knowledge Check

1. All four types start from a CTI report. True or false?
2. Name the four types.
3. “If they persist, we should see Run `Updater` on more hosts.” Which type, and what do you search?

---

## 3. Summary

Four types. Each has a different start. Execute is type plus look-for, not a rewritten ticket and not a SIEM session.

**Next:** **3.2.2** Hunt development.

---

## 4. Related modules

- 3.1 – Purpose of Threat Hunting (previous)
- 3.2.2 – Hunt development (the card)
- 2.11.3 – CTI RFI (intel seed)
- 3.6.3 – Hunt one named technique
- 3.7 – Site-specific hunt control (do not invent a ticket)


---

# Lesson 3.2.2 – Hunt Development Concepts

Source: `modules/03-hunter/02-methodology/02-hunt-development/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.2 B / C / C ; 3.2.2.1–3.2.2.3 3c / 4c / 4d  
- SOC: 3.2.2 A / B / B ; 3.2.2.1–3.2.2.3 1a / 1a / 2b  
- CTI: 3.2.2 A / B / B ; 3.2.2.1 1a / 2b / 3c ; 3.2.2.2 1a / 2b / 3c ; 3.2.2.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Write a **hypothesis**, **scope**, and **priority** for a hunt.
2. Name a **unique pattern** worth searching internally.

**Mapped Proficiency Items:**
- K: 3.2.2 – Hunt development concepts
- T: 3.2.2.1 – Develop and document a hunt hypothesis
- T: 3.2.2.2 – Scope and prioritize a hunt
- T: 3.2.2.3 – Identify unique patterns or behaviors suitable for hunting

---

## 1. Key Concepts

Hunters bound a search **before** they query. An unbounded look — “search everything for malware” — is not a hunt. That is the job in this lesson: write a short **hunt card** so someone else can tell what you are looking for, where, why now, and which pattern is specific enough to search internally. The card is the four-line write-up: **hypothesis**, **scope**, **priority**, and **unique pattern**.

**3.2.1** named the hunt types. This lesson is the **write-up**. It is **not** a SIEM session (**3.3.1**). It is **not** your site’s hunt ticket or form (**3.7**). It is **not** “hunt persistence” (**3.6.3**).

| Piece | Meaning | A12 example |
|-------|---------|-------------|
| **Hypothesis** | If X is true, we should see Y | If A12 persistors exist elsewhere, we see HKCU Run **`Updater`** → `%TEMP%\update.exe` |
| **Scope** | Where / how long / which telemetry | User workstations, last 14 days, registry and file events (not every log source) |
| **Priority** | Why this hunt now | Open A12 incident plus the missed `GET /update.exe` download (a false negative); not a blog read |
| **Unique pattern** | Something specific enough to search internally | Run value name **`Updater`**, not “any Run key” |

A **hypothesis** is a testable if/then, not a topic. “Hunt persistence” names a class of techniques. “If A12 persistors exist elsewhere, we see HKCU Run `Updater` pointing at `%TEMP%\update.exe`” is a hypothesis you can document and check.

**Scope** names hosts, a time window, and which telemetry you will use. It does not say the whole estate, all time, and every log source.

**Priority** is why this hunt now. An open incident and a known miss beat a vendor write-up you just read.

A **unique pattern** is a behavior or artifact you can actually search for inside the network. The Run value name `Updater` is unique enough. “Any Run key” is not.

**What good looks like:** four lines on the card. Not a SIEM query this lesson. Not “hunt persistence.”

- **Hypothesis:** If A12 persistors exist elsewhere, we see HKCU Run **`Updater`** → `%TEMP%\update.exe`.
- **Scope:** User workstations, last 14 days, registry and file events.
- **Priority:** Open A12 incident plus the missed download.
- **Unique pattern:** Value name **`Updater`**, not any Run key.

Do not invent a ticket name or a tracking board. That is local process (**3.7**).

---

## 2. Knowledge Check

1. A hunt card is “search everything for malware.” True or false?
2. What four pieces does the hunt card have?
3. Write a one-line **A12** hypothesis and one unique pattern (not “any Run key”).

---

## 3. Summary

Hypothesis, scope, priority, unique pattern. Bound the search. The classroom card is training, not a ticket name you invent.

**Next:** **3.3.1** Hunt tool capabilities.

---

## 4. Related modules

- 3.2.1 – Hunt types (previous)
- 3.3.1 – Hunt tools
- 3.6.3 – Hunt one named technique
- 3.7.2 – Local documentation


---

# Lesson 3.3.1 – Tool Capabilities for Hunting

Source: `modules/03-hunter/03-online-tools/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.3.1 B / C / C ; 3.3.1.1–3.3.1.3 3c / 4c / 4d  
- SOC: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 1a / 2b / 3c ; 3.3.1.3 1a / 2b / 3c  
- CTI: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 2b / 3c / 4c ; 3.3.1.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name each tool’s **hunt** strength and **hunt** limit (VirusTotal, AnyRun, URLScan, Silent Push).
2. From a classroom result card, pull a **hunt lead** and turn it into a **precise** internal SIEM or Zeek query.

**Mapped Proficiency Items:**
- K: 3.3.1 – Tool capabilities for hunting
- T: 3.3.1.1 – Perform advanced querying and pivoting in VirusTotal, AnyRun, URLScan, and Silent Push
- T: 3.3.1.2 – Extract actionable hunting leads from external tool results
- T: 3.3.1.3 – Convert external findings into precise internal SIEM or Zeek queries

---

## 1. Key Concepts

Hunters take a finding from an external tool and turn it into a search they can run **here**, in the SIEM or in Zeek. They do that because a public detection count, a “malicious” tag, or a screenshot does not tell you whether that activity happened on your network. That is the job in this lesson: name each tool’s hunt strength and hunt limit, pull a lead you can actually search, and write a **precise** internal query.

You work from a **classroom result card** — a copy of an external-tool result this lesson provides. You write what the card shows. You do not log in. You do not need a live vendor account.

When to pick a tool is **0.7**. How CTI reads each platform’s tabs is **2.9**. This lesson is that conversion. It is not those lessons.

| Tool | Hunt strength | Hunt limit |
|------|---------------|------------|
| **VirusTotal** | Linked objects and sandbox events (Relations / Behavior) can name a host or dropped file | A detection count is not a hunt query |
| **AnyRun** | Process and network facts from a detonation | A “malicious” tag is not a query |
| **URLScan** | Requested hosts on a URL | A screenshot is not a query |
| **Silent Push** | Other names on an **A** record (an IPv4 mapping) or an **NS** (nameserver) | The whole **/24** (a 256-address block) is noise |

**Query** means you look up a seed the card already has — a hash, an IP, a URL — and you write the related object the card shows. **Pivot** means you take that object and name the next related object on the **same** card: a contacted host, a dropped file, another name on the same A record. You do not invent a sibling. You do not open a live account.

A **hunt lead** is a named artifact you can search internally: an IP, a port, a URI, a file name, a hostname. A detection count, a “malicious” tag, or a screenshot is not a lead.

A **precise** query names that lead in SIEM or Zeek — the IP **and** the port **and** the URI. It is not a filter that matches every destination (`dest=*`). It is not the whole `/24`.

**What good looks like:**

- **Query / pivot:** the card shows the hash of `update.exe` contacted `203.0.113.88` on port `8080`. You name that host and port. You do not write a sibling domain you did not see. You do not query `203.0.113.0/24`.
- **Lead:** `GET /update.exe` to `203.0.113.88:8080`. Not “VirusTotal said malicious.”
- **Convert:** Zeek `http` `id.resp_h == 203.0.113.88 && id.resp_p == 8080 && uri == "/update.exe"` (or the SIEM equivalent). **Not** `dest=*`. **Not** a `/24`.

---

## 2. Knowledge Check

1. A VirusTotal detection count is a hunt query. True or false?
2. Name one hunt limit for Silent Push.
3. The classroom result card shows `GET /update.exe` to `203.0.113.88:8080`. Write one precise Zeek or SIEM query. Do not use a `/24`.

---

## 3. Summary

Each tool has a hunt strength and a hunt limit. A lead is a named artifact you can search here. The query names that lead — not a count, not a tag, not a screenshot, and not a whole `/24`.

**Next:** **3.4.1** Assessing CTI for hunting value.

---

## 4. Related modules

- 3.2.2 – Hunt development concepts
- 3.4.1 – Assessing CTI for hunting value
- 0.7 – External tools (when to pick)
- 2.9 – Platform-specific skills
- 1.2.5 – HTTP engine


---

# Lesson 3.4.1 – Assessing CTI for Hunting Value

Source: `modules/03-hunter/04-cti-for-hunters/01-assessing-cti/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.1 B / C / C ; 3.4.1.1 3c / 4c / 4d  
- SOC: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
- CTI: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Sort a CTI report as **hunt-worthy**, **awareness-only**, or a **hand-off** to detections or IR.
2. Triage a report: **hunt** / **don’t hunt** / **hand off**, and say why.

**Mapped Proficiency Items:**
- K: 3.4.1 – Assessing CTI for hunting value
- T: 3.4.1.1 – Triage a CTI report: hunt / don’t hunt / hand off, and say why

---

## 1. Key Concepts

A CTI report usually names an actor, a method, or a set of indicators. Before you hunt from it, you have to know whether it is worth a hunt at all. Hunters do **not** hunt every report. That is the job in this lesson: label the report first — **hunt-worthy**, **awareness-only**, or a **hand-off** — and say why. Extracting leads is **3.4.2**. STIX objects are **3.4.3**. ATT&CK coverage is **3.5**. This lesson is the **gate**: you decide whether a hunt starts.

| Label | Meaning |
|-------|---------|
| **Hunt-worthy** | You can name a question, telemetry that could answer it here, and a bound scope |
| **Awareness-only** | Useful context. No hunt from this report |
| **Hand-off** | Not a hunt. Detections or IR already own it |

The task product is **hunt**, **don’t hunt**, or **hand off**, plus why. Hunt-worthy is hunt. Awareness-only is don’t hunt. Hand-off is hand off.

**Actionable for a hunt** means you can name three things: a **question** the hunt would answer, **telemetry** that could answer it here, and a bound **scope**. “Interesting” is not a hunt. CTI’s own actionable test (**2.1.5**) is whether a product names a who and a next step. This lesson is the hunter’s test: can you hunt from the report.

**Rapid triage** is a **label and one sentence why**. You read enough to decide hunt, don’t hunt, or hand off. You do not copy every ATT&CK ID. You do not extract the lead list (**3.4.2**). If you start mapping coverage, you have left this lesson (**3.5**).

**What good looks like:** someone gives you a report. You label it and say why. You do not pull the TTP table yet.

- Given: the report names `GET /update.exe` to `203.0.113.88:8080` and HKCU Run **`Updater`**. User workstations. Registry and HTTP logs exist. No detection covers that path. No open IR on that hash. **Hunt-worthy** — hunt. You can name the question, the telemetry, and the scope.
- Given: “This APT exists.” No object, no telemetry, no scope. **Awareness-only** — don’t hunt.
- Given: IR is already working the same `update.exe` hash. **Hand-off** — detections or IR already own it.

Do not invent a hunt ticket (**3.7**). Do not author STIX (**3.4.3**).

---

## 2. Knowledge Check

1. An interesting actor profile is a hunt. True or false?
2. What three things must you name before a report is actionable for a hunt?
3. Label this report and say why: `GET /update.exe` to `:8080`, HKCU Run **`Updater`**, registry and HTTP logs exist, no detection on that path, no open IR.

---

## 3. Summary

Hunt, don’t hunt, or hand off — plus why. Actionable for a hunt means question, telemetry, and scope. Interesting is not a hunt.

**Next:** **3.4.2** Extracting hunt leads from CTI.

---

## 4. Related modules

- 3.3.1 – Tool capabilities for hunting
- 3.4.2 – Extracting hunt leads from CTI
- 3.4.3 – STIX as hunt input
- 2.1.5 – Ensuring intelligence is actionable
- 3.5.1 – Using MITRE ATT&CK for hunt planning


---

# Lesson 3.4.2 – Extracting Hunt Leads from CTI

Source: `modules/03-hunter/04-cti-for-hunters/02-extracting-leads/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.2 B / C / C ; 3.4.2.1–3.4.2.3 3c / 4c / 4d  
- SOC: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
- CTI: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Pull hunt-suitable **TTPs** and **artifacts** from a CTI report that is already worth hunting.
2. Drop what you cannot search, then state the **hunt question** those leftovers support.

**Mapped Proficiency Items:**
- K: 3.4.2 – Extracting hunt leads from CTI
- T: 3.4.2.1 – Extract hunt-suitable TTPs from a CTI report
- T: 3.4.2.2 – Extract hunt-suitable artifacts (IOCs, patterns, behaviors)
- T: 3.4.2.3 – State the hunt question those leads support

---

## 1. Key Concepts

A hunter does not paste a CTI report into a search. After a report is already worth hunting, they pull the methods and objects they can actually search internally, drop the rest, and write one **hunt question** those leftovers can answer. That is the job in this lesson: keep, drop, then the question — so you do not hunt a slogan, an expired hash, or a whole address block.

**3.4.1** is whether to hunt at all. This lesson is extract. It is **not** how to author STIX (**3.4.3** / **2.10**). It is **not** mapping the hunt onto ATT&CK (**3.5**). The full hunt-card format is **3.2.2**.

If the report is awareness-only or a full hand-off, stop. If it is mixed, extract only the hunt-worthy slice.

| Kind | What it is | Keep when it can drive a hunt |
|------|------------|-------------------------------|
| **TTP** | How they work — a method (tactic, technique, or procedure) | Specific enough, and you have **telemetry** (logs you can search) |
| **IOC** | A named object — hash, host, IP, or URL (indicator of compromise) | Current, rare enough, and queryable here |
| **Behavior** | A pattern over time | Off-baseline or scoped, not daily admin |

Copying the IOC appendix is not extract. Extract is a keep list you can search.

**Drop** what you cannot hunt:

| Drop | Why |
|------|-----|
| **No telemetry** | You cannot see it here. Name that **visibility gap**. Do not keep it as a lead. |
| **Expired IOC** | Stale, or a hash with no reuse note (for example a 2019 hash the report does not say is still in use). |
| **Noise** | A slogan TTP (“they use persistence”), a whole `/24`, or already-blocked objects that only produce volume. |

Record **ATT&CK** IDs **if the report already printed them**. Do not invent an ID the page never had. Do not open ATT&CK Navigator. Mapping this hunt onto tactics and techniques is **3.5**.

**What good looks like:** someone gives you a hunt-worthy report. You write keep TTPs, keep artifacts, drop lines, and one hunt question. The question is an if/then the leftovers can answer. It must be able to come back empty. If the leftovers cannot form that question, you extracted noise.

Classroom slice (**A12**): a vendor report leftover about the same activity this course already uses — HKCU Run **`Updater`**, a download of `/update.exe` on port **8080**, and more `invoice.vbs`.

- **Keep TTP:** HKCU Run **`Updater`** → `%TEMP%\update.exe`.
- **Keep artifacts:** `GET /update.exe` to `203.0.113.88:8080`; more `invoice.vbs`.
- **Drop:** “they use persistence”; the whole `203.0.113.0/24`.
- **Hunt question:** If more A12 persistors exist, we see Run **`Updater`**, `update.exe`, or another `invoice.vbs`.

Do not write the SIEM query here. Do not fill the four-field hunt card (**3.2.2**). Do not tell the rest of the incident.

---

## 2. Knowledge Check

1. Copying the IOC appendix is extract. True or false?
2. Name one reason to **drop** an object.
3. From the A12 slice, name one keep TTP, one keep artifact, and the hunt question.

---

## 3. Summary

Keep searchable TTPs and artifacts. Drop noise, expired objects, and anything you cannot see. One hunt question that can come back empty.

**Next:** **3.4.3** STIX as hunt input.

---

## 4. Related modules

- 3.4.1 – Assessing CTI for hunting value
- 3.4.3 – STIX as hunt input
- 3.2.2 – Hunt development concepts
- 3.5.1 – Using MITRE ATT&CK for hunt planning


---

# Lesson 3.4.3 – STIX as Hunt Input

Source: `modules/03-hunter/04-cti-for-hunters/03-stix-as-hunt-input/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.3 B / C / C ; 3.4.3.1 3c / 4c / 4c ; 3.4.3.2 3c / 4c / 4d  
- SOC: 3.4.3 A / A / B ; 3.4.3.1 1a / 1a / 2b ; 3.4.3.2 1a / 1a / 2b  
- CTI: 3.4.3 A / B / B ; 3.4.3.1 1a / 2b / 3c ; 3.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the STIX objects a hunter actually uses in a report or bundle.
2. Turn those objects into hunt leads — you do **not** author STIX here.

**Mapped Proficiency Items:**
- K: 3.4.3 – STIX as hunt input
- T: 3.4.3.1 – Identify hunt-relevant objects in a report or bundle
- T: 3.4.3.2 – Turn those objects into hunt leads

---

## 1. Key Concepts

Hunters read CTI that arrives as a **report** or as a **STIX** package. **STIX** (Structured Threat Information Expression) is the language CTI uses to label threat facts as objects. Version **2.1** is the spec this course uses. A **bundle** is a wrapper that carries those objects as one package. Structured JSON looks official. It is not automatically a hunt. Your job is to name the objects that can actually drive a search, then turn those objects into a hunt question that can fail. That is the job in this lesson.

You do **not** author, validate, or share STIX here (**2.10**). Extracting leads from prose is **3.4.2**. Mapping this hunt onto ATT&CK is **3.5**. Classroom bundle only. Do not stand up a TAXII server.

These are the objects a hunter actually uses. The name in the first column is the STIX **2.1** `type` you see in the bundle.

| Object | Hunt-relevant when |
|--------|--------------------|
| **indicator** | It is a current pattern you can query (hash, host, IP, URL) |
| **attack-pattern** | It names a method specific enough to search, and you have telemetry |
| **observed-data** | It is a recorded sample that still names something searchable |
| **malware** | It gives a current hash or named installer — not the family slogan |
| **threat-actor** / **intrusion-set** | It is a scope or priority hook. It is not a search by itself |
| **relationship** | It ties the other objects together (`indicates`, `uses`) |

**Campaign**, **course-of-action**, **identity**, and **sighting** exist in STIX **2.1**. Hunters may see them in a bundle. They are not the objects this lesson asks you to use as hunt input.

A bundle **seeds** a hunt when the objects you pick can support a question that can fail. An actor name is not a search. Dumping every IPv4 **indicator** into a block list is not a seed.

**What good looks like:** someone gives you a classroom bundle for incident **A12**. You name the hunt-relevant objects. You write the lead. You do not write STIX.

- **Identify:** `indicator` for `GET /update.exe` to `203.0.113.88:8080`; `attack-pattern` for HKCU Run **`Updater`**; `relationship` `uses`.
- **Seed:** if more persistors exist, we see that Run value or that URI.
- **Not a seed:** dump every IPv4 `indicator` into a block list.

Do not author the bundle (**2.10**). Do not open Navigator (**3.5**).

---

## 2. Knowledge Check

1. Hunters author STIX in this lesson. True or false?
2. Name four objects a hunter actually uses.
3. A classroom bundle has an `indicator` for `GET /update.exe` on `203.0.113.88:8080` and an `attack-pattern` for HKCU Run **`Updater`**. Name one hunt-relevant object and the lead it seeds.

---

## 3. Summary

Identify hunt-relevant STIX objects. Seed a question that can fail. Do not author STIX. Structured JSON is not automatically a hunt.

**Next:** **3.5.1** ATT&CK for hunt planning.

---

## 4. Related modules

- 3.4.2 – Extract leads (previous)
- 3.5.1 – ATT&CK map
- 2.10.1 – STIX types (label)
- 2.10.2 – STIX production (author / TAXII)


---

# Lesson 3.5.1 – Using MITRE ATT&CK for Hunt Planning

Source: `modules/03-hunter/05-framework-application/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 3c / 4c / 4d  
- SOC: 3.5.1 A / B / B ; 3.5.1.1–3.5.1.2 1a / 2b / 3c ; 3.5.1.3 1a / 1a / 2b  
- CTI: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Map a hunt plan or hunt findings to ATT&CK tactics and techniques.
2. Use that map to name a **detection** or **visibility** gap, and to **support** hunt priority.

**Mapped Proficiency Items:**
- K: 3.5.1 – Using MITRE ATT&CK for hunt planning and coverage analysis
- T: 3.5.1.1 – Map a hunt plan or hunt findings to MITRE ATT&CK
- T: 3.5.1.2 – Use ATT&CK to identify detection or visibility gaps
- T: 3.5.1.3 – Use ATT&CK to support hunt prioritization

---

## 1. Key Concepts

Hunters look for activity the alerts missed. Before they search, they need a shared name for the **method** they will hunt, or for the method they already found. ATT&CK is that name. Putting **this hunt** on it shows whether you can see that method, whether a detection already covers it, and whether this hunt is worth doing now. That is the job in this lesson: map this hunt, name the gap, and use the map to support priority.

You **map** a hunt when you write the method as a **tactic** (why — the goal) and a **technique** or **sub-technique** (how — the named way). Map this hunt. Do not paint the whole Enterprise matrix because a group was named. Do not invent an ID so the card looks complete.

A report may already print an ATT&CK ID. Copying that ID onto a hunt card is not a hunt map. The map is the method **this** hunt will search, or the finding **this** hunt already has.

| You write | You do not |
|-----------|------------|
| Method you will search → tactic + technique (or sub-technique) | Color every ATT&CK Navigator cell (the heatmap view) because a group was named |
| What you observed → the technique that describes *that* method | Invent an ID so the card looks complete |

This lesson maps a **hunt**. It is not labeling one alert. It is not putting IDs on a CTI product.

Reading that map for holes is **coverage analysis**. Two kinds of hole:

| Gap | Meaning |
|-----|---------|
| **Detection gap** | Telemetry exists; no detection covers that technique in this scope |
| **Visibility gap** | You cannot see the technique here — name it; do not hunt it as written |

ATT&CK **supports** priority. It does not replace scope, how fresh the lead is, or whether an incident is already open. “The tactic is red” is not a reason.

**What good looks like:**

- **Map:** the A12 hunt for the current-user (HKCU) Run value named **`Updater`** → **TA0003** Persistence / **T1547.001** Registry Run Keys / Startup Folder.
- **Detection gap:** registry telemetry exists; no detection on value name `Updater`.
- **Visibility gap:** no registry logging on that host class — not a hunt as written.
- **Priority:** open incident + a download with no alert + a mapped technique you can see. Not “Persistence is always first.”

How the Run key works on disk is **3.6.1**. Hunt-card format is **3.2.2**.

---

## 2. Knowledge Check

1. Copying T1547.001 from a report is the same as mapping this hunt. True or false?
2. What is the difference between a detection gap and a visibility gap?
3. Map the A12 Run-**`Updater`** hunt to one tactic and one technique. If registry logs exist and no detection fires on that value name, which gap is it?

---

## 3. Summary

Map this hunt. Name the gap. ATT&CK supports priority; it does not replace it.

**Next:** **3.6.1** Persistence techniques.

---

## 4. Related modules

- 3.4.3 – STIX as hunt input (previous)
- 3.6.1 – Persistence techniques
- 0.6.1 – ATT&CK floor (one activity, not this hunt)
- 2.7.1 – ATT&CK for CTI products
- 3.2.2 – Hunt card


---

# Lesson 3.6.1 – Persistence Techniques

Source: `modules/03-hunter/06-attacker-techniques/01-persistence/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.1 B / C / C ; 3.6.1.1 3c / 4c / 4c  
- SOC: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
- CTI: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name four persistence classes: registry-based, start menu / startup folder, scheduled tasks, and other common methods.
2. Recognize those methods in logs or telemetry — not a one-off run, not a registry-event write-up, not privilege escalation.

**Mapped Proficiency Items:**
- K: 3.6.1 – Persistence techniques
- T: 3.6.1.1 – Recognize persistence techniques in logs or telemetry

---

## 1. Key Concepts

Hunters look at host telemetry to see whether something will **run again** after reboot, logon, or a time trigger. SOC already described the registry **set** on that host (**1.1.5**): which hive and key changed, and who changed it. That write-up is the event. This lesson names the **method**: if Windows will launch that payload later, the set is **persistence**. Hunters do this so they can tell autorun from a one-off run, and so a later hunt can pick one named method instead of “hunt persistence.”

**Persistence** is a method that makes code **run again** after reboot, logon, or a time trigger.

This lesson is **not** how to read a registry event (**1.1.5**). It is **not** privilege escalation (**3.6.2**). It is **not** a hunt for a named technique (**3.6.3**). **3.5.1** mapped a hunt to a Persistence technique. This lesson is recognizing the mechanism.

| Class | What recognition looks like |
|-------|-----------------------------|
| **Registry-based** | A value **set** under Run, RunOnce, or Winlogon (Shell, Userinit). The **data** is the payload path Windows will launch. |
| **Start menu / startup folder** | A file or `.lnk` **created** in the user Startup folder or All Users Startup. That path runs at logon. |
| **Scheduled tasks** | A task **created** or **updated**. Name the trigger, the command, and the account it runs as. |
| **Other common methods** | A new or changed **service**, a **WMI** event subscription, or a **logon script**. Say which. |

A one-off process is not persistence. `wscript` running Temp `invoice.vbs` once is execution. The Run key that PowerShell set afterward is persistence.

A privilege change by itself is **3.6.2**.

A catalogued vendor updater under `Program Files` that writes a Run key is still persistence *as a method*. Expected autorun is still the class.

Name the **class** and the **field that proves it**. If you cannot see that class in the telemetry you have, name a **visibility gap**. Do not invent a method.

**What good looks like:**

- Given: on host **WS-JLEE**, HKCU Run value **`Updater`** = `%TEMP%\update.exe`. **Class:** registry-based persistence. **Proof:** value name + payload path. That is the method that will run again at logon.
- Given: `wscript.exe` runs Temp `invoice.vbs` once. **Not persistence.** One-off execution.
- Not this lesson: search every Run key, or write a hunt named “persistence.” That is **3.6.3**.

---

## 2. Knowledge Check

1. A one-off `wscript invoice.vbs` is persistence. True or false?
2. Name the four persistence classes.
3. Class + proof for HKCU Run **`Updater`** → `%TEMP%\update.exe`.

---

## 3. Summary

Persistence is a method that will run again. Four classes. Name the class and the proof in the log. A one-off run is not persistence. Do not hunt the tactic.

**Next:** **3.6.2** Privilege escalation techniques.

---

## 4. Related modules

- 3.5.1 – ATT&CK map (previous)
- 1.1.5 – Registry activity
- 3.6.2 – Privilege escalation techniques
- 3.6.3 – Hunt one named technique


---

# Lesson 3.6.2 – Privilege Escalation Techniques

Source: `modules/03-hunter/06-attacker-techniques/02-privilege-escalation/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.2 B / C / C ; 3.6.2.1 3c / 4c / 4c  
- SOC: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
- CTI: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name common Windows privilege-escalation methods and the indicators that prove elevation.
2. Recognize those methods in logs or telemetry — not persistence, and not a process that was already privileged.

**Mapped Proficiency Items:**
- K: 3.6.2 – Privilege escalation techniques
- T: 3.6.2.1 – Recognize privilege escalation techniques in logs or telemetry

---

## 1. Key Concepts

Threat hunters read host telemetry to see whether an actor **gained a higher privilege** than they started with. That change is **privilege escalation** (elevation): typically a standard user to administrator or **SYSTEM**. Persistence is a method that will **run again**. That was **3.6.1**. If you call a Run key elevation, you hunt the wrong class. The job in this lesson is to name the method and the indicator that proves the privilege changed. You do not hunt a named technique (**3.6.3**).

The A12 Run key **`Updater`** is **not** privilege escalation. It starts as the logged-on user. A scheduled task that runs as SYSTEM is persistence unless you also see **how** a non-privileged actor got SYSTEM.

| Method | Indicator that proves elevation |
|--------|---------------------------------|
| **Token theft / impersonation** | A user-context parent starts a child as SYSTEM (or High integrity). The parent was not already that privileged, and it is not an auto-elevate Windows binary. |
| **UAC bypass** | An **auto-elevate** Windows binary — a built-in program Windows will raise without a real consent prompt — launches an unexpected payload, and there is no real consent. |
| **Privileged service / image abuse** | The service image path points at a user-writable file, or a user who was not already privileged creates a service that then runs as SYSTEM. |
| **Other** | A named tool, named pipe, or other method you can point at, plus a SYSTEM spawn. Say which. |

A process that was **already** SYSTEM is not elevation. A user who clicked **Yes** on a signed installer is usual User Account Control (UAC) consent, not a bypass.

If you cannot see integrity level, tokens, or service-image changes, name a **visibility gap**. Do not invent a method.

**What good looks like** (classroom examples — not A12 facts):

- Given: user `helpdesk.exe` → `cmd.exe` as SYSTEM, no consent event. **Token theft.** Proof: parent identity versus child identity, and no consent.
- Given: `fodhelper.exe` → unknown executable, no consent. **UAC bypass.**
- Given: HKCU Run **`Updater`**. **Not** this class. That is persistence (**3.6.1**).

Do not hunt “privilege escalation” as a tactic. That is **3.6.3**.

---

## 2. Knowledge Check

1. HKCU Run **`Updater`** is privilege escalation. True or false?
2. Name two privilege-escalation methods.
3. A user `helpdesk.exe` launches `cmd.exe` as SYSTEM with no consent event. What method, and what indicator proves it?

---

## 3. Summary

Privilege escalation is a privilege change, not an autorun. Name the method and the indicator, or name a visibility gap.

**Next:** **3.6.3** Hunt one named technique.

---

## 4. Related modules

- 3.6.1 – Persistence techniques
- 3.6.3 – Hunt one named technique
- 3.5.1 – ATT&CK map


---

# Lesson 3.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique

Source: `modules/03-hunter/06-attacker-techniques/03-hunt-specific/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.3 3c / 4c / 4d  
- SOC: 3.6.3 1a / 1a / 2b  
- CTI: 3.6.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Turn **one named** persistence or privilege-escalation technique into a **scoped hunt**.
2. Reject “hunt persistence / hunt privilege escalation” and a hunt that uses the **wrong class**.

**Mapped Proficiency Items:**
- T: 3.6.3 – Hunt for specific persistence or privilege escalation techniques

---

## 1. Key Concepts

Hunters search for activity the alerts missed. After you can recognize a persistence or privilege-escalation method, you still have to turn it into a hunt someone can run. That is the job in this lesson: name **one method**, a **unique pattern**, and a **bound**, so you do not sweep a whole tactic and call it a hunt.

**3.6.1** and **3.6.2** taught you to *recognize* the method. This lesson **hunts one named technique**. You do not rewrite the hunt-development card (**3.2.2**). You do not open the local ticket path (**3.7**).

**Named** means a method you can point at: a current-user (HKCU) Run value named **`Updater`**, or a user parent launching a SYSTEM child. “Persistence” and “privilege escalation” are **classes**, not hunts.

A **unique pattern** is the specific thing you search — a value name, a parent/child pair, a specific binary — not every method in the class. **Scope** is where you look, how long, and which telemetry. Together those pieces are the **hunt line** — the bounded hunt in one pass:

| Piece | What you name |
|-------|----------------|
| **Named technique** | The method you can point at |
| **Class** | Persistence or privilege escalation |
| **Unique pattern** | What you search (not the whole tactic) |
| **Scope** | Where / how long / which telemetry |
| **Why not the whole tactic** | Why this pattern, not “all persistence” or “all privilege escalation” |

**What good looks like:**

- **Hunt:** HKCU Run **`Updater`** → `%TEMP%\update.exe` on user workstations, last 14 days, registry + file. Unique pattern is the **value name `Updater`**, not “any Run key.” Class is persistence. Why not the whole tactic: you are looking for this value, not every autorun.
- **Fail:** “Hunt persistence.” No unique pattern and no bound.
- **Fail:** Call a SYSTEM scheduled task privilege escalation when no elevation was shown. Wrong class. A task that *runs as* SYSTEM is persistence unless the log also shows how a non-privileged actor *got* SYSTEM.

The product is a **bounded hunt**, not a rewrite of the SOC ticket, and not a ticket name you invent.

Hunt types (**3.2.1**), the full hunt card (**3.2.2**), and ATT&CK remapping (**3.5**) are other lessons. Local control of the hunt is **3.7**.

---

## 2. Knowledge Check

1. “Hunt persistence” is a valid 3.6.3 hunt. True or false?
2. What does **named** mean in this lesson?
3. Write one hunt line for HKCU Run **`Updater`** → `%TEMP%\update.exe` (named technique, class, unique pattern, scope).

---

## 3. Summary

One named method. A unique pattern. A bound. Wrong class fails. Persistence and privilege escalation are classes, not hunts.

**Next:** **3.7.1** Hunt control and lead management.

---

## 4. Related modules

- 3.6.2 – Privilege escalation (previous)
- 3.6.1 – Persistence recognition
- 3.2.2 – Hunt card
- 3.7.1 – Local control


---

# Lesson 3.7.1 – Hunt control and lead management

Source: `modules/03-hunter/07-site-specific/01-hunt-control/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.1 B / C / C ; 3.7.1.1 3c / 4c / 4c  
- SOC: 3.7.1 A / A / B ; 3.7.1.1 1a / 1a / 2b  
- CTI: 3.7.1 A / A / B ; 3.7.1.1 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that **how hunts are initiated and controlled**, and **how leftover leads are managed**, **varies by site**.
2. **Follow** the local process you were shown — or record that you **do not have the local process yet**. Do not invent a ticket or a board.

**Mapped Proficiency Items:**
- K: 3.7.1 – Hunt control and lead management
- T: 3.7.1.1 – Follow the local process for initiating and controlling a hunt

---

## 1. Key Concepts

A hunter who already has a named technique still does not start searching the live environment on their own. The shop decides **how a hunt is opened**, **who can change its scope or stop it**, and **where leftover findings go**. That path is local. Every shop builds its own. That is the job in this lesson: obtain that path and follow it, so a hunt is official — not only interesting.

You do **not** invent a hunt ticket, a lead board, or policy for the classroom firm (**DYA**). This course does **not** publish those. **3.2.2** taught the classroom hunt card. **3.6.3** scoped one named technique. This lesson is the site path that makes a hunt official. How the hunt is written down is **3.7.2**. Finished outputs and hand-off are **3.7.3**. The SOC queue is **1.5**.

| Piece | What it is | You do not invent |
|------|------------|-------------------|
| **Initiate** | How a hunt is opened here — who may start it, and on what path | A ticket name so the hunt looks official |
| **Control** | Who may widen scope, pause, or stop | Running a hunt because the technique is interesting |
| **Leads** | Where leftovers that are not this hunt’s scope are parked, and who triages them | A personal spreadsheet or classroom board as shop policy |

A hunt **lead** in this lesson is leftover work from a hunt that is not this hunt’s scope. It is not the TTP you extracted from a CTI report (**3.4.2**). You obtain where those leftovers go. You do not stand up a board.

**Obtain-and-follow.** Ask where the initiate / control / lead path lives (the role or place your lead names). Use that path. If no one has shown you the process, write **I do not have the local process yet.** If an instructor overlays a real shop path, that overlay is the path for the room. It is still not DYA policy.

A made-up ticket number, a DYA hunt board, and a spreadsheet treated as the shop’s lead process are invented. Do not use them.

**What good looks like:** someone asks you to open a hunt, change its scope, or park a leftover.

- **Obtain:** “I obtain the initiate, control, and lead path from [the role or place the instructor names, or my lead].” If none was shown: **“I do not have the local process yet.”**
- **Follow:** Use only the path you were shown. Do not open a hunt on a made-up ticket. “Not yet” is a pass.

Do not rewrite the classroom card (**3.2.2**). Do not invent a documentation form (**3.7.2**).

---

## 2. Knowledge Check

1. You should invent a DYA hunt ticket so the exercise has a number. True or false?
2. What three path pieces does this lesson obtain?
3. What do you write if no one has shown you the process?

---

## 3. Summary

Every shop has a path to initiate a hunt, control it, and manage leftover leads. Obtain that path. Follow what you were shown. If you do not have the process, write that. Do not invent a ticket or a board.

**Next:** **3.7.2** Hunt documentation standards.

---

## 4. Related modules

- 3.6.3 – Hunt for a specific persistence or privilege-escalation technique (previous)
- 3.7.2 – Hunt documentation standards
- 3.2.2 – Hunt development concepts (classroom card)
- 2.12.1 – Local intelligence requirements and priorities (same obtain-and-follow rule)


---

# Lesson 3.7.2 – Hunt Documentation Standards

Source: `modules/03-hunter/07-site-specific/02-hunt-documentation/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.2 B / C / C ; 3.7.2.1 3c / 4c / 4c  
- SOC: 3.7.2 A / A / B ; 3.7.2.1 1a / 1a / 2b  
- CTI: 3.7.2 A / A / B ; 3.7.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two local facts you must obtain — **required elements** of hunt documentation, and **where and how** hunts are documented — and say that both **vary by site**.
2. **Document** a hunt only on the form and in the official place you were shown — or record that you **do not have the local standard yet**.

**Mapped Proficiency Items:**
- K: 3.7.2 – Hunt documentation standards
- T: 3.7.2.1 – Document a hunt according to local standards

---

## 1. Key Concepts

Hunters write the hunt on the shop’s form, in the shop’s official place, so the next person can find a complete record. That is the job in this lesson: obtain the local documentation standard, then write there. You do **not** invent a DYA hunt template or an archive path.

**3.7.1** was how a hunt is opened and controlled. This lesson is how it is **written down**. **3.2.2** already taught a classroom hunt card (hypothesis, scope, priority, unique pattern). That card is training. It is not your site’s form. What the hunt must produce, and who receives it, is **3.7.3**.

Every shop lists its own required elements and official place. A new hunter obtains them early. This course does **not** publish DYA’s hunt template or the path where hunts are stored.

| Idea | What it is |
|------|------------|
| **Required elements** | What the site form always wants on a hunt write-up. You obtain that list. You do not write one for DYA. |
| **Where and how** | The official place and method the shop uses to record hunts (sometimes called the **store**). Your lead names it. Personal notes and Slack are **not** that record. |
| **Obtain-and-follow** | Ask where the standard lives (the role or place your lead names). Write there, on that form. If no one has shown you the standard, write **I do not have the local standard yet.** |

If an instructor overlays a real shop form, that overlay is the standard for the room. It is still not DYA policy.

**What good looks like:** someone asks you to document a hunt.

- **Obtain:** “I obtain the required elements and where hunts are documented from [the role or place the instructor names, or my lead]. I write there.” If none was shown: **“I do not have the local standard yet.”**
- **Document:** only on the form and in the official place you were shown. Do **not** declare a scratch note the hunt record. Do **not** invent a template name or a folder path as policy.

The classroom card is still useful as *ideas*. It is not the site form.

Do not invent an initiate path (**3.7.1**). Do not invent an output list or recipient chart (**3.7.3**).

---

## 2. Knowledge Check

1. The 3.2.2 classroom card is the shop’s official hunt form. True or false?
2. What two things does this lesson obtain?
3. What do you write if no one has shown you the standard?

---

## 3. Summary

Every shop has hunt documentation standards. Obtain the required elements and where hunts are documented. Write there. If you do not have the standard, write that. Do not invent a template.

**Next:** **3.7.3** Hunt outputs and hand-off.

---

## 4. Related modules

- 3.7.1 – Hunt control and lead management
- 3.7.3 – Hunt outputs and hand-off
- 3.2.2 – Hunt development (classroom card)


---

# Lesson 3.7.3 – Hunt Outputs and Hand-off

Source: `modules/03-hunter/07-site-specific/03-hunt-outputs/student-guide.md`

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.3 B / C / C ; 3.7.3.1 3c / 4c / 4c  
- SOC: 3.7.3 A / A / B ; 3.7.3.1 1a / 1a / 2b  
- CTI: 3.7.3 A / A / B ; 3.7.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that **what a finished hunt must produce** and **who it is handed to** (SOC, IR, or CTI) **varies by site**.
2. **Produce** those required outputs and **hand off** only on the path you were shown — or record that you **do not have the local list yet**. Do not invent a recipient.

**Mapped Proficiency Items:**
- K: 3.7.3 – Hunt outputs and hand-off
- T: 3.7.3.1 – Produce required hunt outputs and perform proper hand-off

---

## 1. Key Concepts

Hunters finish a hunt by producing what this shop calls **done** and sending that product to the team this shop names. Inventing an output or a recipient so the hunt can close sends the work to the wrong place, or as the wrong product. That is the job in this lesson: obtain the required outputs and the hand-off path, then follow them — or write that you do not have them yet.

The hunt **product** is a **package**: more hosts, a gap. That idea is already in **3.1**. It is **not** a rewrite of the SOC ticket. **3.7.2** is where the hunt is written down. This lesson is what **leaves** the hunt.

This course does **not** publish a DYA output list or a DYA recipient list. You know **SOC**, **IR**, and **CTI** exist as kinds of teams. You do **not** know this site's names, queues, or “always IR if **A12**.”

| Idea | What it is |
|------|------------|
| **Expected outputs** | What this shop always wants when a hunt is finished. Obtain that list. Do not invent “always file an incident report.” |
| **Hand-off** | Which team and which local channel receive the package. Obtain that path. Do not invent a queue. |

**Hand-off** here means sending the finished hunt product. Shops often keep the path as a **hand-off chart**: who gets it, and on which channel. You **obtain** the output list and that chart from the role or place your lead names. You use the names **on that chart**. You do **not** invent a DYA ticket, an email address, or a DE queue so the package has somewhere to go.

SOC reporting is **1.5**. How DE reviews a hunt package is **4.5**. Those are not this site's recipient list.

**What good looks like:** someone asks you to close the **A12** hunt. You name what “done” includes here and who receives the package, or you say those lists are missing. You do not invent a recipient.

- List and chart shown: produce what the output list requires. Send the **A12** package (more hosts, the gap) on the path the chart names. Do not add a team the chart does not name.
- No list or chart: **I do not have the local output list / hand-off chart yet.** Do not email a made-up queue.

If an instructor overlays a real shop list, that overlay is for the room. It is still not DYA policy.

This closes **3.x** Hunt. Detection Engineer is **4.x**.

---

## 2. Knowledge Check

1. You should email a made-up SOC queue so the hunt is “handed off.” True or false?
2. What two things do you obtain so a hunt can close here?
3. You have not been shown a list or a chart. What do you write, and what do you **not** send?

---

## 3. Summary

Obtain the required outputs and the hand-off path. Follow them. Or write that you do not have them yet, and do not send. Do not invent a recipient. Hunt `3.x` ends.

**Next track:** **4.x** Detection Engineer.

---

## 4. Related modules

- 3.7.2 – Hunt documentation standards (previous)
- 3.1 – Purpose of threat hunting (the package)
- 1.5 – SOC reporting
- 4.1 – What DE owns
- 4.5 – Hunt and intel packages


---

# Lesson 4.1 – What DE owns

Source: `modules/04-de/01-what-de-owns/student-guide.md`

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.1 B / C / C ; 4.1.1 3c / 4c / 4c  
- SOC: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
- Hunter: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
- CTI: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what Detection Engineering **owns**.
2. Given a piece of work, say whether it is **DE**, a **nominator**, **1.3**, or a **block**.

**Mapped Proficiency Items:**
- K: 4.1 – What DE owns
- T: 4.1.1 – Sort work to DE, nominator, 1.3, or block

---

## 1. Key Concepts

Detection engineers turn what the other desks learned into lasting rules. That only works if you know which work is yours. Before you write or ship a detection, sort the request: DE owning the detections, someone nominating work, how a rule is written, or a firewall block. Mix those up and you send a rough ask away as “not DE’s problem,” or you treat a block request as a deploy. That is the job in this lesson.

DE owns the **set of detections** — the rules the shop runs: **new**, **change**, **retire**, and **deploy**. This lesson names those four. It does not teach how to do them.

| Kind of work | What it is |
|--------------|------------|
| **DE** | New, change, retire, or deploy — owning the set |
| **Nominator** | SOC, hunt, or CTI asking DE to look. A sketch is enough |
| **1.3** | How a rule *works* (syntax, a first read or write) |
| **Block** | Firewall / IA stopping traffic. Not a DE deploy |

**SOC**, **hunt**, and **CTI** **nominate**. The draft need not be perfect. A sketch is still DE’s to review. “Rough” is not “not DE’s problem.”

How a rule *works* is **1.3** — syntax, a first read or write. Detection Engineering is how we **run** detections as a service. Do not write SIGMA, Suricata, YARA, or a SIEM rule in this lesson.

**Firewall / IA** **blocks** what intel names. DE does not. A block request is not a DE deploy.

**What good looks like:** someone hands you a piece of work. You say DE, nominator, 1.3, or a block. You reject two mixes: treating a rough nomination as not DE, and treating a block request as a deploy.

- Given: “Write me a SIGMA rule for this log.” **1.3.** That is how a rule is written, not how we run detections.
- Given: “We keep missing this. Can you look?” A **nomination**. Rough is still DE’s to review.
- Given: “Block this IP at the firewall.” A **block**, not a DE deploy.

Do not invent a ticket name. Do not invent a field list. Those wait for **4.8**, and you obtain them.

---

## 2. Knowledge Check

1. What four things does DE own on the set of detections?
2. A rough nomination is not DE’s problem. True or false?
3. Someone asks you to block an IP at the firewall. Is that DE, a nominator, 1.3, or a block?

---

## 3. Summary

DE owns new, change, retire, and deploy. Nominations can be rough. 1.3 is how a rule works. A block is not a DE deploy.

**Next:** **4.2** Making a detection sound and meeting shop requirements.

---

## 4. Related modules

- 0.3 – Jobs in one sentence
- 0.4 – How work can move
- 1.3 – Detection authoring (how a rule works)
- 4.2 – Making a detection sound and meeting shop requirements


---

# Lesson 4.2 – Making a detection sound and meeting shop requirements

Source: `modules/04-de/02-sound-and-shop-requirements/student-guide.md`

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.2 B / C / C ; 4.2.1 3c / 4c / 4d ; 4.2.2 3c / 4c / 4c ; 4.2.3 3c / 4c / 4c  
- SOC: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
- Hunter: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
- CTI: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what **sound** means, and what you state before a draft or a change goes live.
2. Mark shop requirements against a list you were **shown** — or say you do not have the list.
3. Name the four **close-the-loop** notes to the nominator.

**Mapped Proficiency Items:**
- K: 4.2 – Making a detection sound and meeting shop requirements
- T: 4.2.1 – Test a draft or change: what must fire and what must not
- T: 4.2.2 – Mark which shop requirements are met and which are still missing
- T: 4.2.3 – Write the close-the-loop note to the nominator

---

## 1. Key Concepts

A detection on DE’s desk does not ship because someone asked. It ships when it is **sound** and when it meets the shop list you were shown. **Sound** means it **fires** on the activity you meant, and it does **not** fire on what it must not. The job in this lesson is that ship bar: test those two things, check the list you were shown, and tell the nominator what happened.

This lesson is **not** how to write the rule (**1.3**). **4.1** named what DE owns: new, change, retire, and deploy. This lesson is what good enough to ship looks like.

**Sound** is two facts: the detection **fires** on the intended activity, and it does **not** fire on what it must not.

**Test** a draft or a change **before it goes live**. State what **must fire** and what **must not**. If you cannot name both, you are not ready to ship.

**Shop requirements** DE owns are kinds of requirement: required **meta fields**, **naming**, **IDs**, **tags**, and **logging**. The *list* of actual fields is local (**4.8**). You check the list you were **shown**. Mark met vs missing. If nobody showed you a list, say that. Do not invent fields.

**Close the loop** with the nominator (and SOC). The note is one of: **shipped**, **changed**, **sent back**, or **retired**. That is the note, not a ticket name you made up.

**What good looks like:**

- Test: one line for must-fire, one line for must-not-fire. A draft and a change both get those two lines.
- Shop list: met / missing against a list you were shown — or “I do not have the list yet.”
- Note to the nominator: shipped / changed / sent back / retired.

Do not write SIGMA, Suricata, YARA, or a SIEM rule here. Do not invent a DYA field list. Nomination accept / send back / reject as a *review* is **4.3**.

---

## 2. Knowledge Check

1. A detection is sound when it does what two things?
2. You were not shown a shop list. Do you invent the fields?
3. Name the four close-the-loop notes.

---

## 3. Summary

Sound means it fires on the intended activity and does not fire on what it must not. Test those two before a draft or a change goes live. Check the list you were shown. Close the loop: shipped, changed, sent back, or retired.

**Next:** **4.3** Nominations from SOC, hunt, and CTI.

---

## 4. Related modules

- 4.1 – What DE owns
- 1.3 – Detection authoring (how a rule works)
- 4.3 – Nominations from SOC, hunt, and CTI
- 4.8 – Site-specific DE knowledge (the list)


---

# Lesson 4.3 – Nominations from SOC, hunt, and CTI

Source: `modules/04-de/03-nominations/student-guide.md`

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.3 B / C / C ; 4.3.1 3c / 4c / 4d  
- SOC: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
- Hunter: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
- CTI: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say who can **nominate**, and what the nomination must contain (the **need** and a **pointer**; a drafted rule only if they have one).
2. Review a nomination: **accept** for work, **send back**, or **reject** — and say who still owes what.

**Mapped Proficiency Items:**
- K: 4.3 – Nominations from SOC, hunt, and CTI
- T: 4.3.1 – Review a nomination: accept, send back, or reject, and say who finishes what

---

## 1. Key Concepts

SOC, hunt, and CTI send Detection Engineering work. That hand-off is a **nomination**. DE reviews it because a rough ask is still detection work — but only if it is clear enough to review. This lesson is who can send one, what it must contain, and how you **accept** it for work, **send it back**, or **reject** it.

**4.1** named that those three desks nominate, and that the draft need not be perfect. **4.2** was making a detection sound and closing the loop. This lesson is the inbound nomination itself.

**Who can nominate:** a **SOC analyst**, a **hunter**, or a **CTI analyst**.

A nomination can be a draft, a sketch, or “we need something on this.” It does **not** have to be production-ready.

The bar for the nominator is **“clear enough to review,”** not “ready to deploy.” Clear enough means two things are present:

- The **need** — what activity, and where it showed up.
- **Context or a reference** — this came from an investigation or an intel **report**. This lesson calls that a **pointer**. The pointer is an investigation number, or the report title and URL.

A **drafted rule** goes with it **if the nominator has one**. It is **not** required. DE can finish the rule.

Do not invent a ticket name or a form. The *kinds* of pointer are enough. Site lists and paths wait for **4.8**.

**DE review** is one of three:

| Review | What it means |
|--------|----------------|
| **Accept** for work | Need + pointer. DE will finish (including the rule if they did not send one). |
| **Send back** | Say what is missing (need, pointer, or both). The nominator still owes that. |
| **Reject** | Say why. Not DE work (a block, an investigation, or “write me SIGMA” as **1.3**). |

**What good looks like:** pick accept / send back / reject, say why, and name what the **nominator** still owes vs what **DE** will finish.

- Given: encoded PowerShell on workstations, plus the intel report title and URL. No drafted rule. **Accept.** DE finishes the rule.
- Given: the need, no pointer. **Send back.** Nominator owes the investigation number, or the report title and URL.
- Given: “Block this IP at the firewall.” **Reject.** That is a **block**, not a nomination.

Hunt and intel **packages** are **4.5**. Tunes on a *live* rule are **4.4**.

---

## 2. Knowledge Check

1. Who can nominate?
2. A nomination names the need and points at a report, but has no drafted rule. Accept or send back?
3. A nomination names the activity but has no investigation or report pointer. Accept, send back, or reject? Who still owes what?

---

## 3. Summary

SOC, hunt, and CTI nominate. Clear enough means the need plus a pointer. A drafted rule is extra if they have one. Accept, send back, or reject — and say who finishes what.

**Next:** **4.4** Tune requests from SOC.

---

## 4. Related modules

- 4.1 – What DE owns
- 4.2 – Making a detection sound and meeting shop requirements
- 4.4 – Tune requests from SOC
- 4.5 – Hunt and intel packages
- 4.8 – Site-specific DE knowledge


---

# Lesson 4.4 – Tune requests from SOC

Source: `modules/04-de/04-tune-requests/student-guide.md`

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.4 B / C / C ; 4.4.1 3c / 4c / 4d ; 4.4.2 3c / 4c / 4c  
- SOC: 4.4 A / B / B ; 4.4.1 1a / 2b / 3c ; 4.4.2 1a / 2b / 2b  
- Hunter: 4.4 A / A / B ; 4.4.1 1a / 1a / 2b ; 4.4.2 1a / 1a / 2b  
- CTI: 4.4 A / A / B ; 4.4.1 1a / 1a / 2b ; 4.4.2 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that a **tune request** is about a *live* rule, that it sits in a different **inbox** from a nomination, and that it must name **which rule** and a **pointer**.
2. Given a SOC tune request, pick **tune**, **exception**, **replace**, **leave**, or **retire** and cite why — or reject a request that is really an investigation, a **block**, or IR containment.

**Mapped Proficiency Items:**
- K: 4.4 – Tune requests from SOC
- T: 4.4.1 – Pick tune / exception / replace / leave / retire and cite why
- T: 4.4.2 – Reject a request that is investigation, a block, or IR containment

---

## 1. Key Concepts

After a detection is **live**, SOC lives with the alerts it fires. When that rule is noisy, brittle, or missing context, they ask Detection Engineering to change it. That ask is a **tune request**. This lesson is that work: you name the live rule, you point at the investigation or intel report, and you pick what to do — or you reject an ask that is really investigation, a block, or IR containment.

**4.3** was a **nomination** (something new). A tune is about a rule that is already live.

A tune request is about a *live* rule that is **noisy**, **brittle**, or **missing context**. “Missing context” here means the **rule** fires without enough of the picture. It is not the pointer below.

You sit at the same desk as nominations. The work sits in a different pile — a different **inbox**. Do not treat a tune as a new nomination.

**Clear enough to review** means two things are present:

- **Which live rule.**
- **Context or a reference** — this came from an investigation or an intel **report**. The pointer is an investigation number, or the report title and URL.

Do not invent a ticket name or a DYA form. The *kinds* of pointer are enough. The local form is **4.8**. If the pointer is missing, **send it back**. You cannot cite why without it.

**Possible answers** (only after it is clear enough):

| Answer | What it means |
|--------|----------------|
| **Tune** the logic | Change the rule so it still catches the intended activity and fires less on the rest. |
| Add an **exception** | Leave the rule; carve out what must not fire. |
| **Replace** the rule | This live rule is the wrong shape. A different rule should take its place. |
| **Leave** it | The rule is doing its job. Do not change it because someone is tired of the alert. |
| **Retire** it | This live rule should come out. When to retire in general is **4.6**. |

**Reject** a request that is really:

- an **investigation** (“go look at the host”)
- a **block** (“stop this IP at the firewall”)
- **IR containment** (“take the host off the network”)

**What good looks like:**

- Given: the live rule fires on a nightly backup *and* on the intended encoded PowerShell, plus an investigation number. **Tune** or **exception**. Keep the intended fire.
- Given: which live rule, no pointer. **Send back.** SOC owes the investigation number, or the report title and URL.
- Given: “This rule is noisy — investigate the host” or “block that IP.” **Reject.** Not a tune.

Do not write the rule (**1.3**). Hunt and intel **packages** are **4.5**.

---

## 2. Knowledge Check

1. A tune request and a nomination are the same inbox. True or false?
2. A tune request names the live rule but has no investigation or report pointer. Pick a tune answer, or send it back?
3. SOC says a live rule is noisy and asks you to investigate the host. Tune or reject?

---

## 3. Summary

Tunes are about *live* rules. Same desk, different inbox. Clear enough = which rule plus a pointer. Then tune, exception, replace, leave, or retire — and reject investigation, block, or IR.

**Next:** **4.5** Hunt and intel packages.

---

## 4. Related modules

- 4.3 – Nominations from SOC, hunt, and CTI
- 4.5 – Hunt and intel packages
- 4.6 – Detection lifecycle
- 4.8 – Site-specific DE knowledge (the local form)
- 1.3 – Detection authoring (how a rule works)


---

# Lesson 4.5 – Hunt and intel packages

Source: `modules/04-de/05-hunt-and-intel-packages/student-guide.md`

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.5 B / C / C ; 4.5.1 3c / 4c / 4d ; 4.5.2 3c / 4c / 4c  
- SOC: 4.5 A / A / B ; 4.5.1 1a / 1a / 2b ; 4.5.2 1a / 1a / 2b  
- Hunter: 4.5 A / B / B ; 4.5.1 1a / 2b / 3c ; 4.5.2 1a / 2b / 2b  
- CTI: 4.5 A / B / B ; 4.5.1 1a / 2b / 3c ; 4.5.2 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Treat a hunt or intel **package** like a **nomination** — not a finished detection.
2. Name one **add**, one **change**, or **no new rule**, and reject turning the package into a **block** list.

**Mapped Proficiency Items:**
- K: 4.5 – Hunt and intel packages
- T: 4.5.1 – Review a package: one add, one change, or no new rule
- T: 4.5.2 – Reject turning the package into a block list

---

## 1. Key Concepts

Detection engineers review inbound work from other desks. Hunters and intel send **packages** — a hunt write-up or an intel **report**. Those are inputs, not finished detections you can deploy. The job in this lesson is to review the package the same way you review a **nomination**: confirm it is clear enough, then name one **add**, one **change**, or **no new rule**, and reject a **block** list. You do that so a package does not skip review, and so extra infrastructure does not become a DE deploy.

A **package** comes from **CTI** or from **hunters**. Both are inputs. A **tune request** (**4.4**) is about a *live* rule already on the desk. A package is new inbound material from those two desks.

A package is **not** a finished detection. Treat it like a **nomination** (**4.3**). A nomination is clear enough to review when it names the **need** — what activity, where it showed up — and a **pointer**. The pointer is an investigation number, or the intel **report** title and URL. The package itself is often the pointer. A drafted rule if they have one is not required. If the need or pointer is missing, **send it back**.

Then review for a chance to add or change a detection. **“No new rule”** is a valid product.

| Product | What it means |
|---------|----------------|
| One **add** | A new detection this package supports. |
| One **change** | A live rule should change because of this package. |
| **No new rule** | Nothing to add or change. That is still a finished review. |

**Reject** turning the package into a **block** list. Extra infrastructure goes to whoever **blocks** (firewall / IA). That is not a DE deploy.

**What good looks like:**

- Given: a hunt package with the need and the package as the pointer; activity we do not detect. **Add.**
- Given: an intel report we already cover; no gap. **No new rule.**
- Given: a list of IPs to put on the firewall. **Reject.** That is a block list.

Do not write the rule (**1.3**). Do not invent a ticket. Tunes on a live rule are **4.4**. When to retire a live rule in general is **4.6**.

---

## 2. Knowledge Check

1. A package is a finished detection. True or false?
2. Name the three valid review products for a package.
3. A package is a list of IPs to put on the firewall. Add a rule, or reject?

---

## 3. Summary

Packages come from CTI and from hunters. Treat them like a nomination. Add, change, or no new rule. A block list is not DE.

**Next:** **4.6** Detection lifecycle.

---

## 4. Related modules

- 4.3 – Nominations from SOC, hunt, and CTI
- 4.4 – Tune requests from SOC
- 4.6 – Detection lifecycle
- 1.3 – Detection authoring (how a rule works)


---

# Lesson 4.6 – Detection lifecycle

Source: `modules/04-de/06-detection-lifecycle/student-guide.md`

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.6 B / C / C ; 4.6.1 3c / 4c / 4d ; 4.6.2 3c / 4c / 4d  
- SOC: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
- Hunter: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
- CTI: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Given a live rule and a reason, call **modify**, **retire**, or **leave**.
2. Given “we **blocked** this infrastructure,” decide whether the matching rule still earns its keep.

**Mapped Proficiency Items:**
- K: 4.6 – Detection lifecycle
- T: 4.6.1 – Call modify / retire / leave and cite the reason
- T: 4.6.2 – Given a block, decide whether the matching rule still earns its keep

---

## 1. Key Concepts

Detection engineers own **live** detections: rules that are already deployed. Those rules do not stay useful forever. In this job you review a detection you already own and call **modify**, **retire**, or **leave**, and you cite the reason. You do it because a noisy rule, a rule aimed at a gone threat, or a rule that only watched something now blocked should not sit unchanged — and a still-useful rule should not come out just because the queue is busy.

This lesson is that regular review. It is not a SOC request to change a noisy live rule. That request is a different inbox (**4.4**).

| Call | When |
|------|------|
| **Modify** | The rule should stay, but not as it is (too noisy, or a nomination replaced part of it). |
| **Retire** | The rule should come out (threat gone, sensor gone, a nomination replaced it, or it no longer earns its keep). |
| **Leave** | Still useful. Do not change it because someone is tired of it. |

**Earn its keep** means the rule still does useful work — it still watches something that matters.

**Reasons** you cite:

- still useful
- too noisy
- threat gone
- sensor gone
- a nomination replaced it
- already **blocked**, so the rule *may* not be needed

A **nomination** here means someone asked for a new or different detection that now covers this activity. **Sensor gone** means the log source that fed this rule is no longer there. How to check a dead sensor is **4.7**.

**A block is not automatic retire.** Whoever **blocks** (firewall / IA) already stopped that infrastructure. Ask: does this rule still earn its keep? Keep it if it still watches something else (other hosts, other paths). Retire it if it only existed for what is now blocked.

**What good looks like:**

- Given: live rule, still the right activity, too noisy. **Modify.** Reason: too noisy.
- Given: live rule, the threat is gone. **Retire.** Reason: threat gone.
- Given: live rule, still catching the intended activity; SOC is tired of it. **Leave.** Reason: still useful.
- Given: “We blocked this IP.” **Not automatic retire.** Decide if the matching rule still earns its keep.

Do not write the rule (**1.3**). Do not invent a ticket.

---

## 2. Knowledge Check

1. Name the three lifecycle calls.
2. “We blocked this infrastructure” means you must retire the matching rule. True or false?
3. A live rule still catches the intended activity. SOC wants it gone because it is busy. Modify, retire, or leave?

---

## 3. Summary

Managing live detections is regular DE work. Modify, retire, or leave — and cite the reason. A block is not automatic retire. Ask whether the rule still earns its keep.

**Next:** **4.7** Sensor availability and performance.

---

## 4. Related modules

- 4.4 – Tune requests from SOC
- 4.5 – Hunt and intel packages
- 4.7 – Sensor availability and performance
- 4.1 – What DE owns


---

# Lesson 4.7 – Sensor availability and performance

Source: `modules/04-de/07-sensors/student-guide.md`

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.7 A / B / B ; 4.7.1 2b / 3c / 3c ; 4.7.2 2b / 3c / 3c  
- SOC: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
- Hunter: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
- CTI: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that DE sometimes checks whether **sensors** are up and seeing the right place — and that this is **not** a vendor-admin course.
2. Given “the rule never fired,” say whether you would check the **rule**, the **sensor**, or **both**, and reject treating a down sensor as proof the activity did not happen.

**Mapped Proficiency Items:**
- K: 4.7 – Sensor availability and performance
- T: 4.7.1 – Given “the rule never fired,” check the rule, the sensor, or both
- T: 4.7.2 – Reject treating a down sensor as proof the activity did not happen

---

## 1. Key Concepts

Detections only fire on what a **sensor** actually saw. When a rule never fires, Detection Engineering sometimes has to ask whether that sensor was **up** and looking at the **right place**. A silent rule is not always a broken rule. A **dead** or **blind** sensor is not proof the activity did not happen. That is the job in this lesson: check the **rule**, the **sensor**, or **both**. This is **not** how to administer those tools, and it is **not** an architecture course.

A **sensor** here is a collector that records host or network activity for detections. **Sometimes** DE watches whether those collectors are up and seeing the right place. Examples: **MDE**, **Zeek**, **IDS**. “Up and seeing the right place” means the collector is working and looking at the host or path the rule needs. You are not the vendor admin. This lesson does not place sensors, size them, or log into the box.

| Word | What it means here |
|------|--------------------|
| **Dead** | The sensor is down or not sending. |
| **Blind** | The sensor is up, but it is not looking at that host or path. |

A **dead** or **blind** sensor is **not** “no threat.” The activity may still have happened. You just could not see it.

**What good looks like:**

- Given: “the rule never fired,” and the sensor was up and seeing that host. Check the **rule**.
- Given: “the rule never fired,” and the sensor was down or not seeing that place. Check the **sensor**, or **both**.
- Given: the sensor was down all week, so “nothing happened.” **Reject.** A down sensor is not proof the activity did not happen.

Do not log into the vendor box. Do not size a sensor. Do not invent a ticket or a site architecture.

---

## 2. Knowledge Check

1. A down sensor means the activity did not happen. True or false?
2. Someone says “the rule never fired.” What two things might you check?
3. Name three kinds of sensor this lesson uses as examples.

---

## 3. Summary

Sometimes DE checks whether sensors are up and seeing the right place. A dead sensor is not “no threat.” Check the rule, the sensor, or both. This is not vendor admin.

**Next:** **4.8** Site-specific DE knowledge.

---

## 4. Related modules

- 4.6 – Detection lifecycle
- 4.8 – Site-specific DE knowledge
- 1.2 – Zeek (how those logs work)
- 1.1 – Endpoint logs (MDE as a source)


---

# Lesson 4.8 – Site-specific DE knowledge

Source: `modules/04-de/08-site-specific/student-guide.md`

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.8.1 B / C / C ; 4.8.1.1 3c / 4c / 4c ; 4.8.2 B / C / C ; 4.8.2.1 3c / 4c / 4c ; 4.8.2.2 3c / 4c / 4c  
- SOC: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1 1a / 1a / 1a ; 4.8.2.2 1a / 1a / 1a  
- Hunter: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1 1a / 1a / 1a ; 4.8.2.2 1a / 1a / 1a  
- CTI: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1 1a / 1a / 1a ; 4.8.2.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that **local policy** exists — a requirements list, and a review / deploy / retire path — and that it **varies by shop**.
2. **Obtain** that policy, **follow** only what you were shown, and **reject** inventing a list, change board, or ticket name.

**Mapped Proficiency Items:**
- K: 4.8.1 – Local detection requirements
- T: 4.8.1.1 – Identify whether you have the local list and align only to a list you were shown
- K: 4.8.2 – Local review, deploy, and retire paths
- T: 4.8.2.1 – Follow the local path you were shown (or record that you do not have it yet)
- T: 4.8.2.2 – Reject inventing a change board or ticket name as policy

---

## 1. Key Concepts

A detection engineer ships a new rule, changes a live one, or retires one that no longer earns its keep. That work has to match this shop’s rules: which checks a detection must pass, how a change is reviewed and deployed, and how a retire is recorded. Those rules are local. They are not in this course. That is the job in this lesson: obtain the current list and the path, then follow only what you were shown, so you do not invent policy to make a nomination look complete.

**4.2** named the kinds of shop requirements (meta fields, naming, IDs, tags, logging) and said the *list* is local. **4.6** said you retire and deploy. This lesson is *this shop’s* current list and *this shop’s* path. You do **not** invent either. You do **not** write a rule (**1.3**). This course does **not** publish policy for the classroom firm (**DYA**).

Every shop has its own DE **policy**. It has two parts.

| Piece | What it is |
|-------|------------|
| **Local detection requirements** (the **list**) | Required meta fields, naming, and other deploy checks. They vary by shop. Obtain the current list. Do not invent one. |
| **Local review, deploy, and retire paths** (the **path**) | How a change is reviewed and deployed, and how a retire is recorded. Obtain that path. Do not invent a change board or a ticket name. |

**Obtain-and-follow** means you get the current list and path from the role or place your lead names, then use only that. If no one has shown you the list or the path, write **I do not have it yet.** If an instructor overlays a real shop list or path, that overlay is for the room. It is still not DYA policy.

**What good looks like:** someone asks you to align a nomination, ship a change, or record a retire.

- Given: someone showed you the list. You **have** it. Align the nomination or change **only** to that list. Mark met versus missing.
- Given: no one has shown you the list or the path. You **do not have it yet**. Record that. Do not fill the gap with made-up fields or a made-up ticket.
- Given: you invent “change board X” or a ticket name and treat it as policy. **Reject.**

Do not write the rule (**1.3**). Do not invent DYA policy.

---

## 2. Knowledge Check

1. This course publishes the DYA field list and deploy path. True or false?
2. You do not have the local requirements list. Do you invent the fields?
3. You invent a change board or ticket name and treat it as policy. Follow it, or reject?

---

## 3. Summary

Local policy exists. It varies by shop. Obtain the list and the path. Follow only what you were shown. Do not invent policy.

**Next:** Section 4 is complete.

---

## 4. Related modules

- 4.2 – Making a detection sound and meeting shop requirements
- 4.6 – Detection lifecycle
- 4.7 – Sensor availability and performance


---

# Companion story

Source: `docs/companion-story/story.md`

Dixon, Yamada, & Associates is a law firm. This course uses it as the firm in the scenario, not as live policy. The adversary name on the vendor PDF is **Pink River Dolphin** (**PRD**). That label is a name on a page, not proof of who they are.

Building C has a user workstation **WS-JLEE** (`10.10.8.40`). The account is `jlee` / `BUILDINGC\jlee`. The incident on that host is **A12**.

The **alert** is not the whole incident. The **notification** is not the whole investigation. CTI and hunt add facts the SOC product did not owe. Same evidence can sit on more than one desk. The *product* is different.

This story is the syllabus again, as that one case.

---

## 1. The alert in the queue

A SOC analyst gets an alert.

The detection that fired is the SIEM rule they already know how to read (**1.3**). It keys on a **process** create: parent `wscript`, child PowerShell with `-enc`, user `jlee`, host **WS-JLEE**. That is the first object in the queue. That is **A12**.

The job in this beat is to investigate the fired object (**1.4.1**), not to write a new rule.

Present on the alert: host, user, time, rule name, parent, the encoded command line. Missing until they pull more: destination IP, URI (the path on the server), file hash. Missing is a gap, not “benign.” The command line on the alert is the command line they have.

**Configuration:** PowerShell with `-enc` and parent `wscript` would fire.

**Upstream hops:** SIEM rule → SIEM alert. This is a SIEM-only process alert. There is no Suricata hop unless the given includes a Suricata rule.

This alert is process-only. A packet capture (**PCAP**) is **not applicable** until they have a flow.

Registry activity is not required to close this first pass. Hunt will use it later (**3.x**).

---

## 2. Triage

They put a label on what they have, and they cite it (**1.4.2**).

**True positive (TP).** The rule said this process chain was bad. The activity is the activity the rule is for: `wscript` launched encoded PowerShell on **WS-JLEE**. Cite: parent + `-enc`. “Malicious” without a field is a slogan, not evidence.

They pull related host logs for that host and window (**1.4.1** / **1.1**). Those logs are events: a program ran, a file changed, this host talked.

| Kind | What this beat pulled |
|------|------------------------|
| **Process** | The create that fired: `wscript` → `powershell -enc` |
| **File** | A file event **adds** Temp `invoice.vbs` and its hash |
| **Host-network** | Encoded PowerShell connected outbound to `203.0.113.88:8080`. The process is named. URI may be empty. |

Registry is a fifth kind. It is not required to close this pass. Image and driver load are not this incident.

If the tenant has no parent process, they write that the logs **fail to add** it.

The file event has a hash. They look that hash up on VirusTotal (**1.4.1** / **0.7**) during this first pass. The one-line result: the hash is **not in VT**. Relations is a later CTI skill (**2.9**), not this first pass. AnyRun is the wrong first tool: they have a hash, not a sample to detonate.

Once they have a flow, they can read the talk two ways. A **host-network** event names the initiating process: encoded PowerShell connected to `203.0.113.88` on port **8080**. A Zeek HTTP log names the protocol: method `GET`, Host `prd-updates.net`, URI `/update.exe`. Zeek does not name the process that opened the socket. If a capture exists for that flow, PCAP can **add** the URI when the alert only had IP:port.

Nothing in the queue fired on that download. That is a **false negative (FN)**. A false negative is a miss: activity that should have been detected and was not. It is not a fired alert they dislike.

The product of this beat is a TP process alert, a file path, a VT line on the hash, and a named miss on the download. Scan / root / user is a later category (**1.4.4**). Attribution is not a SOC triage field.

---

## 3. IR and leadership

SOC opens the incident product and routes it (**1.5**).

**Type:** incident report — the case record for IR. The adjacent type is a **Request for Information (RFI)**. This product is the case, not the question (**1.5.1**).

**Route** (classroom chart — not a live shop matrix): recipients are the SOC queue and **IR**. Leadership awareness is **yes** — the duty SOC lead. Approved channel is the **ticket**. Personal chat to the IR analyst only is the wrong path (**1.5.3**).

**Sam** has the host.

The leadership product is one sentence: **WS-JLEE** / `jlee`, `wscript` → encoded PowerShell, Temp `invoice.vbs`. The file hash and the Run key are not leadership fields.

Classroom clocks (**1.5.2**), not live DYA policy: the **submit — incident** clock is 30 minutes from the decision that an incident report is required. That is not the alert 15 / 45 clocks (**1.4.5**).

---

## 4. The question for intel

SOC still needs a fact they do not have: is the update domain / `203.0.113.88` the payload host — the host that served the file?

That ask is an **RFI**. It sits beside the incident. It is not a second case (**1.5.1**). Recipients are **CTI**. Leadership awareness is **no**, unless the shop chart says otherwise. Channel is the ticket or the approved RFI form. Texting a CTI friend is the wrong path (**1.5.3**).

**Jordan** owns the RFI.

Classroom clock: **submit — RFI** is 60 minutes from when the question arises (**1.5.2**).

The body is that one question. CTI will answer it. They will not rewrite the leadership notify.

---

## 5. CTI answers

Jordan receives, evaluates, prioritizes, and answers (**2.11.3**).

**Evaluate:** The question is bounded. They have the Zeek **A** record — the name-to-IP the network sensor logged — and the host file. They can answer.

**Prioritize:** An incident is open, and IR already has the host. Work now. This does not sit behind standing work such as a blog read.

The objects on the desk sit on three layers (**2.1.1**). `203.0.113.88` is **data**. The Zeek A record plus the file on **WS-JLEE** is **information**. The RFI answer is **intelligence**: a judged answer to the question.

**Respond:** **Likely** yes — the update domain / `203.0.113.88` is the payload host for A12. Treat it as such.

**Likely** is estimative language (**2.2.1**): more probable than not. It is not the confidence scale from **2.1.7**. Medium confidence names how good the sourcing is (Zeek A and the host file). It is not a country.

Diamond (**0.6.2** / **2.7.2**), filled only from evidence this beat has:

| Vertex | Fill |
|--------|------|
| **Victim** | **WS-JLEE** / `jlee` / DYA |
| **Capability** | Encoded PowerShell; `update.exe` |
| **Infrastructure** | Update domain / `203.0.113.88` |
| **Adversary** | Unknown cluster — **not** “PRD APT” |

Weakest is **Adversary**. That gap constrains the write-up. The weakest vertex is the next question, not a guess. Beacon POST is not this activity set.

The answer is not a second incident. Local queue policy is obtain-and-follow (**2.12**). A **Priority Intelligence Requirement (PIR)** list is a shop document; they obtain it.

---

## 6. One hop

While answering, CTI enriches the seed they already have: the update domain / `203.0.113.88`.

**Registration (**2.5**).** They look up registration on the domain (RDAP first; WHOIS if RDAP has no record). The nameservers on the record are `ns1.cdn-test.net` and `ns2.cdn-test.net`. Distinctive nameservers are enrichment, not a country. The IP sits in `203.0.113.0/24`. The org on that block is **Example Cloud** — who holds the address, not the actor.

**Authoritative DNS (**2.6**).** The SOA (Start of Authority) RNAME is `hostmaster.cdn-test.net`: the mailbox that runs the zone is `hostmaster` at `cdn-test.net`. That is an operator mailbox, not a country. The sibling name **`login-prd.net`** publishes the same nameserver pair and the same A record (`203.0.113.88`). Same control and same address. The whole Example Cloud prefix is not theirs.

**Hop sentence (**2.8.1**).** Seed | shared characteristic | candidate | why not coincidence:

`prd-updates.net` / `203.0.113.88` | distinctive nameserver pair `ns1.cdn-test.net` + `ns2.cdn-test.net` | candidate **`login-prd.net`** | same nameservers, same A, not a public resolver.

They reject the whole `203.0.113.0/24`. Shared hosting is not a hop.

**IOC handling (**2.8.3**).** Keep the cited current objects: the update domain, `203.0.113.88`, `login-prd.net`, and the hash of Temp `invoice.vbs`. Expire the whole `203.0.113.0/24` as shared-infrastructure noise. Link the sibling to the seed because they share nameservers and the same A — one activity set. “PRD APT” on the PDF is not a link.

**So what here (**2.8.4**).** DYA is a law firm that runs Windows workstations. Encoded PowerShell and the update-domain fetch already happened on **WS-JLEE**, so the finding applies here. The sibling shares that payload host’s control; if it is live, other workstations could use it. That is relevance and impact, not a PIR and not a country.

`login-prd.net` is extra infrastructure. It is not a SOC notify field. It is not a hunt of every name in the zone.

---

## 7. Block, not a detection

The extra name goes to whoever **blocks** — firewall or **IA** (Information Assurance) (**0.3 f**). That block is the change that follows from the relevance line: keep other workstations from using the sibling. It is not a new course, and it is not a Detection Engineering deploy. DE will **reject** a package that is only a list of IPs to put on the firewall (**4.5.2**).

SOC still owns the incident. IR still has the host. CTI still owns the answer and the hop.

---

## 8. The hunt package

Hunting exists to find what the alerts **missed**, and to name **gaps** the detections cannot see (**3.1**). The hunt product is a package, not a rewrite of the SOC ticket.

The first alert did not require the registry Run key. Hunt uses it.

**Gate (**3.4.1**):** the CTI leftovers are hunt-worthy. There is a question, telemetry that could answer it, and a bound scope. “APT exists” is awareness-only. Sam already has **WS-JLEE**; that host is a hand-off to IR. Hunt is *who else*.

**Type (**3.2.1**):** **hypothesis-driven**. If more A12 persistors exist, we should see Run **`Updater`**. The leftovers came from CTI; the start of *this* search is the if/then, not a rewritten ticket. Execute is type plus look-for, not a SIEM query and not a **3.2.2** card.

**Leads (**3.4.2**):** keep current-user (**HKCU**) Run **`Updater`** → `%TEMP%\update.exe`. Keep `GET /update.exe` `:8080`. Keep more `invoice.vbs`. Drop “they use persistence.” Drop the `/24`.

**Question:** if more A12 persistors exist, we see Run **`Updater`**, `update.exe`, or another `invoice.vbs`.

**Hunt line (**3.6.3**):** named technique = HKCU Run **`Updater`** → `%TEMP%\update.exe`. Class = persistence. Unique pattern = the value name **`Updater`**, not any Run key. Scope = user workstations, a bounded window, registry + file. Why not the whole tactic: this value, not every autorun.

ATT&CK can map *this* hunt to TA0003 / T1547.001 and name the detection gap (**3.5.1**). It does not replace the question.

How the shop **starts** a hunt, where the write-up lives, and who receives the package is local (**3.7**). A new hunter obtains that path. If no one has shown it, they write **not yet**.

The product is a **package**: more hosts, the gap, something DE can take. Same package. Different desks.

---

## 9. DE reviews the package

Detection Engineering does not own the block list. They own the set of detections (**4.1**).

SOC, hunt, or CTI may **nominate** (**4.3**). The nomination needs a **need** and a **pointer**. A drafted rule only if they have one. The local form is **4.8** — obtain it.

The hunt package is the pointer. The need is the FN download and the persistence the first alert missed. Need and pointer are present, so DE **accepts** the nomination for work. The nominator does not owe a drafted rule. DE will finish it. Send-back would be a missing need or pointer. Reject would be a block, an investigation, or “write me SIGMA” as **1.3**.

Then DE reviews the package like any other nomination (**4.5**):

- **Add** — a detection this package supports, if the shop does not already cover `Updater` / the `:8080` URI.
- **Change** — only if a live rule should change.
- **No new rule** — valid, if they already cover it.
- **Reject** — if someone handed them IPs “for the firewall.” That is beat 7, not this desk.

They do not write the detection text (SIGMA or SIEM) in this beat (**1.3**). Who finishes what stays on the card.

---

## Close

Four products. One chain.

The same `GET /update.exe` `:8080` is a SOC false negative, the CTI RFI seed, a hunt lead, and a DE gap. The evidence is the same. The products are not. A smaller shop may have one person write two of them (**0.5**).

| Desk | Product |
|------|---------|
| SOC | TP process alert on **A12**; VT line: `invoice.vbs` hash not in VT; incident to **Sam**; leadership one-liner; RFI to **Jordan** |
| CTI | Answer: likely the payload host. Hop: `login-prd.net`. Extra name to block. |
| Hunt | Package: **`Updater`** / `update.exe` / more `invoice.vbs`. Not a rewritten ticket. |
| DE | Accept for work (**4.3**). Then add or not (**4.5**). Not a block list. |

Firewall / IA took the extra name. IR still has the host.

Nothing in this file is a second plot. If a later lesson needs a new fact, add it to the [story bible](../story-bible.md) first.
