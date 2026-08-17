# Module 1.4.1 – Alert Context and Investigation

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.1.1 A / B / C · 1.4.1.2 2b / 3c / 4c · 1.4.1.3 2b / 3c / 4c · 1.4.1.4 2b / 3c / 4c · 1.4.1.5 2b / 3c / 4c · 1.4.1.6 2b / 3c / 4c  
- Hunter: 1.4.1.1 B / C / C · 1.4.1.2 2b / 3c / 4c · 1.4.1.3 2b / 3c / 4c · 1.4.1.4 2b / 3c / 4c · 1.4.1.5 2b / 3c / 4c · 1.4.1.6 2b / 3c / 4c  
- CTI: 1.4.1.1 A / A / B · 1.4.1.2 1a / 1a / 2b · 1.4.1.3 1a / 1a / 2b · 1.4.1.4 1a / 1a / 2b · 1.4.1.5 1a / 1a / 1a · 1.4.1.6 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Identify which **context** an alert already has and which it is missing.
2. Read the **alert configuration** and explain what would fire.
3. Trace **upstream hops** (for example Suricata → SIEM correlation → SIEM alert) and name each one.
4. Collect related **endpoint logs** and state what they add — or fail to add.
5. Collect related **PCAP** (when the alert is network-based) and state what it adds versus the alert fields.

**Mapped Proficiency Items:**
- K: 1.4.1.1 – Alert context and investigation
- T: 1.4.1.2 through 1.4.1.6 – the five investigation tasks

---

## 1. Key Concepts

An **alert** is a fired detection (SIEM analytics rule, Suricata sid, or similar) plus whatever **context** the platform attached. This lesson is **investigation of that object**. You do not write the rule (**1.3**). You do not classify TP/FP (**1.4.2**).

| This lesson | Later / other |
|-------------|---------------|
| What the alert already shows vs what you still need | TP / FP / TN / FN — **1.4.2** |
| What the **config** would fire | Authoring SIGMA / Suricata / SIEM — **1.3** |
| Name each hop in the chain | Alert categories / SLA clocks — **1.4.4** / **1.4.5** |

If a field is empty, say **missing**. Do not invent a command line, a parent, or a PCAP.

### 1.1 Context and configuration

**Context (outline a)** is what arrived *with* the alert: host, user, time, dest IP/port, snippet of command line, rule name, severity. Your job is a two-column list: **present** / **missing**. Missing is a visibility note, not “benign.”

**Configuration (outline b)** is the detection object behind the alert — the SIEM rule, SIGMA that was translated, or Suricata sid. Read it and say **what would fire**, in one sentence, using the same field language as **1.3**. You are not proposing a new rule.

| Present (usually) | Missing (often) |
|-------------------|-----------------|
| Device, account, rule name, time | Parent process, full command line, `uid` |
| Dest IP / port on a network alert | HTTP URI, User-Agent, process that opened the socket |
| “PowerShell created” | Whether `-enc` or `wscript` is in the payload |

### 1.2 Upstream hops, endpoint logs, PCAP

**Upstream (outline c)** is the chain that produced the row you are looking at. Name each hop. Classroom pattern:

`Suricata sid` → `SIEM correlation / analytics rule` → `SIEM alert`

Some alerts have one hop (SIEM-only). Say so. Do not invent a Suricata hop.

**Endpoint logs (outline d)** are **1.1** rows (Sysmon / MDE) for that host and window. After you pull them, write **what they add** or **fail to add**. “I opened DeviceProcessEvents” is not the task.

**PCAP (outline e)** is the packet capture for the flow that fired a **network** alert. Contrast it with the alert fields: method, URI, SNI, payload length. If the alert is process-only and no capture exists, write **PCAP not applicable** — do not pretend you opened one.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Context has host + user + the field the rule keys on | Context has dest IP only; URI and process missing |
| Config sentence matches the alert title | Title says “beacon”; config is `FileName == powershell.exe` |
| Hops you can name | “The SIEM did it” with no rule/sid |
| Endpoint logs add parent / command line | Endpoint logs fail to add a process for a 443 connect |
| PCAP confirms GET `/payload/update.exe` | Alert says “malware”; PCAP is TLS to a CDN with no URI |

---

## 2. Detailed Walkthrough / Examples

Classroom alerts reuse **1.1** / **1.2** / **1.3** stories. They are not automatic incidents.

### Example 1: Complete Process Alert (Expected investigation)

**Alert context:** Device `WS-JLEE`, account `BUILDINGC\jlee`, time `14:10`, rule `Encoded PowerShell from script host`, `FileName=powershell.exe`, command line contains `-enc`, parent `wscript.exe`.

**Configuration (would fire):** `DeviceProcessEvents` where powershell + `-enc` / `-EncodedCommand` + parent wscript/cscript (**1.3.1** Example 1 / **1.3.4** Example 1).

**Hops:** SIEM analytics rule → SIEM alert. No Suricata hop.

**Endpoint logs add:** Matching Sysmon 1 / MDE create; parent command line `invoice.vbs` under Temp. That is extra, not a new alert.

**PCAP:** Not applicable (process alert, no network object).

**What occurred (investigation only):** Context is complete for the rule. Config matches the title. One hop. Logs add the vbs path. Do not classify.

### Example 2: Thin Context, Broad Config (Lead)

**Alert context:** Device `WS-JLEE`, `FileName=powershell.exe`, rule title `Any PowerShell`. **Missing:** command line, parent, user (empty).

**Configuration (would fire):** process_creation where `Image` ends with `\powershell.exe` only (**1.3.1** Example 2).

**Hops:** SIEM analytics rule → SIEM alert.

**Endpoint logs add:** Parent `explorer.exe`, command line `powershell.exe Get-Help`. That **changes** the story the alert could not tell.

**PCAP:** Not applicable.

**Interpretation:** Lead *as an investigation*: name the missing fields, say the config would fire on every PowerShell, and state what the logs added. Do not spend this hour rewriting the SIGMA (**1.3**). Do not call FP (**1.4.2** / **1.4.3**).

### Example 3: Network Alert, Logs Fail, PCAP Adds (Lead)

**Alert context:** `10.10.22.17` → `198.51.100.80:8080`, rule `BUILDINGC TRAIN GET /payload/update.exe`, sid `1000001`. **Missing:** URI on the alert pane, process name.

**Configuration (would fire):** `alert http` HOME→EXT, `http.method` GET, `http.uri` `/payload/update.exe` (**1.3.2** Example 1).

**Hops:** Suricata sid `1000001` → SIEM correlation (sid present) → SIEM alert.

**Endpoint logs fail to add:** No `DeviceNetworkEvents` / Sysmon 3 for that dest in the window (visibility gap). You still have the alert.

**PCAP adds:** GET `/payload/update.exe` HTTP/1.1, empty User-Agent — the URI the alert pane lacked. Same session as **1.2.5** Example 3.

**Interpretation:** Lead. Three hops named. Logs failed to add a process. PCAP added the URI versus the alert’s IP:port only. Do not write YARA (**1.3.3**).

---

## 3. Hands-On Exercise

**Objective:** Practice the five investigation tasks. Do not classify. Do not author a rule.

**Instructions:**

1. One sentence per example: complete vs thin vs network; what you still needed.
2. For **Example 2** and **Example 3**, fill a five-line card:
   - Present context / missing context
   - What the configuration would fire
   - Upstream hops (name each)
   - What endpoint logs add **or** fail to add
   - What PCAP adds versus the alert, or **PCAP not applicable**
3. This short card is a **new** process alert. Do the same five lines:

> Context: `WS-FIN01`, user `finance`, rule `Office Spawns Cmd`, child `cmd.exe`. Missing: parent image. Config: Office parent → cmd/powershell (**1.3.1** exercise). Hops: SIEM only. Endpoint: parent `WINWORD.EXE`. No PCAP.

4. Do **not** write a SIGMA change or a TP/FP label.

**Expected Outcome:**
- Three short summaries
- Two full five-line cards (Ex 2, Ex 3)
- One five-line card for the Office/cmd alert
- No classification, no new rule

---

## 4. Knowledge Check

1. What is the difference between **alert context** and **alert configuration**?
2. What does “missing context” mean, and what do you write instead of inventing a field?
3. Give a three-hop upstream chain and a one-hop chain.
4. After you pull endpoint logs, what must your sentence contain besides “I queried them”?
5. When is PCAP **not applicable**, and when must you contrast it with the alert fields?

---

## 5. Summary

- Investigation = present vs missing, what the config would fire, named hops, what logs/PCAP add.
- Empty field → “missing.” No process row → “logs fail to add.” Process-only alert → “PCAP not applicable.”
- Do not author rules (**1.3**). Do not classify (**1.4.2**).
- Next: alert classification (**1.4.2**).

---

## 6. References & Further Reading

- Related modules:
  - 1.1.2 – Process activity
  - 1.1.4 – Network activity (endpoint)
  - 1.2.5 – HTTP engine
  - 1.3.1 – SIGMA rules
  - 1.3.2 – Suricata rules
  - 1.3.4 – SIEM rules
  - 1.4.2 – Alert classification (next)
- Local alert-console field guide used in class (optional)
