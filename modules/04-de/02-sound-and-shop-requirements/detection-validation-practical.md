# Detection Validation Practical — Draft Analytic Test

**Purpose:** demonstrate `4.2.1` with an actual controlled test, then provide the handoff point for `4.2.2` after local onboarding in 4.8. This is a separate training scenario, not canonical A12.

## Inputs

- [de-validation-practical.csv](../../../labs/de-validation-practical.csv)
- [de-validation-runner.py](../../../labs/de-validation-runner.py)

The draft analytic claims to detect suspicious encoded PowerShell launched by `wscript.exe`. The supplied runner implements **draft v1**. It is intentionally imperfect so the learner has evidence to evaluate rather than a guaranteed pass.

Run from the repository root or equivalent working directory, for example:

```bash
python labs/de-validation-runner.py labs/de-validation-practical.csv
```

Use an approved equivalent query environment if Python is not available. The requirement is to actually execute the draft logic against the controlled evidence, not merely inspect the rows.

## Part A — Test the draft (`4.2.1`)

1. **Positive/intended behavior:** identify which supplied events are expected to match the behavioral claim.
2. **Benign near-neighbor:** verify that the approved deployment and non-encoded PowerShell cases do not match.
3. **Data path:** identify any event where required fields are missing or incomplete.
4. Run the draft and preserve the output.
5. Compare actual results with the expected classes.
6. Make one decision: **PASS**, **CHANGE**, or **FAIL / HOLD**. Justify it from the evidence.

A strong answer notices that a syntactically valid draft can still need change because a supported encoded-command variant is missed and because one sensor does not populate a required parent field.

### Required validation record

Record:

- draft/version tested;
- exact command/query run;
- intended positive results;
- benign-control results;
- false positives / false negatives;
- data-path gaps;
- decision;
- specific change or scoping action, if needed.

## Part B — Local requirement check (`4.2.2`)

Do **not** complete this part from fictional DYA/BHM policy. After 4.8, obtain the **verified local shop requirement list** or an authorized local simulation. Then mark each applicable requirement as met, missing, or not applicable if local policy allows that state.

Attach that checklist to the same validation record. If the real local list is unavailable, record an onboarding/qualification gap rather than inventing requirements.

## Part C — Close the loop (`4.2.3`)

Write a short note to the nominator that states:

- disposition: shipped / changed / sent back / held / superseded, as appropriate;
- what changed from the original need;
- validation result and important limitation;
- next owner/action.

## Evaluator criteria

For `4.2.1`, the evaluator should observe the learner actually execute the test and interpret the results. A satisfactory demonstration includes target, benign near-neighbor, and data-path evidence plus a justified pass/change/fail decision.

For `4.2.2`, qualification requires the verified **real local** requirements artifact or an authorized local simulation after 4.8. The training dataset cannot substitute for local policy.

At higher proficiency, expect the learner to isolate why a case was missed, propose a bounded rule/data-path correction, rerun where practical, and explain residual coverage limitations. Qualification/sign-off remains a separate evaluator action under the course standard.
