# Module 3.7.2 – Diamond Model Application in CTI

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.7.2 A / B / B · 3.7.2.1 1a / 2b / 3c  
- Hunter: 3.7.2 B / C / C · 3.7.2.1 3c / 4c / 4d  
- CTI: 3.7.2 B / C / C · 3.7.2.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use the Diamond Model on an **intelligence problem** — a report or activity set — not a single alert card.
2. **Fill four vertices** from evidence and **name the weakest**.
3. Let that weakest vertex **constrain the product claim** (especially Adversary).
4. **Reject** filling Adversary from a vendor name, and reject uncited Capability.

**Mapped Proficiency Items:**
- K: 3.7.2 – Diamond Model application in CTI
- T: 3.7.2.1 – Apply the Diamond Model to an intelligence problem

---

## 1. Key Concepts

**1.5.2** is the floor: purpose, four vertices, fill an **incident / indicator** card, name the weakest. This hour is **advanced CTI use**: a *report or activity set*, honest vertices, and what the **intel product** may (and may not) claim.

Attribution *confidence and types* are **3.1.7**. A finished actor profile is **3.11**. ATT&CK IDs are **3.7.1**. Kill Chain stages are **3.7.3**. DTF is **3.7.4**.

**Advanced application (outline a):**

| Move | What you do |
|------|-------------|
| **Fill** | Put *facts* under Adversary / Capability / Infrastructure / Victim |
| **Empty** | Leave a vertex blank if the excerpt does not earn it |
| **Weakest** | Circle the vertex with the least evidence |
| **Constrain** | That vertex limits what the *product* may say |
| **Reject** | Vendor group name ≠ Adversary; uncited tool/impact ≠ Capability |

Social-political and technology meta-features exist in the paper. They are **not** a fifth and sixth vertex you invent this hour, and they are not a **3.11** profile.

**Diamond line:**  
`Adversary | Capability | Infrastructure | Victim | weakest | what the product cannot claim`

**In the product:** one short Diamond sentence under the judgment — observed C / I / V; Adversary unattributed if that vertex is empty. Not a four-paragraph actor write-up.

| This lesson | Other |
|-------------|-------|
| Report / activity set → vertices + product constraint | Single incident card — **1.5.2** |
| Not ATT&CK IDs | **3.7.1** |
| Not Kill Chain stage | **3.7.3** |
| Not confidence letter / activity-group vs nation-state lecture | **3.1.7** |
| Not the finished profile | **3.11** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| C / I / V filled from Harbor excerpt; Adversary unknown | Vendor “Night Owl APT” in Adversary |
| Weakest = Adversary → product cannot name a group | All four “complete” because the PDF named someone |
| Capability = what *this* excerpt shows | Vendor T1486 as Capability |

---

## 2. Detailed Walkthrough / Examples

**Classroom report excerpt (Night Owl):**

> WS-JLEE launched `wscript` then `powershell -enc`. A HKCU Run value `Updater` points at `%TEMP%\update.exe`. Zeek shows HTTP GET `update.exe` on 8080 to `nightowl-updates.net` (`203.0.113.88`). Vendor PDF calls the cluster “Night Owl APT” (nation-state) and lists T1486. No encryption was observed here.

### Example 1: Honest Four-Vertex Card (Expected)

| Vertex | Fill |
|--------|------|
| Adversary | Unknown / unattributed |
| Capability | Encoded PowerShell; HKCU Run persistence; HTTP GET of `update.exe` |
| Infrastructure | `nightowl-updates.net`, `203.0.113.88:8080` |
| Victim | `BUILDINGC\jlee`, `WS-JLEE` |

**Weakest:** **Adversary**.  
**Product cannot claim:** a group name, a nation-state, or “Night Owl APT.”  
**Product may say:** capability and infrastructure observed against `jlee` / `WS-JLEE`.

### Example 2: Vendor Name as Adversary (Lead)

**Draft:** Adversary = Night Owl APT (nation-state), because the vendor PDF said so.

**Fail.** A marketing / cluster name is not evidence on *this* problem. Adversary stays empty until *this* activity set supports a who.  
**Lead:** Vendor label in the Adversary vertex. (Whether that label is even the right *type* of attribution is **3.1.7**. Writing the profile is **3.11**.)

### Example 3: Uncited Capability (Lead)

**Draft:** Capability = ransomware encryption (T1486), because the vendor listed it.

**Fail.** T1486 is in the *source* report. It is **not** in the Harbor excerpt. Uncited capability does not go on *this* diamond. (ATT&CK IDs themselves are **3.7.1**; the vertex error here is stuffing a tool you did not see.)  
**Lead:** Diamond is **evidence-bound**, same rule as the ATT&CK product line.

---

## 3. Hands-On Exercise

**Objective:** Apply Diamond to the excerpt. Reject vendor-name Adversary and uncited Capability.

**Instructions:**

1. One sentence each for Examples 1–3: honest vs fail.
2. **Apply** (task): write a **Diamond line** for each.

   - A. The Harbor excerpt (full story above).  
   - B. Vendor sentence only: “Night Owl is a nation-state APT.”  
   - C. Vendor line “they use ransomware (T1486)” — not seen here.  
   - D. Victim written as “all of Harbor / the finance sector” from `WS-JLEE` alone.  
   - E. “Write the Night Owl actor profile from this card.”

3. Write the **product Diamond sentence** for A only.
4. Do not assign ATT&CK IDs (**3.7.1**). Do not pick a Kill Chain stage (**3.7.3**). Do not write DTF PTA/P IDs (**3.7.4**). Do not assign a 3.1.7 confidence letter.
5. Empty vertices are allowed. Guessing is not.

**Expected Outcome:**
- Three example summaries
- Five Diamond lines (B, C, D, E fail or refuse)
- One product sentence for A
- No actor profile, no ATT&CK stack

---

## 4. Knowledge Check

1. How is this hour **advanced** compared with **1.5.2**?
2. What must a **Diamond line** include besides the four vertex fills?
3. Why does a vendor “APT” name not fill **Adversary**?
4. Why is vendor T1486 not **Capability** on this card?
5. Where do you write the finished actor profile?

---

## 5. Summary

- Fill vertices from *this* evidence. Empty is honest. Weakest vertex limits the product.
- Vendor name ≠ Adversary. Uncited tool ≠ Capability.
- Next: **3.7.3** Cyber Kill Chain in CTI.

---

## 6. References & Further Reading

- Related modules:
  - 3.7.1 – ATT&CK for CTI (previous)
  - 1.5.2 – Diamond floor (incident card)
  - 3.1.7 – Attribution confidence and types
  - 3.7.3 – Cyber Kill Chain in CTI (next)
  - 3.11 – Actor profile
- Diamond Model of Intrusion Analysis (Caltagirone, Pendergast, Betz)
- `modules/00-intro/06-frameworks/` (reference; do not copy here)
