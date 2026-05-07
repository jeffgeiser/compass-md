#!/usr/bin/env python3
"""
pending-refinements.py — lists pending refinements in a Compass with a summary table

Usage: python pending-refinements.py <compass-folder>

Dependencies: none (stdlib only)
"""

import sys
import re
from pathlib import Path
from typing import Optional


def parse_frontmatter(content: str) -> tuple[Optional[dict], str]:
    """Return (frontmatter_dict, remaining_content). frontmatter_dict is None if not found."""
    if not content.startswith("---"):
        return None, content
    end = content.find("\n---", 3)
    if end == -1:
        return None, content
    fm_text = content[4:end]
    remaining = content[end + 4:].lstrip("\n")
    fields = {}
    for line in fm_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.split("#")[0].strip()
    return fields, remaining


def extract_observation_first_line(body: str) -> str:
    """Find the ## Observation section and return its first non-empty line."""
    in_observation = False
    for line in body.splitlines():
        if line.strip().lower().startswith("## observation"):
            in_observation = True
            continue
        if in_observation:
            if line.startswith("## "):
                break
            stripped = line.strip()
            if stripped:
                if len(stripped) > 80:
                    stripped = stripped[:77] + "..."
                return stripped
    return ""


def col(text: str, width: int) -> str:
    text = str(text) if text else ""
    if len(text) > width:
        text = text[:width - 1] + "…"
    return text.ljust(width)


def main():
    if len(sys.argv) != 2:
        print("Usage: python pending-refinements.py <compass-folder>", file=sys.stderr)
        sys.exit(2)

    compass_path = Path(sys.argv[1]).expanduser().resolve()
    pending_dir = compass_path / "refinements" / "pending"

    if not pending_dir.is_dir():
        print(f"No refinements/pending/ directory found at {compass_path}", file=sys.stderr)
        sys.exit(1)

    refinements = []
    for rf in sorted(pending_dir.iterdir()):
        if rf.name.startswith(".") or rf.suffix != ".md":
            continue
        content = rf.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(content)
        obs = extract_observation_first_line(body)
        refinements.append({
            "filename": rf.name,
            "proposed_at": (fm or {}).get("proposed_at", ""),
            "proposed_by": (fm or {}).get("proposed_by", ""),
            "target_file": (fm or {}).get("target_file", ""),
            "target_section": (fm or {}).get("target_section", ""),
            "change_type": (fm or {}).get("change_type", ""),
            "confidence": (fm or {}).get("confidence", ""),
            "observation": obs,
        })

    if not refinements:
        print(f"No pending refinements in {pending_dir}")
        sys.exit(0)

    print(f"\nPending refinements: {len(refinements)}\n")
    print(f"{'Filename':<45} {'Proposed at':<22} {'By':<12} {'Target file':<30} {'Type':<12} {'Conf':<8}")
    print("-" * 131)
    for r in refinements:
        print(
            f"{col(r['filename'], 45)} "
            f"{col(r['proposed_at'], 22)} "
            f"{col(r['proposed_by'], 12)} "
            f"{col(r['target_file'], 30)} "
            f"{col(r['change_type'], 12)} "
            f"{col(r['confidence'], 8)}"
        )
        if r["target_section"]:
            print(f"  Section: {r['target_section']}")
        if r["observation"]:
            print(f"  Observation: {r['observation']}")
        print()


if __name__ == "__main__":
    main()
