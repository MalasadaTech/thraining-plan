# Module 0.7 – External tools

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
- Hunter: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- CTI: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- DE: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
**Estimated Time:** 20 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say the purpose, one strength, and one weakness of VirusTotal, AnyRun, Silent Push, and URLScan.
2. Pick the first external tool for a need and say why the neighbor is wrong.

**Mapped Proficiency Items:**
- K: 0.7 – External tools (VirusTotal, AnyRun, Silent Push, URLScan)  
  SOC A / B / B · Hunter B / C / C · CTI B / C / C · DE A / B / B
- T: 0.7.1 – Select the appropriate external tool for a given enrichment or analysis need  
  SOC 1a / 2b / 3c · Hunter 3c / 4c / 4d · CTI 3c / 4c / 4d · DE 1a / 2b / 3c

---

## 1. Key Concepts

You will get a hash, a file, a domain, or a live URL. These four public tools each answer a different question. You pick the one that matches the need and you say why the neighbor is the wrong first tool. You do this so you do not detonate a file when you only needed history, or screenshot a page when you needed a hash reputation.

**Purpose, strength, weakness.**

| Tool | Purpose | Strength | Weakness |
|------|---------|----------|----------|
| **VirusTotal** | Multi-engine look-up of a file, URL, hash, or IP | Fast reputation | Public; not historical PDNS; not a full sandbox story |
| **AnyRun** | Detonate a **sample** and watch this run | Process tree and dropped files from *this* run | Needs a file; evadable; not infra history |
| **Silent Push** | Passive DNS / infra clustering | Historical resolutions and sibling domains | Not a detonation; not a page screenshot |
| **URLScan** | Scan a **URL / page now** | Redirects, screenshot, hosts from *this* load | Not PDNS history; not file behavior |

**When to pick.**

| Need | First external tool |
|------|---------------------|
| Hash or file reputation | **VirusTotal** |
| You have a binary and need behavior | **AnyRun** |
| Domain or IP *history* or cluster | **Silent Push** |
| Live URL / how the page looks now | **URLScan** |
| “Have we seen this internally?” | **Not these** — that is the internal TIP (**3.3.1**), later |

| This lesson | Other |
|-------------|-------|
| Purpose and when to pick | Live vendor account — not this hour |
| Select and reject the neighbor | Relations / multi-hop pivot — **3.9** |
| External tools only | Internal TIP — **3.3.1** |

**What good looks like (0.7.1):** you have a file hash and need vendor reputation. You pick **VirusTotal**. You reject AnyRun because you do not have a sample to detonate. You reject Silent Push because this is not a domain-history question.

Platform depth and a Relations graph are later (**3.9**). You do not need a live account this hour.

---

## 2. Knowledge Check

1. Give one purpose and one weakness of Silent Push.
2. When do you pick URLScan instead of Silent Push?
3. You have a hash and need reputation. Which tool, and why not AnyRun?

---

## 3. Summary

Four tools. Match the need. Reject the neighbor. Do not open the sandbox when the question is history, and do not treat a page scan as PDNS.

**Next:** **0.8** Environment / signal flow.

---

## 4. Related modules

- 0.6.3 – Cyber Kill Chain (previous)
- 0.8 – Environment / signal flow (next)
- 3.3.1 – Internal TIP (later)
- 3.9 – Platform depth (later)
