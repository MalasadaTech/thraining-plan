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

**Open (law firm vs old Harbor map):**

- **OT** (`10.10.50.0/24`, `fw-ot`, `ot-hist-01`, no span on OT) does not fit a law firm. Keep in lessons until we decide to drop or replace it.
- **`pay-db-01`** (payroll) can stay or become a client/billing system. Not decided.
- Vendor VPN and payroll SaaS via SAML are still on the old card. Not decided.

Users still do not initiate to OT **if** we keep OT. If we drop OT, delete that rule when we update 1.8.1.

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

## Companion story (later)

Not written yet. Planned shape: one short story, same facts as this file, told from more than one desk. Starting spine (from existing A12 / RFI / Sam):

SOC gets the alert → triages → sends to IR and does leadership notification → RFI to intel for more work.

Do not add new plot to that story until it is in this bible.

---

## How to update this file

When training grows:

1. Add or change the fact here (date it in the git commit; no need for a changelog in the page).
2. Then change the lesson (or the companion story).
3. If you are unsure whether a classroom row is “plot” or “extra example,” leave it off the main incident list.
