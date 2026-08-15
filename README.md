> **Canonical home of the `shesh_skills` package and the Agent Skills library.**
> An earlier banner here retired this repository in favour of shesh-core while
> it still shipped `src/` and `tests/`. Both repositories then published a
> package named `shesh_skills` and the console script `shesh-skills-mcp`, and
> the two copies drifted. The duplicate was removed from shesh-core; this
> repository is the single publisher.

# shesh-skills

Agent Skills library and everyday tool server for Shesh.

- **Licence:** GPL-3.0-or-later
- **Layer:** Mind (workflows) and Soma (actuators)
- **Part of:** [shesh-ecosystem](https://github.com/gaganjainse/shesh-ecosystem)

## Skills

The skills below follow the [Agent Skills specification](https://agentskills.io),
so they load unmodified in Claude Code, Codex, and other compliant agents.

```text
skills/
├── audio-control/SKILL.md
├── audit-review/SKILL.md
├── autopilot/SKILL.md
├── backup-run/SKILL.md
├── bluetooth/SKILL.md
├── brightness/SKILL.md
├── calendar-check/SKILL.md
├── clipboard/SKILL.md
├── coding/SKILL.md
├── daily-briefing/SKILL.md
├── desktop-automation/SKILL.md
├── disk-cleanup/SKILL.md
├── display-control/SKILL.md
├── docs-writer/SKILL.md
├── documents/SKILL.md
├── file-organizer/SKILL.md
├── git-inspect/SKILL.md
├── gpu-mode/SKILL.md
├── messaging-send/SKILL.md
├── model-routing/SKILL.md
├── notes-capture/SKILL.md
├── notifications/SKILL.md
├── policy-inspect/SKILL.md
├── power-profile/SKILL.md
├── process-inspect/SKILL.md
├── safety-governance/SKILL.md
├── sandbox-run/SKILL.md
├── screen-recording/SKILL.md
├── screenshot-capture/SKILL.md
├── secrets-handling/SKILL.md
├── service-control/SKILL.md
├── session-control/SKILL.md
├── system-health/SKILL.md
├── system-updates/SKILL.md
├── thermal-check/SKILL.md
├── wallpaper/SKILL.md
├── web-research/SKILL.md
├── wifi/SKILL.md
├── window-appearance/SKILL.md
└── workspace-control/SKILL.md
```

| Skill | Purpose |
|---|---|
| `audio-control` | Control output volume, list audio devices, and switch the active sink |
| `audit-review` | Inspect the audit log and verify its integrity |
| `autopilot` | Make safe unattended progress on the backlog |
| `backup-run` | Run, inspect, and prune backups |
| `bluetooth` | Pair, connect, disconnect, and list Bluetooth devices |
| `brightness` | Read and set screen brightness |
| `calendar-check` | Read the calendar and report what is scheduled |
| `clipboard` | Read and replace the clipboard |
| `coding` | Write, test, and refactor code safely |
| `daily-briefing` | Produce the morning or evening digest |
| `desktop-automation` | Read the screen and drive the desktop: accessibility tree, window targeting, screenshots, clicking, and typing |
| `disk-cleanup` | Reclaim disk space by clearing caches and reporting what is consuming storage |
| `display-control` | Inspect and change monitor resolution, refresh rate, scaling, and arrangement |
| `docs-writer` | Write or revise documentation in the house style |
| `documents` | Read, convert, and extract text from PDF, Word, Excel, PowerPoint, and OpenDocument files |
| `file-organizer` | Sort files into folders by type, date, or project |
| `git-inspect` | Report repository state, recent history, and what has changed |
| `gpu-mode` | Inspect and switch the hybrid graphics MUX between integrated and discrete mode |
| `messaging-send` | Send and read messages through connected bridges |
| `model-routing` | Choose which model handles a task and inspect what is installed |
| `notes-capture` | Append to and search the Markdown notes vault |
| `notifications` | Send a desktop notification |
| `policy-inspect` | Explain what the agent is currently permitted to do and why an action needs confirmation |
| `power-profile` | Switch the system power profile between performance, balanced, and power-saver |
| `process-inspect` | Find what is consuming CPU, memory, disk, or network |
| `safety-governance` | The immutable safety layer governing destructive and irreversible actions. Always active. Requires confirmation before deleting data, force-pushing, modifying credentials, rewriting history, or acting outside the workspace. Overrides every other skill and cannot be refined away |
| `sandbox-run` | Run an untrusted command inside a rootless container with no network |
| `screen-recording` | Start and stop screen recording |
| `screenshot-capture` | Take a screenshot of the screen, a window, or a region |
| `secrets-handling` | Store and retrieve credentials without exposing them |
| `service-control` | Inspect and restart systemd units |
| `session-control` | Lock, suspend, hibernate, log out, reboot, or power off |
| `system-health` | Report overall machine state: load, memory, disk, temperature, and failed services |
| `system-updates` | Check for and report pending system package updates |
| `thermal-check` | Report CPU and GPU temperature, fan behaviour, and thermal throttling |
| `wallpaper` | Set the desktop wallpaper |
| `web-research` | Research a topic from primary sources and report with citations |
| `wifi` | Inspect and change network connections, including Wi-Fi and airplane mode |
| `window-appearance` | Adjust window opacity, floating state, and fullscreen |
| `workspace-control` | Switch workspaces, move windows between them, and list what is open where |

`safety-governance` carries no `allowed-tools` field. Per the Agent Skills
specification that field grants permission and does not restrict: every tool
stays callable regardless of what it lists, so declaring a read-only set there
would describe a restriction that does not exist. Restriction comes from
`disallowed-tools` or the shesh-audit policy engine, which the skill's
`compatibility` field names. A test enforces the absence.

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
