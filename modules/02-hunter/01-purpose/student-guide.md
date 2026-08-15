# Module 2.1 – Purpose of Threat Hunting

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.1.1 B / C / C · 2.1.1.1 3c / 4c / 4c · 2.1.1.2 3c / 4c / 4d  
- SOC: 2.1.1 A / B / B · 2.1.1.1 1a / 2b / 3c · 2.1.1.2 1a / 2b / 3c  
- CTI: 2.1.1 A / B / B · 2.1.1.1 1a / 2b / 3c · 2.1.1.2 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State the purpose of threat hunting in the security program.
2. Explain how hunting finds malicious or suspicious activity that existing mechanisms missed.
3. Distinguish a **detection gap** from a **visibility gap**.
4. Identify examples of activity that existing controls might miss.

**Mapped Proficiency Items:**
- K: 2.1.1 – Purpose of Threat Hunting
- T: 2.1.1.1 – Explain the purpose of threat hunting in the context of the security program
- T: 2.1.1.2 – Identify examples of activity that existing controls might miss

---

## 1. Key Concepts

### 1.1 Purpose in the Security Program

Threat hunting is a **proactive** search for malicious or suspicious activity that existing security mechanisms did not surface — and for the **gaps** that let that happen.

It sits next to SOC and CTI. It does not replace them.

| Function | What it is paid to do | When it usually starts |
|----------|----------------------|------------------------|
| **SOC** | Triage and respond to what the stack already raised | An alert, a ticket, a reported incident |
| **CTI** | Turn questions into judged intelligence | A requirement or a lead that needs analysis |
| **Hunt** | Look for what the stack did *not* raise, and name the gap | A hypothesis, an intel lead, or a known blind spot — *before* (or without) an alert |

**Most critical distinction for daily work:**  
If the only input is yesterday’s alert queue, you are doing SOC work. Calling it a hunt does not change the job.

Hunting earns its seat in the program when it does two things:

1. Finds **activity** that detections, preventions, or the ticket process missed.
2. Returns a **gap** the program can close (a new detection, a logging hole, a coverage exception) — or a reasoned “we looked; this path is quiet.”

A lead is not an incident. A quiet hunt is not a failure if you can say what you could and could not see.

### 1.2 Activity Existing Mechanisms Miss

“Existing security mechanisms” means the controls you already run: EDR, SIEM detections, email/web filters, preventions, playbooks, and the SOC queue. They miss activity for two different reasons. Name the reason. Do not treat them as the same problem.

| Gap | What is true | What hunt can still do | What “fix” looks like (later work) |
|-----|----------------|------------------------|------------------------------------|
| **Detection gap** | The telemetry exists. No rule, analytic, or process turned it into a useful alert. | Search the data you already have. Show the missed pattern. | A detection, a tuned rule, a playbook change |
| **Visibility gap** | The telemetry does not exist, is incomplete, or is not where you can query it. | State what you *cannot* see. Bound the hunt. Do not invent coverage. | Sensor, log source, retention, or scope change |

**Detection gap example:** Process and DNS logs are in the SIEM. A host periodically resolves a lookalike name. No analytic fires. Hunt can find the rows.

**Visibility gap example:** A lab VLAN is excluded from EDR and has no DNS logging. Hunt cannot “prove quiet” there. The finding is the hole, not a clean bill of health.

Common failure: people say “no hits” when they had **no visibility**. That is not the same sentence.

| Signal | Points toward |
|--------|----------------|
| You can show the events; nothing alerted | Detection gap |
| The host, network, or time window is not in the data | Visibility gap |
| Prevention blocked it and SOC already has the ticket | Not a hunt miss — the mechanism worked |
| You reran the same alert and called it a hunt | Not hunting |

How to write persistence or privilege-escalation hunts is the next unit. Here you only need: those classes of activity (and many others) are *why* hunt exists — because controls miss them.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Missed Activity, Then the Gap)

**Program context:** EDR is on user workstations. SIEM has DNS and TLS. SOC is current on the overnight queue. No open incident for finance.

**Hunt question:** Are any finance workstations talking to the “fake update CDN” names from this week’s report, even if nothing alerted?

| What hunt did | What it showed |
|---------------|----------------|
| Searched DNS/TLS for the report names (last 7 days, finance VLAN) | `10.10.22.17` resolved and opened TLS to `update.not-a-real-cdn.example` on 8443, nightly, 14 days |
| Checked the SOC queue and EDR preventions | No ticket. No block. No detection name. |
| Named the gap | **Detection gap:** the rows were in the SIEM; nothing turned them into an alert. EDR did not prevent the outbound session. |

**Interpretation:**  
This is hunting. The stack was “green.” The activity was still there. The purpose is not a cooler ticket — it is finding what existing mechanisms missed and handing SOC/IR a lead plus a gap. Do not call the 14-day beacon an incident until IR says so. Do not skip the gap: “we found a host” without “the DNS/TLS pattern never alerted” leaves the program blind next week.

### Example 2: Alert Queue Labeled “Hunt” (Lead)

A chat message to the hunt channel:

> Morning hunt: re-pull all High EDR alerts from last night, mark TP/FP, close the queue. Status: hunt complete.

**Interpretation:**  
This is **SOC triage**. The activity was already raised by an existing mechanism. Re-working the queue does not identify missed activity and does not identify a detection or visibility gap. Treat the queue as SOC work. If something in those alerts *suggests a path the stack does not cover* (for example, the same parent process on a server class that has no EDR), *that* path can become a hunt. The queue itself is not the hunt.

### Example 3: “No Hits” on a Blind Segment (Lead)

**Write-up A**

> Hunted ransomware on the lab VLAN. Zero EDR hits. Environment is clean.

**Write-up B**

> Question: is the lab VLAN showing the same installer hash / DNS names as this week’s ransomware reporting?  
> Lab VLAN is **excluded from EDR** and has **no DNS logging**. We cannot see process or resolution data there.  
> Finding is a **visibility gap**, not a clean bill of health. Recommend: do not claim “no activity.” Ask for logging or a scoped sensor before the next pass. Workstations *with* DNS (Building C) had no matching names in 7 days — that statement is limited to where we can see.

**Interpretation:**  
A fails the purpose. “Zero hits” on a segment with no telemetry is a visibility gap dressed up as a result. B does the job: it explains hunt in the program (answer a question the stack cannot already answer), and it identifies what existing controls cannot see. Same topic, only B is hunting.

---

## 3. Hands-On Exercise

**Objective:** Practice stating the purpose and spotting missed activity vs the wrong job.

**Instructions:**

1. Review the three examples above and write a one-sentence summary for each (was it hunting, and what was missed — activity, a gap, or neither?).
2. For each item below, say whether it is **hunting**, **SOC / already-covered work**, a **detection gap**, a **visibility gap**, or **not enough to claim quiet**. Give one reason.
   - Re-triaging last night’s High EDR alerts
   - DNS rows in the SIEM show a 14-day lookalike beacon; no analytic fired
   - A server class is excluded from EDR and has no process logging
   - Prevention blocked a known malware hash and opened a SOC ticket
   - “Lab is clean — we have no EDR data from lab”
   - “Explain to the SOC lead why we are hunting finance TLS when the queue is empty”
3. In four sentences or fewer, explain the **purpose of threat hunting in this security program** to a SOC lead who thinks hunt is “extra triage.” Include both missed activity and gaps.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- A purpose statement that names missed activity *and* detection/visibility gaps — not “we pull more alerts”

---

## 4. Knowledge Check

1. What is the purpose of threat hunting in the security program?
2. What is the difference between a detection gap and a visibility gap?
3. Why is re-working last night’s alert queue not hunting?
4. Identify: DNS and TLS for a lookalike name are in the SIEM; nothing alerted for 14 days.
5. Identify: “Zero EDR hits on the lab VLAN” when that VLAN is excluded from EDR.

---

## 5. Summary

- Hunt looks for malicious or suspicious activity that existing mechanisms did not surface.
- It also names **detection gaps** (data exists, no useful alert) and **visibility gaps** (you cannot see).
- In the program: SOC works what the stack raised; hunt works what it did not; CTI judges and directs questions.
- A lead is not an incident. “No hits” is not “clean” if you had no visibility.
- Relabeling triage as a hunt does not fulfill the purpose.

---

## 6. References & Further Reading

- Related modules:
  - 2.2 – Attacker techniques (next)
  - 2.3 – Hunt methodology
  - 3.1.1 – Data, information, and intelligence
- Local hunt charter / intake process (when published)
- Internal detection-engineering hand-off (when published)
