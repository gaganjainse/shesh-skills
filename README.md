> **Consolidated into [shesh-core](https://github.com/gaganjainse/shesh-core)** — the MCP server and tools in this repository now live in the shesh-core monorepo under the same package name and console script. Archived 2026-08-13. The `skills/` library remains canonical here.

# shesh-skills

Agent Skills library and everyday tool server for Shesh.

- **Licence:** GPL-3.0-or-later
- **Layer:** Mind (workflows) and Soma (actuators)
- **Part of:** [shesh-ecosystem](https://github.com/gaganjainse/shesh-ecosystem)

## Skills

Six skills following the [Agent Skills specification](https://agentskills.io),
so they load unmodified in Claude Code, Codex, and other compliant agents.

```text
skills/
├── autopilot/SKILL.md
├── coding/SKILL.md
├── daily-briefing/SKILL.md
├── docs-writer/SKILL.md
├── safety-governance/SKILL.md
└── web-research/SKILL.md
```

| Skill | Purpose | Pre-approved tools |
|---|---|---|
| `coding` | Implement, refactor, and review code | Read, edit, git, test runners |
| `web-research` | Research from primary sources with citations | Read, search, fetch |
| `docs-writer` | Write documentation in the house style | Read, edit |
| `safety-governance` | Govern destructive actions; always active | Read only |
| `daily-briefing` | Morning and evening digest | Read, git log |
| `autopilot` | Safe unattended progress on the backlog | Read, edit, git, gates |

`safety-governance` is deliberately granted read-only tools: the layer that
governs destructive actions must not be able to take them. A test enforces this.

### Using them elsewhere

Skills are plain files with no Shesh-specific dependency. Copy a directory into
any compliant agent's skill path:

```bash
cp -r skills/coding ~/.claude/skills/
```

### Loading

Skills follow progressive disclosure: listing costs only the name and
description, and the body is read when a skill is selected.

```python
from shesh_skills import skills

for s in skills.discover():
    print(s.name, "-", s.description)

body = skills.get("coding").body()
```

Resolution order, first match winning, so a user-installed skill overrides a
shipped one:

1. `$SHESH_SKILLS_DIR`
2. `$XDG_DATA_HOME/shesh/skills`
3. The directory shipped with this package

A malformed skill is skipped rather than raising, so one bad directory cannot
make the rest unavailable.

## Tools

The stdio MCP server exposes the skill library plus everyday tools.

| Tool | Purpose |
|---|---|
| `list_skills` / `get_skill` | Skill discovery and loading |
| `append_note` / `find_notes` / `search_notes` | Markdown notes vault |
| `web_search` / `fetch_url` | Search and retrieval, no API key |
| `git_status` / `git_log` / `github_view` | Repository inspection |
| `convert_to_markdown` | Document conversion through pandoc |
| `remind` | Desktop notification scheduler |

Every call passes through the audit guard, which returns allow, confirm, or deny
and records the decision.

## Develop

```bash
uv sync --extra dev
uv run pytest -q
uv run ruff check .
uv run shesh-skills-mcp
```

`tests/test_skills_spec.py` validates every skill against the specification:
directory layout, front-matter fields and limits, name and directory agreement,
body length, loader behaviour, and the read-only constraint on the safety skill.

## Design

- **Local-first.** Search and retrieval use endpoints that need no API key.
- **Text only.** No code ships with a skill, so a poor skill can degrade style
  but cannot act.
- **Least privilege.** `allowed-tools` is scoped to what each skill needs.

## Security

Vulnerability reporting and the security posture are documented in the
[ecosystem security policy](https://github.com/gaganjainse/shesh-ecosystem/blob/main/SECURITY.md).

## Licence

GPL-3.0-or-later — see [LICENSE](LICENSE).
