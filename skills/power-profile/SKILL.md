---
name: power-profile
description: Switch the system power profile between performance, balanced, and power-saver. Use when the user asks to save battery, speed the machine up, quieten the fans, or prepare for gaming, compiling, or travel.
license: GPL-3.0-or-later
---

# Power profile

Read the current profile before changing it, and report the change.

## Tools

| Task | Call |
|---|---|
| Read current profile | `shesh-system-mcp` → `get_power_profile` |
| Change profile | `shesh-system-mcp` → `set_power_profile(profile)` |

Accepted values: `performance`, `balanced`, `power-saver`.

## Choosing a profile

| Situation | Profile |
|---|---|
| Compiling, gaming, video export | `performance` |
| Normal interactive work | `balanced` |
| On battery, travelling, presenting | `power-saver` |

## Rules

- State the previous and new profile in the reply.
- `performance` on battery drains quickly. Say so once; do not refuse.
- The desktop reduces blur and shadows on battery automatically. Do not also
  change the theme unless asked.
