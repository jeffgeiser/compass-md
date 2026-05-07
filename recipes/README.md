# Recipes

Instructions for connecting various AI tools to a Compass. Each recipe is self-contained: read it, follow the steps, and your chosen tool will read your Compass before acting on your behalf.

---

## Start here: Cowork (recommended)

**[`cowork.md`](cowork.md)** — Claude Cowork with Google Drive

Cowork is the recommended starting recipe for most people. It has native Drive integration, which means it can both read your Compass files and write refinement proposals back to your Compass folder — the full read-write loop without additional tooling. If you're not sure where to start, start here.

---

## Other recipes

**[`claude-ai.md`](claude-ai.md)** — Claude.ai Projects (Drive-connected)

Claude.ai Projects syncs your Drive folder automatically. Refinement proposals come back as text in the conversation (no direct file write), so you paste them into your Compass manually. Good for people already using Claude.ai as their primary AI surface.

**[`claude-code.md`](claude-code.md)** — Claude Code (local filesystem)

For terminal users who want a local Compass. Claude Code has full filesystem access, so it can read your Compass and write refinement files directly. Best for technical users who are comfortable with the CLI.

**[`cursor.md`](cursor.md)** — Cursor (local filesystem)

For Cursor users. Uses `.cursorrules` for project-level Compass instructions. Local Compass only.

**[`chatgpt.md`](chatgpt.md)** — ChatGPT custom instructions

ChatGPT's file access model is different from the others. The recipe covers Custom GPTs with file uploads and the custom instructions pattern. Good starting point if ChatGPT is your primary AI tool; acknowledge the limitations upfront.

**[`local-ollama.md`](local-ollama.md)** — Local models (Ollama, llama.cpp, etc.)

For fully-local setups. Works with any local model, but instruction-following for the read-write protocol varies by model. Use local Compass only.

---

## Combining recipes

Recipes can be combined. The most common pattern: use Cowork for active work (drafting, reviewing, planning) and Claude Code for Compass maintenance (accepting refinements, updating files, running lint). Each serves a different job.

You can also point multiple tools at the same Compass — each tool gets its own setup instructions, and they all read from the same source of truth.
