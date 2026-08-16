# Module 3.7.4 – MalasadaTech Defender’s ThreatMesh Framework (DTF)

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.7.4 A / A / B · 3.7.4.1 1a / 1a / 2b · 3.7.4.2 1a / 1a / 2b · 3.7.4.3 1a / 1a / 2b  
- Hunter: 3.7.4 A / B / B · 3.7.4.1 1a / 2b / 3c · 3.7.4.2 1a / 2b / 3c · 3.7.4.3 1a / 2b / 3c  
- CTI: 3.7.4 B / C / C · 3.7.4.1 3c / 4c / 4d · 3.7.4.2 3c / 4c / 4d · 3.7.4.3 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State **why DTF exists**: see a **pattern**, then **prioritize** what to defend or enrich next.
2. Fill the **classroom mesh** (indicator / infrastructure / behavior + links) and **score** it.
3. Use that score to **name the next seed** — not to run the 3.8 pivot this hour.
4. Explain how DTF **complements** ATT&CK, Diamond, and Kill Chain — it does not replace them.

**Mapped Proficiency Items:**
- K: 3.7.4 – MalasadaTech Defender’s ThreatMesh Framework (DTF)
- T: 3.7.4.1 – Apply DTF to identify patterns and score or prioritize indicators or infrastructure
- T: 3.7.4.2 – Use DTF pattern analysis to guide enrichment and pivoting
- T: 3.7.4.3 – Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain

---

## 1. Key Concepts

There is no SOC 1.5 floor for DTF. This is the **local** framework. ATT&CK IDs are **3.7.1**. Diamond vertices are **3.7.2**. Kill Chain stages are **3.7.3**. **Doing** the infra pivot is **3.8.1**. Which TTPs apply on Harbor is **3.8.2**. A finished actor profile is **3.11**.

**Classroom DTF card (this lesson only, not a live org policy).** If your site posts a real DTF card, use it. The obligation is purpose + mesh + score + next seed + complement — not these numbers.

**Purpose (outline a):** Identify a **pattern** across indicators, infrastructure, and behavior, then **prioritize** what deserves the next defensive or enrichment look.

**Components (outline b) — classroom mesh:**

| Node | Question | Night Owl fill |
|------|----------|----------------|
| **Indicator** | What concrete artifact? | `update.exe`, `powershell -enc`, Run `Updater` |
| **Infrastructure** | What host / domain / IP? | `nightowl-updates.net`, `203.0.113.88:8080` |
| **Behavior** | What did they *do*? | Encoded PS; persist; HTTP GET of the payload |
| **Link** | What ties two nodes? | Same host `WS-JLEE`; Run → `%TEMP%\update.exe`; GET of that file |

**Classroom scoring (0–3 each; sum). Lesson-only.**

| Factor | 0 | 1 | 2 | 3 |
|--------|---|---|---|---|
| **Mesh** | Isolated IOC | Two nodes linked | Three-node cluster | Same mesh on a second host or name |
| **Recency** | Stale / unknown | Seen once | Active this window | Just changed (new persist + GET) |
| **Reach** | Cannot act | Watch only | Can block or hunt one node | Can interrupt the cluster |

**Prioritize** the higher total. A lone vendor claim with no Harbor mesh scores **low**.

**Pattern (outline c):** A pattern is a **link** across indicator + infrastructure + behavior — not a vendor group name, and not one hash sitting alone.

**Guide the next look (outline d):** The high node / weak link is the **seed** you would hand to **3.8.1**. You do **not** RDAP, PDNS, or VT-Relations this hour.

**Complement (outline e):**

| Framework | What it owns | What DTF does **not** do |
|-----------|--------------|--------------------------|
| **ATT&CK (3.7.1)** | Behavior IDs | Assign T-IDs |
| **Diamond (3.7.2)** | Know / don’t-know vertices | Fill Adversary or write a profile |
| **Kill Chain (3.7.3)** | Ordered stages | Replace Delivery / Installation labels |

Same facts, three other views. DTF **clusters and ranks**. It does not absorb them.

**DTF line:**  
`nodes (ind / infra / beh) | links | mesh+recency+reach = total | prioritize? | next seed`

| This lesson | Other |
|-------------|-------|
| Mesh + classroom score + next seed | ATT&CK IDs — **3.7.1** |
| Not Diamond vertices | **3.7.2** |
| Not Kill Chain stages | **3.7.3** |
| Name the seed; do not pivot | **3.8.1** |
| Not “applies on Harbor?” | **3.8.2** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Three-node Night Owl mesh scores high | Vendor T1486 / “APT” scores high with no mesh |
| Next seed = `nightowl-updates.net` | Running RDAP / Silent Push this hour |
| DTF complements the other three | DTF score = nation-state / T-IDs in the score box |

---

## 2. Detailed Walkthrough / Examples

**Classroom report excerpt (Night Owl):**

> WS-JLEE launched `wscript` then `powershell -enc`. A HKCU Run value `Updater` points at `%TEMP%\update.exe`. Zeek shows HTTP GET `update.exe` on 8080 to `nightowl-updates.net` (`203.0.113.88`). Vendor PDF calls the cluster “Night Owl APT” and lists T1486. No encryption was observed here.

### Example 1: Meshed Cluster Scores High (Expected)

| Node | Fill |
|------|------|
| Indicator | `powershell -enc`; Run `Updater`; `update.exe` |
| Infrastructure | `nightowl-updates.net`, `203.0.113.88:8080` |
| Behavior | Encoded PS; persist; HTTP GET payload |
| Links | Same host; Run → Temp path; GET of that file |

| Factor | Score | Why |
|--------|-------|-----|
| Mesh | **3** | Three-node cluster (one host; not yet a second name) |
| Recency | **3** | Persist + GET in this window |
| Reach | **2** | Can hunt / block the domain; not the whole cluster yet |
| **Total** | **8** | **Prioritize** |

**Next seed (not the pivot):** `nightowl-updates.net` → **3.8.1**.  
**Product:** “Harbor mesh (PS-enc + Run + GET + `nightowl-updates.net`) scores 8. Next seed: the domain. Vendor T1486 not meshed.”

### Example 2: Unmeshed Vendor Claim (Lead)

**Draft:** T1486 / “Night Owl APT” → mesh 3, total 9, prioritize first.

**Fail.** No Harbor indicator, no Harbor infra, no observed encrypt behavior. Mesh **0**.  
**Lead:** A PDF label is not a pattern. (T-IDs stay in **3.7.1**. Group names stay out of Diamond Adversary — **3.7.2**.)

### Example 3: DTF as a Replacement (Lead)

**Draft A:** Put `T1059.001` in the score box.  
**Draft B:** “Total 8 = nation-state.”  
**Draft C:** Open RDAP on `nightowl-updates.net` now.

**Fail.** DTF does not assign ATT&CK IDs, does not attribute, and does not *do* the 3.8.1 pivot.  
**Lead:** Complements. Score → seed name → stop.

---

## 3. Hands-On Exercise

**Objective:** Mesh and score the excerpt, name the next seed, and say how DTF sits next to the other three frameworks.

**Use the classroom card above. Lesson-only numbers.**

**Instructions:**

1. One sentence each for Examples 1–3: honest vs fail.
2. **Apply** (3.7.4.1): write a **DTF line** for each.

   - A. The Harbor excerpt (full story).  
   - B. Vendor sentence only: “Night Owl uses ransomware (T1486).”  
   - C. A second Harbor name `login-nightowl.net` with the **same** GET pattern (classroom add-on) — say what happens to **Mesh**.

3. **Guide** (3.7.4.2): for A only, name the **next seed** and why. Do not query RDAP, PDNS, or VT.
4. **Complement** (3.7.4.3): one sentence each — DTF vs ATT&CK, vs Diamond, vs Kill Chain.
5. Do not assign T-IDs. Do not fill Diamond. Do not pick a Kill Chain stage. Do not write a **3.11** profile.

**Expected Outcome:**
- Three example summaries
- Three DTF lines (B = low / no mesh; C = Mesh can go to 3 if it was 2, or stay 3 if already clustered)
- One next-seed line for A
- Three complement sentences
- No 3.8 pivot, no actor profile

---

## 4. Knowledge Check

1. What is DTF **for**, in one sentence?
2. What must a **DTF line** include besides a total?
3. Why does vendor T1486 **not** score high on this card?
4. What does a high score tell you to do **this hour** — and what does it tell you **not** to do?
5. Give one way DTF **complements** ATT&CK, Diamond, **or** Kill Chain without replacing it.

---

## 5. Summary

- Mesh what you can link. Score with the classroom factors. Prioritize the cluster, not the PDF label.
- Name the next seed. Stop. **3.8.1** does the pivot.
- DTF ranks; ATT&CK names behavior; Diamond shows gaps; Kill Chain orders stages.
- Next: **3.8.1** Identifying additional adversary infrastructure from seed indicators.

---

## 6. References & Further Reading

- Related modules:
  - 3.7.3 – Cyber Kill Chain in CTI (previous)
  - 3.7.1 – ATT&CK for CTI
  - 3.7.2 – Diamond Model in CTI
  - 3.8.1 – Infrastructure pivot from a seed (next)
- `modules/shared/frameworks/` (reference; empty stand-in — do not copy here)
- Classroom DTF card in this guide (lesson-only)
