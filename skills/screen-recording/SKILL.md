---
name: screen-recording
description: Start and stop screen recording. Use when the user asks to record the screen, capture a demo, film a bug reproduction, or stop a recording already running.
license: GPL-3.0-or-later
---

# Screen recording

## Tools

| Task | Call |
|---|---|
| Start | `shesh-media-mcp` → `start_recording` |
| Stop | `shesh-media-mcp` → `stop_recording` |

## Procedure

1. Before starting, confirm what is on screen. A recording captures
   notifications, message previews, and open credentials.
2. Start, and state clearly that recording is active.
3. On stop, report the output path and duration.

## Rules

- Never start a recording implicitly as part of another task.
- If a recording is already running, say so instead of starting a second one.
- Recording is disk-intensive. On low disk space, warn before starting.
- Do not switch GPU mode or power profile while recording.
