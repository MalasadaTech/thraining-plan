# Module 1.2.8 – Weird Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.8.1 A / B / C · 1.2.8.2 2b / 3c / 4c · 1.2.8.3 2b / 3c / 4c  
- Hunter: 1.2.8.1 B / C / C · 1.2.8.2 3c / 4c / 4c · 1.2.8.3 3c / 4c / 4c  
- CTI: 1.2.8.1 A / A / A · 1.2.8.2 1a / 1a / 1a · 1.2.8.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the Zeek `weird` log: activity type (`name`), the `notice` flag (where used), source/destination, and `uid` linking.
2. Analyze a Zeek weird log entry and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* weird pattern — not “all weird.”
4. Pivot from a `weird` row to `conn` (and protocol logs) using `uid`.

**Mapped Proficiency Items:**
- K: 1.2.8.1 – Weird engine
- T: 1.2.8.2 – Analyze a Zeek weird log and accurately describe what occurred
- T: 1.2.8.3 – Create a SIEM query to detect specific weird activity

---

## 1. Key Concepts

### 1.1 Purpose of the weird Log

Zeek’s weird engine writes the **`weird` log**. A row means Zeek saw **protocol or traffic behavior that is unusual relative to the spec or to common practice** — a malformed handshake, data before the connection was established, an unmatched DNS reply, and similar.

It is a **lead generator**, not a verdict. Many `weird` names fire on noisy but benign networks. A single row is rarely an incident.

This is **not** the `notice` log. `notice.log` is Zeek raising a policy notice. The `weird` row may include a **`notice` field** (boolean): whether *this* weird was also raised as a notice. Do not turn this hour into a notice-framework course.

| This lesson | Other |
|-------------|-------|
| `weird.name` + 5-tuple + `uid` | `notice` log policy / types — later / local |
| Sensor anomaly hook | Host process (**1.1**), HTTP/SMTP/files engines (**1.2.5–1.2.7**) |
| Query a specific `name` | Writing a Zeek script to emit new weirds |

If `name` is empty or you do not recognize it, write the string you have and pivot. Do not invent a story from the word “weird” alone.

### 1.2 Key Fields

| Field | Description | Why it matters |
|-------|-------------|----------------|
| `ts` | Timestamp | When Zeek flagged it |
| `uid` | Connection identifier | Links to `conn` and protocol logs — **outline c** |
| `id.orig_h` / `id.orig_p` | One endpoint | Usually the initiator |
| `id.resp_h` / `id.resp_p` | Other endpoint | Usually the responder |
| `name` | Weird **type** | What Zeek thought was off — **outline a** |
| `addl` | Extra detail (when present) | Often the clarifying string |
| `notice` | Whether this weird was also a notice | Flag only; not the whole notice log |
| `source` | Where in Zeek it fired (when present) | Analyzer / script hint |

**Most critical for daily work:** `name`, `id.orig_h`, `id.resp_h`, `id.resp_p`, `uid`, `notice` (if logged), `addl`

| Expected / noisy (often) | Lead (usually) |
|--------------------------|----------------|
| Occasional `dns_unmatched_reply` on a busy resolver path | Same `name` **volume** from one `id.orig_h` in a short window |
| One `window_recision` on a long flow | `data_before_established` or handshake weirds **plus** an odd `conn` state |
| A name your site already allow-lists | A name you have never seen, or `notice=true` on a rare name |
| Weird on a known scanner / vulnerability-mgmt range | Weird from a user workstation to the internet on 443/80 with no matching `http`/`ssl` story |

**name (weird activity type):** This is the field you query. Learn the *names you actually see* in the tenant. Do not memorize the entire Zeek catalog in this hour. Describe: “Zeek flagged `data_before_established` between these IPs.”

**notice (flag):** If `notice` is true, someone configured this type to raise a notice. Still describe the weird row. Open `notice.log` only if your site uses it and the instructor says so — it is not a sign-off item here.

**Source and destination:** Same 5-tuple habit as Conn. Weird without addresses is incomplete — say what is missing.

**uid:** Always copy it. Search `conn` first (state, history, bytes). Then `http` / `dns` / `ssl` / `files` if those rows exist. A weird with no `uid` (some analyzer-level events) → write “no connection uid” and use the 5-tuple + time.

This lesson **closes 1.2**. Protocol deep-dives are done. Detection engineering is **1.3**.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Noisy but Common DNS Weird

```
ts: 2026-08-15T14:08:01.002Z
uid: CDnsAa11Bb22Cc33
id.orig_h: 10.10.8.53
id.orig_p: 53
id.resp_h: 10.10.50.23
id.resp_p: 52881
name: dns_unmatched_reply
addl: -
notice: false
```

**What occurred:** Zeek flagged `dns_unmatched_reply` involving the internal resolver (`10.10.8.53`) and a workstation. `notice` is false. On many sites this is **noise**.

**Interpretation:** Expected-as-noise unless volume spikes. Describe the `name` and the pair. Pivot `uid` to `dns` / `conn` only if you are hunting a spike. Do not ticket a single row.

### Example 2: data_before_established (Lead)

```
uid: CWrdXy98Zt76Uv54
id.orig_h: 10.10.50.88
id.orig_p: 50821
id.resp_h: 203.0.113.88
id.resp_p: 80
name: data_before_established
addl: -
notice: false
```

**What occurred:** Workstation `10.10.50.88` talked to `203.0.113.88:80` and Zeek saw **data before the handshake finished**. Same orig/dest as the **1.2.5** PowerShell POST example if the `uid` matches that session — *if it does, say so after you pivot*.

**Interpretation:** Lead. The `name` says the TCP/HTTP timing was off. It is not “malware.” Pivot `uid` to `conn` (`history`, `conn_state`) and `http`. Stack the weird with the HTTP story; do not treat the weird alone as C2.

### Example 3: Rare Name + notice true (Lead)

```
uid: CWrdQr11Mn22Op33
id.orig_h: 10.10.22.17
id.orig_p: 51100
id.resp_h: 198.51.100.80
id.resp_p: 8080
name: line_terminated_with_single_CR
addl: HTTP
notice: true
source: HTTP
```

**What occurred:** Zeek flagged `line_terminated_with_single_CR` on an HTTP session to `198.51.100.80:8080` (same dest as the **1.2.5** `update.exe` GET). `notice` is **true** — this type was configured to raise a notice.

**Interpretation:** Lead. Name the type, dest, and `notice=true`. Pivot `uid` to `http` / `conn` / `files`. Do not teach how to write `notice` policy. A non-standard HTTP line ending is a reason to look at the session, not a conviction.

---

## 3. Hands-On Exercise

**Objective:** Practice describing weird rows and writing queries that find a specific type.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (noise vs lead).
2. Write **two SIEM-style pseudo-queries**:
   - One for a **specific `name`** you care about (use `data_before_established` or another name from the examples) from **non-infra** origins (e.g. `10.10.50.` / `10.10.22.`).
   - One for **volume**: count of a given `name` by `id.orig_h` (or `notice == true` on names that are rare on your list).
3. Explain how you would pivot from a suspicious `weird` entry to `conn` using `uid`. What do you write if `uid` is empty?
4. For each item below, say **weird event** or **not this log**. Give one reason.
   - Zeek `weird` `name=data_before_established`
   - Zeek `http` POST `/api/v1/beacon`
   - Zeek `notice` log policy row (not the `weird.notice` flag)
   - MDE `DeviceNetworkEvents` connection

**Expected Outcome:**
- Accurate short summaries
- Two specific weird queries (not `weird` with no filter)
- A correct `uid` pivot (and empty-uid note)
- Four identifications with a reason each

---

## 4. Knowledge Check

1. What is the primary purpose of the Zeek `weird` log? Why is a single row rarely an incident?
2. Which field is the **weird activity type**? What is the `notice` *field* on that row?
3. How is `weird` different from the `notice` log?
4. What source and destination fields do you read?
5. Why is `uid` important here, and what do you write if it is missing?

---

## 5. Summary

- The weird engine writes the `weird` log: “this looked off to Zeek,” not “this is malicious.”
- Critical fields: `name`, 5-tuple, `uid`, `notice` (flag), `addl` when present.
- Query **specific names** or **volume**. Do not alert on all weird.
- Always pivot with `uid` to `conn` (then protocol logs). Empty uid → say so; use IP/port/time.
- This closes unit **1.2**. Next unit: Detection Engineering (**1.3**).

---

## 6. References & Further Reading

- Zeek weird.log documentation: https://docs.zeek.org/en/current/scripts/base/frameworks/notice/weird.zeek.html
- Related modules:
  - 1.2.2 – Conn engine
  - 1.2.3 – DNS engine
  - 1.2.5 – HTTP engine
  - 1.2.7 – Files engine (previous)
  - 1.3.1 – SIGMA rules (next unit)
