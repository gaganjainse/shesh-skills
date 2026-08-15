# Capability gaps

The skill library covers what `shesh-core` actually exposes. This file records
what it does not, so nobody writes a skill whose instructions cannot execute.

A skill is only useful if the tool it names exists. Writing "control Bluetooth"
against a server with no Bluetooth tool produces a skill that fails at the first
call, which is worse than having no skill: the agent believes it can do the job.

## What exists today

Sixty Model Context Protocol tools across twelve packages in `shesh-core`,
covering power and thermal, GPU mode, audio, screenshots, recording, wallpaper,
windows and workspaces, files, disk, backup, updates, observability, audit,
policy, secrets, containers, model routing, calendar, messaging, and notes.

Twenty-nine skills are built on those tools.

## What is missing

Each entry needs a tool before a skill can be written. Ordered by how often a
desktop user would reach for it.

### Closed on 2026-08-15

Implemented in `shesh_desktop_ctl` (19 tools, 46 tests) with skills to match.

| Capability | Skill | Tools |
|---|---|---|
| Bluetooth | `bluetooth` | status, power, devices, connect, disconnect |
| Wi-Fi and networking | `wifi` | status, list, connect, airplane mode |
| Brightness | `brightness` | get, set (floored at 1%) |
| Clipboard | `clipboard` | get, set |
| Session control | `session-control` | lock, suspend, hibernate, logout, reboot, poweroff |
| Service management | `service-control` | status, list failed, restart |
| Notifications | `notifications` | send |

Destructive actions require an explicit `confirm=True`; the tool refuses
without it.

### Still open, high value

| Capability | Needs | Backing interface |
|---|---|---|
| Display and monitors | Resolution, refresh rate, scaling, arrangement, rotation | `hyprctl` monitors, `wlr-randr` |
| Clipboard history | Recall past entries | `cliphist` |
| VPN | Connect, disconnect, status | NetworkManager |
| Do-not-disturb | Query and set | The shell's notification daemon |

### Moderate value

| Capability | Needs | Backing interface |
|---|---|---|
| Input devices | Keyboard layout, repeat rate, touchpad gestures | `hyprctl`, `libinput` |
| Printing | Queue, print, cancel | CUPS |
| Firewall | Rules, zones, port state | `firewalld`, `nftables` |
| Package management | Install, remove, search, orphans | `pacman`, an AUR helper |
| Locale and time | Timezone, locale, NTP sync | `systemd-timedated`, `localectl` |
| Fonts | List, install, rebuild the cache | `fontconfig` |
| Theming | Colour scheme, cursor, icons, dark mode | The shell's configuration |
| Archives | Create and extract | `tar`, `zip`, `7z` |
| Search | Content and filename search across the machine | `ripgrep`, `fd`, `plocate` |
| Browser control | Tabs, navigation, extraction | A browser automation MCP server |

### Specialised

| Capability | Needs | Backing interface |
|---|---|---|
| Phone control | Tap, screenshot, notifications, files | `shesh-phone` (exists; skills not yet written) |
| Virtual machines | Lifecycle, snapshots | `libvirt` |
| Databases | Query, dump, restore | Per-engine clients |
| Photo and video editing | Crop, convert, compress | `ffmpeg`, ImageMagick |
| OCR | Text from an image or screenshot | `tesseract` |
| PDF | Merge, split, extract, fill | `qpdf`, `pdftk` |
| Document conversion | Between office formats | `pandoc` (partially present) |

## Recommended sources rather than reimplementation

Several gaps are better closed by adopting a maintained server than by writing
one.

| Gap | Candidate | Licence |
|---|---|---|
| Desktop control, accessibility tree, input | [computer-use-linux](https://github.com/agent-sh/computer-use-linux) | MIT |
| Windows, clipboard, audio, OCR, notifications | [mcp-linux-desktop](https://glama.ai/mcp/servers/wizardofweb125-lab/mcp-linux-desktop) | Check before adopting |
| Compositor control | [hyprmcp](https://github.com/stefanoamorelli/hyprmcp) | Check before adopting |
| Document handling | [anthropics/skills](https://github.com/anthropics/skills) — `pdf`, `docx`, `xlsx`, `pptx` | Check before adopting |

Adoption follows [ADR-0018](https://github.com/gaganjainse/shesh-docs/blob/main/src/governance/adr/0018-adopt-vs-build.md):
prefer a maintained upstream, verify the licence is compatible with
GPL-3.0-or-later, and wrap it behind the policy engine rather than calling it
directly.

## Adding a skill

1. Confirm the tool exists. Run the server and call it.
2. Add the skill directory with `SKILL.md`.
3. Name the exact tool calls in the body. Do not describe a capability
   abstractly.
4. State the failure mode and the irreversible step, if any.
5. Run `pytest tests/test_skills_spec.py`.

A skill that cannot name a real tool does not get written.
