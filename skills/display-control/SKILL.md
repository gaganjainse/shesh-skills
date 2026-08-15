---
name: display-control
description: Inspect and change monitor resolution, refresh rate, scaling, and arrangement. Use when the user mentions a second screen, a projector, text being too small or too large, the wrong refresh rate, or a display that is not working.
license: GPL-3.0-or-later
---

# Display control

## Tools

| Task | Call |
|---|---|
| List monitors and modes | `shesh-desktop-ctl-mcp` → `list_monitors` |
| Resolution and refresh | `shesh-desktop-ctl-mcp` → `set_monitor_mode(name, width, height, refresh, confirm)` |
| Fractional scaling | `shesh-desktop-ctl-mcp` → `set_monitor_scale(name, scale, confirm)` |
| Enable or disable | `shesh-desktop-ctl-mcp` → `set_monitor_enabled(name, on, confirm)` |

## Procedure

1. List monitors first. Never assume a name: `eDP-1` is the internal panel on
   most laptops, but external outputs vary by machine.
2. Quote the current mode and the mode you propose, then ask.
3. Apply, then confirm the result by listing again.

## Rules

- **A wrong mode can leave the screen unreadable, and the user may not be able
  to see well enough to undo it.** Every change requires `confirm=True`, and
  the tool returns the previous value so it can be restored. Do not supply the
  flag on the user's behalf.
- Only modes the monitor advertises are accepted. If the requested mode is
  refused, report the available list rather than trying a near match.
- Scaling is bounded between 0.5 and 3.0. Below about 0.8 most interfaces
  become unreadable; say so before applying.
- Disabling the only active output is refused outright, not confirmed.
- Changing the mode during a screen recording or a call disrupts what the
  audience sees. Check before acting.
