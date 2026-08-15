---
name: model-routing
description: Choose which model handles a task and inspect what is installed. Use when a response is poor, a task needs a stronger or faster model, or the user asks which model is running.
license: GPL-3.0-or-later
---

# Model routing

Callers name a role, never a model. The router maps roles to whatever is
available, preferring local inference.

## Tools

| Task | Call |
|---|---|
| Select for a task | `shesh-mind-mcp` → `select_model` |
| List roles | `shesh-mind-mcp` → `list_roles` |
| Bind a role | `shesh-mind-mcp` → `set_model_for_role` |
| Installed models | `shesh-mind-mcp` → `list_installed_models` |
| Plan a session | `shesh-mind-mcp` → `plan_session` |

## Roles

| Role | Used for |
|---|---|
| `planner` | Decomposing a goal into steps |
| `coder` | Writing and editing code |
| `researcher` | Search and summarising sources |
| `vision` | Screenshots and image understanding |
| `critic` | Reviewing output before it is accepted |

## Rules

- Video memory is limited; one model is resident at a time. Switching evicts the
  current model and costs several seconds. Do not switch mid-task.
- Never claim a larger model is in use when routing fell back to a smaller one.
- If every route fails, say so. Never fabricate an answer to hide the failure.
