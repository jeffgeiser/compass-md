#!/usr/bin/env python3
"""
lint-compass.py — produces a Compass health check report using Claude

Usage: ANTHROPIC_API_KEY=your-key python lint-compass.py <compass-folder>

Writes output to <compass-folder>/lint/<YYYY-MM-DD>.md
Appends a 'lint' entry to <compass-folder>/log.md

Dependencies:
  pip install anthropic

Model: claude-sonnet-4-6 (configurable via COMPASS_LINT_MODEL env var)
"""

import sys
import os
from datetime import datetime, timezone
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic", file=sys.stderr)
    sys.exit(1)


LINT_PROMPT = """You are performing a health check on a compass-md Compass — a collection of markdown files that captures personal or team context for use by AI agents.

The Compass files are provided below. Read them carefully, then produce a structured health check report.

Check for all of the following:

1. **Contradictions between files.** Look for factual inconsistencies across Compass files. For example: if facts.md says the owner is a "solo founder" but team/guidelines.md or other files mention "managing 5 engineers," flag this as a contradiction. If voice.md says the owner avoids passive voice but decisions.md uses passive voice throughout, note it. Look for these factual inconsistencies — they accumulate as the Compass grows and need explicit human reconciliation.

2. **Stale claims.** Content that is likely outdated based on dates in the Compass or internal evidence. For example: a facts.md entry that says "currently fundraising" but a decisions.md entry from 3 months later says the raise is complete.

3. **Sparse categories.** Files that have placeholders remaining or sections that are empty or nearly empty when they should have content for a healthy Compass.

4. **Dense categories that may need organization.** Files that have grown long enough to benefit from an INDEX.md entry or from being split into multiple more-specific files.

5. **Missing cross-references.** Cases where one file references a topic that another file covers, but doesn't link to it. Examples: a perspective file on pricing doesn't reference the decisions.md entry about a pricing decision.

6. **Refinements pending unusually long.** Any pending refinements that have been waiting more than 30 days without acceptance or rejection.

7. **Other health signals.** Anything else that would make this Compass less useful to an AI agent reading it — vague language that could be more specific, perspective files that lack the "What would change my mind" section, voice files with no concrete examples.

For each finding, provide:
- **Category:** (contradiction / stale / sparse / dense / cross-reference / pending-refinement / other)
- **File(s) involved:** specific file paths
- **Finding:** what the issue is
- **Recommendation:** what to do about it

End the report with a **Summary** section: overall health rating (Healthy / Needs attention / Significant issues) and the top 3 priority actions.

---

Compass files:

{compass_content}
"""


def read_compass_files(compass_path: Path) -> str:
    """Read all markdown files in the Compass and return them concatenated with file headers."""
    sections = []
    for md_file in sorted(compass_path.rglob("*.md")):
        rel = md_file.relative_to(compass_path)
        # Skip lint reports
        if rel.parts and rel.parts[0] == "lint":
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        sections.append(f"### {rel}\n\n{content}")
    return "\n\n---\n\n".join(sections)


def append_log_entry(compass_path: Path, date_str: str) -> None:
    log_file = compass_path / "log.md"
    if not log_file.exists():
        return
    entry = f"\n## [{date_str}] lint | Compass health check performed by lint-compass.py\n"
    with log_file.open("a", encoding="utf-8") as f:
        f.write(entry)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ANTHROPIC_API_KEY=your-key python lint-compass.py <compass-folder>", file=sys.stderr)
        sys.exit(2)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    compass_path = Path(sys.argv[1]).expanduser().resolve()
    if not compass_path.is_dir():
        print(f"Error: '{compass_path}' is not a directory", file=sys.stderr)
        sys.exit(1)

    model = os.environ.get("COMPASS_LINT_MODEL", "claude-sonnet-4-6")
    now = datetime.now(tz=timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    timestamp_str = now.strftime("%Y-%m-%d %H:%M")

    print(f"Reading Compass at {compass_path}...")
    compass_content = read_compass_files(compass_path)

    if not compass_content.strip():
        print("Error: No markdown files found in Compass", file=sys.stderr)
        sys.exit(1)

    print(f"Running lint with {model}...")
    client = anthropic.Anthropic(api_key=api_key)

    prompt = LINT_PROMPT.format(compass_content=compass_content)

    message = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    report_content = message.content[0].text

    report = f"# Compass Lint Report — {date_str}\n\nGenerated by lint-compass.py using {model}.\n\n---\n\n{report_content}\n"

    lint_dir = compass_path / "lint"
    lint_dir.mkdir(exist_ok=True)
    report_file = lint_dir / f"{date_str}.md"
    report_file.write_text(report, encoding="utf-8")
    print(f"Report written to {report_file}")

    append_log_entry(compass_path, timestamp_str)
    print(f"Log entry appended to log.md")


if __name__ == "__main__":
    main()
