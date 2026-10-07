# A12 story bible

This file is the **fact ledger for the recurring A12 classroom case**. Student lessons, the companion story, and later derived publications should remain consistent with it.

How lessons use the case is governed by [A12 Scenario Governance Standard](a12-scenario-governance-standard.md), including canonical facts/assessments, hypothetical A12 practice extensions, separate classroom examples, and spoiler-light progressive disclosure.

The scenario is training fiction. It supplies enough facts to support the course examples while deliberately leaving some questions unresolved. Site-specific ticket names, PIR lists, approval chains, and local control thresholds belong to the learner's real organization rather than to DYA.

Use this ledger as the factual baseline. When a revised lesson exposes an analytical overstatement, reconcile the claim here before updating the story and rebuilding the ebook. Narrow the conclusion to the available evidence rather than adding fictional evidence to preserve an older label.

---

## Canonical names

| Role / object | Canonical fact |
|---|---|
| Organization | Dixon, Yamada, & Associates (**DYA**), a law firm |
| Vendor tracking label | **Pink River Dolphin (PRD)** |
| User | `jlee` / `BUILDINGC\jlee` |
| Workstation | **WS-JLEE** (`10.10.8.40`) |
| Location | Building C, a DYA office building |
| Incident | **A12** |
| IR owner | **Sam** has the affected host |
| CTI RFI owner | **Jordan** |
| Changeover names retained for classroom examples | outgoing lead **Pat**, incoming lead **Riley** |

**PRD is a vendor tracking label.** The label may be cited as source context, but A12 does not independently establish the responsible actor's identity.

First names for Dixon or Yamada are intentionally undefined.

---

## Main incident facts

The recurring A12 chain is:

1. `wscript.exe` runs `invoice.vbs` from a Temp path on **WS-JLEE**.
2. `wscript.exe` launches encoded PowerShell (`powershell.exe -enc ...`).
3. PowerShell sets HKCU Run value **`Updater`** to `%TEMP%\update.exe`.
4. The host makes an outbound connection to `203.0.113.88:8080`.
5. Zeek HTTP evidence records a request with Host `prd-updates.net` and URI `/update.exe`.

### Evidence boundary for the request and Run configuration

The HTTP evidence establishes a **request / attempted retrieval** of `/update.exe`.

Successful transfer, creation of `%TEMP%\update.exe` from that request, execution of that file, and achievement of an attacker objective remain unresolved. The observed Run value establishes a **configured persistence mechanism**; it does not establish that its target file was present or subsequently launched. Later lessons may reveal the registry evidence without changing what was available in the initial process alert.

The teaching sequence uses **spoiler-light progressive disclosure**. Earlier orientations may preview the question or evidence class, but detailed A12 observations first appear where the learner is expected to interpret or operationally use them. Exact event timestamps and additional outcome evidence remain unspecified; a later lesson needing them requires an intentional canonical update.

---

## Initial access status

A12 begins after the possible entry point. The canonical evidence does **not** establish how `invoice.vbs` or the earlier access reached **WS-JLEE**.

Phishing/malspam, a drive-by or watering-hole path, public-facing exploitation, valid-account or remote-service abuse, a trusted relationship, and a supply-chain path remain hypotheses rather than case facts. The Temp path and later `wscript.exe` execution do not identify the delivery mechanism by themselves.

If reconstructing initial access becomes necessary, the next collection should follow the hypothesis being tested—for example mail/message records, browser/proxy evidence, identity/remote-access logs, public-facing application/service records, or third-party/software-provenance evidence. A future version of the case should establish a specific entry path only by adding the supporting observation here first.

## Initial SOC alert

The initial alert is a SIEM process alert on:

`wscript.exe` → `powershell.exe -enc ...`

with `jlee` on **WS-JLEE**.

The alert establishes that the configured detection matched the process pattern. The story does not use the rule match alone to establish maliciousness or unauthorized activity.

### Classification status

The initial alert's malicious/unauthorized target-condition assessment remains **unresolved**.

A TP label requires evidence that the assessed target condition—malicious or unauthorized activity within the stated detection requirement—is present. The companion story may describe the alert as suspicious and incident-worthy while keeping the TP/FP assessment unresolved unless sufficient evidence is supplied.

### Download-request coverage status

The story records no fired alert specifically for the `/update.exe` request.

That absence is a **coverage question**, not automatically a false negative. A confirmed FN would require:

1. evidence that the target condition is present;
2. an established expectation that the relevant detector should cover it;
3. confirmation that required telemetry reached the detector; and
4. a checked alert outcome showing no expected alert.

Detection Engineering may later assess whether the behavior represents a detection gap, a telemetry/visibility gap, existing coverage, or no required coverage.

---

## First-pass enrichment status

The investigation may use a hash, domain, or IP for an approved VirusTotal lookup.

The canonical record is **VirusTotal lookup result not supplied**. The file-event hash has no published literal value or service verdict in this case. A future lookup would record the exact searched value, report, time, and result. No live service lookup was performed to reconcile or publish this fictional case.

A hash can also be used to search for an **existing** ANY.RUN report when one exists. A new file detonation requires the actual sample or another supported submission input. The story should distinguish lookup from new submission.

---

## Infrastructure

| Object | Canonical fact | Analytical status |
|---|---|---|
| `prd-updates.net` | Host value in the A12 HTTP request | Case infrastructure / RFI seed |
| `203.0.113.88` | Address associated with the A12 network activity | Case infrastructure / RFI seed |
| `login-prd.net` | Shares the uncommon `cdn-test.net` nameserver pair and the same observed A address during the relevant period | **Candidate related infrastructure** |
| `ns1.cdn-test.net`, `ns2.cdn-test.net` | Nameserver pair used in the infrastructure example | Pivot characteristics |
| `hostmaster.cdn-test.net` | SOA RNAME used in the DNS example | Enrichment context |
| Example Cloud `203.0.113.0/24` | Shared hosting range containing `203.0.113.88` | Too broad to promote as A12 adversary infrastructure |

The overlap between `prd-updates.net` and `login-prd.net` supports a **candidate relationship worth investigating**. It does not, by itself, prove common ownership, common adversary control, one activity set, a campaign, or actor attribution.

The Example Cloud `/24` is **rejected / not promoted** as an IOC because the candidate is too broad. It is not described as an expired indicator unless it had previously been valid and later lost utility.

---

## DYA environment facts

These values are classroom stand-ins, not a complete site architecture.

| Fact | Value |
|---|---|
| User VLAN | `10.10.8.0/24` (includes WS-JLEE) |
| Servers | `10.10.20.0/24` |
| Management | `10.10.1.0/24` |
| Internet egress | `fw-edge-01` NAT `198.51.100.0/28` |
| Guest Wi-Fi | `fw-guest` |
| Mail path | `mail-edge` → `mail-filter` → `mail-int` |
| Domain controller | `dc-01` `10.10.20.10` |
| PCAP examples | `span-1` on edge; `span-2` on user↔server |

The following are separate classroom examples rather than A12 facts:

- OT network examples;
- `pay-db-01`;
- vendor VPN / payroll SaaS examples;
- `checkin.*` / beacon POST examples;
- `helpdesk.exe`;
- Word → `helper.dll`;
- SYSTEM scheduled-task examples;
- the platform-specific `update.exe` sandbox cards: observations in a supplied sandbox session are not proof of execution on WS-JLEE;
- the separate Sysmon file-event exercise in 1.1.3 that uses WS-JLEE and `update.exe`; it supplies field-reading practice, not a demonstrated link between an A12 HTTP request and a resulting file;
- hypothetical successful-transfer and progression examples in 2.3.1 and 2.3.3;
- explicitly hypothetical DE replay/deployment cards and prospective lifecycle examples. These teach possible follow-through without establishing an A12 deployment outcome.

---

## RFI

The RFI is intended to answer the role of the update domain without overstating successful delivery.

A suitable question is:

> **Was the update domain the host that successfully delivered the payload in A12?**

The evidence supports this response:

> **We assess that the update domain was likely used for attempted payload delivery in A12. `WS-JLEE` requested `/update.exe` from that destination during the suspicious activity, but current evidence does not establish successful transfer or execution of the file.**

This is a partial answer to the successful-delivery question used in 2.1.5 and 2.7.4. The delivery role is an assessment; the request is the observation. Confidence wording must explain the quality of the supporting evidence and cannot supply the missing transfer evidence. A separate fixed confidence rating is not a new case fact.

---

## Analytical-framework facts

A12 can support several framework views without changing the underlying evidence.

### ATT&CK

The observed PowerShell execution supports **T1059.001 – PowerShell** as a behavioral description. That mapping leaves authorization and maliciousness to the investigation.

A mapping such as **T1105 – Ingress Tool Transfer** requires evidence that a file or tool was actually transferred into the environment. The HTTP request alone is weaker than confirmed transfer evidence.

### Diamond Model

A defensible A12 Diamond can include:

| Vertex | A12 fill |
|---|---|
| Victim | **WS-JLEE** / `jlee` / DYA |
| Capability | encoded PowerShell; requested `/update.exe` as a candidate payload name |
| Infrastructure | `prd-updates.net` / `203.0.113.88` |
| Adversary | unresolved; PRD remains a source/vendor label |

The incomplete Adversary vertex is analytically useful and should remain unresolved rather than being completed from the vendor label.

### Cyber Kill Chain

Stage assignment depends on the role an observation played in the intrusion. The process event or HTTP request should not be translated directly into Installation or another stage without the surrounding evidence needed to support that role.

---

## How A12 facts enter the course

The same incident is revealed progressively so each role works with the evidence appropriate to its question. Under the [A12 Scenario Governance Standard](a12-scenario-governance-standard.md), orientations and advance organizers may preview questions/evidence classes but should not reveal detailed canonical observations before the mapped lesson below.

| Fact | First introduced / planted | First operational use | Keep for later |
|---|---|---|---|
| A12 initial-access mechanism remains unresolved | 0.9 common initial-access lesson | 1.x investigation may identify what evidence would test a path | Keep mail/web/exploit/account/third-party paths as hypotheses unless canonical evidence is added |
| `wscript` → encoded PowerShell on WS-JLEE | 1.1.2 process activity | 1.4 initial alert/investigation | Later framework and hunt examples may reuse it |
| Temp `invoice.vbs` and its hash | 1.4.1 context; file-event interpretation taught in 1.1.3 | 1.4.1 related endpoint evidence | Leadership can use the path; a lookup uses the hash |
| VT / external lookup workflow | 0.7 tool survey | 1.4.1 approved lookup | Record “lookup result not supplied”; retain provenance if a result is later supplied |
| HKCU Run `Updater` → `%TEMP%\update.exe` | 1.1.5 registry activity | 3.x hunt lead | The first process alert does not need this field |
| Outbound `203.0.113.88:8080` + HTTP `GET /update.exe` to `prd-updates.net` | 1.1.4 / 1.2 network evidence | 1.4.1 investigation and 2.7.4 RFI evidence | Treat as request/attempt until transfer evidence is supplied |
| No fired alert specifically for the GET | 1.4.2 classification discussion | 3.x / 4.x coverage question | Confirm expectation + telemetry + target condition before calling FN |
| `login-prd.net` shares uncommon NS pair + same observed A | 2.5.3–2.5.5 | Infrastructure pivot | Keep as candidate until corroborated |
| Example Cloud `/24` | 2.5.1 / 2.5.5 | IOC/pivot scope check | Reject as too broad for promotion |
| Hunt package: `Updater`, `update.exe`, `invoice.vbs`, request pattern | 3.x | Hunt product and DE nomination pointer | Local ticket/control names remain site-specific |
| DE coverage review | 4.x | Assess existing coverage, visibility, and need for change | Outcome may be add/change/no new rule/data gap |

---

## Product boundaries

The same evidence may support different products because each role is answering a different question.

- **SOC** investigates the alert, records the evidence and unresolved questions, routes the incident, and raises the RFI.
- **CTI** answers the intelligence requirement, preserves uncertainty, and develops candidate relationships for further analysis.
- **Threat Hunting** converts supported behaviors and artifacts into a bounded search for related activity.
- **Detection Engineering** reviews the need and pointer, checks current coverage/visibility, and decides whether a detection change is warranted.
- **IR** continues to own host containment and incident response actions.
- **Protective-control owners** decide whether candidate infrastructure should be blocked under local policy and evidence thresholds.

The course may use one person in multiple roles in a small organization; the products and questions remain distinct.

---

## Companion story

The learner-facing retelling is in [companion-story/story.md](companion-story/story.md).

Its sequence is:

**SOC alert → investigation and escalation → RFI → CTI assessment → candidate infrastructure pivot → protective-control consideration → hunt package → Detection Engineering coverage review**

The companion story should explain the reasoning between those steps rather than compressing it into slogans or boundary-only language.

---

## Outcome boundary

The case reaches a hunt package and a Detection Engineering coverage review. Additional affected-host counts, a completed coverage decision, deployment, eradication, and incident closure remain unspecified. The protective-control owner receives a candidate for review; no block or monitoring action is asserted as completed.

## Updating A12

When the training needs a new case fact:

1. Add or change the factual baseline here.
2. Update the lesson or lessons that plant or use that fact.
3. Update the companion-story outline and finished story.
4. Rebuild derived learner publications, including the ebook manuscript.

If a classroom example is useful but does not belong to the A12 chain, use the scenario-status labels and separation rules in [A12 Scenario Governance Standard](a12-scenario-governance-standard.md) rather than silently promoting it into the incident.
