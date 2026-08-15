---
name: notifications
description: Send a desktop notification. Use when a long task finishes, something needs attention, or the user asks to be reminded on screen.
license: GPL-3.0-or-later
---

# Notifications

## Tools

| Task | Call |
|---|---|
| Send | `shesh-desktop-ctl-mcp` → `notify(summary, body, urgency)` |

Urgency: `low`, `normal`, `critical`.

## Rules

- A notification is visible to anyone near the screen and appears in a screen
  recording. Never put a credential, a token, or private content in one.
- Reserve `critical` for something that needs action now. A critical
  notification may bypass do-not-disturb; overusing it trains the user to ignore
  it.
- Keep the summary under about 40 characters; longer text is truncated by the
  shell.
- One notification per event. Do not send progress updates unless asked.
