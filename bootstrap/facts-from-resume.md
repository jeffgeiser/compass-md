# Bootstrap: Facts from Resume

A quick prompt for populating `self/facts.md` from your resume, LinkedIn profile, or any "about me" document.

---

## When to use this

When you want a structured `facts.md` without starting from a blank template. Paste your resume or LinkedIn and get a draft back in under 10 minutes.

This is deliberately the simplest bootstrap. `facts.md` is mostly structured information — role, organization, location, context — rather than inferred patterns. The model's job is formatting and extraction, not interpretation. Low risk of the model getting things wrong.

## What this produces

A draft `self/facts.md` ready to review and save. Most of what the model produces should be accurate; you'll mostly be adding context that wasn't in the source document rather than correcting errors.

## How to use

1. Copy your resume text, LinkedIn profile, or any bio/about-me document
2. Open any LLM
3. Paste the prompt with your source material
4. Review the output — add anything missing, remove anything confidential
5. Save to `self/facts.md`

## The prompt

```
I want to create a facts.md file for my compass-md Compass.

Here's my source material:
[paste your resume, LinkedIn, or about-me text]

Please produce a draft self/facts.md using this structure:

# Facts

Stable facts about me. Used by agents to ground their understanding of
who they're working with.

## Identity

- Name:
- Role:
- Organization:
- Location:
- Time zone:

## Context

- What I'm currently working on: [infer from most recent roles/projects]
- Primary focus areas: [infer from experience and current role]
- Constraints I'm operating under: [leave blank if not evident]

## Relationships

- Key collaborators: [only if evident from source material]
- Direct reports: [only if evident]
- Manager / who I report to: [only if evident]
- Important external contacts: [only if evident]

## Background

- [Relevant background that explains how I think — infer from career
  trajectory, domain shifts, notable experiences]
- [Domains of expertise — be specific, not generic]
- [Domains where I'm a novice — only if evident]

## Current state

- [Things in flux — infer from recent role changes, projects starting or ending]
- [Recent changes in role, focus, or context]

Rules:
- Only include information that's actually in the source material
- Leave fields blank if you'd be guessing
- Don't add generic filler ("strong communicator," etc.)
- Flag anything you're uncertain about

## Last updated

[today's date]
```

---

## After generating

**Add what's missing.** The resume captures your professional history but often misses your actual current context — what you're working on right now, what constraints you're operating under, what's changed recently. Add those manually.

**Remove anything you don't want in the Compass.** The Compass shouldn't include anything you'd be uncomfortable with if it were seen by someone you gave agent access to. Client names, financial details, sensitive projects — consider whether they belong here.

**Update when things change.** `facts.md` should reflect current reality. If you change roles, move cities, or shift focus, update the file. Six-month-stale facts are worse than no facts — agents make wrong assumptions based on them.
