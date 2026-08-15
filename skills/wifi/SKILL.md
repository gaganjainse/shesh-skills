---
name: wifi
description: Inspect and change network connections, including Wi-Fi and airplane mode. Use when the user asks about the network, wants to join a Wi-Fi network, reports no connectivity, or wants to go offline.
license: GPL-3.0-or-later
---

# Networking

## Tools

| Task | Call |
|---|---|
| Device states | `shesh-desktop-ctl-mcp` → `network_status` |
| Scan | `shesh-desktop-ctl-mcp` → `wifi_list` |
| Join | `shesh-desktop-ctl-mcp` → `wifi_connect(ssid, password)` |
| All networking on or off | `shesh-desktop-ctl-mcp` → `network_set_enabled(on)` |

## Procedure

1. For a connectivity complaint, read `network_status` first. The device may be
   connected while something further out is broken.
2. Scan before joining. Report signal strength; a weak network will disappoint.
3. Prefer a saved profile: call `wifi_connect` without a password and let
   NetworkManager use the stored credential.

## Rules

- **A password passed to `wifi_connect` appears in the process table.** Ask
  whether a saved profile exists first. If a password is unavoidable, resolve it
  through `shesh-secrets` rather than taking it in conversation.
- Never print a network password back to the user.
- Disabling networking drops running downloads, calls, and sync. Confirm first.
- Joining an open network is a privacy decision, not a convenience. Say so once.
