# Module 1.2.5 – HTTP Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.5.1 A / B / C · 1.2.5.2 2b / 3c / 4c · 1.2.5.3 2b / 3c / 4c  
- Hunter: 1.2.5.1 B / C / C · 1.2.5.2 3c / 4c / 4c · 1.2.5.3 3c / 4c / 4c  
- CTI: 1.2.5.1 A / B / B · 1.2.5.2 1a / 2b / 3c · 1.2.5.3 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of the Zeek `http` log and the fields method, host, URI/URL, User-Agent, status code, and source/destination.
2. Analyze a Zeek HTTP log entry and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* HTTP pattern — not “all HTTP.”
4. Pivot from an `http` row to `conn` (and `dns` / `ssl` when useful) using `uid`.

**Mapped Proficiency Items:**
- K: 1.2.5.1 – HTTP engine
- T: 1.2.5.2 – Analyze a Zeek HTTP log and accurately describe what occurred
- T: 1.2.5.3 – Create a SIEM query to detect specific HTTP activity

---

## 1. Key Concepts

### 1.1 Purpose of the http Log

Zeek’s HTTP engine writes the **`http` log**. Each row is one HTTP request/response pair that the sensor saw **on the wire** (or reconstructed from the stream).

This is **not** host-observed network (**1.1.3**). A Sysmon 3 / `DeviceNetworkEvents` row names the process. An `http` row names **method, host, URI, User-Agent, and status**. It does not name `chrome.exe`.

You usually do **not** get the full body. You get metadata. Body *lengths* may be present; extracted files are **1.2.7**.

| This lesson | Later / other |
|-------------|---------------|
| Method, host, URI, User-Agent, status, 5-tuple, `uid` | File extract / hashes (`files` log) — **1.2.7** |
| Cleartext HTTP and HTTP that Zeek still parsed | TLS handshake fields — **1.2.4** (`ssl` log) |
| Sensor HTTP | SIGMA / Suricata HTTP options — **1.3** |

If a field is empty (no User-Agent, no host), say so. Do not invent it.

### 1.2 Key Fields

| Field | Description | Why it matters |
|-------|-------------|----------------|
| `ts` | Timestamp | When the request happened |
| `uid` | Connection identifier | Links to `conn`, `dns`, `ssl`, `files`, `weird` |
| `id.orig_h` / `id.orig_p` | Client IP / port | Who requested |
| `id.resp_h` / `id.resp_p` | Server IP / port | Who answered (often 80 or 8080; 443 may appear if HTTP is still parsed) |
| `method` | GET, POST, PUT, HEAD, … | What the client asked to do |
| `host` | Host header | The name the client put on the request |
| `uri` | Path and query | The object. Combine with `host` for the URL |
| `user_agent` | User-Agent header | What the client claimed to be. Can lie. |
| `status_code` | HTTP status | 200 vs 301 vs 404 vs 401/403 |

**URL:** Zeek splits it. **Host** + **URI** is the URL you describe (`http://intranet.buildingc.internal/docs/q3.pdf`). There is often no single `url` field.

**Most critical for daily work:** `method`, `host`, `uri`, `user_agent`, `status_code`, `id.orig_h`, `id.resp_h`, `id.resp_p`, `uid`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| `GET` + known `host` + document/image `uri` + browser User-Agent + `200` | `POST` to a new/rare host, or `GET` of `.exe` / `.ps1` / `.dll` |
| Browser User-Agent you see every day | Empty User-Agent, `curl`/`python`/`PowerShell` on a workstation, or a UA that does not match the host’s job |
| `200` / `304` / expected `302` to a known site | Many `404`/`401` from one orig, or `200` on a URI that should not exist |
| Port 80 to an internal intranet | HTTP to the internet on an odd port, or HTTP where you expected TLS |

**Method:** `GET` is the common read. `POST` / `PUT` means the client sent a body — you still may not see the bytes. Describe the method; do not invent the payload.

**Host vs dest IP:** `host` is the name on the request. `id.resp_h` is where the packets went. They should tell a consistent story. A well-known host header to an unexpected IP is a lead.

**User-Agent:** A name, not an identity. Office and browsers have long UAs. Scripting UAs on a user VLAN are a lead. Empty UA is a visibility note and sometimes a lead.

**Status:** `200` is not “benign.” `404` is not “safe.” Read them with method + host + URI.

Always copy `uid` and search `conn` (bytes, state, duration). Search `dns` / `ssl` when the session has those rows.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal GET

```
ts: 2026-08-15T14:10:03.120Z
uid: CHttpAb12Cd34Ef56
id.orig_h: 10.10.50.23
id.orig_p: 49112
id.resp_h: 10.10.8.20
id.resp_p: 80
method: GET
host: intranet.buildingc.internal
uri: /docs/q3-notes.pdf
user_agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0.0.0
status_code: 200
```

**What occurred:** Internal host `GET` a PDF from the intranet web server. Browser UA. Status 200. Expected.

**Next if you still care:** Pivot on `uid` to `conn` to confirm duration and bytes. Do not open a files-log lesson unless you need the hash (**1.2.7**).

### Example 2: POST + Scripting User-Agent (Lead)

```
uid: CHttpXy98Zt76Uv54
id.orig_h: 10.10.50.88
id.orig_p: 50821
id.resp_h: 203.0.113.88
id.resp_p: 80
method: POST
host: checkin.nightowl-updates.net
uri: /api/v1/beacon
user_agent: WindowsPowerShell/5.1.19041.1
status_code: 200
```

**What occurred:** A workstation **POST**ed to `checkin.nightowl-updates.net/api/v1/beacon` with a **PowerShell** User-Agent and got `200`. Dest is internet (`203.0.113.88`).

**Interpretation:** Lead, not an automatic incident. Describe method + host + URI + UA + status. Pivot `uid` to `conn` (and `dns` for the name). Do not invent a body. Do not write a Suricata rule in this hour (**1.3**).

### Example 3: GET of an Executable, Odd Status Mix (Lead)

```
uid: CHttpQr11Mn22Op33
id.orig_h: 10.10.22.17
id.orig_p: 51100
id.resp_h: 198.51.100.80
id.resp_p: 8080
method: GET
host: update-cdn.not-a-real-cdn.net
uri: /payload/update.exe
user_agent: -
status_code: 200
```

Compare a miss that is *not* this row:

> Same orig, `GET /login` → `404` twenty times in a minute on another `uid`. That is a **different** request. Status 404 is its own story.

**What occurred:** `GET` of `/payload/update.exe` on port **8080**, empty User-Agent, status **200**. Host looks like an “update CDN.”

**Interpretation:** Lead. Name method, URI extension, port, empty UA, and 200. Empty UA → write “not logged.” Pivot `uid` to `conn` and, if a file was extracted, to `files` (**1.2.7**). Do not treat every `.exe` URI as malware.

---

## 3. Hands-On Exercise

**Objective:** Practice describing HTTP rows and writing queries that find a specific pattern.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (expected vs lead).
2. Write **two SIEM-style pseudo-queries**:
   - One for **scripting or empty User-Agent** making a `POST` (or `GET` of `.exe` / `.ps1` / `.dll`) to a non-internal host.
   - One for **status_code** `401` or `404` **count** from a single `id.orig_h` (or any specific status hunt you can explain).
3. Explain how you would pivot from a suspicious `http` entry to the related `conn` activity using the `uid`. Name one more log you might open (`dns`, `ssl`, or `files`) and why.
4. For each item below, say **HTTP event** or **not this log**. Give one reason.
   - Zeek `http` `GET /docs/q3-notes.pdf` 200
   - Zeek `ssl` SNI `intranet.buildingc.internal`
   - MDE `DeviceNetworkEvents` `chrome.exe` → `10.10.8.20:80`
   - Zeek `files` hash of a PDF

**Expected Outcome:**
- Accurate short summaries of the three examples
- Two specific HTTP queries (not `http` with no filter)
- A correct `uid` pivot explanation
- Four identifications with a reason each

---

## 4. Knowledge Check

1. What is the primary purpose of the Zeek `http` log? How is it different from host-observed network (**1.1.3**)?
2. Which fields do you combine to describe the **URL**?
3. Why is User-Agent useful, and why is it not an identity?
4. Why is `status_code` 200 not a verdict?
5. Why is the `uid` field important when analyzing HTTP activity?

---

## 5. Summary

- The HTTP engine writes the `http` log: request/response **metadata**, not a full body dump.
- Critical fields: `method`, `host`, `uri`, `user_agent`, `status_code`, addresses/ports, `uid`.
- URL = host + URI. Empty UA or host → write “not logged.”
- POST, odd UA, `.exe` URI, unexpected port, and status spikes are leads — not automatic incidents.
- Always pivot with `uid` to `conn` (then `dns` / `ssl` / `files` as needed).
- Next: SMTP engine (**1.2.6**). File extract is **1.2.7**.

---

## 6. References & Further Reading

- Zeek http.log documentation: https://docs.zeek.org/en/current/scripts/base/protocols/http/main.zeek.html
- Related modules:
  - 1.1.3 – Network activity (endpoint)
  - 1.2.2 – Conn engine
  - 1.2.3 – DNS engine
  - 1.2.4 – TLS engine
  - 1.2.6 – SMTP engine (next)
  - 1.2.7 – Files engine
