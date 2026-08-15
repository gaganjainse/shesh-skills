---
name: backup-run
description: Run, inspect, and prune backups. Use when the user asks to back up, check whether backups are current, free space in the backup repository, or verify that a restore would work.
license: GPL-3.0-or-later
---

# Backup

## Tools

| Task | Call |
|---|---|
| Configure | `shesh-backup-mcp` → `configure` |
| Status and snapshots | `shesh-backup-mcp` → `status` |
| Run a backup | `shesh-backup-mcp` → `run_backup` |
| Remove old snapshots | `shesh-backup-mcp` → `run_prune` |

## Procedure

1. Read `status` first. Report the most recent snapshot and its age.
2. Run the backup and report what it captured.
3. Prune only when asked, and state exactly which snapshots the policy removes.

## Rules

- **Pruning deletes history and cannot be undone.** Always list what will be
  removed and require explicit confirmation. Never prune as part of a backup.
- An untested backup is not a backup. If no restore has ever been verified,
  say so.
- Never print the repository password. If a credential is missing, report the
  missing name only.
- A backup during heavy disk activity will be slow. Report, do not refuse.
