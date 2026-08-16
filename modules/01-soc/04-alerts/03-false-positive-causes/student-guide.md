# Module 1.4.3 – Common False Positive Causes

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.3.1 A / B / C · 1.4.3.2 2b / 3c / 4c  
- Hunter: 1.4.3.1 B / C / C · 1.4.3.2 2b / 3c / 4c  
- CTI: 1.4.3.1 A / A / B · 1.4.3.2 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two classroom **cause classes**: analyst/tool activity, and untuned or overly broad logic.
2. Given a case that is already an **FP**, identify the class **and** what you would change.

**Mapped Proficiency Items:**
- K: 1.4.3.1 – Common false positive causes
- T: 1.4.3.2 – Given a false positive, identify the cause class and what you would change

---

## 1. Key Concepts

This lesson starts **after** the label. **1.4.2** already called it an FP. You now pick a **cause class** and a **change**. You do not re-argue TP vs FP. You do not deploy the change (**1.3** / DE).

| Class (outline) | What it looks like | Change you can name |
|-----------------|--------------------|---------------------|
| **a. Analyst or tool activity** | Someone on the SOC/hunt/DE VLAN downloaded a rule already in prod; packet-broker **replay**; scanner the site owns | Exclude the lab/analyst range; schedule the test; tag the replay; allow-list the scanner *identity* |
| **b. Untuned or overly broad logic** | `Any PowerShell`; `content:"GET"` on any TCP; MZ-only YARA that someone wired to an alert | Add a second selector; bind an HTTP buffer; add parent/`-enc`; raise a threshold |

Those are the two classes this syllabus signs off. Other real-world causes exist (bad intel, clock skew). If you see one, say **other — not a/b** and still name a change. Do not invent a third official class.

| This lesson | Other |
|-------------|-------|
| Cause class + a change | The FP *label* — **1.4.2** |
| Name the change | Write/deploy SIGMA/Suricata/SIEM — **1.3** |
| “Allow-list this host” as a sentence | Persistence / hunt how-to — **2.6** |

A change is one concrete sentence: “Add parent in (wscript, cscript) and `-enc`.” Not “tune it.”

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Replay/lab VLAN → class **a** + exclude that range | Calling a live user Get-Help “analyst activity” |
| Any-PowerShell → class **b** + add parent/cmdline | Class **b** with no change |
| Both could apply — pick the **primary** class and say why | Listing every possible cause |

---

## 2. Detailed Walkthrough / Examples

All three are **already FP**. Do not reclassify.

### Example 1: Analyst / Tool Activity (Expected)

**FP:** Alert `BUILDINGC TRAIN GET /payload/update.exe` during a 7-level lab. Traffic is a **replay** of yesterday’s PCAP on the packet broker (**1.4.2** case D).

**Class:** **a** — tool/analyst activity (authorized replay).  
**Change:** Tag or exclude the broker replay interface / lab window so production detections do not page. Do not delete sid `1000001`.

### Example 2: Over-Broad Logic (Lead)

**FP:** `Any PowerShell` on `Get-Help` from explorer (**1.4.2** Ex 2).

**Class:** **b** — overly broad logic (only `Image=powershell.exe`).  
**Change:** Propose the **1.3.1** Example 1 shape: require `-enc` **and** a script-host (or Office) parent. Hand it to DE. Do not publish.

### Example 3: Pick a Primary Class (Lead)

**FP:** SOC 3 downloaded the public SIGMA for “Office Spawns Cmd” that is **already deployed**, then opened a documented finance export (Word → cmd). Alert fired on the 3-level’s own test **and** the logic also matches the export.

**Class:** Primary **a** (analyst tested a live rule). Secondary note: the rule is also broad for a documented export — that part is **b**, but the *event you were handed* is the test.  
**Change:** Test in a lab tenant or with a suppression for the analyst account during the exercise. Separately, tell DE the export path may need a filter — that is a second ticket, not this row.

---

## 3. Hands-On Exercise

**Objective:** On given FPs, write **class (a or b)** and **one change**.

**Instructions:**

1. One sentence each for Examples 1–3: class + change.
2. For each FP below, write **a or b** (or “other — not a/b”) and **one change sentence**.

   - A. Sid `1000002` (`content:"GET"` on any TCP) fired on an internal software-update HTTP GET.
   - B. Night-shift hunter ran AnyRun **in the SOC**, downloaded the sample, and the already-deployed `update.exe` URI rule fired on *that* download.
   - C. MZ-only YARA (1.3.3 Ex 2) was attached to a SIEM rule; it fired on `notepad.exe` on a kiosk.
   - D. Scanner `10.10.8.90` (documented vuln-mgmt) tripped `Office Spawns Cmd` because the scanner spawned `cmd.exe` under a packed Office test file.

3. Do not change the label to TP. Do not write full YAML unless one line of a selector is the change.
4. Do not assign scan/user/root categories (**1.4.4**).

**Expected Outcome:**
- Three example summaries
- Four class + change pairs
- No reclassification, no deploy

---

## 4. Knowledge Check

1. What are the two syllabus **cause classes**?
2. Why is this lesson not “classify TP vs FP” again?
3. What makes a **change** sentence acceptable?
4. When would you say **other — not a/b**?
5. Who deploys the change?

---

## 5. Summary

- After FP: **class + change**.
- **a** = analyst/tool activity. **b** = untuned / too broad.
- Name the change; DE deploys (**1.3**). Next: categories (**1.4.4**).

---

## 6. References & Further Reading

- Related modules:
  - 1.3.1 – SIGMA rules
  - 1.4.2 – Alert classification (previous)
  - 1.4.4 – Common alert categorizations (next)
