# Instructor Guide – Module 1.1.3 – Network Activity (Endpoint)

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.3.1 A / B / C · 1.1.3.2 2b / 3c / 4c · 1.1.3.3 2b / 3c / 4c  
- Hunter: 1.1.3.1 A / B / B · 1.1.3.2 1a / 2b / 3c · 1.1.3.3 1a / 2b / 3c  
- CTI: 1.1.3.1 A / A / A · 1.1.3.2 1a / 1a / 1a · 1.1.3.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read host-observed network telemetry (Sysmon 3 / 22 and MDE `DeviceNetworkEvents`), describe what occurred, and write a SIEM query for a specific host-network pattern.

**Key Teaching Points:**
- Endpoint network rows, not Zeek (**1.2**), not Sysmon install, not process/file create (**1.1.1** / **1.1.2**).
- The initiating process is why this lesson exists next to Zeek.
- Source/dest IP and port, protocol, direction; domain/URL only when logged.
- Sysmon 3 = connect. Sysmon 22 = DNS (if in the feed). MDE `DeviceNetworkEvents` carries both shapes when the tenant logs them.
- Stay out of registry / image-load (1.1.4–1.1.5), persistence how-to (2.6), and protocol deep-dive (1.2).

**Common Student Challenges:**
- Treating every outbound 443 as expected (initiator is the story).
- Calling Event 22 a connect, or Event 3 a DNS query.
- Writing `DeviceNetworkEvents` with no filter.
- Pasting a Zeek `conn` row and claiming they have the process.
- Asking how to enable Event 22 or deploy Sysmon.
- Opening JA3 / `ssl.log` / `uid` in this hour.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for Sysmon 3 / 22 vs MDE field names; “process lives here / protocol lives in 1.2”
- Optional: one sanitized Event 3 and Event 22 screenshot
- Answer key (this guide)

---

## Learning Objectives

1. Explain host-observed connect and DNS rows: source/dest IP and port, protocol, direction, domain/URL when logged, and initiating process.
2. Analyze a Sysmon or MDE endpoint network event and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* host-network pattern — not “all connections.”

**Mapped Items:**
- K: 1.1.3.1 – Network activity (endpoint) concepts
- T: 1.1.3.2 – Analyze an endpoint network event (Sysmon or MDE)
- T: 1.1.3.3 – Create a SIEM query to detect specific endpoint network activity

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Host vs Zeek; not install |
| What a host network event is   | 8 min    | Process is the point |
| Fields + how logged            | 16 min   | a–e on the board; 3 vs 22 |
| Walkthrough Examples           | 14 min   | Students describe first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~70 min** | Stretch Example 3 if they treat Zeek dns as this row |

---

## Detailed Teaching Notes

### 1. What a host network event is

**Talking Points:**
- SOC 3 is facts (A / 2b). Push field names and “what occurred” in one sentence.
- SOC 5/7: initiator + dest + direction story and a query a teammate can run (B/C, 3c/4c).
- Hunter secondary: A / B / B and 1a / 2b / 3c — recognize the row, not own the query bar.
- CTI: A / A / A and 1a / 1a / 1a — nomenclature only. Do not grade them as SOC 5.

**What to emphasize:**
- Empty hostname / URL / no Event 22 = say “not logged,” not “no DNS.”
- Do not install Sysmon in this hour. Do not teach how to enable 22.

**Questions to ask:**  
“Which process talked, and to where?”  
“Is this a connect or a DNS query?”

### 2. Fields and logging shape

**Talking Points:**
- Walk outline a–e once. e is the fence: protocol depth is 1.2.
- Dual-map Sysmon `DestinationIp`/`DestinationPort` ↔ MDE `RemoteIP`/`RemotePort`. Dual-map `Image` ↔ `InitiatingProcessFileName`.
- `Initiated=true` = this process started it. MDE `ConnectionSuccess` is a completed connect, not a DNS query.
- Event 22 is optional in the feed. Park “how do I turn it on.”

**What to emphasize:**
- No `uid` on these rows. Do not invent a Zeek pivot.
- Next activity types are later 1.1.x. Park them on the board.

**Question to ask:**  
“If I only give you dest `203.0.113.88:443`, do you have a story yet?”

### 3. Examples

Work through all three interactively. Students say connect/DNS and expected/lead before you read the interpretation.

**Extra point for Example 1:**  
Baseline. Chrome + outbound 443 + a name that fits.

**Extra point for Example 2:**  
Good dest port, bad initiator. Empty URL is a visibility note. Process create is a different row.

**Extra point for Example 3:**  
22 ≠ 3. Zeek `dns` does not name PowerShell. If 22 is missing, they still must describe a 3 / `DeviceNetworkEvents` row honestly.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow use of the Student Guide.
- Grade description + specific queries. Do not grade Sysmon config.
- Review as a group. Do not collect a grade.
- Park file, process-only, Zeek, registry, and 2.6 labs.

**What good answers look like:**

**Summaries:**
- Example 1: Connect; Chrome → `203.0.113.20:443` outbound; expected.
- Example 2: Connect; hidden encoded PowerShell → `203.0.113.88:443`; lead. URL not logged.
- Example 3: DNS; PowerShell queried `checkin.nightowl-updates.net`; lead. Not a connect.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Sysmon 3 Chrome → 443 | **Connect** | Event 3 |
| Sysmon 22 PowerShell query | **DNS query** | Event 22 |
| MDE ConnectionSuccess powershell -enc | **Connect** | MDE connect |
| DeviceProcessEvents ProcessCreated | **Not a host network event** | **1.1.1** |
| DeviceFileEvents Temp file | **Not a host network event** | **1.1.2** |
| Zeek `conn` to 443 | **Not a host network event** | **1.2** |

**Pseudo-queries (equivalent is fine):**

```
DeviceNetworkEvents
| where ActionType == "ConnectionSuccess"
| where RemotePort == 443
| where InitiatingProcessFileName in (
    "powershell.exe", "wscript.exe", "cscript.exe",
    "winword.exe", "excel.exe", "outlook.exe")
```

```
// Sysmon Event ID 22 shape
dns_query
| where Image endswith @"\powershell.exe"
    or Image endswith @"\wscript.exe"
    or Image endswith @"\cscript.exe"
| project QueryName, Image, QueryResults
```

Fail a query with no initiator/dest filter, a `DeviceProcessEvents`-only query, or a Zeek `conn` / `dns` query (`id.orig_h`, `query`, `uid`).

**Analysis card (example — Example 2):**  
Connect (`ConnectionSuccess`). Initiator: `powershell.exe -NoP -W Hidden -enc …`. Dest: `203.0.113.88:443` TCP. URL not logged. Lead because of initiator + command line. Not an incident by itself. The matching process create is a different row.

Fail the card if they only write “C2 on 443,” call Event 22 a connect, or add a Zeek `uid` pivot.

---

## Knowledge Check – Answer Key

1. **Event 3 vs 22? Missing 22?**  
   **Answer:** Event 3 is a network **connection** (IPs, ports, `Initiated`). Event 22 is a **DNS query** (`QueryName` / results) by a process. If 22 is not in the feed, write “DNS not logged on the endpoint” and use Event 3 / `DeviceNetworkEvents` plus whatever name fields exist.  
   **Explanation:** 22 is not a connect. Absence of 22 is visibility, not “no DNS.”

2. **Why initiating process vs Zeek?**  
   **Answer:** This row names **which process on the host** opened the socket or issued the query. Zeek (**1.2**) sees the wire and does not give you `Image` / `InitiatingProcess*`.  
   **Explanation:** That is the point of 1.1.3.

3. **`Initiated=true`? MDE direction?**  
   **Answer:** Sysmon `Initiated=true` = this process **started** the connection (outbound from the host). On MDE, `ConnectionSuccess` / outbound remote fields show a completed connect the process made; listen / inbound `ActionType` values are the other direction.  
   **Explanation:** Direction is a field, not a guess from port 443.

4. **Empty RemoteUrl / DestinationHostname?**  
   **Answer:** Write “name not logged.” Still use initiator, IPs, ports, protocol, and direction.  
   **Explanation:** Do not invent a domain.

5. **Zeek conn has no process?**  
   **Answer:** A Zeek `conn` row cannot name the process. Look at Sysmon 3 / MDE `DeviceNetworkEvents` on that host for the same time, dest IP, and port.  
   **Explanation:** Host vs sensor. Do not fake a process onto the Zeek row.

---

## Additional Instructor Resources

- Local expected browser / Office dest names if you have a list
- Escalation: process → 1.1.1; file → 1.1.2; Zeek → 1.2; persistence → 2.6
- Next recommended module: Registry activity (1.1.4)
