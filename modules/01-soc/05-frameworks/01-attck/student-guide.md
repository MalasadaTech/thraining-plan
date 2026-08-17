# Module 1.5.1 – MITRE ATT&CK

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C · 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C · 1.5.1.2 3c / 4c / 4c  
- CTI: 1.5.1.1 B / C / C · 1.5.1.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of ATT&CK and how the matrix is structured.
2. Distinguish **tactics** from **techniques** and **sub-techniques**.
3. Map an alert or observed activity to a tactic and a technique (or sub-technique) and **cite the evidence**.

**Mapped Proficiency Items:**
- K: 1.5.1.1 – MITRE ATT&CK
- T: 1.5.1.2 – Map an alert or observed activity to MITRE ATT&CK tactics/techniques

---

## 1. Key Concepts

**MITRE ATT&CK** is a knowledge base of adversary **behaviors** arranged as a matrix. You use it to label *what you saw*, not to decorate a ticket with a random ID.

This lesson is the **shared floor**: purpose, structure, and mapping an **alert or log story**. Hunt planning, Navigator coverage, and ranking hunts are **2.5**. Copying IDs out of a CTI PDF is **2.4.2**. A finished actor profile is **3.11**.

| This lesson | Later / other |
|-------------|---------------|
| Tactic + technique + cite | Hunt coverage / prioritization — **2.5** |
| Behavior label | Alert category (scan/user/root) — **1.4.4** |
| One activity → one primary map | Diamond vertices — **1.5.2**; Kill Chain stage — **1.5.3** |

Do not memorize every cell. You must know **what the columns and cells are** and be able to map a case you already investigated.

### 1.1 Purpose and structure

**Purpose:** Describe adversary behavior in a shared language so SOC, hunt, and CTI can point at the same thing.

**Structure (Enterprise matrix, classroom view):**

| Piece | What it is |
|-------|------------|
| **Matrix** | Tactics as columns, techniques (and sub-techniques) as cells |
| **Tactic** | *Why* — the adversary’s goal at that step (Execution, Persistence, Command and Control, …) |
| **Technique** | *How* — a named way to achieve that goal (`T1059` Command and Scripting Interpreter) |
| **Sub-technique** | A more specific how (`T1059.001` PowerShell, `T1059.005` Visual Basic) |

Enterprise tactics you will **see in this hour** (not a memorize-all list): Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact. Reconnaissance and Resource Development exist; they are often thin in SOC telemetry.

A map is **tactic + ID + name + evidence**. An ID without evidence is a slogan.

### 1.2 Mapping observed activity

1. What did the telemetry actually show (process, file, HTTP, registry)?
2. What **goal** does that step serve? That is the **tactic**.
3. What **named how** fits? That is the **technique / sub-technique**.
4. Cite one field (command line, URI, parent, hive).
5. If two IDs fit, pick the **primary** (what this row *is*) and say why the neighbor is weaker.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| `wscript` → `powershell -enc` → **Execution** `T1059.001` | Same row labeled **Command and Control** because “beacon later” |
| HTTP GET `/payload/update.exe` → **Ingress Tool Transfer** `T1105` | Same row labeled **Impact** |
| HKLM `Services\HelpdeskSvc` create → **Persistence** `T1543.003` | Labeled **Execution** because an `.exe` ran earlier (different row) |

You may attach a second ID if a second row supports it. Do not stack five IDs on one process-create.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Execution — Encoded PowerShell (Expected)

**Activity:** Alert / **1.4.1** Ex 1: `wscript.exe` + Temp `invoice.vbs` → `powershell.exe -enc …`, user Medium.

**Map:** **Execution** / **T1059.001** Command and Scripting Interpreter: PowerShell.  
**Evidence:** Child is PowerShell with `-enc`.  
**Neighbor you reject:** Command and Control — this *row* is a process create, not a C2 channel. (A later **1.1.4** / **1.2.5** connect can be mapped separately.)

### Example 2: Wrong Tactic (Lead)

**Activity:** Same encoded PowerShell row. Analyst writes **TA0011 Command and Control** / T1071 because the vbs name “looks like a beacon.”

**Why it is a lead:** The *observed* activity is script execution. C2 needs a network row (dest, URI, beacon).  
**Correct primary:** still **T1059.001**. Optional second map *if* you have the POST `/api/v1/beacon` (**1.2.5** Ex 2): **Command and Control** / **T1071.001** Web Protocols — cite `method` + `uri` + `user_agent`, not the process name alone.

### Example 3: Ingress Tool Transfer, Not Impact (Lead)

**Activity:** GET `/payload/update.exe` on 8080 (**1.2.5** Ex 3 / **1.4.1** Ex 3).

**Map:** **Command and Control** or **Lateral/Ingress** depending on matrix view — classroom primary: **Ingress Tool Transfer T1105** (bringing a tool onto the host).  
**Evidence:** HTTP GET of an `.exe`.  
**Reject:** **Impact** (T1486 etc.) — no encryption, wipe, or service stop is in this row.  
**Reject:** **Initial Access** unless you have the *first* foothold story; this GET can be post-access staging.

---

## 3. Hands-On Exercise

**Objective:** Map cases to tactic + technique and cite. Do not plan a hunt.

**Instructions:**

1. One sentence each for Examples 1–3: tactic, ID, evidence, rejected neighbor.
2. Map each case. Write **tactic**, **technique or sub-technique (ID + name)**, **cite**, **rejected neighbor**.

   - A. Sysmon 11 / **1.1.3** Ex 2: `wscript.exe` creates `Temp\update.exe`.
   - B. Sysmon 13: PowerShell sets HKCU `Run\Updater` = Temp `update.exe` (**1.1.5** Ex 2).
   - C. MDE: `powershell.exe -enc` as **SYSTEM** after a service start (**1.4.4** exercise B).
   - D. Zeek `http` POST `/api/v1/beacon` with PowerShell UA (**1.2.5** Ex 2).

3. Do not write a Navigator layer. Do not assign scan/user/root (**1.4.4**). Do not fill Diamond vertices (**1.5.2**).
4. One primary ID per case. A second ID is allowed only if you name a second row.

**Expected Outcome:**
- Three example summaries
- Four maps with cite + rejected neighbor
- No hunt plan, no Kill Chain stage

---

## 4. Knowledge Check

1. What is ATT&CK *for*, and what is a **matrix** in this lesson?
2. What is the difference between a **tactic** and a **technique** (and a **sub-technique**)?
3. What four parts belong in a map (tactic, ID/name, evidence, neighbor)?
4. Why is hunt coverage / Navigator **not** this hour?
5. Why is “it looks like C2” not enough to pick TA0011?

---

## 5. Summary

- ATT&CK = shared language for **behavior**: tactic (why) + technique (how).
- Map the **row you have**. Cite a field. Reject the neighbor tactic.
- Hunt planning is **2.5**. Next: Diamond Model (**1.5.2**).

---

## 6. References & Further Reading

- MITRE ATT&CK Enterprise matrix: https://attack.mitre.org/
- Related modules:
  - 1.4.4 – Common alert categorizations
  - 1.5.2 – Diamond Model (next)
  - 1.5.3 – Cyber Kill Chain
  - 2.4.2 – Extracting hunt leads (ATT&CK IDs in a report)
  - 2.5.1 – Using ATT&CK for hunt planning
