# Instructor Guide – Module 2.1 – Purpose of Threat Hunting

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.1.1 B / C / C · 2.1.1.1 3c / 4c / 4c · 2.1.1.2 3c / 4c / 4d  
- SOC: 2.1.1 A / B / B · 2.1.1.1 1a / 2b / 3c · 2.1.1.2 1a / 2b / 3c  
- CTI: 2.1.1 A / B / B · 2.1.1.1 1a / 2b / 3c · 2.1.1.2 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach why hunt exists in the security program: find malicious or suspicious activity that existing mechanisms missed, and identify detection and visibility gaps. Make students practice explaining that purpose and spotting examples of missed activity.

**Key Teaching Points:**
- Hunt is proactive. The input is not “the alert fired.”
- Two jobs: missed **activity**, and the **gap** that allowed it.
- Detection gap ≠ visibility gap. “No hits” on a blind segment is not clean.
- SOC / hunt / CTI are different seats. Relabeling triage is not hunting.
- Stay out of persistence/privesc how-to (2.2) and hunt types (2.3). Point forward if asked.

**Common Student Challenges:**
- Equating hunt with “deeper SOC” or “more alerts.”
- Collapsing detection gaps and visibility gaps.
- Claiming a segment is clean when they had no telemetry.
- Jumping into technique catalogs (scheduled tasks, token theft) instead of purpose.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard or shared doc for live sorting
- Answer key (this guide)

---

## Learning Objectives

1. State the purpose of threat hunting in the security program.
2. Explain how hunting finds malicious or suspicious activity that existing mechanisms missed.
3. Distinguish a **detection gap** from a **visibility gap**.
4. Identify examples of activity that existing controls might miss.

**Mapped Items:**
- K: 2.1.1 – Purpose of Threat Hunting
- T: 2.1.1.1 – Explain the purpose of threat hunting in the context of the security program
- T: 2.1.1.2 – Identify examples of activity that existing controls might miss

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | “What is hunt for?” on the board before the definition |
| Purpose in the program         | 12 min   | SOC vs hunt vs CTI table |
| Missed activity and two gaps   | 12 min   | Detection vs visibility |
| Walkthrough Examples           | 14 min   | Interactive; students speak first |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~68 min** | Stretch Example 3 if the room still says “no hits = clean” |

---

## Detailed Teaching Notes

### 1. Purpose in the Security Program

**Talking Points:**
- Ask the room for a one-line definition before you show the table. Write the wrong ones (“deeper alerts,” “when SOC is bored”) and leave them up until the examples kill them.
- Hunt 3 is already at principles (B / 3c). Push them to explain *to SOC and CTI*, not to recite a slogan.
- A quiet hunt that documents a gap is a valid program output.

**What to emphasize:**
- Two clauses in the purpose: missed activity **and** gaps.
- A lead is not an incident. Do not let IR language take over.

**Questions to ask the class:**
- “If the queue is empty, is hunt done for the day?”
- “What do you owe the program besides a host name?”

### 2. Activity Existing Mechanisms Miss

**Talking Points:**
- Detection gap: data yes, alert no.
- Visibility gap: data no. Hunt’s honest product is the hole.
- Mechanisms that *worked* (block + ticket) are not hunt findings.

**What to emphasize:**
- Do not teach how to hunt scheduled tasks or privesc. Name them only as *classes* of activity controls miss. Depth is 2.2.
- Hunt types (intel-driven vs hypothesis) are 2.3. If someone asks “how do we pick the question?,” park it.

**Question to ask:**  
“Can you show me the events, or can you only show me the absence of a sensor?”

### 3. Examples

Work through all three interactively. Ask students to label hunting vs not, and gap type, before you read the interpretation.

**Extra point for Example 1:**  
Green queue + 14-day beacon + detection gap. If they only remember one thing, make it this.

**Extra point for Example 2:**  
The word hunt in the chat title is the trap. Same family as the CTI “INTEL” paste: the label is not the job.

**Extra point for Example 3:**  
Write-up A will be popular. Force the sentence: you cannot claim clean where you cannot see.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- Review answers as a group afterward. Do not collect a grade.

**What good answers look like:**

**Summaries:**
- Example 1: Hunting — finance host beaconed 14 days; detection gap (data in SIEM, no alert).
- Example 2: Not hunting — SOC queue work; no missed activity, no gap.
- Example 3: A is a false “clean”; B is hunting because it names a visibility gap and limits claims to visible data.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Re-triage High EDR alerts | SOC / already-covered work | Mechanism already raised it |
| 14-day lookalike beacon in SIEM, no analytic | Hunting finding / **detection gap** | Telemetry exists; nothing alerted |
| Server class excluded from EDR, no process logs | **Visibility gap** | Cannot see the activity class |
| Prevention blocked a hash and opened a ticket | Not a hunt miss | Control worked |
| “Lab is clean — we have no EDR data from lab” | Not enough to claim quiet / visibility gap | Absence of sensor ≠ absence of activity |
| Explain to SOC lead why we hunt finance TLS when the queue is empty | Hunting purpose (2.1.1.1) | Queue empty is why hunt still has a job |

**Purpose statement (Example answer):**  
Hunt exists to find malicious or suspicious activity the SOC stack did not raise, and to name detection or visibility gaps so the program can close them. Empty queues mean the *known* paths are quiet, not that finance TLS is unused. We owe you leads and gaps, not a second triage shift.

Fail the answer if it only says “we look harder” or “we pull more alerts.”

---

## Knowledge Check – Answer Key

1. **What is the purpose of threat hunting in the security program?**  
   **Answer:** Proactively find malicious or suspicious activity that existing security mechanisms missed, and identify detection and visibility gaps so the program can close them.  
   **Explanation:** Two jobs: activity and gaps. Not a second SOC queue.

2. **What is the difference between a detection gap and a visibility gap?**  
   **Answer:** Detection gap: the telemetry exists but nothing useful alerted. Visibility gap: you do not have the telemetry (or cannot query it).  
   **Explanation:** “No hits” only means something if you could have seen the activity.

3. **Why is re-working last night’s alert queue not hunting?**  
   **Answer:** That activity was already raised by an existing mechanism. Hunt starts where the stack did not surface the work.  
   **Explanation:** The title “hunt” does not change the job.

4. **Identify: DNS and TLS for a lookalike name are in the SIEM; nothing alerted for 14 days.**  
   **Answer:** Missed activity plus a **detection gap**.  
   **Explanation:** Data was there; the mechanism did not raise it.

5. **Identify: “Zero EDR hits on the lab VLAN” when that VLAN is excluded from EDR.**  
   **Answer:** **Visibility gap.** Not a clean environment.  
   **Explanation:** You measured the sensor’s absence, not activity.

---

## Additional Instructor Resources

- Local examples of a quiet hunt that found a gap (sanitize before class)
- Escalation: if students ask how to hunt persistence/privesc, or intel-driven vs hypothesis hunts, park it for 2.2 / 2.3
- Next recommended module: Attacker techniques (2.2)
