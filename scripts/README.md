# Scripts

Optional helper utilities for working with a Compass. None of these are required — the convention works without them. They're useful when manual inspection becomes tedious.

**Requirements:** Python 3.10+. Each script lists its additional dependencies in a comment at the top.

---

## `validate-compass.py`

Checks a Compass folder against the convention spec. Reports violations with file paths and explanations. Exits with code 0 if valid, 1 if violations found.

```bash
python scripts/validate-compass.py ~/compass
```

Checks:
- `COMPASS.md` and `log.md` exist at root
- `refinements/pending/`, `refinements/accepted/`, `refinements/rejected/` exist
- If `self/` is active (per COMPASS.md): required files exist
- If `team/` is active: required files exist
- All pending refinements have valid frontmatter
- Log entries follow the standard format

Useful in CI if you keep your Compass in a git repo.

---

## `pending-refinements.py`

Lists all pending refinements with a summary table. Faster than opening each file when you're deciding which to review first.

```bash
python scripts/pending-refinements.py ~/compass
```

Output is a formatted table showing: filename, proposed_at, proposed_by, target_file, change_type, confidence, and the first line of the Observation section.

---

## `lint-compass.py`

Sends your Compass to Claude for a health check. Produces a report in `lint/{date}.md` inside your Compass folder covering contradictions, stale content, sparse categories, and long-pending refinements.

```bash
ANTHROPIC_API_KEY=your-key python scripts/lint-compass.py ~/compass
```

Requires an Anthropic API key. The API call uses claude-sonnet-4-6 by default and costs a few cents for a typical Compass.

---

## These are starting points

The scripts are simple and intentionally so. They're meant to be readable and hackable. If you need different behavior (Slack notifications for pending refinements, GitHub Actions integration for validation, a different lint model), fork and adapt.
