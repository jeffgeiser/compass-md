# Compass Schema

This Compass follows the [compass-md convention](https://github.com/[org]/compass-md) v0.1.

---

## Owner

[Name or identifier — used by agents to know who they're acting for]

## Active modules

- `self/`: yes  ← personal context (voice, perspectives, preferences, facts)
- `team/`: no   ← team context (set to yes if this Compass supports team work)

## Conventions

[Note any deviations from the standard convention, custom file types, or patterns specific to this Compass. Leave empty if following the standard.]

## Refinement workflow

- Refinements are proposed by agents to `refinements/pending/`
- Human reviews via [your chosen tool: dashboard / GitHub PRs / weekly email digest / etc.]
- Approved refinements are applied within [your target timeframe: 24 hours / weekly / monthly]
- Refinement frequency expectations: [e.g., "Cowork should propose at most 3 refinements per session to avoid review overload"]
- Confidence thresholds: [e.g., "Only propose 'high confidence' refinements automatically; queue 'low confidence' for explicit ask"]

## Engagement notes

[High-level notes about how agents should engage with the Compass owner. Examples:]

- Be concise. Don't overexplain.
- Push back when I'm wrong rather than just agreeing.
- When uncertain, ask rather than assume.
- I prefer concrete examples over abstract frameworks.

## Sensitive content

[What should NOT be in this Compass. Examples:]

- Never include client names or financial details
- Never include personal health information
- Never include credentials, API keys, or secrets
- Don't store anything that would be embarrassing if leaked

## Agent instructions

When acting on behalf of [owner]:

1. **Read COMPASS.md first** to understand this Compass's conventions
2. **Identify relevant files** for the current task:
   - Drafting content → read `self/voice.md`, relevant `self/perspectives/`
   - Making recommendations → read `self/preferences.md`, relevant `self/perspectives/`
   - Establishing context → read `self/facts.md`
   - Recalling decisions → read `self/decisions.md`
3. **Read those files** before generating output
4. **Act with that context** informing your output
5. **Cite which Compass files** informed your output (e.g., "Drawing on self/voice.md and self/perspectives/strategy.md")
6. **If you observe something** that warrants a Compass refinement (a correction, a stated preference, a new perspective), propose it to `refinements/pending/` per the refinement format
7. **Append to log.md** for significant events: `## [YYYY-MM-DD HH:MM] {event-type} | {description}`

## File coverage

What's currently populated in this Compass:

- `self/voice.md`: [populated / draft / empty]
- `self/preferences.md`: [populated / draft / empty]
- `self/facts.md`: [populated / draft / empty]
- `self/decisions.md`: [populated / draft / empty]
- `self/perspectives/`: [list topics or "empty"]

## Last updated

[YYYY-MM-DD]
