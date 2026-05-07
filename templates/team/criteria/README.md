# Criteria

One file per evaluation type. Each file is self-contained: an agent can do a competent evaluation by reading only the relevant criteria file and the item being evaluated.

---

## When to create a criteria file

Create a file for any recurring evaluation task where:
- The team does it more than occasionally
- Quality depends on applying consistent standards
- An agent should be able to do a first-pass evaluation

Good candidates: proposal reviews, contract reviews, candidate screening, content quality checks, code review standards, vendor evaluation.

Don't create a file for one-off evaluations. Write the criteria in the task itself and capture any reusable patterns here afterward.

## File naming

Use descriptive, hyphenated names that make the evaluation type clear:
- `proposal-review.md`
- `contract-review.md`
- `hiring-screening.md`
- `content-quality.md`

## File structure

Each criteria file should have:

```markdown
# [Evaluation type] Criteria

## Purpose

[What this evaluation is for. One paragraph.]

## Required inputs

[What the evaluating agent needs to do a complete review.]

## Evaluation dimensions

[The scoring or assessment framework. Each dimension should have:]
- Name and weight (if applicable)
- What good looks like
- What weak looks like
- Deal-breakers for this dimension

## Deal-breakers

[Conditions that disqualify regardless of other scores.]

## Output format

[How the evaluation should be structured. Paste the template if there is one.]

## Notes for agents

[Any gotchas, common mistakes, or special instructions.]
```

## The canonical example

`criteria/proposal-review.md` is the most worked-out example in this repo. If you're creating your first criteria file, use it as a reference for level of detail and structure. The relevant example lives in `examples/team-proposal-review-example/team/criteria/proposal-review.md`.
