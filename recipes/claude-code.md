# Recipe: Claude Code

Connect Claude Code to your compass-md so coding sessions benefit from your voice, preferences, and decisions — and so Claude Code can propose refinements as it observes your patterns.

---

## Setup (5 minutes)

### 1. Locate your Compass

For Claude Code, a local Compass is the natural fit. Recommended path: `~/compass/`. If your Compass currently lives in Drive, you can either:
- Sync the Drive folder locally (use Drive Desktop or rclone)
- Or maintain a separate local Compass for code work

### 2. Add a CLAUDE.md or AGENTS.md to the Compass folder

In `~/compass/`, create a `CLAUDE.md` file:

```markdown
# Claude Code Instructions

This directory is my compass-md following the v0.1 convention.

## What this is

This folder contains my personal context Compass. The structure follows
the compass-md convention (see COMPASS.md for details).

## How to interact with this Compass

When I'm working in this directory or you're acting on my behalf:

1. Read COMPASS.md first to understand conventions
2. Read relevant Compass files based on the task:
   - Code style questions → self/preferences.md (look for "Tools and workflows" section)
   - Drafting commit messages, PR descriptions, docs → self/voice.md
   - Architectural recommendations → self/perspectives/ if relevant topics exist
   - Context about projects I'm working on → self/facts.md
3. When generating output (commit messages, PR descriptions, code comments,
   documentation), match the voice from self/voice.md
4. Cite Compass files you used: "Drawing on self/voice.md and self/preferences.md..."

## Refinement workflow

When you observe something that warrants a Compass refinement:

1. Don't modify Compass files directly
2. Create a file in refinements/pending/ following the format in
   templates/refinements/EXAMPLE-refinement.md
3. Append to log.md: ## [YYYY-MM-DD HH:MM] refinement-proposed | description
4. Maximum 3 refinements per session
5. Only propose medium+ confidence refinements
```

### 3. Open Claude Code in the Compass directory

```bash
cd ~/compass
claude
```

Claude Code automatically reads CLAUDE.md and follows the instructions.

### 4. For other projects: reference the Compass from their CLAUDE.md

When working in a code project elsewhere on your machine, add to that project's CLAUDE.md:

```markdown
## Personal Compass

I have a compass-md at ~/compass/. When generating commit messages,
PR descriptions, documentation, or any other content that should reflect
my voice and preferences, read the relevant files there first.

Specifically:
- Voice for written content: ~/compass/self/voice.md
- Coding preferences: ~/compass/self/preferences.md (Tools and workflows section)
- Relevant perspectives: ~/compass/self/perspectives/

If you observe patterns worth capturing in the Compass, propose
refinements to ~/compass/refinements/pending/ following the convention.
```

This way every code project benefits from your central Compass without duplicating context.

---

## What to expect

Claude Code is great for this because it has filesystem access — it can read Compass files directly, write refinement files directly, and even apply accepted refinements to Compass files when you tell it to.

After a few sessions, expect:
- Commit messages and PR descriptions in your voice
- Code comments and docs that match your style
- Architectural suggestions that respect your stated perspectives
- Refinement proposals when Claude Code notices patterns

---

## Tips

**Use Claude Code to maintain the Compass itself.** When you want to update Compass files, work with Claude Code to do it cleanly. "Read voice.md and add a section about how I write commit messages" is a great Claude Code task.

**Use Claude Code to review pending refinements.** "Read refinements/pending/, summarize each one, and recommend which to accept based on whether they align with the rest of the Compass." Faster than reviewing manually.

**Keep Compass-related git history clean.** If your Compass is in a git repo (recommended), commit Compass updates separately from work commits. "Compass: accept voice refinement re: commit message style" reads better than mixing it into a feature commit.

**Periodic lint.** Once a month, ask Claude Code: "Lint my Compass per the convention. Check for contradictions, stale claims, orphan content, missing cross-references. Output findings to lint/{today}.md."

---

## Limitations

If your Compass is in Drive (synced locally) and Drive sync conflicts happen, you can lose Compass edits. Consider keeping the Compass in a local git repo as the source of truth and syncing TO Drive if you need it accessible from elsewhere, rather than the other way around.

Claude Code is best for users who are comfortable with terminal and git. Less technical users probably want the Cowork or Claude.ai recipes instead.
