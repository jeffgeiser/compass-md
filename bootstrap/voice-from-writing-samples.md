# Bootstrap: Voice from Writing Samples

A prompt to extract a draft `voice.md` from samples of your existing writing.

---

## When to use this

When you have writing samples (emails you've sent, blog posts, project briefs, slack messages, etc.) and want to bootstrap a `self/voice.md` from them rather than starting blank.

## What this produces

A draft `voice.md` describing observed patterns in your writing. The output is a *draft* — review and edit before saving to your Compass. Inferred voice is not always accurate voice.

## How to use

1. Gather 5-15 samples of your writing. Mix of contexts (formal, casual, internal, external) is better than all one type. More samples ≠ better — quality matters more than quantity.
2. Open Cowork, Claude.ai, or any LLM with file access
3. Provide the samples (paste into chat, attach files, or point at a folder)
4. Paste the prompt below
5. Review the output. Cross out things that don't sound like you. Add things that are missing. Save the edited version to `self/voice.md`.

## The prompt

```
I want you to analyze these writing samples to draft a voice.md file
for the compass-md convention.

Samples are attached / pasted below.

Your output should follow this structure:

# Voice

How I write and speak. Used by agents drafting content on my behalf.

## Tone and register
[What's the dominant tone? How does it shift across contexts?]

## Vocabulary preferences
**I use:** [Words and phrases I gravitate toward, with examples]
**I avoid:** [Words and phrases conspicuously absent from my writing,
or that I deliberately don't use, with reasoning]

## Sentence and paragraph structure
[Patterns in how I structure things — sentence length, use of dashes,
paragraph length, etc.]

## Patterns I tend to use
[Recurring patterns observable across samples]

## Patterns I avoid
[Patterns that are conspicuously absent — what I don't do]

## Notes on confidence
[Sections where the inference is solid vs. where you're guessing.
Mark guesses clearly so I know what to scrutinize.]

Important rules:
- Cite specific samples for each observation ("In email 3, the user...")
- Mark low-confidence inferences clearly
- Don't invent patterns — only describe what's actually visible in the samples
- If samples are inconsistent on something, say so rather than picking one
- This is a DRAFT for human review, not a final voice document
```

---

## Tips for better output

**Sample diversity matters.** If all your samples are formal client emails, the inferred voice will only describe your client-email voice. Include casual messages, internal docs, and external-facing writing for a fuller picture.

**Recent samples are better.** Voice evolves. Samples from this year are more useful than samples from five years ago.

**Curate before submitting.** If you have an embarrassing email from a stressful week that doesn't represent how you usually write, don't include it. The model can't tell what's representative; you can.

**Review skeptically.** Inferred voice often has plausible-sounding-but-wrong claims ("the author values directness over diplomacy") that you'd want to cross out. Your job is to keep what's true and remove what isn't.

**Iterate.** First pass gets you a baseline. Use it for a week, notice where Cowork gets your voice wrong, refine the file based on what you learned.
