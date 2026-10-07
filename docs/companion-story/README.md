# A12 companion story

This folder connects one fictional case across SOC investigation, CTI assessment, Threat Hunting, and Detection Engineering. Each role builds a different product from the evidence available at that point.

| File | Purpose |
|---|---|
| [story.md](story.md) | Complete learner-facing case study and source for ebook Appendix A |
| [outline.md](outline.md) | Nine-stage sequence, evidence limits, and reader outcome |
| [desk-beats.md](desk-beats.md) | Fact introduction, first operational use, and later use |
| [plan.md](plan.md) | Evidence reconciliation, voice, review, and publishing procedure |

The [story bible](../story-bible.md) is the fact ledger. Resolve claim-strength disagreements there with the current lessons before revising the narrative. The [reconciliation review](../a12-reconciliation-review.md) records the seven evidence decisions and this pass's QA scope.

## Learner use

The main lessons reveal A12 progressively. Read the complete story afterward to reconnect the products and handoffs. Its preview and closing table also support a skim: predict how each role will use the evidence, then confirm whether you can explain the reasoning and remaining uncertainty.

The narrative reaches a DE coverage review. Initial access, transfer, execution of the requested file, additional affected hosts, control actions, completed DE outcomes, and incident resolution remain open. Hypothetical practice cards in later lessons are separate from established case outcomes.

## Publication

Canonical modules and A12 sources feed the [ebook builder](../../ebook/build_ebook.py), which generates [ebook-manuscript.md](../../ebook/ebook-manuscript.md). The learner manuscript can then be used for NotebookLM/Gemini or later approved document exports. The retired Gemini split-export tree is not a required output. Preserve canonical corrections before rebuilding; the copied Appendix A is not a separate editing source.
