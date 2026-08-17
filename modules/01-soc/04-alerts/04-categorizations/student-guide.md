# Module 1.4.4 – Common Alert Categorizations

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.4.1 A / B / C · 1.4.4.2 2b / 3c / 4c  
- Hunter: 1.4.4.1 B / C / C · 1.4.4.2 2b / 3c / 4c  
- CTI: 1.4.4.1 A / A / A · 1.4.4.2 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the classroom categories: scanning/reconnaissance, root-level access, user-level access, unsuccessful activity, and **other** as your site uses it.
2. Assign a category to an alert and **justify why it is not the adjacent category**.

**Mapped Proficiency Items:**
- K: 1.4.4.1 – Common alert categorizations
- T: 1.4.4.2 – Assign a category and justify why it is not the adjacent category

---

## 1. Key Concepts

A **category** is how the SOC buckets a **working** alert for reporting and handoff. It is not TP/FP (**1.4.2**) and not an ATT&CK ID (**0.6**). You pick one bucket and say why the **neighbor** is wrong.

| Category | Use when | Adjacent — do not confuse with |
|----------|----------|--------------------------------|
| **Scanning / reconnaissance** | Wide, unauthenticated probing (many ports/hosts, no session that is an access attempt) | **Unsuccessful** — a failed login is an access *attempt*, not a sweep |
| **Root-level access** | SYSTEM / admin / service-level control on the host (or clear evidence of it) | **User-level** — same malware, medium user token |
| **User-level access** | Activity as a normal user token (Medium `jlee`) | **Root-level** — do not upgrade because it “looks scary” |
| **Unsuccessful activity** | An access or exploit *attempt* that failed (denied logon, 401 burst against one app) | **Scanning** — failed auth is not a port sweep |
| **Other (local)** | What your site listed (policy, phishing-reported-only, etc.) | Say which local name, and which neighbor you rejected |

If your site adds buckets, they live under **other**. Do not invent ATT&CK tactics as categories.

| This lesson | Other |
|-------------|-------|
| One category + rejected neighbor | TP/FP — **1.4.2** |
| Site buckets | ATT&CK map — **0.6** |
| Working alert | SLA clocks — **1.4.5** |

The task is **not** “assign an appropriate category.” It is **assign + rule out the adjacent one** in one sentence each.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| SYN to 200 ports, no auth → **scan**, not unsuccessful | Failed RDP labeled **scan** |
| `jlee` Medium + `-enc` → **user-level**, not root | Encoded PS labeled **root** because “malware” |
| SYSTEM service key create → **root-level**, not user | Helpdesk.exe in Temp labeled user because the *file* is user-writable |
| 50× 401 on one mailbox → **unsuccessful**, not scan | |

---

## 2. Detailed Walkthrough / Examples

Assume these are **working** alerts (you are not classifying TP/FP here).

### Example 1: Scan, Not Unsuccessful (Expected)

**Alert:** Many `S0` / unanswered SYN from `10.10.50.88` to 150 internal ports in two minutes. No login attempt.

**Category:** **Scanning / reconnaissance**.  
**Not unsuccessful:** Nothing was presented as credentials or an exploit against a service — it is a sweep.

### Example 2: User-Level, Not Root (Lead)

**Alert:** Encoded PowerShell from `wscript` as `BUILDINGC\jlee`, integrity Medium (**1.4.1** Ex 1).

**Category:** **User-level access**.  
**Not root-level:** Token is a standard user. Encoded does not upgrade the category. (Escalation *how-to* is **2.6.2**, not this label.)

### Example 3: Unsuccessful, Not Scan (Lead)

**Alert:** 40× `401` from `10.10.22.17` to `mail.buildingc.internal` `/login` in three minutes. One mailbox, auth failing.

**Category:** **Unsuccessful activity**.  
**Not scanning:** This is a failed access attempt against one application, not a wide unauthenticated sweep.

**Nearby root (not a fourth full example):** Temp `helpdesk.exe` **CreateKey** under `HKLM\...\Services\HelpdeskSvc` (**1.1.5** Ex 3) → **root-level** (service/HKLM), **not user-level**, even though the binary sat in a user path.

---

## 3. Hands-On Exercise

**Objective:** Assign a category and reject the neighbor.

**Instructions:**

1. One sentence each for Examples 1–3: category + rejected neighbor.
2. For each alert below, write **category**, **adjacent you reject**, and **why**.

   - A. Sysmon 3: `jlee` Medium `chrome.exe` → 2000 internet IPs on port 80, `Initiated=true`, 1-second bursts, no HTTP 401 story.
   - B. MDE: `powershell.exe -enc` as `SYSTEM` after a service start.
   - C. SIEM: 15 failed `ssh` logons to one jump box from one external IP, then stop. No session.
   - D. Alert on documented vuln-mgmt scanner SYN sweep (if you already know it is authorized, you still **categorize** the *activity type* here — do not spend the hour on FP cause).

3. Do not write TP/FP. Do not write T1059.
4. If you need **other**, name the local bucket and the neighbor you rejected.

**Expected Outcome:**
- Three example summaries
- Four category + rejected-neighbor pairs
- No classification, no ATT&CK

---

## 4. Knowledge Check

1. Name the four syllabus categories plus **other**.
2. What is the **adjacent** pair for scanning vs unsuccessful?
3. What is the **adjacent** pair for user-level vs root-level?
4. Why is “assign an appropriate category” not enough for sign-off?
5. Where does ATT&CK belong?

---

## 5. Summary

- Category = site bucket, not TP/FP and not ATT&CK.
- Always reject the neighbor.
- Next: SLA clocks (**1.4.5**).

---

## 6. References & Further Reading

- Related modules:
  - 1.4.2 – Alert classification
  - 1.4.3 – Common false positive causes (previous)
  - 1.4.5 – SLA / response time goals (next)
  - 0.6.1 – MITRE ATT&CK
  - Local category list used on shift (optional)
