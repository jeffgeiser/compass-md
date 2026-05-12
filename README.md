# compass-md

**An open convention for the human-curated identity layer that AI tools share.**

Every AI session starts from scratch. Your voice, your preferences, your reasoning — rebuilt from context every time, lost when the session ends. Compass-md solves that.

A Compass is a folder of structured markdown files capturing the context an AI agent needs to act in alignment with someone — their voice, perspectives, preferences, decisions, values, criteria. The convention defines the folder structure, the file purposes, and how agents and humans should interact with the Compass.

The name comes from what the convention is for AI tools: a compass for who you are, what you value, and how you work. Tools that read your Compass can navigate by it.

Unlike topical knowledge bases (Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) approach), compass-md captures *who you are*, not *what you know*. The difference matters: agents acting on your behalf need your judgment, voice, and preferences — not a Wikipedia.

---

## Just want to use it?

If you're ready to set up your Compass and start using it, follow this path:

1. Go to the **Setup** section below — pick the storage that fits your situation (Drive, local folder, or Git), then follow that path
2. Then read **[GETTING_STARTED.md](./GETTING_STARTED.md)** for a practical walkthrough of daily use, the weekly review, and the monthly maintenance routine

The rest of this README is the formal spec — useful as reference, but you don't need to read all of it to get started.

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

## Where compass fits

Personal AI is a stack with several layers. Different products and conventions address different layers. Understanding where compass sits clarifies what it does and what it deliberately does not do.

A rough map of the landscape:

1. **Per-tool memory features** — ChatGPT memory, Claude.ai memory, per-product personalization. Siloed, tool-specific, not portable.

2. **Cross-tool identity conventions (compass-md lives here).** A shared, human-curated representation of the user that any tool can read. Simple, portable, deliberately small.

3. **Memory architectures and retrieval systems** — vector stores, knowledge graphs, RAG pipelines, hierarchical memory like MemGPT, self-editing systems like Letta. The infrastructure that tools build internally to handle context at scale. (Mert Cobanov's [essay on agent memory](https://memory.cobanov.dev/) is a good guide to this layer.)

4. **Personal AI applications** — full products that ingest your calendar, finances, health data, and communications; run continuous analysis; surface predictions and decision support. Examples include various "personal life OS" products in development.

5. **Long-term agent partner visions** — speculative, multi-year products that aim to be a continuous AI presence in the user's life.

Compass-md occupies layer 2 specifically because that's where a *convention* makes the most sense. Below it (layer 1), conventions don't help — each tool just has its own memory feature. Above it (layers 3-5), conventions are too constraining — real applications need flexibility in how they architect memory, ingest data, and surface insights. The middle layer — "what should be in the human-curated identity layer that any tool can read?" — is the right place for an open standard.

The relationship to the layers above is complementary. A memory architecture (layer 3) can use compass as a content schema for the human-curated portion of its store. A personal AI application (layer 4) can use compass as the value-alignment layer that ensures its recommendations match what the user has stated they want. Tools at every layer benefit from a shared substrate they don't have to invent.

---

## What compass is not

Being explicit about scope helps users self-select correctly. Compass is *not*:

- **A continuous-ingestion system.** Compass doesn't watch your calendar, monitor your inbox, or track your health data. Updates happen via human curation or AI proposals during sessions.

- **A real-time monitoring system.** No background processes, no scheduled analysis, no anomaly detection.

- **A predictive analytics platform.** Compass stores stated values and observed patterns; it doesn't analyze them to predict your future state.

- **A privacy-first encrypted architecture.** Compass is just files. Privacy is whatever your storage layer (Google Drive, local filesystem, GitHub) provides. For sensitive content, choose your storage accordingly.

- **A decision support tool on its own.** AI tools that read your compass provide decision support; compass just provides the substrate they consult. The intelligence lives in the tools, not in the convention.

- **A memory architecture.** Compass doesn't define how memory is stored, retrieved, or compressed. Tools implementing compass make their own architectural choices.

- **A complete personal AI solution.** If you want a full personal AI product that ingests data and surfaces insights, that's an application, not a convention. Compass might be one component of such an application's stack.

Users who want any of the above should look at products in layers 3-5. Users who want a portable, simple, AI-readable layer for their stated identity, voice, and preferences should look at compass.

---

## Core principles

**Markdown files in a folder.** No databases, no APIs, no proprietary formats. The Compass is human-readable, version-controllable, and portable across every storage and tool.

**Conventions, not infrastructure.** The Compass works with any AI tool that can read files. No required server, no required protocol, no required runtime.

**Agents propose, humans dispose.** Agents never modify Compass files directly. They write proposals to a known location. Humans review and accept or reject. This keeps quality high and keeps the Compass trustworthy.

**Storage-agnostic.** The convention works with any storage that holds files: Google Drive, local filesystem, git repository, Dropbox, S3, or anything else. No storage is required; all are valid. See Setup below for guidance on which fits your situation.

**Composable with existing tools.** Works alongside CLAUDE.md, AGENTS.md, and any other meta-files. Doesn't conflict with existing AI tool conventions.

**Generalizable.** The same convention supports personal context (voice, preferences) and team context (guidelines, criteria). The folder structure adapts to use case; the conventions stay constant.

**Value alignment over context dumping.** Compass is designed to capture stated values, perspectives, and preferences that AI tools should align with — not to be a complete record of everything about you. The user explicitly states what matters; AI tools validate their recommendations against those statements. This is more useful than passive context accumulation because it makes the user's intent explicit and reviewable.

---

## Setup: Pick your storage

The Compass is just files. Where those files live determines which AI tools can access them and how you manage them day to day. Choose before setting up — migrating later is easy but requires updating your tool connections.

### Which storage fits you?

| | Google Drive | Local folder | Git repository |
|---|---|---|---|
| **Good for** | Multi-device access; Drive-native tools | Privacy; local-first tools; simplest setup | Audit trail; teams; diff/PR workflows; multi-device sync |
| **Works with** | Cowork, Claude.ai | Claude Code, Cursor, Ollama | Claude Code, Cursor |
| **Device access** | Any device | This machine (or synced) | Any device; auto-synced via included launchd agents |
| **Requires** | Google account | Nothing | Git familiarity |
| **Privacy** | Google's terms apply | Fully local | Depends on repo visibility |

**Google Drive** is a popular choice for people who want their Compass accessible across devices and plan to use Drive-connected AI tools (Cowork, Claude.ai). Requires a Google account; no command line.

**Local folder** keeps everything on your machine — nothing in the cloud, no dependencies beyond a text editor and an AI tool. The natural fit for Claude Code, Cursor, and local model users. One terminal command sets it up.

**Git repository** is for developers who want diff, branch, and PR workflows for their Compass changes, or teams who want code-review-style refinement approval. Requires Git familiarity.

Once you've chosen, follow the matching path below.

---

### Setup: Google Drive (~1 hour)

1. **Create the folder structure in Drive.** In Google Drive, create a folder called `compass`. Inside it, create the subfolders shown in the "Folder structure" section below.

2. **Copy the templates.** Clone this repo or download the `templates/` folder. Copy the templates into your Drive structure. Most users need the `self/` templates, `COMPASS.md`, `log.md`, and the `refinements/` folders.

3. **Edit `COMPASS.md`.** Customize it — owner name, active modules, engagement notes. Spend 10 minutes here; this file shapes how every agent reads your Compass.

4. **Draft initial content.** Fill in rough drafts of `self/voice.md`, `self/preferences.md`, and `self/facts.md`. Don't aim for completeness — agents need *something* to read for the convention to work from session one.

   **Faster option:** If your Drive already contains a lot of your writing and documents, use `bootstrap/full-drive-scan.md` to have Cowork scan your Drive and produce drafts automatically (~1 hour total). For perspectives, use `bootstrap/interview-perspectives.md` separately — perspectives inferred from Drive content tend to be wrong.

5. **Connect an AI tool.** See `recipes/cowork.md` (recommended for Drive) or `recipes/claude-ai.md`. Cowork is the easiest starting point because it has native Drive integration and can both read and write to your Compass folder.

6. **Use it for two weeks before optimizing.**

After setup, see **[GETTING_STARTED.md](./GETTING_STARTED.md)** for the daily/weekly/monthly rhythm.

---

### Setup: Local folder (~30 minutes)

Everything stays on your machine. No account required, no cloud sync, no dependencies beyond a text editor and an AI tool that can read files.

**Step 1: Create the folder structure.** One command sets up everything:

```bash
mkdir -p ~/compass/{self/perspectives,team/criteria,refinements/{pending,accepted,rejected}}
```

This creates your Compass at `~/compass/` with all required subfolders. Use a different path if you prefer — just substitute it throughout.

**Step 2: Copy the templates.** Clone this repo and copy the starter files:

```bash
git clone https://github.com/jeffgeiser/compass-md /tmp/compass-md
cp -r /tmp/compass-md/templates/self ~/compass/
cp /tmp/compass-md/templates/COMPASS.md ~/compass/
cp /tmp/compass-md/templates/log.md ~/compass/
cp /tmp/compass-md/templates/CLAUDE.md ~/compass/
```

`CLAUDE.md` is what makes Claude Code and Cursor automatically Compass-aware. Without it, those tools won't know your Compass exists.

**Step 3: Edit `COMPASS.md`.** Open `~/compass/COMPASS.md` in any text editor. Set your name as owner, mark `self/` as active, and add any engagement notes. Spend 10 minutes here — this file shapes how every agent reads your Compass.

**Step 4: Draft initial content.** Open the three core files and fill in rough drafts:
- `self/voice.md` — how you write: tone, vocabulary, structure
- `self/preferences.md` — what you always want and never want from AI tools
- `self/facts.md` — your role, location, current focus

Don't aim for completeness. Agents need *something* to work with from session one; the Compass gets richer through use.

**Faster option:** Use `bootstrap/local-folder-scan.md` to have Claude Code scan your local Documents folder and produce draft files automatically (~1 hour total). For perspectives, use `bootstrap/interview-perspectives.md` separately — perspectives inferred from documents tend to be wrong.

**Step 5: Connect Claude Code.** Create a `CLAUDE.md` in your Compass folder so Claude Code knows how to use it:

```bash
cat > ~/compass/CLAUDE.md << 'EOF'
# Claude Code Instructions

This directory is my compass-md following the v0.1 convention.

Before acting on my behalf, read COMPASS.md, then read the Compass files
relevant to the task:
- Drafting content → self/voice.md + relevant self/perspectives/
- Recommendations → self/preferences.md + relevant self/perspectives/
- Context about me → self/facts.md
- Prior decisions → self/decisions.md

Cite which files you read. When you observe something worth capturing,
write a refinement file to refinements/pending/ following the format in
templates/refinements/EXAMPLE-refinement.md. Max 3 per session. Never
modify Compass files directly.
EOF
```

Then reference your Compass from any code project by adding to that project's `CLAUDE.md`:

```
## Personal Compass

My compass-md is at ~/compass/. When generating commit messages, PR
descriptions, docs, or other written output, read the relevant files
there first. Propose refinements to ~/compass/refinements/pending/ when
you observe patterns worth capturing.
```

**Step 6: Test it.** Open Claude Code in your Compass folder:

```bash
cd ~/compass && claude
```

Ask something that should trigger a Compass read:

> "Draft a quick email to a client telling them a project is delayed by a week. Match my voice."

The response should cite which Compass files it read (e.g., "Drawing on self/voice.md..."). If it doesn't, check that `CLAUDE.md` is in `~/compass/` and that you opened Claude Code from that directory.

**Use it for two weeks before optimizing.** When refinements appear in `~/compass/refinements/pending/`, review and accept the good ones.

After setup, see **[GETTING_STARTED.md](./GETTING_STARTED.md)** for the daily/weekly/monthly rhythm.

---

### Setup: Git repository (~1 hour)

1. **Create a private repository** called `compass` on GitHub (or GitLab, or wherever you host). Clone it locally.

2. **Copy the templates.**

   ```bash
   cd ~/compass  # wherever you cloned
   cp -r /path/to/compass-md/templates/self .
   cp /path/to/compass-md/templates/COMPASS.md .
   cp /path/to/compass-md/templates/log.md .
   cp /path/to/compass-md/templates/CLAUDE.md .
   mkdir -p team/criteria refinements/{pending,accepted,rejected}
   touch refinements/{pending,accepted,rejected}/.gitkeep
   ```

3. **Edit `COMPASS.md`.** Customize it — same as above.

4. **Draft initial content.** Fill in rough drafts of `self/voice.md`, `self/preferences.md`, and `self/facts.md`.

5. **Connect an AI tool.** Claude Code works natively with a local clone. See `recipes/claude-code.md`. Add a reference to your Compass path in each code project's CLAUDE.md per the recipe.

   For team Compasses: multiple contributors clone the same repository. Use branches for proposed refinements, PRs for the review step. See `docs/github-storage.md` for the full Git-native workflow.

6. **Commit your initial Compass.** A clean commit history of Compass evolution is one of the main reasons to use Git.

7. **Set up auto-sync across devices (recommended).** The Compass repo includes launchd agents that automatically push file changes to GitHub and pull updates every 5 minutes — so edits on one machine appear on all others within minutes, with no manual `git push` required.

   Install on each machine:

   ```bash
   bash ~/compass/.scripts/install-sync.sh
   ```

   This installs two background agents:
   - **push agent** — watches `~/compass` for file changes and commits + pushes to GitHub automatically (with a 3-second debounce to let writes settle)
   - **pull agent** — pulls from GitHub every 5 minutes so changes from other machines arrive automatically

   The scripts live inside your compass repo (`.scripts/`), so they're already present after `git pull`. Run the install once per machine; it's idempotent. Logs go to `/tmp/compass-pull.log` and `/tmp/compass-push.log`.

   **If your tracking branch isn't set up**, run this before the install:
   ```bash
   git -C ~/compass branch --set-upstream-to=origin/main main && git -C ~/compass pull
   ```

After setup, see **[GETTING_STARTED.md](./GETTING_STARTED.md)**.

---

## Folder structure

A Compass is a folder named `compass` (or any name you choose) containing:

```
compass/
├── COMPASS.md                      ← schema file: tells agents how to follow the convention
├── CLAUDE.md                       ← tells Claude Code how to use this Compass automatically
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
├── .scripts/                       ← optional: git sync agents (Git storage only)
│   ├── compass-push.sh             ← auto-push on file change
│   ├── compass-pull.sh             ← auto-pull on schedule
│   └── install-sync.sh             ← installs launchd agents on macOS
├── log.md                          ← chronological event log
└── INDEX.md                        ← optional: catalog of Compass files for fast lookup
```

Not every Compass needs every folder. A pure personal Compass might use only `self/`. A pure team Compass might use only `team/`. A Compass supporting both individual and team work uses both. The schema file declares which folders are active.

---

## File purposes

### Personal context (`self/`)

**`voice.md`** — How the person writes and speaks. Tone, register, vocabulary preferences, sentence structure tendencies, things they say, things they avoid. Used by agents drafting content on the person's behalf.

```markdown
# Voice

## Tone and register
Direct and concise. Internal notes are casual; external communication is
professional but not stiff. No hedging when I have a view.

## Vocabulary
**I use:** short sentences, active verbs, specific numbers over vague quantifiers
**I avoid:** "it's worth noting", "perhaps", "synergy", "circle back", "reach out"

## Structure
Lead with the conclusion, then the reasoning.
Short paragraphs. One idea per paragraph.
Use dashes for asides — not parentheses.
```

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

Humans can edit any Compass file directly at any time. The Compass belongs to the human; agents are visitors. Direct edits should be noted in `log.md` with `manual-edit` event type. In Google Drive, this is just opening the markdown file in any Drive-aware editor. In a local or Git setup, this is any text editor.

### Reviewing pending refinements

Periodically (daily, weekly, on notification), humans review files in `refinements/pending/`. For each one:

- **Accept**: apply the proposed change to the target file, move the refinement file to `refinements/accepted/`
- **Reject**: move the refinement file to `refinements/rejected/` with a `## Rejection reason` section appended
- **Edit and accept**: modify the proposed change as needed, then accept

The mechanics depend on your storage: in Drive, this can be as simple as dragging files between folders. In a local or Git setup, it's moving files on the filesystem (and committing if using Git). Tools and dashboards can be built around this pattern. The convention defines the *location* of pending refinements; the *interface* for review is implementation-specific.

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
1. Create a `compass` folder (Drive, local, or Git — see Setup above)
2. Copy templates from this repo
3. Fill in initial drafts of `self/voice.md`, `self/preferences.md`, `self/facts.md`
4. Create initial perspective files in `self/perspectives/` for topics with strong views
5. Customize `COMPASS.md` for personal use
6. Connect an AI tool using the appropriate recipe

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

Different tools, different purposes:

- **CLAUDE.md / AGENTS.md** — project-specific instructions for a codebase. Travels with the repo. Describes the project.
- **Compass-md** — person-specific context. Travels with you. Describes the person.

They're complementary. A developer using both gets project context (CLAUDE.md) and personal context (compass-md) in every session. `COMPASS.md` (the schema file inside your Compass folder) is not a replacement for `CLAUDE.md` — it's the per-Compass instructions that tell agents how to read and contribute to the Compass itself.

### Karpathy's LLM Wiki

The compass-md convention is inspired by Karpathy's pattern but focused differently:

- LLM Wiki: build a topical knowledge base around subjects of interest
- compass-md: build a personal/team context Compass around the person/team itself

Both are valid uses of the schema-driven LLM-maintained markdown approach. They can coexist (a person could have both a knowledge wiki and a personal Compass). The compass-md convention focuses on the contextual rather than the topical.

### Notion / Obsidian / Roam

The Compass is just markdown files. It works alongside any tool that reads markdown. Obsidian users can browse their Compass in Obsidian. Notion users can sync the folder to Notion. The convention is independent of any specific tool.

---

## Connecting AI tools: what's actually required

Different tools work differently. The table below answers the key question for each one: what do you actually need to set up, and is pasting a prompt enough?

| Tool | What makes it persistent | Is a prompt alone enough? | Where to set it up |
|---|---|---|---|
| **Claude Code** | `CLAUDE.md` file in the compass folder *and* in each code project | No — prompt works for one session only, forgotten next time | Create `~/compass/CLAUDE.md`; add a compass reference block to each project's `CLAUDE.md` |
| **Cursor** | `.cursorrules` file in the compass folder *and* in each code project | No — prompt works for one session only | Create `~/compass/.cursorrules`; add a compass reference block to each project's `.cursorrules` |
| **Claude Cowork** | Project custom instructions (paste the prompt there once) | Yes, but only for that one conversation | Cowork → your project → Edit custom instructions |
| **Claude.ai Projects** | Project custom instructions + compass folder added to project files | Prompt alone = one conversation, no file access | Claude.ai → project → Custom instructions + Files → Add from Drive |
| **ChatGPT** | Custom GPT with files uploaded + system prompt | Prompt alone = one conversation, no file access | ChatGPT → Explore GPTs → Create a GPT → Knowledge + Instructions |

**The core distinction:**

- **File-reading tools (Claude Code, Cursor)** — these tools read a configuration file (CLAUDE.md or .cursorrules) at the start of every session. Without that file, they have no idea your Compass exists. Pasting a prompt works once but disappears when the session ends. The file is what makes it automatic.

- **Chat tools (Cowork, Claude.ai, ChatGPT)** — these tools use custom instructions or project system prompts that persist across conversations. Setting up the instructions *is* the setup. No separate file is required (except for file access — Claude.ai and Cowork need the Compass folder connected to read the actual files).

**What "connecting" actually means in practice:**

For Claude Code:
```
Session without CLAUDE.md:  You open a project → Claude Code knows nothing about your Compass
Session with CLAUDE.md:     You open a project → Claude Code automatically reads CLAUDE.md → knows your Compass exists and how to use it
```

For Cowork / Claude.ai:
```
Session without custom instructions:  You start a conversation → Claude reads nothing → no Compass context
Session with custom instructions:     You start a conversation → custom instructions applied automatically → Claude reads your Compass files before responding
```

See the detailed recipes in `/recipes/` for the exact text to paste for each tool.

---

## Reference implementations

This repo includes:

**Templates** (`/templates/`): Empty markdown files for each Compass category, ready to copy into a new Compass.

**Agent integration recipes** (`/recipes/`): System prompt snippets and instructions for connecting various AI tools to a Compass. Includes:
- `cowork.md` — instructions for Claude Cowork (Drive-native)
- `claude-ai.md` — instructions for Claude.ai Projects (Drive-connected)
- `claude-code.md` — instructions for Claude Code (local filesystem or Git)
- `cursor.md` — instructions for Cursor (local filesystem)
- `chatgpt.md` — instructions for ChatGPT custom instructions
- `local-ollama.md` — instructions for fully-local setups

**Bootstrap prompts** (`/bootstrap/`): Prompts for initializing a Compass from existing material:
- `full-drive-scan.md` — scan your Google Drive to produce initial substrate drafts (Drive users)
- `local-folder-scan.md` — scan your local documents folder to produce initial substrate drafts (local and Git users)
- `voice-from-writing-samples.md` — focused voice extraction from writing samples
- `interview-perspectives.md` — conversational interview to populate perspective files (required for perspectives regardless of storage)
- `team-guidelines-from-history.md` — extract team guidelines from past decisions
- `facts-from-resume.md` — quick bootstrap of facts.md

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

**What's the recommended storage?**

There isn't one universal answer — it depends on your situation. Google Drive for non-technical users who want multi-device access and Cowork/Claude.ai integration. Local folder for developers who want sovereignty and use Claude Code or Cursor. Git for developers who want audit trails, diffs, or team collaboration. See the Setup section for a comparison table.

**How does this differ from "Notion AI" or "ChatGPT custom instructions"?**

Both are tool-specific. Your context lives in their product. You can't take it with you. Switching tools means rebuilding context.

The Compass is portable and tool-agnostic. The same files work with Cowork, Claude.ai, Cursor, ChatGPT, Claude Code, and any future tool that can read markdown. You own your Compass; tools are visitors.

**What about privacy?**

The Compass lives in your storage of choice. You control who has access. For maximum privacy, use a local folder — nothing leaves your machine. For team Compasses, apply appropriate access controls in your storage system (Drive sharing, repo visibility settings, etc.).

**How do I bootstrap a Compass when starting from nothing?**

See `/bootstrap/` for prompts that help. Drive users start with `full-drive-scan.md`; local and Git users start with `local-folder-scan.md`. Both produce drafts in about an hour that you then review. The Compass gets richer through use; perfect bootstrapping isn't necessary.

**What if I disagree with the folder structure?**

The structure is a convention, not a requirement of the universe. Fork the repo, propose changes, or just adapt the structure for your needs and document the adaptation in your `COMPASS.md`. Other adopters will know what you've done because they can read your schema.

The hope is that the standard structure works for most use cases and adaptations are rare. Feedback welcome.

---

## Get involved

- **Use it:** Bootstrap your own Compass from the templates in `/templates`. Follow the recipes in `/recipes` to connect your AI tool of choice.
- **Integrate it:** Add compass-md support to your agent or tool. The refinement format is the integration surface — your tool reads Compass files before acting and writes to `refinements/pending/` when it observes something worth capturing.
- **Improve it:** File issues for spec gaps. Submit PRs for new integration recipes, better bootstrap prompts, or anonymized example Compasses. Implementations (dashboards, CLI tools, MCP servers, IDE plugins) belong here too — link them in an issue so the community can find them.

See `CONTRIBUTING.md` for details.

---

## Status

**Current version:** v0.1 (initial draft)
**Stability:** Pre-stable. Expect refinements based on early adopter feedback.
**Published by:** [Hiipo](https://hiipo.io). Compass-md is the open context substrate. Hiipo is the commercial active memory layer that sits alongside it — handling real-time, conviction-scored memory that complements the stable context compass-md maintains.

---

## Acknowledgments

This convention is inspired by:

- [Andrej Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the schema-driven LLM-maintained wiki pattern
- [Vannevar Bush's Memex (1945)](https://en.wikipedia.org/wiki/Memex) — the original vision of personal, curated context with associative trails
- The CLAUDE.md and AGENTS.md conventions — the pattern of meta-files that instruct agents how to operate

The personal-context-Compass framing and the team-context extension are this convention's specific contributions on top of those foundations.

## Further reading

For the broader landscape that compass sits within:

- [How AI Agent Memory Works](https://memory.cobanov.dev/) by Mert Cobanov — an excellent interactive essay on memory architectures (vector stores, knowledge graphs, hierarchical memory, multi-agent systems). Covers layer 3 of the personal AI stack described in "Where compass fits."
- [MemGPT paper](https://arxiv.org/abs/2310.08560) — hierarchical memory for stateful agents
- [Letta documentation](https://docs.letta.com/guides/core-concepts/stateful-agents) — self-editing memory architectures
- [ChatGPT memory announcement](https://openai.com/index/memory-and-new-controls-for-chatgpt/) — the per-tool memory pattern compass-md is positioned alongside, not against
