# Hunt Execution Practical — Controlled Telemetry

**Purpose:** demonstrate the operational verbs in `3.2.1.1`–`3.2.1.4` and `3.6.3` with one reusable dataset. This is a **separate training scenario**, not canonical A12.

## Inputs

Use [hunt-execution-practical.csv](../../../../labs/hunt-execution-practical.csv). The dataset represents a fictional organization, **Blue Heron Manufacturing (BHM)**.

Run the searches with a tool that actually filters or queries the supplied data: a spreadsheet filter, command-line tool, Python, a notebook, or an approved training SIEM. **Do not satisfy the practical by only reading the table and describing what you would search.**

For every execution, preserve:

1. initiating signal / hunt type;
2. scope and time window;
3. exact query or filter used;
4. returned rows / hosts;
5. telemetry or interpretation gaps;
6. bounded finding and next action.

## Practical A — Intel-driven hunt (`3.2.1.1`)

**Seed intelligence:** CTI reports that suspicious activity may use domain `cdn-sync.example` and Run value name `Updater`.

Execute a local search for both observables, identify matching hosts, then decide whether a broader behavior search is justified. Record which results are exact matches and which are only related candidates.

## Practical B — Hypothesis-driven hunt (`3.2.1.2`)

**Hypothesis:** If unauthorized persistence is using user-writable temporary directories, recent Run-key modifications should reference executables under a user's `AppData\Local\Temp` path more often on affected hosts than on ordinary workstations.

Execute a search for the condition. Review all returned rows rather than assuming every Temp-path Run key is malicious. Use signature/context fields to separate suspicious results from the benign near-neighbor.

## Practical C — Reactive hunt (`3.2.1.3`)

**Incident seed:** `BHM-WKS-07` is the known affected host.

Execute an estate search for exact and related artifacts from that host. Identify any additional hosts that merit incident scoping and state which evidence created the relationship. Do not claim compromise where the evidence only creates a candidate lead.

## Practical D — Anomaly-based hunt (`3.2.1.4`)

**Anomaly seed:** outbound HTTP traffic on destination port `8080` is rare in the workstation population.

Execute a search for port `8080`, group or compare the results by destination/process/path, and determine which results can be explained as approved activity versus which remain suspicious. A rare event is a lead, not a verdict.

## Practical E — Technique-focused hunt (`3.6.3`)

Execute **two** searches for ATT&CK `T1547.001` behavior:

1. **Exact-observed layer:** Run value `Updater` or exact Temp updater paths.
2. **Behavior-broadened layer:** Run-key values that launch executables from user-writable temporary locations.

Compare the returned hosts. Explain what the exact layer misses, what the broadened layer adds, and why the broadened result set requires contextual review.

## Evaluator evidence

The evaluator should observe the learner actually execute the filters/queries and retain the query text or filter criteria. A satisfactory result includes:

- correct scope and use of the initiating signal;
- reproducible query/filter logic;
- accurate identification of returned hosts/events;
- explicit handling of benign near-neighbors and visibility limits;
- findings bounded to the supplied evidence;
- a defensible next action.

At higher proficiency, expect efficient query refinement, explanation of false-positive/false-negative risk, and adaptation when the first search is too narrow or too broad. Qualification/sign-off remains a separate evaluator action under the course standard.
