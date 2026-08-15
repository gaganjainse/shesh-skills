---
name: git-inspect
description: Report repository state, recent history, and what has changed. Use when the user asks what changed, wants a commit message, needs a review of their diff, or asks which branch they are on.
license: GPL-3.0-or-later
allowed-tools: Read Grep Glob Bash(git status:*) Bash(git diff:*) Bash(git log:*)
---

# Git inspection

## Tools

| Task | Call |
|---|---|
| Working tree | `shesh-skills-mcp` → `git_status(path)` |
| History | `shesh-skills-mcp` → `git_log(path, n)` |
| Remote metadata | `shesh-skills-mcp` → `github_view(repo)` |

## Procedure

1. Read status before describing state. Never infer from open files.
2. For a commit message, read the actual diff and summarise what changed and why.
3. Flag risk: missing error handling, hardcoded values, secrets, absent tests.

## Rules

- This skill is read-only. It never commits, pushes, or rewrites history.
- **If a diff contains something that looks like a credential, stop and say so
  before anything is committed.**
- Do not describe a change as safe without reading it.
