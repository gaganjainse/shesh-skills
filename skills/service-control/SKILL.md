---
name: service-control
description: Inspect and restart systemd units. Use when a background service is misbehaving, something is not starting, or the user asks what is failing.
license: GPL-3.0-or-later
---

# Service control

## Tools

| Task | Call |
|---|---|
| One unit | `shesh-desktop-ctl-mcp` → `service_status(unit, user)` |
| Failed units | `shesh-desktop-ctl-mcp` → `service_list_failed(user)` |
| Restart | `shesh-desktop-ctl-mcp` → `service_restart(unit, user, confirm)` |

User units are the default. Pass `user=False` for system units.

## Procedure

1. Start with `service_list_failed` for both scopes. It usually finds the fault
   immediately.
2. Read a unit's status before acting on it.
3. Restart only after confirming, and report the state afterwards.

## Rules

- **A restart interrupts whatever the unit is doing.** The tool requires
  `confirm=True`; obtain that from the user, do not supply it yourself.
- Never restart the audio server, the compositor, or the display manager without
  warning that the session may visibly disrupt.
- Never restart a unit mid-backup.
- Restarting is not a diagnosis. Read the failure before recommending it.
