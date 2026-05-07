# Compass Event Log

Append-only chronological record of Compass events. Most recent first.

Event format: `## [YYYY-MM-DD HH:MM] {event-type} | {description}`

Event types:
- `init` — Compass created or major reorganization
- `manual-edit` — human edited Compass file directly
- `read` — agent read Compass files (optional; can be noisy)
- `refinement-proposed` — agent placed a proposal in `refinements/pending/`
- `refinement-accepted` — human accepted a pending refinement
- `refinement-rejected` — human rejected a pending refinement
- `lint` — Compass health check performed

---

## [2026-04-23 09:00] init | Compass created from compass-md v0.1 templates
