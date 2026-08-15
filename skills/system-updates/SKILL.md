---
name: system-updates
description: Check for and report pending system package updates. Use when the user asks whether updates are available, what changed, or whether it is safe to update.
license: GPL-3.0-or-later
---

# System updates

## Tools

| Task | Call |
|---|---|
| Pending updates | `shesh-system-mcp` → `check_system_updates` |
| Disk headroom | `shesh-system-mcp` → `system_health` |

## Procedure

1. Report the count and name the significant packages: kernel, graphics driver,
   compositor, libc.
2. Flag anything that requires a reboot or a session restart.
3. Confirm there is enough free space.

## Rules

- **This skill never applies updates.** It reports. The user runs the update
  themselves. This is deliberate: the distribution is a rolling release, and an
  unattended update can leave the machine without a working desktop or driver.
- Recommend a backup before a kernel or graphics driver update.
- Never update while a backup, recording, or long build is running.
