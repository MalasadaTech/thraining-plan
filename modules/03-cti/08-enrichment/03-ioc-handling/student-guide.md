# Module 3.8.3 – IOC Handling and Enrichment Concepts

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.8.3 A / B / B · 3.8.3.1 1a / 2b / 3c · 3.8.3.2 1a / 1a / 2b  
- Hunter: 3.8.3 B / C / C · 3.8.3.1 3c / 4c / 4d · 3.8.3.2 1a / 2b / 3c  
- CTI: 3.8.3 B / C / C · 3.8.3.1 3c / 4c / 4d · 3.8.3.2 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Treat an **IOC** as an observable you **handle** (keep, enrich, expire) — not a TTP.
2. **Record** the next enrichment (tool + field) without re-teaching that tool.
3. **Link** handled IOCs into one activity set — or keep them apart.
4. **Reject** stale / uncited / shared-infra noise and a vendor group name with no shared objects.

**Mapped Proficiency Items:**
- K: 3.8.3 – IOC handling and enrichment concepts
- T: 3.8.3.1 – Enrich and pivot on IOCs using internal and external tools
- T: 3.8.3.2 – Link analysis and campaign tracking

---

## 1. Key Concepts

**3.8.1** wrote the generic hop sentence (one cited sibling name). **3.8.2** decided which TTPs apply here. This hour you **handle the objects**: what to keep, what to enrich next, and which objects belong in the **same activity set**.

Do not re-open RDAP (**3.5**), SOA (**3.6**), tool choice (**3.3.2**), or VT/Silent Push depth (**3.9**). Do not write DTF PTA/P IDs (**3.7.4**). Do not write **3.8.4** impact. Do not write a **3.11** actor profile.

**IOC vs TTP (outline a):**

| Term | This hour | Not this hour |
|------|-----------|---------------|
| **IOC** | Domain, IP, hash, registry value, filename you can record | “They use PowerShell” (that is a TTP — **3.8.2**) |
| **Handle** | Keep / expire / reject + why | Assign T1059.001 |

**Handling rules (outline b):**

| Call | When | Example on this card |
|------|------|----------------------|
| **Keep** | Cited, current, distinctive | `nightowl-updates.net`, hash `6734f374…`, HKCU Run `Updater` |
| **Expire** | Cited once, now stale or recycled | A vendor IP from 2019 with no Harbor sighting |
| **Reject** | Uncited, shared hosting, or not an IOC | `evil-c2.net` with no link; whole `203.0.113.0/24`; “Night Owl APT” |

**Enrichment record (outline c / task 3.8.3.1):** name the tool you already know and the field you want. Do **not** run the query. Do **not** write the 3.8.1 hop sentence.

**Enrich line:**  
`IOC | tool (already taught) | field | what you hope to learn`

| IOC type | Tool you already have | Field you name |
|----------|----------------------|----------------|
| Domain | RDAP (**3.5**) / SOA (**3.6**) / PDNS (**3.3.2**) | NS, RNAME, historical A |
| IP | PDNS / RDAP | siblings on that A; org (hosting, not “theirs”) |
| Hash | VT Relations (**3.9.1**) | contacted hosts (name the tab, do not open a 3.9 lab) |
| Host / registry | TIP (**3.3.1**) | other Harbor sightings |

**Link / campaign track (outline d / task 3.8.3.2):** same **activity set** if objects share a cited property on *this* card. Separate if they do not. A vendor cluster name is not a link.

**Handle line:**  
`IOC | type | keep / expire / reject | why`

**Link line:**  
`objects | same activity set? | shared cite | not a group name`

**In the product:** keep the Night Owl domain + hash + Run key as **one set**. Expire the 2019 IP. Reject `evil-c2.net` and “Night Owl APT.” Enrich the domain via NS/PDNS (named, not run).

| This lesson | Other |
|-------------|-------|
| Handle + enrich-record + link | Hop sentence — **3.8.1** |
| Not TTP apply | **3.8.2** |
| Not “so what to pay-db-01” | **3.8.4** |
| Not tool reading | **3.5 / 3.6 / 3.9** |
| Not actor profile | **3.11** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Domain + hash + Run key = one set | Vendor APT name glues the set |
| 2019 IP = expire | Whole /24 = keep |
| Enrich line names RDAP NS | Re-run the 3.8.1 hop |

---

## 2. Detailed Walkthrough / Examples

**Classroom IOC tray (lesson-only):**

| Object | Cite |
|--------|------|
| `nightowl-updates.net` | WS-JLEE GET; same A as `login-nightowl.net` (**3.8.1**) |
| SHA256 `6734f374…` | `update.exe` on WS-JLEE |
| HKCU Run `Updater` | same host |
| `203.0.113.88` | A of the domain |
| Vendor IP `198.51.100.12` (2019 PDF, no Harbor row) | none here |
| Vendor `evil-c2.net` | none here |
| Label “Night Owl APT” | none — a name |

### Example 1: One Activity Set (Expected)

**Handle:** keep domain, hash, Run key, and the A.  
**Enrich:** `nightowl-updates.net | SOA/PDNS | RNAME + historical A | more siblings on the same stack`  
**Link:** `domain + hash + Run + A | same set | same host + same A | not “APT”`  
**Not:** the 3.8.1 hop sentence without a handle call. **Not:** a 3.11 profile.

### Example 2: Stale / Shared / Uncited (Lead)

**Draft:** Keep `198.51.100.12`, the whole `/24`, and `evil-c2.net`.

**Fail.** 2019 IP has no Harbor cite (**expire**). `/24` is shared hosting (**reject**). `evil-c2.net` is uncited (**reject**).  
**Lead:** Handling is evidence-bound. Same rule as an uncited hop (**3.8.1**).

### Example 3: Name as the Glue (Lead)

**Draft:** “All of these plus the vendor Linux backdoor are Night Owl APT, one campaign.”

**Fail.** A group name is not a shared object. Linux backdoor is a TTP question (**3.8.2**), not an IOC link.  
**Lead:** Link objects. Do not link labels.

---

## 3. Hands-On Exercise

**Objective:** Handle the tray. Record one enrichment. Link the set. Reject noise and names.

**Use only the classroom tray.**

**Instructions:**

1. One sentence each for Examples 1–3: keep/expire/reject vs fail.
2. **Handle** (outline b): a **handle line** for each.

   - A. `nightowl-updates.net`  
   - B. SHA256 `6734f374…`  
   - C. Vendor IP `198.51.100.12` (2019)  
   - D. Whole `203.0.113.0/24`  
   - E. “Night Owl APT”

3. **Enrich** (3.8.3.1): one **enrich line** each for A and B only. Name the tool/field. Do not run it. Do not write a 3.8.1 hop sentence.
4. **Link** (3.8.3.2): one **link line** for A+B+Run key. One line that **rejects** E as glue.
5. Do not assign T-IDs (**3.8.2**). Do not write **3.8.4** impact. Do not open VT (**3.9**). Do not invent a group.

**Expected Outcome:**
- Three example summaries
- Five handle lines (C expire; D and E reject)
- Two enrich lines
- Two link lines (one set; name is not glue)
- No hop sentence, no actor profile

---

## 4. Knowledge Check

1. What is an **IOC** this hour, versus a TTP?
2. When do you **expire** versus **reject**?
3. What belongs on an **enrich line** — and what does it **not** include?
4. What makes two IOCs the **same activity set**?
5. Why is a vendor **APT name** not campaign tracking?

---

## 5. Summary

- Keep cited current objects. Expire stale. Reject uncited and shared noise. Record the next lookup. Link objects, not names.
- Next: **3.8.4** Threat relevance and organizational impact.

---

## 6. References & Further Reading

- Related modules:
  - 3.8.1 – Generic infra hop
  - 3.8.2 – Applicable TTPs
  - 3.8.4 – Relevance / impact (next)
  - 3.3.2 / 3.5 / 3.6 / 3.9 – Tools already taught
- Classroom tray in this guide (lesson-only)
