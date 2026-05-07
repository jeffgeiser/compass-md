# Design Rationale

Why compass-md is shaped the way it is. Useful for adopters wondering why certain choices were made, and for anyone considering a fork.

---

## Why markdown?

Markdown is the universal format for AI-readable human text. Every AI tool that handles files handles markdown. Every version control system versions it. Every programmer can open and edit it. Every storage system can hold it.

More structured formats (YAML, JSON, TOML) would be more parseable but less writable. A voice.md that reads like prose is easier for a human to write well than a voice.yaml with nested keys. The richness of voice patterns is hard to capture in structured data; prose lets you use examples, qualifications, and nuance.

More proprietary formats would create lock-in. The Compass should travel with the person, not with the tool.

Markdown is the lowest common denominator that still supports rich content. That's what we want.

---

## Why no required server?

Every required server is a point of failure, a cost, and a dependency. The convention should work for someone without technical infrastructure — a founder in Google Drive, a researcher in Dropbox, a developer in a local folder.

Any architecture requiring a server would exclude the majority of potential adopters and create maintenance burden for everyone. The convention defines the file structure and the interaction protocols. Infrastructure is implementation detail.

An MCP server, a dashboard, a CLI — these can all be built on top of the convention (and we hope people do). But they're not part of the convention.

---

## Why "agents propose, humans dispose"?

The core discipline of the convention.

Agents making direct edits to Compass files is a plausible design. It would be simpler — no pending folder, no review step. But it breaks trust quickly.

An agent that gets your voice wrong and then writes its mistake into voice.md has made your context worse. The next agent to read that file will produce worse outputs based on bad data. Errors compound.

The propose-and-review discipline means the Compass only gets updated when a human confirms an update. Refinements accumulate slowly, but they accumulate correctly. After six months, the Compass reliably reflects you — not you as mediated by a series of unreviewed agent inferences.

The review step is deliberately low-friction: a folder of files you drag to accepted/ or rejected/. It doesn't require a dashboard or a CLI. It can be as simple as opening the pending folder in Drive once a week.

---

## Why the specific folder structure?

The folder structure is a constraint, and constraints are useful. When the structure is agreed on, every agent knows where to look and every tool knows how to navigate. A personal Compass and a team Compass built by different people look the same from the outside.

The specific choices:

**`self/` and `team/` as top-level modules.** The two most common Compass use cases — personal context and shared team context — are different enough in purpose and audience to warrant separate modules. A personal voice.md and a team style.md serve different functions; keeping them in separate folders prevents confusion about which is which.

**`refinements/pending/`, `accepted/`, `rejected/`.** Three-state tracking for proposed changes mirrors code review: proposed, merged, closed. The rejected folder is as important as the accepted folder — it's the record of what the Compass explicitly doesn't want, which is valuable signal.

**`perspectives/` as a subfolder of `self/`.** Perspectives accumulate over time and vary enormously in topic. Keeping them in a subfolder keeps the root `self/` folder navigable. The file-per-topic pattern makes it easy for agents to read only the relevant perspective without loading everything.

**`COMPASS.md` at root.** The schema file that tells agents how to read the Compass must be the first thing they read. Putting it at root makes it the natural starting point.

---

## Why "Compass" as the name?

Several alternatives were considered:
- "Context" — too generic
- "Profile" — implies demographics, not principles
- "Wiki" — too close to Karpathy's LLM Wiki, which has a different purpose
- "Substrate" — accurate but technical

"Compass" works because:
- A compass tells you where you are and what direction to go — which is exactly what the convention does for AI tools
- "Reading your Compass" is a natural phrase; "reading your profile" is not
- The name implies orientation and navigation, not just storage
- It's memorable and pronounceable across languages

The metaphor isn't perfect — a compass doesn't know about your voice or your decisions about SaaS pricing. But it's close enough and evocative enough to be useful.

---

## Why Google Drive as the recommended starting point?

The convention is storage-agnostic. So why recommend Drive?

Because most people need a recommendation. "Storage-agnostic" as a primary message leads to decision paralysis and inconsistent setups. Drive is the right default because:

1. The AI tools with the best file integration today (Cowork, Claude.ai) have native Drive connectors
2. Drive works on every device without setup
3. Drive is familiar to non-technical users — important for teams where not everyone is a developer
4. Drive has built-in versioning via revision history
5. Drive sharing is fine-grained and well-understood

Local filesystem is a valid choice for technical users who want sovereignty. GitHub repos are valid for users who want diff/branch/PR affordances. But Drive is the recommendation because it's lowest-friction for the most people.

---

## Why a human review step for team Compasses?

Team Compasses have the same propose-and-review discipline as personal Compasses, but the stakes are higher. Changes to team criteria or guidelines affect every output the team produces. An agent that mistakenly updates proposal criteria based on one data point can degrade every proposal review until the error is caught.

The weekly review cadence (Agent 3 proposes, team lead reviews on Monday) is designed to buffer against this. Frequent enough to keep the Compass improving; slow enough that errors are caught before they propagate.

---

## Why no versioning of individual Compass files?

The convention doesn't require version tracking within Compass files (e.g., keeping old versions of voice.md). The reasoning:

- `log.md` captures when files were edited and why
- `refinements/accepted/` captures what proposals were applied
- The Compass is a living document; old versions of a file are less useful than a good current version

For users who want complete version history (every change, diffable), keeping the Compass in a git repo solves this without adding convention complexity. See `docs/github-storage.md`.

---

## Why allow empty modules?

A Compass with only `self/voice.md` and `COMPASS.md` is a valid Compass. A Compass with only `team/criteria/proposal-review.md` is also valid.

The convention is opt-in by file. Don't create files you don't need. An empty `preferences.md` is worse than no `preferences.md` — it takes up agent context window with placeholder text.

The `COMPASS.md` schema file declares which modules are active. Agents read that first and only look for files in active modules.
