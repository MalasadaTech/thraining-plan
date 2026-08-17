# Companion story outline

This is the training outline again, as one incident. It is not a second plot.

**Canon:** [story-bible.md](../story-bible.md). If this file and the bible disagree, the bible wins.

**Training fiction only.** Not live org policy. Do not invent DYA hunt tickets, PIR lists, approval chains, or a site architecture card.

---

## Purpose

After the lessons, a reader should be able to walk **A12** from the first queue row to the last hand-off and see the same beats the syllabus already taught.

The story does not teach new obligations. It names which desk owns which product.

---

## Names (from the bible)

| Thing | Canonical |
|-------|-----------|
| Company | Dixon, Yamada, & Associates (**DYA**), law firm |
| Adversary label | Pink River Dolphin (**PRD**) — a vendor label, not proof of who they are |
| User / host | `jlee` / `BUILDINGC\jlee` on **WS-JLEE** (`10.10.8.40`), Building C |
| Incident | **A12** |
| IR | **Sam** has the host |
| RFI owner | **Jordan** (CTI) |
| Payload | `GET /update.exe` on port **8080** to `prd-updates.net` / `203.0.113.88` |
| Dropper | `invoice.vbs` in Temp |
| Persistence (not on first alert) | HKCU Run **`Updater`** → `%TEMP%\update.exe` |
| Sibling infra | `login-prd.net` — same NS pair, same A |
| Not plot | OT network, `pay-db-01`, `checkin` / beacon POST, `helpdesk.exe`, Word → `helper.dll` |

Do not invent first names for Dixon or Yamada.

---

## Spine (nine beats)

These are the same nine steps from the course todo. Each beat maps to teaching-unit IDs. Plant or read only that beat’s facts.

| # | Beat | Desk | Product | Teach / read |
|---|------|------|---------|--------------|
| 1 | A SOC analyst gets an alert | SOC | Queue row | **1.3** wrote the rule. **1.4.1** is the fired object: `wscript` → `powershell -enc` on **WS-JLEE** / `jlee`. |
| 2 | They triage it | SOC | Label + cite | **1.4.2** TP on the process alert. **1.4.1** file row adds Temp `invoice.vbs` and its hash. SOC looks that hash up on **VirusTotal** (one line: what it adds, or not in VT). Not Relations. **FN:** `GET /update.exe` `:8080` with no queue row. Run key is **not** required on this pass. |
| 3 | Forward to IR and leadership notify | SOC | Incident route | **1.5.1** type = incident. **1.5.2** clocks (training). **1.5.3** SOC + **IR Sam**; leadership **yes**; approved **ticket**. One sentence for leadership: host, user, process chain, the `.vbs`. Not the hash. Not the Run key. |
| 4 | RFI to CTI | SOC | Question, not a second case | **1.5.1** type = RFI. **1.5.3** recipients **CTI**; leadership **no**; ticket or approved RFI form. Question: is the update domain / `203.0.113.88` the payload host? **Jordan** owns it. |
| 5 | CTI works the RFI | CTI | Answer | **2.11.3** receive → evaluate → answer. Open incident + IR has the host → work now. Response: **likely** yes — treat it as the payload host. No country. No second incident. |
| 6 | Enrich; find more infra | CTI | Hop sentence | **2.5** / **2.6** / **2.8.1**. Seed = update domain / `203.0.113.88`. Shared NS `ns1.cdn-test.net` / `ns2.cdn-test.net` → candidate **`login-prd.net`**. Reject the whole `/24`. |
| 7 | Extra infra to firewall / IA | CTI → block team | Block / blacklist | **0.3 e**. Extra adversary infrastructure is a **block**, not a DE job (**4.5.2**). Not a new course. |
| 8 | Hunt package | Hunt (CTI seeds) | Package, not a rewritten ticket | **3.1** purpose: missed activity + gaps. **3.4** gate then leads. **3.6.3** one named technique: HKCU Run **`Updater`**. Look for `Updater` / `update.exe` / more `invoice.vbs`. Obtain local control (**3.7**); do not invent a ticket. |
| 9 | Same package to DE | DE | Nomination review | **4.3** / **4.5**. Need + pointer. **Add** a detection if the FN path is a gap. **Reject** turning the package into a block list. Do not write the rule here (**1.3**). Local form is **4.8**. |

---

## What each desk does *not* owe

| Desk | Does not dump / invent |
|------|------------------------|
| SOC first alert | Run key, sibling domain, nation-state, hunt ticket |
| Leadership notify | File hash, Run key, `/24`, DE rule text |
| RFI | A rewritten incident; a second question |
| CTI enrich | OT, payroll DB, invented PIR-01 |
| Hunt | “Hunt persistence”; a made-up Hunt-17 |
| DE | Firewall blocks; a finished SIGMA/YARA in this story |

---

## Shared-floor hooks (not extra plot)

The reader already sat **0.x** before SOC. The story may *name* those hours. It does not retell them.

- **0.2** DYA / PRD names live here first.
- **0.3** jobs in one sentence; extra infra → block.
- **0.4** same evidence, different products; one person may wear two hats.
- **0.6.1** ATT&CK map of *this* hunt is **3.5**, not the first alert.
- **0.7** VT is context on a hash/IP/domain you already have. SOC uses it on the first pass in **1.4.1**, not as a Relations hour.
- **0.8** ask your shop; do not invent spans or a DYA site card.

---

## Story shape (for the finished file)

1. Title and one-paragraph setup (DYA, Building C, A12).
2. One section per spine beat, in order.
3. Close: same chain, four products (SOC case, CTI answer + hop, hunt package, DE review).
4. No epilogue that adds plot.

Length follows the beats. Do not pad.
