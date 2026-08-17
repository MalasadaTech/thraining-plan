# Instructor Guide – Module 2.2.1 – Hunt Types

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.2.1 B / C / C · 2.2.1.1 3c / 4c / 4c · 2.2.1.2 3c / 4c / 4c · 2.2.1.3 3c / 4c / 4c · 2.2.1.4 3c / 4c / 4c  
- SOC: 2.2.1 A / B / B · 2.2.1.1 1a / 1a / 2b · 2.2.1.2 1a / 1a / 2b · 2.2.1.3 1a / 1a / 2b · 2.2.1.4 1a / 1a / 2b  
- CTI: 2.2.1 A / B / B · 2.2.1.1 1a / 1a / 2b · 2.2.1.2 1a / 1a / 2b · 2.2.1.3 1a / 1a / 2b · 2.2.1.4 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the four hunt types and how execution *starts* for each. Make students classify work by input and practice a four-sentence execute (type, first search, quiet, hand-back).

**Key Teaching Points:**
- Type follows the **input**, not the chat title.
- Four types only: intel-driven, hypothesis-driven, reactive, anomaly-based.
- Reactive ≠ SOC queue. Anomaly needs a baseline. Hypothesis needs a testable Y.
- Execute here is the first move, not a 2.2.2 hunt plan.
- Stay out of hypothesis-writing depth (2.2.2), VT/AnyRun (2.3), TTP extraction (2.4), ATT&CK (2.5), persistence how-to (2.6).

**Common Student Challenges:**
- Relabeling triage as reactive.
- Calling any idea a hypothesis-driven hunt.
- Calling any “weird” an anomaly-based hunt.
- Writing a full scope/priority memo when asked only to execute the first search.
- Mixing types without saying the type changed.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for a four-column type sort
- Answer key (this guide)

---

## Learning Objectives

1. Name the four hunt types and the input that starts each one.
2. Tell a **reactive hunt** apart from SOC work on an existing alert.
3. Tell a **hypothesis-driven hunt** apart from an **anomaly-based hunt**.
4. Execute a hunt *by type*: pick the type, take the first search, and say what you will hand back.

**Mapped Items:**
- K: 2.2.1 – Hunt types
- T: 2.2.1.1 – Execute an intel-driven hunt
- T: 2.2.1.2 – Execute a hypothesis-driven hunt
- T: 2.2.1.3 – Execute a reactive hunt
- T: 2.2.1.4 – Execute an anomaly-based hunt

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Four names on the board; no definitions yet |
| Four types                     | 14 min   | Input table; students fill “starts from” |
| Execute by type / traps        | 10 min   | Reactive vs SOC; anomaly vs hypothesis |
| Walkthrough Examples           | 14 min   | Interactive; students name type first |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~68 min** | Stretch Example 2 if the room still says the queue is reactive |

---

## Detailed Teaching Notes

### 1. Four Hunt Types

**Talking Points:**
- Ask for types before you show the table. Write wrong ones (“EDR hunt,” “Zeek hunt,” “when SOC is bored”).
- Hunter 3 is already at principles (B / 3c). Push them to *classify from the input*, not recite four slogans.
- SOC/CTI in the room: they must recognize the names and not treat hunt-channel titles as types (A / 1a).

**What to emphasize:**
- One input → one starting type. Changing type is fine if spoken.
- Purpose (2.1) is unchanged. Type is not a new mission.

**Questions to ask the class:**
- “What started this work — objects, an if/then, a spark, or a baseline?”
- “If the title says reactive and the work is the High queue, what is it really?”

### 2. Execute by Type

**Talking Points:**
- Four-sentence execute is the whole task bar for this lesson.
- Park “how do I write a better hypothesis?” and “how do I prioritize?” for 2.2.2.

**What to emphasize:**
- Quiet is only allowed where they had visibility (reuse 2.1; do not re-teach the whole gaps lesson).
- Intel that becomes a broader if/then is a type change. Reward people who say it.

**Question to ask:**  
“Can your first search fail? If not, you do not have a type yet.”

### 3. Examples

Work through all three interactively. Students name type (or “not a hunt”) before you read the interpretation.

**Extra point for Example 1:**  
Bulletin objects → search → lead + detection gap. Clean intel-driven execute.

**Extra point for Example 2:**  
Same trap family as 2.1 Example 2. The word reactive is the bait.

**Extra point for Example 3:**  
A will be popular. Force: no baseline = not anomaly; no Y = not a finished hypothesis.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- Review answers as a group afterward. Do not collect a grade.
- If someone writes a one-page scope/priority plan, thank them and park it for 2.2.2. Grade the four sentences.

**What good answers look like:**

**Summaries:**
- Example 1: Intel-driven execute — bulletin names searched; host + detection gap; lab not claimed clean.
- Example 2: First message not a hunt (SOC). Second is reactive — peers around an IR spark.
- Example 3: A is neither anomaly nor a usable hypothesis. B is anomaly-based execute (baseline, deviation, visibility).

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Weekly bulletin hashes in 7-day EDR | **Intel-driven** | Objects came from intel |
| Re-triage High EDR alerts | **Not a hunt** | Already raised; SOC |
| IR host; unalerted peers, same parent | **Reactive** | Spark + related unalerted activity |
| If finance laptops beacon after 21:00, we should see repeated DNS+TLS | **Hypothesis-driven** | Testable if/then |
| New outbound 8443 vs 30-day none | **Anomaly-based** | Baseline + deviation |
| “Anomaly hunt: attackers use scheduled tasks” | **Not a hunt yet** / not a type | No baseline, no Y |

**Execute blocks (example answers):**

Intel-driven (bulletin hashes):  
Type is intel-driven. First search is those hashes in EDR for 7 days on in-scope endpoints. Quiet means no hash match where EDR exists — not “the company is clean.” Hand-back is any host hits plus whether anything already alerted (detection gap) or a bounded quiet.

Anomaly-based (new 8443):  
Type is anomaly-based. First search is outbound 8443 on that VLAN vs the 30-day baseline, then peer hosts. Quiet means no new 8443 where we have conn/TLS — not lab if lab is dark. Hand-back is the deviant hosts plus the missing analytic (detection gap) or the dark segment (visibility gap).

Fail the answer if it only says “look harder,” relabels the queue, or turns into a 2.2.2 priority memo.

---

## Knowledge Check – Answer Key

1. **What are the four hunt types, and what input starts each one?**  
   **Answer:** Intel-driven (report/IOC/TTP set). Hypothesis-driven (testable if/then). Reactive (spark that is not finished SOC work). Anomaly-based (measurable baseline + deviation).  
   **Explanation:** Type follows the input.

2. **Why is re-working last night’s alert queue not a reactive hunt?**  
   **Answer:** That activity was already raised. Reactive hunt expands around a spark to find *related* activity the stack did not raise.  
   **Explanation:** The word reactive does not change SOC work into a hunt type.

3. **How is a hypothesis-driven hunt different from an anomaly-based hunt?**  
   **Answer:** Hypothesis starts from an if/then you will test (Y must be searchable). Anomaly starts from a baseline and a deviation in the data.  
   **Explanation:** “Looks weird” is neither until you have Y or a baseline.

4. **Bulletin domain names searched in DNS/TLS. Which type, and what do you hand back if you find rows and no alert?**  
   **Answer:** **Intel-driven.** Hand back the lead and a **detection gap**.  
   **Explanation:** Objects came from intel; telemetry existed; nothing alerted.

5. **30-day baseline of no new SYSTEM tasks; two appear overnight. Which type, and what about a segment with no process logging?**  
   **Answer:** **Anomaly-based.** That segment is a **visibility gap**, not quiet.  
   **Explanation:** Baseline + deviation. No sensor ≠ clean.

---

## Additional Instructor Resources

- Local examples of a hunt that changed type mid-flight (sanitize before class)
- Escalation: hypothesis writing, scope, and priority → 2.2.2; tools → 2.3; CTI extract → 2.4
- Next recommended module: Hunt development concepts (2.2.2)
