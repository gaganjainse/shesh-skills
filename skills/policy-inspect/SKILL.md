---
name: policy-inspect
description: Explain what the agent is currently permitted to do and why an action needs confirmation. Use when the user asks about permissions, why something was denied, or wants to review the guard rules.
license: GPL-3.0-or-later
---

# Policy inspection

## Tools

| Task | Call |
|---|---|
| Current policy | `shesh-brain-mcp` → `get_policy` |
| Test a call | `shesh-audit-mcp` → `check(actor, tool, args)` |
| Add a rule | `shesh-audit-mcp` → `add_rule` |

## Verdicts

| Verdict | Meaning |
|---|---|
| `allow` | Runs without prompting; read-only operations |
| `confirm` | Requires the user to agree first; the default for unknown actions |
| `deny` | Refused; protected paths and destructive operations |

Rules are evaluated in order and the first match wins.

## Rules

- Explain a denial by quoting the rule that produced it.
- **Never add or relax a rule to work around a denial.** A denial is a decision,
  not an obstacle. If the user wants it changed, they change it deliberately,
  as its own task, with the consequence stated.
- Never weaken protection on credentials, keys, or employer data.
