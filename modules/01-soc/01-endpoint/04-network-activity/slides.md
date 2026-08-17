# Module 1.1.4 – Network Activity (Endpoint)  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.1.4 – Network Activity (Endpoint)  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Host-observed connect and DNS. Sysmon 3 / 22 and MDE DeviceNetworkEvents. Not install. Not Zeek.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain source/dest IP and port, protocol, direction, domain/URL when logged, and initiating process
2. Analyze a Sysmon or MDE endpoint network event and describe what occurred
3. Write a SIEM query for *specific* host-network activity

**Mapped Items:**  
K: 1.1.4.1 | T: 1.1.4.2 | T: 1.1.4.3

**Speaker Notes:**  
SOC 3 is A / 2b. CTI is nomenclature only (A / 1a).

---

### Slide 3 – Agenda
**Title:** Agenda

- What a host network event is
- Fields (outline a–c)
- Sysmon 3 / 22 and DeviceNetworkEvents
- Host vs Zeek (outline e)
- Three worked examples
- Identification + two queries
- Knowledge check

**Speaker Notes:**  
1.2 is later. Stay on the host row.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Sysmon install / “turn on Event 22”  
Zeek `conn` / `dns` / `ssl` / `uid` / JA3 (**1.2**)  
Process create of `powershell.exe` (**1.1.2**)  
File create under Temp (**1.1.3**)  
“443 means browsing”

**Key Point:** Describe *this* host network row.

**Speaker Notes:**  
Park deploy and protocol-depth questions on the board.

---

### Slide 5 – Host vs Zeek
**Title:** Why This Lesson Exists

**1.1.4** — process on the endpoint → IP / port / name  
**1.2** — what the sensor saw on the wire

Same dest IP can appear in both. Only this row names `Image` / `InitiatingProcess*`.

**Analyst Tip:** Do not paste a process onto a Zeek `conn` row.

**Speaker Notes:**  
This is outline e. Repeat it if they drift.

---

### Slide 6 – IP, Port, Protocol, Direction
**Title:** Who Talked to Whom

**IPs / ports** — Sysmon Source* / Destination*; MDE Local* / Remote*  
**Protocol** — `tcp` / `udp`  
**Direction** — Sysmon `Initiated=true` means this process started it

**Key Point:** Port 443 is common. Initiator + direction are the story.

**Speaker Notes:**  
Map Destination* ↔ Remote* live.

---

### Slide 7 – Domain / URL When Logged
**Title:** A Name Is Optional

Sysmon **3** — `DestinationHostname` if present  
Sysmon **22** — `QueryName` (only if 22 is in the feed)  
MDE — `RemoteUrl` if present

Empty → write “name not logged.” Do not invent a domain.

**Speaker Notes:**  
Event 22 enablement is not this hour.

---

### Slide 8 – Initiating Process
**Title:** Who Opened the Socket

Sysmon: `Image`  
MDE: `InitiatingProcess*` = **who talked**

**Expected:** `chrome.exe` → 443  
**Lead:** `powershell.exe` / `wscript.exe` / Office → 443 or a high port

**Speaker Notes:**  
Same field family as 1.1.2/1.1.3, different job.

---

### Slide 9 – How It Is Logged
**Title:** Sysmon 3 / 22 ↔ DeviceNetworkEvents

| Need | Look at |
|------|---------|
| Connect | **3** / `ConnectionSuccess` |
| DNS on the host | **22** / name fields when logged |
| Dest | `DestinationIp`:`DestinationPort` or `RemoteIP`:`RemotePort` |
| Actor | `Image` or `InitiatingProcess*` |

**Speaker Notes:**  
3 ≠ 22. Missing 22 = visibility.

---

### Slide 10 – Example 1: Expected Connect
**Title:** Example 1 – Chrome → 443

- Sysmon **3**
- `Initiated=true`, `tcp/443`
- `DestinationHostname` `office-cdn.buildingc.internal`

**Interpretation:**  
Connect. Expected. Not an incident.

**Speaker Notes:**  
Students describe the row before you reveal.

---

### Slide 11 – Example 2: PowerShell Connect
**Title:** Example 2 – powershell -enc → 443

- MDE `ConnectionSuccess`
- Parent story is **1.1.2** (different row)
- `RemoteUrl` empty
- Dest `203.0.113.88:443`

**Interpretation:**  
Connect **lead** because of initiator + command line.

**Speaker Notes:**  
Force: 443 ≠ expected chain.

---

### Slide 12 – Example 3: DNS
**Title:** Example 3 – Event 22 vs Zeek dns

**22:** `powershell.exe` query `checkin.nightowl-updates.net`  
**Zeek `dns`:** same name, **no** process — that is **1.2**

**Interpretation:**  
DNS lead. Not a connect. Not a Zeek row.

**Speaker Notes:**  
If their lab has no 22, still run the contrast.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Event 22 = connect
- Query with no filter
- Zeek `conn` as “host network”
- Inventing a domain
- Asking how to deploy Sysmon / enable 22
- Opening JA3 or `uid`

**Speaker Notes:**  
Then the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide.
3. Two queries: script/Office/PowerShell outbound connect; DNS from script host / PowerShell.
4. One analysis card (Example 2 or 3).

**Speaker Notes:**  
Park Zeek, install, file. Review with the Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Event 3 vs 22? Missing 22?
2. Why initiating process vs Zeek?
3. What does `Initiated=true` mean?
4. Empty hostname / URL — what do you write?
5. Zeek `conn` to that IP — where is the process?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Host network row: this process connected or queried DNS.
- IP/port/protocol/direction + initiator; name when logged.
- Sysmon 3 / 22 ↔ `DeviceNetworkEvents`.
- 3 = connect. 22 = DNS. Zeek is **1.2**.
- Next: registry activity (**1.1.5**).

**Speaker Notes:**  
Do not open a 1.1.5 registry lab.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Endpoint Network — Quick Reference

| Need | Look at |
|------|---------|
| Connect | Sysmon 3 / `ConnectionSuccess` |
| DNS on host | Sysmon 22 / name fields |
| Dest | Destination* or Remote* |
| Direction | `Initiated` / ActionType |
| Actor | `Image` / `InitiatingProcess*` |

**Coming next:** Module 1.1.5 – Registry activity

**Footer:** SOC / Hunter / CTI Training Program
