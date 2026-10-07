# Ebook QA Report

**Build date:** 2026-10-05  
**Status:** Markdown review build completed successfully.

## Structural validation

- Existing lesson/conclusion chapters: **108**
- Skim-first subunit wrappers: **36** (18 introductions + 18 summaries)
- Embedded learner practicals: **3**
- Embedded controlled lab assets: **3**
- Parts: **6**
- Explicitly unmapped track/course bookends preserved: **10**
- Broken internal Markdown links: **0**
- Fenced code blocks preserved: **22**
- Relative source links converted to book anchors: **67**
- Source lesson line-coverage exceptions: **0**
- Wrapper line-coverage exceptions: **0**
- A12 story line-coverage exceptions: **0**

The builder also verifies unique lesson identifiers, one occurrence of every lesson and wrapper heading, unchanged canonical source inputs during the build, code-block preservation, external-link occurrence preservation, and valid internal anchors.

## Skim-first structure

All **18 meaningful multi-lesson subunits** now appear in the manuscript with a learner-facing introduction and summary. These wrappers implement the course's **Preview → Predict → Read → Confirm** model and are placed around the existing lessons rather than treated as new proficiency chapters.

Detection Engineering has no additional lower-level multi-lesson grouping requiring another wrapper; its existing 4.0 introduction and 4.9 summary remain the appropriate framing layer.

## A12 and editorial review

**Review status:** Current for these source hashes.

The reviewed source snapshot resolves the seven prior A12 issues:

- **A12-01:** Rule match established; malicious/unauthorized classification unresolved.
- **A12-02:** Unalerted request is a coverage question; confirmed FN criteria are not supplied.
- **A12-03:** Likely attempted payload delivery; successful transfer and execution unresolved.
- **A12-04:** Shared NS/A observations support a candidate, with stronger relationships requiring corroboration.
- **A12-05:** Shared /24 rejected as too broad for promotion, rather than expired.
- **A12-06:** Existing sandbox-report lookup by hash is distinct from a new detonation.
- **A12-07:** VirusTotal lookup result not supplied; no live lookup or fictional verdict added.

Current learner and narrative sources were reviewed in the targeted remediation/closure scope. A12 facts and practice extensions are separated, mapped performance verbs retain their approved meaning, skim-first navigation is restored, and the ebook embeds the new practicals without adding numbered proficiency chapters. Broad stylistic rewriting outside identified coherence consequences remains out of scope.

The detailed decisions, live lesson references, voice scope, and 18-subunit skim results are in [the canonical reconciliation review](../docs/a12-reconciliation-review.md). The builder checks that this editorial review covers the current source hashes; it does not infer semantic correctness from a successful compile.

## Editorial / content checks

- Current reorganized CTI structure (2.1–2.8) is retained.
- All 18 wrapper pairs enclose exactly their intended lessons; the complete reading order is in the manifest.
- The complete canonical story becomes Appendix A through heading/link adaptation, with no phrase-based story rewrite or removal.
- Detailed proficiency mappings remain in Appendix B; wrappers and embedded practical sections add no new numbered requirements.
- The three approved learner practicals are embedded under their owning lessons; their small controlled CSV/Python assets are embedded as fenced blocks so the single-file learner artifact remains usable.
- External-link occurrences from lessons, wrappers, practicals, and the story are preserved; all are eligible for the consolidated bibliography.
- Table column checks pass. All generated internal anchors resolve.
- Instructor guides, answer keys, slides, and planning files are excluded from the learner body.
- Gemini split exports are outside the build. Canonical sources feed the ebook, which is the single learner upload.
- Live external website availability and platform-interface currency were not independently revalidated.

## Remaining publication work

This build is ready for content review with the editorial status above. Final publishing work—DOCX/PDF/EPUB styling, pagination, visual QA, and any refreshed live-platform reference checks—remains a later phase.
