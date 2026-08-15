---
name: desktop-automation
description: Read the screen and drive the desktop: accessibility tree, window targeting, screenshots, clicking, and typing. Use when a task needs a graphical application that has no command-line equivalent, or when the user asks to click, type into, or read something on screen.
license: GPL-3.0-or-later
---

# Desktop automation

Provided by computer-use-linux, adopted under ADR-0020 and proxied through the
policy guard. Never configure the upstream server directly in a client: that
bypasses the guard.

## Tools

| Task | Call |
|---|---|
| Check readiness | `shesh-desktop-ctl-mcp` → `automation_doctor` |
| Any operation | `shesh-desktop-ctl-mcp` → `automation_call(tool, arguments, confirm)` |

## Reading, no confirmation

`doctor`, `apps`, `state`, `screenshot`, `windows`, `list_windows`,
`focused_window`, `accessibility_tree`.

## Acting, confirmation required

`click`, `double_click`, `right_click`, `drag`, `scroll`, `type_text`,
`press_key`, `activate_window`, `move_window`, `resize_window`,
`close_window`, `invoke_action`.

## Procedure

1. Run `automation_doctor` first. Most failures are the accessibility bus
   being disabled, which is a setup problem, not a bad instruction.
2. Read the accessibility tree before acting. Never click a coordinate derived
   from a screenshot alone; the window may have moved.
3. Name the exact element and the exact action, then ask.
4. Act only after the user confirms, then verify by reading the tree again.

## Rules

- **An agent that can click and type can do anything the operator can.** There
  is no undo. Every acting call requires `confirm=True`, and the tool refuses
  without it. Do not supply that flag on the user's behalf because the request
  sounded decisive.
- Never type into a field you have not identified. A password manager, a
  terminal with a root shell, and a chat box all accept keystrokes.
- Never click through a dialogue you cannot read. If the tree is unavailable,
  stop and say so.
- Screenshots may contain credentials and private messages. Say where the file
  was written; do not send it anywhere.
- Prefer a command-line equivalent when one exists. Driving a graphical
  application is the least reliable way to accomplish anything.
