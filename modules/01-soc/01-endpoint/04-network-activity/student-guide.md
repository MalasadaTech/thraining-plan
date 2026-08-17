# Module 1.1.4 – Network Activity (Endpoint)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.4.1 A / B / C ; 1.1.4.2 2b / 3c / 4c ; 1.1.4.3 2b / 3c / 4c  
- Hunter: 1.1.4.1 A / B / B ; 1.1.4.2 1a / 2b / 3c ; 1.1.4.3 1a / 2b / 3c  
- CTI: 1.1.4.1 A / A / A ; 1.1.4.2 1a / 1a / 1a ; 1.1.4.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a host-network row: IP/port, protocol, direction, domain/URL when logged, and which process talked.
2. Describe what a Sysmon or MDE endpoint network event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.4.1 – Network activity (endpoint) concepts
- T: 1.1.4.2 – Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.4.3 – Create a SIEM query to detect specific endpoint network activity

---

## 1. Key Concepts

SOC analysts read **host** network rows to see **which process on this device** talked, and to where. **1.1.3** was the file row. This hour is the **host-network** row. It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Network activity (endpoint)** is host telemetry that a process **connected** (or tried to) or issued a **DNS query** (when that is logged here). The point of this hour versus Zeek is the **initiating process**. Zeek sees the wire. This row sees **who on the host** opened the socket.

| Idea | What to read |
|------|----------------|
| **Source / dest IP and port, protocol, direction** | Sysmon `Source*` / `Destination*`, `Protocol`, `Initiated`. MDE `Local*` / `Remote*`, `Protocol`. `Initiated=true` = this process started the connection. |
| **Domain / URL when logged** | Sysmon 3 `DestinationHostname`; Sysmon **22** `QueryName` if 22 is in the feed; MDE `RemoteUrl`. Empty ≠ “no DNS happened.” |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*`. **Who talked.** A Zeek `conn` row will not give you this field. |

**How this shows up:** Sysmon **3** (connect) and **22** (DNS, if logged here); MDE `DeviceNetworkEvents`. Same story, different names. This is **host-observed** activity. Protocol deep-dive is **1.2**.

MDE `ActionType` values you will use on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **ConnectionSuccess** | This process completed a connection | Event **3** (`Initiated` tells direction) |
| DNS on the endpoint | A query name, **if** your feed logs it here | Event **22** |

The full `ActionType` set is in the Defender portal schema. Do not invent a value. If Event **22** is not in the Sysmon feed, write “DNS not logged on the endpoint,” not “no DNS happened.”

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — which process talked, to which IP/port (or which name), which direction. Do not jump to a process create (**1.1.2**), a file drop (**1.1.3**), or a Zeek `conn` / `dns` field (**1.2**).
- Given: MDE `ConnectionSuccess`, `powershell.exe -enc …` → `203.0.113.88:443`, `RemoteUrl` empty. **What occurred:** hidden encoded PowerShell successfully connected outbound TCP/443 to that IP. URL not logged. The process create is a different row.
- Query: names a **specific** pattern (initiator + dest port or remote IP), not “all connections.”

Registry and image-load rows are the next **1.1** lessons.

---

## 2. Knowledge Check

1. A Zeek `conn` row names the initiating process. True or false?
2. `powershell.exe -enc …` has `ConnectionSuccess` to `203.0.113.88:443` and no `RemoteUrl`. In one sentence, what occurred?
3. A SIEM query that matches every `DeviceNetworkEvents` row is a good “specific endpoint network” query. True or false?

---

## 3. Summary

A host-network row is which process talked, to where. Direction and initiator tell the story. A missing name is a gap. Zeek does not name the process. A query names a specific pattern.

**Next:** **1.1.5** Registry activity.

---

## 4. Related modules

- 1.1.3 – File system activity (previous)
- 1.1.5 – Registry activity
- 1.1.2 – Process activity
- 1.2 – Zeek
