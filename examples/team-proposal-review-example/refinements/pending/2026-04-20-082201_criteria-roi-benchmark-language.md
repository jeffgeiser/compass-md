---
proposed_at: 2026-04-20T08:22:01Z
proposed_by: agent-3
target_file: team/criteria/proposal-review.md
target_section: "Evaluation dimensions > ROI clarity"
change_type: modification
confidence: high
session_context: weekly-refinement-cycle-2026-04-20
---

## Observation

Feedback log entries from 2026-04-18 and 2026-03-21 both document proposals where the ROI section used Foundry's generic benchmark numbers ("teams reduce MTTR by 40%") rather than numbers derived from the prospect's discovery call. Both were flagged correctly by Agent 1 and confirmed by Jordan — but the current criteria language doesn't explicitly distinguish Foundry benchmarks from prospect-derived data.

## Proposed change

In `team/criteria/proposal-review.md`, under "Evaluation dimensions > ROI clarity > Weak":

**Current:**
"Uses numbers we provided rather than numbers derived from the prospect's context."

**Proposed:**
"Uses Foundry-provided benchmark numbers (e.g., 'teams reduce MTTR by 40%') rather than numbers derived from the prospect's actual context — their observed incident frequency, documented engineering hours, or other data from the discovery call. Benchmark numbers are not a substitute for prospect-specific ROI math."

## Reasoning

Two feedback log entries in 5 weeks with the same failure pattern, both confirmed by Jordan, indicates this is a consistent enough gap to warrant a criteria update. The current language is technically correct but not specific enough to prevent the failure — reps interpret "numbers we provided" as external competitor data, not Foundry's own benchmarks. Making the failure mode explicit will catch it before review.

## Evidence

- 2026-04-18: Feedback log entry, Prospect-009: "ROI section used Foundry's internal benchmark data rather than numbers derived from Prospect-009's discovery call"
- 2026-03-21: Feedback log entry, Prospect-003: "proposal had narrative about reduced alert fatigue but no numbers" — similar root cause (generic claims vs. prospect-specific data)
