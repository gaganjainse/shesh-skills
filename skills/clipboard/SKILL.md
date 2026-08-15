---
name: clipboard
description: Read and replace the clipboard. Use when the user asks what they copied, wants something put on the clipboard, or wants to move text between applications.
license: GPL-3.0-or-later
---

# Clipboard

## Tools

| Task | Call |
|---|---|
| Read | `shesh-desktop-ctl-mcp` → `clipboard_get` |
| Replace | `shesh-desktop-ctl-mcp` → `clipboard_set(text)` |

## Rules

- **The clipboard frequently holds a password.** A user copies a credential from
  a password manager seconds before pasting it. Never echo clipboard contents
  into a log, a note, a commit, a message, or a summary.
- If the content looks like a credential, a token, or a key, say that something
  sensitive is present and stop. Do not quote it.
- `clipboard_set` destroys the previous contents irrecoverably. If the user may
  still need what is there, read it and confirm before replacing.
- An empty clipboard is a normal state, not an error.
