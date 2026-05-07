# compass-md

**An open convention for personal and team context that AI agents can read, propose changes to, and learn from over time.**

A Compass is a folder of structured markdown files that captures the context an agent needs to act on someone's behalf — voice, perspectives, preferences, decisions, criteria, guidelines. The convention defines the folder structure, the file purposes, and how agents and humans should interact with the Compass.

Inspired by Andrej Karpathy's [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), focused specifically on personal and team context rather than topical knowledge bases.

The name comes from what the convention is for AI tools: a compass for who you are, what you value, and how you work. Tools that read your Compass can navigate by it.

---

## Just want to use it?

**[GETTING_STARTED.md](GETTING_STARTED.md)** — a practical walkthrough for someone who just set up their Compass and wants to know what to do next: day one bootstrap, the daily flow, the weekly review, monthly maintenance.

The rest of this document is the full convention spec. Read it if you want to understand how it works, contribute to it, or build tools on top of it.

---

## What this is

This is a **specification**, not a product. It defines:

- A folder structure that any AI agent can read
- Conventions for how agents propose changes to Compass files
- A human review pattern for accepting or rejecting agent-proposed changes
- A schema file (`COMPASS.md`) that tells agents how to follow the convention

What this is *not*:

- A SaaS product
- A required runtime
- A proprietary format
- A replacement for any existing tool

If you adopt the convention, you can use any agent (Claude Cowork, Claude.ai, Claude Code, Cursor, ChatGPT, local models) and any storage that holds files. The Compass is just markdown that follows agreed conventions.

---

## Why this exists

Every modern AI tool has the same gap: it doesn't know who you are. Each session starts from scratch. Even tools with memory features keep that memory locked in their own product. There's no shared Compass that travels with you across tools.

For teams, the same gap exists at the team level: institutional knowledge (style guides, decision frameworks, criteria) lives in wikis nobody updates, gets out of date, and provides no value to AI agents working on the team's behalf.

This convention proposes a simple, portable Compass that any agent can consult and contribute to:

- Your voice, perspectives, preferences, and stable facts (personal use)
- A team's guidelines, criteria, and accumulated wisdom (team use)
- A project's conventions, standards, and decisions (project use)

All as markdown files in a known structure. Agents read them before acting. Agents propose refinements as they observe your corrections and decisions. Humans review and accept or reject proposed changes. The Compass compounds over time without requiring active maintenance work.

---

## Core principles

**Markdown files in a folder.** No databases, no APIs, no proprietary formats. The Compass is human-readable, version-controllable, and portable across every storage and tool.

**Conventions, not infrastructure.** The Compass works with any AI tool that can read files. No required server, no required protocol, no required runtime.

**Agents propose, humans dispose.** Agents never modify Compass files directly. They write proposals to a known location. Humans review and accept or reject. This keeps quality high and keeps the Compass trustworthy.

**Storage-agnostic, Drive-friendly.** The convention works with any storage that holds files. Google Drive is the recommended starting point because it has the broadest AI tool integration and works well for both individual and team use (see Setup below).

**Composable with existing tools.** Works alongside CLAUDE.md, AGENTS.md, and any other meta-files. Doesn't conflict with existing AI tool conventions.

**Generalizable.** The same convention supports personal context (voice, preferences) and team context (guidelines, criteria). The folder structure adapts to use case; the conventions stay constant.

---

## Setup: Google Drive (recommended starting point)

For most people starting out, putting your Compass in Google Drive is the right default. Reasons:

- Cowork, Claude.ai, and most modern AI tools have Drive connectors and can read your Compass files automatically
- Accessible from any device — your Compass is available wherever you are
- Built-in versioning via Drive's revision history
- Familiar interface for non-technical users to browse, read, and edit Compass files
- Easy to share scoped slices with collaborators when needed

**Setup steps (about an hour, mostly drafting initial content):**

1. **Create the folder structure in Drive.** In your Google Drive, create a folder called `compass` at the top level (or wherever you prefer). Inside it, create the subfolders shown in the "Folder structure" section below.

2. **Copy the templates.** Clone this repo or download the `templates/` folder. Copy the templates into your Drive folder structure. Most users just need the `self/` templates plus `COMPASS.md`, `log.md`, and the `refinements/` folders.

3. **Edit `COMPASS.md`.** This is your schema file. Customize it for your situation — owner name, active modules, engagement notes. Spend 10 minutes here; this file shapes how every agent reads your Compass.

4. **Draft initial content.** Spend 30 minutes filling in rough drafts of `self/voice.md`, `self/preferences.md`, and `self/facts.md`. Don't aim for completeness — agents need *something* to read for the convention to be useful from session one.

   **Faster option:** If your Drive already contains a lot of your writing and documents, use `bootstrap/full-drive-scan.md` to have Cowork scan your Drive and produce drafts automatically. Takes about an hour total (setup + scan + review). Covers facts.md, voice.md, preferences.md, and decisions.md. For perspectives, use the interview bootstrap separately — perspectives inferred from Drive content tend to be wrong.

5. **Connect an AI tool.** See the recipes in `/recipes/` for how to point Cowork, Claude.ai, or other tools at your Compass. Cowork is the easiest starting point because it has native Drive integration and can both read and write to your Compass folder.

6. **Use it for two weeks.** Don't optimize prematurely. Use the Compass with your AI tool of choice. When refinements get proposed (in `refinements/pending/`), review and accept the good ones. The Compass gets richer through use.

After setup, see **[GETTING_STARTED.md](GETTING_STARTED.md)** for the daily/weekly/monthly rhythm that keeps the Compass compounding in value.

**Other storage options:**

- **Local filesystem:** for users who want sovereignty (nothing in the cloud) and use local-first tools. See `recipes/claude-code.md`.
- **GitHub repo:** for users who want diff/branch/PR workflows and code-review affordances for their Compass. See `docs/github-storage.md`.
- **Dropbox, OneDrive, etc.:** the convention works with any storage that holds files. Adapt the Drive setup to your tool.

---

## Folder structure

A Compass is a folder named `compass` (or any name you choose) containing:

```
compass/
├── COMPASS.md                      ← schema file: tells agents how to follow the convention
├── README.md                       ← human-readable description of this Compass
├── self/                           ← personal context (for individual use)
│   ├── voice.md
│   ├── perspectives/
│   │   └── (one file per topic, accumulates over time)
│   ├── preferences.md
│   ├── facts.md
│   └── decisions.md
├── team/                           ← team context (for shared use)
│   ├── guidelines.md
│   ├── criteria/
│   │   └── (one file per criteria type)
│   ├── style.md
│   └── feedback_log.md
├── refinements/
│   ├── pending/                    ← agent-proposed changes awaiting human review
│   ├── accepted/                   ← review history of approved changes
│   └── rejected/                   ← review history of rejected changes (with reasons)
├── log.md                          ← chronological event log
└── INDEX.md                        ← optional: catalog of Compass files for fast lookup
```

Not every Compass needs every folder. A pure personal Compass might use only `self/`. A pure team Compass might use only `team/`. A Compass supporting both individual and team work uses both. The schema file declares which folders are active.

---

## File purposes

### Personal context (`self/`)

**`voice.md`** — How the person writes and speaks. Tone, register, vocabulary preferences, sentence structure tendencies, things they say, things they avoid. Used by agents drafting content on the person's behalf.

**`perspectives/*.md`** — One file per topic the person has stated views on. Examples: `perspectives/competitive-strategy.md`, `perspectives/ai-safety.md`, `perspectives/management.md`. Each file captures the person's actual position on the topic with supporting reasoning, ideally with citations to where they expressed it. Used by agents reasoning about decisions or producing content where the person's perspective should be reflected.

**`preferences.md`** — Stable preferences. Communication frequency, decision-making style, things the person always wants, things they never want. Sectioned by category. Used by agents to align defaults with the person's preferences.

**`facts.md`** — Stable facts about the person. Role, location, relationships, current context. Things that change rarely. Used by agents to ground their understanding of who they're working with.

**`decisions.md`** — Significant decisions the person has made and the reasoning behind them. Append-only log. Used by agents to understand precedent and avoid contradicting prior choices.

### Team context (`team/`)

**`guidelines.md`** — The team's working agreements, standards, and best practices. The constitution that drives agent behavior on team work.

**`criteria/*.md`** — Specific evaluation criteria for recurring tasks. Examples: `criteria/proposal-review.md`, `criteria/contract-review.md`, `criteria/hiring-screening.md`. Used by agents performing those evaluations.

**`style.md`** — Team writing/communication style. Different from personal voice — this is the team's collective voice for external communications.

**`feedback_log.md`** — Structured log of feedback observations that should eventually inform updates to guidelines or criteria.

### Refinements

**`refinements/pending/`** — A directory where agents place proposed changes to Compass files. Each pending refinement is a single markdown file containing the proposed change (see refinement format below). Humans review files in this directory and either move them to `accepted/` (after applying the change) or to `rejected/` (with a reason).

**`refinements/accepted/`** — Historical record of accepted refinements. Useful audit trail.

**`refinements/rejected/`** — Historical record of rejected refinements with reasons. Helps agents learn what kinds of refinements get rejected and avoid proposing similar ones.

### Navigation

**`log.md`** — Append-only chronological log of Compass events. Each entry has a consistent prefix (`## [YYYY-MM-DD HH:MM] {event-type} | {description}`) so it's parseable with simple tools. Event types include: `ingest`, `refinement-proposed`, `refinement-accepted`, `refinement-rejected`, `lint`, `manual-edit`.

**`INDEX.md`** — Optional. Catalog of Compass files with one-line summaries. Useful when the Compass grows large enough that an agent benefits from reading an index before drilling into specific files.

### Schema

**`COMPASS.md`** — The schema file. Tells agents reading this Compass how to follow the convention. Includes which folders are active, which categories are populated, what conventions to follow, and any custom extensions to the spec. See `templates/COMPASS.md` for the full template — copy it to your Compass folder and customize it for your situation.

The schema file is the most important artifact in the Compass. Spend time on it. Iterate on it as you learn what works.

---

## How agents interact with a Compass

There are three operations agents perform on a Compass.

### 1. Read

Before acting on the Compass owner's behalf, an agent reads relevant Compass files to ground its understanding. Typical pattern:

1. Agent reads `COMPASS.md` to understand the convention being followed
2. Agent identifies which Compass files are relevant to the current task
3. Agent reads those specific files (and `INDEX.md` if present)
4. Agent acts with that context informing its output

For personal use cases: drafting an email reads `self/voice.md` and possibly `self/preferences.md`. Evaluating an opportunity reads relevant `self/perspectives/*.md`. Recommending a decision reads `self/decisions.md` for precedent.

For team use cases: reviewing a proposal reads `team/criteria/proposal-review.md` and `team/guidelines.md`. Drafting external communication reads `team/style.md`.

### 2. Propose refinements

When an agent observes information that should refine the Compass (a corrected output, a stated preference, a new perspective expressed, an inconsistency with existing files), it writes a refinement file to `refinements/pending/`.

A refinement file follows this format:

```markdown
---
proposed_at: 2026-04-23T14:32:07Z
proposed_by: cowork
target_file: self/voice.md
target_section: "Email tone"
change_type: addition | modification | removal
confidence: low | medium | high
---

## Observation

[What the agent observed that motivated this proposed change. Include specific quotes or examples.]

## Proposed change

[The exact change being proposed. For additions, the new content. For modifications, the before/after. For removals, what's being removed.]

## Reasoning

[Why the agent believes this change is warranted. Confidence and uncertainty.]

## Evidence

[Specific examples or interactions that support the proposed change.]
```

The file should be named with timestamp and brief description: `2026-04-23-143207_voice-tone-update.md`.

Agents never modify Compass files directly. All proposed changes go through `refinements/pending/`. This keeps quality high and gives humans control over Compass evolution.

### 3. Append to logs

Agents may append entries to `log.md` to record significant events:

```
## [2026-04-23 14:32] refinement-proposed | Voice update from Cowork email-drafting session
## [2026-04-23 09:15] read | Cowork read self/voice.md and self/perspectives/strategy.md
```

Append-only. Never modify or remove past entries.

---

## How humans interact with a Compass

Humans have three primary interactions with the Compass:

### Direct editing

Humans can edit any Compass file directly at any time. The Compass belongs to the human; agents are visitors. Direct edits should be noted in `log.md` with `manual-edit` event type. In Google Drive, this is just opening the markdown file in any Drive-aware editor.

### Reviewing pending refinements

Periodically (daily, weekly, on notification), humans review files in `refinements/pending/`. For each one:

- **Accept**: apply the proposed change to the target file, move the refinement file to `refinements/accepted/`
- **Reject**: move the refinement file to `refinements/rejected/` with a `## Rejection reason` section appended
- **Edit and accept**: modify the proposed change as needed, then accept

For Drive-based Compasses, this can be as simple as: open the `refinements/pending/` folder in Drive, read each refinement file, drag it to `accepted/` or `rejected/`. Tools, dashboards, or workflows can be built around this pattern. The convention defines the *location* of pending refinements; the *interface* for review is implementation-specific.

### Lint operations

Humans (or scheduled agents) can request a Compass health check. This produces a report in `lint/{date}.md` covering:

- Contradictions between Compass files
- Stale claims that newer evidence supersedes
- Categories that are sparsely populated
- Categories that are dense and might benefit from further organization
- Missing cross-references
- Refinements that have been pending for unusually long

The lint report is a markdown file the human reviews to maintain Compass health.

---

## Use case: personal context

A person sets up a Compass to capture their voice, perspectives, and preferences for use across AI tools.

**Setup:**
1. Create a `compass` folder in Google Drive
2. Copy templates from this repo
3. Fill in initial drafts of `self/voice.md`, `self/preferences.md`, `self/facts.md`
4. Create initial perspective files in `self/perspectives/` for topics with strong views
5. Customize `COMPASS.md` for personal use
6. Connect Cowork or Claude.ai (with Drive connector) using the provided recipe

**Daily use:**
1. Use AI tools configured to read the Compass
2. Tools draft, evaluate, recommend with Compass as context
3. When tools propose refinements, they land in `refinements/pending/`
4. Review refinements weekly or on notification
5. Compass gets richer over time

**Outcome:**
The Compass becomes a portable, AI-readable representation of the person that compounds in value as AI tools observe and contribute to it. Switching tools is friction-free — any tool that can read files can use the Compass.

---

## Use case: team workflow (proposal review example)

A sales team uses the Compass to maintain proposal review guidelines that agents can apply automatically and that improve over time based on leader feedback.

**Setup:**
1. Create `compass` folder in team-shared Drive (or shared GitHub repo for diff visibility)
2. Populate `team/guidelines.md` with the team's proposal best practices
3. Populate `team/criteria/proposal-review.md` with specific evaluation criteria
4. Configure agents:
   - Agent 1 reviews proposals using `team/criteria/proposal-review.md`
   - Agent 2 extracts feedback into `team/feedback_log.md`
   - Agent 3 weekly proposes refinements to `team/criteria/proposal-review.md` based on feedback patterns

**Operation:**
- Salespeople upload proposals via Cowork
- Agent 1 reviews and produces marked-up file
- Leader reviews and adds comments
- Agent 2 logs feedback in structured form
- Agent 3 weekly proposes guideline updates as refinements
- Leader reviews refinements via the team's chosen review interface
- Approved refinements update guidelines for next cycle

**Outcome:**
The team's review criteria evolve based on actual feedback patterns rather than ad-hoc updates. Audit trail is complete: every change to guidelines is documented, every agent action is logged, every leader decision is captured.

---

## Compatibility with existing conventions

### CLAUDE.md / AGENTS.md

`COMPASS.md` does not replace `CLAUDE.md` or `AGENTS.md`. They serve different purposes:

- `CLAUDE.md`/`AGENTS.md`: instructions to the AI agent about how to operate in this project/repo
- `COMPASS.md`: instructions to the AI agent about how to read and contribute to the Compass

A repo can have both. A typical setup: `CLAUDE.md` instructs Claude Code on the codebase conventions, `COMPASS.md` instructs any agent on the personal/team context Compass.

### Karpathy's LLM Wiki

The compass-md convention is inspired by Karpathy's pattern but focused differently:

- LLM Wiki: build a topical knowledge base around subjects of interest
- compass-md: build a personal/team context Compass around the person/team itself

Both are valid uses of the schema-driven LLM-maintained markdown approach. They can coexist (a person could have both a knowledge wiki and a personal Compass). The compass-md convention focuses on the contextual rather than the topical.

### Notion / Obsidian / Roam

The Compass is just markdown files. It works alongside any tool that reads markdown. Obsidian users can browse their Compass in Obsidian. Notion users can sync the folder to Notion. The convention is independent of any specific tool.

---

## Reference implementations

This repo includes:

**Templates** (`/templates/`): Empty markdown files for each Compass category, ready to copy into a new Compass.

**Agent integration recipes** (`/recipes/`): System prompt snippets and instructions for connecting various AI tools to a Compass. Includes:
- `cowork.md` — instructions for Claude Cowork (Drive-native, recommended starting point)
- `claude-ai.md` — instructions for Claude.ai Projects (Drive-connected)
- `claude-code.md` — instructions for Claude Code (local filesystem)
- `cursor.md` — instructions for Cursor (local filesystem)
- `chatgpt.md` — instructions for ChatGPT custom instructions
- `local-ollama.md` — instructions for fully-local setups

**Bootstrap prompts** (`/bootstrap/`): Prompts for initializing a Compass from existing material:
- `full-drive-scan.md` — scan your Google Drive to produce initial substrate drafts (recommended starting point)
- `voice-from-writing-samples.md` — focused voice extraction from writing samples
- `interview-perspectives.md` — conversational interview to populate perspective files (required for perspectives)
- `team-guidelines-from-history.md` — extract team guidelines from past decisions
- `facts-from-resume.md` — quick bootstrap of facts.md from a resume

**Helper scripts** (`/scripts/`): Optional utilities:
- `validate-compass.py` — checks a folder against the convention, reports violations
- `pending-refinements.py` — lists pending refinements with summaries
- `lint-compass.py` — produces a Compass health report (calls an LLM)

**Examples** (`/examples/`): Anonymized real Compasses contributed by adopters:
- Personal Compass example
- Sales team proposal review Compass
- Research project Compass

---

## Versioning

The convention itself is versioned. Current version: **v0.1**.

A Compass's `COMPASS.md` declares which version of the convention it follows. Agents reading the Compass should respect that version's conventions.

Breaking changes get a major version bump (v1 → v2). Additions and clarifications get minor bumps (v0.1 → v0.2). The repo maintains compatibility documentation.

---

## Frequently asked questions

**Why "Compass"?**

Because that's what the convention is for AI tools: a compass for who you are, what you value, and how you work. Tools that read your Compass can navigate by it instead of guessing.

**Why not use a database or structured format?**

Markdown files are universally readable, human-editable, version-controllable, portable across storage, and consumable by every AI tool. Any structured format would introduce dependencies and friction. Markdown is the lowest common denominator that still supports rich content.

**Why not use MCP?**

MCP solves the problem of agents discovering and calling tools at runtime. The Compass doesn't need that — every modern agent already knows how to read and write files. The convention is the API. Adding MCP would be infrastructure overhead without proportional benefit.

That said, an MCP server that exposes Compass operations is a valid implementation choice for tools that benefit from it. The convention doesn't prevent it; it just doesn't require it.

**Why Google Drive as the recommended starting point?**

Drive has the broadest AI tool integration today (Cowork, Claude.ai, ChatGPT all have connectors), works on every device, has built-in versioning, and is familiar to non-technical users. The convention works in any storage; Drive is just the lowest-friction starting point for most people.

**How does this differ from "Notion AI" or "ChatGPT custom instructions"?**

Both are tool-specific. Your context lives in their product. You can't take it with you. Switching tools means rebuilding context.

The Compass is portable and tool-agnostic. The same files work with Cowork, Claude.ai, Cursor, ChatGPT, Claude Code, and any future tool that can read markdown. You own your Compass; tools are visitors.

**What about privacy?**

The Compass lives in your storage of choice. You control who has access. Agents reading the Compass operate under whatever permissions you give them in their respective products (your Cowork session, your Claude.ai account, etc.). Nothing in the convention requires you to share Compass with anyone.

For team Compasses, treat the Compass folder like any other team document — apply appropriate access controls in your storage system.

**How do I bootstrap a Compass when starting from nothing?**

See `/bootstrap/` for prompts that help. The general approach: spend 30 minutes manually drafting initial files, then use bootstrap prompts to enrich them from existing material (your writing samples, team docs, past decisions). The Compass gets richer through use; perfect bootstrapping isn't necessary.

**What if I disagree with the folder structure?**

The structure is a convention, not a requirement of the universe. Fork the repo, propose changes, or just adapt the structure for your needs and document the adaptation in your `COMPASS.md`. Other adopters will know what you've done because they can read your schema.

The hope is that the standard structure works for most use cases and adaptations are rare. Feedback welcome.

---

## Contributing

This is a community spec. Contributions welcome:

- Refinements to the convention itself (PRs to this repo)
- New agent integration recipes (`/recipes/`)
- Better bootstrap prompts (`/bootstrap/`)
- Anonymized example Compasses (`/examples/`)
- Implementations: dashboards, CLI tools, MCP servers, IDE plugins — whatever helps adopters

See `CONTRIBUTING.md` for details.

---

## Status

**Current version:** v0.1 (initial draft)
**Stability:** Pre-stable. Expect refinements based on early adopter feedback.
**Published by:** [Hiipo](https://hiipo.io). Hiipo also ships a sovereign AI governance proxy — a related but distinct product.

---

## Acknowledgments

This convention is inspired by:

- [Andrej Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the schema-driven LLM-maintained wiki pattern
- [Vannevar Bush's Memex (1945)](https://en.wikipedia.org/wiki/Memex) — the original vision of personal, curated context with associative trails
- The CLAUDE.md and AGENTS.md conventions — the pattern of meta-files that instruct agents how to operate

The personal-context-Compass framing and the team-context extension are this convention's specific contributions on top of those foundations.
