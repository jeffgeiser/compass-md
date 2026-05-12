# Claude Code Instructions

This directory is my compass-md following the v0.1 convention.

## What this is

This folder contains my personal context Compass. The structure follows
the compass-md convention — see COMPASS.md for details on what's active.

## How to use this Compass

Before acting on my behalf, read the files relevant to the task:

- **Drafting content** → `self/voice.md` + relevant `self/perspectives/`
- **Recommendations** → `self/preferences.md` + relevant `self/perspectives/`
- **Context about me** → `self/facts.md`
- **Prior decisions** → `self/decisions.md`

Cite which files you read at the start of your response.

## Proposing refinements

If you observe something during a session that warrants updating this
Compass (a corrected preference, a new pattern, a stated perspective),
write a refinement file rather than editing Compass files directly.

**File location:** `refinements/pending/<target-file>-<unix-timestamp-ms>.md`

**Required format:**

```markdown
---
proposed_at: <ISO 8601 timestamp>
proposed_by: claude-code
target_file: <relative path, e.g. self/voice.md>
target_section: "<section heading>"
change_type: addition | modification | removal
confidence: low | medium | high
---

## Observation

[What you observed that motivated this proposal.]

## Proposed change

[The exact content to add, modify, or remove.]

## Reasoning

[Why this change is warranted. Include uncertainty.]

## Evidence

[Specific examples from this session.]
```

**Rules:**
- Maximum 3 refinements per session
- Only propose medium or high confidence refinements
- Never edit Compass files directly — always use the pending queue
- After proposing, append to `log.md`:
  `## [YYYY-MM-DD HH:MM] refinement-proposed | <brief description>`
