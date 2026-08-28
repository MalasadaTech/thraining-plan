This is classroom fiction, not live org policy. If a lesson and the story bible disagree, **the bible wins**. Night Owl / Harbor in a lesson means **Pink River Dolphin (PRD)** / **Dixon, Yamada, & Associates (DYA)**.

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
