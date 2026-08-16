# Module 3.8.2 – Extracting Applicable TTPs from Intelligence Reports

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.8.2 A / B / B · 3.8.2.1 1a / 2b / 3c  
- Hunter: 3.8.2 B / C / C · 3.8.2.1 3c / 4c / 4d  
- CTI: 3.8.2 B / C / C · 3.8.2.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Identify **relevant TTPs** in a report (behavior + enough *how* — the **3.7.1** gate).
2. Apply **Harbor criteria** to decide which of those TTPs **apply here**.
3. **Extract** only the IDs that pass **both** gates into the product.
4. **Reject** a TTP that is Unix/ESXi-only, or that is only a vendor footnote.

**Mapped Proficiency Items:**
- K: 3.8.2 – Extracting applicable TTPs from intelligence reports
- T: 3.8.2.1 – Extract applicable TTPs from an intelligence report

---

## 1. Key Concepts

**3.7.1** mapped a report onto **real T-IDs** and left uncited IDs out of *that* product. This hour asks a second question: of the TTPs that are actually *in the report*, **which ones apply to Harbor?**

Hunt-facing copy-the-PDF is **2.4.2**. Navigator coverage is **2.5**. Infra hops are **3.8.1**. IOC handling is **3.8.3**. “Does this matter to pay-db-01?” is **3.8.4**. Actor profile is **3.11**.

**Relevant in the report (outline a):** same evidence rule as **3.7.1**. A TTP is relevant if the report gives a *behavior* you can point at. A motive, a group name, or a footnote “they sometimes encrypt” is not enough. Do **not** invent T-IDs.

**Applicable here (outline b) — classroom criteria (Harbor card, lesson-only):**

| Criterion | Question | Harbor stand-in (**1.8.1**) |
|-----------|----------|-----------------------------|
| **Platform** | Could this run on what we have? | User endpoints are **Windows** (`WS-JLEE`). No Unix fleet, no macOS, no ESXi on the card. |
| **Path** | Does the traffic/path exist? | HTTP egress via **`fw-edge-01`**. Users do **not** initiate to OT. |
| **Visibility** | Could we *see* it if it ran? | Sysmon/MDE + Zeek `http` (and `dns`). |

A TTP must pass **platform + path**. Visibility tells you whether Harbor can *detect* it; a gap is not “does not apply” — note the gap, still mark apply if platform+path are yes. Do not turn this into **3.8.4** impact.

**Two gates:**

| Gate | Pass | Fail |
|------|------|------|
| **1 Relevant** | Behavior + how in *this* report | Vendor dump / footnote / “APT” |
| **2 Applicable** | Harbor platform + path | Unix/ESXi/macOS-only; path we do not have |

**Classroom IDs (real; use these):**

| TTP | Gate 1 | Gate 2 | Extract? |
|-----|--------|--------|----------|
| **T1059.001** PowerShell | `powershell -enc` | Windows yes | **Yes** |
| **T1547.001** Run key | HKCU `Updater` | Windows yes | **Yes** |
| **T1071.001** / **T1105** HTTP GET payload | GET `update.exe` :8080 | HTTP egress + Zeek `http` | **Yes** |
| **T1059.004** Unix Shell | Vendor “Linux backdoor” | No Unix user fleet | **No** |
| **T1486** ESXi encrypt | Vendor “they encrypt ESXi” | No ESXi on the card | **No** |
| **T1071.004** DNS C2 | Footnote “other campaigns” — no how *here* | (Harbor has Zeek `dns`, but gate 1 failed) | **No** |

**Apply line:**  
`T-ID | in the report because | Harbor fact | apply? | reject`

**In the product:** `T1059.001, T1547.001, T1071.001, T1105` — not the vendor’s Unix/ESXi/footnote rows.

| This lesson | Other |
|-------------|-------|
| Report TTP → apply on Harbor? | Evidence-bound map only — **3.7.1** |
| Not hunt ID skim | **2.4.2** |
| Not Navigator coverage | **2.5** |
| Not “so what to pay-db-01” | **3.8.4** |
| Not an infra hop | **3.8.1** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Four Windows/HTTP IDs apply | T1059.004 because “they have a backdoor” |
| ESXi T1486 stays out | Whole vendor matrix because “we have computers” |
| DNS C2 footnote fails gate 1 | “Zeek has `dns` so T1071.004 applies” with no how |

---

## 2. Detailed Walkthrough / Examples

**Classroom report (Night Owl + vendor table):**

> Harbor excerpt: WS-JLEE launched `wscript` then `powershell -enc`. HKCU Run `Updater` → `%TEMP%\update.exe`. Zeek HTTP GET `update.exe` on 8080 to `nightowl-updates.net`.  
> Vendor PDF also lists T1059.004 (Linux backdoor), T1486 against ESXi, and a footnote “other campaigns use DNS C2 (T1071.004).”

### Example 1: Four Apply (Expected)

| T-ID | Harbor fact | Apply |
|------|-------------|-------|
| T1059.001 | Windows user endpoints | Yes |
| T1547.001 | Windows Run keys exist | Yes |
| T1071.001 / T1105 | HTTP egress; Zeek `http` | Yes |

**Product:** “Applicable to Harbor: T1059.001, T1547.001, T1071.001, T1105.”

### Example 2: Unix / ESXi as Applicable (Lead)

**Draft:** Extract T1059.004 and T1486 because the vendor listed them and “encryption would be bad.”

**Fail.** T1059.004 needs a Unix fleet. T1486 here is **ESXi** — not on the Harbor card. Badness is **3.8.4**, not applicability.  
**Lead:** Platform miss. (Windows T1486 with a *how* would be a different row — this report did not give that how.)

### Example 3: Footnote DNS C2 (Lead)

**Draft:** T1071.004 applies because Harbor has Zeek `dns`.

**Fail.** Gate 1 first. A footnote about *other* campaigns is not a TTP *in this report*. Visibility does not rescue an uncited ID.  
**Lead:** Same uncited rule as **3.7.1**, now with an applicability coat of paint.

---

## 3. Hands-On Exercise

**Objective:** Extract only Harbor-applicable TTPs. Reject platform misses and footnotes.

**Use only the classroom table. Real IDs only.**

**Instructions:**

1. One sentence each for Examples 1–3: apply vs fail.
2. **Extract** (task): write an **apply line** for each.

   - A. `powershell -enc` / T1059.001.  
   - B. HKCU Run `Updater` / T1547.001.  
   - C. HTTP GET `update.exe` / T1071.001 and T1105.  
   - D. Vendor T1059.004 Unix Shell.  
   - E. Vendor T1486 against ESXi.

3. Write the **product applicable-TTP line** for A–C only.
4. Do not pivot infra (**3.8.1**). Do not score DTF. Do not write **3.8.4** impact. Do not open Navigator (**2.5**). Do not invent IDs.
5. If they ask about T1071.004, treat it like Example 3 (no apply line required unless you add it — then **no**).

**Expected Outcome:**
- Three example summaries
- Five apply lines (D and E = no)
- One product ID list
- No hunt coverage, no impact paragraph

---

## 4. Knowledge Check

1. How is this hour **different** from **3.7.1**?
2. What are the **two gates** a TTP must pass?
3. Why does **T1059.004** fail on Harbor?
4. Why does **Zeek `dns`** not make T1071.004 applicable *here*?
5. Where do you judge **organizational impact** (pay-db-01 / Sev)?

---

## 5. Summary

- Relevant in the report, then applicable on Harbor. Both gates, or it stays out.
- Unix/ESXi/macOS-only TTPs fail platform. Footnotes fail gate 1.
- Next: **3.8.3** IOC handling and enrichment concepts.

---

## 6. References & Further Reading

- Related modules:
  - 3.8.1 – Infra pivot (previous)
  - 3.7.1 – ATT&CK for CTI (evidence-bound map)
  - 1.8.1 – Harbor orientation
  - 3.8.3 – IOC handling (next)
  - 3.8.4 – Relevance and organizational impact
- MITRE ATT&CK Enterprise (lookup only — do not invent cells)
- Harbor card in **1.8.1** (lesson-only facts)
