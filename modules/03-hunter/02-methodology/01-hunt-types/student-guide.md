# Module 2.2.1 – Hunt Types

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.2.1 B / C / C · 2.2.1.1 3c / 4c / 4c · 2.2.1.2 3c / 4c / 4c · 2.2.1.3 3c / 4c / 4c · 2.2.1.4 3c / 4c / 4c  
- SOC: 2.2.1 A / B / B · 2.2.1.1 1a / 1a / 2b · 2.2.1.2 1a / 1a / 2b · 2.2.1.3 1a / 1a / 2b · 2.2.1.4 1a / 1a / 2b  
- CTI: 2.2.1 A / B / B · 2.2.1.1 1a / 1a / 2b · 2.2.1.2 1a / 1a / 2b · 2.2.1.3 1a / 1a / 2b · 2.2.1.4 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the four hunt types and the input that starts each one.
2. Tell a **reactive hunt** apart from SOC work on an existing alert.
3. Tell a **hypothesis-driven hunt** apart from an **anomaly-based hunt**.
4. Execute a hunt *by type*: pick the type, take the first search, and say what you will hand back.

**Mapped Proficiency Items:**
- K: 2.2.1 – Hunt types
- T: 2.2.1.1 – Execute an intel-driven hunt
- T: 2.2.1.2 – Execute a hypothesis-driven hunt
- T: 2.2.1.3 – Execute a reactive hunt
- T: 2.2.1.4 – Execute an anomaly-based hunt

---

## 1. Key Concepts

### 1.1 Four Hunt Types

Hunt type is named from **what started the work**, not from the tool and not from the chat title.

How to write a tight hypothesis, set scope, and rank hunts is the next lesson (**2.2.2**). Here you only need the four types and how execution *starts* for each.

| Type | Starts from | Question you can actually search | First execute move |
|------|-------------|----------------------------------|--------------------|
| **Intel-driven** | A report, bulletin, or IOC/TTP set someone else produced | Are *these* objects or named behaviors here? | Take the objects. Search the places you can see. Bound the window. |
| **Hypothesis-driven** | An if/then *you* can test: if X is true, we should see Y | Do we see Y in this scope? | Write Y so a query can fail. Search for Y. Keep or kill the story. |
| **Reactive** | A spark that is not already finished SOC work: IR ask, near-miss, odd ticket | Given this spark, is there *related* activity the stack did not raise? | Expand around the spark (peers, parent, nearby time). Do not re-close the original ticket and call it done. |
| **Anomaly-based** | A measurable baseline and a deviation detections ignore | What is new, rare, or off-baseline? | Name the baseline. Name the deviation. Search peers. |

**Most critical distinction for daily work:**  
The label in the hunt channel is not the type. Type follows the input.

A hunt can change type mid-flight (intel objects go quiet, so you form a hypothesis). Say so. Do not keep the old label out of habit.

Purpose still applies (module **2.1**): you are looking for activity existing mechanisms missed, and for the gap. Type is *how you started*. It is not a new purpose.

### 1.2 Execute by Type (and What Is Not a Type)

**Execute**, in this lesson, means four sentences you can say out loud before you open the SIEM:

1. **Type** — named from the input.
2. **First search** — what you will query, where, and for how long.
3. **Quiet** — what “no hits” is allowed to mean (only where you had visibility).
4. **Hand-back** — lead, gap, or reasoned quiet. A lead is not an incident.

| Trap | Why it fails | What to do instead |
|------|----------------|--------------------|
| Re-pull last night’s High queue as a “reactive hunt” | The mechanism already raised that work. That is SOC. | If the *spark* suggests unalerted peers or a path with no coverage, hunt *that*. The queue itself is not the hunt. |
| Paste a report title and call it intel-driven | You never searched the objects. | Execute: names, hashes, or named behaviors into DNS/TLS/process — then report hits or bounded quiet. |
| “I hypothesize attackers use scheduled tasks” with no Y | Not yet hypothesis-driven. Nothing can fail. | Either write a testable Y (**2.2.2** will go deeper) or switch to anomaly-based if you have a baseline (new tasks vs 30-day none). |
| “Looks weird” with no baseline | Not anomaly-based. | Name what “normal” was. No baseline → you do not have this type yet. |
| Intel objects used to invent a broader if/then, still labeled intel-driven | You changed type. | Say it: intel *seeded* a **hypothesis-driven** hunt. |

How to extract TTPs from a CTI report is **2.4**. How to hunt persistence/privesc is **2.6**. Online enrichment is **2.3**. Do not pull those in here.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Intel-Driven Execute)

**Input:** This week’s internal bulletin lists `update.not-a-real-cdn.example` and a lookalike registrar pattern. No open incident.

**Type:** **Intel-driven.** The objects came from intel, not from a hypothesis you wrote and not from a SOC ticket.

| Execute step | What the hunter did |
|--------------|---------------------|
| First search | DNS and TLS, last 7 days, user + finance VLANs, exact name and close lookalikes from the bulletin |
| Result | `10.10.22.17` resolved and opened TLS to that name on 8443, 14 nights. No detection name. No ticket. |
| Quiet / visibility | Lab VLAN still has no DNS — do not claim lab is clean. |
| Hand-back | Lead on `10.10.22.17` plus a **detection gap**. Type stays intel-driven. |

**Interpretation:**  
This is how you execute an intel-driven hunt: search the named objects, bound what you could see, return a lead and a gap. You did not write a new if/then. You did not re-triage an alert. Do not call the 14-day activity an incident until IR says so.

### Example 2: Queue Labeled “Reactive Hunt” (Lead)

A chat message:

> Reactive hunt: re-pull all High EDR alerts from last night, mark TP/FP, close the queue.

Compare a real reactive start from the same morning:

> IR: `10.10.22.17` had the bulletin name last week. Hunt **peer finance workstations** for the same parent process and JA3 over 14 days. Those peers never alerted.

**Interpretation:**  
The first message is **SOC triage**. The activity was already raised. Calling it reactive does not change the type — it is not a hunt type at all.

The second is a **reactive hunt**. The spark is the IR host. Execution looks for *related* activity the stack did not raise. You are not closing the original ticket as the hunt. If you later drop the host and instead test “finance workstations talk to lookalike CDNs after hours,” say you switched to **hypothesis-driven**.

### Example 3: “Anomaly Hunt” That Is a Hypothesis (Lead)

**Write-up A**

> Anomaly hunt: I hypothesize attackers persist with scheduled tasks. Zero hits. Clean.

**Write-up B**

> Anomaly-based: Building C Windows servers had **no** new scheduled tasks in 30 days (baseline). Last 24 hours, `SRVpay02` created two tasks as `SYSTEM` at 02:14. No analytic. Peer servers: none. Lab servers: **no process logging** — visibility gap, not quiet.

**Interpretation:**  
A is not anomaly-based (no baseline) and is a weak hypothesis (no testable Y, “zero hits” with no scope). B executes **anomaly-based**: baseline, deviation, peers, honest visibility. If A had said “if staging uses new SYSTEM tasks after hours, we should see task-create events on servers with no 30-day history,” that would be **hypothesis-driven** — and it would still need a search that can fail. Depth on writing that sentence is **2.2.2**.

---

## 3. Hands-On Exercise

**Objective:** Practice naming the type and executing the first move.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (type, or not a hunt, and what was executed).
2. For each item below, name the **type** (**intel-driven**, **hypothesis-driven**, **reactive**, **anomaly-based**) or **not a hunt**. Give one reason.
   - Weekly bulletin hashes searched in the last 7 days of EDR
   - Re-triaging last night’s High EDR alerts
   - IR host from last week; you search unalerted peers for the same parent process
   - “If finance laptops beacon to lookalike CDNs after 21:00, we should see repeated DNS+TLS to those names”
   - New outbound 8443 from a VLAN that had none in 30 days; no analytic
   - “Anomaly hunt: attackers use scheduled tasks” with no baseline and no Y
3. Pick **one intel-driven** item and **one anomaly-based** item from the list. In four sentences each, execute: type, first search, what quiet is allowed to mean, what you hand back.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- Two four-sentence execute blocks that name type and first search — not a 2.2.2 hunt plan

---

## 4. Knowledge Check

1. What are the four hunt types, and what input starts each one?
2. Why is re-working last night’s alert queue not a reactive hunt?
3. How is a hypothesis-driven hunt different from an anomaly-based hunt?
4. You are given a bulletin of domain names and you search DNS/TLS for those names. Which type are you executing, and what do you hand back if you find rows and no alert?
5. You have a 30-day baseline of “no new SYSTEM scheduled tasks on Building C servers” and overnight two appear on one host. Which type, and what must you say about a segment with no process logging?

---

## 5. Summary

- Four types: **intel-driven**, **hypothesis-driven**, **reactive**, **anomaly-based**. Type follows the input.
- Execute = type + first search + honest quiet + hand-back (lead, gap, or bounded quiet).
- Reactive ≠ SOC. Anomaly ≠ “looks weird.” Hypothesis ≠ a slogan with no Y.
- Changing type mid-hunt is allowed if you say so.
- Writing, scoping, and prioritizing the hunt is **2.2.2**.

---

## 6. References & Further Reading

- Related modules:
  - 2.1 – Purpose of Threat Hunting
  - 2.2.2 – Hunt development concepts (next)
  - 2.3 – Online tools and enrichment
  - 2.4 – CTI for hunters
- Local hunt charter / intake process (when published)
