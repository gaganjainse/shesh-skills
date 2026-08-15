---
name: file-organizer
description: Sort files into folders by type, date, or project. Use when the user asks to tidy Downloads, organise a folder, clean up the desktop, or file documents.
license: GPL-3.0-or-later
---

# File organizer

## Scope

The organizer works on `~/Downloads`, `~/Desktop`, `~/Documents`, and
`~/Pictures`. It must never touch protected locations. The policy engine denies
those paths, and an attempt is recorded as a violation.

Protected: `~/.ssh`, `~/.gnupg`, vaults, and any employer or client directory.

## Procedure

1. List the target directory and group the files before moving anything.
2. Present the plan: how many files, into which folders.
3. Move only after the user agrees.
4. Report what moved, and where the undo record is.

## Rules

- Never move a file that is currently open or being written.
- Never overwrite. On a name collision, suffix the new file.
- Never delete as part of organising. Sorting and deleting are separate actions.
- Preserve modification times.
