# Markdown Ebook QA Report

**Version:** v0.1 Review Draft  
**Build:** 2026-10-03  
**Source snapshot:** current `/thraining-plan/` files retrieved 2026-10-02

**Result:** The Markdown assembly is complete. All 107 student-facing chapters are included in teaching order, with the current CTI organization. Structural checks pass. Substantive A12 differences remain visible and require an editorial decision before final publication.

## Coverage and Order

| Check | Result |
|---|---|
| Student-facing chapters | 107: Parts I–VI contain 11, 28, 41, 16, 10, and 1 respectively |
| Missing or duplicate chapters | None detected; each source student guide appears once |
| Student guide missing from a teaching folder | None: all inventoried module folders containing instructor guides or slides also contain a student guide |
| README references to missing student guides | None detected in downloaded module README files |
| Teaching order | Numeric module order; unnumbered course conclusion follows 4.9 |
| CTI structure | 2.0, all eight current 2.1–2.8 units, and 2.9; no reversion to the former 2.1–2.12 sequence |
| Introductions, section summaries, conclusion | All included |
| Proficiency mappings | 97 mapped chapters; all source ratings and task statements retained in Appendix B |
| Unmapped modules | 0.9, 1.0, 1.6, 2.0, 2.9, 3.0, 3.8, 4.0, 4.9, and the course conclusion remain unmapped |
| Canonical source modifications | None; all edits are in the derived ebook project |
| Instructor-only chapters | None included |

Chapter identifiers remain separate from task identifiers. For example, chapter 3.1 contains a 3.1.1 proficiency requirement; this is not a missing learner chapter. Subordinate task references link to their owning chapter.

## Content, Links, and Markdown

- **Content preservation:** Every non-heading source content line is accounted for in the learner chapter, Appendix B, or the explicit editorial log after Markdown/link normalization. No unexplained omissions were detected. This is a conservative coverage check, not a claim that automated comparison can validate every teaching judgment.
- **Code:** All 18 fenced code blocks from 16 student guides are preserved exactly. All fences close.
- **References:** All 202 external Markdown-link occurrences in the student guides remain in their chapters. The consolidated bibliography contains 83 distinct exact URLs, grouped by domain with chapter backlinks. Live URL availability and the currency of platform interfaces were not independently checked.
- **Internal navigation:** All generated heading links resolve. The remaining relative file link in the manuscript points to the accompanying QA report. No learner link targets an obsolete module file path.
- **Headings:** One book H1; consistent Part, chapter, and lesson hierarchy. The course summary’s secondary H1 becomes a lesson section. No heading exceeds level 6.
- **Tables:** Pipe-row column counts were checked across the manuscript; no inconsistent rows were detected. Proficiency ratings stay in their original compact role lists rather than being forced into very wide tables.
- **Assets:** No Markdown image assets are referenced by the student guides; none had to be copied or reconstructed. Technical examples remain inline.
- **A12 coverage:** The manifest identifies explicit case references and shared-value overlaps across 80 chapters. Some Zeek examples reuse an address while using another host or domain; overlap alone does not make them new A12 facts.
- **Scope:** No DOCX, PDF, EPUB, or final-layout export was created. Review is in Markdown; no claim of print-rendering QA is made.

## Editorial Changes

The assembly adds spoiler-light front matter, a complete linked contents list, Part introductions, short unit bridges, a course-grounded glossary, and a consolidated acronym list. Existing purpose sections precede objectives where available. It removes 165 standalone navigation/index lines and converts useful relative chapter links into book references. “Previous” labels are removed from related-reading entries. CTI references to finished products now lead directly to 2.7.3, and obsolete platform-enrichment labels use the current platform-unit name.

Ratings, task mappings, target-audience metadata, and explicit unmapped status move to Appendix B. Platform exercises retain their two-pass model; “instructor-provided” becomes “provided,” with the front matter explaining that some activities need supplied reports or an authorized environment. A few repetitive summary-boundary sentences are smoothed. Deliberate teaching repetition, knowledge checks, and technical evidence boundaries remain.

The complete source narrative retains its voice and conclusions for review. Appendix A removes its final maintainer-only sentence pair, repairs nested bold formatting, and updates structural references for RFI intake/response and the supporting roles chapter. These changes do not resolve the substantive discrepancies below. The detailed edit inventory is in [editorial-audit.json](editorial-audit.json).

## A12 Consistency Review

**Canonical narrative:** `/thraining-plan/docs/companion-story/story.md`. The companion README identifies it as the finished retelling. `/thraining-plan/docs/story-bible.md` is the governing fact ledger and was consulted alongside the revised student guides.

The front introduction reveals only the fictional organization, workstation, account, and progressive teaching purpose. Appendix A includes the full nine-stage narrative and close, with no invented ending. The following discrepancies are retained, not silently reconciled:

| ID | Canonical story statement | Revised lesson boundary | Review needed |
|---|---|---|---|
| A12-01 | Stage 2 labels the process alert a TP because `wscript` launched encoded PowerShell and matched the rule. | 1.4.1 leaves important context unresolved; 1.4.2 requires evidence of the malicious or unauthorized target condition, beyond a rule match. | Supply the missing assessed-condition evidence or revise the story’s classification. |
| A12-02 | Stage 2 and the close call the unalerted download an FN. | 1.4.2 and 3.1 require an established detection expectation, evidence of the relevant activity, and a checked alert/telemetry scope. | Establish the required coverage and checked outcome before treating the miss as a confirmed FN. |
| A12-03 | Stage 5 answers “likely yes” to whether the destination served the payload and directs the recipient to treat it as the payload host. It relies on a Zeek A record and a host file. | 2.1.1 and 2.7.4 assess attempted payload delivery; successful transfer and execution remain unestablished. The host file mentioned in early triage is `invoice.vbs`, not proof that `/update.exe` transferred. | Distinguish the domain’s assessed delivery role from confirmed delivery; decide whether additional evidence belongs in the canonical facts. |
| A12-04 | Stage 6 claims “same control,” one activity set, and shared payload-host control from nameserver/A-record overlap. | 2.4.5, 2.5.5–2.5.7, and 2.6.2 treat overlap as a candidate relationship that needs time, distinctiveness, hosting context, and corroboration. | Keep candidate, assessed relationship, activity set/campaign, and attribution as separate claims, or supply the supporting evidence for the stronger narrative. |
| A12-05 | Stage 6 says to expire the entire shared-cloud `/24`. | 2.5.1 distinguishes rejecting an overbroad candidate from expiring a previously valid indicator. | Select the correct lifecycle decision; the narrative also says the range is rejected, so its wording is internally inconsistent. |
| A12-06 | Stage 2 says ANY.RUN is the wrong first tool because the analyst has a hash rather than a sample to detonate. | 0.7 and 2.4.4 allow looking up an existing report using a hash; new detonation and existing-report retrieval are different actions. | Preserve the chosen workflow without implying that hash-based report lookup is impossible. |
| A12-07 | Stage 2 and the bible supply the fictional result that the `invoice.vbs` hash is not in VirusTotal. | 1.4.1 explicitly leaves lookup pending because no real service result is supplied. | Clarify whether the lesson’s evidence card contains a fictional result or leaves the lookup unresolved. Do not present either as a real lookup performed for this ebook. |

These issues affect the story’s evidence model and are the principal remaining publication blockers. The manuscript flags the unresolved review status at the beginning of Appendix A without interrupting every story paragraph.

### Continuity Details Retained

- DYA, Building C, WS-JLEE, `jlee`, the host address, process chain, file/registry names, network values, and handoff owners remain as supplied.
- Pink River Dolphin remains a vendor label, not established actor attribution.
- Classroom response clocks remain examples, not live DYA policy.
- The complete story reaches a hunt package and DE’s acceptance/review of a nomination. It does not specify the final deployed rule, a verified count of additional affected hosts, eradication, or final incident resolution. No such outcome is added.
- The later DE and course-summary chapters also use A12 to illustrate a prospective full lifecycle. Read that instructional flow as a model where the source uses conditional or planning language, not as added proof of an actual deployed result in the canonical story.
- Standalone Zeek examples with `192.0.2.10` or `update.example` remain separate examples. They were not renamed to WS-JLEE or merged into A12’s evidence.
- The bible mentions older domain aliases and a historical hash/JA3 concern. Those old aliases and the noted hash prefix were not found in the live student guides used here; they are not reported as active learner-text defects.

## Remaining Review Items

1. Resolve A12-01 through A12-07 in a later canonical editing pass, then rebuild this derived manuscript.
2. Decide whether the next voice pass should revise the source lessons more broadly. This edition smooths book continuity while preserving the existing instructional prose and intentional repetition.
3. Package any separate supplied reports and local-environment exercises before presenting the ebook as a self-contained practical lab.
4. Recheck external references and platform guidance before final publication. Their source URLs and technical examples are preserved here, not independently refreshed.

The Markdown deliverables are complete for review. These remaining issues are documented source/editorial decisions, not missing assembly work.
