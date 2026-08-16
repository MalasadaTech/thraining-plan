# Module 1.1.3 – Network Activity (Endpoint)

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.3.1 A / B / C · 1.1.3.2 2b / 3c / 4c · 1.1.3.3 2b / 3c / 4c  
- Hunter: 1.1.3.1 A / B / B · 1.1.3.2 1a / 2b / 3c · 1.1.3.3 1a / 2b / 3c  
- CTI: 1.1.3.1 A / A / A · 1.1.3.2 1a / 1a / 1a · 1.1.3.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain host-observed connect and DNS rows: source/dest IP and port, protocol, direction, domain/URL when logged, and initiating process.
2. Analyze a Sysmon or MDE endpoint network event and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* host-network pattern — not “all connections.”

**Mapped Proficiency Items:**
- K: 1.1.3.1 – Network activity (endpoint) concepts
- T: 1.1.3.2 – Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.3.3 – Create a SIEM query to detect specific endpoint network activity

---

## 1. Key Concepts

### 1.1 What an endpoint network event is

**Network activity (endpoint)** is host telemetry that a **process on this device** connected (or tried to) or issued a **DNS query** (when that is logged here).

This unit is **endpoint** telemetry (Sysmon / Microsoft Defender for Endpoint). It is **not** Zeek (**1.2**). It is **not** how to install or configure Sysmon. Process create is **1.1.1**. File create is **1.1.2**. Those are different rows.

| This lesson | Later |
|-------------|-------|
| Which process talked to which IP/port (or queried which name) | Protocol fields, `uid`, JA3, TLS/HTTP bodies (**1.2**) |
| Fields on the host network event | Registry (**1.1.4**), image load (**1.1.5**) |
| Sysmon Event IDs and MDE table names as they appear in a SIEM | Sysmon XML / deployment |

**Most critical distinction for daily work:**  
The point of **1.1.3** vs **1.2** is the **initiating process**. Zeek sees the wire. This row sees **who on the host** opened the socket or asked DNS.

If a field is empty in your tenant (no hostname, no URL, no Event 22), say so. Do not invent it.

### 1.2 Addresses, names, initiator, and how it is logged

| Idea | What to read | Why it matters |
|------|----------------|----------------|
| **Source / dest IP and port** | Sysmon `SourceIp` / `SourcePort`, `DestinationIp` / `DestinationPort`; MDE `LocalIP` / `LocalPort`, `RemoteIP` / `RemotePort` | Who talked to whom, on which port. Remote 443 is common; remote 4444 is a different story. |
| **Protocol** | `Protocol` (`tcp` / `udp`) | TCP vs UDP. Not a Zeek `service` guess. |
| **Direction** | Sysmon `Initiated`; MDE `ActionType` (`ConnectionSuccess` vs inbound / listen) | `Initiated=true` = this process started the connection (outbound from the host’s view). |
| **Domain / URL** | Sysmon 3 `DestinationHostname`; Sysmon **22** `QueryName`; MDE `RemoteUrl` **when logged** | A name is useful when present. Empty ≠ “no DNS happened.” |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*` | **Who** on this host. This is why the row exists next to Zeek. |

**How this shows up (outline d–e)**

| Source | Events / table | Key fields |
|--------|----------------|------------|
| Sysmon | **3** Network connection; **22** DNS query (if logged here) | `Image`, `Initiated`, `SourceIp`/`SourcePort`, `DestinationIp`/`DestinationPort`, `Protocol`, `DestinationHostname`; Event **22**: `QueryName`, `QueryStatus`, `QueryResults` |
| MDE | `DeviceNetworkEvents` | `ActionType`, `LocalIP`/`LocalPort`, `RemoteIP`/`RemotePort`, `Protocol`, `RemoteUrl`, `InitiatingProcess*` |

MDE network rows use **initiating** process = who opened the connection and **Remote\*** = the other side. Sysmon 3 uses `Image` / `Destination*`. Same story, different names.

This is **host-observed** activity. Protocol deep-dive — `conn` / `dns` / `ssl` fields, `uid` pivots, JA3 — is **1.2**. Do not treat a Sysmon 3 row as a Zeek `conn` log.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| `chrome.exe` / `msedge.exe` → `tcp/443`, `Initiated=true`, known dest | `powershell.exe` / `wscript.exe` / Office → `tcp/443` or a high port, especially with `-enc` / Temp script |
| Browser or Outlook `DestinationHostname` / `RemoteUrl` you recognize | No hostname **and** an unexpected initiator (say “name not logged”) |
| Event **22** from the browser for a site the user opened | Event **22** from `powershell.exe` / script host / Office for a name you cannot tie to that user |
| Inbound to a server role you expect (`Initiated=false` on a listener) | User workstation `Initiated=false` from the internet, or a listen you cannot explain |

**Source / dest / direction:** On a workstation, `Initiated=true` plus a remote `443` is the common outbound web path. Flip `Initiated` or the remote port and the story changes. Do not call it “C2” from port number alone.

**Domain / URL when logged:** Sysmon 3 may have `DestinationHostname`. Event **22** is the DNS query name *if your Sysmon feed includes 22*. MDE may have `RemoteUrl`. If none of those are present, describe IP + port + process and write “name not logged.”

**Initiating process:** On this row, `InitiatingProcess*` / `Image` is **who talked**. It is not a file create and not a process-create parent. A Zeek `conn` row will not give you this field.

Stay on the host network row. File drops are **1.1.2**. Registry Run keys are **1.1.4**. Zeek is **1.2**.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Browser → 443)

**Sysmon Event ID 3 (network connection)**

| Field | Value |
|-------|--------|
| Image | `C:\Program Files\Google\Chrome\Application\chrome.exe` |
| Initiated | `true` |
| Protocol | `tcp` |
| SourceIp / SourcePort | `10.20.30.41` / `51884` |
| DestinationIp / DestinationPort | `203.0.113.20` / `443` |
| DestinationHostname | `office-cdn.buildingc.internal` |
| User | `BUILDINGC\jlee` |

**What occurred:** Chrome on `jlee`’s workstation started an outbound TCP/443 connection to an internal office CDN name. Initiator, direction, and dest agree. Expected.

**Not done:** Did not call it an incident. Did not open a Zeek `ssl` lesson on the certificate (**1.2.4**). Did not rewrite this as a process-create card (**1.1.1**).

### Example 2: Encoded PowerShell → Outbound 443 (Lead)

**MDE `DeviceNetworkEvents` (`ConnectionSuccess`)**

| Field | Value |
|-------|--------|
| ActionType | `ConnectionSuccess` |
| InitiatingProcessFileName | `powershell.exe` |
| InitiatingProcessCommandLine | `powershell.exe -NoP -W Hidden -enc SQBFAFgA...` |
| InitiatingProcessFolderPath | `C:\Windows\System32\WindowsPowerShell\v1.0\` |
| LocalIP / LocalPort | `10.20.30.41` / `50912` |
| RemoteIP / RemotePort | `203.0.113.88` / `443` |
| Protocol | `Tcp` |
| RemoteUrl | *(empty)* |
| AccountName | `jlee` |

Compare a process row that is *not* this event:

> MDE `DeviceProcessEvents` `ProcessCreated`: `wscript.exe` → this `powershell.exe -enc …`. That is a **process create** (**1.1.1**). This row is the **connection**.

**What occurred:** Hidden, encoded PowerShell **successfully connected** outbound TCP/443 to `203.0.113.88`. No `RemoteUrl`. The process create is a different event.

**Interpretation:** Lead, not an automatic incident. Describe initiator + dest IP/port + direction. Write “URL not logged.” Do not pivot into Zeek JA3 (**1.2**). Do not write a persistence hunt (**2.6**).

### Example 3: PowerShell DNS Query (Lead)

**Sysmon Event ID 22 (DNS query)** — *if Event 22 is in this tenant’s Sysmon feed*

| Field | Value |
|-------|--------|
| Image | `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` |
| QueryName | `checkin.nightowl-updates.net` |
| QueryStatus | `0` |
| QueryResults | `203.0.113.88` |
| ProcessId | 8812 |
| User | `BUILDINGC\jlee` |

Compare a Zeek row that is *not* this event:

> Zeek `dns` query `checkin.nightowl-updates.net` with a `uid`. That is **1.2**. It does not name `powershell.exe`.

**What occurred:** `powershell.exe` **queried DNS** for `checkin.nightowl-updates.net` and got `203.0.113.88`. That is Event **22**, not Event **3**. If your feed has no 22, you will not see this row — write “DNS not logged on the endpoint.”

**Interpretation:** Lead. Name the query and the initiating process. Do not teach DGA methodology here. Do not treat the Zeek `dns` log as a substitute for the process field.

---

## 3. Hands-On Exercise

**Objective:** Practice describing host network events and writing queries that find a specific pattern.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (connect vs DNS; expected vs lead).
2. For each item below, say **connect**, **DNS query**, or **not a host network event**. Give one reason.
   - Sysmon 3: `chrome.exe` → `203.0.113.20:443`, `Initiated=true`
   - Sysmon 22: `powershell.exe` query `checkin.nightowl-updates.net`
   - MDE `DeviceNetworkEvents` `ConnectionSuccess`: `powershell.exe -enc` → `203.0.113.88:443`
   - MDE `DeviceProcessEvents` `ProcessCreated`: `wscript.exe` → `powershell.exe -enc ...`
   - MDE `DeviceFileEvents` `FileCreated` under Temp
   - Zeek `conn` row to 443
3. Write **two SIEM-style pseudo-queries**:
   - One for **script-host, Office, or PowerShell** making a **successful outbound** connection (use initiator + dest port or remote IP; require a connect `ActionType` or Sysmon 3 `Initiated=true`).
   - One for **DNS** where the initiating process is `powershell.exe`, `wscript.exe`, or `cscript.exe` (Sysmon 22 `QueryName` / Image, or the equivalent name field you have).
4. Write **one analysis card** (small table or four sentences) for Example 2 *or* Example 3: action (connect vs DNS), initiator, dest IP/port or query name, expected vs lead. Do not install Sysmon. Do not write a Zeek `conn` / `dns` query.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- Two specific host-network queries (not `DeviceNetworkEvents` with no filter)
- One card that describes *this* event, not a slogan

---

## 4. Knowledge Check

1. What is the difference between a Sysmon **3** row and a Sysmon **22** row? What do you write if 22 is not in the feed?
2. Why is **initiating process** the point of this lesson versus Zeek (**1.2**)?
3. What does Sysmon `Initiated=true` tell you? How do you read direction on MDE `DeviceNetworkEvents`?
4. `RemoteUrl` and `DestinationHostname` are empty. What do you write, and what do you still use?
5. A teammate pastes a Zeek `conn` row to `203.0.113.88:443` and asks which process did it. What is missing, and where do you look?

---

## 5. Summary

- Endpoint network activity = this **process** connected (or queried DNS) — on the **host**.
- Read source/dest IP and port, protocol, direction, domain/URL if present, and initiating process.
- Sysmon **3 / 22** and MDE `DeviceNetworkEvents` are the same story in different shapes. 22 is present only if logged.
- Event 3 is a connect. Event 22 is a DNS query. A Zeek `conn` / `dns` row is **1.2** and has no process.
- A missing name is a visibility note. An expected port (443) does not make an unexpected initiator “expected.”
- Next: registry activity (**1.1.4**). Zeek is **1.2**.

---

## 6. References & Further Reading

- Related modules:
  - 1.1.1 – Process activity
  - 1.1.2 – File system activity (previous)
  - 1.1.4 – Registry activity (next)
  - 1.1.5 – Image and driver load
  - 1.2.1 – Zeek concepts
  - 1.2.2 – Conn engine
  - 1.2.3 – DNS engine
- Local Sysmon / MDE field guide used in class (optional)
- Sysmon Event ID reference (3 / 22) and MDE `DeviceNetworkEvents` schema — as deployed, not as a config lesson
