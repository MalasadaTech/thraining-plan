# Module 3.7.1 – MITRE ATT&CK for CTI Analysis and Reporting

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.7.1 A / B / B · 3.7.1.1 2b / 3c / 4c  
- Hunter: 3.7.1 B / C / C · 3.7.1.1 3c / 4c / 4c  
- CTI: 3.7.1 B / C / C · 3.7.1.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use ATT&CK for **intelligence analysis and reporting** — not as ticket decoration.
2. **Extract TTPs** from a report or multi-event story onto **tactic + technique (or sub-technique) IDs**.
3. **Cite the evidence span** and **reject the neighbor ID**.
4. Put those IDs in a product as **supported mappings**, not a 14-column dump.

**Mapped Proficiency Items:**
- K: 3.7.1 – MITRE ATT&CK for CTI analysis and reporting
- T: 3.7.1.1 – Map activity or reports to MITRE ATT&CK

---

## 1. Key Concepts

**1.5.1** is the floor: purpose, tactic vs technique, map an **alert**. This hour is **advanced CTI use**: a *report or activity set*, real **T-IDs**, evidence, neighbor reject, and what belongs in the **intel product**.

Hunt coverage / Navigator is **2.5**. Skimming a PDF to copy IDs for a hunt card is **2.4.2**. Which extracted TTPs *apply here* is **3.8.2**. Diamond / Kill Chain / DTF are **3.7.2–3.7.4**. A finished actor profile is **3.11**.

**Advanced application (outline a):**

| Move | What you do |
|------|-------------|
| **Extract** | Pull a *behavior*, not a group name or an IOC |
| **Map** | Tactic + technique or sub-technique + **real** ID |
| **Cite** | The sentence or log line that earns that ID |
| **Reject** | The adjacent technique (e.g. T1059.001 vs T1059.003) |
| **Report** | List only supported IDs next to the judgment |

Do **not** invent T-IDs. If you cannot find the cell, write the behavior and leave the ID blank — do not mint `T9999`.

**Classroom IDs (use these; they are real):**

| Behavior | Tactic | ID | Neighbor to reject |
|----------|--------|-----|--------------------|
| `powershell -enc` | Execution | **T1059.001** | T1059.003 (Windows Command Shell) |
| HKCU Run key → payload | Persistence | **T1547.001** | T1547.009 (shortcut) / startup folder |
| GET `/update.exe` over HTTP | C2 or Ingress | **T1071.001** / **T1105** | T1071.004 (DNS) if the evidence is HTTP |
| “Nation-state APT” with no behavior | — | **None** | Any tactic |

**Map line:**  
`evidence span | tactic | T-ID | name | rejected neighbor | why`

**In the product:** one short ATT&CK line under the judgment — `T1059.001, T1547.001` — not the whole Enterprise matrix.

| This lesson | Other |
|-------------|-------|
| Report / multi-event story → IDs | Single alert map — **1.5.1** |
| Not hunt coverage | **2.5** |
| Not “does this TTP apply on Harbor?” | **3.8.2** |
| Not Diamond vertices | **3.7.2** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Encoded PS → T1059.001, reject .003 | Mapping “APT” to Impact |
| Run key → T1547.001 with the key path cited | Pasting a vendor’s 20 IDs with no local evidence |
| HTTP GET payload → T1105 and/or T1071.001 | Inventing a T-code |

---

## 2. Detailed Walkthrough / Examples

**Classroom report excerpt (Night Owl):**

> WS-JLEE launched `wscript` then `powershell -enc`. A HKCU Run value `Updater` points at `%TEMP%\update.exe`. Zeek shows HTTP GET `update.exe` on 8080 to `nightowl-updates.net`. Vendor PDF also lists T1486 (ransomware encryption). No encryption was observed here.

### Example 1: Three Supported Maps (Expected)

| Evidence | Tactic | ID | Reject |
|----------|--------|-----|--------|
| `powershell -enc` | Execution | **T1059.001** | T1059.003 — no `cmd.exe` |
| Run `Updater` → Temp `update.exe` | Persistence | **T1547.001** | Startup folder — this is a Run key |
| HTTP GET `update.exe` :8080 | Command and Control / Ingress | **T1071.001** and **T1105** | T1071.004 — this is HTTP, not DNS |

**In the product:** “Observed T1059.001, T1547.001, T1071.001, T1105 (evidence in excerpt).”

### Example 2: Group Name as a Tactic (Lead)

**Draft:** “Financially motivated APT → TA0040 Impact.”

**Fail.** A motive or a vendor name is not a behavior. Impact needs evidence of *impact* (wipe, encrypt, deface).  
**Lead:** No T-ID until there is a *how*.

### Example 3: Vendor ID Dump (Lead)

**Draft:** Copy T1486 from the vendor PDF into the Harbor product.

**Fail.** T1486 is in the *source* report. It is **not** in the Harbor excerpt. Uncited IDs do not go in *this* product. (Whether ransomware TTPs *could* apply later is **3.8.2**.)  
**Lead:** Advanced mapping is **evidence-bound**, not copy-paste.

---

## 3. Hands-On Exercise

**Objective:** Map the excerpt and reject uncited / neighbor IDs.

**Use only real IDs. Classroom table above is enough.**

**Instructions:**

1. One sentence each for Examples 1–3: supported vs fail.
2. **Map** (task): write a **map line** for each.

   - A. `powershell -enc` on WS-JLEE.  
   - B. HKCU Run `Updater`.  
   - C. HTTP GET `update.exe` on 8080.  
   - D. Vendor line “they sometimes use DNS C2” — not seen here.  
   - E. “Night Owl is an APT” as the only sentence.

3. Write the **product ATT&CK line** for A–C only (comma-separated IDs).
4. Do not open Navigator. Do not fill Diamond. Do not invent IDs. Do not decide Harbor *applicability* (**3.8.2**).
5. If two IDs both fit C (T1071.001 and T1105), keep **both** and say why.

**Expected Outcome:**
- Three example summaries
- Five map lines (D and E = no ID)
- One product ID list
- No hunt coverage, no DTF

---

## 4. Knowledge Check

1. How is this hour **advanced** compared with **1.5.1**?
2. What must a **map line** include besides the T-ID?
3. Why is a vendor T1486 not automatically in *your* product?
4. Why can you not map “APT” to a tactic?
5. Where do you decide which mapped TTPs **apply to Harbor**?

---

## 5. Summary

- Extract behavior → real ID → cite → reject neighbor → list only those IDs in the product.
- Next: **3.7.2** Diamond Model in CTI.

---

## 6. References & Further Reading

- Related modules:
  - 3.6.1 – Advanced DNS (previous)
  - 1.5.1 – ATT&CK floor (alert mapping)
  - 2.5.1 – ATT&CK for hunt planning
  - 3.7.2 – Diamond Model in CTI (next)
  - 3.8.2 – Applicable TTPs from reports
- MITRE ATT&CK Enterprise (lookup only — do not invent cells)
- `modules/00-intro/06-frameworks/` (reference; do not copy here)
