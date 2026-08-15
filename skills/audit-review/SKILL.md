---
name: audit-review
description: Inspect the audit log and verify its integrity. Use when the user asks what an agent did, why an action was blocked, whether the log has been tampered with, or wants a record of recent activity.
license: GPL-3.0-or-later
---

# Audit review

Every tool call passes the policy engine and is appended to a hash-chained log.
This skill reads that record.

## Tools

| Task | Call |
|---|---|
| Recent events | `shesh-audit-mcp` → `recent_events` |
| Verify hash chain | `shesh-audit-mcp` → `verify_integrity` |
| Policy tail | `shesh-brain-mcp` → `audit_tail` |
| Current policy | `shesh-brain-mcp` → `get_policy` |

## Procedure

1. For "what happened", read recent events and summarise by actor and outcome.
2. For "why was this blocked", read the policy and find the matching rule.
3. For an integrity question, run `verify_integrity` and report the result
   verbatim.

## Rules

- **A failed integrity check is a security incident.** Report it plainly, do not
  minimise it, and do not attempt to repair the log.
- Never edit, truncate, or rotate the audit log.
- Quote log entries exactly. Do not paraphrase a denial into an approval.
