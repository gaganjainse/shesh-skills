---
name: web-research
description: Research a topic from primary sources and report with citations. Use when asked to investigate, compare options, check current documentation, or verify a claim.
license: GPL-3.0-or-later
---

# Web research

## Tools

| Task | Call |
|---|---|
| Search | `shesh-skills-mcp` → `web_search(query)` |
| Fetch a page | `shesh-skills-mcp` → `fetch_url(url)` |

## Procedure

1. Search, then read the primary source. Do not report from a search snippet.
2. Prefer official documentation, specifications, and source repositories over
   blog summaries.
3. Note the publication date. For fast-moving tooling, a two-year-old page is
   probably wrong.
4. Report findings with a link for each claim.

## Rules

- **Every factual claim carries a source link.** A claim you cannot source is
  stated as your inference, labelled as such.
- When sources disagree, say so and give both.
- Never present a model recollection as a search result.
- If search returns nothing useful, report that. Do not fill the gap from memory.
