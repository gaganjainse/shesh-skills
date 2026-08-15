---
name: messaging-send
description: Send and read messages through connected bridges. Use when the user asks to message someone, check messages, or when a long task should report its result to a phone.
license: GPL-3.0-or-later
---

# Messaging

## Tools

| Task | Call |
|---|---|
| List bridges | `shesh-messaging-mcp` → `list_bridges` |
| Send | `shesh-messaging-mcp` → `send_telegram`, `send_signal` |
| Read | `shesh-messaging-mcp` → `read_telegram` |
| Bridge state | `shesh-messaging-mcp` → `telegram_status` |
| Enable or disable | `shesh-messaging-mcp` → `enable_bridge`, `disable_bridge` |

## Rules

- **Sending a message leaves the machine and cannot be recalled.** Always show
  the exact recipient and the exact text, and get confirmation, before sending.
- Never send to a recipient inferred from context. Ask which one.
- Never include a credential, a token, or the contents of a protected file in a
  message.
- Never send automatically on task completion unless the user set that up in
  this session.
- When reading, summarise. Do not repeat message contents into a shared or
  recorded context without being asked.
