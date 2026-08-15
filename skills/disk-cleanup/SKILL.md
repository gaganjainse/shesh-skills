---
name: disk-cleanup
description: Reclaim disk space by clearing caches and reporting what is consuming storage. Use when the disk is full, a build fails for space, or the user asks what is taking up room.
license: GPL-3.0-or-later
---

# Disk cleanup

## Tools

| Task | Call |
|---|---|
| Disk usage and health | `shesh-system-mcp` → `system_health` |
| Clear caches | `shesh-system-mcp` → `clean_system_caches(scope)` |

Scope is `user` or `system`.

## Procedure

1. Report current free space and the largest consumers first.
2. Propose what to clear and how much it will reclaim.
3. Clear only after agreement, starting with `user` scope.
4. Report space reclaimed.

## Rules

- Never clear a package cache while an update is running.
- Never remove anything from a project directory as "cache" without asking;
  build outputs may be expensive to regenerate.
- Model files are large but slow to re-download. Never remove them implicitly.
- Report a measured figure, not an estimate.
