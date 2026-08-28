# Track 3 — hunt

This is classroom fiction, not live org policy. If a lesson and the story bible disagree, **the bible wins**. Night Owl / Harbor in a lesson means **Pink River Dolphin (PRD)** / **Dixon, Yamada, & Associates (DYA)**.

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
