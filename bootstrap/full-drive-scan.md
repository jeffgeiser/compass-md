# Bootstrap: Full Drive Scan

A prompt that has Cowork (or any Drive-connected AI tool) scan your Google Drive and produce drafts for your Compass files.

---

## When to use this

When you want to bootstrap your Compass quickly using what's already in your Drive, rather than starting from blank templates or doing a long interview.

This is the highest-leverage bootstrap option because Drive contains the most material to work with. It's also the highest-risk because AI inference from Drive content can produce plausible-sounding but incorrect output. Review carefully.

## What this produces

Draft versions of `self/facts.md`, `self/voice.md`, `self/preferences.md`, and `self/decisions.md`. The drafts are starting points — review and edit before saving as your final substrate.

This bootstrap deliberately does NOT produce `self/perspectives/` files. Perspectives inferred from Drive content tend to be plausible-but-wrong. Use the `interview-perspectives.md` bootstrap for those instead.

## How to use

1. Make sure Cowork (or your AI tool) has Drive connector enabled
2. Identify which folders in your Drive contain the most representative content. Good candidates: your "about me" docs, your writing folder, your meeting notes folder, your projects folder. Skip junk folders, archived tax returns, shared docs from other people that you didn't write, etc.
3. Open Cowork in a fresh conversation
4. Paste the prompt below, customizing the folder list
5. Watch Cowork work through the scan (this can take 5-15 minutes for a substantial Drive)
6. Review the output carefully before saving anything to your Compass

## Time required

- Setup and prompt customization: 10 minutes
- Cowork scan: 5-15 minutes
- Human review and editing: 30-60 minutes
- **Total: ~1 hour**

This is faster than manual creation but the review step is non-negotiable. Skipping review means accepting AI inferences that may be wrong.

## The prompt

```
I want to bootstrap my Compass (a personal context substrate following the
compass-md convention v0.1) by scanning my Google Drive content.

Scan the following folders:
- [List your folders here, e.g., /My Drive/Writing, /My Drive/Notes, /My Drive/About Me]
- [Add as many as relevant]
- Skip anything in: /Tax, /Archive/Old Projects, /Shared from others
  [customize this exclusion list]

Your task is to produce drafts for four files. For each file, follow the
specific guidance below.

================================================================
FILE 1: self/facts.md
================================================================

Reliability: HIGH. Drive should contain explicit factual content.

Look for:
- Resume, CV, or "about me" documents
- Email signature blocks
- Project bios or "team" documents that mention me
- Calendar invites or meeting notes that mention my role
- Profile docs

Extract stable facts:
- Name, role, organization, location, time zone
- Current focus areas
- Key relationships (collaborators, manager, direct reports)
- Background and expertise areas

Output format:
[Use the facts.md template structure]

For each fact, cite the source document so I can verify.

================================================================
FILE 2: self/voice.md
================================================================

Reliability: MEDIUM. Drive contains my writing but it's mostly output for
audiences, not private voice.

Look for:
- 5-15 emails I've sent (Gmail integration if available, or sent email
  archives in Drive)
- Documents I authored (not collaborated on with many others)
- Project briefs, memos, or other prose I wrote

Sample diverse contexts: formal client emails, casual internal docs, longer
prose. Don't just sample one type.

Extract:
- Tone and register patterns (with examples from samples)
- Vocabulary preferences (words I gravitate toward, words I avoid)
- Sentence structure tendencies
- Recurring patterns

Output format:
[Use the voice.md template structure]

CRITICAL: For each pattern you describe, cite the specific sample where
you observed it. Mark inferences clearly:
- HIGH CONFIDENCE: pattern appears consistently across 3+ samples
- MEDIUM CONFIDENCE: pattern appears in some samples
- LOW CONFIDENCE: weak inference, may not be a real pattern

I will use confidence markers to decide what to keep vs. cut.

================================================================
FILE 3: self/preferences.md
================================================================

Reliability: MEDIUM-LOW. Drive rarely contains explicit preference statements.

Look for:
- Explicit statements like "I prefer X" or "I always do Y" in any documents
- Patterns in how I structure things (recurring formats, naming conventions)
- Consistent stylistic choices across documents
- Signature behaviors visible in meeting notes or planning docs

Extract:
- Communication preferences (when explicit)
- Decision-making style (when inferable from how I've documented decisions)
- "Things I always want" (when explicitly stated or strongly patterned)
- "Things I never want" (when explicitly stated)
- Working hours and availability (from calendar patterns or stated)

Output format:
[Use the preferences.md template structure]

CRITICAL: Mark every entry with confidence:
- EXPLICIT: I literally stated this somewhere (cite the document)
- PATTERNED: Inferred from consistent behavior across documents (cite examples)
- WEAK: Possible inference, low confidence (this should be rare; prefer to omit)

Do not invent preferences. If you can't find evidence for a preference,
leave that section empty rather than filling it with plausible guesses.

================================================================
FILE 4: self/decisions.md
================================================================

Reliability: MEDIUM. Drive contains records of decisions but reasoning
is often not written down.

Look for:
- Meeting notes that record decisions ("Decided to..." "Will go with...")
- Project briefs that document a chosen direction
- Planning docs that record choices made
- Email exchanges where a decision was reached

Extract significant decisions (not minor ones):
- Date of decision (from document timestamps when explicit)
- What was decided
- Context that prompted the decision (when documented)
- Reasoning given (when documented)
- Outcome (when known from later documents)

Output format:
[Use the decisions.md template structure, most recent first]

For each decision, cite the source document. If reasoning isn't documented,
say so explicitly: "Reasoning: [not documented in source]" rather than
making it up.

================================================================
WHAT NOT TO DO
================================================================

DO NOT produce content for self/perspectives/. Inferred perspectives from
Drive content tend to be plausible-but-wrong. The user will populate
perspectives separately through interview.

DO NOT invent content to fill empty sections. Empty is better than wrong.
The user wants to know where the substrate is thin so they can choose
what to add manually.

DO NOT pad the output. Concise, accurate drafts beat comprehensive guesses.

DO NOT proceed to file 2 until I've reviewed file 1. Show me each draft,
wait for me to confirm I've reviewed it, then move to the next file.

================================================================
OUTPUT FORMAT
================================================================

Show me your scan plan first:
1. Confirm which folders you'll scan
2. Estimate how many files you'll review
3. Confirm you understand the four file outputs and the no-perspectives rule
4. Wait for me to say "proceed"

Then produce the four files one at a time, waiting for my review between
each.

Begin with the scan plan.
```

---

## Reviewing the output

For each file Cowork produces:

**facts.md:** Read each fact. Verify against your actual current state. Cross out anything stale or wrong. Add facts the scan missed. This file should end up close to what Cowork produced for most fields.

**voice.md:** Read critically. Cross out claims you don't agree with. Cowork will produce plausible-sounding patterns that may not actually be how you write. Keep only what feels true. The HIGH/MEDIUM/LOW confidence markers should guide your trust.

**preferences.md:** This is where the most editing will happen. Cowork will produce inferred preferences with various confidence levels. Keep only EXPLICIT preferences and the PATTERNED ones you actually agree with. Cut everything else. Empty sections are fine.

**decisions.md:** Verify each decision is real and the date/context is accurate. Cross out anything Cowork misread. Add reasoning to important entries based on what you actually remember (Drive may not have captured the real reasoning).

Plan to spend 30-60 minutes on the review. The bootstrap saves time vs. manual creation, but only if you actually do the review.

---

## After the bootstrap

You now have draft substrate files. Two more steps:

1. **Save to Drive.** Move the reviewed files to your `compass/self/` folder. Update `compass/COMPASS.md` "File coverage" section to reflect what's populated.

2. **Populate perspectives separately.** Use `bootstrap/interview-perspectives.md` to add 3-5 perspective files for topics you actually have views on. This typically takes 30-45 minutes.

After both steps, your Compass has a real foundation. From here, the daily/weekly use loop in `GETTING_STARTED.md` takes over and the substrate compounds through use.

---

## What this bootstrap is not good at

A few honest limitations:

**Private voice vs. public voice.** Drive contains output you wrote for audiences. Your private voice — how you write to yourself, how you'd talk casually — isn't really there. Voice.md from a Drive scan captures your public-facing voice. That's still useful but it's not the whole picture.

**Recent context.** Drive contains historical material weighted by what's been there longest. Your most recent perspectives, current focus areas, and present-day preferences may not be well-represented. The bootstrap produces a substrate that reflects who you've been, not necessarily who you are right now.

**Tacit knowledge.** Most of what makes you distinctive isn't in your Drive. It's in your head, in conversations you've had, in choices you've made for reasons you didn't write down. The Drive scan can't capture this. Use the interview bootstrap to surface it.

**Things you've never written about.** If you've never written about a topic, the scan can't infer your view on it. Don't expect the bootstrap to produce a comprehensive substrate — expect it to populate the categories where Drive has signal, and accept that other categories need other approaches.

---

## When to redo this bootstrap

You can re-run a Drive scan periodically. Useful situations:

- After a significant role change, to refresh facts.md based on new Drive content
- When you've been through a substantial body of new work and want to update voice patterns
- When you suspect the substrate has gotten stale

A monthly scan is too much. A quarterly or annual scan can be useful. Each time, do it as a "propose updates" exercise — produce drafts, compare to your current substrate, accept the meaningful changes via the normal refinement workflow.
