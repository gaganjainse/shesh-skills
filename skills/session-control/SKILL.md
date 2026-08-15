---
name: session-control
description: Lock, suspend, hibernate, log out, reboot, or power off. Use when the user is stepping away, finishing for the day, or asks to restart or shut down the machine.
license: GPL-3.0-or-later
---

# Session control

## Tools

| Task | Call |
|---|---|
| Any action | `shesh-desktop-ctl-mcp` → `session_action(action, confirm)` |
| What blocks sleep | `shesh-desktop-ctl-mcp` → `idle_inhibit_status` |

Actions: `lock`, `suspend`, `hibernate`, `logout`, `reboot`, `poweroff`.

## Confirmation

`lock` runs immediately; it is reversible and loses nothing.

Every other action ends the session or the machine and requires `confirm=True`.
The tool refuses without it. **Do not pass `confirm=True` on the user's behalf
because the request sounded decisive.** Ask, then pass it.

## Procedure

1. Before suspend, reboot, or power off, check `idle_inhibit_status`. A running
   backup, download, build, or recording will be interrupted.
2. Name what will be lost, then ask.
3. Act only on an explicit yes.

## Rules

- Never reboot to "fix" something without being asked.
- A GPU mode change needs a reboot, but the reboot is still the user's decision.
- If a backup or recording is running, say so and recommend waiting.
