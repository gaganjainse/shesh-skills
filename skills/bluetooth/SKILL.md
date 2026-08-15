---
name: bluetooth
description: Pair, connect, disconnect, and list Bluetooth devices. Use when the user asks about headphones, a speaker, a keyboard, or any wireless device, or reports that audio is not reaching the right place.
license: GPL-3.0-or-later
---

# Bluetooth

## Tools

| Task | Call |
|---|---|
| Adapter state | `shesh-desktop-ctl-mcp` → `bluetooth_status` |
| Power on or off | `shesh-desktop-ctl-mcp` → `bluetooth_power(on)` |
| List devices | `shesh-desktop-ctl-mcp` → `bluetooth_devices(paired_only)` |
| Connect | `shesh-desktop-ctl-mcp` → `bluetooth_connect(mac)` |
| Disconnect | `shesh-desktop-ctl-mcp` → `bluetooth_disconnect(mac)` |

## Procedure

1. Check the adapter is powered before anything else. Most failures are that.
2. List devices and match the user's words to a device name, never a position
   in the list.
3. Connect by MAC address, and report the name back so the user can confirm it
   was the right device.

## Rules

- Connecting headphones moves audio output. If media is playing, say so.
- Never power the adapter off while a device is connected without saying which
  device will drop.
- If the device is not in the paired list, it must be paired first, which
  requires physical interaction. Say so rather than retrying.
