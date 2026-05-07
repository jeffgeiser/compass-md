# Getting Started with Compass

A practical walkthrough for someone who just set up a Compass in Google Drive and wants to know what to do next. No dashboard required — just Drive and your AI tool of choice.

---

## What you have at this point

Assuming you followed the Setup section in the README, you have:

- A `compass` folder in Google Drive with the template files copied in
- A `COMPASS.md` schema file that you've customized for yourself
- Initial drafts of `self/voice.md`, `self/preferences.md`, and `self/facts.md`
- A Cowork project (or Claude.ai Project) configured to read from your Compass

Now what?

---

## The basic loop

Using a Compass is mostly four activities, repeated:

1. **Use AI tools normally** — drafting, planning, evaluating, deciding
2. **Notice when AI tools propose refinements** to your Compass
3. **Review pending refinements** in the `refinements/pending/` folder
4. **Periodically lint and curate** the Compass to keep it healthy

Most of the value comes from steps 1 and 3. Steps 2 and 4 are what make the loop compound over time.

---

## Day one: bootstrap your Compass

Before connecting AI tools, populate the substrate. An empty Compass produces no value.

**Time investment: ~60 minutes.**

**Faster option: Drive scan.** If your Drive already contains a lot of your writing, documents, and notes, you can have Cowork (or any Drive-connected AI tool) scan it and produce drafts for facts.md, voice.md, preferences.md, and decisions.md. See `bootstrap/full-drive-scan.md` for the prompt. This produces drafts in 5-15 minutes that you then review (~30-60 minutes). Total: about an hour, similar to manual but produces more comprehensive starting drafts.

If you go this route, follow the Drive scan bootstrap, then come back here for steps 4-5 (creating perspective files and updating COMPASS.md). For perspectives specifically, use the interview bootstrap rather than the Drive scan — perspectives inferred from Drive content tend to be wrong.

**Manual route below if you prefer to start from scratch:**

### 1. Open `self/voice.md` in Drive

Spend 15 minutes filling in the sections. Don't aim for completeness — aim for *honesty about what you actually do*. Look at recent emails or messages you've sent if you need examples.

The minimum useful content:
- 2-3 sentences describing your default tone
- 5-10 vocabulary preferences ("I avoid X, I prefer Y")
- 2-3 sentence-structure patterns you actually use

If you get stuck, use the `bootstrap/voice-from-writing-samples.md` prompt with your AI tool of choice. Paste in 5-10 of your recent emails or documents and ask for a draft.

### 2. Open `self/preferences.md`

Spend 10 minutes. Focus on the "Things I always want" and "Things I never want" sections — these are the highest-leverage content because agents use them to set defaults.

Examples that work well:
- "Never start an email with 'Hope this finds you well.'"
- "Always lead with the bad news rather than burying it."
- "When recommending a decision, give me 2-3 options before recommending one."
- "If I'm clearly wrong about something, push back. Don't just agree."

### 3. Open `self/facts.md`

Spend 5 minutes. Just put down the stable basics — name, role, location, current focus. Don't overthink this; it's reference material.

### 4. Optional: Create one perspective file

If there's a topic you have strong views on that you'd want agents to know about, create `self/perspectives/{topic}.md` and write a few paragraphs. Examples: pricing strategy, hiring philosophy, technical preferences, decision-making frameworks.

You don't need many of these on day one. One good perspective file is more useful than five thin ones. The collection grows naturally over time as agents propose new ones based on your work.

### 5. Update `COMPASS.md`

Now go back to your `COMPASS.md` schema file and update the "File coverage" section to reflect what you've populated. This tells agents which files have content worth reading.

---

## Day one: test the connection

Before relying on the Compass, verify your AI tool is actually using it.

### In Cowork (or Claude.ai)

Open your Compass-aware project and ask something that should trigger Compass reads:

> "Draft a quick email to a client telling them the project is delayed by a week. Match my voice."

The response should:
- Cite which Compass files it read at the end of the response (e.g., "Drawing on self/voice.md and self/preferences.md")
- Reflect your actual voice patterns from voice.md
- Avoid words you said you avoid in voice.md

If the response doesn't cite Compass files, the integration isn't working. Re-check your project's custom instructions per the recipe.

If the response cites the files but doesn't actually match your voice, your voice.md may not be specific enough. Read what was generated, identify what's off, and add more specific guidance to voice.md.

---

## The daily flow

Once your Compass is set up, daily use is mostly invisible:

### Just use AI tools normally

When you have work to do (drafting, evaluating, recommending), use your Compass-aware project. The Compass does its job in the background — agents read it before responding, your output is more aligned with you than it would be otherwise.

You don't need to think about the Compass during normal use. If you're consciously managing it, something is wrong.

### Watch for refinement proposals

Periodically — at the end of a session, or when you correct an agent's output meaningfully — the agent should propose a refinement to your Compass. This shows up in two places depending on the tool:

**In Cowork:** A new file appears in `compass/refinements/pending/` in your Drive. Cowork creates it and writes the proposed change.

**In Claude.ai:** The proposal comes back as a section in the chat response (Claude.ai can't write to Drive directly). You manually save it to `refinements/pending/` if you want to keep it for review.

If proposals never come, the agent isn't following the convention's refinement workflow. Check your project's custom instructions.

If proposals come too often (more than 2-3 per session consistently), the cap in your custom instructions isn't being respected. Tighten the instructions.

---

## The weekly review (most important habit)

This is the practice that determines whether your Compass actually compounds in value over time. **Set a recurring weekly time on your calendar — 15-30 minutes.**

### Step 1: Open `compass/refinements/pending/` in Drive

You'll see a list of proposed refinements. Each is a markdown file with a timestamp prefix. Open them one at a time.

### Step 2: For each pending refinement, decide

Read the refinement. It should have:
- An **Observation** section explaining what the agent noticed
- A **Proposed change** section with the actual edit
- A **Reasoning** section explaining why
- An **Evidence** section with specific examples

Decide one of three things:

**Accept it.** The proposed change is correct and worth keeping. To accept:

1. Open the target file (e.g., `self/voice.md`) in Drive
2. Apply the proposed change manually — paste the new content, or modify the existing content as proposed
3. Save the target file
4. Move the refinement file from `refinements/pending/` to `refinements/accepted/` (right-click → Move to in Drive)
5. Append a line to `log.md` (in Drive): `## [YYYY-MM-DD HH:MM] refinement-accepted | brief description`

**Reject it.** The proposed change isn't right — the agent misread the situation, the pattern wasn't real, or the change would harm the Compass. To reject:

1. Open the refinement file
2. Add a section at the bottom: `## Rejection reason: [your explanation]`
3. Save
4. Move the file to `refinements/rejected/`
5. Append to `log.md`: `## [YYYY-MM-DD HH:MM] refinement-rejected | brief description | reason`

**Edit and accept.** The refinement is mostly right but needs adjustment. Edit the proposed change in the refinement file, then proceed as if accepting it.

### Step 3: Note any patterns

If you're consistently rejecting a certain type of refinement, that's signal. Maybe the agent is misreading something, or maybe your COMPASS.md instructions need to be tighter. Make a note for next week's review.

If you're consistently accepting refinements that mostly say the same thing (e.g., "user prefers shorter emails"), your underlying voice.md may be missing something fundamental. Update the source rather than accepting endless refinements that point at the same gap.

### Step 4: Done

That's the entire weekly review. 15-30 minutes, done.

---

## The monthly maintenance (lighter touch)

Once a month, do a quick health check on your Compass. **Set a recurring monthly time, ~30 minutes.**

### Step 1: Skim your substrate files

Open each of your `self/` files in Drive and read them. You're looking for:

- Things that are stale and no longer true (your role changed, your views evolved, your preferences shifted)
- Things you've been meaning to add but haven't
- Contradictions across files
- Sections that have grown too long and would benefit from being split

Make edits directly in Drive. Note significant changes in `log.md`.

### Step 2: Run a lint pass with your AI tool

In your Compass-aware project (Cowork, Claude.ai, etc.), ask:

> "Lint my Compass per the convention. Read all files in self/, look for: contradictions between files, stale claims, sparse categories, dense categories that should be split, missing cross-references between perspectives. Output the findings as a structured report I can review."

Read the report. Apply the obvious fixes. Note things you want to think about more.

### Step 3: Check refinement folders

Quick scan of `refinements/pending/`. If there are very old pending refinements (more than 2 weeks), either review them now or clean them up by rejecting with reason "stale, didn't get to it."

Quick scan of `refinements/rejected/`. If you see a pattern of similar rejections, consider updating COMPASS.md to instruct agents not to propose that type of refinement.

### Step 4: Done

Monthly maintenance complete. The Compass stays healthy.

---

## What "good" looks like over time

After a month of use, expect:
- Your voice.md has noticeably more specific content than your day-one draft
- You have 3-5 perspective files for topics that came up in your work
- Your decisions.md has 2-5 entries from real decisions
- Cowork's drafts feel more like yours than they did at the start
- You have a small accepted-refinements history showing how the Compass evolved

After three months, expect:
- Cowork drafts that often need only minor edits
- A clear sense of which Compass files matter most for which kinds of work
- Some intuition for when to add a new perspective file vs. when to update an existing one
- Possibly a custom modification to COMPASS.md based on what you've learned about how you work

After six months, expect:
- The Compass to feel genuinely personal — like a representation of you that you'd defend
- Compounding value: new AI tools you try are immediately better because they read your existing Compass
- Confidence that this approach is more valuable than per-tool memory features

If after three months you're not seeing this pattern, something is wrong with the loop. Most common causes:
- You're not reviewing pending refinements (they pile up unread)
- Your initial substrate was too thin and you didn't enrich it
- You're not actually using the Compass-aware project for relevant work
- The agent isn't actually reading the Compass (test by checking citations)

Diagnose and fix the underlying issue.

---

## Common situations and how to handle them

### "Cowork's draft sounds nothing like me"

Most common cause: voice.md is too generic. "Be direct and concise" doesn't help much. Specific patterns help — "Use dashes instead of semicolons. Never start a paragraph with 'However.' Cut hedging phrases like 'I think' or 'maybe.'"

Fix: Open voice.md, read what's there critically, add specific patterns from how you actually write. Save 3-4 examples of your real writing in the file as "before/after" pairs showing your voice in action.

### "I have no idea what to put in perspectives/"

Don't force it. Perspectives files only matter for topics you have actual stated views on. If you don't have strong views on something, that file shouldn't exist.

The right way to discover them: notice when you correct an agent's recommendation in a way that reflects a real position. "Actually, I'd push back on that — I think X because Y." That's a perspective. Capture it.

### "Pending refinements are piling up and I'm not getting to them"

This is the failure mode that kills the convention's value. The substrate doesn't compound if you don't review.

Two fixes: shorten the cadence (review every few days rather than weekly), or constrain the agent more aggressively in COMPASS.md so it proposes fewer refinements (only "high confidence" ones, only "addition" change types, etc.).

If you're consistently not getting to the review, the convention may not be a fit for you. That's okay to discover — better than building a graveyard of unreviewed proposals.

### "I want to share my Compass with a collaborator"

For team contexts, set up a shared Drive folder with both of you having access. Both of you connect your Cowork projects to the shared folder. Agree on conventions for who reviews refinements (e.g., only the team lead, or weekly review meeting).

For sharing scoped slices (e.g., letting a contractor see specific perspectives but not your full Compass): use Drive's per-file sharing to give them access only to the files they need. The convention doesn't care about access controls — that's Drive's job.

### "I want to use multiple AI tools"

You can. Set up a Cowork project, a Claude.ai Project, a Cursor `.cursorrules`, etc. — all pointing at the same Compass folder. Each tool reads independently; refinements from any tool land in the same `refinements/pending/` folder for unified review.

Be aware that different tools may propose conflicting refinements (Cowork's refinement says voice should be more direct; Claude Code's refinement says more polished). Your weekly review is where you reconcile these.

### "My Compass is getting really big"

If your Compass grows past ~30-50 files, agents may have trouble efficiently reading it. Two fixes:

1. **Use INDEX.md more aggressively.** Maintain a catalog file at the root that lists all files with one-line summaries. Update COMPASS.md to instruct agents to read INDEX.md first and then drill into specific files.
2. **Split into multiple Compasses.** Maybe one personal Compass for general work, one project-specific Compass for a particular initiative. Agents reading either get only the relevant context.

### "I want to migrate from Drive to local files (or vice versa)"

The convention doesn't care where files live. To migrate: copy the entire `compass` folder from current storage to new storage. Update your AI tool projects to point at the new location. Done.

---

## What to track

If you want to know whether the Compass is actually working for you, track these informally over your first couple of months:

- **Acceptance rate of refinements:** What percentage of proposed refinements do you accept? Healthy range is 30-70%. Below that, the agent is misreading you. Above that, you're being too permissive.
- **Time to draft vs. time to edit:** When you ask Cowork to draft something, are you spending less time editing than you used to? If yes, the Compass is delivering value. If no, something's off.
- **Compass file growth:** Are your substrate files getting noticeably richer week over week? Stagnation suggests the loop has broken.
- **Agent citation rate:** When you ask agents to do work, are they actually citing Compass files? If they stop citing, they may have stopped reading.

These aren't formal metrics — just honest periodic gut checks.

---

## When to ask for help

If you're stuck or the Compass isn't producing value:

- Check the FAQ in the main README
- Check the docs folder for specific topic docs
- Search closed issues on the compass-md GitHub repo
- Open an issue describing your situation

The community is small but engaged. Real questions help us improve the convention and the docs.

---

## Summary

Daily: use AI tools normally. They read the Compass automatically.

Weekly (15-30 min): review pending refinements in `refinements/pending/`. Accept good ones (apply to target file, move refinement file to accepted/), reject bad ones (move to rejected/ with reason).

Monthly (~30 min): skim substrate files for staleness, run a lint pass with your AI tool, scan refinement folders for old items.

That's it. The Compass works in the background. You curate periodically. The substrate compounds in value over time.
