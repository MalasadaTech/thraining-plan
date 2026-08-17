# Module 3.4.2 – Extracting Hunt Leads from CTI

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.2 B / C / C ; 3.4.2.1–3.4.2.3 3c / 4c / 4d  
- SOC: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
- CTI: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Pull hunt-suitable **TTPs** and **artifacts** from a report that already passed the gate.
2. Drop what you cannot search, then state the **hunt question** the leftovers support.

**Mapped Proficiency Items:**
- K: 3.4.2 – Extracting hunt leads from CTI
- T: 3.4.2.1 – Extract hunt-suitable TTPs from a CTI report
- T: 3.4.2.2 – Extract hunt-suitable artifacts (IOCs, patterns, behaviors)
- T: 3.4.2.3 – State the hunt question those leads support

---

## 1. Key Concepts

You extract **after** the **3.4.1** gate. If the report is awareness-only or a full hand-off, stop. Mixed reports: extract only the hunt-worthy slice. Full card format is **3.2.2**. Mapping coverage is **3.5**. This hour is **keep / drop / question**.

| Kind | What it is | Keep when |
|------|------------|-----------|
| **TTP** | How they work — a method you can search | Specific enough, and you have telemetry |
| **IOC** | A named object — hash, host, IP, URL | Current, rare enough, queryable here |
| **Behavior** | A pattern over time | Off-baseline or scoped, not daily admin |

**Drop:** no telemetry (name the **visibility gap**), expired IOCs, noise (whole `/24`, slogan TTP, already-blocked firehose).

Record ATT&CK IDs **if the report already has them**. Do not invent IDs. Do not open Navigator (**3.5**).

**What good looks like (A12 slice):**

- **Keep TTP:** HKCU Run **`Updater`** → `%TEMP%\update.exe`.
- **Keep artifacts:** `GET /update.exe` to `203.0.113.88:8080`; more `invoice.vbs`.
- **Drop:** “they use persistence”; a 2019 hash with no reuse note; the vendor `/24`.
- **Question:** If more A12 persistors exist, we see Run **`Updater`**, `update.exe`, or another `invoice.vbs`.

If leftovers cannot form a question that can fail, you extracted noise.

---

## 2. Knowledge Check

1. Copying the IOC appendix is extract. True or false?
2. Name one reason to **drop** an object.
3. From the A12 slice, name one keep TTP, one keep artifact, and the hunt question.

---

## 3. Summary

Keep searchable TTPs and artifacts. Drop noise. One question that can fail.

**Next:** **3.4.3** STIX as hunt input.

---

## 4. Related modules

- 3.4.1 – Gate (previous)
- 3.4.3 – STIX input
- 3.2.2 – Hunt card
- 3.5.1 – ATT&CK map
