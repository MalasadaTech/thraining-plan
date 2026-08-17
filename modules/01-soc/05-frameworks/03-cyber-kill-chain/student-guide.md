# Module 1.5.3 – Cyber Kill Chain

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C · 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 B / C / C · 1.5.3.2 3c / 4c / 4c  
- CTI: 1.5.3.1 B / C / C · 1.5.3.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of the Cyber Kill Chain.
2. Name the **seven stages** in order.
3. Identify the stage of observed activity and say **why it is not the previous or next stage**.

**Mapped Proficiency Items:**
- K: 1.5.3.1 – Cyber Kill Chain
- T: 1.5.3.2 – Identify the Kill Chain stage of observed activity

---

## 1. Key Concepts

The **Cyber Kill Chain** (Hutchins, Cloppert, Amin / Lockheed Martin) is a **sequence** of stages in an intrusion. You use it to place **this activity** on a timeline of progression — what already happened, what might be next.

It is not ATT&CK (a matrix of behaviors). It is not Diamond (four vertices). It is not the **1.4.4** category list.

| This lesson | Other |
|-------------|-------|
| One stage + reject previous/next | ATT&CK tactic/technique — **1.5.1** |
| Order of an attack | Diamond know/don’t know — **1.5.2** |
| Progression | Hunt methodology — **2.2** |

### 1.1 Purpose and the seven stages

**Purpose:** Understand **where you are** in an intrusion so you can describe progression (and where you might still interrupt it). You are not writing a blocking architecture this hour.

| # | Stage | What it means | Often visible in SOC? |
|---|--------|---------------|------------------------|
| 1 | **Reconnaissance** | Research / probing the victim | Sometimes (scans) |
| 2 | **Weaponization** | Pairing exploit + payload *off* your network | **Rarely** — usually no log |
| 3 | **Delivery** | Getting the payload to the victim (mail, HTTP GET, link) | Often |
| 4 | **Exploitation** | Triggering the flaw / code exec start | Sometimes (crash, exploit kit) |
| 5 | **Installation** | Foothold on the host (drop + persist) | Often (file, Run key, service) |
| 6 | **Command and Control** | Channel back to attacker infrastructure | Often (beacon HTTP/TLS) |
| 7 | **Actions on Objectives** | Why they came (steal, encrypt, destroy) | Sometimes — do not assume |

**Weaponization** is the usual empty stage on a SOC desk. Write **not observed** — do not invent a builder VM.

### 1.2 Using it for progression

1. What did *this* telemetry show?
2. Which stage is that step?
3. Why not the **previous** stage? Why not the **next**?
4. One row = one primary stage. A later row can be the next stage.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| GET `update.exe` → **Delivery** (or Installation if already written + persisting) | Same GET labeled **Actions on Objectives** |
| Encoded PS create → **Exploitation** or **Installation** (code is running / foothold) | Labeled **C2** with no network row |
| Port sweep → **Reconnaissance** | Labeled **Actions on Objectives** |
| POST `/api/v1/beacon` → **Command and Control** | Labeled **Delivery** |

Do not force every alert into Actions on Objectives because “they must want something.”

---

## 2. Detailed Walkthrough / Examples

### Example 1: Delivery, Not Installation (Expected)

**Activity:** GET `/payload/update.exe` on 8080. File may not yet be confirmed on disk in the alert.

**Stage:** **Delivery** — the payload is being brought to the host.  
**Not Exploitation:** You have no exploit-trigger row.  
**Not Installation:** You have not shown a persist or a confirmed foothold file+autorun. (If **1.1.3** also shows `Temp\update.exe` created, you may say Delivery *and* a *second* row is Installation.)

### Example 2: Installation, Not C2 (Lead)

**Activity:** PowerShell sets HKCU `Run\Updater` = Temp `update.exe`. No connect in this row.

**Stage:** **Installation** — persist on the host.  
**Not C2:** No channel.  
**Not Delivery:** The file is already there; this row is the autorun.

### Example 3: Reconnaissance, Not Actions (Lead)

**Activity:** 150-port SYN sweep, no auth (**1.4.4** Ex 1).

**Stage:** **Reconnaissance**.  
**Not Weaponization:** You did not see them build a payload (and you usually will not).  
**Not Actions on Objectives:** A sweep is not the objective itself.

**Nearby C2:** POST `/api/v1/beacon` → **Command and Control**, not Delivery (the beacon is the channel, not the first drop).

---

## 3. Hands-On Exercise

**Objective:** Name the stage and reject previous or next.

**Instructions:**

1. One sentence each for Examples 1–3: stage + rejected neighbor.
2. For each case, write **stage**, **not previous because**, **not next because**.

   - A. `wscript` → `powershell -enc` (process create only).
   - B. SMTP invoice from internet orig with `mailfrom` spoof (**1.2.6** Ex 2) — no attachment extract yet.
   - C. POST `/api/v1/beacon` + PowerShell UA.
   - D. 40× 401 on one mailbox login (**1.4.4** Ex 3).

3. Do not write ATT&CK IDs. Do not fill Diamond vertices.
4. If the stage is not in the telemetry (Weaponization), write **not observed**.

**Expected Outcome:**
- Three example summaries
- Four stage + neighbor pairs
- No ATT&CK stack, no Diamond card

---

## 4. Knowledge Check

1. What is the Kill Chain *for*?
2. Name the seven stages in order.
3. Why is **Weaponization** often empty on a SOC desk?
4. Why must you reject the previous or next stage?
5. How is a Kill Chain **stage** different from an ATT&CK **tactic**?

---

## 5. Summary

- Seven stages in order. One row, one primary stage.
- Reject previous/next. Weaponization is often **not observed**.
- This closes unit **1.5**. Next unit: **1.6** Reporting.

---

## 6. References & Further Reading

- Intelligence-Driven Computer Network Defense (Hutchins, Cloppert, Amin)
- Related modules:
  - 1.4.4 – Common alert categorizations
  - 1.5.1 – MITRE ATT&CK
  - 1.5.2 – Diamond Model (previous)
  - 1.6.1 – Report types (next unit)
