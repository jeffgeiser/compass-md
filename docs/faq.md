# FAQ

Frequently asked questions about compass-md.

---

**Why "Compass"?**

Because that's what the convention is for AI tools: a compass for who you are, what you value, and how you work. Tools that read your Compass can navigate by it instead of guessing.

---

**Why not use a database or structured format?**

Markdown files are universally readable, human-editable, version-controllable, portable across storage, and consumable by every AI tool. Any structured format would introduce dependencies and friction. Markdown is the lowest common denominator that still supports rich content.

---

**Why not use MCP?**

MCP solves the problem of agents discovering and calling tools at runtime. The Compass doesn't need that — every modern agent already knows how to read and write files. The convention is the API. Adding MCP would be infrastructure overhead without proportional benefit.

That said, an MCP server that exposes Compass operations is a valid implementation choice for tools that benefit from it. The convention doesn't prevent it; it just doesn't require it.

---

**Why Google Drive as the recommended starting point?**

Drive has the broadest AI tool integration today (Cowork, Claude.ai, ChatGPT all have connectors), works on every device, has built-in versioning, and is familiar to non-technical users. The convention works in any storage; Drive is just the lowest-friction starting point for most people.

---

**How does this differ from "Notion AI" or "ChatGPT custom instructions"?**

Both are tool-specific. Your context lives in their product. You can't take it with you. Switching tools means rebuilding context.

The Compass is portable and tool-agnostic. The same files work with Cowork, Claude.ai, Cursor, ChatGPT, Claude Code, and any future tool that can read markdown. You own your Compass; tools are visitors.

---

**What about privacy?**

The Compass lives in your storage of choice. You control who has access. Agents reading the Compass operate under whatever permissions you give them in their respective products (your Cowork session, your Claude.ai account, etc.). Nothing in the convention requires you to share Compass content with anyone.

For team Compasses, treat the Compass folder like any other team document — apply appropriate access controls in your storage system.

---

**How do I bootstrap a Compass when starting from nothing?**

See `/bootstrap/` for prompts that help. The general approach: spend 30 minutes manually drafting initial files, then use bootstrap prompts to enrich them from existing material (your writing samples, team docs, past decisions). The Compass gets richer through use; perfect bootstrapping isn't necessary.

---

**What if I disagree with the folder structure?**

The structure is a convention, not a requirement of the universe. Fork the repo, propose changes, or just adapt the structure for your needs and document the adaptation in your `COMPASS.md`. Other adopters will know what you've done because they can read your schema.

The hope is that the standard structure works for most use cases and adaptations are rare. Feedback welcome.

---

**Do I need all the folders?**

No. A purely personal Compass might use only `self/`. A team Compass might use only `team/`. A project Compass might use a custom structure. The only required files are `COMPASS.md` and `log.md`. Everything else is opt-in.

---

**How often should I review pending refinements?**

Weekly is a good starting cadence. If you're using the Compass heavily, refinements accumulate faster and you may want to review more often. If usage is light, monthly is fine.

The important thing is to review them rather than letting them pile up. A backlog of unreviewed refinements means the Compass isn't improving.

---

**Can multiple people share a Compass?**

Yes. Team Compasses are explicitly designed for shared use. Put the Compass in a shared folder (Google Drive, GitHub repo) and each team member connects their agent tool to the shared Compass. Coordinate on who reviews refinements.

Personal Compasses generally aren't shared — they're personal context. You can share specific slices (a perspective file, a voice.md) with collaborators if you want an AI tool to understand both of you, but the convention doesn't have a built-in multi-owner personal Compass pattern.

---

**Is this compatible with CLAUDE.md?**

Yes. See `docs/compatibility.md` for details. Short answer: `CLAUDE.md` tells Claude Code how to operate in a project; `COMPASS.md` tells any agent how to read and contribute to the Compass. They serve different purposes and can coexist in the same repo.
