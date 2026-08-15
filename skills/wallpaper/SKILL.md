---
name: wallpaper
description: Set the desktop wallpaper. Use when the user asks to change the background, set a wallpaper, or restore the default desktop image.
license: GPL-3.0-or-later
---

# Wallpaper

## Tools

| Task | Call |
|---|---|
| Set wallpaper | `shesh-media-mcp` → `set_wallpaper(path)` |

## Procedure

1. Confirm the file exists and is an image.
2. Set it and confirm.

## Rules

- The desktop derives its accent colours from the wallpaper. A change may
  restyle the whole shell. Mention this the first time.
- Prefer a resolution at or above the display's native resolution.
