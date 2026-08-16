# Module 3.9.4 – URLScan

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.9.4 A / A / B · 3.9.4.1 1a / 1a / 2b  
- Hunter: 3.9.4 A / B / B · 3.9.4.1 2b / 3c / 4c  
- CTI: 3.9.4 B / C / C · 3.9.4.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State URLScan **capabilities** (submit or retrieve a **page load**).
2. **Submit or retrieve** a result from the classroom card (no live malware URL).
3. **Extract** actionable intel: redirect, contacted host, screenshot *as appearance*.
4. **Reject** using URLScan for PDNS history, or treating a fake-login screenshot as a finished theft case.

**Mapped Proficiency Items:**
- K: 3.9.4 – URLScan
- T: 3.9.4.1 – Submit or retrieve a URLScan result and extract actionable intelligence

---

## 1. Key Concepts

**3.3.2** taught *when* URLScan is the tool (live **URL / page**). This hour is **get a result** and **read it**. Silent Push is history (**3.9.3**). AnyRun is a *file* (**3.9.2**). Hunt SIEM/Zeek is **2.3.1**. Do **not** submit live malware URLs in class.

**Capabilities (outline a):**

| Capability | Intel use | Not |
|------------|-----------|-----|
| **Submit / retrieve scan** | This URL, this load | Historical A records |
| **Redirect chain** | Where the browser actually went | The registrant |
| **Contacted hosts / IPs** | Hosts *this page* called | PDNS siblings |
| **Screenshot / DOM** | What the user was *shown* | Proof credentials were stolen |
| **Cert / cookies** | Weak extra context | Actor name |

**Interpret (outline b):** take redirects + contacted hosts + what the page *looked like*. Leave history, process trees, and impact to other modules.

**Classroom URLScan cards (this lesson only):**

**URL:** `https://invoice-harbor.example/pay` (retrieve existing scan — do not submit live).

| Field | Value |
|-------|--------|
| Final URL | `https://nightowl-updates.net/invoice` |
| Redirects | `invoice-harbor.example/pay` → `nightowl-updates.net/invoice` |
| Contacted | `nightowl-updates.net`, `203.0.113.88` |
| Screenshot | Fake Harbor finance login (classroom description) |
| Title / DOM | “Harbor Invoice — Sign in” |
| Cert | `nightowl-updates.net` (not Harbor) |
| Scan age | today |

**Retrieve/submit line:** `URL | submit or retrieve | why that one`  
**Extract line:** `redirect | contacted host | appearance | what you will not claim`

| This lesson | Other |
|-------------|-------|
| This page load | When to pick URLScan — **3.3.2** |
| Not PDNS history | **3.9.3** |
| Not file process tree | **3.9.2** / **3.9.1** |
| Not SIEM/Zeek query | **2.3.1** |
| Not “user was phished, Sev1” | **3.8.4** / **1.8.5** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Retrieve → redirect + contacted host | URLScan for last year’s A records |
| Screenshot = *appearance* | Screenshot = confirmed credential theft |
| Cert CN ≠ Harbor | Actor profile from the fake login |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Retrieve and Extract (Expected)

**Retrieve:** existing scan of `https://invoice-harbor.example/pay` (safer than a live submit of a known-bad URL).  
**Extract:** redirect to `nightowl-updates.net/invoice`; contacted `203.0.113.88`; page *looks like* Harbor finance login; cert is `nightowl-updates.net`.  
**Product:** those facts. Not “jlee was compromised.”

### Example 2: URLScan for History (Lead)

**Draft:** Use URLScan to list every IP `nightowl-updates.net` has used this year.

**Fail.** That is **3.9.3**. This scan is *one load*.  
**Lead:** Right domain. Wrong tool.

### Example 3: Screenshot as Theft (Lead)

**Draft:** Fake login screenshot → “credential theft succeeded; write the actor profile.”

**Fail.** Appearance ≠ successful theft. Profile is **3.11**. Impact/Sev is **3.8.4** / **1.8.5**.  
**Lead:** Extract what the page *showed*. Stop.

---

## 3. Hands-On Exercise

**Objective:** Retrieve the classroom scan. Extract redirects/hosts/appearance. Reject history and over-claim.

**Do not submit a live malware URL.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Retrieve/submit** (task 1): write a **retrieve/submit line** for each.

   - A. The invoice URL above (retrieve).  
   - B. “Submit the live Night Owl C2 URL from class Wi-Fi.”  
   - C. Need last year’s IPs for `nightowl-updates.net`.

3. **Extract** (task 2): one **extract line** for the classroom scan, plus:

   - D. “Screenshot proves jlee entered a password.”  
   - E. Contacted `203.0.113.88` as a fact from *this* load.

4. Do not open Silent Push for A’s extract. Do not write a SIEM query. Do not write a **3.11** profile.
5. B is **refuse** (safety + not needed — the retrieve card exists).

**Expected Outcome:**
- Three example summaries
- Three retrieve/submit lines (B refuse; C = wrong tool)
- Extract line + D reject + E keep
- No live submit, no PDNS dump

---

## 4. Knowledge Check

1. What is URLScan **for**, in one sentence?
2. When do you **retrieve** instead of **submit**?
3. Name **two** fields you extract from the classroom scan.
4. Why is URLScan the wrong tool for **historical A** records?
5. Why does a fake-login **screenshot** not prove theft?

---

## 5. Summary

- This page load: redirect, contacted host, appearance. Not PDNS. Not a profile.
- This closes unit **3.9**. Next: **3.10** Common STIX Objects.

---

## 6. References & Further Reading

- Related modules:
  - 3.9.3 – Silent Push (previous)
  - 3.3.2 – When to open URLScan
  - 3.10 – STIX objects (next unit)
- Classroom URLScan cards in this guide (lesson-only)
- Do not submit live malware URLs from the classroom network
