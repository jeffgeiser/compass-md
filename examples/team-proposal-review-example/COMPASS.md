# Compass Schema

This Compass follows the [compass-md convention](https://github.com/jeffgeiser/compass-md) v0.1.

---

## Owner

Foundry Sales Team — shared Compass for the proposal review and feedback workflow

## Active modules

- `self/`: no   ← this is a team Compass; individual personal Compasses are maintained separately
- `team/`: yes  ← team guidelines, proposal-review criteria, external style, feedback log

## Conventions

- Feedback log entries are added by Agent 2 after each proposal review cycle
- Agent 3 runs weekly on Sundays at 8am PT; produces refinement proposals based on feedback patterns
- Refinements are reviewed by Jordan (sales lead) on Monday mornings
- Criteria files are versioned in the frontmatter — track changes explicitly

## Refinement workflow

- Refinements are proposed by Agent 3 to `refinements/pending/`
- Jordan reviews on Monday mornings
- Approved refinements applied within 24 hours, effective for proposals reviewed that week
- Refinement frequency: Agent 3 proposes maximum 2 refinements per weekly cycle
- Only propose refinements backed by 3+ consistent feedback observations (avoid one-off changes)

## Engagement notes

- Agent 1 (proposal reviewer): read criteria/proposal-review.md and guidelines.md before every review. Don't improvise criteria.
- Agent 2 (feedback logger): extract structured feedback from leader review sessions. Keep observations factual, not interpretive.
- Agent 3 (refinement proposer): propose changes to criteria, not to style. Style changes need human decision.
- All agents: append to log.md when performing significant actions.

## Sensitive content

- Never include client names or deal details in this Compass
- Proposal files themselves are never stored here — only the criteria and feedback patterns
- Compensation or quota details are not stored here

## Agent instructions

### Agent 1 — Proposal Reviewer

When reviewing a proposal:
1. Read `team/guidelines.md` for context on what the team values
2. Read `team/criteria/proposal-review.md` for specific evaluation dimensions
3. Read `team/style.md` to understand our external voice (relevant for flagging voice deviations in proposals)
4. Evaluate the proposal against the criteria
5. Output a structured review following the format in criteria/proposal-review.md
6. Append to log.md: `## [YYYY-MM-DD HH:MM] read | Agent 1 reviewed proposal [anonymized ID]`

Do not modify criteria files. Do not improvise new criteria during a review.

### Agent 2 — Feedback Logger

When a leader review session is complete:
1. Extract structured feedback from the session notes or marked-up proposal
2. Append to `team/feedback_log.md` in the standard format
3. Note the observation type (criteria gap, style issue, deal-breaker missed, etc.)
4. Append to log.md: `## [YYYY-MM-DD HH:MM] ingest | Agent 2 logged feedback for proposal [anonymized ID]`

### Agent 3 — Refinement Proposer

Weekly cycle:
1. Read `team/feedback_log.md` in full
2. Identify patterns across 3+ feedback entries
3. Identify which criteria or guideline changes would address those patterns
4. Write at most 2 refinement proposals to `refinements/pending/`
5. Append to log.md: `## [YYYY-MM-DD HH:MM] refinement-proposed | Agent 3 weekly cycle: [brief description]`

Only propose refinements where the pattern is clear and the proposed change is specific.

## File coverage

- `team/guidelines.md`: populated
- `team/style.md`: populated
- `team/feedback_log.md`: active — ongoing log
- `team/criteria/proposal-review.md`: populated — current version 1.3

## Last updated

2026-04-20
