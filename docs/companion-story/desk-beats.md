# A12 evidence and handoff card

This author/instructor reference shows when to reveal established facts and how to use them. The [story bible](../story-bible.md) governs the evidence; the [story](story.md) supplies learner-facing explanation.

| Fact | Introduced in | First operational use | Keep for later |
|---|---|---|---|
| A12 initial-access mechanism is unresolved | 0.9 shared initial-access lesson | SOC investigation can identify the evidence needed to test candidate paths | Mail, web, public-facing exploit, account/remote-service, trusted-relationship, and supply-chain paths remain hypotheses unless the story bible adds supporting evidence. |
| `wscript` → encoded PowerShell on WS-JLEE / jlee | 1.1.2 | 1.4 investigation of the process alert | Framework mapping and hunt planning; malicious/unauthorized classification remains unresolved. |
| Temp `invoice.vbs` and a recorded hash | 1.4.1 context; field-reading skills in 1.1.3 | 1.4.1 endpoint context | Leadership uses relevant context; enrichment uses the hash. A literal hash and VT result are not supplied. |
| External lookup methods | 0.7 | 1.4.1 approved lookup workflow | 2.4 platform evidence: existing ANY.RUN report retrieval by hash is distinct from new detonation. |
| PowerShell sets HKCU Run `Updater` → `%TEMP%\update.exe` | 1.1.5 | 3.x persistence hunt lead | Configuration is established; target presence, execution, and persistence taking effect remain open. |
| `203.0.113.88:8080`; Host `prd-updates.net`; GET `/update.exe` | 1.1.4 / 1.2, progressively | 1.4 investigation and 2.1.5 RFI intake | 2.7.4 answers likely attempted delivery with transfer/execution unresolved. |
| No supplied alert specific to the GET | 1.4.2 classification reasoning | 3.x / 4.x coverage review | FN requires target-condition evidence, expected coverage, telemetry, and checked alert outcome. |
| `login-prd.net`; shared NS pair and observed A | 2.5.3–2.5.5 | CTI candidate pivot | Corroboration before common-control, activity-set, campaign, or attribution claims. |
| Example Cloud `203.0.113.0/24` | 2.5.1 / 2.5.5 | Candidate scope decision | Reject as too broad for promotion; expiration concerns previously valid indicators. |
| Case artifacts and scoped hypothesis | 3.x | Hunt package | Results and additional-host counts remain unspecified; use conditional language for possible findings. |
| Need and evidence pointer | 4.x | DE coverage/visibility review | Existing analytic reuse, change, add, data gap, or routing are possible outcomes; none is supplied as completed. |

## Product ownership

SOC owns the investigation record and RFI request. Jordan owns the CTI answer and candidate relationship record. Hunting develops the scoped search package. DE evaluates the need and evidence pointer against coverage and telemetry. Sam retains the affected host for IR. The protective-control owner applies the local threshold to a candidate referred for review.

Each handoff carries observations, reasoning, limitations, and the next decision. Ticket names, approval paths, and operational thresholds are intentionally left to the learner's organization.

## Separate examples

Keep OT, `pay-db-01`, vendor VPN, beacon POST, `helpdesk.exe`, Word → `helper.dll`, and unrelated SYSTEM-task examples outside the A12 event chain. The separate 1.1.3 Sysmon `update.exe` record teaches field reading; the hypothetical successful-transfer/progression records in 2.3 teach framework use. Supplied sandbox cards describe their own sessions; hypothetical DE replay or deployment cards describe practice conditions. Neither adds a local execution or deployment result to the canonical case.
