---
name: window-appearance
description: Adjust window opacity, floating state, and fullscreen. Use when the user asks to make a window transparent, float or tile it, or toggle fullscreen.
license: GPL-3.0-or-later
---

# Window appearance

## Tools

| Task | Call |
|---|---|
| Opacity | `shesh-shell-mcp` → `set_opacity(window, value)` |
| Float or tile | `shesh-shell-mcp` → `toggle_floating(window)` |
| Fullscreen | `shesh-shell-mcp` → `fullscreen(window)` |
| Reduce effects on battery | `shesh-shell-mcp` → `set_power_saver_visuals(on)` |

Opacity runs from 0.0 to 1.0.

## Rules

- Do not set opacity below 0.6. Lower values make a window unreadable, and the
  user may not be able to find it again to undo the change.
- Toggling fullscreen on the active window during a screen share changes what
  the audience sees. Confirm first.
- `set_power_saver_visuals` is applied automatically on battery. Do not fight it.
