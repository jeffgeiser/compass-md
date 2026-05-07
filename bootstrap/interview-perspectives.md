# Bootstrap: Interview to Populate Perspectives

A conversational interview prompt that helps you populate `self/perspectives/` files quickly.

---

## When to use this

When you want to populate Compass files for topics you have views on but haven't written down. Most people's strongest takes live in their head, not their Drive — interviewing yourself is a faster way to surface them than scanning past writing.

## What this produces

Draft perspective files for topics the conversation surfaces, plus possibly a draft `decisions.md` and additions to `preferences.md`.

## How to use

1. Open Cowork or Claude.ai
2. Paste the prompt below as the first message
3. Engage with the questions — be candid, push back when the model misreads you
4. At the end, ask the model to output the Compass files
5. Review and save to your Compass

Plan for 30-60 minutes for a meaningful interview. Don't rush — the value comes from depth.

## The prompt

```
I want you to interview me to populate my compass-md. Specifically,
help me draft perspectives/, refine preferences.md, and capture significant
decisions.

Conduct the interview with these principles:

1. Ask one question at a time, not lists of questions
2. Follow up on interesting answers rather than moving to the next topic
3. When I express a view, ask "what would change your mind?" — this surfaces
   the actual conviction level
4. When I express a preference, ask for an example — concrete examples
   distinguish real preferences from aspirational ones
5. When I describe a decision, ask about the alternatives I considered and
   why I rejected them
6. Push back gently when my answers contradict each other or seem
   underspecified
7. Don't accept platitudes — "I value authenticity" is meaningless;
   "I prefer to lead with the bad news rather than burying it" is real
8. Adapt the topics to what I'm actually opinionated about — don't ask
   me about things I clearly don't care about

Start with these warm-up questions to find what I'm opinionated on:

- What's a take you hold that most people you know would disagree with?
- What's something you've changed your mind about in the last year?
- What's a piece of conventional wisdom in your field that you think is wrong?
- What's a recent decision you made where the reasoning wasn't obvious?

Use my answers to identify topics worth deeper exploration. For each
identified topic, drill in until you have enough material to draft a
perspective file.

After 30-45 minutes of conversation (or when I tell you we're done), output:

1. Draft perspective files for each topic that warranted one. Use the
   format from the compass-md convention:
   - # Topic
   - ## My view
   - ## Why I hold it
   - ## Where I differ from common takes
   - ## What would change my mind
   - ## Related perspectives

2. A draft addition to preferences.md if any preferences emerged

3. A draft addition to decisions.md if any significant decisions came up

4. A list of topics we touched on but didn't fully explore — for future
   interview sessions

Begin the interview now.
```

---

## Tips for a productive interview

**Don't overthink the first answer.** Say what comes to mind, refine through follow-ups.

**Push back if the model misreads you.** "No, that's not quite my view — what I actually think is..." is the Compass getting more accurate.

**Stop when you're tired.** Better to have 15 minutes of sharp thinking than 60 minutes of vague answers. The Compass isn't going anywhere; you can interview again next month.

**Re-do this periodically.** Views evolve. An interview every 6 months keeps the Compass current. Compare new answers to old perspective files; the diffs are interesting and worth noting.

**Use voice mode if available.** Talking through your views often surfaces things you'd never type. Cowork's voice mode or Claude.ai's voice mode work well for this.

**Output to a fresh document, not directly to Compass.** Have the model output the drafts in chat, paste into a working doc, then move to Compass after editing. Reduces risk of overwriting carefully crafted existing content.
