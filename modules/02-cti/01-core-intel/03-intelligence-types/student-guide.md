# Module 3.1.3 – Intelligence Types

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- CTI: 3-level (B/3c) → 5-level (C/4c) → 7-level (C/4c)  
- Hunter: A/1a → B/2b → B/3c  
- SOC: awareness only (A / 1a)  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Define strategic, operational, tactical, and technical intelligence.
2. State what question each type is built to answer and who usually consumes it.
3. Correctly classify an intelligence product or requirement by type.
4. Spot a product that is labeled as one type but is actually another.

**Mapped Proficiency Items:**
- K: 3.1.3 – Intelligence types (strategic, operational, tactical, technical)
- T: 3.1.3.1 – Classify an intelligence product or requirement by type

---

## 1. Key Concepts

### 1.1 Four Types, Four Jobs

Type is about the **decision the product exists to support**, not the file format and not how “important” it sounds.

| Type | Question it answers | Horizon | Typical consumer | Typical form |
|------|---------------------|---------|------------------|--------------|
| **Strategic** | What should leadership change about risk, investment, or posture? | Months to years | Executives, program owners | Assessment of intent, capability, and implication for the mission |
| **Operational** | How should we run this campaign, incident, or hunt over days to weeks? | Days to weeks | IR leads, hunt leads, CTI leads | Campaign picture, sequencing, priorities, resource focus |
| **Tactical** | What should a responder or hunter do *now* on this activity? | Hours to days | SOC, hunt, IR | Judged next action on a host, name, or cluster |
| **Technical** | What are the observable mechanics we can detect or pivot on? | Immediate, reusable | Detections, SOC, hunt, malware analysts | Hashes, JA3, SNI, mutex, C2 pattern, YARA-ready detail |

**Most critical distinction for daily work:**  
A long PDF is not automatically strategic. A hash is not automatically intelligence. Type follows the question.

These types stack. The same campaign can produce all four. They are not lifecycle stages. Collection vs analysis is a *stage*. Strategic vs tactical is *what kind of answer* you are producing.

How this sits on the last two modules:

| Earlier idea | How type uses it |
|--------------|------------------|
| Data / information / intelligence | Type applies to **intelligence** (and to the *requirement* that asks for it). A raw IOC list is still data. |
| Lifecycle | You can collect technical data in service of a strategic question. Stage ≠ type. |

### 1.2 Strategic and Operational

**Strategic intelligence** judges long-horizon risk. It tells a decision-maker whether to fund a control, accept a threat, or change a program. It names implication, not a ticket action.

| Signal | Points toward strategic |
|--------|-------------------------|
| Audience is leadership or a program owner | Yes |
| Horizon is posture, budget, or annual risk | Yes |
| Product is a host isolate or a block list | No — that is tactical or technical |
| Product only restates a news headline | No — that is information, not strategic intelligence |

**Operational intelligence** judges how to run a *body of work*: this incident, this hunt series, this campaign window. It sequences effort. It does not set five-year posture, and it is not a single-host action.

| Signal | Points toward operational |
|--------|---------------------------|
| “Where do we put hunt/IR time this week?” | Yes |
| Campaign grouping, phasing, or coverage gaps | Yes |
| One host, one ticket, one block | No — tactical |
| Board-level investment question | No — strategic |

Common failure: calling every campaign brief “strategic” because it mentions a nation-state.

### 1.3 Tactical and Technical

**Tactical intelligence** tells an operator what to do about *this* activity: isolate, hunt this cluster, watch this window. It is still intelligence — it has a requirement, a judgment, and a decision.

**Technical intelligence** describes *how the thing works* in observables: hashes, JA3, SNI, ports, mutexes, implant build details. It enables detection and pivoting. It does not, by itself, tell leadership what to fund or tell SOC which host to isolate.

| Signal | Tactical | Technical |
|--------|----------|-----------|
| Answers “what do we do about this activity?” | Yes | No |
| Answers “what can we detect or pivot on?” | Supporting only | Yes |
| A judged isolate / hunt recommendation | Yes | No |
| A field list, fingerprint, or sample note with no action | No | Yes (if analyzed; else it is still data) |

Common failure: shipping a hash dump and calling it tactical intelligence. That is technical *data* until you analyze it. Even then, a clean hash list is technical, not tactical, until someone judges an action.

If you are unsure, ask: **what decision does this unlock?**  
Posture → strategic. Campaign effort → operational. Immediate action → tactical. Detection/pivot mechanics → technical.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (One Campaign, Four Types)

**Requirement set (already given):** Understand the “fake update CDN” activity that showed up this week.

| Product | Type | Why |
|---------|------|-----|
| “This cluster is a financially motivated access broker. We assess it will keep targeting our finance VLAN this quarter; fund the extra TLS sensor, do not wait for next year’s cycle.” | **Strategic** | Posture / investment decision |
| “Run a 10-day hunt series: lab VLANs first, then finance. IR owns confirmed victims; CTI updates the campaign picture daily.” | **Operational** | How to run the body of work |
| “Isolate 10.10.22.17; hunt the same SNI/cert pair fleet-wide this shift.” | **Tactical** | Immediate action on this activity |
| “SNI `update.not-a-real-cdn.example`, TLS 1.0 + RC4 on 8443, JA3 `a0e9f5…`. Same JA3 on two lab VLANs.” | **Technical** | Observables for detect/pivot |

**Interpretation:**  
Same campaign, four products, four decisions. Do not brief the JA3 row to a director and call it strategic. Do not paste the investment paragraph into a SOC ticket and call it tactical.

### Example 2: “Strategic APT Brief” That Is Technical Data (Lead)

A slide titled **STRATEGIC INTEL – NEW APT**:

> Nation-state group (blog name). Block these now:  
> `45.76.12.88`  
> `update.not-a-real-cdn.example`  
> `6734f37431670b3ab4292b8f60f29984`  
> Source: public blog, posted today.

**Interpretation:**  
The title says strategic. The content is **technical data** (three indicators) plus a claim. There is no posture judgment, no campaign plan, and “block these now” is an instruction without a supported tactical assessment. Classify what it *is*, not what the cover says. Treat it as a **lead**: if the real question is strategic, you still have to produce a strategic answer. If the real question is “are we hit?,” you need tactical/technical work first.

### Example 3: Two Requirements, Same Indicators (Lead)

**Requirement A**

> Leadership: do we accept this ransomware family’s risk against our Windows 10 image, or do we buy the extra EDR pack this quarter?

**Requirement B**

> SOC: if this family is in the environment tonight, what do we hunt and what do we isolate on?

**Write-up shipped for both**

> Hash `6734f374…` and installer name `update.exe`. Three public reports. TIP updated.

**Interpretation:**  
A is a **strategic** requirement. B is a **tactical** requirement (with a **technical** layer). The write-up is a technical indicator dump. It does not answer A or B. Same observables can support both types — but only after you write the product that matches the question. Classifying the *requirement* and classifying the *product* are separate steps. Here they do not match.

---

## 3. Hands-On Exercise

**Objective:** Practice naming the four types and classifying products and requirements.

**Instructions:**

1. Review the three examples above and write a one-sentence summary for each (what type was claimed vs what type it actually was).
2. Classify each item below as **strategic**, **operational**, **tactical**, or **technical**. Give one reason. If it is not intelligence yet, say that too.
   - “Fund east-west DNS logging this year; this access-broker set will keep hitting finance.”
   - “This week: hunt lab VLANs first, then finance; IR takes confirmed victims.”
   - “Isolate 10.10.22.17 and hunt that JA3 this shift.”
   - A one-page note of hashes, JA3, SNI, and port with no recommended action
   - “Are we going to keep accepting last year’s phishing loss rate?”
   - A STIX bundle imported from a vendor and not yet reviewed
3. Take the technical row in Example 1 (SNI + JA3 + port). Write:
   - one **tactical** sentence that answers: *What should SOC do about 10.10.22.17 tonight?*
   - one **strategic** sentence that answers: *Does this activity change what we fund this quarter?*

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six classifications with a reason each
- A clear tactical sentence and a clear strategic sentence from the same technical facts

---

## 4. Knowledge Check

1. What question does strategic intelligence answer that tactical intelligence does not?
2. What is the difference between tactical intelligence and technical intelligence?
3. Why is a long “APT” PDF not automatically strategic?
4. Classify: “Run a 10-day hunt series on the fake-update cluster; IR owns victims.”
5. Classify: “SNI `update.not-a-real-cdn.example`, JA3 `a0e9f5…`, port 8443.”

---

## 5. Summary

- Four types: strategic, operational, tactical, technical. Type follows the decision, not the filename.
- Strategic = posture / investment. Operational = how to run the campaign or hunt. Tactical = what to do now. Technical = observables for detect and pivot.
- The same campaign can produce all four. Types are not lifecycle stages.
- A labeled “strategic brief” that is only indicators is technical data, not strategy.
- Classify the requirement and the product separately. If they do not match, you are not done.

---

## 6. References & Further Reading

- Related modules:
  - 3.1.2 – Intelligence lifecycle (previous)
  - 3.1.4 – Intelligence requirements (next)
  - 3.1.5 – Ensuring intelligence is actionable
  - 3.1.6 – Tailoring output to the audience
- Internal product catalog / naming (when published)
- Joint / ODNI primers on intelligence types (use the local copies)
