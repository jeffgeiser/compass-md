# Recipe: Claude Cowork

Connect Cowork to your Compass so it reads your context before acting and proposes refinements as it works with you.

This is the recommended starting recipe — Cowork has native Drive integration and can both read and write to your Compass folder, which makes the full read-write loop work end-to-end without additional tooling.

---

## Setup (5 minutes)

### 1. Confirm your Compass location

Your Compass folder should be in your Google Drive. Recommended path: `My Drive/compass/`. If you haven't created it yet, follow the Setup section in the main README first.

### 2. Connect Drive to Cowork

If you haven't already:
- Open Cowork
- Settings → Connectors → Google Drive
- Authorize the connection

### 3. Add the Compass instructions to a Cowork project

Create or open a Cowork project where you'll do work that should benefit from your Compass (drafting, planning, research, evaluation).

In the project's custom instructions, paste:

```
You have access to my Compass at /compass/ in my Google Drive.
This Compass follows the compass-md convention v0.1.

Before acting on my behalf, follow this workflow:

1. Read /compass/COMPASS.md to understand the conventions
2. Identify which Compass files are relevant to the current task:
   - Drafting content → read /compass/self/voice.md and any relevant /compass/self/perspectives/*.md
   - Making recommendations → read /compass/self/preferences.md and relevant /compass/self/perspectives/*.md
   - Establishing context → read /compass/self/facts.md
   - Recalling decisions → read /compass/self/decisions.md
3. Read those files
4. Act with that context informing your output
5. At the end of your response, briefly cite which Compass files informed your output

If during our session you observe something that warrants a Compass refinement (a correction I made, a stated preference, a new perspective I expressed, an inconsistency with an existing file), propose a refinement following these rules:

- Don't modify Compass files directly. Ever.
- Write a refinement file to /compass/refinements/pending/ following this format:
  - Filename: YYYY-MM-DD_HHMMSS_brief-description.md
  - Frontmatter: proposed_at, proposed_by (cowork), target_file, target_section, change_type, confidence
  - Sections: Observation, Proposed change, Reasoning, Evidence, Suggested follow-up
- Maximum 3 refinements per session — pick the most valuable ones
- Only propose refinements you're at least medium-confidence on
- After proposing a refinement, append an entry to /compass/log.md:
  ## [YYYY-MM-DD HH:MM] refinement-proposed | brief description

Always cite Compass files in your responses. Always follow the refinement workflow. Never edit Compass files directly.
```

### 4. Test the connection

Start a new conversation in the project. Ask Cowork something that should engage your Compass, like:
- "Draft a quick email to a client telling them the project is delayed by a week."
- "What's my view on [topic you have a perspective file for]?"

In its response, Cowork should cite which Compass files it read. If it doesn't, the instructions aren't taking — re-check the project setup.

### 5. Observe a refinement cycle

Use Cowork normally for a few sessions. When you correct its output, see if it proposes a refinement to /compass/refinements/pending/.

If refinements aren't getting proposed:
- Check that the instructions specifically tell it to propose refinements (not just "consider proposing")
- Check that you're actually correcting Cowork in articulable ways (not just rewriting silently)

### 6. Review pending refinements

Periodically (weekly is a good cadence to start), open /compass/refinements/pending/ in Drive and review what's there.

For each pending refinement:
- **Accept**: Apply the proposed change to the target file (you can do this manually or ask Cowork to apply it). Move the refinement file to /compass/refinements/accepted/.
- **Reject**: Move the refinement file to /compass/refinements/rejected/. Append a `## Rejection reason` section explaining why.
- **Edit and accept**: Modify the proposed change as needed before applying.

In Drive, this can be as simple as right-click → Move to → drag to the right folder.

---

## What to expect

The first few sessions, Cowork will read your Compass but the Compass is sparse so the impact is modest. As you accept refinements and the Compass grows, the impact grows. After a month of regular use, output should feel noticeably more aligned with your voice and preferences.

If you hit a session where Cowork's output feels off, that's signal:
- Is it because the Compass is missing something?
- Is it because Cowork isn't actually reading the Compass?
- Is it because the Compass has stale or incorrect content?

Diagnose and fix the underlying cause rather than just rewriting the output.

---

## Tips

**Bootstrap before relying.** Don't connect Cowork to an empty Compass. Spend 30 minutes filling in initial drafts of voice.md, preferences.md, and facts.md before connecting Cowork. The Compass needs *something* to be useful from session one.

**Use a dedicated project for Compass-aware work.** You may not want every Cowork session reading and writing to your Compass. A dedicated project keeps the Compass-aware behavior scoped.

**Watch for refinement spam.** If Cowork starts proposing 10 refinements per session, the cap in the instructions isn't being respected — adjust the instructions to be stricter.

**Iterate on the instructions.** The instructions above are a starting point. As you learn what Cowork does well or poorly with your Compass, refine the instructions. The project custom instructions field is itself a part of your Compass stack.

---

## Limitations

Cowork's Drive connector reads files on demand, not continuously. It won't notice changes to your Compass mid-conversation. If you edit a Compass file during a session, ask Cowork to re-read it to pick up the change.

Cowork's ability to write directly to specific paths in Drive can vary. If writing refinement files to /compass/refinements/pending/ isn't working in your version of Cowork, you may need to have Cowork output the refinement content in chat and manually save it. This is friction; we expect Cowork's write capabilities to keep improving.

For team Compasses with multiple users sharing the same /compass/ folder: each team member sets up their own Cowork project pointing at the team Compass. Coordinate on conventions for who reviews refinements (e.g., team lead reviews, or weekly review meeting).
