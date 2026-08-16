# Module 1.8.1 – Environment Orientation

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.8.1.1 A / B / C · 1.8.1.2 2b / 3c / 4c  
- Hunter: 1.8.1.1 B / C / C · 1.8.1.2 2b / 3c / 4c  
- CTI: 1.8.1.1 A / B / B · 1.8.1.2 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the seven **orientation** facts on the site card.
2. Identify **which fact** applies to a situation and **why it is not the adjacent fact**.

**Mapped Proficiency Items:**
- K: 1.8.1.1 – Environment orientation
- T: 1.8.1.2 – Identify which orientation fact applies and reject the adjacent fact

---

## 1. Key Concepts

This hour is **where things sit** on the site. How you **download** PCAP is **1.8.2**. Tool URLs are **1.8.3**. Zeek field reading is **1.2**. Host-observed network is **1.1.3**.

**Classroom site card — Harbor (this lesson only, not a live org policy):**

| Fact | Outline | Harbor stand-in |
|------|---------|-----------------|
| **Egress** | a | User/server internet via **`fw-edge-01`** NAT `198.51.100.0/28`. Guest Wi-Fi via **`fw-guest`** (separate door). |
| **Segments** | b | Users `10.10.8.0/24` (WS-JLEE). Servers `10.10.20.0/24`. OT `10.10.50.0/24`. Mgmt `10.10.1.0/24`. Users do **not** initiate to OT. |
| **Email** | c | Inbound MX **`mail-edge`** → **`mail-filter`** → Exchange **`mail-int`**. Outbound is the reverse. Not “just fw-edge NAT.” |
| **Choke points** | d | **`fw-edge-01`** (internet). **`fw-ot`** (everything → OT). **`fw-guest`**. |
| **Third-party** | e | Vendor VPN **`vpn-vendor`** → `10.10.90.0/24`. Payroll SaaS via SAML **`idp-corp`**. |
| **Crown jewels** | f | Payroll DB **`pay-db-01`** `10.10.20.15`. DC **`dc-01`** `10.10.20.10`. OT historian **`ot-hist-01`** `10.10.50.20`. |
| **PCAP sensors** | g | **`span-1`** on fw-edge (internet). **`span-2`** on core (user ↔ server). **No sensor** on `fw-ot`. |

If your site posts a real card, use it. The obligation is **seven facts + pick the right one**, not these names.

| This lesson | Other |
|-------------|-------|
| Where the sensor *is* | How to export/view PCAP — **1.8.2** |
| Which choke / segment | Zeek `id.orig_h` reading — **1.2.2** |
| Crown jewel vs user host | IR severity / containment — **1.8.5** |

The task is **fact + rejected neighbor**, not “describe the network.”

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| WS-JLEE → 203.0.113.88:8080 = **egress** via fw-edge / **span-1** can see it | Calling that OT / fw-ot |
| Vendor invoice mail = **email path** (mail-edge) | Treating it as raw user NAT only |
| Need PCAP of ot-hist-01 = **sensor gap** (no span on fw-ot) | Assuming span-2 sees OT |

---

## 2. Detailed Walkthrough / Examples

### Example 1: A12 Beacon Egress (Expected)

**Situation:** `WS-JLEE` (`10.10.8.40`) GET `update.exe` to `203.0.113.88:8080`.

**Fact:** **Egress (a)** via `fw-edge-01`. **Sensor (g)** that can see it: **`span-1`**. Segment is user VLAN (b), but the *question* “how did it leave?” is egress.  
**Not OT / fw-ot:** `10.10.8.0/24` is not `10.10.50.0/24`.  
**Not email:** This is HTTP, not the MX path.

### Example 2: Invoice Mail vs Egress (Lead)

**Situation:** User reports a vendor PDF via email. You need the path the message took.

**Fact:** **Email flow (c)** — `mail-edge` → `mail-filter` → `mail-int`.  
**Not egress-only:** Mail does not leave as raw `fw-edge` user NAT. Those are adjacent and both “off-box,” but the card separates them.  
**Lead:** “It went to the internet” is true and the **wrong fact**.

### Example 3: OT Historian — No Sensor (Lead)

**Situation:** Hunt wants PCAP of `ot-hist-01` (`10.10.50.20`) talking east-west.

**Fact:** **PCAP sensors (g)** — **no sensor on `fw-ot`**. Also **segment (b)** / **choke (d)** (`fw-ot`), but the *gap* you must name is the missing span.  
**Not span-2:** span-2 is user ↔ server core, not OT.  
**Lead:** Do not promise a 1.8.2 download for a sensor that does not exist.

---

## 3. Hands-On Exercise

**Objective:** Name the fact and reject the neighbor.

**Use the Harbor card** unless the instructor overlays a site card.

**Instructions:**

1. One sentence each for Examples 1–3: fact + rejected neighbor.
2. For each item, write **fact (letter)**, **adjacent you reject**, and **why**.

   - A. `pay-db-01` is the payroll database. A beacon from it is not “just another server.”
   - B. Guest laptop hits the same 8080 IP. Which **egress** door?
   - C. Helpdesk scanner `10.10.8.90` — is that **third-party VPN** (`10.10.90.0/24`) or the **user segment**?
   - D. You need packets of `WS-JLEE` ↔ `10.10.20.10` (DC). Which **sensor**?

3. Do not download PCAP (**1.8.2**). Do not open a tool URL (**1.8.3**). Do not write the IR step (**1.8.5**).
4. If two facts are both true, name the one the *question* is asking about.

**Expected Outcome:**
- Three example summaries
- Four fact + neighbor pairs
- No PCAP export, no IR playbook

---

## 4. Knowledge Check

1. Name the seven orientation facts.
2. How does **guest** egress differ from **user** egress on the Harbor card?
3. Why is **email flow** not the same fact as **internet egress**?
4. Which Harbor sensor sees OT? What do you say if none does?
5. Why is “describe the network” not enough for sign-off?

---

## 5. Summary

- Seven facts. Pick the one the situation is asking about. Reject the neighbor.
- Next: PCAP download and view tool (**1.8.2**).

---

## 6. References & Further Reading

- Related modules:
  - 1.7.2 – Changeover report content (previous unit)
  - 1.8.2 – PCAP handling (next)
  - 1.1.3 – Host-observed network
  - 1.2.2 – Conn engine
- Local environment / architecture card (optional — substitutes Harbor)
