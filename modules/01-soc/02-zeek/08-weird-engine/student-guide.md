# Module 1.2.8 – Weird Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.8.1 A / B / C ; 1.2.8.2 2b / 3c / 4c ; 1.2.8.3 2b / 3c / 4c  
- Hunter: 1.2.8.1 B / C / C ; 1.2.8.2 3c / 4c / 4c ; 1.2.8.3 3c / 4c / 4c  
- CTI: 1.2.8.1 A / A / A ; 1.2.8.2 1a / 1a / 1a ; 1.2.8.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `weird` row: the type, who talked to whom, and the UID that joins other Zeek logs.
2. Describe what a `weird` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.8.1 – Weird engine
- T: 1.2.8.2 – Analyze a Zeek weird log and accurately describe what occurred
- T: 1.2.8.3 – Create a SIEM query to detect specific weird activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`weird`** log when the sensor saw protocol behavior that is **off-spec or uncommon**. **1.2.7** was the file on the wire. This hour closes **1.2**. A weird row is a **lead**, not a verdict. It does **not** name the initiating process (**1.1.4**).

**`weird`** is one row for something Zeek flagged.

| Idea | What to read |
|------|----------------|
| **Type / notice** | `name` — the weird type (the string you query). `notice` (when present) is only whether *this* type was also raised as a notice. This is **not** a `notice.log` course |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` |
| **Connection UID** | `uid` — same join as `conn` / `http` / `files`. Empty → write “no uid” and use IP/port/time |

Do not memorize the Zeek catalog. Describe the `name` you have. Do not invent a story from the word “weird.”

**What good looks like:**

- Describe: one sentence — Zeek flagged this `name` between these IPs/ports. Then say which `uid` you would open on `conn`. Do not call it malware.
- Given: `name` `data_before_established`, `id.resp_h` `203.0.113.88`, `id.resp_p` `8080`, `uid` present. **What occurred:** Zeek saw data before the handshake finished on the same dest as the **1.2.5** GET. Look at `conn` / `http` on that `uid`. The file extract is **1.2.7**.
- Query: names a **specific** `name` (or dest), not “all `weird` rows.”

Detection rule syntax is **1.3**.

---

## 2. Knowledge Check

1. A single `weird` row is an incident. True or false?
2. `name` `data_before_established`, dest `203.0.113.88:8080`, `uid` present. In one sentence, what occurred?
3. A SIEM query that matches every `weird` row is a good “specific weird activity” query. True or false?

---

## 3. Summary

A `weird` row is a type, two endpoints, and a UID. It is a lead. The process is not on this row. A query names a specific type.

**Next:** **1.3.1** SIGMA rules.

---

## 4. Related modules

- 1.2.7 – Files engine (previous)
- 1.2.2 – Conn engine
- 1.2.5 – HTTP engine
- 1.3.1 – SIGMA rules
