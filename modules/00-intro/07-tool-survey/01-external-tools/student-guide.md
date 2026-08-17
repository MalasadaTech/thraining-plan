# Module 3.3.2 – External Tools

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.3.2 A / B / B · 3.3.2.1 1a / 2b / 3c  
- Hunter: 3.3.2 B / C / C · 3.3.2.1 3c / 4c / 4d  
- CTI: 3.3.2 B / C / C · 3.3.2.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State the **purpose, strength, and weakness** of VirusTotal, AnyRun, Silent Push, and URLScan.
2. Say **when** each belongs in the intelligence process.
3. **Select** the right tool for a need and reject the neighbor.
4. **Enrich or pivot once** (classroom: first query + one hop).

**Mapped Proficiency Items:**
- K: 3.3.2 – External tools (VirusTotal, AnyRun, Silent Push, URLScan)
- T: 3.3.2.1 – Select the appropriate external tool and perform enrichment or pivoting

---

## 1. Key Concepts

These four are **external**. Check the **internal TIP** first if the question is “have *we* seen this?” (**3.3.1**). Hunt-lead → SIEM/Zeek conversion is **2.3.1**. VT Relations/Behavior graphs are **3.9**.

**Purpose, strengths, weaknesses (outline a) — classroom card:**

| Tool | Purpose | Strength | Weakness |
|------|---------|----------|----------|
| **VirusTotal** | Multi-engine file / URL / hash / IP look-up | Fast reputation + related *files* on a hash | Public; not historical PDNS; not a full sandbox story |
| **AnyRun** | Detonate a **sample** and watch behavior | Process tree, dropped files, live C2 from *this* run | Needs a file; evadable; not infra history |
| **Silent Push** | Passive DNS / infra clustering | Historical resolutions, sibling domains | Not a detonation; not a page screenshot |
| **URLScan** | Scan a **URL/page now** | Redirects, DOM, screenshot, contacted hosts *this load* | Not PDNS history; not file behavior |

**When in the intel process (outline b):**

| Need | First external tool |
|------|---------------------|
| Hash / file reputation, “what else submitted this hash?” | **VirusTotal** |
| You have a binary and need *behavior* | **AnyRun** |
| Domain / IP *history* or cluster | **Silent Push** |
| Live phishing / URL appearance | **URLScan** |
| “Have we seen it internally?” | **Not these** — **3.3.1** TIP |

**Classroom pivot (task 2 — one hop, not 3.9):**

| Tool | First query | One legal hop |
|------|-------------|----------------|
| VT | Hash `6734f374…` | One **contacted domain** or **communicating file** |
| AnyRun | Submit `update.exe` | One **dropped hash** or **C2 host** from the run |
| Silent Push | `nightowl-updates.net` | One **historical A** or **sibling domain** |
| URLScan | The live URL | One **redirect** or **contacted host** from that scan |

A 12-node Relations graph is **3.9**. A SIEM query from the hop is **2.3.1**.

| This lesson | Other |
|-------------|-------|
| Select + one hop | Internal TIP retrieve — **3.3.1** |
| Not hunt-to-Zeek | **2.3.1** |
| Not VT Relations depth | **3.9** |
| Not imphash / ssdeep | **3.4** |

The tasks: a **select line** and a **pivot line**.

`need | tool | rejected neighbor | why`  
`tool | first query | one hop | what that hop is for`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Hash → VT, one communicating file | URLScan for PDNS history |
| Domain history → Silent Push | AnyRun with no sample |
| Live phish URL → URLScan | 12-hop VT Relations (**3.9**) |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Hash → VT + One Hop (Expected)

**Need:** What do vendors say about `6734f374…`, and what else talks like it?

**Select:** **VirusTotal**. Reject Silent Push (no domain question yet). Reject AnyRun until you *have* the file.  
**Pivot:** Query the hash → open one **contacted domain** (classroom: `nightowl-updates.net`). Stop.  
**Then:** If you need *history* on that domain, **next** tool is Silent Push — that is a *second* select, not this hop.

### Example 2: URLScan for History (Lead)

**Need:** What IPs has `nightowl-updates.net` used this year?

**Wrong:** URLScan (that is *this page load*).  
**Select:** **Silent Push**. Reject URLScan. Reject VT as the *first* tool for historical PDNS.  
**Pivot:** Query the domain → one **historical A** or sibling.  
**Lead:** Right IOC type (domain). Wrong tool.

### Example 3: AnyRun with No File (Lead)

**Need:** Behavior of Night Owl. Analyst has only the SNI, no binary.

**Wrong:** AnyRun (nothing to detonate).  
**Select:** Silent Push (infra) and/or VT *URL/domain* look-up. If a sample appears later, then AnyRun.  
**Lead:** “Advanced” is not “open the sandbox anyway.”

---

## 3. Hands-On Exercise

**Objective:** Pick the tool and name one hop.

**Use the classroom card.** Do not convert hops into Zeek queries.

**Instructions:**

1. One sentence each for Examples 1–3: tool + rejected neighbor.
2. **Select** (task 1): `need | tool | rejected | why`.

   - A. Live invoice URL the user still has open.  
   - B. You have `update.exe` from WS-JLEE Temp. Need process tree + dropped files.  
   - C. “Have we seen this JA3 on Harbor before?”  
   - D. Domain cluster: what else shares infra with `nightowl-updates.net`?

3. **Pivot** (task 2): for **A**, **B**, and **D**, write `tool | first query | one hop | what for`.
4. Do not open the internal TIP as an *external* tool (C should point at **3.3.1**). Do not draw a Relations graph. Do not write a SIEM query.
5. One hop. If you need a second tool, say so as a *new* select — do not chain 3.9.

**Expected Outcome:**
- Three example summaries
- Four select lines (C = TIP, not these four)
- Three pivot lines
- No Zeek query, no Relations graph

---

## 4. Knowledge Check

1. Give **one strength and one weakness** for each of the four tools.
2. When do you pick **Silent Push** over **URLScan**?
3. What is a classroom **one-hop** on VT, and what is **3.9** instead?
4. Why is “have we seen this internally?” not an external-tool select?
5. Where do you turn a hop into a **hunt / SIEM** query?

---

## 5. Summary

- Four tools: purpose, strength, weakness, when.
- Select + reject neighbor. One hop. Not the TIP, not 3.9, not 2.3.1.
- This closes cluster **3.3**. Next: **3.4** file similarity / hashing.

---

## 6. References & Further Reading

- Related modules:
  - 3.3.1 – Internal TIP (previous)
  - 2.3.1 – Tool capabilities for hunting
  - 3.9 – VirusTotal / platform depth
  - 3.4 – File similarity and hashing
- Local tool SOP / licenses (optional)
