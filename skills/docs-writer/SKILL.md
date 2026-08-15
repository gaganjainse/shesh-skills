---
name: docs-writer
description: Write or revise documentation in the house style. Use when asked to create, rewrite, or review a README, guide, reference page, or architecture decision record.
license: GPL-3.0-or-later
allowed-tools: Read Grep Glob Edit Write
---

# Documentation

## Structure

Every page is exactly one Diátaxis type. Do not mix them; link instead.

| Type | Answers | Must not contain |
|---|---|---|
| Tutorial | "Teach me by doing" | Options, rationale |
| How-to | "Help me do X" | Teaching, theory |
| Reference | "Tell me the exact fact" | Steps, opinion |
| Explanation | "Help me understand why" | Instructions |

## Voice

- Second person, present tense, active voice.
- Sentence case headings. No emoji.
- No first person: no "we", "our", "I".
- No self-assessment: not "clean", "robust", "foolproof".
- No filler: not "simply", "just", "obviously".

## Facts

- **No volatile counts.** Test counts, component counts, and provider counts are
  wrong shortly after writing. Generate the page or give the command instead.
- Document committed behaviour only. Unbuilt work goes on a roadmap, dated.
- Never state that a component does something without checking that it does.
- One fact lives in exactly one place; everything else links to it.
