# Module 3.9.1 – VirusTotal Relations and Behavior

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.9.1 A / B / B · 3.9.1.1 1a / 2b / 3c  
- Hunter: 3.9.1 B / C / C · 3.9.1.1 3c / 4c / 4d  
- CTI: 3.9.1 B / C / C · 3.9.1.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use the **Relations** tab to walk from a seed to **additional infrastructure**.
2. Use the **Behavior** tab to extract **file, network, registry, and process** events.
3. **Cite** the graph edge or behavior row — do not dump the whole graph.
4. **Reject** “related” nodes that share no property, and Detection-tab labels as a substitute for Behavior.

**Mapped Proficiency Items:**
- K: 3.9.1 – VirusTotal (Relations and Behavior tabs)
- T: 3.9.1.1 – Use VirusTotal Relations and Behavior to pivot and extract events

---

## 1. Key Concepts

**3.3.2** taught *when* to open VirusTotal (hash / reputation, one hop). This hour is **the two tabs**: Relations (infra) and Behavior (events). Hunt conversion to SIEM/Zeek is **2.3.1**. Conceptual hop without a vendor UI is **3.8.1**. imphash / ssdeep are **3.4**. Applicable TTPs are **3.8.2**. AnyRun is **3.9.2**.

**Relations (outline a):** a graph of *how VT linked objects* — contacted domains/IPs, communicating files, execution parents, bundled files. A node is not adversary infra until you can name the **edge**.

**Behavior (outline b):** sandbox *events* from *this* hash — process tree, dropped files, registry, network. It is not the Detection tab and not AnyRun (different sandbox, **3.9.2**).

**Classroom VT cards (this lesson only, not a live graph):**

**Seed file:** `update.exe` hash `6734f374…` (WS-JLEE Temp).

| Relations node | Edge | Take? |
|----------------|------|-------|
| `nightowl-updates.net` | **Contacted domain** | Yes — infra |
| `203.0.113.88` | **Contacted IP** | Yes — same infra |
| `login-nightowl.net` | **Contacted domain** | Yes — additional name |
| `88aa9911…` (`helpdesk.exe`) | **Communicating file** | File, not infra — note it; do not call it a domain |
| `invoice.vbs` | **Bundled / dropped** | File — Behavior, not Relations infra |
| `random-cdn.example` | “Related” / community tag only | **No** — no edge |

| Behavior row | Event |
|--------------|--------|
| Process | `wscript` → `powershell -enc` |
| File | Drop `%TEMP%\update.exe` |
| Registry | HKCU Run `Updater` → `%TEMP%\update.exe` |
| Network | HTTP GET `update.exe` :8080 `nightowl-updates.net` |

**Relations line:** `seed | edge | additional infra | why not a coincidence`  
**Behavior line:** `process | file | registry | network`

| This lesson | Other |
|-------------|-------|
| Walk the two tabs | Pick VT vs Silent Push — **3.3.2** |
| Graph edge → infra | Conceptual hop — **3.8.1** |
| Behavior *events* | AnyRun review — **3.9.2** |
| Not SIEM/Zeek query | **2.3.1** |
| Not applicable-TTP product | **3.8.2** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Contacted domain/IP as additional infra | Every “related” file is infra |
| Four Behavior event classes | Detection-tab T-IDs as Behavior |
| Stop after cited edges | 12-node dump |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Relations Hop (Expected)

**Seed:** `6734f374…`.  
**Edges:** contacted `nightowl-updates.net`, `login-nightowl.net`, `203.0.113.88`.  
**Additional infra:** those two names + the IP.  
**Reject:** `random-cdn.example` (no edge).  
**Product:** “VT Relations (contacted): `nightowl-updates.net`, `login-nightowl.net`, `203.0.113.88`.”

### Example 2: Related-File Dump (Lead)

**Draft:** `88aa9911…` / `helpdesk.exe` is additional *infrastructure*.

**Fail.** A communicating *file* is another sample. It may seed a *second* Relations walk or **3.4**. It is not a domain/IP.  
**Lead:** Edge type matters.

### Example 3: Detection Instead of Behavior (Lead)

**Draft:** Copy VT’s ATT&CK labels (including T1486) as the Behavior extract.

**Fail.** Behavior is the four event classes on the card. Labels without a process/file/reg/net row are **3.7.1** / **3.8.2**, and T1486 is still uncited.  
**Lead:** Tab name is not optional.

---

## 3. Hands-On Exercise

**Objective:** Walk Relations and extract Behavior. Reject unlabeled nodes and Detection-tab dumps.

**Use only the classroom cards.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Relations** (task 1): write a **Relations line** for each.

   - A. Contacted `nightowl-updates.net`.  
   - B. Contacted `login-nightowl.net`.  
   - C. Communicating file `88aa9911…`.  
   - D. Community “related” `random-cdn.example`.

3. **Behavior** (task 2): one **Behavior line** for `6734f374…` (all four classes).
4. Do not write a SIEM query (**2.3.1**). Do not write DTF PTA/P IDs (**3.7.4**). Do not open AnyRun (**3.9.2**). Do not extract applicable TTPs (**3.8.2**).
5. Empty hop is allowed. A 12-node paste is not.

**Expected Outcome:**
- Three example summaries
- Four Relations lines (C = file not infra; D = reject)
- One four-class Behavior line
- No SIEM query, no TTP product

---

## 4. Knowledge Check

1. What is the **Relations** tab *for*, versus **Behavior**?
2. What must a **Relations line** include besides the node name?
3. Why is a communicating **file** not additional infrastructure?
4. Why are Detection-tab T-IDs not a Behavior extract?
5. Where do you convert a contacted domain into a **Zeek/SIEM** query?

---

## 5. Summary

- Relations: cite the edge. Behavior: four event classes. Stop.
- Next: **3.9.2** AnyRun.

---

## 6. References & Further Reading

- Related modules:
  - 3.8.2 – Applicable TTPs (previous cluster)
  - 3.3.2 – When to open VT
  - 3.8.1 – Conceptual infra hop
  - 3.9.2 – AnyRun (next)
- Classroom VT cards in this guide (lesson-only)
