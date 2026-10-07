# Training resource improvement backlog

Recorded: 2026-10-01 (Hawaii)

Scope: Review recommendations for the supplied thraining-plan.zip. These are proposed changes, not approved curriculum requirements. Existing lesson content has not been changed. Follow the existing requirement-review process before adding obligations or modules. Hands-on work remains deliberately deferred.

## Authoring and voice work

| ID | Item | Status | Next action |
|---|---|---|---|
| VOICE-01 | Add a voice-quality check to the training resource review process. | Implemented 2026-10-04. | Maintain the skim-first / advance-organizer standard and mentor-like evidence-first voice during future revisions; use the required skim test in QA. |

## Corrections to review first

| ID | Priority | Location | Proposed improvement | Acceptance evidence |
|---|---|---|---|---|
| REV-01 | High | 2.6.1 Applicable TTPs | Separate applicability from telemetry visibility; retain applicable threats with visibility gaps. | Examples distinguish not applicable, applicable and visible, and applicable with a visibility gap. |
| REV-02 | High | 2.5.2 File similarity | Treat matching imphashes as candidates for comparison; avoid categorical family/common-origin conclusions. | Student, instructor, slides, and answer key consistently distinguish similarity from a supported relationship. |
| REV-03 | High | 1.1.2 Process activity | Remove the unsupported inference that -enc establishes a hidden PowerShell window. | Example interpretation uses only the displayed evidence. |
| REV-04 | High | 1.4.2 Alert classification; companion story | Separate a correctly matched behavior from established malicious activity; establish context and detection expectations before calling an unalerted download a false negative. | Worked cases explicitly state the classification target and supporting evidence. |
| REV-05 | High | 3.2.2 Hunt development; related A12 examples | Replace unsupported uniqueness claims about Updater with assessment of combined artifacts and local prevalence. | Reasoning explains specificity, benign alternatives, and what additional evidence is needed. |
| REV-06 | High | 2.5.6 DTF; 2.5.5 Infrastructure pivots; companion story | Add observation dates, alternative explanations, and corroboration before promoting a candidate into adversary infrastructure or recommending a block. | Candidate relationships and recommended actions carry an explicit evidence basis. |
| REV-07 | High | 3.2.1 Hunt types; proficiency matrices | Distinguish concept preparation from demonstrated task performance; naming a hunt is not executing one. | Qualification guidance identifies the separate performance demonstration needed for sign-off. |
| REV-08 | Medium | 3.2.1 Hunt types | Explain trigger, search method, and hypothesis as potentially overlapping dimensions. | A CTI-led hunt can test a hypothesis without an artificial category conflict. |
| REV-09 | Medium | 3.4.2 Hunt leads | Assess old indicators against the hunt window and retained history rather than discarding them primarily by age. | A retrospective example explains when an old hash remains useful. |
| REV-10 | Medium | Student guides and knowledge checks | Move authoring/scope instructions into instructor guidance and assess analyst judgment instead. | Review with the future voice criteria; preserve meaningful boundaries and required concepts. |
| REV-11 | Medium | Concept index; retired external-tools redirect | Repair 18 broken relative-link occurrences identified during review, including 17 in the concept index. | Local path-link validation passes; missing content is not invented just to satisfy links. |
| REV-12 | Medium | tracker.csv; STIX classroom collection naming | Correct encoding artifacts and reconcile remaining legacy classroom naming with the story bible. | Existing values and status meanings preserved; names consistent across dependent copies. |

## Later teaching additions

| ID | Item | Proposed scope | Status |
|---|---|---|---|
| ADD-01 | Unfamiliar knowledge-check variants | Retain A12 as the worked example; vary legitimate administration, telemetry gaps, shared infrastructure, or conflicting evidence. No lab is needed for conceptual checks. | Proposed |
| ADD-02 | Initial access | Complete the existing TODO for initial access; connect delivery, execution, and observable evidence through the approved curriculum process. | Implemented 2026-10-04 as shared module 0.9; A12 entry path remains evidence-bounded and unresolved |
| ADD-03 | File-enrichment workflow | Connect seed file, related candidates, behavioral comparison, supported relationships, and useful outputs across existing file similarity, signing, VT, and ANY.RUN lessons. Preserve DTF's infrastructure scope. | Proposed |
| ADD-04 | Empty hunt results | Distinguish no matches from missing sensors, insufficient retention, absent fields, or poor query/scope choices. | Proposed |
| ADD-05 | Role-specific learning routes | Identify prerequisites and shorter routes for experienced SOC, CTI, Hunt, and DE personnel while retaining the full sequence. | Proposed |

## Implementation sequence for later approval

1. Apply the implemented skim-first / voice standard to future learner-facing revisions.
2. Review the remaining high-priority reasoning corrections and choose a small pilot set where needed.
3. Revise pilot lessons and obtain user review before applying a new technical approach broadly.
4. Keep student guides, instructor notes, slides, knowledge checks, matrices, and concept index aligned where affected.
5. Rebuild the ebook when learner-facing canonical sources change.

## Review basis and limits

The prior review covered curriculum structure, proficiency design, the companion story, representative lessons across tracks, and local links, with selected technical checks. It was not exhaustive validation of every technical statement. Technical recommendations should be verified against primary documentation during revision.

Primary references checked for specific findings:
- Import-hash limitations: https://cloud.google.com/blog/topics/threat-intelligence/tracking-malware-import-hashing/
- PowerShell command-line parameters: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_powershell_exe?view=powershell-5.1
