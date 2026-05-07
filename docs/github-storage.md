# GitHub as Compass Storage

How to keep your Compass in a GitHub repository instead of Google Drive.

---

## Tradeoffs vs. Drive

**GitHub gives you:**
- Complete diff history for every change — you can see exactly what changed in voice.md between two dates
- Branch and PR workflows — review Compass changes in pull requests with inline comments
- GitHub Actions for automation — run `validate-compass.py` and `lint-compass.py` on a schedule
- PRs as the native interface for refinement review — pending refinements become PRs; accepting means merging
- Familiar workflow for technical users

**GitHub costs you:**
- Requires git literacy — not accessible to non-technical team members
- No native Drive connector — tools like Cowork and Claude.ai can't read private GitHub repos directly (though GitHub Apps and MCP servers can bridge this)
- More friction to edit — changing a Compass file means editing, committing, and pushing
- Private repos require careful access management for shared Compasses

**Who should use GitHub storage:** technical users who are comfortable with git, want complete version history, or want CI-based automation for their Compass. Non-technical users and teams with mixed technical skill should start with Drive.

---

## Setup

### Personal Compass

```bash
# Create a private GitHub repo (CLI)
gh repo create my-compass --private

# Or via the GitHub UI, then clone
git clone git@github.com:yourname/my-compass.git ~/compass
cd ~/compass

# Create the structure
mkdir -p self/perspectives refinements/pending refinements/accepted refinements/rejected
touch COMPASS.md log.md self/voice.md self/preferences.md self/facts.md self/decisions.md
touch refinements/pending/.gitkeep refinements/accepted/.gitkeep refinements/rejected/.gitkeep

# Copy templates from this repo
# Initial commit
git add .
git commit -m "Compass: initial structure"
git push
```

### Team Compass

Same as above, but create the repo under your GitHub organization and invite team members with appropriate permissions:
- Team leads: write access (can merge refinement PRs)
- Team members: write access (can propose refinements, append to feedback_log)
- Read-only stakeholders: read access

---

## PRs as the refinement review interface

The most natural GitHub pattern for refinements: agents propose changes as pull requests rather than files in `refinements/pending/`.

**Agent workflow:**
1. Agent observes something worth capturing
2. Agent creates a branch: `refinement/voice-avoid-learnings-2026-04-14`
3. Agent commits the proposed change to the relevant Compass file on that branch
4. Agent opens a PR with the observation and reasoning as the PR description

**Human workflow:**
1. Review the PR diff — see exactly what changed
2. Add comments inline if you want to adjust the proposed change
3. Merge if you accept; close if you reject (add a closing comment with the reason)

This pattern requires agents that can use the GitHub API or git CLI (Claude Code can; Cowork cannot directly). If your agent can't create PRs, use the file-in-pending-folder pattern and commit the file; the PR interface is an enhancement, not a requirement.

---

## GitHub Actions for automation

### Validate on push

```yaml
# .github/workflows/validate.yml
name: Validate Compass

on: [push]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python scripts/validate-compass.py .
```

This runs `validate-compass.py` on every push. Any structural violation fails the check — useful for catching broken frontmatter in refinement files or missing required files.

### Weekly lint

```yaml
# .github/workflows/lint.yml
name: Weekly Compass Lint

on:
  schedule:
    - cron: "0 9 * * 1"  # Mondays at 9am UTC

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install anthropic
      - run: python scripts/lint-compass.py .
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      - run: |
          git config user.name "compass-lint[bot]"
          git config user.email "compass-lint@noreply"
          git add lint/
          git diff --cached --quiet || git commit -m "Compass: weekly lint $(date +%Y-%m-%d)"
          git push
```

This runs the lint script weekly and commits the report. Add `ANTHROPIC_API_KEY` as a GitHub Actions secret in your repo settings.

---

## Keeping Claude Code in sync

If you're using Claude Code with a local Compass that's backed by a GitHub repo, the standard git workflow applies:

```bash
# Pull latest Compass changes before starting a session
cd ~/compass && git pull

# After accepting refinements or editing files
git add .
git commit -m "Compass: accept voice refinement re: learnings"
git push
```

You can add this to your Claude Code workflow via a shell alias or a hook.

---

## Connecting to AI tools that need file access

Private GitHub repos aren't directly accessible to Cowork or Claude.ai. Options:

1. **Local sync:** `git pull` before sessions, then use local files with Claude Code
2. **GitHub App:** some tools (including emerging MCP servers) can read private repos via GitHub App auth
3. **Export to Drive:** sync your GitHub repo to Drive using a script or GitHub Action, then use the Drive-based recipes

If your primary tool is Claude Code, the local git workflow is the right fit. If you need Cowork or Claude.ai access, Drive (with the repo as a backup/source-of-truth) may be more practical than pure GitHub.
