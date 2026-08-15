---
name: process-inspect
description: Find what is consuming CPU, memory, disk, or network. Use when the machine is slow, a fan is loud, the network is saturated, or the user asks what is running.
license: GPL-3.0-or-later
---

# Process inspection

## Tools

| Task | Call |
|---|---|
| Process list | `shesh-ebpf-mcp` → `list_processes` |
| Per-process I/O | `shesh-ebpf-mcp` → `get_process_io` |
| Network | `shesh-ebpf-mcp` → `get_network_stats` |
| System metrics | `shesh-ebpf-mcp` → `get_system_metrics` |

## Procedure

1. Identify the resource under pressure before listing processes.
2. Report the top consumers with measured figures.
3. Explain what each is, where recognisable.

## Rules

- Never terminate a process from this skill.
- Do not describe a process as malicious without evidence. Unfamiliar is not
  the same as hostile.
- Browsers and language servers legitimately use large amounts of memory.
