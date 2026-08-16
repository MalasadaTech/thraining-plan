# Module 1.5.2 – Diamond Model

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C · 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 B / C / C · 1.5.2.2 3c / 4c / 4d  
- CTI: 1.5.2.1 B / C / C · 1.5.2.2 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of the Diamond Model.
2. Name the four core features (vertices): **Adversary**, **Capability**, **Infrastructure**, **Victim**.
3. Apply the model to a case: **fill all four vertices** and **state which vertex is weakest**.

**Mapped Proficiency Items:**
- K: 1.5.2.1 – Diamond Model
- T: 1.5.2.2 – Apply the Diamond Model to an incident or set of indicators

---

## 1. Key Concepts

The **Diamond Model** (Caltagirone, Pendergast, Betz) organizes an intrusion as a **relationship** among four features. You use it to see **what you know and what you do not**. That is how it supports analysis and, later, attribution.

It is not ATT&CK (behavior IDs). It is not the Kill Chain (order of stages). It is not a finished actor profile (**3.11**).

| This lesson | Later / other |
|-------------|---------------|
| Four vertices + weakest | ATT&CK map — **1.5.1** |
| “Adversary unknown” is allowed | Attribution product — **3.1.7** / **3.11** |
| Organize indicators | Kill Chain stage — **1.5.3** |

### 1.1 Purpose and the four vertices

**Purpose:** Force a complete picture so you do not treat one IP as the whole story.

| Vertex | Question | Typical contents |
|--------|----------|------------------|
| **Adversary** | Who is directing this? | Named group **only if evidence**; otherwise “unknown / unattributed” |
| **Capability** | What can they do / what tool or method? | Encoded PowerShell, a specific sid-matching URI, a service-key create |
| **Infrastructure** | What systems do they use? | `203.0.113.88`, `checkin.nightowl-updates.net`, sideloaded host |
| **Victim** | Who/what is being acted on? | `BUILDINGC\jlee`, `WS-JLEE`, finance mailbox, Building C |

Two meta-features exist in the original paper (social-political, technology). You may hear them. They are **not** a fifth and sixth vertex you must fill this hour.

**Attribution (outline c):** Diamond *supports* attribution by showing whether **Adversary** is actually populated. One IP in Infrastructure is not an actor name. Write **unknown** rather than invent a group.

### 1.2 Applying the model

1. List facts from the case under the four headings.
2. Empty is allowed — that vertex is **weak**.
3. Circle the **weakest** vertex (least evidence).
4. One sentence: what you would collect next to strengthen it (SOC: a log/PCAP; not a CTI paper).

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Victim + capability filled; adversary unknown | Adversary filled with a blog name from the dest IP alone |
| Weakest vertex named | All four “complete” because you guessed |
| Infra = domain/IP you actually saw | Infra = “the internet” |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Encoded PS + Beacon (Expected)

**Facts:** `jlee` / `WS-JLEE`; wscript → powershell `-enc`; POST `/api/v1/beacon` to `checkin.nightowl-updates.net` / `203.0.113.88`.

| Vertex | Fill |
|--------|------|
| Adversary | Unknown |
| Capability | Encoded PowerShell; HTTP POST beacon path |
| Infrastructure | `checkin.nightowl-updates.net`, `203.0.113.88` |
| Victim | `BUILDINGC\jlee`, `WS-JLEE` |

**Weakest:** **Adversary**.  
**Next (SOC-sized):** more infra/capability (other hosts, other URIs) — not “name the APT.”

### Example 2: IP-Only Over-Fill (Lead)

**Facts:** Only a SIEM dest IP `198.51.100.80:8080` (GET update.exe story) and no process.

| Vertex | Honest fill | Wrong fill |
|--------|-------------|------------|
| Adversary | Unknown | “Night Owl gang” |
| Capability | HTTP GET of `update.exe` (if PCAP/Zeek exists) | “Full RAT” |
| Infrastructure | `198.51.100.80:8080` | — |
| Victim | `10.10.22.17` (host IP only) | “Entire Building C” |

**Weakest:** **Adversary** and **Victim** (no user/host name) — pick **Victim** if you must name one (you can still enrich the host).  
**Lead:** Inventing an adversary from the IP.

### Example 3: Capability Strong, Infra Weak (Lead)

**Facts:** HKCU Run `Updater` = Temp `update.exe` (**1.1.4** Ex 2). No network row yet.

| Vertex | Fill |
|--------|------|
| Adversary | Unknown |
| Capability | Registry Run persistence; dropped `update.exe` |
| Infrastructure | Not observed on the wire (empty) |
| Victim | `jlee` / that user’s hive |

**Weakest:** **Infrastructure** (and Adversary).  
**Next:** host network / Zeek for that time (**1.1.3** / **1.2**) — still not an actor name.

---

## 3. Hands-On Exercise

**Objective:** Fill four vertices and name the weakest. Do not write an actor profile.

**Instructions:**

1. One sentence each for Examples 1–3: weakest vertex + why.
2. For each case, fill **A / C / I / V** (empty allowed) and **circle the weakest**.

   - A. GET `/payload/update.exe` on 8080; no process; PCAP has empty UA (**1.4.1** Ex 3).
   - B. Temp `helpdesk.exe` creates `HKLM\...\Services\HelpdeskSvc` as `jlee` (**1.1.4** Ex 3).
   - C. Inbox: `mailfrom` claims `jlee@buildingc.internal` from `203.0.113.88`, invoice subject (**1.2.6** Ex 2).

3. Do not assign ATT&CK IDs (**1.5.1**). Do not pick a Kill Chain stage (**1.5.3**).
4. Do not name a threat group unless the case already gave you one (none of these do).

**Expected Outcome:**
- Three weakest-vertex sentences
- Three four-vertex cards
- No actor profile, no ATT&CK stack

---

## 4. Knowledge Check

1. What is the Diamond Model *for*?
2. Name the four vertices and the question each answers.
3. Why is “unknown” an acceptable **Adversary** fill?
4. What does **weakest vertex** mean, and what do you do with it?
5. Why is a finished actor profile **not** this hour?

---

## 5. Summary

- Four vertices. Empty is honest. Weakest vertex drives the next look.
- One IP is Infrastructure, not Adversary.
- Next: Cyber Kill Chain (**1.5.3**).

---

## 6. References & Further Reading

- Diamond Model of Intrusion Analysis (Caltagirone, Pendergast, Betz)
- Related modules:
  - 1.5.1 – MITRE ATT&CK (previous)
  - 1.5.3 – Cyber Kill Chain (next)
  - 3.1.7 – Attribution
  - 3.11.1.2 – Threat actor profile
