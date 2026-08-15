---
name: secrets-handling
description: Store and retrieve credentials without exposing them. Use when a task needs an API key, token, or password, or when the user asks where a credential is kept.
license: GPL-3.0-or-later
---

# Secrets handling

## Reference form

Credentials are referenced, never written inline:

| Form | Source |
|---|---|
| `env:NAME` | Environment variable |
| `gopass:path/to/secret` | Password store |
| `keepassxc:entry` | KeePassXC database |

Resolution happens through `shesh-secrets-mcp` at call time.

## Rules

- **Never print a secret value.** Not in a reply, a log, a commit, an error
  message, or a comment. Report the reference name and whether it resolved.
- Never write a credential into a configuration file, a script, or a
  conversation.
- A credential that has appeared in plain text is compromised. Say so and
  recommend rotation. Do not continue using it quietly.
- Refuse to move a credential into a file the organizer or a backup would copy.
- If a secret is missing, name the reference that failed. Do not guess a value
  or fall back to an unauthenticated path without saying so.
