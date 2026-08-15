---
name: system-health
description: Report overall machine state: load, memory, disk, temperature, and failed services. Use when the machine feels slow, something is wrong but unclear, or the user asks for a status check.
license: GPL-3.0-or-later
---

# System health

## Tools

| Task | Call |
|---|---|
| Summary | `shesh-system-mcp` → `system_health` |
| Status detail | `shesh-system-mcp` → `get_system_status` |
| Metrics | `shesh-ebpf-mcp` → `get_system_metrics` |
| Processes | `shesh-ebpf-mcp` → `list_processes` |
| Network | `shesh-ebpf-mcp` → `get_network_stats` |

## Procedure

1. Take the summary first.
2. Investigate only what looks abnormal. Do not dump every metric.
3. Lead with the finding, then the evidence.

## Reporting

- Give measured numbers with units.
- Name the specific process or service responsible.
- If everything is normal, say so in one line.

## Rules

- Never kill a process or restart a service from this skill. Report and propose.
- Distinguish "high but expected under this load" from "abnormal".
