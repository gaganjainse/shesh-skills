---
name: thermal-check
description: Report CPU and GPU temperature, fan behaviour, and thermal throttling. Use when the machine feels hot, the fans are loud, performance has dropped unexpectedly, or the user asks whether the system is throttling.
license: GPL-3.0-or-later
---

# Thermal check

## Tools

| Task | Call |
|---|---|
| Temperatures and load | `shesh-ebpf-mcp` → `get_system_metrics` |
| Overall health | `shesh-system-mcp` → `system_health` |
| Heaviest processes | `shesh-ebpf-mcp` → `list_processes` |
| Current profile | `shesh-system-mcp` → `get_power_profile` |

## Procedure

1. Read metrics and health.
2. Identify the top processes by CPU and GPU.
3. Report temperature, the load causing it, and whether throttling is occurring.
4. Offer a remedy: switch profile, close a process, or wait.

## Interpreting

| Reading | Meaning |
|---|---|
| Sustained high CPU temperature under load | Expected while compiling |
| High temperature at idle | A runaway process; find it before changing profile |
| Clock speed far below base under load | Thermal throttling |

## Rules

- Never kill a process to reduce temperature without asking.
- Report measured values, not reassurance.
