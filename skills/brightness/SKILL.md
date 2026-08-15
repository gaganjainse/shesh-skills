---
name: brightness
description: Read and set screen brightness. Use when the user says the screen is too dark or too bright, wants to save battery, or is moving between indoors and sunlight.
license: GPL-3.0-or-later
---

# Brightness

## Tools

| Task | Call |
|---|---|
| Read | `shesh-desktop-ctl-mcp` → `brightness_get` |
| Set | `shesh-desktop-ctl-mcp` → `brightness_set(percent)` |

## Procedure

1. For a relative change ("dimmer"), read the current value first, then set.
2. Move in steps of 10 to 20 unless the user names a level.
3. Confirm the resulting percentage.

## Rules

- The floor is 1 percent, enforced by the tool. Zero blanks the panel and the
  user may not be able to see well enough to undo it.
- Brightness is the largest single battery draw on a laptop. When the user asks
  to save power, offer this before anything else.
- Do not change brightness during a screen recording or a presentation without
  asking; it is visible to the audience.
