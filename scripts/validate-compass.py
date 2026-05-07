#!/usr/bin/env python3
"""
validate-compass.py — validates a Compass folder against the compass-md v0.1 spec

Usage: python validate-compass.py <compass-folder>

Dependencies: none (stdlib only)

Exit codes:
  0 — valid Compass
  1 — violations found (details printed to stdout)
  2 — usage error
"""

import sys
import os
import re
from pathlib import Path
from typing import Optional


REQUIRED_ROOT_FILES = ["COMPASS.md", "log.md"]
REQUIRED_REFINEMENT_DIRS = ["refinements/pending", "refinements/accepted", "refinements/rejected"]
REQUIRED_SELF_FILES = ["self/voice.md", "self/preferences.md", "self/facts.md", "self/decisions.md"]
REQUIRED_TEAM_FILES = ["team/guidelines.md"]

REFINEMENT_FRONTMATTER_FIELDS = [
    "proposed_at",
    "proposed_by",
    "target_file",
    "target_section",
    "change_type",
    "confidence",
]
VALID_CHANGE_TYPES = {"addition", "modification", "removal"}
VALID_CONFIDENCE_LEVELS = {"low", "medium", "high"}

LOG_ENTRY_PATTERN = re.compile(
    r"^## \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\] "
    r"(init|manual-edit|read|refinement-proposed|refinement-accepted|refinement-rejected|lint|ingest)"
    r" \| .+$"
)


def parse_frontmatter(content: str) -> Optional[dict]:
    """Extract YAML-style frontmatter from a markdown file. Returns None if not found."""
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    fm_text = content[4:end]
    fields = {}
    for line in fm_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.split("#")[0].strip()
    return fields


def check_compass_active_modules(compass_path: Path) -> tuple[bool, bool]:
    """Read COMPASS.md and return (self_active, team_active)."""
    compass_file = compass_path / "COMPASS.md"
    if not compass_file.exists():
        return False, False
    content = compass_file.read_text(encoding="utf-8")
    self_active = False
    team_active = False
    for line in content.splitlines():
        line_lower = line.lower()
        if "`self/`" in line_lower or "self/:" in line_lower:
            if "yes" in line_lower:
                self_active = True
        if "`team/`" in line_lower or "team/:" in line_lower:
            if "yes" in line_lower:
                team_active = True
    return self_active, team_active


def validate(compass_path: Path) -> list[str]:
    violations = []

    if not compass_path.is_dir():
        return [f"ERROR: '{compass_path}' is not a directory"]

    # Required root files
    for fname in REQUIRED_ROOT_FILES:
        if not (compass_path / fname).exists():
            violations.append(f"MISSING: {fname} (required at Compass root)")

    # Required refinement directories
    for rel_dir in REQUIRED_REFINEMENT_DIRS:
        if not (compass_path / rel_dir).is_dir():
            violations.append(f"MISSING: {rel_dir}/ (required directory)")

    # Read active modules from COMPASS.md
    self_active, team_active = check_compass_active_modules(compass_path)

    # Self module checks
    if self_active:
        for rel_file in REQUIRED_SELF_FILES:
            path = compass_path / rel_file
            if not path.exists():
                violations.append(f"MISSING: {rel_file} (self/ is active in COMPASS.md)")

    # Team module checks
    if team_active:
        for rel_file in REQUIRED_TEAM_FILES:
            path = compass_path / rel_file
            if not path.exists():
                violations.append(f"MISSING: {rel_file} (team/ is active in COMPASS.md)")

    # Validate pending refinements
    pending_dir = compass_path / "refinements" / "pending"
    if pending_dir.is_dir():
        for rf in sorted(pending_dir.iterdir()):
            if rf.name.startswith(".") or rf.suffix != ".md":
                continue
            content = rf.read_text(encoding="utf-8")
            fm = parse_frontmatter(content)
            if fm is None:
                violations.append(f"REFINEMENT: {rf.name} — missing frontmatter (expected YAML between --- markers)")
                continue
            for field in REFINEMENT_FRONTMATTER_FIELDS:
                if field not in fm or not fm[field]:
                    violations.append(f"REFINEMENT: {rf.name} — missing required frontmatter field: {field}")
            if "change_type" in fm and fm["change_type"] not in VALID_CHANGE_TYPES:
                violations.append(
                    f"REFINEMENT: {rf.name} — invalid change_type '{fm['change_type']}' "
                    f"(expected: {', '.join(sorted(VALID_CHANGE_TYPES))})"
                )
            if "confidence" in fm and fm["confidence"] not in VALID_CONFIDENCE_LEVELS:
                violations.append(
                    f"REFINEMENT: {rf.name} — invalid confidence '{fm['confidence']}' "
                    f"(expected: {', '.join(sorted(VALID_CONFIDENCE_LEVELS))})"
                )

    # Validate log entries
    log_file = compass_path / "log.md"
    if log_file.exists():
        for i, line in enumerate(log_file.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("## ["):
                if not LOG_ENTRY_PATTERN.match(line):
                    violations.append(
                        f"LOG: line {i} — entry doesn't match format "
                        f"'## [YYYY-MM-DD HH:MM] {{event-type}} | {{description}}': {line[:80]}"
                    )

    return violations


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate-compass.py <compass-folder>", file=sys.stderr)
        sys.exit(2)

    compass_path = Path(sys.argv[1]).expanduser().resolve()
    violations = validate(compass_path)

    if not violations:
        print(f"✓ Compass at {compass_path} is valid (compass-md v0.1)")
        sys.exit(0)
    else:
        print(f"Compass at {compass_path} has {len(violations)} violation(s):\n")
        for v in violations:
            print(f"  {v}")
        sys.exit(1)


if __name__ == "__main__":
    main()
