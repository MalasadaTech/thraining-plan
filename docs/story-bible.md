# Story bible

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

This is the one chain that is “what happened.” Other classroom rows can reuse the names; they are **not** the plot unless we promote them here.

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

- **OT** (`10.10.50.0/24`, `fw-ot`, `ot-hist-01`, no span on OT) is **not** DYA plot. A law firm does not run that plant network. Do not use OT in the companion story. Leftover classroom rows may still say OT until a rename pass; they are not architecture policy.
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
- Side rows (SYSTEM scheduled task, `helpdesk.exe`, Word → `helper.dll`) use the same user/host. They are extra examples, not the plot.

---

## When each fact appears

One chain. Each lesson plants or reads a beat. The **alert** is not the whole incident. The **notification** is not the whole investigation. CTI and hunt add facts the SOC product did not owe.

Do not invent a second plot. Extra classroom rows (`helpdesk.exe`, Word → `helper.dll`) stay off this table.

| Beat (already in “Main incident”) | First teach / plant | First *use* in the flow | Do **not** dump it in |
|-----------------------------------|---------------------|-------------------------|------------------------|
| `wscript` → hidden `powershell -enc` on **WS-JLEE** / `jlee` | **1.1.2** process | **1.4** the alert (this is what fired) | — |
| `invoice.vbs` in Temp (file row, hash) | **1.1.3** file | **1.4.1** investigation; **1.5** notify / escalate (path + hash we have) | Leadership one-liner does not need the hash |
| HKCU Run **`Updater`** → `%TEMP%\update.exe` | **1.1.5** registry | **3.x** hunt (more hosts the alert missed) | Not in the first alert. Not required on the leadership notify |
| Host GET `update.exe` :8080 to PRD domain / `203.0.113.88` | **1.1.4** host-network + **1.2** Zeek | **1.4.1** if they pull PCAP/Zeek; **2.11.3** RFI seed (the domain) | Not all of this in the leadership notify |
| Sibling `login-prd.net`, same NS, same A, SOA | **2.5** / **2.6** / **2.8** | **2.x** enrichment; extra infra → **block** (0.3 e) | Not a SOC notify field |
| Hunt package: look for `Updater` / `update.exe` / more `invoice.vbs` | **3.x** | Hunt product; same package can go to **4.x** DE | Not a rewrite of the SOC ticket |
| Nomination / tune / new rule | **4.x** | After the hunt or SOC “we keep missing this” | Not invented in 1.1 |

**Alert (1.4):** only what a detection would fire on first — the process create (`wscript` → encoded PowerShell).

**Notify / escalate (1.5):** what SOC knows at hand-off — host, user, process chain, the `.vbs` they pulled. One sentence for leadership. The RFI asks intel to work the domain / file, not to rewrite the notify.

**CTI:** more infrastructure and “so what.” **Hunt:** activity the alerts missed. **DE:** lasting rule. Same evidence can sit on more than one desk (**0.4**); the *product* is different.

When we revise a 1.1 / 1.2 / 1.4 / 1.5 lesson, plant or read only that row’s beat. Do not retell the whole chain.

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
3. If you are unsure whether a classroom row is “plot” or “extra example,” leave it off the main incident list.
