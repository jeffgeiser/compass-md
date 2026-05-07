# Alex's Compass

This is a populated example Compass for Alex Chen — founder and CEO of Foundry, a B2B SaaS company in infrastructure observability. It's constructed to be realistic, not to be prescriptive. Use it to understand what a working Compass looks like after a few months of use.

---

## How this Compass was built

Alex bootstrapped the initial Compass using the full Drive scan (`bootstrap/full-drive-scan.md`), which produced first drafts of `self/facts.md`, `self/voice.md`, `self/preferences.md`, and an early version of `self/decisions.md` from Foundry's project docs and Alex's sent emails.

The Drive scan took about an hour total. Voice and preferences needed the most editing — the scan caught the right patterns but wasn't always precise about which contexts they applied to. Facts were mostly accurate out of the box.

The three perspective files (`competitive-strategy.md`, `hiring.md`, `pricing.md`) came from a follow-up interview session using `bootstrap/interview-perspectives.md`. That took about 45 minutes and produced sharper takes than anything inferrable from Drive content.

After that initial bootstrap, the Compass has evolved through regular use — two pending refinements are in `refinements/pending/`, and the accepted refinements folder shows what's already been incorporated.

---

## What to look at

**If you want to understand voice files:** Start with `self/voice.md`. Notice that the useful sections are specific — particular words avoided, concrete before/after examples — not just vague descriptions of tone.

**If you want to understand perspective files:** Read `self/perspectives/pricing.md` and then `self/decisions.md`. Alex's pricing perspective directly connects to the anti-freemium decision; the two should be consistent with each other.

**If you want to understand the refinement format:** Read the files in `refinements/pending/`. One is high confidence (clear repeated pattern), one is medium (single instance). The difference in confidence level shows up in the proposed change's scope.

**If you want to understand how the log works:** Check `log.md`. The entries show the actual history — when files were created, when refinements were proposed and accepted, when direct edits were made.

---

## Daily use with a Compass like this

For the daily/weekly/monthly rhythm of using a Compass, see [`GETTING_STARTED.md`](../../GETTING_STARTED.md) at the repo root. That document covers:

- How to test that your AI tool is actually reading the Compass
- The weekly refinement review (the most important habit)
- Monthly maintenance to keep the Compass healthy
- Common failure modes and how to diagnose them

This example Compass represents roughly 3-4 months of regular use. That's enough time to have real refinement history, multiple perspective files, and enough decisions captured to see patterns.

---

## A note on what this example omits

Alex's Compass doesn't have an `INDEX.md` — at this file count it isn't necessary. It also doesn't have a `team/` module, since Alex uses a separate team Compass for Foundry's sales team (the team example is at `examples/team-proposal-review-example/`).

The perspective files cover three topics. Alex might have views on many more topics that aren't captured here — the Compass doesn't need to be comprehensive, just accurate for what's in it.
