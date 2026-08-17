# Module 3.9.2 – AnyRun

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.9.2 A / A / B · 3.9.2.1 1a / 1a / 2b  
- Hunter: 3.9.2 A / B / B · 3.9.2.1 2b / 3c / 4c  
- CTI: 3.9.2 B / C / C · 3.9.2.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. **Search** AnyRun by **tag, IP, domain, or hash**.
2. **Review** a submission and extract **actionable** intelligence.
3. **Reject** a tag-only hit and AnyRun’s ATT&CK labels without a matching event.
4. Leave SIEM/Zeek conversion and VT Behavior for their own hours.

**Mapped Proficiency Items:**
- K: 3.9.2 – AnyRun
- T: 3.9.2.1 – Search and review AnyRun submissions for actionable intelligence

---

## 1. Key Concepts

**3.3.2** taught *when* AnyRun is the tool (you have a **sample**). This hour is **search** and **review**. VT Behavior is sandbox events on a *hash in VT* (**3.9.1**). Hunt SIEM/Zeek is **2.3.1**. Applicable TTPs are **3.8.2**. Do not detonate live malware in class — use the cards.

**Search (outline a):**

| Query type | Classroom use | Trap |
|------------|---------------|------|
| **Hash** | `6734f374…` — exact sample | No hit ≠ “benign” |
| **Domain / IP** | `nightowl-updates.net` / `203.0.113.88` — runs that *talked* there | Other people’s malware that happened to beacon there |
| **Tag** | `nightowl` — only if the run’s events match | Tag `apt` is marketing |

**Review (outline b) — actionable vs not:**

| Actionable (take) | Not actionable (leave) |
|-------------------|------------------------|
| Process tree from *this* run | “Malicious” score alone |
| Dropped file hash / path | AnyRun MITRE tags with no matching event |
| C2 host / URI this run contacted | Unrelated public run that shares a popular tag |

**Classroom AnyRun cards (this lesson only):**

**Search `nightowl-updates.net`:** two public runs.

| Run | Hash | What the run shows |
|-----|------|--------------------|
| **R1** (keep) | `6734f374…` `update.exe` | `wscript` → `powershell -enc`; drop `%TEMP%\update.exe`; GET `update.exe` :8080 `nightowl-updates.net` |
| **R2** (reject) | `deadbeef…` | Tag `nightowl` only; process is a coin miner; no Harbor IOCs |

**Search tag `apt`:** dozens of unrelated runs. Do not pick the first one.

**Search line:** `query type | query | run kept | why that run`  
**Review line:** `process tree | dropped | C2 | what you will not take`

| This lesson | Other |
|-------------|-------|
| Search + review a *run* | When to pick AnyRun — **3.3.2** |
| Not VT Behavior tab | **3.9.1** |
| Not SIEM/Zeek query | **2.3.1** |
| Not applicable-TTP product | **3.8.2** |
| Need a file to *submit* | No file → not this tool (**3.3.2**) |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Domain search → keep R1 | Tag `apt` → first hit |
| Extract tree + drop + C2 | AnyRun T1486 tag as a TTP |
| Reject R2 | Score 100 = take everything |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Domain Search → R1 (Expected)

**Search:** domain `nightowl-updates.net`.  
**Keep:** R1 (`6734f374…`) — events match Harbor.  
**Extract:** process tree, dropped `update.exe`, C2 `nightowl-updates.net:8080`.  
**Product:** those three. Not the miner.

### Example 2: Tag `apt` (Lead)

**Draft:** Search tag `apt`, take the first Windows run as Night Owl.

**Fail.** A tag is not a shared property.  
**Lead:** Search by hash/domain/IP first. Tag is a *filter*, not a verdict.

### Example 3: AnyRun ATT&CK Tag (Lead)

**Draft:** R1 shows an AnyRun T1486 tag → extract ransomware as actionable intel.

**Fail.** R1’s events have no encrypt. Same uncited rule as **3.7.1** / **3.8.2**.  
**Lead:** Event first. Label second — or not at all.

---

## 3. Hands-On Exercise

**Objective:** Search, pick the run, extract only events.

**Use only the classroom cards.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Search** (task 1): write a **search line** for each.

   - A. Hash `6734f374…`.  
   - B. Domain `nightowl-updates.net`.  
   - C. Tag `apt`.  
   - D. IP `203.0.113.88` (treat like the domain card — R1 only).

3. **Review** (task 2): one **review line** for R1, and say why R2 is out.
4. Do not write a SIEM query. Do not open VT Relations. Do not submit a live file.
5. No file in the scenario means **no submit** — search public runs only.

**Expected Outcome:**
- Three example summaries
- Four search lines (C = no keep / too broad)
- One R1 review line + R2 reject
- No TTP product, no Zeek query

---

## 4. Knowledge Check

1. Name the **four** AnyRun search types in this hour.
2. What makes a submission **actionable**?
3. Why is tag `apt` a bad first query?
4. Why is an AnyRun **T1486** tag not automatically extracted?
5. When do you use **VT Behavior** instead of AnyRun?

---

## 5. Summary

- Search hash/domain/IP first. Keep the run whose *events* match. Extract those events.
- Next: **3.9.3** Silent Push.

---

## 6. References & Further Reading

- Related modules:
  - 3.9.1 – VT Relations / Behavior (previous)
  - 3.3.2 – When to open AnyRun
  - 3.9.3 – Silent Push (next)
- Classroom AnyRun cards in this guide (lesson-only)
