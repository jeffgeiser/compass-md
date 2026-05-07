# Proposal Review Criteria

version: 1.3
last_updated: 2026-04-10
maintained_by: Jordan (sales lead)

---

## Purpose

Specific evaluation criteria for reviewing proposals before they're sent to prospects. Agent 1 uses this file to conduct structured reviews and produce a scored review document. Jordan uses the same criteria in leader review sessions.

## Required inputs

To complete a full review, Agent 1 needs:
- The draft proposal document
- The prospect profile or discovery notes (if available)
- Any prior correspondence with the prospect (if available)

If discovery notes aren't available, flag this in the review — the evaluation of "problem specificity" will be limited.

## Evaluation dimensions

### 1. Problem specificity (weight: high)

Does the proposal describe the prospect's actual problem, or a generic version of the problem we solve?

**Strong:** Names the prospect's specific pain point with evidence from discovery. Example: "Your team is spending 4+ hours per incident correlating signals across 6 monitoring tools" — not "observability challenges."

**Weak:** Uses generic problem framing that could apply to any prospect in our ICP. Describes our solution category rather than their specific situation.

**Deal-breaker:** Proposal could be from a template with prospect name swapped in; no evidence of actual discovery.

### 2. ROI clarity (weight: high)

Can the prospect's champion defend this purchase internally without our help?

**Strong:** Quantifies the cost of the current problem (incident costs, engineering hours, alert fatigue) and shows Foundry's impact on a metric the company already tracks. The math works without us being in the room.

**Weak:** States benefits without numbers ("reduces alert noise") or uses numbers we provided rather than numbers derived from the prospect's own context.

**Deal-breaker:** No quantifiable ROI case. "Improves observability" is not an ROI case.

### 3. Implementation plausibility (weight: medium)

Does the proposed implementation plan make success within 60 days plausible?

**Strong:** Names specific integration points, identifies the prospect's technical contact by role (not name), acknowledges any known complexity (legacy systems, existing tooling), and proposes concrete milestones at 30/60 days.

**Weak:** Generic implementation plan that doesn't reference anything specific to this prospect's stack or team structure.

**Deal-breaker:** No implementation plan, or plan that requires the prospect to have done things they haven't done (e.g., assumes clean data pipeline when discovery revealed mixed signals).

### 4. Structural compliance (weight: medium)

Does the proposal follow our standard format?

**Strong:** Executive Summary → Problem Statement → Solution → Implementation Plan → Pricing. Under 4 pages main body. Supporting data in appendix.

**Weak:** Minor structural deviations that don't affect readability.

**Deal-breaker:** Missing a required section (especially Pricing or Implementation Plan).

### 5. Voice and tone (weight: low)

Does the proposal sound like us?

Refer to `team/style.md` for our external voice. Common failures: too salesy in Executive Summary, too technical in the Problem Statement, passive voice in the Implementation section.

**Strong:** Confident, specific, direct. Reads like a peer talking to a peer about a shared problem.

**Weak:** Reads like a sales document. Uses the word "leverage" or "synergy." Leads with company history rather than the prospect's problem.

## Deal-breakers (auto-fail)

Any of the following should result in "Do Not Send" regardless of other scores:

- No evidence of prospect-specific discovery (template swap)
- No quantifiable ROI case
- Missing pricing section
- Commitments about unreleased features
- SLA commitments beyond standard terms
- References to prospects by name in examples (compliance risk)

## Output format

Each review should produce a document with:

```
## Proposal Review: [Prospect anonymized ID] — [Date]

### Summary
[1-2 sentence verdict: send, revise and send, do not send. Reasoning in one sentence.]

### Dimension scores
| Dimension | Score (Strong / Acceptable / Weak / Deal-breaker) | Notes |
|-----------|--------------------------------------------------|-------|
| Problem specificity | | |
| ROI clarity | | |
| Implementation plausibility | | |
| Structural compliance | | |
| Voice and tone | | |

### Required changes before sending
[Bulleted list of specific changes needed. Empty if "send as-is."]

### Notes for Jordan
[Anything that warrants leader attention beyond the standard criteria.]
```

## Notes for agents

Don't soften deal-breaker calls. If a proposal hits a deal-breaker, say "Do Not Send" — don't say "consider revising." The distinction matters for tracking.

If discovery notes weren't provided, note the limitation explicitly. Problem specificity can't be fully evaluated without them.

When flagging required changes, be specific about what to change and why. "The ROI section is weak" is not a useful flag. "The ROI section uses Foundry's benchmark numbers rather than the prospect's own incident data — replace with numbers from the discovery call" is.
