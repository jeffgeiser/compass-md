# Recipe: Claude.ai Projects

Set up a Claude.ai Project that reads from your compass-md so every conversation in that project benefits from your context.

---

## Setup (5 minutes)

### 1. Confirm your Compass location

Your Compass folder should be in your Google Drive. Recommended path: `My Drive/compass/`.

### 2. Connect Drive to Claude.ai

If you haven't:
- Open Claude.ai → Settings → Connectors → Google Drive
- Authorize the connection

### 3. Create a Claude.ai Project

- Claude.ai → Projects → New Project
- Name: "My Hiipo" (or similar)
- Description: "Substrate-aware conversations"

### 4. Add your Compass folder to the project

- In the project's Files section, click "+" → Google Drive
- Navigate to your /compass/ folder
- Add the entire folder (Claude.ai will sync changes automatically)

### 5. Add custom instructions

In the project's custom instructions, paste:

```
You have access to my personal Compass in this project's files. The Compass
follows the compass-md convention v0.1.

Before responding to any request, follow this workflow:

1. Check COMPASS.md for conventions specific to this Compass
2. Identify which Compass files are relevant to the request:
   - Voice and tone questions → self/voice.md
   - Drafting on my behalf → self/voice.md + relevant self/perspectives/
   - Recommendations and decisions → self/preferences.md + relevant self/perspectives/ + self/decisions.md
   - Context about who I am → self/facts.md
3. Read those files
4. Respond with that context informing your output
5. Briefly cite which Compass files informed your response

If you observe something that warrants a Compass refinement (a correction, a stated preference, a new perspective, an inconsistency), at the end of your response include a section called "Compass refinement proposal" with:

- Target file (e.g., self/voice.md)
- Target section (e.g., "Vocabulary preferences")
- Change type (addition / modification / removal)
- Confidence (low / medium / high)
- Proposed change (the actual content)
- Reasoning (1-2 sentences)

Don't include refinement proposals in every response — only when you've observed something concrete that warrants one. Maximum one refinement per response.

I will manually save accepted refinements to my Compass. Don't try to write files directly.

Always cite Compass files. Always follow the proposal pattern. Never claim to have updated the Compass yourself.
```

### 6. Test

Start a new conversation in the project. Try:
- "Help me draft a response to this email." [paste email]
- "What's my view on [topic]?"
- "Recommend an approach to [decision I'm facing]."

The response should cite Compass files. After a meaningful exchange where you've corrected or refined Claude's output, see if it offers a refinement proposal.

---

## What to expect

Claude.ai's Projects feature with Drive integration syncs files automatically — when you update your Compass (in Drive or via accepted refinements), the project picks up the changes within minutes.

The custom instructions become part of every conversation in the project, so you don't need to re-explain the workflow each time.

Claude.ai cannot write files to Drive directly, so refinement proposals come back as text in the conversation. You manually save them to /compass/refinements/pending/ if you want to keep them for later review, or apply them directly to the target file if you're ready to accept them.

---

## Tips

**Make this your default Claude.ai surface for Compass-relevant work.** Drafting, planning, decision-making — anything where your context matters. Use vanilla Claude.ai for general questions where your context isn't relevant.

**Voice mode works.** Talking to Claude.ai in voice mode in this project gets all the Compass benefits. Useful for "talk through a decision" sessions.

**Mobile works.** Claude.ai on mobile in this project also reads the Compass. Useful for Compass-aware conversations on the go.

**Keep the Compass small enough to fit.** Claude.ai's Project file capacity is generous but not infinite. If your Compass grows large (mostly via accumulating perspective files), the index file pattern from Karpathy's wiki helps — Claude reads INDEX.md first to find relevant files rather than loading everything.

---

## Limitations

No automatic refinement file creation. Refinements come back as text proposals you manually save.

No background watching. Refinements only get proposed during conversations, not when you're not in the project.

If your Compass gets very large (hundreds of files), you may want to use the index pattern more aggressively, or split Compasses by context (one for personal, one for a specific work project, etc.).
