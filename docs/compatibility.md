# Compatibility with Existing Conventions

How compass-md relates to other AI context conventions and tools.

---

## CLAUDE.md and AGENTS.md

`COMPASS.md` does not replace `CLAUDE.md` or `AGENTS.md`. They serve different purposes and can coexist.

- **`CLAUDE.md` / `AGENTS.md`**: instructions to the AI agent about how to operate in a specific project or repository — coding conventions, testing patterns, deploy instructions, repository-specific protocols.
- **`COMPASS.md`**: instructions to the AI agent about how to read and contribute to a personal or team context Compass — who the owner is, what conventions the Compass follows, how to propose refinements.

A typical setup for a technical user:
- `~/myproject/CLAUDE.md` tells Claude Code about the codebase conventions
- `~/compass/COMPASS.md` tells any agent about the personal Compass
- The project's `CLAUDE.md` references the personal Compass at `~/compass/` for voice and preferences

The two files don't conflict because they answer different questions: CLAUDE.md answers "how do I work in this codebase?" and COMPASS.md answers "who am I working for and what do they care about?"

---

## Karpathy's LLM Wiki pattern

The compass-md convention is directly inspired by [Andrej Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The core insight — use a schema file to tell an LLM how to maintain a markdown knowledge base, then let the LLM maintain it — is Karpathy's.

compass-md applies that pattern specifically to personal and team context rather than topical knowledge bases:

| | Karpathy's LLM Wiki | compass-md |
|---|---|---|
| **Purpose** | Topical knowledge base (what I know about X) | Personal/team context (who I am, what I value) |
| **Schema file** | Custom | `COMPASS.md` |
| **Refinement workflow** | Agent writes directly | Agent proposes, human reviews |
| **Multi-user** | Designed for individuals | Supports both individual and team |
| **Storage** | Local or any | Any; Drive recommended |

The two patterns can coexist. A person could maintain both a topical wiki (for domain knowledge) and a personal Compass (for voice, preferences, perspectives). They serve different jobs.

---

## Notion AI

Notion AI can read and operate on Notion pages within your workspace. If your Compass content lives in Notion, Notion AI can interact with it.

compass-md works alongside Notion:
- You can keep a Notion version of your Compass and sync the markdown files (Notion supports markdown export)
- You can use Notion as the human-facing interface and keep the canonical Compass as markdown files in Drive
- Notion AI doesn't support the full refinement workflow (files in refinements/pending/) but can approximate it with database entries

The Compass files are portable to and from Notion. The convention is in the structure and content, not in any tool.

---

## Obsidian

Obsidian natively reads markdown files and has a graph view for linking between files. A Compass in a local folder is a natural fit for Obsidian:

- Browse your Compass in Obsidian's vault
- Use Obsidian's backlink features for cross-references between perspective files
- Obsidian's git plugin syncs changes if you want version history

Obsidian doesn't run AI agents natively (some plugins add this), but it's an excellent human interface for browsing and editing a local Compass. Combine with the Claude Code recipe for the agent layer.

---

## Roam Research

Roam's bidirectional linking and block-level organization map reasonably well to the Compass convention. The `[[double-bracket]]` link syntax can cross-reference between files.

compass-md doesn't require any specific linking syntax — cross-references can be markdown links or plain text mentions. If you're a Roam user, you can maintain your Compass in Roam and use Roam's export to generate the markdown files that agents read. The friction is in keeping the two in sync.

---

## mem0 and AI memory tools

Tools like mem0 attempt to solve the same problem — persistent AI memory across sessions — using a different approach: a managed service that intercepts agent conversations and extracts memories automatically.

The tradeoffs:
- **mem0 / managed memory:** lower setup friction, automatic extraction, but memory lives in their service, not yours
- **compass-md:** higher setup friction, human-reviewed refinements, but fully portable and you own the data

The two aren't mutually exclusive. A Compass gives you a human-curated, portable context layer; a memory service can add automatic ambient capture. If you use both, make sure they're not contradicting each other — a managed memory service that captures something your Compass explicitly says to avoid can produce confusing agent behavior.

---

## Custom instructions in ChatGPT and Claude.ai

Both products have custom instructions features — persistent text that gets included in every conversation. These are:

- Product-specific (locked to that product)
- Limited in length
- Not version-controlled or inspectable

compass-md is complementary: use the full Compass as the source of truth and use custom instructions as a compressed summary for tools that don't support file access. When the tool does support file access (Claude.ai Projects with Drive, Cowork), use the files directly rather than the compressed summary.

---

## GitHub Copilot

Copilot doesn't have a native file-reading mechanism for personal context (as of v0.1). The compass-md convention doesn't have a Copilot recipe for this reason.

If Copilot ships a context file convention (similar to CLAUDE.md or .cursorrules), a recipe can be added. Until then, the Claude Code or Cursor recipes are the closest analog for IDE-based coding workflows.

---

## AGENTS.md (the broader convention)

The [AGENTS.md convention](https://www.agentprotocol.ai/) is emerging as a standard for agent instructions at the repository level. It's similar in purpose to CLAUDE.md — repo-level agent instructions — rather than personal context.

compass-md is compatible with AGENTS.md: put AGENTS.md at the repo level for repo-specific instructions, and reference the personal Compass from AGENTS.md for voice and preferences.
