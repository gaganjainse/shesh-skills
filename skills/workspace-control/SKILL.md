---
name: workspace-control
description: Switch workspaces, move windows between them, and list what is open where. Use when the user asks to change workspace, move a window, tidy their desktop layout, or find where an application is.
license: GPL-3.0-or-later
---

# Workspace control

## Tools

| Task | Call |
|---|---|
| List workspaces and windows | `shesh-shell-mcp` → `list_workspaces` |
| Switch workspace | `shesh-shell-mcp` → `switch_workspace(n)` |
| Move a window | `shesh-shell-mcp` → `move_window_to_workspace(window, n)` |
| Focus a window | `shesh-shell-mcp` → `focus_window(window)` |
| Active window | `shesh-shell-mcp` → `get_active_window` |

## Procedure

1. List workspaces before moving anything. Never assume a layout.
2. Match windows by title or class, not by index.
3. Report what moved and where.

## Rules

- Moving a fullscreen window can disrupt a presentation or a call. Check
  `get_active_window` first.
- If the target workspace does not exist, say so rather than creating one
  silently.
