# Recipe: Cursor

**Storage assumed: Local filesystem or Git repository.** Cursor reads files from your machine. If your Compass is in Drive, sync it locally first (Drive Desktop or rclone) before continuing.

Connect Cursor to your compass-md so coding sessions benefit from your voice, preferences, and decisions.

> **Is a prompt alone enough?**
> No. Cursor applies `.cursorrules` automatically at the start of every session in a project — that's how it gets instructions. Pasting a prompt works for one conversation but is forgotten when the session ends. You need a `.cursorrules` file in your Compass folder *and* a compass reference in each code project's `.cursorrules`. Once those files exist, every Cursor session in those projects is automatically Compass-aware.

---

## Setup (5 minutes)

### 1. Locate your local Compass

Your Compass should be on the local filesystem. Recommended path: `~/compass/`. If your Compass is in Drive and you haven't synced it locally, do that first before continuing.

### 2. Add a `.cursorrules` file to your Compass folder

In `~/compass/`, create a `.cursorrules` file:

```
You are working in my compass-md, which follows the compass-md convention v0.1.

Before acting on my behalf:
1. Read COMPASS.md to understand the conventions
2. Read the Compass files relevant to the task:
   - Drafting content → self/voice.md and relevant self/perspectives/
   - Preferences and defaults → self/preferences.md
   - Context about me → self/facts.md
   - Prior decisions → self/decisions.md
3. Act with that context informing your output
4. Cite which Compass files informed your output

When you observe something worth capturing as a refinement:
- Don't modify Compass files directly
- Create a file in refinements/pending/ following the format in templates/refinements/EXAMPLE-refinement.md
- Append to log.md: ## [YYYY-MM-DD HH:MM] refinement-proposed | description
- Maximum 3 refinements per session
```

### 3. Reference the Compass from your code projects

**This step is required for Compass context to apply to your actual work.** The `.cursorrules` in `~/compass/` only applies when you open Cursor *inside* the compass folder. For every code project where you want Compass context, you need a compass reference in that project's own `.cursorrules`.

For each code project where you want Compass context, add a `.cursorrules` reference:

```
## Personal Compass

I have a compass-md at ~/compass/. When generating commit messages,
PR descriptions, documentation, or other written content, read the
relevant files there before drafting.

- Voice: ~/compass/self/voice.md
- Preferences: ~/compass/self/preferences.md
- Relevant perspectives: ~/compass/self/perspectives/
- Prior decisions: ~/compass/self/decisions.md

If you observe something worth capturing, propose a refinement to
~/compass/refinements/pending/ following the compass-md convention.
```

### 4. Test

Open your Compass folder in Cursor. Ask it to draft something — a commit message, a readme, a design doc. The response should cite Compass files. If it doesn't, check that `.cursorrules` is in the right folder and that Cursor's rules file feature is enabled in settings.

---

## What to expect

Cursor reads `.cursorrules` at the project level, so Compass context applies to everything you do in that project window. When you work in your code projects with the Compass reference in `.cursorrules`, Cursor will consult the Compass for written outputs.

Cursor has filesystem access, so it can write refinement files directly to `refinements/pending/`. Whether it does depends on the instructions and whether it observes something worth capturing.

---

## Tips

**Cursor's context window is large but not infinite.** If your Compass grows (many perspective files), reference only the most relevant ones in `.cursorrules` rather than the entire `self/` folder. Add specific files as you discover which ones matter for coding work.

**`.cursorrules` is project-scoped.** Each project has its own `.cursorrules`. If you work across many projects, a short Compass reference in each project's `.cursorrules` is more useful than a very detailed one — you want agents to read the Compass files directly rather than relying on a summary.

**Commit your `.cursorrules`.** If your Compass is in a git repo (recommended), commit `.cursorrules` there. If it's a reference in a code project, commit it alongside the code — it's part of the project's development environment.

---

## Limitations

Cursor's `.cursorrules` affects behavior within the current project window. Context doesn't carry across unrelated projects unless you add the Compass reference to each one.

Local-only: Cursor can't read files directly from Drive. If your Compass is Drive-based, use the Cowork or Claude.ai recipes for Drive-native access and keep Cursor for local work.
