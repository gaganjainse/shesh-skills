---
name: notes-capture
description: Append to and search the Markdown notes vault. Use when the user wants to write something down, capture an idea, keep a decision, or find an earlier note.
license: GPL-3.0-or-later
---

# Notes

## Tools

| Task | Call |
|---|---|
| Append | `shesh-skills-mcp` → `append_note(name, content)` |
| Full-text search | `shesh-skills-mcp` → `search_notes(query)` |
| Find by filename | `shesh-skills-mcp` → `find_notes(query)` |

## Procedure

1. Search before creating. Appending to the right note beats making a duplicate.
2. Append with a timestamp so the note stays chronological.
3. Report the file written.

## Rules

- Append; never rewrite an existing note to "tidy" it.
- Never write a credential into a note. The vault is synced and backed up.
- Keep the user's own words. Do not paraphrase a captured thought into your own
  phrasing.
