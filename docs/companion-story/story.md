# A12 — the same incident from four desks

Dixon, Yamada, & Associates is a law firm. This course uses it as the firm in the scenario, not as live policy. The adversary name on the vendor PDF is **Pink River Dolphin** (**PRD**). That label is a name on a page, not proof of who they are.

Building C has a user workstation **WS-JLEE** (`10.10.8.40`). The account is `jlee` / `BUILDINGC\jlee`.

What happened is one chain:

1. `wscript` runs `invoice.vbs` from Temp.
2. That launches hidden encoded PowerShell (`powershell -enc`).
3. PowerShell sets HKCU Run **`Updater`** → `%TEMP%\update.exe`.
4. The host GET `update.exe` on port **8080** to `prd-updates.net` / `203.0.113.88`.

The **alert** is not the whole incident. The **notification** is not the whole investigation. CTI and hunt add facts the SOC product did not owe. Same evidence can sit on more than one desk. The *product* is different.

This story is the syllabus again, as that one case.

---

## 1. The queue row

A SOC analyst gets an alert.

The detection that fired is the one they already know how to read (**1.3**). It keys on a process create: parent `wscript`, child PowerShell with `-enc`, user `jlee`, host **WS-JLEE**. That is the first object in the queue. That is **A12**.

The analyst does not write a new rule. They investigate the fired object (**1.4.1**).

Present on the row: host, user, time, rule name, parent, the encoded command line. Missing until they pull more: dest IP, URI, file hash. Missing is a gap, not “benign.”

They do not invent a command line. They do not need the Run key on this first pass.

---

## 2. Triage

They put a label on what they have, and they cite it (**1.4.2**).

**True positive.** The rule said this process chain was bad. The activity is the activity the rule is for: `wscript` launched encoded PowerShell on **WS-JLEE**. Cite: parent + `-enc`. A slogan is not evidence.

Endpoint logs for that host and window add the dropper path: Temp `invoice.vbs`. That is what they pulled. The file row has a hash. They look that hash up on VirusTotal (**1.4.1** / **0.7**) during this first pass and write the one-line result — what VT adds, or that the hash is not in VT. They do not open Relations. If the tenant has no parent process, they write that the logs **fail to add** it. Opening the table is not the task.

They also see a miss. Zeek or PCAP — if they have a flow — shows `GET /update.exe` to `203.0.113.88:8080`. Nothing in the queue fired on that download. That is a **false negative**. FN is not a fired alert they dislike. It is activity that should have been detected and was not.

HKCU Run **`Updater`** is already on the host. It is **not** on this first alert, and it is not required to close the triage. Hunt will use it.

They do not classify the case as a nation-state. They do not pick a scan/root/user category as the whole story. They have a TP process alert, a file path, a VT line on the hash, and a named miss on the download.

---

## 3. IR and leadership

SOC opens the incident product and routes it (**1.5**).

**Type:** incident. Not an RFI. Not a second case.

**Route (training chart — not a live shop matrix):** recipients are the SOC queue and **IR**. Leadership awareness is **yes** — the duty SOC lead. Approved channel is the **ticket**. Personal chat to the IR analyst only is the wrong path.

**Sam** has the host.

The leadership product is one sentence: **WS-JLEE** / `jlee`, `wscript` → encoded PowerShell, Temp `invoice.vbs`. It does not need the file hash. It does not need the Run key. It does not need the sibling domain.

The clocks in **1.5.2** are for this course. This story does not invent DYA SLAs.

---

## 4. The question for intel

SOC still needs a fact they do not have: is the update domain / `203.0.113.88` the payload host?

That is an **RFI**, not a rewrite of the incident (**1.5.1**). Recipients are **CTI**. Leadership awareness is **no**, unless the shop chart says otherwise. Channel is the ticket or the approved RFI form. Texting a CTI friend is the wrong path.

**Jordan** owns the RFI.

The question is the question. SOC does not invent a second one. They do not ask CTI to rewrite the notify.

---

## 5. CTI answers

Jordan evaluates, prioritizes, and answers (**2.11.3**).

**Evaluate:** the question is bounded. They have Zeek A and the file. They can answer.

**Prioritize:** open incident, IR already has the host. Work now. Not behind a blog read.

**Respond:** **Likely** yes — the update domain / `203.0.113.88` is the payload host for A12. Treat it as such.

No country. No “PRD APT” as proof. No second incident. Local queue policy is obtain-and-follow (**2.12**). This story does not invent a DYA PIR list.

---

## 6. One hop

While answering, CTI hops from the seed they already have (**2.8.1**). They do not re-teach RDAP or SOA this hour. They write a sentence:

`prd-updates.net` / `203.0.113.88` | distinctive NS pair `ns1.cdn-test.net` + `ns2.cdn-test.net` | candidate **`login-prd.net`** | same NS, same A, not a public resolver.

They reject the whole `203.0.113.0/24`. Shared hosting is not “theirs.”

`login-prd.net` is extra infrastructure. It is not a SOC notify field. It is not a hunt of every name in the zone.

---

## 7. Block, not a detection

The extra name goes to whoever **blocks** — firewall or IA (**0.3 e**).

That hand-off is a block / blacklist request. It is not a new course. It is not a DE deploy. Detection Engineering will **reject** a package that is only a list of IPs to put on the firewall (**4.5.2**).

SOC still owns the incident. IR still has the host. CTI still owns the answer and the hop.

---

## 8. The hunt package

Hunting exists to find what the alerts **missed**, and to name **gaps** the detections cannot see (**3.1**). It is not a rewrite of the SOC ticket.

The first alert did not require the Run key. Hunt uses it.

**Gate (**3.4.1**):** the CTI leftovers are hunt-worthy. There is a question, telemetry that could answer it, and a bound scope. Not “APT exists.” Not a full hand-off to IR — Sam already has **WS-JLEE**; hunt is *who else*.

**Leads (**3.4.2**):** keep HKCU Run **`Updater`** → `%TEMP%\update.exe`. Keep `GET /update.exe` `:8080`. Keep more `invoice.vbs`. Drop “they use persistence.” Drop the `/24`.

**Question:** if more A12 persistors exist, we see Run **`Updater`**, `update.exe`, or another `invoice.vbs`.

That is **one named** technique (**3.6.3**), not “hunt persistence.” Unique pattern is the value name **`Updater`**, not any Run key. Scope is user workstations, a bounded window, registry + file. ATT&CK can map *this* hunt to TA0003 / T1547.001 and name the detection gap (**3.5.1**). It does not replace the question.

How the shop **starts** a hunt, where the write-up lives, and who receives the package is local (**3.7**). A new hunter obtains that path. If no one has shown it, they write **not yet** and they do not invent Hunt-17.

The product is a **package**: more hosts, the gap, something DE can take. Same package. Different desks.

---

## 9. DE reviews the package

Detection Engineering does not own the block list. They own the set of detections (**4.1**).

SOC, hunt, or CTI may **nominate** (**4.3**). The nomination needs a **need** and a **pointer**. A drafted rule only if they have one. This story does not invent a DYA form. The local form is **4.8** — obtain, do not invent.

The hunt package is the pointer. The need is the FN download and the persistence the first alert missed.

DE reviews it like any other package (**4.5**):

- **Add** — a detection this package supports, if the shop does not already cover `Updater` / the `:8080` URI.
- **Change** — only if a live rule should change.
- **No new rule** — valid, if they already cover it.
- **Reject** — if someone handed them IPs “for the firewall.” That is beat 7, not this desk.

They do not write the SIGMA or the SIEM rule in this story (**1.3**). They accept the nomination for work, or they send it back for a missing need or pointer. Who finishes what stays on the card.

---

## Close

Four products. One chain.

| Desk | Product |
|------|---------|
| SOC | TP process alert on **A12**; VT line on the `invoice.vbs` hash; incident to **Sam**; leadership one-liner; RFI to **Jordan** |
| CTI | Answer: likely the payload host. Hop: `login-prd.net`. Extra name to block. |
| Hunt | Package: **`Updater`** / `update.exe` / more `invoice.vbs`. Not a rewritten ticket. |
| DE | Nomination review. Add or not. Not a block list. |

Firewall / IA took the extra name. IR still has the host.

Nothing in this file is a second plot. If a later lesson needs a new fact, add it to the [story bible](../story-bible.md) first.
