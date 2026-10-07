# Instructor Guide – Module 2.4.3 – VirusTotal Relations and Behavior

**Estimated Time:** 20–25 minutes

## Two-pass delivery

Spend about 5 minutes here on retrieval and evidence capture: the retrieved file/report identity, report time, and one relationship or observed event. Use a supplied static result if a live account or permitted query is unavailable. Reserve the remaining stated lesson time and the knowledge check for 2.5.2, alongside file relationships and sandbox behavior. Do not mark the platform task complete after orientation alone.

Use the first two slides for orientation; use the remaining slides and worked example during the paired method lesson. Reuse the same result in both passes.

## Purpose

Teach learners to distinguish VirusTotal object relationships from sandbox behavior and to interpret both as evidence rather than conclusions.

## Core Teaching Points

**Relations**
- linked objects in VirusTotal's data model;
- useful for candidate pivots;
- not automatic proof of common ownership or actor control.

Reference: [VirusTotal – Relationships](https://docs.virustotal.com/reference/relationships)

**Behavior**
- observations from sandbox reports;
- may vary across sandbox engines and execution conditions;
- absence from one report is not proof a behavior never occurs.

Reference: [VirusTotal – File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)

## Separate Classroom Card — Not A12

State explicitly that A12 does **not** supply a recovered sample, hash, or VirusTotal behavior record. These values are training-only.

Seed: `sync-client.exe` SHA256

Relations:
- `198.51.100.77`

Behavior:
- `sync-client.exe` starts;
- Temp file write;
- connection to `198.51.100.77:8080`;
- no Run-key event shown.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| “VT relationship = adversary infrastructure.” | Ask what the relationship type actually says and what corroborates malicious control. |
| “Not in Behavior = never happens.” | Reframe as not observed in this report. |
| Copies verdict count instead of evidence. | Return to the relationship or behavior event. |
| Combines Relations and Behavior into one vague claim. | Require the learner to name which source of evidence supports each statement. |

## Knowledge Check – Answer Key

1. It establishes that VirusTotal records a relationship between the objects. Relevance, malicious control, and campaign relationship still require analysis.
2. No. You can say the event was not observed on that report/card; sandbox coverage is conditional.
3. Accept: relationship to `198.51.100.77`; behavior connection to `198.51.100.77:8080`, process start, or Temp write.

## References

- [VirusTotal – Relationships](https://docs.virustotal.com/reference/relationships)
- [VirusTotal – File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)
