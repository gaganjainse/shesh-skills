---
name: screenshot-capture
description: Take a screenshot of the screen, a window, or a region. Use when the user asks for a screenshot, a screen capture, or wants an image of what is on screen to share or annotate.
license: GPL-3.0-or-later
---

# Screenshot capture

## Tools

| Task | Call |
|---|---|
| Capture | `shesh-media-mcp` → `screenshot` or `take_screenshot` |
| Identify the active window first | `shesh-shell-mcp` → `get_active_window` |

## Procedure

1. Establish scope: whole screen, one window, or a region.
2. For a window capture, resolve the window with `get_active_window` or
   `list_workspaces` rather than guessing.
3. Capture and report the saved path.

## Rules

- A screenshot may contain passwords, tokens, private messages, or client data.
  Say where the file was written so the user can decide before sharing.
- Never upload or send a screenshot as a side effect. Sending is a separate,
  confirmed action.
