# Recipe: Local Models (Ollama, llama.cpp, etc.)

Use the Compass with a fully local LLM setup. No data leaves your machine.

Local models can't read Google Drive directly. Your Compass must be on the local filesystem — `~/compass/` is the recommended path.

---

## Setup

### 1. Get your Compass locally

If your Compass is in Drive, sync or copy it to your local machine. Then keep it on the filesystem as your source of truth. Drive can be a backup or secondary access point, but local is the path local models can read.

### 2. Choose your interface

How you interact with Ollama or llama.cpp determines how you inject Compass context. Common patterns:

**a) Prompt injection (any interface)**

The simplest approach: at the start of each conversation, paste the relevant Compass files into the prompt. Most local model UIs (Open WebUI, Enchanted, etc.) support large system prompts.

Typical starting prompt:
```
You are acting on behalf of [name] using the compass-md convention v0.1.

Compass files attached below. Read them before responding.

--- COMPASS.md ---
[paste contents]

--- self/voice.md ---
[paste contents]

--- self/preferences.md ---
[paste contents]

[paste other relevant files]
---

Now: [your actual request]
```

**b) System prompt in Open WebUI**

If you use Open WebUI with Ollama, create a model preset with a system prompt that includes your Compass content. This saves you from pasting each session.

**c) Shell script**

A short shell script can inject Compass files automatically:

```bash
#!/bin/bash
# compass-chat.sh
COMPASS_DIR=~/compass

# Build context from relevant files
CONTEXT=$(cat <<EOF
You are acting on behalf of the Compass owner using the compass-md convention v0.1.

$(cat "$COMPASS_DIR/COMPASS.md")

$(cat "$COMPASS_DIR/self/voice.md")

$(cat "$COMPASS_DIR/self/preferences.md")

$(cat "$COMPASS_DIR/self/facts.md")

Follow the convention: read context before responding, propose refinements
to refinements/pending/ when you observe something worth capturing.
EOF
)

# Pass to ollama
ollama run mistral --system "$CONTEXT" "$@"
```

Then: `./compass-chat.sh "Draft a quick email declining a meeting."`

---

## Refinement workflow with local models

Local models can propose refinements, but the workflow is more manual:

1. Ask the model to propose a refinement at the end of the session if it observed something worth capturing
2. The model outputs the refinement as text
3. You save it to `refinements/pending/` manually
4. Review and apply accepted refinements yourself

Local models generally can't write directly to the filesystem unless you're running them through a tool like Aider or a custom wrapper with file write access. If you are, adapt the Claude Code recipe's refinement instructions.

---

## What to expect

Local models vary significantly in instruction-following quality. Larger models (70B+) generally follow the Compass read-before-responding workflow reliably. Smaller models (7B-13B) often do, but may need more explicit instructions or may ignore the convention under load.

Adjust your expectations proportionally. The Compass adds value even if the model doesn't follow every instruction perfectly — having voice.md and preferences.md in context improves alignment even when the model doesn't cite the files.

---

## Tips

**Keep injected context lean.** Local models have context window limits, and a full Compass with many perspective files can crowd out the actual task. Inject only relevant files: voice.md and facts.md as defaults, then add specific perspectives or guidelines based on the task.

**Cache your most-used context.** If you have a system prompt that includes your core Compass files, create a model preset for it in your UI. The goal is zero friction for the sessions where you always want Compass context.

**Test instruction-following explicitly.** Ask the model: "What does my voice.md say about things I avoid?" If it can't answer from the injected context, the context isn't being used properly — adjust your system prompt or use a larger model.

**Check for context window cutoffs.** If you're injecting many Compass files and responses feel disconnected from the context, the model may have exceeded its usable context. Trim the injected files.

---

## Limitations

No Drive access. Local filesystem only.

Refinement file write-back requires manual steps or a custom wrapper.

Instruction-following for the full read-write protocol is weaker with smaller models. Treat refinement proposals from local models as drafts that need scrutiny.

Performance depends heavily on your hardware and the model size. The Compass works with any model that can follow instructions; better instruction-following gives better Compass alignment.
