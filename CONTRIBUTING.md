# Contributing to compass-md

Thanks for considering a contribution. This is a community spec — improvements come from people actually using it.

## What to contribute

**Refinements to the convention itself.** Found a gap in the spec? Discovered a better folder structure for a use case? Open an issue or PR against the README.

**New agent integration recipes.** Got the substrate working with a tool that doesn't have a recipe yet (e.g., Cursor, Windsurf, Cline, Aider, ChatGPT, local LLMs)? Submit your recipe to `/recipes/`.

**Better bootstrap prompts.** Found a prompting pattern that produces better initial substrate content? Add it to `/bootstrap/`.

**Anonymized example substrates.** Sharing a (sanitized) example of your real substrate is one of the most useful things you can do — newcomers learn faster from concrete examples than from documentation.

**Tools and implementations.** Built a dashboard, CLI tool, MCP server, IDE plugin, or other utility that helps people use the convention? Open an issue with a link — we'll reference notable implementations in the docs.

## What's the scope of v0.1

We're trying to establish a stable enough foundation to be useful while leaving room to learn. v0.1 covers:

- Core folder structure (self/, team/, refinements/)
- File purposes for each substrate category
- Refinement format and workflow
- The COMPASS.md schema file
- Compatibility with CLAUDE.md/AGENTS.md

Things explicitly NOT in scope for v0.1:

- A required runtime or server
- A specific dashboard implementation (encourage forks instead)
- Specific LLM model requirements
- Authentication/authorization patterns (use whatever your storage provides)
- Multi-substrate sync or federation

We'll consider expanding scope based on what early adopters actually need.

## Process

For minor changes (typos, clarifications, new recipes): open a PR directly.

For convention changes (new folders, modified file formats, new conventions): open an issue first to discuss. Convention changes affect every adopter; they need consensus.

For new ideas: open an issue with the use case and proposed solution. Discussion welcome.

## Style for contributed docs

- Plain language, no jargon where avoidable
- Concrete examples over abstract descriptions
- Honest about limitations
- Short over long where the meaning is clear

## Code of conduct

Be helpful. Be specific. Disagree with ideas, not people. If you submit something and it gets rejected or modified, that's the process working — keep contributing.
