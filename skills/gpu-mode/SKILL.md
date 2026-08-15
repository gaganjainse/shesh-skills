---
name: gpu-mode
description: Inspect and switch the hybrid graphics MUX between integrated and discrete mode. Use when the user asks about the GPU, wants longer battery life, needs maximum graphics performance, or asks why an external display is not working.
license: GPL-3.0-or-later
---

# GPU mode

Switching the MUX requires a reboot. Never reboot without explicit confirmation.

## Tools

| Task | Call |
|---|---|
| Current MUX state | `shesh-system-mcp` → `mux_status` |
| Switch mode | `shesh-system-mcp` → `switch_gpu_mode(mode)` |
| GPU load and temperature | `shesh-ebpf-mcp` → `get_system_metrics` |

## Modes

| Mode | Effect |
|---|---|
| `integrated` | Discrete GPU powered down; longest battery life |
| `hybrid` | Discrete GPU on demand; default |
| `discrete` | All output through the discrete GPU; required by some external displays |

## Procedure

1. Read `mux_status`.
2. If already in the requested mode, say so and stop.
3. State that the change requires a reboot and ask for confirmation.
4. Only after the user confirms, call `switch_gpu_mode`.
5. Tell the user to reboot. Do not reboot for them.

## Rules

- Never switch the MUX during a screen recording or a running build.
- Video memory on the reference machine is limited. If two models are resident,
  warn before adding graphics load.
