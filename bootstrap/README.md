# Bootstrap Prompts

Prompts for initializing a Compass from existing material. Use these when starting from scratch or when you want to enrich an existing Compass quickly.

---

## When to bootstrap

A blank Compass is better than no Compass, but agents need *something* to read for the convention to be useful from session one. Bootstrap prompts help you get to a useful first draft in about an hour instead of starting completely empty.

Bootstrap outputs are always drafts. Review carefully before saving to your Compass. Models can produce plausible-sounding-but-wrong inferences, especially about voice and perspective. Your job is to keep what's accurate and cross out what isn't.

---

## Start here: full Drive scan (recommended)

### [`full-drive-scan.md`](full-drive-scan.md) ★ Recommended starting point

**Use when:** You already have a meaningful amount of content in Google Drive — writing, notes, docs, project files. This is most people.

**What it produces:** Draft versions of `self/facts.md`, `self/voice.md`, `self/preferences.md`, and `self/decisions.md` — the core of a personal Compass — produced by Cowork scanning your Drive content directly.

**Why start here:** Drive contains more signal about you than any other single source. A Drive scan produces more comprehensive starting drafts than manual creation, and it catches patterns you wouldn't have thought to write down. The tradeoff is that the output requires careful review — AI inference from Drive content can produce plausible-but-wrong claims, especially for voice and preferences.

**Time:** ~1 hour total (10 min setup, 5-15 min scan, 30-60 min review)

**Note:** This bootstrap deliberately does NOT produce `self/perspectives/` files — use the interview bootstrap for those. Perspectives inferred from Drive content tend to be wrong.

---

## After the Drive scan: what to do next

Once you have draft facts/voice/preferences/decisions from the Drive scan:

1. **Add perspectives** using [`interview-perspectives.md`](interview-perspectives.md) — this is the step the Drive scan can't do for you.
2. **Tune voice specifically** using [`voice-from-writing-samples.md`](voice-from-writing-samples.md) if you want to go deeper on voice than the Drive scan reached.
3. **For team Compasses**, see [`team-guidelines-from-history.md`](team-guidelines-from-history.md).

---

## All bootstrap prompts

### [`full-drive-scan.md`](full-drive-scan.md)

**Best for:** facts.md, voice.md, preferences.md, decisions.md — the recommended starting point for anyone with Drive content.

**Input:** Your Google Drive (Cowork scans it directly).

**Output:** Draft substrate files for the four core categories. Produces more comprehensive output than other bootstraps because it works from everything you've written, not just samples you select.

**Time:** ~1 hour.

---

### [`interview-perspectives.md`](interview-perspectives.md)

**Best for:** `self/perspectives/` files — required for perspectives regardless of how you do the rest of your bootstrap. Also surfaces tacit knowledge the Drive scan can't reach.

**Why perspectives need the interview:** Drive content shows what you've written, not what you actually think. Perspectives inferred from past writing tend to be plausible-but-wrong. The interview elicits your actual views through follow-up questions.

**Input:** Just yourself — the prompt conducts a conversational interview.

**Output:** Draft perspective files, and possibly additions to `preferences.md` and `decisions.md`.

**Time:** 45-60 minutes for a meaningful interview.

---

### [`voice-from-writing-samples.md`](voice-from-writing-samples.md)

**Best for:** Focused, deep tuning of `self/voice.md` when you want more precision than the Drive scan produced.

**When to use instead of (or after) the Drive scan:** When you have specific writing samples you want analyzed in detail, or when the Drive scan's voice output doesn't feel precise enough. This bootstrap is slower but produces more specific observations.

**Input:** 5-15 samples of your writing across contexts. You select and paste these, so you control exactly what the model sees.

**Output:** A draft `self/voice.md` with confidence-marked observations and specific examples.

**Time:** 20-30 minutes.

---

### [`team-guidelines-from-history.md`](team-guidelines-from-history.md)

**Best for:** Bootstrapping a team Compass — extracting `team/guidelines.md` and possibly a criteria file from past team work.

**Input:** Examples of the team's past outputs and any written guidelines that exist.

**Output:** A draft `team/guidelines.md` and possibly a draft criteria file.

**Time:** 30-45 minutes.

---

### [`facts-from-resume.md`](facts-from-resume.md)

**Best for:** A quick `self/facts.md` when you don't want to do a full Drive scan — just paste your resume and get structured output.

**When to use instead of the Drive scan:** When you don't have Cowork's Drive connector set up, or when your Drive is thin but your resume is comprehensive. This is the lowest-friction bootstrap for facts.md specifically.

**Input:** Your resume, LinkedIn profile, or any "about me" document.

**Output:** A structured draft `self/facts.md`.

**Time:** 10-15 minutes.

---

## After bootstrapping

1. Review each output file carefully
2. Cross out anything that doesn't ring true
3. Add anything that's missing or that the model wouldn't have known
4. Save the edited version to your Compass
5. Follow the daily/weekly rhythm in [`GETTING_STARTED.md`](../GETTING_STARTED.md) — the Compass compounds through use, not through perfecting the initial bootstrap
