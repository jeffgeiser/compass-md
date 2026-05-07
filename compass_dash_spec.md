# compass-dash — Specification

A small local dashboard for reviewing and applying refinements to a Compass that follows the [compass-md convention](https://github.com/[org]/compass-md).

This is a **companion tool**, not part of the Compass convention itself. The convention works without this dashboard; the dashboard makes the weekly review of pending refinements easier for users who don't want to manage file moves manually in Drive or their filesystem.

---

## Purpose and scope

### What this does

1. Shows pending refinements with full content and target file context
2. Lets the user accept, reject, or edit-and-accept each refinement with one click
3. Applies all the file operations (modifying target files, moving refinement files, logging events) automatically when the user accepts or rejects
4. Shows a simple home view with substrate health indicators (pending count, recent activity, weekly review status)

### What this does NOT do

- **No chat interface.** The dashboard does not talk to LLMs or generate content. For that, use Cowork, Claude.ai, or any other AI tool.
- **No primary authoring.** Users edit substrate files in their preferred editor (Drive's UI, VS Code, Obsidian). The dashboard is for reviewing AI-proposed changes only.
- **No sync management.** If using Drive storage, Drive Desktop or rclone handles sync. The dashboard operates on a local folder.
- **No lint generation.** Lint runs separately (via the spec's `lint-compass.py` script or via an AI tool). The dashboard may *display* lint reports but doesn't produce them.
- **No multi-user, no team mode.** Single Compass folder, single reviewer. Future enhancement.
- **No background process.** User opens the dashboard when they want to review. No tray icon, no notifications, no daemon.
- **No SaaS, no hosting, no auth.** Localhost only. Single-user only.

### Hard constraints

- One person can build this in a weekend (target ~1500 lines of code total)
- Single binary distribution (compile once, run anywhere)
- No external service dependencies at runtime
- No database — the filesystem is the data layer
- No build step for the frontend (vanilla HTML/CSS/JS, no React/npm/webpack)

---

## Architecture

### Stack

- **Language:** Go (recommended for single-binary distribution and built-in HTTP server). Alternatives: Rust, Node with `pkg`, Python with PyOxidizer/Nuitka.
- **Backend:** HTTP server on `localhost:7174`. RESTful endpoints. Standard library only where possible.
- **Frontend:** Vanilla HTML/CSS/JS served by the Go binary. No framework. No build step. Files embedded in the binary at compile time.
- **Storage:** Direct filesystem access to the user's Compass folder. No database.
- **Config:** Single config file at `~/.compass-dash/config.json` storing the path to the Compass folder and minor preferences.

### Why these choices

Go gives you a single 5-15MB binary that runs on Mac, Linux, and Windows with no dependencies. The standard library has everything needed (HTTP, filesystem, YAML/JSON parsing). Go's `embed` package lets you compile static frontend files into the binary so distribution is truly single-file.

Vanilla JS for the frontend keeps the build simple and the codebase small. The dashboard doesn't need React or any framework — it has 3 screens, all forms and lists. Adding a build step would double the project complexity for marginal UX gain.

Direct filesystem access is correct because the spec defines the substrate as files in a folder. Adding a database would create a sync problem (database state vs. filesystem state). Reading files on demand and watching for changes is simpler.

### Data flow

```
User opens browser → localhost:7174
        ↓
Go binary serves index.html
        ↓
Frontend JS calls GET /api/refinements/pending
        ↓
Backend reads compass/refinements/pending/*.md from disk
Backend parses each file's frontmatter and content
Backend returns JSON array of refinements
        ↓
Frontend renders list

User clicks a refinement
        ↓
Frontend calls GET /api/refinements/{id}
Backend returns full refinement content + current state of target file
        ↓
User reviews and clicks Accept

Frontend calls POST /api/refinements/{id}/accept
        ↓
Backend:
  1. Reads target file
  2. Applies the proposed change (parse "Proposed change" section)
  3. Writes modified target file back to disk
  4. Moves refinement file from pending/ to accepted/
  5. Appends entry to log.md
  6. Returns success
        ↓
Frontend shows confirmation and removes from list
```

### File system operations

The dashboard performs these operations on the Compass folder:

**Reads:**
- List files in `refinements/pending/`
- Read each refinement file (frontmatter + body)
- Read target files referenced by refinements
- Read `log.md` for recent activity
- Read accepted/rejected counts from `refinements/accepted/` and `refinements/rejected/`

**Writes:**
- Update target files when refinements are accepted (apply the proposed change)
- Move refinement files between pending/, accepted/, rejected/ (using OS rename)
- Append entries to `log.md` (append-only, never modify existing entries)
- Append rejection reasons to refinement files when rejecting
- Update `~/.compass-dash/config.json` when settings change

**Never does:**
- Modify or delete entries in `log.md` other than appending
- Modify accepted/rejected refinement files (they're historical record)
- Touch any file outside the configured Compass folder
- Make any network calls (no telemetry, no auto-update checks, nothing)

---

## API endpoints

All endpoints are JSON over HTTP, served by the Go binary on `localhost:7174`.

### Health and config

**`GET /api/health`** — Returns `{status: "ok", compass_path: "/path/to/compass"}`. Used for sanity checking.

**`GET /api/config`** — Returns the current config (compass folder path, default rejection reason template).

**`POST /api/config`** — Update config. Body: `{compass_path?: string, default_rejection_template?: string}`.

### Refinements

**`GET /api/refinements/pending`** — Returns array of pending refinements:
```json
[
  {
    "id": "2026-04-23-143207_voice-tone-update",
    "filename": "2026-04-23-143207_voice-tone-update.md",
    "proposed_at": "2026-04-23T14:32:07Z",
    "proposed_by": "cowork",
    "target_file": "self/voice.md",
    "target_section": "Vocabulary preferences",
    "change_type": "addition",
    "confidence": "medium",
    "observation_preview": "First 200 chars of observation section..."
  }
]
```

Sorted oldest first (by proposed_at).

**`GET /api/refinements/{id}`** — Returns full refinement detail:
```json
{
  "id": "...",
  "filename": "...",
  "frontmatter": {...},
  "observation": "Full observation section",
  "proposed_change": "Full proposed change section",
  "reasoning": "Full reasoning section",
  "evidence": "Full evidence section",
  "target_file": {
    "path": "self/voice.md",
    "current_content": "Full current content of target file"
  }
}
```

**`POST /api/refinements/{id}/accept`** — Accept a refinement.
- Body: `{edited_change?: string}` — optional override of the proposed change (for edit-and-accept flow)
- Behavior:
  1. Read target file
  2. Apply the change (proposed change or edited change) to target file
  3. Write target file back
  4. Move refinement file from pending/ to accepted/
  5. Append to log.md: `## [YYYY-MM-DD HH:MM] refinement-accepted | {target_file} | {brief description from refinement}`
- Returns `{status: "accepted", commit_url?: null}` (commit_url null for non-git storage)

**`POST /api/refinements/{id}/reject`** — Reject a refinement.
- Body: `{reason: string}` (required)
- Behavior:
  1. Append `## Rejection reason\n\n{reason}` to refinement file
  2. Move refinement file from pending/ to rejected/
  3. Append to log.md: `## [YYYY-MM-DD HH:MM] refinement-rejected | {target_file} | {reason briefly}`
- Returns `{status: "rejected"}`

### Activity and stats

**`GET /api/activity/recent`** — Returns recent log.md entries (last 30 days).
```json
[
  {
    "timestamp": "2026-04-23T14:32:07Z",
    "event_type": "refinement-accepted",
    "description": "self/voice.md | Voice tone update"
  }
]
```

**`GET /api/stats`** — Returns substrate health summary:
```json
{
  "pending_count": 7,
  "oldest_pending_age_days": 12,
  "accepted_this_month": 23,
  "rejected_this_month": 5,
  "last_review_date": "2026-04-16T10:00:00Z",
  "substrate_files_count": 18,
  "lint_report_available": false
}
```

### Substrate browsing (basic)

**`GET /api/files`** — List all markdown files in the Compass folder, organized by directory.

**`GET /api/files/{path}`** — Read a substrate file's content.

These enable the basic browse view. Editing substrate files directly through the dashboard is NOT in scope — the user opens them in their editor of choice.

---

## UI specification

Three screens, all served from the same single-page HTML.

### Screen 1: Home / Dashboard

URL: `/`

Layout: Single-column, max width ~800px, centered.

Sections (top to bottom):

**Header**
- "Compass Dashboard" title
- Compass folder path (small text)
- Settings cog icon (links to settings)

**Pending refinements summary**
- Big number: count of pending refinements
- If pending count > 0: "Review pending refinements →" button (links to /review)
- If pending count is 0: "No pending refinements. Nice." quiet text
- If oldest pending > 14 days: yellow warning indicator with "Some refinements are getting stale"

**This week**
- "Reviewed this week: X" (count of accept+reject events from log.md in last 7 days)
- "Last review: N days ago"

**Recent activity**
- Last 10 events from log.md
- Each event: timestamp, type icon, description
- Compact, scannable

**Substrate at a glance**
- File counts by category (self, team, etc.)
- Sparseness indicators for empty categories ("no perspectives yet")

### Screen 2: Refinement review

URL: `/review` or `/review/{id}`

Layout: Two-column on wide screens, single-column on narrow.

**Left column: List of pending refinements**
- Each item: target_file (bold), target_section, change_type, confidence, age, first line of observation
- Currently selected item highlighted
- Stale items (>14 days) get a subtle warning border
- Keyboard navigation (j/k or arrow keys) for power users

**Right column: Selected refinement detail**

Three tabs at top: **Refinement** | **Target file (current)** | **Target file (after change)**

*Refinement tab:*
- Frontmatter (proposed by, when, confidence) in a small info box
- Observation, Proposed change, Reasoning, Evidence sections rendered as markdown
- Three buttons at bottom: **Accept** (green), **Edit & Accept** (gray), **Reject** (red)

*Target file (current) tab:*
- Current content of target file rendered as markdown
- Useful for context before deciding

*Target file (after change) tab:*
- Preview of what target file will look like after change is applied
- For additions: shows where new content will be inserted (highlighted)
- For modifications: shows diff (current vs. new) with red/green highlighting
- For removals: shows what will be removed (struck through)

**Accept flow:**
- Click Accept
- Brief confirmation toast: "Accepted. Target file updated."
- Refinement removed from list, next pending refinement auto-selected

**Edit & Accept flow:**
- Click Edit & Accept
- Refinement detail collapses, an editor (textarea, monospace, ~20 lines) opens with the proposed change pre-filled
- User edits as needed
- Save & Accept button at bottom; Cancel returns to detail view
- On save, applies edited change instead of original proposed change

**Reject flow:**
- Click Reject
- Modal opens with textarea labeled "Why are you rejecting this?"
- Optional: dropdown of common reasons (false positive, already in substrate, low value, agent misread context, other)
- Submit button confirms rejection
- Brief confirmation toast, refinement removed from list

### Screen 3: Settings

URL: `/settings`

Single-column form.

**Compass folder**
- Text input showing current path
- "Browse" button (opens native folder picker via OS dialog)
- "Validate" button — runs basic checks (folder exists, COMPASS.md present, refinements/ subfolders present) and shows results

**Default rejection reason templates**
- List of common rejection reasons (editable)
- These appear in the reject modal dropdown
- Defaults: "False positive", "Already captured elsewhere", "Low confidence inference", "Stale, no longer relevant"

**Display preferences**
- Stale refinement threshold (default 14 days)
- Theme: light / dark / auto

**About**
- Version
- Link to compass-md spec on GitHub
- Link to compass-dash repo

---

## Implementation notes for Claude Code

### Project structure

```
compass-dash/
├── README.md
├── go.mod
├── go.sum
├── main.go                    # entry point, CLI args, server start
├── server/
│   ├── server.go              # HTTP server setup
│   ├── handlers.go            # all API endpoint handlers
│   ├── middleware.go          # logging, CORS for localhost
│   └── static.go              # embed and serve frontend files
├── compass/
│   ├── compass.go             # main Compass type, folder operations
│   ├── refinement.go          # refinement file parsing
│   ├── log.go                 # log.md operations
│   └── target.go              # target file modification logic
├── config/
│   └── config.go              # load/save ~/.compass-dash/config.json
├── frontend/
│   ├── index.html             # single-page app shell
│   ├── app.js                 # all frontend logic, vanilla JS
│   ├── style.css              # styling, no framework
│   └── markdown.js            # tiny markdown renderer (use marked.js or similar)
├── LICENSE                    # MIT
└── INSTALL.md                 # installation instructions
```

### Key implementation considerations

**Refinement file parsing.** Refinement files have YAML frontmatter (between `---` lines) plus markdown body with H2 sections (Observation, Proposed change, Reasoning, Evidence). Use `gopkg.in/yaml.v3` for frontmatter, simple regex/string operations for sections. Don't over-engineer — these are simple structured documents.

**Applying refinements to target files.** The hardest implementation challenge. The proposed change might be:
- An addition to a specific section ("Add to 'Vocabulary preferences > I avoid' section: ...")
- A modification of existing content (with before/after blocks)
- A removal of specific content

For v1, support these via **simple section-based insertion**:
- If frontmatter says `change_type: addition` and `target_section` is specified, append the proposed change content to that section in the target file
- If `change_type: modification`, look for the exact "before" text in the target and replace with "after" text
- If `change_type: removal`, find and remove the specified content
- If anything is ambiguous (section not found, before text not exact match), DO NOT apply — return error and tell user to use Edit & Accept manually

This conservative approach means some refinements require manual application via Edit & Accept, but prevents bad automatic edits. Better to require occasional manual intervention than to silently corrupt the substrate.

**File moves.** Use `os.Rename()` for moving refinement files between pending/, accepted/, rejected/. Atomic on same filesystem. Handle errors gracefully (file already exists, permission denied, etc.).

**log.md appends.** Open file in append mode, write new entry with consistent format `## [YYYY-MM-DD HH:MM] {event-type} | {description}\n\n`. Always include trailing newlines. Never modify existing log entries.

**Localhost-only binding.** Bind HTTP server to `127.0.0.1:7174` explicitly, NOT `0.0.0.0`. This prevents the dashboard from being accessible over the network. Add a check on startup to confirm binding worked.

**Auto-open browser.** On `compass-dash` command, after server starts, automatically open `http://localhost:7174` in the default browser. Use `github.com/pkg/browser` or the standard library's `os/exec` with platform-specific commands.

**Frontend embedding.** Use Go's `embed` package (`//go:embed frontend/*`) to compile the HTML/CSS/JS into the binary. Distribution becomes a single executable file.

**Error handling.** Every filesystem operation can fail. Surface errors to the user via the API and the UI — don't silently fail. The user needs to know if a refinement couldn't be applied so they can fix it manually.

**Cross-platform.** Build for darwin/amd64, darwin/arm64, linux/amd64, linux/arm64, windows/amd64. Use Go's cross-compilation. Provide download links for each in the README.

**No telemetry.** Zero. The dashboard makes no network calls except serving localhost HTTP. This is a sovereignty product; respect that.

### Build and distribution

**Local development:**
```bash
go run main.go --compass-path=/path/to/compass
```

**Production build:**
```bash
go build -o compass-dash main.go
```

**Cross-platform release:**
```bash
make release  # builds for all platforms, outputs to dist/
```

**Install via curl-bash** (matching Hiipo's pattern):
```bash
curl -sSf https://compass-md.io/dash/install | bash
```

The install script detects OS and architecture, downloads the appropriate binary, places it in `/usr/local/bin/compass-dash` (or user's PATH), prompts for the Compass folder path on first run.

### What to skip in v1

- Lint integration (just display lint reports if present in lint/ folder, don't generate them)
- Multiple Compass support (one folder per dashboard instance)
- Theme customization beyond light/dark/auto
- Keyboard shortcuts beyond j/k navigation
- Search across substrate files
- Direct file editing in the dashboard
- Authentication (single-user, localhost only — no auth needed)
- Multi-language support (English only for v1)
- Mobile-responsive design (desktop only — this is a desktop tool)

These can come in v2 based on actual user feedback.

---

## Integration with the compass-md spec

### Where this lives

**Recommended:** A separate companion repo at `github.com/[org]/compass-dash`.

This keeps the spec repo focused on the convention itself. The dashboard is one of several possible review interfaces (others might include GitHub PR-based review for devs, Slack bot integrations for teams, future tools others build). Bundling the dashboard into the spec repo would imply it's the "canonical" review tool, which would discourage alternative implementations.

The compass-md spec repo should reference compass-dash as a recommended companion tool in its `recipes/README.md` or a new `tools/` doc. Cross-linking, not coupling.

### Repo description / positioning

> compass-dash — A small local dashboard for reviewing refinements to your [compass-md](https://github.com/[org]/compass-md) substrate. Single binary, no SaaS, no auth. Reads and writes your Compass folder directly.

### Versioning and compatibility

The dashboard declares which version of the compass-md convention it supports. Initial release: supports v0.1 of the convention.

If the convention moves to v0.2 with breaking changes, the dashboard ships a v0.2-compatible release. Older dashboard versions remain available for users on older spec versions.

### Distribution

Build the dashboard binary, host downloads at `compass-md.io/dash/` (or wherever the spec hosts its docs). Ship via:

1. Direct binary downloads from a releases page (Mac/Linux/Windows)
2. `curl-bash` install script for one-line setup
3. Eventually: Homebrew formula, Scoop manifest, AUR package

For v1, just direct downloads and curl-bash. Package manager support is a later enhancement.

---

## Build sequence for Claude Code

If this spec is given to Claude Code as a build task:

1. **Create the project structure** with all directories and empty files
2. **Implement `compass/` package** first (folder operations, refinement parsing, log handling) — this is the core logic
3. **Add unit tests** for the `compass/` package — refinement parsing, applying changes to target files, file moves
4. **Implement `config/` package** — load/save config file
5. **Implement `server/` package** — HTTP server, all API endpoints
6. **Implement frontend** — index.html, app.js, style.css
7. **Wire up `main.go`** — CLI args, start server, open browser
8. **Add the static file embedding** via Go's embed package
9. **Test end-to-end** — create a test Compass folder, run the dashboard, accept and reject some test refinements
10. **Build cross-platform binaries** and document distribution

Estimated effort: 2-3 focused days for someone comfortable with Go, plus a day for polish and cross-platform testing. A weekend project for someone moving fast.

### Critical thing to get right

**The "apply refinement to target file" logic in `compass/target.go`.** This is the only place where the dashboard modifies user content automatically. Bugs here corrupt user substrates. Worth extra unit testing, conservative behavior (refuse to apply ambiguous changes), and clear error messages when manual application is needed.

Everything else in the dashboard is straightforward CRUD. This one piece is where care matters.

---

## Future enhancements (post-v1)

Things to defer until real users ask for them:

- File watching for auto-refresh while dashboard is open
- Lint integration (run `lint-compass.py` from the dashboard)
- Multiple Compass folders / Compass switcher
- Drive API integration (talk to Drive directly, no local sync needed)
- Team mode (multiple users, refinement assignment, review queues)
- Refinement search and filtering
- Bulk operations (accept all from this agent, reject all matching pattern)
- Export functionality (CSV of accepted refinements, audit reports)
- Notifications (system tray, desktop notifications when new refinements arrive)
- Dark mode
- Keyboard shortcuts beyond basic navigation

Each of these is reasonable but adds complexity. Ship v1 minimal, see what users actually need, add accordingly.

---

## Risk assessment

**Risk: dashboard corrupts a user's substrate via bad automatic refinement application.**
Mitigation: conservative apply logic, refuse to apply ambiguous changes, comprehensive testing of `compass/target.go`, "Edit & Accept" flow as escape hatch for any case where automatic application would be risky.

**Risk: users use the dashboard but the underlying convention doesn't get adoption.**
Mitigation: the dashboard is positioned as a companion to the convention, not the product itself. If the convention doesn't get adoption, the dashboard isn't valuable, and that's the right outcome — neither should be propped up by the other.

**Risk: building the dashboard distracts from validating the spec.**
Mitigation: ship the spec first, then build the dashboard with concrete signal that the manual review friction is real. Spec launch is a separate, earlier event.

**Risk: dashboard scope creeps over time toward becoming a SaaS or agent product.**
Mitigation: hard scope limits documented up front (this spec). Each new feature request gets evaluated against the "is this still a thin local review tool?" question.

---

## Success criteria for v1

The dashboard is successful if:

- A user can install it in under 2 minutes via curl-bash
- A user can review 10 pending refinements in under 5 minutes
- The accept/reject flow has zero friction (no extra clicks, no ambiguity)
- It works on Mac, Linux, and Windows without modification
- Total install + binary footprint is under 20MB
- Zero crashes during normal operation in the first month of testing
- Users self-report "the weekly review now actually happens because the dashboard makes it easy"

If any of these aren't true, iterate before promoting widely.
