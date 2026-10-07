# Module 3.8 – Threat Hunting Section Summary

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Time:** 15–20 minutes  
**Module Type:** Section summary — no proficiency mapping

## Purpose

Module 3.0 introduced threat hunting as a bounded analytical loop:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

Module 3.8 closes that loop.

By this point, you have learned why hunting exists, how different hunts begin, how to develop a hunt, how CTI and external research become hunt inputs, how ATT&CK supports planning, how to hunt specific techniques, and how a finished hunt is documented and routed.

The goal of this summary is not to reteach each lesson.

It is to reconnect the pieces into one defensible hunt process.

## 1. What You Can Now Do

You should now be able to:

- explain why hunting exists alongside alerting and incident response;
- distinguish an intel-driven, hypothesis-driven, reactive, and anomaly-based starting signal;
- turn a topic into a testable hypothesis;
- define population, time window, telemetry, exclusions, and priority;
- identify a distinctive behavior or artifact worth searching;
- use external research and CTI to sharpen an internal search;
- distinguish a CTI lead from proof of local occurrence;
- use ATT&CK to organize behavior without allowing the framework to replace the hunt question;
- recognize persistence and privilege-escalation evidence without overstating the technique used;
- document the search so another hunter can understand or reproduce it;
- separate findings, detection gaps, visibility gaps, and follow-on leads;
- hand different outcomes to the correct downstream owner.

The important skill is not running a large number of queries.

It is producing a bounded answer that another defender can understand and act on.

## 2. The 3.x Block at a Glance

| Unit | Core skill retained |
|---|---|
| **3.1 – Purpose** | Explain why hunting searches beyond what existing alerts have already surfaced. |
| **3.2 – Methodology** | Convert a starting signal into a hypothesis, scope, priority, and distinctive search pattern. |
| **3.3 – Online Tools** | Use external evidence to sharpen leads and build an internal query plan. |
| **3.4 – CTI for Hunters** | Assess intelligence for hunt value and extract behaviors, indicators, procedures, and structured inputs. |
| **3.5 – Framework Application** | Use ATT&CK to organize the behavior and support hunt planning without replacing the evidence. |
| **3.6 – Attacker Techniques** | Translate technique knowledge into specific huntable observations while preserving method/evidence boundaries. |
| **3.7 – Site-Specific Operations** | Follow the local process for hunt control, documentation, completion, and handoff. |

Together, these units answer one question:

> **How do we search deliberately for relevant activity that existing controls have not already answered well enough?**

## 3. A12 End to End

The A12 scenario can show the entire hunt workflow.

### Step 1 – Starting signal

The original incident identified suspicious activity on `WS-JLEE`.

Available evidence included:
- encoded PowerShell;
- a request for `/update.exe`;
- a Run-key persistence pattern such as `Updater → %TEMP%\update.exe`.

The incident creates a reasonable hunt question:

> **Are there additional Windows workstations with the same or closely related persistence behavior?**

This is primarily a **reactive** starting signal because an active/known incident created the need to determine wider scope.

The hunt may still use CTI and a formal hypothesis. The course labels describe the primary starting signal, not mutually exclusive boxes.

### Step 2 – Hypothesis

Turn the question into an expectation:

> If A12-style persistence exists on additional managed Windows user workstations, we expect to observe Run-key values pointing to `update.exe` or closely related payloads in user-writable paths.

That statement can be supported or fail to be supported by evidence.

### Step 3 – Scope

Define what the result will actually mean.

Example:

- **Population:** managed Windows user workstations
- **Window:** previous 14 days
- **Telemetry:** registry modification plus process/file telemetry
- **Important exclusions:** approved updater/software-management patterns where known

A negative result is only meaningful for systems and time periods where the required telemetry is available.

### Step 4 – Search pattern

Start with the distinctive behavior.

Examples:

- Run-key modification;
- target path in `%TEMP%` or another user-writable location;
- value or filename relationship;
- related process/file context.

Do not assume the exact value name is the only possible variant.

Use exact artifacts when useful, then expand carefully into behavioral relationships.

### Step 5 – CTI and external research

CTI or an external platform may provide:
- related hashes;
- infrastructure;
- filenames;
- process behavior;
- registry artifacts;
- additional procedures.

Those findings sharpen the hunt.

They do **not** prove that the same artifact or behavior occurred internally.

The hunter still needs local evidence.

### Step 6 – ATT&CK and technique reasoning

The Run-key pattern can be mapped to the appropriate ATT&CK technique when the observed behavior supports it.

Keep three levels separate:

- **Technique:** the ATT&CK behavior category
- **Procedure:** how the activity was carried out in this case
- **Local observation:** the specific registry/process/file evidence you actually saw

The framework helps organize the hunt. It does not replace the hypothesis or evidence.

### Step 7 – Refine the candidates

Suppose the first query returns many Run-key entries.

Refine using context such as:
- target path;
- filename;
- signer;
- parent/process relationship;
- timing;
- known-good software.

The goal is to reduce the candidate set without filtering away the behavior you are trying to find.

### Step 8 – Findings

The canonical A12 story does not specify the hunt outcome. For practice, suppose a hunt produced the following result:

- 2 additional hosts show the exact `Updater → %TEMP%\update.exe` pattern;
- 3 other hosts show related Run-key behavior needing review;
- 18 hosts were searched with complete required telemetry;
- 7 hosts lack the registry telemetry needed to test the hypothesis;
- no current analytic appears to cover the exact behavior.

This produces several different findings.

### Step 9 – Handoff

The hunt does not have to solve every downstream problem itself.

Possible routing:

| Finding | Downstream owner category |
|---|---|
| Additional affected hosts | SOC / Incident Response |
| No existing analytic for the behavior | Detection Engineering |
| Missing registry telemetry | Telemetry / platform owner |
| New infrastructure or intelligence question | CTI |
| Related unexplained pattern | Follow-on hunt / lead-management process |

The actual local team names and queues come from the site's hunt-governance process.

## 4. Distinctions That Keep a Hunt Reviewable

Hunting combines intelligence, hypotheses, telemetry, and search logic. The concepts below stay useful when each one is tied to the question it is meant to answer.

### Hunt type describes the starting signal, not the whole design

**Reactive**, **intel-driven**, **hypothesis-driven**, and **anomaly-based** describe how a hunt primarily begins.

Regardless of the starting signal, a reviewable hunt still needs a testable question, bounded scope, required telemetry, search logic, and a documented result.

### A topic becomes a hypothesis when it predicts evidence

> Hunt persistence

names an area of interest.

> If A12-style persistence exists elsewhere, we expect to observe Run values pointing into user-writable paths

creates an expectation that can be tested. The second form tells the hunter what evidence would support or weaken the idea.

### CTI creates a lead; local telemetry establishes local occurrence

A sandbox observation, passive-DNS result, indicator, or STIX object can give the hunter a reason to search. It does not establish that the activity occurred inside the organization.

The hunt connects the external lead to local evidence within a defined population and time window.

### Indicators and behaviors support different kinds of searching

An exact hash, domain, or IP can provide a precise match. A behavior or procedure can survive infrastructure or file changes and support a broader search.

Good hunts often use both: exact artifacts for precision and behavior for durability.

### ATT&CK names the technique; the hunt needs the observable procedure

ATT&CK gives the team a shared behavior category. The hunt still needs the specific procedure, fields, and telemetry pattern that can be tested locally.

Technique mapping helps organize the question; the procedure makes it searchable.

### Detection gaps and visibility gaps require different fixes

A **detection gap** exists when the required telemetry is available but current analytics do not adequately cover the behavior.

A **visibility gap** exists when the telemetry needed to test or detect the behavior is absent or insufficient.

The first points toward analytic coverage. The second points toward collection, ingestion, parsing, or population coverage.

### Unalerted activity becomes a false negative only when an expected detector failed

The absence of an alert can reveal a coverage question, but a confirmed false negative requires an established expectation that a control should have detected the target condition and evidence that the required telemetry reached that control.

This prevents the hunt from labeling every previously unalerted finding as a detection failure.

### A privileged outcome does not identify the privilege-escalation method by itself

Observing a process running as SYSTEM can establish a high-privilege state when the context supports that comparison. Identifying token theft, UAC bypass, or another specific escalation method requires evidence of how that state was reached.

### A negative hunt result is bounded by what was actually tested

A defensible result says:

> **Not found within the tested population, time window, and available telemetry.**

That statement preserves the scope of the search. It does not imply that the activity cannot exist elsewhere in the enterprise or outside the observable period.

## 5. Integrated Review Exercise

Use this **hypothetical practice card based on A12 behavior**. These results extend the case for the exercise and are not canonical A12 outcomes:

> **Seed:** A12 incident  
> **Known behavior:** Run-key persistence pointing to `%TEMP%\update.exe`  
> **Population:** managed Windows user workstations  
> **Window:** 14 days  
> **Telemetry:** registry + process/file events  
> **Results:** 2 exact matches, 3 related candidates, 18 fully visible hosts, 7 hosts missing registry telemetry, no known analytic covering the exact pattern

Write a short hunt summary using:

### Hunt question
What are you trying to determine?

### Hypothesis
What evidence should exist if the behavior is present?

### Scope
Which population, time window, and telemetry were tested?

### Findings
What did the hunt actually observe?

### Limitations
What could the hunt not determine?

### Gaps
Which findings are detection gaps versus visibility gaps?

### Handoff
Which outcomes belong to SOC/IR, DE, CTI, telemetry owners, or follow-on hunting?

A strong answer should make the boundaries of the conclusion obvious.

## 6. Threat-Hunting Readiness Checklist

Before moving into 4.x, you should be comfortable saying:

- [ ] I can explain why hunting exists alongside alerts and incident response.
- [ ] I can identify the primary starting signal for a hunt without treating hunt types as rigid boxes.
- [ ] I can turn a topic into a testable hypothesis.
- [ ] I can define population, time window, telemetry, and important exclusions.
- [ ] I can identify a distinctive pattern worth searching.
- [ ] I can turn CTI or external research into an internal query plan.
- [ ] I can distinguish external intelligence from local evidence.
- [ ] I can use ATT&CK to organize behavior without replacing the hypothesis.
- [ ] I can preserve the difference between a technique and the observed procedure.
- [ ] I can distinguish detection gaps, visibility gaps, and possible false negatives.
- [ ] I can write a negative result that is bounded by scope and visibility.
- [ ] I can document the hunt so another hunter can understand what was tested.
- [ ] I can route different findings to different downstream owners.

If one of these is weak, return to the corresponding 3.x unit before moving forward.

## 7. Bridge Into 4.x Detection Engineering

A hunt can discover activity, but some findings are really questions about **durable coverage**.

For example:

> We can find this A12 persistence behavior manually.  
> Should the organization detect it automatically in the future?

That is where Detection Engineering enters.

The hunter provides:
- the observed behavior;
- evidence;
- scope;
- useful search logic;
- benign context;
- limitations.

Detection Engineering determines whether to:
- reuse existing coverage;
- modify an existing analytic;
- create new coverage;
- or decide that another control is more appropriate.

The hunt identifies defensive knowledge.

DE turns appropriate knowledge into maintained detection capability.

## Summary

The 3.x block taught one complete hunt loop:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

A defensible hunt tells the reader:
- what was tested;
- where and when it was tested;
- what evidence was available;
- what was found;
- what could not be seen;
- what should happen next.

Keep one principle with you into 4.x:

> **A hunt result is only as broad as the scope and visibility that produced it.**

**Next:** [4.0 – Detection Engineering Orientation](../../04-de/00-intro/student-guide.md).
