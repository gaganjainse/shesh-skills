---
name: audio-control
description: Control output volume, list audio devices, and switch the active sink. Use when the user asks to change the volume, mute, pick headphones or speakers, or reports that sound is coming from the wrong device.
license: GPL-3.0-or-later
---

# Audio control

## Tools

| Task | Call |
|---|---|
| List sinks | `shesh-media-mcp` → `list_sinks` |
| Read volume | `shesh-media-mcp` → `get_volume` |
| Set volume | `shesh-media-mcp` → `set_volume(level)` |

Volume is a percentage from 0 to 100.

## Procedure

1. For a relative change ("turn it up"), read the volume first, then set it.
2. For a device change, list sinks and match the user's words to a description,
   not an index. Indices change between reboots.
3. Confirm the resulting level.

## Rules

- Cap at 100 unless the user explicitly asks to overdrive.
- A large jump can be painful on headphones. Change in steps of 10 or less
  unless the user names a level.
- Muting is volume 0; remember the previous level so it can be restored.
