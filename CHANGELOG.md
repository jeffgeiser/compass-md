# Changelog

All notable changes to the compass-md convention are documented here.

---

## [v0.1.0] — 2026-05-06

Initial release.

### Included in this release

**Convention spec**
- Core folder structure (`self/`, `team/`, `refinements/`)
- File purposes for all Compass categories
- Refinement format and propose/review workflow
- `COMPASS.md` schema file definition
- Log format and event types
- Compatibility notes for `CLAUDE.md`, `AGENTS.md`, Karpathy's wiki pattern

**Templates** (`/templates/`)
- `COMPASS.md` — schema file template
- `log.md` — event log template
- `self/voice.md`, `preferences.md`, `facts.md`, `decisions.md`
- `self/perspectives/README.md` — perspectives folder guide
- `team/README.md`, `guidelines.md`, `style.md`, `feedback_log.md`
- `team/criteria/README.md`
- `refinements/EXAMPLE-refinement.md`
- `INDEX.md` — optional index template

**Recipes** (`/recipes/`)
- `cowork.md` — Claude Cowork (Drive-native, recommended starting point)
- `claude-ai.md` — Claude.ai Projects (Drive-connected)
- `claude-code.md` — Claude Code (local filesystem)
- `cursor.md` — Cursor (local filesystem)
- `chatgpt.md` — ChatGPT custom instructions
- `local-ollama.md` — fully-local setups

**Bootstrap prompts** (`/bootstrap/`)
- `voice-from-writing-samples.md`
- `interview-perspectives.md`
- `team-guidelines-from-history.md`
- `facts-from-resume.md`

**Examples** (`/examples/`)
- Personal Compass example (Alex, B2B SaaS founder)
- Team proposal-review Compass example

**Helper scripts** (`/scripts/`)
- `validate-compass.py` — structural validation
- `pending-refinements.py` — pending refinement summary table
- `lint-compass.py` — Claude-powered health check

**Documentation** (`/docs/`)
- `faq.md`
- `compatibility.md`
- `design-rationale.md`
- `github-storage.md`

---

*Versions follow [Semantic Versioning](https://semver.org). Breaking convention changes bump the major version. Additions and clarifications bump the minor version.*
