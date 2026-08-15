---
name: daily-briefing
description: Produce the morning or evening digest. Use when asked for a daily summary, a standup note, or an end-of-day report.
license: GPL-3.0-or-later
allowed-tools: Read Grep Bash(git log:*)
---

# Daily briefing

## Gather

| Source | Call |
|---|---|
| Schedule | `shesh-calendar-mcp` → `upcoming_events` |
| Machine state | `shesh-system-mcp` → `system_health` |
| Backup age | `shesh-backup-mcp` → `status` |
| Repository activity | `shesh-skills-mcp` → `git_log` |
| Pending updates | `shesh-system-mcp` → `check_system_updates` |

## Format

Lead with anything that needs a decision today. Then:

1. **Schedule** — next event and the gap before it.
2. **Needs attention** — failed backup, low disk, failed service. Omit if clear.
3. **Yesterday** — what actually landed, from the log rather than intention.
4. **Today** — the open items, in priority order.

## Rules

- Under 200 words. A briefing nobody reads is worthless.
- Omit empty sections rather than writing "nothing to report".
- State facts from tools. Never invent progress.
- Do not repeat sensitive event titles if the briefing is being read aloud.
