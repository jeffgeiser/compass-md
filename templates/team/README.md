# Team Compass

The `team/` folder holds shared context for a team using the Compass convention. It works alongside or independently of a personal `self/` folder.

---

## When to use `team/`

Use `team/` when:
- Multiple people are sharing a Compass (a team, a project, a partnership)
- You want agents to apply consistent evaluation criteria across team members' work
- You want institutional knowledge to accumulate in a shared, AI-readable place

You don't need `team/` for a purely personal Compass. A personal Compass using only `self/` is perfectly complete.

## How it differs from `self/`

`self/` is personal context — voice, preferences, decisions that belong to one person.

`team/` is shared context — guidelines, criteria, and style that the team agrees on and agents apply consistently. It's written collaboratively and maintained collaboratively.

When a team Compass is in use, individual team members may also have personal Compasses. The two don't conflict: agents use the team Compass for team work (proposal reviews, external communications, hiring decisions) and personal Compasses for personal work (drafting emails, capturing individual decisions).

## Files in this folder

**`guidelines.md`** — The team's working agreements and standards. The constitution that drives agent behavior on team tasks. Think of it as the document every agent reads before touching anything that belongs to the team.

**`style.md`** — The team's collective voice for external communications. Different from personal voice — this is what the team sounds like, not what any one person sounds like.

**`feedback_log.md`** — A structured log of feedback observations. Agents and team leads append to this. Periodically reviewed to propose updates to guidelines and criteria.

**`criteria/`** — One file per evaluation type. The canonical example is `criteria/proposal-review.md` — specific scoring dimensions, deal-breakers, and thresholds for a given type of recurring evaluation. Each file is self-contained: an agent can do a competent review by reading only the relevant criteria file and the task at hand.

## Canonical example

The proposal-review setup described in the main README is the most worked-out example of a team Compass in use. See `examples/team-proposal-review-example/` for a complete populated version. The flow:

- Proposals come in
- Agent reads `team/criteria/proposal-review.md` and reviews the proposal
- Team lead reviews and comments
- Agent extracts feedback into `team/feedback_log.md`
- Weekly, an agent proposes guideline updates to `refinements/pending/` based on feedback patterns
- Team lead reviews and accepts or rejects the proposed updates

Any recurring team evaluation task can follow this pattern. Substitute your own criteria file.

## Getting started

1. Copy the templates from this folder into your team Compass
2. Fill in `guidelines.md` — rough drafts are fine; agents can work with incomplete content
3. Create a criteria file for any recurring evaluation task the team does
4. Connect your chosen agent tool using the relevant recipe
5. Review and refine the guidelines as feedback accumulates
