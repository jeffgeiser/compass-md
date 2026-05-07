# Bootstrap: Team Guidelines from History

A prompt for extracting initial team guidelines from existing material — past decisions, completed work, retrospectives, or existing written guidelines.

---

## When to use this

When you're starting a team Compass and don't want to write `team/guidelines.md` from scratch. Most teams have implicit guidelines that are easier to extract and codify than to invent. This prompt surfaces them.

Works best when you have:
- Examples of the team's past outputs (proposals, reviews, decisions)
- Any existing documentation (even partial or outdated)
- Notes from retrospectives or feedback sessions

If you have nothing, use the interview approach in `interview-perspectives.md` adapted for a team setting — same principle, group conversation instead of individual.

## What this produces

- A draft `team/guidelines.md`
- Optionally, a draft criteria file for the team's primary recurring evaluation task

Review and edit before saving. The model will make inferences from the examples you provide; not all of them will be right.

## How to use

1. Gather your input material (see below)
2. Open Cowork, Claude.ai, or any capable LLM
3. Provide the materials
4. Paste the prompt below
5. Review the output with the team before saving to the Compass

## What to gather

**Examples of your best work.** 3-5 examples of outputs the team is proud of — proposals that won, reviews that were particularly useful, decisions that aged well. These give the model positive signal for what the team considers good.

**Examples of corrected work.** 2-3 examples where output was revised and why. If you have feedback emails, change requests, or annotation notes, these are gold. The corrections reveal implicit standards more clearly than any explicit doc.

**Any existing guidelines.** Even if they're outdated, incomplete, or just notes in a doc. The model can work with partial material.

**Context about what the team does.** 1-2 paragraphs describing the team's function, who it serves, and what "good" looks like from the outside.

## The prompt

```
I want to bootstrap team guidelines for a compass-md Compass. The team's
guidelines will be used by AI agents acting on the team's behalf.

Context about what this team does:
[paste your 1-2 paragraph description]

Examples of our best work:
[paste or attach 3-5 examples]

Examples of corrected work (with notes on what changed and why, if available):
[paste or attach 2-3 examples]

Existing documentation (even if partial or outdated):
[paste or attach]

Please produce:

1. A draft team/guidelines.md following this structure:
   - What this team does (1 paragraph)
   - Core standards (the non-negotiables observed across examples)
   - How we evaluate work (the dimensions that distinguish good from weak)
   - Deal-breakers (patterns that disqualified outputs in the corrected examples)
   - What gets escalated (situations where a human should decide)
   - Output format (structure and length norms from the examples)

2. If a primary recurring evaluation task is evident from the examples,
   a draft criteria file for that task following this structure:
   - Purpose
   - Required inputs
   - Evaluation dimensions (with what good vs. weak looks like for each)
   - Deal-breakers
   - Output format

For each inferred guideline, note where it comes from (which examples
suggested it). Mark low-confidence inferences clearly — I need to know
what to scrutinize vs. what to trust.

Do not invent guidelines that aren't visible in the examples. If the
examples are inconsistent on something, say so rather than picking one.

This is a draft for team review, not a final document.
```

---

## After generating

**Review with the team.** Guidelines that individuals created without team review often miss team disagreements. Walk through the draft in a short meeting. For each guideline: "Does this match how we actually operate?"

**Test against a real example.** Take a recent piece of work and evaluate it against the draft guidelines. Do the guidelines produce the right result? If not, adjust.

**Ship a v1, don't wait for perfect.** An 80% accurate guidelines doc connected to an agent is more valuable than a 100% accurate doc sitting in a doc editor. Ship it, use it for a week, refine based on what the agent gets wrong.
