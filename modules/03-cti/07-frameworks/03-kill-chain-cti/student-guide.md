# Module 3.7.3 – Cyber Kill Chain in Intelligence Analysis

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.7.3 A / B / B · 3.7.3.1 2b / 3c / 4c  
- Hunter: 3.7.3 B / C / C · 3.7.3.1 3c / 4c / 4c  
- CTI: 3.7.3 B / C / C · 3.7.3.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use the Kill Chain on an **intelligence problem** — a report or activity set — not a single alert row.
2. **Identify the stage** of each evidence span and **reject previous / next**.
3. **Place the set** on the chain and list only **supported** stages in the product.
4. **Reject an unobserved stage** (Weaponization, Actions on Objectives) when the excerpt does not earn it.

**Mapped Proficiency Items:**
- K: 3.7.3 – Cyber Kill Chain in intelligence analysis
- T: 3.7.3.1 – Identify the Kill Chain stage of observed or reported activity

---

## 1. Key Concepts

**1.5.3** is the floor: purpose, seven stages, one **observed row**, reject previous/next. This hour is **advanced CTI use**: a *report or activity set*, several spans, and what the **intel product** may say about **progression**.

ATT&CK IDs are **3.7.1**. Diamond vertices are **3.7.2**. DTF is **3.7.4**. Alert categories (scan / user / root) are **1.4.4**. A finished actor profile is **3.11**.

**Advanced application (outline a):**

| Move | What you do |
|------|-------------|
| **Place** | Put each evidence span on **one** primary stage |
| **Reject** | Why not the previous stage? Why not the next? |
| **Stack** | A later span can be a later stage — do not collapse the set to one label |
| **Omit** | Weaponization / Actions on Objectives stay out if not in *this* excerpt |
| **Report** | List only supported stages, in chain order |

An ATT&CK tactic name is **not** a Kill Chain stage. A GET of `update.exe` can be **Delivery** on the chain and **T1105** / **T1071.001** on ATT&CK (**3.7.1**). Do not paste tactic IDs onto the chain.

**Classroom stages (same seven as 1.5.3):**

| # | Stage | This excerpt? |
|---|--------|----------------|
| 1 | Reconnaissance | Not in the Harbor story |
| 2 | Weaponization | **Not observed** (off-net; do not invent a builder) |
| 3 | Delivery | HTTP GET `update.exe` :8080 |
| 4 | Exploitation | `wscript` → `powershell -enc` |
| 5 | Installation | HKCU Run `Updater` → `%TEMP%\update.exe` |
| 6 | Command and Control | Not this GET (a beacon POST would be; this GET is the drop) |
| 7 | Actions on Objectives | Vendor T1486 / encrypt — **not observed** |

**Stage line:**  
`evidence span | stage | not previous because | not next because`

**In the product:** one short progression line — `Delivery, Exploitation, Installation` — not “they reached Actions on Objectives.”

| This lesson | Other |
|-------------|-------|
| Report / activity set → stages + product list | Single-row stage — **1.5.3** |
| Not ATT&CK IDs | **3.7.1** |
| Not Diamond vertices | **3.7.2** |
| Not 1.4.4 categories | scan / user / root |
| Not the finished profile | **3.11** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| GET → Delivery; PS-enc → Exploitation; Run → Installation | Whole story → Actions on Objectives |
| Weaponization = not observed | Inventing a builder VM because “they must have packed it” |
| Product lists only those three stages | Vendor T1486 as Actions on Objectives |

---

## 2. Detailed Walkthrough / Examples

**Classroom report excerpt (Night Owl):**

> WS-JLEE launched `wscript` then `powershell -enc`. A HKCU Run value `Updater` points at `%TEMP%\update.exe`. Zeek shows HTTP GET `update.exe` on 8080 to `nightowl-updates.net` (`203.0.113.88`). Vendor PDF also lists T1486 (ransomware encryption). No encryption was observed here.

### Example 1: Three Supported Stages (Expected)

| Evidence | Stage | Not previous | Not next |
|----------|-------|--------------|----------|
| GET `update.exe` :8080 | **Delivery** | Not Weaponization — you did not see them build it | Not Exploitation — no exploit-trigger row on this GET |
| `powershell -enc` | **Exploitation** | Not Delivery — this row is code running, not the drop | Not Installation — persist is the Run key, a second row |
| Run `Updater` → Temp `update.exe` | **Installation** | Not Exploitation — this row is the autorun | Not C2 — no channel on this row |

**In the product:** “Observed Delivery, Exploitation, Installation. Weaponization and Actions on Objectives not observed.”

### Example 2: Whole Story as Actions on Objectives (Lead)

**Draft:** “Night Owl reached Actions on Objectives (T1486).”

**Fail.** Actions on Objectives needs evidence of *the objective* (steal, encrypt, destroy). The vendor listed T1486. The Harbor excerpt did not.  
**Lead:** Do not collapse a multi-stage set to stage 7 because the PDF named ransomware. (ATT&CK IDs are **3.7.1**; the stage error here is the same uncited leap.)

### Example 3: Invented Weaponization (Lead)

**Draft:** “Weaponization: they built `invoice.vbs` / `update.exe` off-network.”

**Fail.** Weaponization is almost always empty on your desk. “They must have packed it” is not a stage you list in the product.  
**Lead:** **Not observed** is the honest fill. Same rule as an empty Diamond Adversary (**3.7.2**).

---

## 3. Hands-On Exercise

**Objective:** Place the excerpt on the chain. Reject unobserved stages.

**Instructions:**

1. One sentence each for Examples 1–3: supported vs fail.
2. **Identify** (task): write a **stage line** for each.

   - A. `powershell -enc` on WS-JLEE.  
   - B. HKCU Run `Updater`.  
   - C. HTTP GET `update.exe` on 8080.  
   - D. Vendor line “they encrypt with ransomware (T1486)” — not seen here.  
   - E. “They weaponized the VBS off-net” as the only sentence.

3. Write the **product stage list** for A–C only (chain order, comma-separated).
4. Do not assign ATT&CK IDs (**3.7.1**). Do not fill Diamond (**3.7.2**). Do not write DTF PTA/P IDs (**3.7.4**).
5. If a stage is not in the telemetry, write **not observed** — do not invent it.

**Expected Outcome:**
- Three example summaries
- Five stage lines (D and E = no stage / not observed)
- One product stage list
- No Diamond card, no actor profile

---

## 4. Knowledge Check

1. How is this hour **advanced** compared with **1.5.3**?
2. What must a **stage line** include besides the stage name?
3. Why is vendor T1486 not **Actions on Objectives** in *your* product?
4. Why is **Weaponization** usually **not observed**?
5. Why is an ATT&CK tactic **not** the same thing as a Kill Chain stage?

---

## 5. Summary

- Place each span. Reject previous/next. List only supported stages in the product.
- Unobserved stages stay out — including Weaponization and uncited Actions on Objectives.
- Next: **3.7.4** MalasadaTech Defender’s ThreatMesh Framework (DTF).

---

## 6. References & Further Reading

- Related modules:
  - 3.7.2 – Diamond Model in CTI (previous)
  - 1.5.3 – Kill Chain floor (single-row stage)
  - 3.7.1 – ATT&CK for CTI
  - 3.7.4 – DTF (next)
- Intelligence-Driven Computer Network Defense (Hutchins, Cloppert, Amin)
- `modules/00-intro/06-frameworks/` (reference; do not copy here)
